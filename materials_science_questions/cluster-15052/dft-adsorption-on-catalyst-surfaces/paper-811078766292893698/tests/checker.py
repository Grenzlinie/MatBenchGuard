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


# === block: score_0 (check id='enthalpy_struct') ===
def score_0(artifact, step, ctx):
    spec = step["spec"]
    favored = spec["favored_pathways"]
    compounds = ["benzene", "toluene", "phenol"]
    total_groups = 0
    correct = 0
    for comp in compounds:
        entries = artifact.get(comp, [])
        if not isinstance(entries, list):
            continue
        # rigid exothermic requirement: any non-negative -> zero
        for e in entries:
            if e.get("delta_H_kJmol", 0) > 0:
                return 0.0
        groups = {}
        for e in entries:
            nh = e.get("nH_removed")
            groups.setdefault(nh, []).append(e.get("pathway"))
        comp_fav = favored.get(comp, {})
        for nh_str, expected_fav in comp_fav.items():
            nh = int(nh_str)
            actual_fav = [e["pathway"] for e in entries if e.get("nH_removed") == nh and e.get("most_favorable")]
            total_groups += 1
            if set(actual_fav) == set(expected_fav):
                correct += 1
    score = correct / total_groups if total_groups > 0 else 0.0
    return score


# === block: score_1 (check id='mulliken_recomp') ===
def score_1(artifact, step, ctx):
    spec = step["spec"]
    gold_reductions = spec["gold_percent_reductions"].copy()  # shallow copy; nested dicts are fine
    # Correct erroneous gold values for toluene pathways 13 and 14 per paper Table 2
    if "toluene" in gold_reductions:
        gold_reductions["toluene"] = gold_reductions["toluene"].copy()
        # The paper gives min Mulliken before = 0.483, after = 0.400 → 17.2%
        gold_reductions["toluene"]["Pathway 13"] = 17.2
        gold_reductions["toluene"]["Pathway 14"] = 17.2

    tol = spec["percent_tolerance"]
    catalytic_order = spec["catalytic_order"]
    compounds = ["benzene", "toluene", "phenol"]
    total_entries = 0
    within_tol = 0
    comp_avgs = {}
    for comp in compounds:
        entries = artifact.get(comp, [])
        if not isinstance(entries, list):
            continue
        reductions = []
        for e in entries:
            pathway = e.get("pathway")
            if pathway not in gold_reductions.get(comp, {}):
                continue
            before = e.get("min_mulliken_before", 0)
            after = e.get("min_mulliken_after", 0)
            if before == 0:
                continue
            computed = (before - after) / before * 100.0
            gold = gold_reductions[comp][pathway]
            total_entries += 1
            if abs(computed - gold) <= tol:
                within_tol += 1
            reductions.append(computed)
        if reductions:
            comp_avgs[comp] = sum(reductions) / len(reductions)
    pathway_score = within_tol / total_entries if total_entries > 0 else 0.0
    order_score = 0.0
    if len(comp_avgs) == 3:
        ordered = sorted(comp_avgs.items(), key=lambda x: x[1], reverse=True)
        actual_order = [item[0] for item in ordered]
        if actual_order == catalytic_order:
            order_score = 1.0
    final_score = pathway_score * 0.7 + order_score * 0.3
    return final_score


_SCORERS = {
    'enthalpy_struct': score_0,
    'mulliken_recomp': score_1,
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
