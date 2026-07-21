import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, importlib
# Ensure numpy is installed in the verifier environment
try:
    importlib.import_module('numpy')
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
import numpy as np
import csv


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
    import json
    with open('/tests/grading_spec.json') as f:
        spec = json.load(f)
    steps = spec['steps']
    gold_m035 = next(s['gold_m035'] for s in steps if s['output_file'] == 'magnetization_curves.csv')
    gold_m030 = next(s['gold_m030'] for s in steps if s['output_file'] == 'magnetization_curves.csv')
    gold_phase = next(s['gold_phase'] for s in steps if s['output_file'] == 'phase_diagram.csv')
    tol_U_match = next(s['tolerance_U_match'] for s in steps if s['output_file'] == 'magnetization_curves.csv')
    tol_delta = next(s['tolerance_abs'] for s in steps if s['output_file'] == 'magnetization_curves.csv')
    tol_J_match = next(s['tolerance_JoverU_match'] for s in steps if s['output_file'] == 'phase_diagram.csv')
    tol_Uc = next(s['tolerance_abs_Uc'] for s in steps if s['output_file'] == 'phase_diagram.csv')
    return {
        'gold_m035': gold_m035,
        'gold_m030': gold_m030,
        'gold_phase': gold_phase,
        'tol_U_match': tol_U_match,
        'tol_delta': tol_delta,
        'tol_J_match': tol_J_match,
        'tol_Uc': tol_Uc
    }


# === block: score_0 (check id='step_03_magnetization_curves') ===
def score_0(artifact, step, ctx):
    rows = artifact
    col_U = 'U'
    col_m035 = 'delta_G_m0.35'
    col_m030 = 'delta_G_m0.30'

    def extract_numeric(rows, col):
        arr = []
        for r in rows:
            try:
                arr.append(float(r[col]))
            except (ValueError, KeyError):
                arr.append(np.nan)
        return np.array(arr)

    U_agent = extract_numeric(rows, col_U)
    d035_agent = extract_numeric(rows, col_m035)
    d030_agent = extract_numeric(rows, col_m030)

    if len(U_agent) == 0 or np.all(np.isnan(U_agent)):
        return 0.0

    def score_curve(gold_points, U_agent, delta_agent, tol_U, tol_delta):
        matched = 0
        for U_g, d_g in gold_points:
            diff = np.abs(U_agent - U_g)
            idx = np.nanargmin(diff)
            if diff[idx] <= tol_U and np.isfinite(delta_agent[idx]):
                if abs(delta_agent[idx] - d_g) <= tol_delta:
                    matched += 1
        return matched / len(gold_points) if gold_points else 1.0

    gold_m035 = ctx['gold_m035']
    gold_m030 = ctx['gold_m030']
    tol_U = ctx['tol_U_match']
    tol_delta = ctx['tol_delta']
    score_035 = score_curve(gold_m035, U_agent, d035_agent, tol_U, tol_delta)
    score_030 = score_curve(gold_m030, U_agent, d030_agent, tol_U, tol_delta)
    # Average of the two fillings
    return (score_035 + score_030) / 2.0


# === block: score_1 (check id='step_04_phase_diagram') ===
def score_1(artifact, step, ctx):
    rows = artifact
    def extract_numeric(rows, col):
        arr = []
        for r in rows:
            try:
                arr.append(float(r[col]))
            except (ValueError, KeyError):
                arr.append(np.nan)
        return np.array(arr)

    J_over_U_agent = extract_numeric(rows, 'J_over_U')
    Uc_agent = extract_numeric(rows, 'U_c')

    if len(J_over_U_agent) == 0 or np.all(np.isnan(J_over_U_agent)):
        return 0.0

    gold_phase = ctx['gold_phase']
    tol_J = ctx['tol_J_match']
    tol_Uc = ctx['tol_Uc']

    matched = 0
    for J_g, Uc_g in gold_phase:
        diff = np.abs(J_over_U_agent - J_g)
        idx = np.nanargmin(diff)
        if diff[idx] <= tol_J and np.isfinite(Uc_agent[idx]):
            if abs(Uc_agent[idx] - Uc_g) <= tol_Uc:
                matched += 1
    return matched / len(gold_phase) if gold_phase else 1.0


_SCORERS = {
    'step_03_magnetization_curves': score_0,
    'step_04_phase_diagram': score_1,
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
