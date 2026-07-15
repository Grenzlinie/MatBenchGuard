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
    return {}


# === block: score_0 (check id='diffusivity_check') ===
def score_0(artifact, step, ctx):
    import math

    required_deltas = [0.02, 0.04]
    required_Us = [0.0, 0.125, -0.125]
    thetas = [round(0.5 + i * 0.1, 10) for i in range(16)]  # 0.5 .. 2.0 step 0.1
    total_expected = 96  # 2 * 3 * 16

    # Build the set of required parameter triples
    expected_set = set()
    for d in required_deltas:
        for u in required_Us:
            for t in thetas:
                expected_set.add((d, u, t))

    tolerance = step.get("parameters", {}).get("tolerance_rel", 1e-9)
    correct = 0
    seen = set()

    for row in artifact:
        try:
            delta = float(row["delta"])
            U = float(row["U_param"])
            theta = float(row["E_over_kT"])
            key = (delta, U, theta)
            if key in seen:
                continue   # skip duplicates; weight only once per key
            seen.add(key)

            # compute the analytical expressions (same as public instruction)
            w0 = math.exp(theta * (-6.0 + delta * (19.0 - 7.0 * U)))
            w11 = math.exp(theta * (-5.5 - 0.5 * U + 18.0 * delta - 6.0 * delta * U))
            w12 = math.exp(theta * (-5.0 + delta * (17.0 - 7.0 * U)))
            w13 = math.exp(theta * (-4.5 - 0.5 * U + 16.0 * delta - 6.0 * delta * U))

            exp_term = math.exp(-4.0 * theta * (1.0 - U) * (1.0 - 2.0 * delta))
            exp_term_A = math.exp(theta * (1.0 - U) * (4.0 - 7.0 * delta))

            # B correlation factor
            fb = (2.0 * delta * (14.0 * w13 + 25.0 * (w11 + w12)) +
                  8.0 * (1.0 - 15.0 * delta) * w0 +
                  2.0 * (1.0 - 15.0 * delta) * w0 / delta * exp_term)

            # B diffusivity
            Db = (4.0 * delta * (14.0 * w13 + 25.0 * (w11 + w12)) +
                  16.0 * (1.0 - 15.0 * delta) * w0 +
                  4.0 * (1.0 - 15.0 * delta) * w0 / delta * exp_term) / (1.0 + 2.0 * delta)

            # A correlation factor
            fa = (24.1 * delta**2 / (1.0 - 2.0 * delta) * (w13 + 1.5 * (w11 + w12)) * exp_term_A +
                  8.0 * (1.0 - 15.0 * delta) * w0 / (1.0 - 2.0 * delta) *
                  (delta * exp_term_A + math.exp(theta * delta * (1.0 - U))))

            # A diffusivity
            Da = (24.1 * delta**2 * (w13 + 1.5 * (w11 + w12)) +
                  8.0 * (1.0 - 15.0 * delta) * w0 +
                  8.0 * (1.0 - 15.0 * delta) * w0 / delta * exp_term) / (1.0 - 2.0 * delta)

            # read agent's values
            fA = float(row["f_A"])
            fB = float(row["f_B"])
            DA = float(row["D_A_star"])
            DB = float(row["D_B_star"])

            def rel_diff(a, e):
                denom = abs(e) if abs(e) > 1e-300 else 1e-300
                return abs(a - e) / denom

            ok_fa = rel_diff(fA, fa) <= tolerance
            ok_fb = rel_diff(fB, fb) <= tolerance
            ok_da = rel_diff(DA, Da) <= tolerance
            ok_db = rel_diff(DB, Db) <= tolerance

            if ok_fa and ok_fb and ok_da and ok_db:
                correct += 1
        except (ValueError, KeyError, ZeroDivisionError):
            pass

    # missing rows count as incorrect
    score = correct / total_expected
    return max(0.0, min(1.0, score))


_SCORERS = {
    'diffusivity_check': score_0,
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
