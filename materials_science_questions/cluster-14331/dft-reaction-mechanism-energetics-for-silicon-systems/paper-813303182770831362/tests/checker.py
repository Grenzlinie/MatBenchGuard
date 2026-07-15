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


# === block: score_0 (check id='csv_check') ===
def score_0(artifact, step, ctx):
    params = step.get("params", {})
    gold_species = params.get("species_gold", [])
    rel_tol = params.get("relative_tolerance_kJmol", 4.0)
    consistency_tol = params.get("internal_consistency_tolerance_kJmol", 0.5)

    rows_by_species = {row["species"].strip(): row for row in artifact if "species" in row}

    required_cols = ["species", "total_energy_hartree", "relative_energy_kJmol", "reference"]
    schema_ok = all(all(col in row for col in required_cols) for row in artifact)
    schema_score = 1.0 if schema_ok else 0.0

    gold_names = set(g["species"] for g in gold_species)
    present_gold = [name for name in gold_names if name in rows_by_species]
    presence_score = len(present_gold) / len(gold_names) if gold_names else 1.0

    consistency_errors = []
    for name, row in rows_by_species.items():
        ref_name = row.get("reference", "").strip()
        if ref_name and ref_name in rows_by_species:
            ref_total = float(rows_by_species[ref_name]["total_energy_hartree"])
            species_total = float(row["total_energy_hartree"])
            delta_kj = (species_total - ref_total) * 2625.5
            reported_delta = float(row["relative_energy_kJmol"])
            if abs(delta_kj - reported_delta) > consistency_tol:
                consistency_errors.append(name)

    consistency_score = 1.0 - len(consistency_errors) / max(len(rows_by_species), 1)

    accurate = 0
    for g in gold_species:
        name = g["species"]
        if name in rows_by_species:
            row = rows_by_species[name]
            ref_name = row.get("reference", "").strip()
            if ref_name in rows_by_species:
                ref_total = float(rows_by_species[ref_name]["total_energy_hartree"])
                species_total = float(row["total_energy_hartree"])
                delta_kj = (species_total - ref_total) * 2625.5
                if abs(delta_kj - g["relative_energy_kJmol"]) <= rel_tol:
                    accurate += 1
    accuracy_score = accurate / len(present_gold) if present_gold else 0.0

    total = 0.1 * schema_score + 0.2 * presence_score + 0.3 * consistency_score + 0.4 * accuracy_score
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='json_check') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    gold_barriers = params.get("gold_barriers", [])
    tolerance = params.get("tolerance_kJmol", 4.0)

    if not isinstance(artifact, list):
        return 0.0

    artifact_by_channel = {}
    for entry in artifact:
        if isinstance(entry, dict) and "channel" in entry:
            artifact_by_channel[entry["channel"]] = entry

    total_channels = len(gold_barriers)
    if total_channels == 0:
        return 1.0

    match = 0
    for g in gold_barriers:
        chan = g["channel"]
        entry = artifact_by_channel.get(chan)
        if entry is None:
            continue
        barrier_ok = abs(entry.get("barrier_kJmol", 0) - g["barrier_kJmol"]) <= tolerance
        exo_ok = abs(entry.get("exothermicity_kJmol", 0) - g["exothermicity_kJmol"]) <= tolerance
        if barrier_ok and exo_ok:
            match += 1

    return match / total_channels


_SCORERS = {
    'csv_check': score_0,
    'json_check': score_1,
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
