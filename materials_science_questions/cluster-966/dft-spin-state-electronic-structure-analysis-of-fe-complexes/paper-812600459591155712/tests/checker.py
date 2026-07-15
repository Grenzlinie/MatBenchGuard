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


# === block: score_0 (check id='dft_results') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step['reference']
        tol = step['tolerances']
        w = step['scoring_weights']

        ref_Fe2_bl = ref['Fe2+']['bond_lengths']
        ref_Fe3_bl = ref['Fe3+']['bond_lengths']
        art_Fe2 = artifact.get('Fe2+', {})
        art_Fe3 = artifact.get('Fe3+', {})
        art_Fe2_bl = art_Fe2.get('bond_lengths', {})
        art_Fe3_bl = art_Fe3.get('bond_lengths', {})

        # bond length tolerance score
        passed = 0.0
        for key in ref_Fe2_bl:
            if key in art_Fe2_bl and abs(art_Fe2_bl[key] - ref_Fe2_bl[key]) <= tol['bond_length_abs']:
                passed += 1
        for key in ref_Fe3_bl:
            if key in art_Fe3_bl and abs(art_Fe3_bl[key] - ref_Fe3_bl[key]) <= tol['bond_length_abs']:
                passed += 1
        bl_tol_score = (passed / 12.0) * w['bond_length_tolerance']

        # bond length trend: Fe3+ < Fe2+ for each bond
        trend_passed = 0.0
        for key in ref_Fe2_bl:
            val2 = art_Fe2_bl.get(key)
            val3 = art_Fe3_bl.get(key)
            if val2 is not None and val3 is not None and val3 < val2:
                trend_passed += 1
        bl_trend_score = (trend_passed / 6.0) * w['bond_length_trend']

        # binding energy tolerance
        be_Fe2_ref = ref['Fe2+']['binding_energy_kcal_mol']
        be_Fe3_ref = ref['Fe3+']['binding_energy_kcal_mol']
        be_Fe2_art = art_Fe2.get('binding_energy_kcal_mol')
        be_Fe3_art = art_Fe3.get('binding_energy_kcal_mol')
        be_tol = tol['binding_energy_abs_tol']
        be_tol_score = 0.0
        if be_Fe2_art is not None and abs(be_Fe2_art - be_Fe2_ref) <= be_tol:
            be_tol_score += 0.5
        if be_Fe3_art is not None and abs(be_Fe3_art - be_Fe3_ref) <= be_tol:
            be_tol_score += 0.5
        be_tol_score *= w['binding_energy_tolerance']

        # binding energy trend: Fe3+ < Fe2+
        be_trend_score = 0.0
        if be_Fe2_art is not None and be_Fe3_art is not None and be_Fe3_art < be_Fe2_art:
            be_trend_score = w['binding_energy_trend']

        # solvation energy tolerance
        se_Fe2_ref = ref['Fe2+']['solvation_energy_kcal_mol']
        se_Fe3_ref = ref['Fe3+']['solvation_energy_kcal_mol']
        se_Fe2_art = art_Fe2.get('solvation_energy_kcal_mol')
        se_Fe3_art = art_Fe3.get('solvation_energy_kcal_mol')
        se_tol = tol['solvation_energy_abs_tol']
        se_tol_score = 0.0
        if se_Fe2_art is not None and abs(se_Fe2_art - se_Fe2_ref) <= se_tol:
            se_tol_score += 0.5
        if se_Fe3_art is not None and abs(se_Fe3_art - se_Fe3_ref) <= se_tol:
            se_tol_score += 0.5
        se_tol_score *= w['solvation_energy_tolerance']

        # solvation trend: Fe3+ < Fe2+
        se_trend_score = 0.0
        if se_Fe2_art is not None and se_Fe3_art is not None and se_Fe3_art < se_Fe2_art:
            se_trend_score = w['solvation_energy_trend']

        return bl_tol_score + bl_trend_score + be_tol_score + be_trend_score + se_tol_score + se_trend_score


_SCORERS = {
    'dft_results': score_0,
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
