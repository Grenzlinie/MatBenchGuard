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
    return {
        "gold": spec.get("gold", {}),
        "tolerances": spec.get("tolerances", {})
    }


# === block: score_0 (check id='computed_results') ===
def score_0(artifact, step, ctx):
    artifact_data = artifact  # already parsed json
    gold = ctx["gold"]
    tols = ctx["tolerances"]

    def score_field_float(value, expected, rel_tol):
        if rel_tol is None:
            return 0.0
        return max(0.0, 1.0 - abs(value - expected) / (rel_tol * abs(expected) + 1e-9))

    def score_field_abs(value, expected, abs_tol):
        if abs_tol is None:
            return 0.0
        return 1.0 if abs(value - expected) <= abs_tol else 0.0

    def score_array_floats(values, expected_list, abs_tol):
        if not isinstance(values, list) or len(values) != len(expected_list):
            return 0.0
        scores = []
        for v, e in zip(values, expected_list):
            if not isinstance(v, (int, float)):
                scores.append(0.0)
            else:
                scores.append(score_field_abs(v, e, abs_tol))
        return sum(scores) / len(scores)

    def score_string_array(values, expected_set):
        if not isinstance(values, list):
            return 0.0
        return 1.0 if set(values) == set(expected_set) else 0.0

    scores = []
    for species_key in ["species1", "species2"]:
        gold_sp = gold.get(species_key, {})
        sp = artifact_data.get(species_key, {})
        if not sp or not gold_sp:
            continue
        # Bond lengths (absolute tolerance)
        for field in ["Fe_N_nacnac", "Fe_N_NO", "N_O"]:
            if field in sp and field in gold_sp:
                scores.append(score_array_floats(sp[field], gold_sp[field], tols.get("bond_length_abs_A")))
        # Mössbauer (absolute)
        for field in ["delta_mm_per_s", "DeltaEQ_mm_per_s"]:
            if field in sp and field in gold_sp:
                scores.append(score_field_abs(sp[field], gold_sp[field], tols.get("mossbauer_abs_mm_per_s")))
        # NO frequencies (relative)
        for field in ["v_NO_sym_cm-1", "v_NO_asym_cm-1"]:
            if field in sp and field in gold_sp:
                scores.append(score_field_float(sp[field], gold_sp[field], tols.get("v_NO_rel")))
        # Spin population (absolute)
        if "Fe_spin_population" in sp and "Fe_spin_population" in gold_sp:
            scores.append(score_field_abs(sp["Fe_spin_population"], gold_sp["Fe_spin_population"], tols.get("spin_population_abs")))
        if "NO_spin_populations" in sp and "NO_spin_populations" in gold_sp:
            scores.append(score_array_floats(sp["NO_spin_populations"], gold_sp["NO_spin_populations"], tols.get("spin_population_abs")))
        # Overlap (absolute)
        if "orbital_overlap_S" in sp and "orbital_overlap_S" in gold_sp:
            scores.append(score_field_abs(sp["orbital_overlap_S"], gold_sp["orbital_overlap_S"], tols.get("overlap_S_abs")))
        # Spin state strings (exact set)
        if "Fe_S_values" in sp and "Fe_S_values_set" in gold_sp:
            scores.append(score_string_array(sp["Fe_S_values"], gold_sp["Fe_S_values_set"]))
        # Integer occupation counts (exact)
        for field in ["num_singly_occupied_Fe_d_orbitals", "num_singly_occupied_NO_pi_orbitals"]:
            if field in sp and field in gold_sp:
                scores.append(1.0 if sp[field] == gold_sp[field] else 0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'computed_results': score_0,
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
