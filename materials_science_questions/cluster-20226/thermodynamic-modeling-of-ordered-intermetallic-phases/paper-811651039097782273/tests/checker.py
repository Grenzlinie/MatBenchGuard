import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy", "scipy"])
import numpy as np
from scipy.optimize import minimize
import math
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
        coeff_path = os.path.join(outputs_dir, "configurational_coefficients.json")
        if not os.path.exists(coeff_path):
            return {"eps1": None, "eps2": None, "eps3": None}
        with open(coeff_path) as f:
            data = json.load(f)
        return {
            "eps1": data.get("epsilon1", None),
            "eps2": data.get("epsilon2", None),
            "eps3": data.get("epsilon3", None),
        }


# === block: score_0 (check id='step_epsilon') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        fields = step.get("fields", {})
        total = 0
        for key, info in fields.items():
            val = artifact.get(key, None)
            if val is None:
                continue
            target = info["target"]
            tol = info["tolerance_abs"]
            if abs(val - target) <= tol:
                total += 1
        if len(fields) == 0:
            return 0.0
        return total / len(fields)


# === block: score_1 (check id='step_tc') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        eps1 = ctx.get("eps1")
        eps2 = ctx.get("eps2")
        eps3 = ctx.get("eps3")
        if eps1 is None or eps2 is None or eps3 is None:
            return 0.0
        rows = artifact
        if not isinstance(rows, list) or len(rows) < step.get("min_rows", 4):
            return 0.0
        try:
            rows_sorted = sorted(rows, key=lambda r: float(r["Co_concentration"]))
            x = np.array([float(r["Co_concentration"]) for r in rows_sorted])
            y_agent = np.array([float(r["Tc"]) for r in rows_sorted])
        except (KeyError, ValueError, TypeError):
            return 0.0
        if len(x) < 2 or (np.diff(x) <= 0).any():
            return 0.0

        def compute_Tc(y):
            kB = 8.617333262145e-5
            C_Ni = 0.5 - y
            C_Ti = 0.5
            C_Co = y
            def delta_E(eta):
                e1, e2 = eta
                return C_Ni*C_Ni * eps1 * e1*e1 + C_Co*C_Co * eps2 * e2*e2 + 2 * C_Ni * C_Co * eps3 * e1 * e2
            def entropy_P(eta):
                e1, e2 = eta
                Pa_Ni = C_Ni * (1 + e1)
                Pa_Ti = 1.0 - Pa_Ni - C_Co * (1 + e2)
                Pa_Co = C_Co * (1 + e2)
                Pb_Ni = C_Ni * (1 - e1)
                Pb_Ti = 1.0 - Pb_Ni - C_Co * (1 - e2)
                Pb_Co = C_Co * (1 - e2)
                S = 0.0
                for p in [Pa_Ni, Pa_Ti, Pa_Co, Pb_Ni, Pb_Ti, Pb_Co]:
                    if p > 0:
                        S += p * math.log(p)
                return -kB / 2.0 * S
            S0 = entropy_P([0.0, 0.0])
            def Delta_F(eta, T):
                return delta_E(eta) + T * (entropy_P(eta) - S0)
            T_low, T_high = 1.0, 12000.0
            try:
                res_low = minimize(lambda e: Delta_F(e, T_low), [0.9, 0.9], bounds=[(0,1),(0,1)], method='L-BFGS-B', options={'maxiter': 1000})
                if res_low.fun >= -1e-8 or max(res_low.x) < 1e-3:
                    return None
                for _ in range(60):
                    T_mid = (T_low + T_high) / 2.0
                    res = minimize(lambda e: Delta_F(e, T_mid), [0.9, 0.9], bounds=[(0,1),(0,1)], method='L-BFGS-B', options={'maxiter': 1000})
                    if res.fun < -1e-8 and max(res.x) > 1e-3:
                        T_low = T_mid
                    else:
                        T_high = T_mid
                    if T_high - T_low < 1e-3:
                        break
                return (T_low + T_high) / 2.0
            except Exception:
                return None

        y_recomp = np.array([compute_Tc(xi) for xi in x])
        if None in y_recomp:
            return 0.0
        y_recomp = y_recomp.astype(float)

        # 1. Self-consistency
        tol_abs = step.get("tc_tolerance_abs", 10.0)
        diff = np.abs(y_agent - y_recomp)
        row_ok = (diff <= tol_abs).astype(float)
        consistency_score = float(np.mean(row_ok))

        # 2. Monotonic increase
        monotonic = bool(np.all(np.diff(y_agent) > 0))

        # 3. Slope check
        slope_target = step.get("slope_target", 200.0)
        slope_tol = step.get("slope_tolerance", 50.0)
        coeffs = np.polyfit(x, y_agent, 1)
        slope = coeffs[0]
        slope_dev = abs(slope - slope_target)
        slope_score = 1.0 if slope_dev <= slope_tol else max(0.0, 1.0 - (slope_dev - slope_tol) / (2 * slope_tol))

        return 0.1 * float(monotonic) + 0.6 * consistency_score + 0.3 * slope_score


_SCORERS = {
    'step_epsilon': score_0,
    'step_tc': score_1,
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
