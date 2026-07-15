import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    ref_list = spec.get("reference_configurations", [])
    ref_by_pos = {}
    for item in ref_list:
        positions = tuple(sorted(item["iron_positions"].split(",")))
        ref_by_pos[positions] = {
            "iron_positions": item["iron_positions"],
            "degeneracy": item["degeneracy"],
            "space_group": item["space_group"],
            "relative_energy": item["relative_energy"],
        }
    ref_ordered = sorted(ref_list, key=lambda x: x["relative_energy"])
    ref_rank = {}
    for idx, item in enumerate(ref_ordered):
        pos_tuple = tuple(sorted(item["iron_positions"].split(",")))
        ref_rank[pos_tuple] = idx
    return {
        "ref_by_pos": ref_by_pos,
        "ref_rank": ref_rank,
        "ref_ordered": ref_ordered,
    }


# === block: score_0 (check id='config_match') ===
def score_0(artifact, step, ctx):
    if len(artifact) != 29:
        return 0.0
    ref_by_pos = ctx["ref_by_pos"]

    def _normalize_sg(s):
        return s.strip().replace(" ", "")

    correct = 0
    for row in artifact:
        pos_str = row["iron_positions"].strip()
        positions = tuple(sorted([p.strip() for p in pos_str.split(",") if p.strip()]))
        ref = ref_by_pos.get(positions)
        if ref is not None:
            agent_sg = _normalize_sg(str(row.get("space_group", "")))
            ref_sg = _normalize_sg(ref["space_group"])
            if str(row.get("degeneracy")) == str(ref["degeneracy"]) and agent_sg == ref_sg:
                correct += 1
    return correct / 29.0


# === block: score_1 (check id='energy_tolerance') ===
def score_1(artifact, step, ctx):
    if len(artifact) != 29:
        return 0.0
    ref_by_pos = ctx["ref_by_pos"]
    within_tol = 0
    for row in artifact:
        pos_str = row["iron_positions"].strip()
        positions = tuple(sorted([p.strip() for p in pos_str.split(",") if p.strip()]))
        ref = ref_by_pos.get(positions)
        if ref is not None:
            agent_energy = float(row["relative_energy_kJ_per_mol"])
            ref_energy = ref["relative_energy"]
            if abs(agent_energy - ref_energy) <= 10.0:
                within_tol += 1
    return within_tol / 29.0


# === block: score_2 (check id='energy_ordering') ===
def score_2(artifact, step, ctx):
    if len(artifact) != 29:
        return 0.0
    ref_by_pos = ctx["ref_by_pos"]
    ref_ordered = ctx["ref_ordered"]
    agent_energy = {}
    for row in artifact:
        pos_str = row["iron_positions"].strip()
        positions = tuple(sorted([p.strip() for p in pos_str.split(",") if p.strip()]))
        if positions in ref_by_pos:
            agent_energy[positions] = float(row["relative_energy_kJ_per_mol"])
    if len(agent_energy) != 29:
        return 0.0
    correct = 0
    total = 0
    ref_positions_list = [tuple(sorted(item["iron_positions"].split(","))) for item in ref_ordered]
    for i in range(len(ref_positions_list)):
        for j in range(i+1, len(ref_positions_list)):
            pos_i = ref_positions_list[i]
            pos_j = ref_positions_list[j]
            if pos_i not in agent_energy or pos_j not in agent_energy:
                continue
            if agent_energy[pos_i] <= agent_energy[pos_j]:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='lowest_energy_config') ===
def score_3(artifact, step, ctx):
    if len(artifact) < 1:
        return 0.0
    target_positions = tuple(sorted(["L1", "L4", "L7", "L10"]))
    min_energy = None
    min_row = None
    for row in artifact:
        energy = float(row["relative_energy_kJ_per_mol"])
        if min_energy is None or energy < min_energy:
            min_energy = energy
            min_row = row
    if min_row is None:
        return 0.0
    pos_str = min_row["iron_positions"].strip()
    positions = tuple(sorted([p.strip() for p in pos_str.split(",") if p.strip()]))
    if positions == target_positions and abs(min_energy) <= 0.001:
        for row in artifact:
            if float(row["relative_energy_kJ_per_mol"]) < min_energy - 1e-6:
                return 0.0
        return 1.0
    return 0.0


_SCORERS = {
    'config_match': score_0,
    'energy_tolerance': score_1,
    'energy_ordering': score_2,
    'lowest_energy_config': score_3,
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
