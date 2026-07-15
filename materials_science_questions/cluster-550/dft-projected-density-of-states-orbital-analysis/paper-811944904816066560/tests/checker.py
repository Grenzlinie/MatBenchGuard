import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
    def prepare(outputs_dir, spec):
        ctx = {}
        die_path = os.path.join(outputs_dir, 'dielectric_function.csv')
        data = []
        if os.path.exists(die_path):
            with open(die_path, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 3:
                        continue
                    try:
                        e = float(row[0])
                        eps2 = float(row[2])
                        data.append((e, eps2))
                    except ValueError:
                        continue
        data.sort(key=lambda x: x[0])
        ctx['dielectric_data'] = data
        return ctx


# === block: score_0 (check id='step_lattice') ===
def score_0(artifact, step, ctx):
    content = artifact.strip() if isinstance(artifact, str) else ""
    try:
        value = float(content)
    except:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance_rel', 0.02)
    if value == 0:
        return 0.0
    rel_err = abs(value - target) / abs(target)
    return 1.0 if rel_err <= tol else 0.0


# === block: score_1 (check id='step_elastic_constants') ===
def score_1(artifact, step, ctx):
    content = artifact.strip() if isinstance(artifact, str) else ""
    try:
        parts = content.split()
        if len(parts) < 3:
            return 0.0
        C11 = float(parts[0])
        C12 = float(parts[1])
        C44 = float(parts[2])
    except:
        return 0.0
    targets = step.get('targets', [181.00667, 37.28050, 38.86243])
    tol = step.get('tolerance_rel', 0.10)
    score = 0.0
    try:
        if abs(C11 - targets[0]) / abs(targets[0]) <= tol:
            score += 0.2
    except:
        pass
    try:
        if abs(C12 - targets[1]) / abs(targets[1]) <= tol:
            score += 0.2
    except:
        pass
    try:
        if abs(C44 - targets[2]) / abs(targets[2]) <= tol:
            score += 0.2
    except:
        pass
    B0_recomp = (C11 + 2 * C12) / 3.0 if (C11 + C12) != 0 else 0
    target_B0 = step.get('derived_targets', {}).get('B0', 85.18922)
    try:
        if abs(B0_recomp - target_B0) / abs(target_B0) <= tol:
            score += 0.2
    except:
        pass
    v_recomp = C12 / (C11 + C12) if (C11 + C12) != 0 else 0
    target_v = step.get('derived_targets', {}).get('v', 0.1708)
    try:
        if abs(v_recomp - target_v) / abs(target_v) <= tol:
            score += 0.2
    except:
        pass
    return score


# === block: score_2 (check id='step_dielectric_csv') ===
def score_2(artifact, step, ctx):
    data = ctx.get('dielectric_data', [])
    if len(data) < step.get('min_rows', 50):
        return 0.0
    energies = [p[0] for p in data]
    if any(energies[i] > energies[i+1] for i in range(len(energies)-1)):
        return 0.0
    emin, emax = energies[0], energies[-1]
    req_emin, req_emax = step.get('energy_range', [0.0, 40.0])
    if emin > req_emin or emax < req_emax:
        return 0.0
    return 1.0


# === block: score_3 (check id='step_peaks') ===
def score_3(artifact, step, ctx):
    data = ctx.get('dielectric_data', [])
    if not data:
        return 0.0
    peaks_config = step.get('peak_ranges', {})
    targets = step.get('target_peaks', {})
    tols = step.get('tolerance_abs', {})
    score = 0.0
    def find_peak(lo, hi):
        best_e, best_eps = None, -1e9
        for e, eps2 in data:
            if lo <= e <= hi and eps2 > best_eps:
                best_eps = eps2
                best_e = e
        return best_e
    for key, rng in peaks_config.items():
        peak_e = find_peak(rng[0], rng[1])
        if peak_e is None:
            continue
        target = targets.get(key)
        tol = tols.get(key, 2.0)
        if target is not None and abs(peak_e - target) <= tol:
            score += 0.5
    return score


_SCORERS = {
    'step_lattice': score_0,
    'step_elastic_constants': score_1,
    'step_dielectric_csv': score_2,
    'step_peaks': score_3,
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
