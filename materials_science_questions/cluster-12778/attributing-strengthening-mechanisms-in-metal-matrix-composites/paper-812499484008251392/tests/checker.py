import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, importlib
for pkg in ("numpy", "scipy"):
    try:
        importlib.import_module(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", pkg])
import numpy as np
from scipy.optimize import minimize


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
        dm = spec["design_matrix"]
        X_list = []
        y_list = []
        for row in dm:
            A = row["A"]
            B = row["B"]
            C = row["C"]
            feats = [1.0, A, B, C, A**2, B**2, C**2, A*B, A*C, B*C]
            X_list.append(feats)
            y_list.append(row["TS"])
        X = np.array(X_list, dtype=float)
        y = np.array(y_list, dtype=float)
        coefs, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
    
        def predict(x):
            A, B, C = x
            feats = np.array([1.0, A, B, C, A**2, B**2, C**2, A*B, A*C, B*C])
            return np.dot(coefs, feats)
    
        best_val = -np.inf
        best_params = None
        for A_int in [1,2,3]:
            def obj(params):
                B, C = params
                return -predict([A_int, B, C])
            bnds = [(800, 1000), (15, 25)]
            x0 = [900, 20]
            res = minimize(obj, x0, bounds=bnds, method='L-BFGS-B')
            if res.success:
                val = -res.fun
                if val > best_val:
                    best_val = val
                    best_params = (A_int, res.x[0], res.x[1])
        return {"opt_A": best_params[0], "opt_B": best_params[1], "opt_C": best_params[2], "opt_TS": best_val, "coefs": coefs.tolist()}


# === block: score_0 (check id='check_optimum') ===
def score_0(artifact, step, ctx):
        opt_params = artifact.get("optimum_parameters", {})
        pred_ts = artifact.get("predicted_tensile_strength", None)
        if pred_ts is None:
            return 0.0
        score = 0.0
        if abs(pred_ts - ctx["opt_TS"]) <= 1.0:
            score += 0.4
        tool_passes = opt_params.get("tool_passes")
        if tool_passes == ctx["opt_A"]:
            score += 0.2
        rot = opt_params.get("rotational_speed")
        if rot is not None and abs(rot - ctx["opt_B"]) <= 10.0:
            score += 0.2
        trans = opt_params.get("transverse_speed")
        if trans is not None and abs(trans - ctx["opt_C"]) <= 1.0:
            score += 0.2
        return score


# === block: score_1 (check id='check_comparison') ===
def score_1(artifact, step, ctx):
        opt_path = "/app/outputs/optimum_parameters.json"
        if not os.path.exists(opt_path):
            return 0.0
        with open(opt_path) as f:
            opt_artifact = json.load(f)
        pred_ts_opt = opt_artifact.get("predicted_tensile_strength", None)
        pred_ts_comp = artifact.get("predicted_tensile_strength", None)
        exp_ts = artifact.get("experimental_tensile_strength", None)
        dev = artifact.get("deviation_percentage", None)
        impr = artifact.get("improvement_percentage", None)
        if None in (pred_ts_opt, pred_ts_comp, exp_ts, dev, impr):
            return 0.0
        score = 0.0
        if abs(pred_ts_comp - pred_ts_opt) < 1e-6:
            score += 0.2
        if exp_ts == 162.89:
            expected_dev = (pred_ts_opt - 162.89) / pred_ts_opt * 100.0
            if abs(dev - expected_dev) < 0.01:
                score += 0.4
            expected_impr = (162.89 - 135.0) / 135.0 * 100.0
            if abs(impr - expected_impr) < 0.01:
                score += 0.4
        return score


_SCORERS = {
    'check_optimum': score_0,
    'check_comparison': score_1,
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
