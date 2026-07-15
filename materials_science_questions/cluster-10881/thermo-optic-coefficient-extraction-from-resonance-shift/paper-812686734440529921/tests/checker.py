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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def compute_gold(ne, T_C):
        lam = 0.6328  # µm
        k = 2*math.pi / lam
        ns = 1.605
        Dns = 0.08875
        n0 = 1.0
        xi = 1.0
        T_K = T_C + 273.15
        # Avoid negative values under sqrt
        ns2_n2 = max(ns**2 - ne**2, 0.0)
        n2_n02 = max(ne**2 - n0**2, 0.0)
        if ns2_n2 <= 0 or n2_n02 <= 0:
            return (0.0, 0.0)
        ks = k * math.sqrt(ns2_n2)
        k0 = k * math.sqrt(n2_n02)
        if ks == 0 or k0 == 0:
            return (0.0, 0.0)
        # Equation (12): d1 ks^3 / (3 k^2 ns Dns) = pi/4 + atan(xi*k0/ks)
        rhs = math.pi/4 + math.atan(xi * k0 / ks)
        d1 = rhs * 3 * k**2 * ns * Dns / ks**3
        # Compute t from d1 using eq. (10) with T in K
        factor = 8.243e3 * math.exp(-1.02e4 / (2 * T_K))
        if factor <= 0:
            return (0.0, 0.0)
        t = (d1 / factor) ** 2
        # Compute alpha
        denom = (ne/k0) * xi * (1 + (k0/ks)**2) / (1 + (xi*k0/ks)**2) + 3.0/ks
        if denom == 0:
            return (0.0, 0.0)
        alpha = ks**4 * d1 / (6 * k**4 * ns * Dns * denom)
        # Sensitivities
        delta_t = alpha / t if t != 0 else 0.0
        delta_T = 1.02e4 * alpha / (T_K**2)
        return (delta_t, delta_T)

    def score(artifact, step, ctx):
        tolerance_rel = step.get("tolerance", {}).get("relative", 0.1)
        tolerance_abs = step.get("tolerance", {}).get("absolute", 0.0002)
        rows = artifact
        if not rows:
            return 0.0
        passed = 0
        for row in rows:
            try:
                ne = float(row["ne"])
                T_C = int(row["temperature_C"])
                agent_delta_t = float(row["delta_ne_delta_t"])
                agent_delta_T = float(row["delta_ne_delta_T"])
            except (ValueError, KeyError):
                continue
            gold_delta_t, gold_delta_T = compute_gold(ne, T_C)
            if gold_delta_t == 0 and gold_delta_T == 0:
                # degenerate, skip row
                continue
            ok_t = (abs(agent_delta_t - gold_delta_t) <= tolerance_rel * abs(gold_delta_t) or
                    abs(agent_delta_t - gold_delta_t) <= tolerance_abs)
            ok_T = (abs(agent_delta_T - gold_delta_T) <= tolerance_rel * abs(gold_delta_T) or
                    abs(agent_delta_T - gold_delta_T) <= tolerance_abs)
            if ok_t and ok_T:
                passed += 1
        return passed / len(rows) if rows else 0.0


_SCORERS = {
    'step_01': score_0,
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
