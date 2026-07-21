import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='step_compute_gbg') ===
def score_0(artifact, step, ctx):
    import math

    def gaussian_kt(t, delta):
        d2 = delta*delta
        t2 = t*t
        exp_term = math.exp(-d2 * t2 / 2.0)
        return 1.0/3.0 + (2.0/3.0) * (1.0 - d2 * t2) * exp_term

    def gbg(t, delta_eff, R):
        d2 = delta_eff*delta_eff
        t2 = t*t
        R2 = R*R
        denom = 1.0 + R2 + R2 * d2 * t2
        factor1 = ((1.0 + R2) / denom) ** 1.5
        factor2 = 1.0 - d2 * t2 / denom
        exp_arg = -d2 * t2 / (2.0 * denom)
        return 1.0/3.0 + (2.0/3.0) * factor1 * factor2 * math.exp(exp_arg)

    tol_r0 = step.get("tolerance_R0", 1e-6)
    tol_r1 = step.get("tolerance_R1", 1e-6)
    mtol = step.get("monotonic_tol", 1e-9)
    expected_t = step.get("expected_t_points", [])
    if len(expected_t) != 11:
        return 0.0

    if not isinstance(artifact, dict):
        return 0.0

    R0 = artifact.get("R0_values")
    R1 = artifact.get("R1_values")
    bool_R0 = artifact.get("R0_matches_Gaussian")
    bool_R1 = artifact.get("R1_monotonic")

    if not (isinstance(R0, list) and isinstance(R1, list) and isinstance(bool_R0, bool) and isinstance(bool_R1, bool)):
        return 0.0
    if len(R0) != 11 or len(R1) != 11:
        return 0.0

    def _validate_pairs(pairs):
        for p in pairs:
            if (not isinstance(p, (list, tuple))) or len(p) != 2:
                return False
            if not (isinstance(p[0], (int, float)) and isinstance(p[1], (int, float))):
                return False
        return True

    if not (_validate_pairs(R0) and _validate_pairs(R1)):
        return 0.0

    # check time points exactly match expected within epsilon
    t_epsilon = 1e-9
    for i, (pair0, pair1) in enumerate(zip(R0, R1)):
        if abs(pair0[0] - expected_t[i]) > t_epsilon or abs(pair1[0] - expected_t[i]) > t_epsilon:
            return 0.0

    # compute reference values
    ref_R0 = [gaussian_kt(t, 1.0) for t in expected_t]   # standard KT with Δ=1
    ref_R1 = [gbg(t, 1.0, 1.0) for t in expected_t]        # GBG with Δ_eff=1, R=1

    max_diff_R0 = max(abs(pair[1] - ref) for pair, ref in zip(R0, ref_R0))
    max_diff_R1 = max(abs(pair[1] - ref) for pair, ref in zip(R1, ref_R1))

    score_R0 = 1.0 if max_diff_R0 <= tol_r0 else 0.0
    score_R1 = 1.0 if max_diff_R1 <= tol_r1 else 0.0

    gz_R1 = [p[1] for p in R1]
    monotonic_true = all(gz_R1[i] >= gz_R1[i+1] - mtol for i in range(len(gz_R1)-1))

    agent_R0_match_truth = max_diff_R0 <= tol_r0
    agent_R1_monotonic_truth = monotonic_true

    score_bool0 = 1.0 if bool_R0 == agent_R0_match_truth else 0.0
    score_bool1 = 1.0 if bool_R1 == agent_R1_monotonic_truth else 0.0

    final = 0.4*score_R0 + 0.4*score_R1 + 0.1*score_bool0 + 0.1*score_bool1
    return final


_SCORERS = {
    'step_compute_gbg': score_0,
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
