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
    params = {"K": 1.0, "gamma1": 1.0, "alpha4": 10.0, "r_core": 0.1, "r_max": 5.0, "d": 10.0, "zeta": 0.1, "channel_alphas": [10.0, 50.0, 100.0, 200.0]}
    L = math.log(params["r_max"] / params["r_core"])
    # compute D1 and D1' using Eq. 33, 35
    c1 = math.pi * params["gamma1"] / 4
    c2 = math.pi * params["gamma1"]**1.5 / (8 * math.sqrt(2))
    D1 = c1 * L - c2 / math.sqrt(params["alpha4"]) * (L**2 + L - 2.5)
    D1p = c1 * L - c2 / math.sqrt(params["alpha4"]) * (L**2 - 7*L + 5.5)
    # channel velocities for each alpha4
    channel_expect = []
    for a in params["channel_alphas"]:
        D1_a = c1 * L - c2 / math.sqrt(a) * (L**2 + L - 2.5)
        D1p_a = c1 * L - c2 / math.sqrt(a) * (L**2 - 7*L + 5.5)
        u_plus = math.pi**2 * params["K"] / (2 * params["d"] * D1_a)
        u_minus = math.pi**2 * params["K"] / (2 * params["d"] * D1p_a)
        channel_expect.append((a, u_plus, u_minus))
    # active free velocity
    D5 = math.pi * params["zeta"] * math.sqrt(params["gamma1"]) * params["r_max"] / (3 * math.sqrt(2 * params["alpha4"]))
    u_free = -D5 / D1
    ctx = {"expected_D1": D1, "expected_D1_prime": D1p, "channel_expect": channel_expect, "expected_u_free": u_free}
    return ctx


# === block: score_0 (check id='drag_coefficients') ===
def score_0(artifact, step, ctx):
    import json, math
    with open("/app/inputs/parameters.json") as f:
        params = json.load(f)
    alpha4 = params["alpha4"]
    gamma1 = params["gamma1"]
    r_max = params["r_max"]
    r_core = params["r_core"]
    L = math.log(r_max / r_core)
    c1 = math.pi * gamma1 / 4
    c2 = math.pi * gamma1**1.5 / (8 * math.sqrt(2))
    expected_D1 = c1 * L - c2 / math.sqrt(alpha4) * (L**2 + L - 2.5)
    expected_D1_prime = c1 * L - c2 / math.sqrt(alpha4) * (L**2 - 7*L + 5.5)
    d1_ok = abs(artifact["D1"] - expected_D1) <= 0.0001
    d1p_ok = abs(artifact["D1_prime"] - expected_D1_prime) <= 0.0001
    return 1.0 if (d1_ok and d1p_ok) else 0.0


# === block: score_1 (check id='channel_velocities') ===
def score_1(artifact, step, ctx):
    expect = ctx["channel_expect"]
    rows = 0
    good = 0
    for row in artifact:
        try:
            a = float(row["alpha4"])
            u_plus = float(row["u_plus_half"])
            u_minus = float(row["u_minus_half"])
        except:
            continue
        rows += 1
        # find matching expected row
        found = None
        for e in expect:
            if abs(e[0] - a) < 1e-6:
                found = e
                break
        if found is None:
            continue
        if abs(u_plus - found[1]) <= 0.0001 and abs(u_minus - found[2]) <= 0.0001 and u_plus > u_minus:
            good += 1
    return good / max(rows, 1)


# === block: score_2 (check id='active_free_velocity') ===
def score_2(artifact, step, ctx):
    if abs(artifact["u_free"] - ctx["expected_u_free"]) <= 0.0001:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'drag_coefficients': score_0,
    'channel_velocities': score_1,
    'active_free_velocity': score_2,
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
