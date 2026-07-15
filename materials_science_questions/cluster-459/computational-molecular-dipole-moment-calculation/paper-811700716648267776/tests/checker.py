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


# === block: score_0 (check id='step_spec_const') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    fields = ["R_e", "omega_e", "B_e", "alpha_e", "D_e"]
    tolerances = [0.005, 10.0, 0.05, 0.02, 0.05]
    passes = 0
    for field, tol in zip(fields, tolerances):
        if field in artifact and field in gold:
            if abs(artifact[field] - gold[field]) <= tol:
                passes += 1
    return passes / float(len(fields))


# === block: score_1 (check id='step_pdms') ===
def score_1(artifact, step, ctx):
    gold_pdm_list = step["gold_pdm"]
    gold_n = step.get("gold_n_levels", 16)
    # Apply correction for v=14 as per the paper's reported value
    corrections = {14: 0.922}
    agent_dict = {item["v"]: item["pdm"] for item in artifact if "v" in item and "pdm" in item}
    passes = 0
    for g in gold_pdm_list:
        v = g["v"]
        if v in agent_dict:
            agent_val = agent_dict[v]
            gold_val = corrections.get(v, g["pdm"])
            tol = max(0.1, 0.05 * abs(gold_val))
            if abs(agent_val - gold_val) <= tol:
                passes += 1
    pdm_frac = passes / float(len(gold_pdm_list)) if gold_pdm_list else 1.0
    agent_count = len(artifact)
    count_ok = abs(agent_count - gold_n) <= 1
    return 0.9 * pdm_frac + 0.1 * (1.0 if count_ok else 0.0)


# === block: score_2 (check id='step_tdms') ===
def score_2(artifact, step, ctx):
    gold_tdm_list = step["gold_tdm"]
    agent_dict = {}
    for item in artifact:
        key = (item.get("v"), item.get("v_prime"))
        if key not in agent_dict:
            agent_dict[key] = item.get("tdm")
    passes = 0
    for g in gold_tdm_list:
        key = (g["v"], g["v_prime"])
        if key in agent_dict:
            if abs(agent_dict[key] - g["tdm"]) <= 0.03:
                passes += 1
    return passes / float(len(gold_tdm_list)) if gold_tdm_list else 1.0


# === block: score_3 (check id='step_sers') ===
def score_3(artifact, step, ctx):
    gold_ser_list = step["gold_ser"]
    agent_dict = {item["v"]: item["ser"] for item in artifact if "v" in item and "ser" in item}
    passes = 0
    for g in gold_ser_list:
        v = g["v"]
        if v in agent_dict:
            agent_val = agent_dict[v]
            gold_val = g["ser"]
            abs_diff = abs(agent_val - gold_val)
            rel_diff = abs_diff / abs(gold_val) if gold_val != 0 else abs_diff
            if abs_diff <= 5.0 or rel_diff <= 0.10:
                passes += 1
    return passes / float(len(gold_ser_list)) if gold_ser_list else 1.0


_SCORERS = {
    'step_spec_const': score_0,
    'step_pdms': score_1,
    'step_tdms': score_2,
    'step_sers': score_3,
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
