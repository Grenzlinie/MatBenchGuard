import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
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
    return {}


# === block: score_0 (check id='helicity_crossings_recompute_kt') ===
def score_0(artifact, step, ctx):
    data = artifact
    xs = [0.4, 0.9]
    gold = step['hidden_gold']
    scores = []
    for x in xs:
        rows = [row for row in data if abs(float(row['x']) - x) < 1e-6]
        if not rows:
            scores.append(0.0)
            continue
        invL = np.array([1.0/float(row['L']) for row in rows])
        T_cross = np.array([float(row['T_cross']) for row in rows])
        coeffs = np.polyfit(invL, T_cross, 2)
        T_KT = coeffs[2]
        key = 'x0_4' if x == 0.4 else 'x0_9'
        target = gold[key]['T_KT']
        tol = gold[key]['tolerance']
        diff = abs(T_KT - target)
        score = max(0.0, 1.0 - diff / tol)
        scores.append(score)
    return float(np.mean(scores))


# === block: score_1 (check id='kt_temperatures_consistency') ===
def score_1(artifact, step, ctx):
    agent = artifact
    data_path = os.path.join('/app/outputs', 'helicity_crossings.csv')
    if not os.path.exists(data_path):
        return 0.0
    with open(data_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    xs = [0.4, 0.9]
    recomputed = {}
    for x in xs:
        rows_x = [r for r in rows if abs(float(r['x']) - x) < 1e-6]
        if not rows_x:
            recomputed[x] = None
            continue
        invL = np.array([1.0/float(r['L']) for r in rows_x])
        T_cross = np.array([float(r['T_cross']) for r in rows_x])
        coeffs = np.polyfit(invL, T_cross, 2)
        recomputed[x] = coeffs[2]
    tol = step.get('consistency_tolerance', 0.02)
    scores = []
    for x in xs:
        key = 'x0_4' if x == 0.4 else 'x0_9'
        agent_val = agent.get(key, {}).get('T_KT')
        if agent_val is None or recomputed.get(x) is None:
            scores.append(0.0)
        else:
            diff = abs(agent_val - recomputed[x])
            s = max(0.0, 1.0 - diff / tol)
            scores.append(s)
    return float(np.mean(scores))


# === block: score_2 (check id='specific_heat_recompute_peak_alpha') ===
def score_2(artifact, step, ctx):
    T_arr = np.array([float(row['T']) for row in artifact])
    C_arr = np.array([float(row['C']) for row in artifact])
    i_max = np.argmax(C_arr)
    T_l = float(T_arr[i_max])
    gold = step['hidden_gold']
    target_T_l = gold['T_l']
    tol_T_l = gold['tolerance_T_l']
    diff_T = abs(T_l - target_T_l)
    score_T = max(0.0, 1.0 - diff_T / tol_T_l)
    mask = (np.abs(T_arr - T_l) > 0.001) & (np.abs(T_arr - T_l) < 0.05)
    if np.sum(mask) < 3:
        score_alpha = 0.0
    else:
        x_fit = np.log(np.abs(T_arr[mask] - T_l))
        y_fit = np.log(C_arr[mask])
        slope, _ = np.polyfit(x_fit, y_fit, 1)
        alpha = -slope
        target_alpha = gold['alpha']
        tol_alpha = gold['tolerance_alpha']
        diff_a = abs(alpha - target_alpha)
        score_alpha = max(0.0, 1.0 - diff_a / tol_alpha)
    return 0.5*score_T + 0.5*score_alpha


# === block: score_3 (check id='ising_analysis_consistency') ===
def score_3(artifact, step, ctx):
    agent = artifact
    data_path = os.path.join('/app/outputs', 'specific_heat_L36_x0.9.csv')
    if not os.path.exists(data_path):
        return 0.0
    with open(data_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    T_arr = np.array([float(r['T']) for r in rows])
    C_arr = np.array([float(r['C']) for r in rows])
    i_max = np.argmax(C_arr)
    T_l_recomputed = float(T_arr[i_max])
    mask = (np.abs(T_arr - T_l_recomputed) > 0.001) & (np.abs(T_arr - T_l_recomputed) < 0.05)
    alpha_recomputed = None
    if np.sum(mask) >= 3:
        x_fit = np.log(np.abs(T_arr[mask] - T_l_recomputed))
        y_fit = np.log(C_arr[mask])
        slope, _ = np.polyfit(x_fit, y_fit, 1)
        alpha_recomputed = -slope
    tol_T = step.get('consistency_tolerance_T_l', 0.02)
    tol_alpha = step.get('consistency_tolerance_alpha', 0.05)
    s_T = 0.0
    agent_T_l = agent.get('T_l')
    if agent_T_l is not None:
        diff = abs(agent_T_l - T_l_recomputed)
        s_T = max(0.0, 1.0 - diff / tol_T)
    s_a = 0.0
    if agent.get('alpha') is not None and alpha_recomputed is not None:
        diff = abs(agent['alpha'] - alpha_recomputed)
        s_a = max(0.0, 1.0 - diff / tol_alpha)
    return 0.5*s_T + 0.5*s_a


_SCORERS = {
    'helicity_crossings_recompute_kt': score_0,
    'kt_temperatures_consistency': score_1,
    'specific_heat_recompute_peak_alpha': score_2,
    'ising_analysis_consistency': score_3,
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
