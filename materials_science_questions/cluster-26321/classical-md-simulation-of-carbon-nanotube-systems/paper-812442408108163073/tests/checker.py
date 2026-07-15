import os
import json
import csv

# === author imports / helpers ===
import math


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
    step = spec["steps"][0]
    ctx = {
        "tau_ref": step["tau_ref"],
        "ordering": step["ordering"],
        "tol_rel": step["tolerance_relative"],
        "tol_abs": step["tolerance_absolute"]
    }
    return ctx


# === block: score_0 (check id='step_04_correlation_functions') ===
def score_0(artifact, step, ctx):
    tau_ref = ctx["tau_ref"]
    ordering = ctx["ordering"]
    tol_rel = ctx["tol_rel"]
    tol_abs = ctx["tol_abs"]
    directions = ["dipole", "hh", "perp"]

    def integrate(time, C):
        n = len(time)
        if n < 2:
            return None
        integral = 0.0
        for i in range(n - 1):
            h = time[i + 1] - time[i]
            integral += 0.5 * (C[i] + C[i + 1]) * h
        return integral

    def score_val(val, ref, tr, ta):
        tol = max(tr * abs(ref), ta)
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        excess = diff - tol
        penalty = excess / (0.5 * abs(ref) + ta)
        return max(0.0, 1.0 - penalty)

    tau_scores = []
    ordering_ok = {d: True for d in directions}

    for d in directions:
        t1_vals = []
        t2_vals = []
        for sys in ordering:
            try:
                sys_obj = artifact[sys]
                vec_obj = sys_obj[d]
                time = [float(x) for x in vec_obj["time"]]
                c1 = [float(x) for x in vec_obj["C1"]]
                c2 = [float(x) for x in vec_obj["C2"]]
            except (KeyError, TypeError, ValueError):
                return 0.0
            if len(time) < 2 or len(time) != len(c1) or len(time) != len(c2):
                return 0.0
            tau1 = integrate(time, c1)
            tau2 = integrate(time, c2)
            if tau1 is None or tau2 is None:
                return 0.0
            t1_vals.append(tau1)
            t2_vals.append(tau2)
            ref1, ref2 = tau_ref[sys][d]
            tau_scores.append(score_val(tau1, ref1, tol_rel, tol_abs))
            tau_scores.append(score_val(tau2, ref2, tol_rel, tol_abs))
        # ordering: strictly decreasing along the given list
        def is_decreasing(vals):
            return all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
        if not is_decreasing(t1_vals) or not is_decreasing(t2_vals):
            ordering_ok[d] = False

    avg_tau = sum(tau_scores) / len(tau_scores) if tau_scores else 0.0
    ord_frac = sum(1.0 for d in directions if ordering_ok[d]) / len(directions)
    final = 0.8 * avg_tau + 0.2 * ord_frac
    return final


_SCORERS = {
    'step_04_correlation_functions': score_0,
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
