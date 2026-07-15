import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    elastic_steps = [s for s in spec['steps'] if s['id'] == 'elastic_constants_0GPa']
    derived_steps = [s for s in spec['steps'] if s['id'] == 'derived_properties_0GPa']
    elastic_targets = elastic_steps[0]['targets'] if elastic_steps else {}
    elastic_tols = elastic_steps[0]['tolerances'] if elastic_steps else {}
    derived_targets = derived_steps[0]['targets'] if derived_steps else {}
    derived_tols = derived_steps[0]['tolerances'] if derived_steps else {}
    return {
        'elastic_targets': elastic_targets,
        'elastic_tols': elastic_tols,
        'derived_targets': derived_targets,
        'derived_tols': derived_tols,
    }


# === block: score_0 (check id='elastic_constants_0GPa') ===
def score_0(artifact, step, ctx):
    import csv
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    if not rows:
        return 0.0
    row = rows[0]
    targets = ctx['elastic_targets']
    tols = ctx['elastic_tols']
    keys = ['C11', 'C12', 'C13', 'C33', 'C44']
    subscores = []
    for k in keys:
        try:
            val = float(row[k])
        except (KeyError, ValueError):
            return 0.0
        target = targets[k]
        tol = tols[k].get('rel_tol')
        if tol is None:
            return 0.0
        if target == 0:
            return 0.0 if val != 0 else 1.0
        rel_err = abs(val - target) / abs(target)
        sub = max(0.0, 1.0 - rel_err / tol)
        subscores.append(sub)
    return sum(subscores) / len(subscores)


# === block: score_1 (check id='derived_properties_0GPa') ===
def score_1(artifact, step, ctx):
    import csv
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    if not rows:
        return 0.0
    row = rows[0]
    targets = ctx['derived_targets']
    tols = ctx['derived_tols']
    keys = ['B','E','G','v','Vp','Vs','zeta','A']
    subscores = []
    for k in keys:
        try:
            val = float(row[k])
        except (KeyError, ValueError):
            return 0.0
        target = targets[k]
        tol = tols[k].get('rel_tol')
        abs_tol = tols[k].get('abs_tol')
        if tol is not None:
            if target == 0:
                sub = 1.0 if val == 0 else 0.0
            else:
                rel_err = abs(val - target) / abs(target)
                sub = max(0.0, 1.0 - rel_err / tol)
        elif abs_tol is not None:
            sub = max(0.0, 1.0 - abs(val - target) / abs_tol) if abs_tol > 0 else (1.0 if val == target else 0.0)
        else:
            sub = 1.0
        subscores.append(sub)
    return sum(subscores) / len(subscores)


# === block: score_2 (check id='pressure_dependence') ===
def score_2(artifact, step, ctx):
    import csv
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    rows = []
    expected_pressures = [0, 100, 200, 300, 400, 500]
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    except Exception:
        return 0.0
    if len(rows) != len(expected_pressures):
        return 0.0
    try:
        rows.sort(key=lambda r: float(r['pressure_GPa']))
    except (KeyError, ValueError):
        return 0.0
    pressures = [float(r['pressure_GPa']) for r in rows]
    if pressures != expected_pressures:
        return 0.0

    # Monotonicity check for Cij columns
    cij_keys = ['C11','C12','C13','C33','C44']
    mono_violations = 0
    total_pairs = 0
    for k in cij_keys:
        vals = []
        for r in rows:
            try:
                vals.append(float(r[k]))
            except (KeyError, ValueError):
                return 0.0
        for i in range(1, len(vals)):
            total_pairs += 1
            if vals[i] < vals[i-1] * 0.99:  # allow 1% noise
                mono_violations += 1
    mono_score = 1.0 if total_pairs == 0 else max(0.0, 1.0 - mono_violations / total_pairs)

    # Born stability conditions
    born_ok = 0
    for r in rows:
        try:
            c11 = float(r['C11'])
            c12 = float(r['C12'])
            c13 = float(r['C13'])
            c33 = float(r['C33'])
            c44 = float(r['C44'])
        except (KeyError, ValueError):
            return 0.0
        cond1 = c44 > 0
        cond2 = c11 > c12
        cond3 = (c11 + 2*c12) * c33 - 2 * c13 * c13 > 0
        if cond1 and cond2 and cond3:
            born_ok += 1
    born_score = born_ok / len(rows)

    # Consistency with elastic_constants_0GPa.csv
    ref_path = os.path.join('/app/outputs', 'elastic_constants_0GPa.csv')
    consistency_score = 0.0
    if os.path.exists(ref_path):
        ref_rows = []
        with open(ref_path, newline='') as f:
            ref_reader = csv.DictReader(f)
            for rr in ref_reader:
                ref_rows.append(rr)
        if ref_rows:
            ref = ref_rows[0]
            row0 = rows[0]
            ref_cij = {}
            row0_cij = {}
            for k in cij_keys:
                try:
                    ref_cij[k] = float(ref[k])
                    row0_cij[k] = float(row0[k])
                except:
                    break
            else:
                diffs = []
                for k in cij_keys:
                    if ref_cij[k] == 0:
                        diffs.append(0.0 if row0_cij[k] == 0 else 1.0)
                    else:
                        diffs.append(abs(row0_cij[k] - ref_cij[k]) / abs(ref_cij[k]))
                max_diff = max(diffs)
                consistency_score = max(0.0, 1.0 - max_diff / 0.02)  # 2% tolerance

    return 0.5 * mono_score + 0.3 * born_score + 0.2 * consistency_score


_SCORERS = {
    'elastic_constants_0GPa': score_0,
    'derived_properties_0GPa': score_1,
    'pressure_dependence': score_2,
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
