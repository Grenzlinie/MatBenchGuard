import os
import json
import csv

# === author imports / helpers ===
import os, json
try:
    import numpy as np
except ImportError:
    np = None


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
    steps = spec.get('steps', spec.get('checks', []))
    return {'steps': steps}


# === block: score_0 (check id='step_3') ===
def score_0(artifact, step, ctx):
    artifact = load_artifact(os.path.join('/app/outputs', 'band_structure_results.json'))
    if artifact is None:
        return 0.0

    # recompute raw band gap from band_energies
    band_energies = artifact.get('band_energies')
    if not isinstance(band_energies, list) or len(band_energies) == 0:
        return 0.0

    all_vals = []
    for kpt_vals in band_energies:
        all_vals.extend(kpt_vals)
    all_vals = np.array(all_vals)
    fermi = artifact.get('fermi_energy', 0.0)

    valence_max = np.max(all_vals[all_vals <= fermi]) if np.any(all_vals <= fermi) else -np.inf
    conduction_min = np.min(all_vals[all_vals > fermi]) if np.any(all_vals > fermi) else np.inf

    if np.isinf(valence_max) or np.isinf(conduction_min):
        return 0.0

    recomputed_gap = float(conduction_min - valence_max)

    # hidden reference
    ref_gap = float(step.get('hidden_raw_gap_ref', 3.06))
    tol = float(step.get('raw_gap_tolerance', 0.3))

    # gap score (symmetric tolerance, partial credit)
    diff = abs(recomputed_gap - ref_gap)
    if diff <= tol:
        gap_score = 1.0
    else:
        gap_score = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))

    # VBM/CBM label & coordinate check
    vbm = artifact.get('vbm_kpoint')
    cbm = artifact.get('cbm_kpoint')
    gap_type = artifact.get('gap_type')

    def check_kpoint(kp, expected_label, expected_coords):
        if not isinstance(kp, dict):
            return 0.0
        label = str(kp.get('label', ''))
        coords = kp.get('coordinates')
        label_ok = (label == expected_label)
        coord_ok = False
        if isinstance(coords, list) and len(coords) == 3:
            coord_ok = np.allclose(coords, expected_coords, atol=0.1)
        if label_ok and coord_ok:
            return 1.0
        if label_ok:
            return 0.75
        if coord_ok:
            return 0.3
        return 0.0

    label_score = 0.0
    if vbm is not None and cbm is not None:
        vbm_s = check_kpoint(vbm, 'G', [0.0, 0.0, 0.0])
        cbm_s = check_kpoint(cbm, 'F', [0.0, 0.5, 0.0])
        # average of the two k-point checks
        label_score = 0.5 * vbm_s + 0.5 * cbm_s
        # if gap_type is not 'direct', penalise slightly
        if gap_type != 'direct':
            label_score = min(label_score, 0.5)

    # scissor shift consistency
    scissor_shift = artifact.get('scissor_shift_applied')
    adjusted_gap = artifact.get('adjusted_band_gap')
    scissor_ok = False
    if isinstance(scissor_shift, (int, float)) and abs(float(scissor_shift) - 0.45) < 1e-5:
        if isinstance(adjusted_gap, (int, float)):
            expected_adjusted = recomputed_gap + 0.45
            if abs(float(adjusted_gap) - expected_adjusted) < 0.01:
                scissor_ok = True

    scissor_score = 1.0 if scissor_ok else 0.0

    # Combine
    score = 0.5 * gap_score + 0.3 * label_score + 0.2 * scissor_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_4') ===
def score_1(artifact, step, ctx):
    artifact = load_artifact(os.path.join('/app/outputs', 'pdos_summary.json'))
    if artifact is None:
        return 0.0

    thresholds = step.get('thresholds', {})
    val_thr = thresholds.get('valence', {})
    cond_thr = thresholds.get('conduction', {})

    valence_list = artifact.get('valence_band_top_contributions')
    conduction_list = artifact.get('conduction_band_bottom_contributions')
    if not isinstance(valence_list, list) or not isinstance(conduction_list, list):
        return 0.0
    if len(valence_list) != 3 or len(conduction_list) != 3:
        return 0.0

    def contributions_sum_to_one(band):
        contribs = band.get('contributions')
        if not isinstance(contribs, dict):
            return False
        total = 0.0
        for species in ['Cd', 'adc', '4-phpy', 'water']:
            sp = contribs.get(species, {})
            if not isinstance(sp, dict):
                return False
            for orb in ['s', 'p', 'd']:
                total += float(sp.get(orb, 0.0))
        return abs(total - 1.0) < 0.02

    def score_valence_band(band):
        if not contributions_sum_to_one(band):
            return 0.0
        contribs = band['contributions']
        Cd_d = float(contribs.get('Cd', {}).get('d', 0.0))
        adc_p = float(contribs.get('adc', {}).get('p', 0.0))
        water_p = float(contribs.get('water', {}).get('p', 0.0))
        adc_water_p = adc_p + water_p

        Cd_d_max = val_thr.get('Cd_d_max', 0.15)
        adc_water_p_min = val_thr.get('adc_water_p_min', 0.5)

        score = 0.0
        if Cd_d <= Cd_d_max:
            score += 0.5
        if adc_water_p >= adc_water_p_min:
            score += 0.5
        return score

    def score_conduction_band(band):
        if not contributions_sum_to_one(band):
            return 0.0
        contribs = band['contributions']
        p_phpy = float(contribs.get('4-phpy', {}).get('p', 0.0))
        p_min = cond_thr.get('four_phpy_p_min', 0.4)
        if p_phpy >= p_min:
            return 1.0
        elif p_phpy >= p_min * 0.5:
            return 0.5
        else:
            return 0.0

    valence_scores = [score_valence_band(b) for b in valence_list]
    conduction_scores = [score_conduction_band(b) for b in conduction_list]

    val_avg = float(np.mean(valence_scores)) if valence_scores else 0.0
    cond_avg = float(np.mean(conduction_scores)) if conduction_scores else 0.0

    score = 0.5 * val_avg + 0.5 * cond_avg
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_3': score_0,
    'step_4': score_1,
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
