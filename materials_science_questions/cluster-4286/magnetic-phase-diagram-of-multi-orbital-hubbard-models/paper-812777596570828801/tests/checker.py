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


# === block: score_0 (check id='zero_field_gaps') ===
def score_0(artifact, step, ctx):
    gold_data = step["config"]["gold"]
    tol = step["config"]["tolerance_abs"]
    if not isinstance(artifact, list):
        return 0.0
    agent_dict = {}
    for entry in artifact:
        v = entry.get("V_over_t")
        if v is not None:
            agent_dict[round(v, 8)] = entry
    matched = 0
    total = len(gold_data)
    for gold_entry in gold_data:
        v = round(gold_entry["V_over_t"], 8)
        agent_entry = agent_dict.get(v)
        if agent_entry is None:
            continue
        up = agent_entry.get("Delta_upup")
        dn = agent_entry.get("Delta_downdown")
        phase = agent_entry.get("phase", "")
        if up is None or dn is None:
            continue
        if (abs(up - gold_entry["Delta_upup"]) <= tol and
            abs(dn - gold_entry["Delta_downdown"]) <= tol and
            phase == gold_entry["phase"]):
            matched += 1
    return matched / total if total > 0 else 0.0


# === block: score_1 (check id='finite_field_scan') ===
def score_1(artifact, step, ctx):
    h_x = step["config"]["h_x"]
    tol_h = step["config"]["tolerance_h"]
    gap_zero_tol = step["config"]["gap_zero_tol"]
    phase_l = step["config"]["phase_lower"]
    phase_u = step["config"]["phase_upper"]
    min_pts = step["config"].get("min_points_per_phase", 3)
    if not isinstance(artifact, list) or len(artifact) < 2 * min_pts:
        return 0.0
    artifact.sort(key=lambda x: x.get("h_over_t", 0.0))
    prev_phase = artifact[0].get("phase")
    transition_field = None
    for i in range(1, len(artifact)):
        curr_phase = artifact[i].get("phase")
        if curr_phase != prev_phase:
            transition_field = artifact[i].get("h_over_t")
            break
    sub_scores = []
    if transition_field is not None and abs(transition_field - h_x) <= tol_h:
        sub_scores.append(1.0)
    else:
        sub_scores.append(0.0)
    lower_phase_exists = any(e.get("phase") == phase_l for e in artifact)
    upper_phase_exists = any(e.get("phase") == phase_u for e in artifact)
    sub_scores.append(1.0 if (lower_phase_exists and upper_phase_exists) else 0.0)
    gap_ok = True
    for e in artifact:
        if e.get("phase") == phase_l:
            up = e.get("Delta_upup", 0.0)
            dn = e.get("Delta_downdown", 0.0)
            if abs(up) > gap_zero_tol or dn <= gap_zero_tol:
                gap_ok = False
                break
    if gap_ok:
        for e in artifact:
            if e.get("phase") == phase_u:
                up = e.get("Delta_upup", 0.0)
                dn = e.get("Delta_downdown", 0.0)
                if up <= gap_zero_tol or dn <= gap_zero_tol or dn <= up:
                    gap_ok = False
                    break
    sub_scores.append(1.0 if gap_ok else 0.0)
    total = 0.5 * sub_scores[0] + 0.25 * sub_scores[1] + 0.25 * sub_scores[2]
    return max(0.0, min(1.0, total))


_SCORERS = {
    'zero_field_gaps': score_0,
    'finite_field_scan': score_1,
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
