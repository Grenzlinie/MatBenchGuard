import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    refs = {}
    for s in spec.get('steps', []):
        cfg = s.get('config', {})
        if cfg:
            refs[s['id']] = cfg
    return refs


# === block: score_0 (check id='static_results_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 1:
        return 0.0

    cfg = step.get('config', {})
    expected_systems = set(cfg.get('expected_systems', ['Cu8','Cu13','Cu20','Cu38','Cu55','Cu(100)']))
    ref_coh_cluster = float(cfg.get('ref_coh_cluster', 0.70))
    ref_coh_cu100 = float(cfg.get('ref_coh_cu100', 0.76))
    ref_barrier_cluster = float(cfg.get('ref_barrier_cluster', 0.73))
    ref_barrier_cu100 = float(cfg.get('ref_barrier_cu100', 0.77))
    tol = float(cfg.get('tol_abs', 0.10))

    systems_data = {}
    found_systems = set()
    all_fields_ok = True
    for entry in artifact:
        if not isinstance(entry, dict):
            all_fields_ok = False
            continue
        sys = str(entry.get('system', ''))
        if sys in expected_systems:
            found_systems.add(sys)
            systems_data[sys] = entry

    n_found = len(found_systems)
    if n_found == 0:
        return 0.0

    required_keys = ['free_energy_COOH', 'free_energy_COH', 'barrier_CC', 'unit']
    schema_ok = True
    for sys in found_systems:
        entry = systems_data[sys]
        if not all(k in entry for k in required_keys):
            schema_ok = False
            break

    schema_score = 0.1 if schema_ok else 0.0

    coh_hits = 0
    for sys in found_systems:
        try:
            val = float(systems_data[sys].get('free_energy_COH', float('nan')))
        except (ValueError, TypeError):
            continue
        ref = ref_coh_cu100 if sys == 'Cu(100)' else ref_coh_cluster
        if abs(val - ref) <= tol:
            coh_hits += 1
    coh_score = 0.4 * (coh_hits / max(1, n_found))

    barrier_hits = 0
    for sys in found_systems:
        try:
            val = float(systems_data[sys].get('barrier_CC', float('nan')))
        except (ValueError, TypeError):
            continue
        ref = ref_barrier_cu100 if sys == 'Cu(100)' else ref_barrier_cluster
        if abs(val - ref) <= tol:
            barrier_hits += 1
    barrier_score = 0.3 * (barrier_hits / max(1, n_found))

    cluster_vals = []
    cu100_val = None
    for sys in found_systems:
        try:
            val = float(systems_data[sys].get('free_energy_COOH', float('nan')))
        except (ValueError, TypeError):
            continue
        if sys == 'Cu(100)':
            cu100_val = val
        else:
            cluster_vals.append(val)

    trend_score = 0.0
    if cu100_val is not None and len(cluster_vals) > 0:
        avg_cluster = sum(cluster_vals) / len(cluster_vals)
        diff = cu100_val - avg_cluster
        if diff > 0.05:
            trend_score = 0.2
        elif diff > 0.01:
            trend_score = 0.1
        elif diff > -0.02:
            trend_score = 0.05

    return min(1.0, schema_score + coh_score + barrier_score + trend_score)


# === block: score_1 (check id='roughness_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    cfg = step.get('config', {})
    min_rows = int(cfg.get('min_rows', 500))
    min_span = float(cfg.get('min_time_span_ps', 4.5))
    min_std = float(cfg.get('min_roughness_std', 0.1))

    row0 = artifact[0]
    if not isinstance(row0, dict):
        return 0.0

    has_time = 'time_ps' in row0
    has_roughness = 'roughness_au' in row0
    if not has_time or not has_roughness:
        return 0.0
    col_score = 0.15

    row_count = len(artifact)
    if row_count >= min_rows:
        row_score = 0.25
    elif row_count >= min_rows * 0.5:
        row_score = 0.25 * (row_count / min_rows)
    else:
        row_score = 0.0

    times = []
    roughness_vals = []
    for row in artifact:
        try:
            t = float(row['time_ps'])
            r = float(row['roughness_au'])
            times.append(t)
            roughness_vals.append(r)
        except (ValueError, TypeError):
            pass

    if len(times) >= 2:
        monotonic = all(times[i] < times[i+1] for i in range(len(times)-1))
        span = times[-1] - times[0]
        if monotonic and span >= min_span:
            time_score = 0.3
        elif monotonic and span >= min_span * 0.5:
            time_score = 0.15
        elif span >= min_span:
            time_score = 0.1
        else:
            time_score = 0.0
    else:
        time_score = 0.0

    if len(roughness_vals) >= 10:
        mean_r = sum(roughness_vals) / len(roughness_vals)
        variance = sum((r - mean_r)**2 for r in roughness_vals) / len(roughness_vals)
        std_r = math.sqrt(variance)
        if std_r >= min_std:
            roughness_score = 0.3
        elif std_r >= min_std * 0.5:
            roughness_score = 0.15
        else:
            roughness_score = 0.05
    else:
        roughness_score = 0.0

    return min(1.0, col_score + row_score + time_score + roughness_score)


# === block: score_2 (check id='barrier_rough_check') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0

    has_barrier = 'barrier' in artifact
    has_unit = 'unit' in artifact
    if not has_barrier or not has_unit:
        return 0.0

    schema_score = 0.1

    cfg = step.get('config', {})
    threshold = float(cfg.get('threshold', 0.55))

    try:
        barrier_val = float(artifact['barrier'])
    except (ValueError, TypeError):
        return schema_score

    if barrier_val <= 0.0:
        barrier_score = 0.9
    elif barrier_val <= threshold:
        barrier_score = 0.9
    elif barrier_val <= threshold + 0.08:
        barrier_score = 0.6
    elif barrier_val <= threshold + 0.15:
        barrier_score = 0.3
    else:
        barrier_score = 0.0

    return min(1.0, schema_score + barrier_score)


_SCORERS = {
    'static_results_check': score_0,
    'roughness_check': score_1,
    'barrier_rough_check': score_2,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
