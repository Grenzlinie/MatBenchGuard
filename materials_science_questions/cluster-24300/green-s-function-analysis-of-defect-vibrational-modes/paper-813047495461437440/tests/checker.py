import os
import json
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
    return {}


# === block: score_0 (check id='curved_line_fit') ===
def score_0(artifact, step, ctx):
    import csv
    import math

    def _fit_no_intercept(xs, ys):
        n = len(xs)
        if n == 0:
            return None, None
        sxy = sum(xs[i]*ys[i] for i in range(n))
        sxx = sum(xs[i]*xs[i] for i in range(n))
        if sxx == 0:
            return None, None
        a = sxy / sxx
        ss_res = sum((ys[i] - a*xs[i])**2 for i in range(n))
        ss_tot = sum(yi**2 for yi in ys)
        if ss_tot == 0:
            r2 = 0.0
        else:
            r2 = 1.0 - ss_res / ss_tot
        return a, r2

    if artifact is None:
        return 0.0

    x_vals = []
    y_vals = []
    try:
        for row in artifact:
            L = float(row["L"])
            K = float(row["K"])
            e = float(row["e_per_L"])
            x_vals.append(K * L)
            y_vals.append(e)
    except (KeyError, ValueError, TypeError):
        return 0.0

    if len(x_vals) < 5:
        return 0.0

    a, r2 = _fit_no_intercept(x_vals, y_vals)
    if a is None or r2 is None:
        return 0.0

    target_a = step.get("target", -43.9)
    tol_a = step.get("tolerance_abs", 2.0)
    min_r2 = step.get("min_r2", 0.9)

    if abs(a - target_a) <= tol_a and r2 > min_r2:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='pair_fit') ===
def score_1(artifact, step, ctx):
    import csv
    import math

    def _fit_no_intercept(xs, ys):
        n = len(xs)
        if n == 0:
            return None, None
        sxy = sum(xs[i]*ys[i] for i in range(n))
        sxx = sum(xs[i]*xs[i] for i in range(n))
        if sxx == 0:
            return None, None
        a = sxy / sxx
        return a, None

    if artifact is None:
        return 0.0

    dists = []
    energies = []
    try:
        for row in artifact:
            d = int(row["distance"])
            e = float(row["interaction_energy"])
            if d <= 0:
                return 0.0
            dists.append(d)
            energies.append(e)
    except (KeyError, ValueError, TypeError):
        return 0.0

    if len(dists) < 3:
        return 0.0

    # Check positivity
    if any(e <= 0 for e in energies):
        return 0.0

    x_vals = [1.0 / d for d in dists]
    y_vals = energies
    a_prime, _ = _fit_no_intercept(x_vals, y_vals)
    if a_prime is None:
        return 0.0

    target_ap = step.get("target", 0.485)
    tol_ap = step.get("tolerance_abs", 0.02)

    if abs(a_prime - target_ap) <= tol_ap:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'curved_line_fit': score_0,
    'pair_fit': score_1,
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
