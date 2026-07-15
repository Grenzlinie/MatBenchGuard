import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys

def _ensure_package(pkg_name, import_name=None):
    if import_name is None:
        import_name = pkg_name
    try:
        __import__(import_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", pkg_name])

_ensure_package("numpy")
_ensure_package("scipy")

import numpy as np
from scipy.optimize import minimize_scalar

def compute_CuMnPt6_order(T, A_k, WCuMn_k):
    def f(S1, S3):
        if 1+3*S1+4*S3 <= 0 or 1+3*S1-4*S3 <= 0 or 1-S1 <= 0 or 3+S1 <= 0:
            return 1e10
        U_k = (3/32)*(A_k * S1*S1 + 4 * WCuMn_k * S3*S3)
        phi_k = -( ( (1+3*S1+4*S3)*np.log(1+3*S1+4*S3) + (1+3*S1-4*S3)*np.log(1+3*S1-4*S3) + 12*(1-S1)*np.log(1-S1) + 6*(3+S1)*np.log(3+S1) ) / 32.0 )
        return U_k - T * phi_k
    best_S1, best_S3, best_F = 0.0, 0.0, 1e100
    for S1_cand in np.linspace(0, 0.999, 200):
        s3_upper = (1+3*S1_cand)/4
        if s3_upper < 0:
            continue
        res = minimize_scalar(lambda s3: f(S1_cand, s3), bounds=(0, s3_upper), method='bounded')
        if res.success and res.fun < best_F:
            best_F = res.fun
            best_S1 = S1_cand
            best_S3 = res.x
    return best_S1, best_S3

def compute_MnPt7_order(T, V_MnPt_k, W_MnPt_k):
    def safe_xlogx(x):
        return 0.0 if x <= 0 else x * np.log(x)
    def f(S1, S3):
        P_C = 1/8.0 - S1/4.0
        if P_C < 0 or P_C > 1: return 1e10
        P_A = (0.25 + 1.5*S1 + S3)/2.0
        P_B = (0.25 + 1.5*S1 - S3)/2.0
        if P_A < 0 or P_A > 1 or P_B < 0 or P_B > 1:
            return 1e10
        U_k = (3/32) * ((4*V_MnPt_k - 6*W_MnPt_k)*S1*S1 + 4*W_MnPt_k*S3*S3)
        phi_k = -(1/32) * ( 4*(safe_xlogx(P_A) + safe_xlogx(1-P_A)) + 4*(safe_xlogx(P_B) + safe_xlogx(1-P_B)) + 24*(safe_xlogx(P_C) + safe_xlogx(1-P_C)) )
        return U_k - T * phi_k
    best_S1, best_S3, best_F = 0.0, 0.0, 1e100
    for S1_cand in np.linspace(0, 0.5, 100):
        s3_upper = min(0.25 + 1.5*S1_cand, 1.0)
        if s3_upper <= 0:
            continue
        res = minimize_scalar(lambda s3: f(S1_cand, s3), bounds=(0, s3_upper), method='bounded')
        if res.success and res.fun < best_F:
            best_F = res.fun
            best_S1 = S1_cand
            best_S3 = res.x
    return best_S1, best_S3

def find_transition_temp(T_arr, S_arr, direction, threshold=0.01):
    T = np.array(T_arr, dtype=float)
    S = np.array(S_arr, dtype=float)
    order = np.argsort(T)
    T = T[order]
    S = S[order]
    if direction == 'rise':
        idx = np.where(S > threshold)[0]
        if len(idx) == 0: return None
        first = idx[0]
        if first == 0: return T[first]
        return (T[first-1] + T[first]) / 2.0
    elif direction == 'fall':
        idx = np.where(S > threshold)[0]
        if len(idx) == 0: return None
        last = idx[-1]
        if last == len(T)-1: return None
        return (T[last] + T[last+1]) / 2.0
    return None


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
    params = {
        'CuMnPt6': {
            'A_k': -6053.0,
            'W_CuMn_k': -395.0,
            'Tc_target': 1241.0,
            'Tcl_target': 1019.0,
        },
        'MnPt7': {
            'V_MnPt_k': -1517.0,
            'W_MnPt_k': -318.0,
            'Tc_target': 1065.0,
            'Tcl_target': 941.0,
        }
    }
    return params


# === block: score_0 (check id='CuMnPt6_order_params') ===
def score_0(artifact, step, ctx):
        tol = step.get('params', {}).get('tolerance_S1_S3', 0.05)
        params = ctx['CuMnPt6']
        A_k = params['A_k']
        W_CuMn_k = params['W_CuMn_k']
        T_vals, S1_agent, S3_agent = [], [], []
        for row in artifact:
            T_vals.append(float(row['T']))
            S1_agent.append(float(row['S1']))
            S3_agent.append(float(row['S3']))
        if len(T_vals) == 0:
            return 0.0
        T_vals = np.array(T_vals)
        S1_agent = np.array(S1_agent)
        S3_agent = np.array(S3_agent)
        S1_ref = np.zeros_like(T_vals)
        S3_ref = np.zeros_like(T_vals)
        for i, T in enumerate(T_vals):
            s1, s3 = compute_CuMnPt6_order(T, A_k, W_CuMn_k)
            S1_ref[i] = s1
            S3_ref[i] = s3
        diff1 = np.abs(S1_agent - S1_ref)
        diff3 = np.abs(S3_agent - S3_ref)
        ok = (diff1 <= tol) & (diff3 <= tol)
        score = np.mean(ok)
        return float(score)


# === block: score_1 (check id='CuMnPt6_transitions') ===
def score_1(artifact, step, ctx):
        params = ctx['CuMnPt6']
        Tc_target = params['Tc_target']
        Tcl_target = params['Tcl_target']
        T_vals, S1_agent, S3_agent = [], [], []
        for row in artifact:
            T_vals.append(float(row['T']))
            S1_agent.append(float(row['S1']))
            S3_agent.append(float(row['S3']))
        if len(T_vals) == 0:
            return 0.0
        T_vals = np.array(T_vals)
        S1_agent = np.array(S1_agent)
        S3_agent = np.array(S3_agent)
        Tc_agent = find_transition_temp(T_vals, S1_agent, direction='fall', threshold=0.1)
        Tcl_agent = find_transition_temp(T_vals, S3_agent, direction='rise', threshold=0.01)
        score = 0.0
        if Tc_agent is not None:
            err = abs(Tc_agent - Tc_target) / Tc_target
            if err <= 0.05:
                score += 0.5
        if Tcl_agent is not None:
            err = abs(Tcl_agent - Tcl_target) / Tcl_target
            if err <= 0.05:
                score += 0.5
        return score


# === block: score_2 (check id='MnPt7_order_params') ===
def score_2(artifact, step, ctx):
        params = ctx['MnPt7']
        V_MnPt_k = params['V_MnPt_k']
        W_MnPt_k = params['W_MnPt_k']
        T_vals, S1_agent, S3_agent = [], [], []
        for row in artifact:
            T_vals.append(float(row['T']))
            S1_agent.append(float(row['S1']))
            S3_agent.append(float(row['S3']))
        if len(T_vals) == 0:
            return 0.0
        T_vals = np.array(T_vals)
        S1_agent = np.array(S1_agent)
        S3_agent = np.array(S3_agent)
        S1_ref = np.zeros_like(T_vals)
        S3_ref = np.zeros_like(T_vals)
        for i, T in enumerate(T_vals):
            s1, s3 = compute_MnPt7_order(T, V_MnPt_k, W_MnPt_k)
            S1_ref[i] = s1
            S3_ref[i] = s3
        diff1 = np.abs(S1_agent - S1_ref)
        diff3 = np.abs(S3_agent - S3_ref)
        ok = (diff1 <= 0.05) & (diff3 <= 0.05)
        score = np.mean(ok)
        return float(score)


# === block: score_3 (check id='MnPt7_transitions') ===
def score_3(artifact, step, ctx):
        params = ctx['MnPt7']
        Tc_target = params['Tc_target']
        Tcl_target = params['Tcl_target']
        T_vals, S1_agent, S3_agent = [], [], []
        for row in artifact:
            T_vals.append(float(row['T']))
            S1_agent.append(float(row['S1']))
            S3_agent.append(float(row['S3']))
        if len(T_vals) == 0:
            return 0.0
        T_vals = np.array(T_vals)
        S1_agent = np.array(S1_agent)
        S3_agent = np.array(S3_agent)
        Tc_agent = find_transition_temp(T_vals, S1_agent, direction='fall', threshold=0.05)
        Tcl_agent = find_transition_temp(T_vals, S3_agent, direction='rise', threshold=0.01)
        score = 0.0
        if Tc_agent is not None:
            err = abs(Tc_agent - Tc_target) / Tc_target
            if err <= 0.05:
                score += 0.5
        if Tcl_agent is not None:
            err = abs(Tcl_agent - Tcl_target) / Tcl_target
            if err <= 0.05:
                score += 0.5
        return score


_SCORERS = {
    'CuMnPt6_order_params': score_0,
    'CuMnPt6_transitions': score_1,
    'MnPt7_order_params': score_2,
    'MnPt7_transitions': score_3,
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
