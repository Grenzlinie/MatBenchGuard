import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='reconstruction_energies') ===
def score_0(artifact, step, ctx):
    expected = step["expected_energies"]
    tolerance = step.get("tolerance_energy", 0.1)
    ordering_required = step.get("ordering_required", [])
    materials = artifact.get("materials", [])
    if not isinstance(materials, list):
        return 0.0
    provided = {}
    for entry in materials:
        mat = entry.get("material", "")
        ct = entry.get("core_type", "")
        val = entry.get("reconstruction_energy_eV", None)
        if mat and ct and val is not None:
            provided[f"{mat}_{ct}"] = val
    total_expected = len(expected)
    if total_expected == 0:
        return 1.0
    score_energy = 0.0
    for key, gold in expected.items():
        if key in provided:
            diff = abs(provided[key] - gold)
            if diff <= tolerance:
                score_energy += 1.0
    score_energy /= total_expected
    ordering_score = 1.0
    if ordering_required:
        ordered = 0
        for pair in ordering_required:
            mat = pair["material"]
            alpha_key = f"{mat}_alpha"
            beta_key = f"{mat}_beta"
            if alpha_key in provided and beta_key in provided:
                if provided[alpha_key] < provided[beta_key]:
                    ordered += 1
            else:
                pass
        if len(ordering_required) > 0:
            ordering_score = ordered / len(ordering_required)
    ew = step.get("energy_weight", 0.8)
    ow = step.get("ordering_weight", 0.2)
    return ew * score_energy + ow * ordering_score


# === block: score_1 (check id='AlP_electronic_structure') ===
def score_1(artifact, step, ctx):
    expected = step["expected_values"]
    tolerances = step.get("tolerances", {})
    checks = 0
    passed = 0
    if "bulk_gap_eV" in artifact:
        val = artifact["bulk_gap_eV"]
        gold = expected.get("bulk_gap_eV", 1.04)
        tol = tolerances.get("bulk_gap_eV", 0.1)
        checks += 1
        if abs(val - gold) <= tol:
            passed += 1
    if "unreconstructed_beta_half_filled_band_present" in artifact:
        if artifact["unreconstructed_beta_half_filled_band_present"] == expected.get("unreconstructed_beta_half_filled_band_present", True):
            passed += 1
        checks += 1
    if "reconstructed_beta_bonding_antibonding_gap_eV" in artifact:
        val = artifact["reconstructed_beta_bonding_antibonding_gap_eV"]
        gold = expected.get("reconstructed_beta_bonding_antibonding_gap_eV", 0.15)
        tol = tolerances.get("reconstructed_beta_bonding_antibonding_gap_eV", 0.05)
        checks += 1
        if abs(val - gold) <= tol:
            passed += 1
    if "alpha_reconstructed_resonant_level_position_below_VBM_eV" in artifact:
        val = artifact["alpha_reconstructed_resonant_level_position_below_VBM_eV"]
        gold = expected.get("alpha_reconstructed_resonant_level_position_below_VBM_eV", 4.0)
        tol = tolerances.get("alpha_reconstructed_resonant_level_position_below_VBM_eV", 0.5)
        checks += 1
        if abs(val - gold) <= tol:
            passed += 1
    if checks == 0:
        return 0.0
    return passed / checks


_SCORERS = {
    'reconstruction_energies': score_0,
    'AlP_electronic_structure': score_1,
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
