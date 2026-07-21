import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
    gold = {}
    checks = spec.get("steps", [])
    for check in checks:
        if check["id"] == "check_half_filling_ms":
            gold["half"] = check["gold"]
        elif check["id"] == "check_doped_mF_dos":
            gold["doped"] = check["gold"]
    return gold


# === block: score_0 (check id='check_half_filling_ms') ===
def score_0(artifact, step, ctx):
    gold = ctx.get("half", {})
    U_AF = gold["U_AF"]
    m_s_jump = gold["m_s_jump"]
    slope = gold["slope"]
    zero_tol = gold["zero_tol"]
    rel_tol = gold["rel_tol"]
    # artifact is a list of dicts with keys U_t and m_s
    below, above = [], []
    for row in artifact:
        U = float(row["U_t"])
        ms = float(row["m_s"])
        if U <= U_AF + 1e-12:
            below.append(ms)
        else:
            above.append((U, ms))
    zero_ratio = 1.0
    if below:
        zero_ratio = sum(1 for ms in below if abs(ms) < zero_tol) / len(below)
    nonzero_ratio = 0.0
    if above:
        correct = 0
        for U, ms in above:
            expected = m_s_jump + slope * (U - U_AF)
            if expected > 1e-12:
                rel_err = abs(ms - expected) / expected
                if rel_err <= rel_tol:
                    correct += 1
        nonzero_ratio = correct / len(above)
    jump_detected = False
    if below and above:
        max_below = max(below)
        min_above = min(ms for _, ms in above)
        if max_below < zero_tol and min_above > 0.05:
            jump_detected = True
    score = 0.3 * zero_ratio + 0.5 * nonzero_ratio + 0.2 * (1.0 if jump_detected else 0.0)
    return score


# === block: score_1 (check id='check_doped_mF_dos') ===
def score_1(artifact, step, ctx):
    gold = ctx.get("doped", {})
    U1 = gold["U1"]
    U2 = gold["U2"]
    m_F_target = gold["m_F_target"]
    rel_tol = gold["rel_tol"]
    rho_thresh = gold["rho_thresh"]
    m_F_small = gold["m_F_small"]
    # artifact: list of dicts with U_t, m_F, rho_up_0, rho_down_0
    in_window = []
    outside = []
    for row in artifact:
        U = float(row["U_t"])
        mF = float(row["m_F"])
        rho_up = float(row["rho_up_0"])
        rho_down = float(row["rho_down_0"])
        if U1 <= U <= U2:
            in_window.append((mF, rho_up, rho_down))
        else:
            outside.append((mF, rho_up, rho_down))
    win_score = 1.0
    if in_window:
        correct = 0
        for mF, rho_up, rho_down in in_window:
            mF_ok = abs(mF - m_F_target) / m_F_target <= rel_tol
            rho_up_ok = rho_up <= rho_thresh
            rho_down_ok = rho_down > rho_thresh
            if mF_ok and rho_up_ok and rho_down_ok:
                correct += 1
        win_score = correct / len(in_window)
    out_score = 1.0
    if outside:
        correct = 0
        for mF, rho_up, rho_down in outside:
            mF_ok = abs(mF) < m_F_small
            rho_up_ok = rho_up > rho_thresh
            rho_down_ok = rho_down > rho_thresh
            if mF_ok and rho_up_ok and rho_down_ok:
                correct += 1
        out_score = correct / len(outside)
    # Window requirement: at least one point in the HM window must pass
    if not in_window or win_score == 0:
        score = 0.0
    else:
        score = 0.7 * win_score + 0.3 * out_score
    return score


_SCORERS = {
    'check_half_filling_ms': score_0,
    'check_doped_mF_dos': score_1,
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
