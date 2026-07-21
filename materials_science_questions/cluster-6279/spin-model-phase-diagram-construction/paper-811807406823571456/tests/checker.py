import os
import json
import csv

# === author imports / helpers ===
import math

try:
    import numpy as np
except ImportError:
    class _FakeNumpy:
        @staticmethod
        def log(x):
            if hasattr(x, '__iter__'):
                return [math.log(v) for v in x]
            return math.log(x)

        @staticmethod
        def polyfit(x, y, deg):
            if deg != 1:
                raise NotImplementedError("Only degree 1 supported")
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_xy = sum(xi * yi for xi, yi in zip(x, y))
            sum_x2 = sum(xi * xi for xi in x)
            denom = n * sum_x2 - sum_x * sum_x
            if denom == 0:
                raise ValueError("Zero denominator in polyfit")
            slope = (n * sum_xy - sum_x * sum_y) / denom
            intercept = (sum_y - slope * sum_x) / n
            return (slope, intercept)
    np = _FakeNumpy()


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
    ctx = {'xi_cross_temp': None, 'q2_fitted_eta': {}}
    return ctx


# === block: score_0 (check id='xi_crossing') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts with keys T_div_x, L, xi_over_L, error
    points = {}
    for row in artifact:
        tx = float(row['T_div_x'])
        L = int(row['L'])
        val = float(row['xi_over_L'])
        points.setdefault(tx, []).append(val)
    tx_list = sorted(points.keys())
    if len(tx_list) < 3:
        score = 0.0
    else:
        stds = []
        for tx in tx_list:
            vals = points[tx]
            if len(vals) > 1:
                mean = sum(vals) / len(vals)
                var = sum((v-mean)**2 for v in vals) / (len(vals)-1)
                std = math.sqrt(var)
            else:
                std = 0.0
            stds.append((tx, std))
        # find tx with minimal std
        min_tx, min_std = min(stds, key=lambda x: x[1])
        T_cross = min_tx
        ctx['xi_cross_temp'] = T_cross
        target = step.get('target', 0.95)
        tol_full = step.get('tolerance_full', 0.1)
        tol_zero = step.get('tolerance_zero', 0.3)
        abs_err = abs(T_cross - target)
        if abs_err <= tol_full:
            score = 1.0
        elif abs_err >= tol_zero:
            score = 0.0
        else:
            score = 1.0 - (abs_err - tol_full) / (tol_zero - tol_full)
    return score


# === block: score_1 (check id='q2_decay') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts with T, L, N, q2, error
    target_etas = step['target_etas']
    tol_full = step.get('tolerance_full', 0.15)
    tol_zero = step.get('tolerance_zero', 0.35)
    data_by_T = {}
    for row in artifact:
        T = float(row['T'])
        N = float(row['N'])
        q2 = float(row['q2'])
        data_by_T.setdefault(T, []).append((N, q2))
    ctx['q2_fitted_eta'] = {}
    scores = []
    for target_T_str, target_eta in target_etas.items():
        target_T = float(target_T_str)
        T_keys = list(data_by_T.keys())
        if not T_keys:
            scores.append(0.0)
            continue
        closest_T = min(T_keys, key=lambda t: abs(t - target_T))
        if abs(closest_T - target_T) > 0.05:
            scores.append(0.0)
            continue
        points = data_by_T[closest_T]
        if len(points) < 3:
            scores.append(0.0)
            continue
        x = np.log([p[0] for p in points])
        y = np.log([p[1] for p in points])
        slope, intercept = np.polyfit(x, y, 1)
        p = -slope
        eta = 3 * p - 1
        ctx['q2_fitted_eta'][closest_T] = eta
        abs_err = abs(eta - target_eta)
        if abs_err <= tol_full:
            score_eta = 1.0
        elif abs_err >= tol_zero:
            score_eta = 0.0
        else:
            score_eta = 1.0 - (abs_err - tol_full) / (tol_zero - tol_full)
        scores.append(score_eta)
    avg_score = sum(scores) / len(scores) if scores else 0.0
    return avg_score


# === block: score_2 (check id='summary_consistency') ===
def score_2(artifact, step, ctx):
    # artifact: dict
    tsg_over_x_rep = float(artifact.get('Tsg_over_x', None)) if artifact.get('Tsg_over_x') is not None else None
    tsg_rep = float(artifact.get('Tsg', None)) if artifact.get('Tsg') is not None else None
    eta_rep = float(artifact.get('eta', None)) if artifact.get('eta') is not None else None
    T_cross = ctx.get('xi_cross_temp', None)
    q2_etas = ctx.get('q2_fitted_eta', {})
    score_tsg = 0.0
    if T_cross is not None and tsg_over_x_rep is not None:
        delta = abs(tsg_over_x_rep - T_cross)
        score_tsg = 1.0 if delta <= 0.05 else max(0.0, 1.0 - (delta - 0.05) / 0.2)
    score_tsg_prod = 0.0
    if tsg_over_x_rep is not None and tsg_rep is not None:
        expected_tsg = tsg_over_x_rep * 0.35
        delta2 = abs(tsg_rep - expected_tsg)
        score_tsg_prod = 1.0 if delta2 < 0.02 else max(0.0, 1.0 - (delta2 - 0.02) / 0.1)
    score_eta = 0.0
    if q2_etas and eta_rep is not None:
        temps = list(q2_etas.keys())
        ref_T = min(temps, key=lambda t: abs(t - 0.1)) if temps else None
        if ref_T is not None:
            ref_eta = q2_etas[ref_T]
            delta3 = abs(eta_rep - ref_eta)
            score_eta = 1.0 if delta3 <= 0.05 else max(0.0, 1.0 - (delta3 - 0.05) / 0.2)
    score = (score_tsg + score_tsg_prod + score_eta) / 3.0
    return score


_SCORERS = {
    'xi_crossing': score_0,
    'q2_decay': score_1,
    'summary_consistency': score_2,
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
