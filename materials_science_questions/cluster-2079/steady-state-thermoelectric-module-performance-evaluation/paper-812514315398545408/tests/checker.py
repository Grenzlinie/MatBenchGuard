import os
import json
import csv

# === author imports / helpers ===
import json
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
    gold_map = {
        "step_01_coupling": {"V_CP": 29.3, "I_CP": 1.55, "T1_CP": 287.0, "T2_CP": 315.0, "eta": 0.139},
        "step_02_optimal": {"eta_opt": 0.144, "beta_opt": 0.00121, "N_opt": 5, "V_opt": 28.1, "I_opt": 1.75},
        "step_03_maximum": {"eta_max": 0.20, "G_eta": 18.1}
    }
    tol_map = {
        "step_01_coupling": {"V_CP": 0.5, "I_CP": 0.05, "T1_CP": 3.0, "T2_CP": 3.0, "eta": 0.005},
        "step_02_optimal": {"eta_opt": 0.005, "beta_opt": 0.0001, "N_opt": 0, "V_opt": 0.5, "I_opt": 0.05},
        "step_03_maximum": {"eta_max": 0.005, "G_eta": 2.0}
    }
    return {"gold": gold_map, "tolerances": tol_map}


# === block: score_0 (check id='step_01_coupling') ===
def score_0(artifact, step, ctx):
    import json
    import os
    outputs_dir = os.environ.get('OUTPUTS_DIR', '/app/outputs')
    artifact_path = os.path.join(outputs_dir, 'step_01_coupling.json')
    if not os.path.exists(artifact_path):
        return 0.0
    with open(artifact_path) as f:
        vals = json.load(f)
    step_id = 'step_01_coupling'
    gold = ctx['gold'][step_id]
    tols = ctx['tolerances'][step_id]
    subs = []
    for key in gold:
        target = gold[key]
        tol = tols[key]
        if key in ('eta',):  # higher is better
            if vals.get(key) is not None and vals[key] >= target - tol:
                subs.append(1.0)
            else:
                subs.append(0.0)
        else:
            if abs(vals.get(key, float('inf')) - target) <= tol:
                subs.append(1.0)
            else:
                subs.append(0.0)
    return sum(subs) / len(subs) if subs else 0.0


# === block: score_1 (check id='step_02_optimal') ===
def score_1(artifact, step, ctx):
    import json
    import os
    outputs_dir = os.environ.get('OUTPUTS_DIR', '/app/outputs')
    # structural check: eta_opt > eta
    paths = {
        'coupling': os.path.join(outputs_dir, 'step_01_coupling.json'),
        'optimal': os.path.join(outputs_dir, 'step_02_optimal.json')
    }
    if not os.path.exists(paths['coupling']) or not os.path.exists(paths['optimal']):
        return 0.0
    with open(paths['coupling']) as f:
        coupling = json.load(f)
    with open(paths['optimal']) as f:
        optimal = json.load(f)
    if coupling.get('eta') is None or optimal.get('eta_opt') is None:
        return 0.0
    if optimal['eta_opt'] <= coupling['eta']:
        return 0.0
    step_id = 'step_02_optimal'
    gold = ctx['gold'][step_id]
    tols = ctx['tolerances'][step_id]
    subs = []
    for key in gold:
        target = gold[key]
        tol = tols[key]
        if key in ('eta_opt',):
            if optimal.get(key) is not None and optimal[key] >= target - tol:
                subs.append(1.0)
            else:
                subs.append(0.0)
        else:
            if key == 'N_opt':
                # exact integer
                if optimal.get(key) == target:
                    subs.append(1.0)
                else:
                    subs.append(0.0)
            else:
                if abs(optimal.get(key, float('inf')) - target) <= tol:
                    subs.append(1.0)
                else:
                    subs.append(0.0)
    return sum(subs) / len(subs) if subs else 0.0


# === block: score_2 (check id='step_03_maximum') ===
def score_2(artifact, step, ctx):
    import json
    import os
    outputs_dir = os.environ.get('OUTPUTS_DIR', '/app/outputs')
    paths = {
        'optimal': os.path.join(outputs_dir, 'step_02_optimal.json'),
        'maximum': os.path.join(outputs_dir, 'step_03_maximum.json')
    }
    if not os.path.exists(paths['optimal']) or not os.path.exists(paths['maximum']):
        return 0.0
    with open(paths['optimal']) as f:
        optimal = json.load(f)
    with open(paths['maximum']) as f:
        maximum = json.load(f)
    if optimal.get('eta_opt') is None or maximum.get('eta_max') is None:
        return 0.0
    if maximum['eta_max'] < optimal['eta_opt']:
        return 0.0
    step_id = 'step_03_maximum'
    gold = ctx['gold'][step_id]
    tols = ctx['tolerances'][step_id]
    subs = []
    for key in gold:
        target = gold[key]
        tol = tols[key]
        if key in ('eta_max',):
            if maximum.get(key) is not None and maximum[key] >= target - tol:
                subs.append(1.0)
            else:
                subs.append(0.0)
        else:
            if abs(maximum.get(key, float('inf')) - target) <= tol:
                subs.append(1.0)
            else:
                subs.append(0.0)
    return sum(subs) / len(subs) if subs else 0.0


_SCORERS = {
    'step_01_coupling': score_0,
    'step_02_optimal': score_1,
    'step_03_maximum': score_2,
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
