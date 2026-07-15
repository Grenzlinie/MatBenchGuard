import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='global_minimum_energies') ===
def score_0(artifact, step, ctx):
    gold_table = step["target"]["energies"]
    gold_dict = {e["n"]: e for e in gold_table}
    n_list = list(range(1,22))
    scores = []
    for n in n_list:
        row = next((r for r in artifact if int(r["n"]) == n), None)
        if row is None:
            scores.append(0.0)
            continue
        gold = gold_dict[n]
        assoc_val = float(row["association_energy_kJ_per_mol"])
        binding_val = float(row["binding_energy_kJ_per_mol"])
        V_dr_val = float(row["V_dr_kJ_per_mol"])
        V_pol_val = float(row["V_pol_kJ_per_mol"])
        assoc_ok = abs(assoc_val - gold["assoc"]) <= gold["assoc_tol"]
        binding_ok = abs(binding_val - gold["binding"]) <= gold["binding_tol"]
        # Per-water V_dr average ~7.26 kJ/mol, slowly growing with n.
        dr_center = 7.26 + 0.05 * (n - 1)
        dr_tol = 1.5
        V_dr_ok = abs(V_dr_val - dr_center) <= dr_tol
        V_pol_ok = gold["V_pol_min"] <= V_pol_val <= gold["V_pol_max"]
        row_score = sum([assoc_ok, binding_ok, V_dr_ok, V_pol_ok]) / 4.0
        scores.append(row_score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='monomer_orientation') ===
def score_1(artifact, step, ctx):
    content = artifact
    angle_match = re.search(r'angle_C2_to_z\s*=\s*([\d.]+)', content)
    dist_match = re.search(r'O_distance\s*=\s*([\d.]+)', content)
    if not angle_match or not dist_match:
        return 0.0
    angle = float(angle_match.group(1))
    dist = float(dist_match.group(1))
    angle_tol = step["target"]["angle_tol"]
    angle_gold = step["target"]["angle_deg"]
    dist_tol = step["target"]["distance_tol"]
    dist_gold = step["target"]["O_distance_A"]
    angle_ok = abs(angle - angle_gold) <= angle_tol
    dist_ok = abs(dist - dist_gold) <= dist_tol
    return 1.0 if angle_ok and dist_ok else 0.0


_SCORERS = {
    'global_minimum_energies': score_0,
    'monomer_orientation': score_1,
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
