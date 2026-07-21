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
    extrapolated_path = os.path.join(outputs_dir, "extrapolated_results.json")
    return {"extrapolated_path": extrapolated_path}


# === block: score_0 (check id='finite_size') ===
def score_0(artifact, step, ctx):
    # Validate structure
    if not isinstance(artifact, list) or len(artifact) != 12:
        return 0.0
    cols = {"transition", "L", "K_c(L)", "Q(L)"}
    counts = {}
    for row in artifact:
        if not all(col in row for col in cols):
            return 0.0
        t = int(row["transition"])
        l = int(row["L"])
        if t not in (1,2,3) or l not in (4,5,6,7):
            return 0.0
        counts[(t,l)] = 1
    if len(counts) != 12:
        return 0.0
    # Load extrapolated results
    prop = ctx.get("extrapolated_path")
    if not prop or not os.path.exists(prop):
        return 0.0
    with open(prop) as f:
        extrap = json.load(f)

    def linear_fit_intercept(xs, ys):
        """Return intercept of linear regression y = a*x + b."""
        n = len(xs)
        if n < 2:
            return None
        sum_x = sum(xs)
        sum_y = sum(ys)
        sum_xy = sum(x*y for x,y in zip(xs,ys))
        sum_xx = sum(x*x for x in xs)
        denom = n*sum_xx - sum_x*sum_x
        if abs(denom) < 1e-12:
            return None
        intercept = (sum_xx*sum_y - sum_x*sum_xy) / denom
        return intercept

    tol = 1e-6
    consistent = 0
    for trans in (1,2,3):
        rows = [row for row in artifact if int(row["transition"]) == trans]
        rows.sort(key=lambda r: int(r["L"]))
        xs = [1.0/(int(r["L"])**2) for r in rows]
        y_Kc = [float(r["K_c(L)"]) for r in rows]
        y_Q = [float(r["Q(L)"]) for r in rows]
        fit_Kc_intercept = linear_fit_intercept(xs, y_Kc)
        fit_Q_intercept = linear_fit_intercept(xs, y_Q)
        exp_Kc = extrap.get(f"K_c_{trans}")
        exp_Q = extrap.get(f"Q_{trans}")
        if exp_Kc is not None and exp_Q is not None and fit_Kc_intercept is not None and fit_Q_intercept is not None:
            if abs(fit_Kc_intercept - exp_Kc) < tol and abs(fit_Q_intercept - exp_Q) < tol:
                consistent += 1
    # Score: 0.2 for structure, 0.8 for consistency
    score = 0.2 + 0.8 * (consistent / 3.0)
    return min(score, 1.0)


# === block: score_1 (check id='extrapolated') ===
def score_1(artifact, step, ctx):
    required_keys = [
        "K_c_1", "K_c_1_err", "Q_1", "Q_1_err",
        "K_c_2", "K_c_2_err", "Q_2", "Q_2_err",
        "K_c_3", "K_c_3_err", "Q_3", "Q_3_err"
    ]
    if not isinstance(artifact, dict):
        return 0.0
    if not all(k in artifact for k in required_keys):
        return 0.0
    for k in required_keys:
        if not isinstance(artifact[k], (int, float)):
            return 0.0
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    vals = ["K_c_1", "Q_1", "K_c_2", "Q_2", "K_c_3", "Q_3"]
    scr_sum = 0.0
    for key in vals:
        g = gold.get(key, None)
        t = tols.get(key, None)
        if g is None or t is None:
            return 0.0
        v = artifact.get(key, None)
        if v is None:
            return 0.0
        diff = abs(v - g)
        if diff <= t:
            scr = 1.0
        elif diff <= 2*t:
            scr = 0.5
        else:
            scr = 0.0
        scr_sum += scr
    return scr_sum / 6.0


_SCORERS = {
    'finite_size': score_0,
    'extrapolated': score_1,
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
