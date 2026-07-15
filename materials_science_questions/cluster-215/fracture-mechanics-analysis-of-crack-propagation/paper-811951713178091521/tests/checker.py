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
    import math

    # Given parameters (mirror instruction.md)
    s = 0.6
    nu = 0.3
    alpha = 0.5
    beta = 0.2
    G_IC = 200.0
    M = 1000.0

    # baseline F_A
    F_A = math.pi * math.sqrt(32.0 * G_IC * M)

    # C1, C2 for saw drill
    lns = math.log(s)
    term = 3.0 + 2.0 * lns
    s2 = s * s
    s4 = s2 * s2
    s6 = s4 * s2
    C1 = 1.0 - term * s2 + term * s4 - s6
    C2 = (1.0 + 2.0 * lns) * s2 - (2.0 + 2.0 * lns) * s4 + s6
    den_SD = C1 + nu * C2
    F_SD = F_A / math.sqrt(den_SD)
    ratio_SD = 1.0 / math.sqrt(den_SD)

    # candle stick drill
    term_CD = 1.0 + (alpha * alpha) * den_SD
    F_CD = (1.0 + alpha) * F_A / math.sqrt(term_CD)
    ratio_CD = (1.0 + alpha) / math.sqrt(term_CD)

    # core drill coefficients
    b1 = 1.0 - beta
    b1_sq = b1 * b1
    linprod = beta * (2.0 - beta)
    ln1mb = math.log(b1)
    factor = (2.0 * b1_sq) / linprod
    A = factor * ln1mb
    A_coeff = 2.0 - 2.0 * beta + beta * beta
    term1_coeff = 2.0 - 2.0 * beta + 1.5 * beta * beta
    Q = term1_coeff + 2.0*lns + A
    term1_C3 = -Q * s2
    inner_C3 = (2.0 - beta + beta*beta) / 2.0 + lns + (b1_sq / linprod) * ln1mb
    term2_C3_coeff = A_coeff * inner_C3
    term2_C3 = term2_C3_coeff * s4
    term3_C3 = -(A_coeff * A_coeff / 4.0) * s6
    C3 = 1.0 + term1_C3 + term2_C3 + term3_C3
    first_C4 = (2.0*lns - A) * s2
    inner_C4 = -0.5 - lns + (b1_sq / linprod) * ln1mb
    term2_C4 = A_coeff * inner_C4 * s4
    term3_C4 = (A_coeff * A_coeff / 4.0) * s6
    C4 = first_C4 + term2_C4 + term3_C4
    den_RD = C3 + nu * C4
    F_RD = F_A / math.sqrt(den_RD)
    ratio_RD = 1.0 / math.sqrt(den_RD)

    ref = {
        "saw_drill": {"F_SD": F_SD, "F_A": F_A, "ratio_SD": ratio_SD},
        "candle_stick_drill": {"F_CD": F_CD, "F_A": F_A, "ratio_CD": ratio_CD},
        "core_drill": {"F_RD": F_RD, "F_A": F_A, "ratio_RD": ratio_RD}
    }
    return ref


# === block: score_0 (check id='compute_thrust') ===
def score_0(artifact, step, ctx):
    ref = ctx
    tol = step.get("tolerance_abs", 1e-9)
    count_total = 0
    count_match = 0
    for drill_key in ["saw_drill", "candle_stick_drill", "core_drill"]:
        drill_artifact = artifact.get(drill_key, {})
        drill_ref = ref.get(drill_key, {})
        for field in drill_ref.keys():
            count_total += 1
            if field in drill_artifact:
                if abs(drill_artifact[field] - drill_ref[field]) <= tol:
                    count_match += 1
    if count_total == 0:
        return 0.0
    return count_match / count_total


_SCORERS = {
    'compute_thrust': score_0,
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
