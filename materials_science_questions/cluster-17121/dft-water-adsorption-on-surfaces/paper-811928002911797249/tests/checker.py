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
    steps = spec.get("steps", [])
    gold_ift = []
    gold_ca = {}
    for step in steps:
        if step["id"] == "step_ift_score":
            gold_ift = step.get("gold_ift_table", [])
        elif step["id"] == "step_ca_score":
            gold_ca = step.get("gold_ca", {})
    ift_lookup = {}
    for row in gold_ift:
        key = (float(row["pressure_Mpa"]), int(row["ethanol_molecules"]))
        ift_lookup[key] = float(row["ift_mN_per_m"])
    return {"ift_lookup": ift_lookup, "gold_ca": gold_ca}


# === block: score_0 (check id='step_ift_score') ===
def score_0(artifact, step, ctx):
    ift_lookup = ctx["ift_lookup"]
    tolerance = step.get("tolerance_mN_per_m", 5.0)
    if not artifact or not isinstance(artifact, list):
        return 0.0
    total = len(ift_lookup)
    if total == 0:
        return 1.0
    matched = 0
    artifact_data = {}
    for row in artifact:
        try:
            p = float(row.get("pressure_Mpa", ""))
            e = int(float(row.get("ethanol_molecules", "")))
            i = float(row.get("ift_mN_per_m", ""))
        except (ValueError, TypeError):
            continue
        artifact_data[(p, e)] = i
    for key, gold_val in ift_lookup.items():
        agent_val = artifact_data.get(key)
        if agent_val is not None and abs(agent_val - gold_val) <= tolerance:
            matched += 1
    return matched / total


# === block: score_1 (check id='step_ca_score') ===
def score_1(artifact, step, ctx):
    gold_ca = ctx["gold_ca"]
    tolerance_deg = step.get("tolerance_deg", 4.0)
    # Allow agent std deviation to be at most paper gold std + 0.5 deg
    std_tol = step.get("std_tol", 0.5)
    if not artifact or not isinstance(artifact, list):
        return 0.0
    artifact_dict = {}
    for row in artifact:
        sys = str(row.get("system", "")).strip()
        try:
            ang = float(row.get("contact_angle_deg", ""))
            std = float(row.get("std_dev_deg", ""))
        except (ValueError, TypeError):
            continue
        artifact_dict[sys] = (ang, std)
    total = len(gold_ca)
    if total == 0:
        return 1.0
    matched = 0
    for sys, gold in gold_ca.items():
        gold_mean = float(gold["contact_angle_deg"])
        gold_std = float(gold.get("std_dev_deg", 0.0))
        if sys in artifact_dict:
            ang, std = artifact_dict[sys]
            if abs(ang - gold_mean) <= tolerance_deg and std <= gold_std + std_tol:
                matched += 1
    return matched / total


_SCORERS = {
    'step_ift_score': score_0,
    'step_ca_score': score_1,
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
