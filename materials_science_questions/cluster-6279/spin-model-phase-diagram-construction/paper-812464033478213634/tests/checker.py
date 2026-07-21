import os
import json
import csv

# === author imports / helpers ===
import math

def linear_regression_slope(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x*y for x,y in zip(xs, ys))
    sum_xx = sum(x*x for x in xs)
    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        return float('inf')
    numerator = n * sum_xy - sum_x * sum_y
    return numerator / denom


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


# === block: score_0 (check id='step_specific_heat_fss') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import numpy as np
        mu_ideal = step.get("mu_ideal", [-1.14, -0.75])
        ref = step.get("ref_alpha_nu", [1.065, 0.529])
        tol = step.get("tolerance_alpha", [0.08, 0.08])
        rows = []
        for r in artifact:
            try:
                rows.append({"N": int(r["N"]), "mu": float(r["mu"]), "c_max": float(r["c_max"])})
            except:
                pass
        scores = []
        for i, mu0 in enumerate(mu_ideal):
            subset = [r for r in rows if abs(r["mu"] - mu0) < 0.005]
            if len(subset) < 3:
                scores.append(0.0)
                continue
            xs = []
            ys = []
            for r in subset:
                xs.append(np.log(r["N"]))
                ys.append(np.log(r["c_max"]))
            if len(xs) < 3:
                scores.append(0.0)
                continue
            slope = np.polyfit(xs, ys, 1)[0]
            error = abs(slope - ref[i])
            if error <= tol[i]:
                sc = 1.0
            else:
                sc = max(0.0, 1.0 - (error - tol[i]) / (0.5 * ref[i]))
            scores.append(sc)
        return np.mean(scores) if scores else 0.0


# === block: score_1 (check id='step_susceptibility_fss') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import numpy as np
        mu_ideal = step.get("mu_ideal", [-1.14, -0.75])
        ref = step.get("ref_gamma_nu", [1.763, 1.540])
        tol = step.get("tolerance_gamma", [0.082, 0.116])
        rows = []
        for r in artifact:
            try:
                rows.append({"N": int(r["N"]), "mu": float(r["mu"]), "chi_max": float(r["chi_max"])})
            except:
                pass
        scores = []
        for i, mu0 in enumerate(mu_ideal):
            subset = [r for r in rows if abs(r["mu"] - mu0) < 0.005]
            if len(subset) < 3:
                scores.append(0.0)
                continue
            xs = []
            ys = []
            for r in subset:
                xs.append(np.log(r["N"]))
                ys.append(np.log(r["chi_max"]))
            if len(xs) < 3:
                scores.append(0.0)
                continue
            slope = np.polyfit(xs, ys, 1)[0]
            error = abs(slope - ref[i])
            if error <= tol[i]:
                sc = 1.0
            else:
                sc = max(0.0, 1.0 - (error - tol[i]) / (0.5 * ref[i]))
            scores.append(sc)
        return np.mean(scores) if scores else 0.0


# === block: score_2 (check id='step_special_points') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        import numpy as np
        gold_points = step.get("gold_points", [])
        rows = []
        for r in artifact:
            try:
                rows.append({"T": float(r["T"]), "Theta": float(r["Theta"]), "boundary_type": r["boundary_type"].strip().lower()})
            except:
                pass
        scores = []
        for gp in gold_points:
            candidates = [r for r in rows if r["boundary_type"] == gp["type"]]
            if not candidates:
                scores.append(0.0)
                continue
            dists = []
            for r in candidates:
                dT = abs(r["T"] - gp["T"]) / gp["abs_tol_T"]
                dT = dT if gp["abs_tol_T"] > 0 else 1e9
                dTheta = abs(r["Theta"] - gp["Theta"]) / gp["abs_tol_Theta"]
                dTheta = dTheta if gp["abs_tol_Theta"] > 0 else 1e9
                dists.append(max(dT, dTheta))
            min_dist = min(dists)
            if min_dist <= 1.0:
                sc = 1.0
            else:
                sc = max(0.0, 1.0 - (min_dist - 1.0) * 0.3)
            scores.append(sc)
        return np.mean(scores) if scores else 0.0


# === block: score_3 (check id='step_topology') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        types = set()
        thetas = []
        for r in artifact:
            try:
                t = r.get("boundary_type", "").strip().lower()
                if t:
                    types.add(t)
                thetas.append(float(r["Theta"]))
            except:
                pass
        required = set(step.get("required_boundary_types", []))
        type_score = len(types & required) / max(len(required), 1)
        if thetas:
            min_t = min(thetas)
            max_t = max(thetas)
            range_score = 1.0 if min_t <= step.get("theta_range_min", 0.05) and max_t >= step.get("theta_range_max", 0.33) else max(0.0, min(1.0, (min_t - 0.0) / 0.1))
        else:
            range_score = 0.0
        return 0.5 * type_score + 0.5 * range_score


_SCORERS = {
    'step_specific_heat_fss': score_0,
    'step_susceptibility_fss': score_1,
    'step_special_points': score_2,
    'step_topology': score_3,
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
