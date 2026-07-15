import os
import json
import csv

# === author imports / helpers ===
import json, os, re


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


# === block: score_0 (check id='phonon_stability') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    strains = gold.get('strains', [])
    expected = gold.get('expected_status', 'stable')
    lines = artifact.strip().splitlines()
    hits = 0
    for strain in strains:
        found = False
        for line in lines:
            if strain in line and expected in line:
                found = True
                break
        if found:
            hits += 1
    return hits / len(strains) if strains else 0.0


# === block: score_1 (check id='results_summary') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    top_gold = gold.get('top', {})
    press_gold = gold.get('pressure_results', {})
    # top-level fields
    top_scores = {}
    # lattice constant (exact_match with tolerance 0.01)
    val = artifact.get('lattice_constant_A')
    if isinstance(val, (int,float)):
        top_scores['lattice'] = 1.0 if abs(val - top_gold['lattice_constant_A']) <= 0.01 else 0.0
    else:
        top_scores['lattice'] = 0.0
    # bandgap no SOC
    val = artifact.get('bandgap_noSOC_eV')
    if isinstance(val, (int,float)):
        top_scores['bg_noSOC'] = 1.0 if abs(val - top_gold['bandgap_noSOC_eV']) <= 0.02 else 0.0
    else:
        top_scores['bg_noSOC'] = 0.0
    # bandgap SOC
    val = artifact.get('bandgap_SOC_eV')
    if isinstance(val, (int,float)):
        top_scores['bg_SOC'] = 1.0 if abs(val - top_gold['bandgap_SOC_eV']) <= 0.02 else 0.0
    else:
        top_scores['bg_SOC'] = 0.0
    # max Seebeck
    val = artifact.get('max_Seebeck_n900K_uVK')
    target_seeb = top_gold['max_Seebeck_n900K_uVK']
    if isinstance(val, (int,float)):
        if val <= target_seeb:
            top_scores['seebeck'] = 1.0
        else:
            diff = val - target_seeb
            tol = 0.1 * abs(target_seeb)
            top_scores['seebeck'] = max(0.0, 1.0 - diff / tol) if tol>0 else 0.0
    else:
        top_scores['seebeck'] = 0.0
    # optimal carrier concentration (factor 2)
    val = artifact.get('optimal_carrier_concentration_cm3')
    target_conc = top_gold['optimal_carrier_concentration_cm3']
    if isinstance(val, (int,float)):
        lo = target_conc / 2.0
        hi = target_conc * 2.0
        top_scores['opt_conc'] = 1.0 if lo <= val <= hi else 0.0
    else:
        top_scores['opt_conc'] = 0.0
    # ZT_e
    val = artifact.get('ZT_e_at_1e19_cm3')
    target_zt = top_gold['ZT_e_at_1e19_cm3']
    if isinstance(val, (int,float)):
        if val >= target_zt:
            top_scores['zt'] = 1.0
        else:
            diff = target_zt - val
            tol = 0.1 * target_zt
            top_scores['zt'] = max(0.0, 1.0 - diff / tol) if tol>0 else 0.0
    else:
        top_scores['zt'] = 0.0
    # weights for top-level group
    top_weights = {
        'lattice': 0.1, 'bg_noSOC': 0.1, 'bg_SOC': 0.1,
        'seebeck': 0.15, 'opt_conc': 0.05, 'zt': 0.15
    }
    top_overall = sum(top_scores[k]*top_weights.get(k,0) for k in top_scores)
    # pressure results
    press_list = artifact.get('pressure_results')
    if not isinstance(press_list, list):
        return top_overall  # no pressure points
    # index by strain
    press_by_strain = {}
    for entry in press_list:
        strain = str(entry.get('strain','')).strip()
        press_by_strain[strain] = entry
    strain_scores = []
    for strain, ref in press_gold.items():
        entry = press_by_strain.get(strain)
        if not isinstance(entry, dict):
            strain_scores.append(0.0)
            continue
        # bandgap
        bg_eV = entry.get('bandgap_eV')
        bg_score = 1.0 if isinstance(bg_eV, (int,float)) and abs(bg_eV - ref['bandgap_eV']) <= 0.02 else 0.0
        # bandgap type
        bg_type = str(entry.get('bandgap_type','')).strip().lower()
        bg_type_score = 1.0 if bg_type == ref['bandgap_type'].lower() else 0.0
        # Seebeck
        seeb = entry.get('Seebeck_n1e19_300K_uVK')
        target_seeb = ref['Seebeck_n1e19_300K_uVK']
        seeb_score = 0.0
        if isinstance(seeb, (int,float)):
            if seeb <= target_seeb:
                seeb_score = 1.0
            else:
                diff = seeb - target_seeb
                tol = 0.1 * abs(target_seeb)
                seeb_score = max(0.0, 1.0 - diff / tol) if tol>0 else 0.0
        # ZT_e
        zt = entry.get('ZT_e')
        target_zt = ref['ZT_e']
        zt_score = 0.0
        if isinstance(zt, (int,float)):
            if zt >= target_zt:
                zt_score = 1.0
            else:
                diff = target_zt - zt
                tol = 0.1 * target_zt
                zt_score = max(0.0, 1.0 - diff / tol) if tol>0 else 0.0
        # absorption null/value check
        abs_val = entry.get('absorption_307nm_cm1')
        target_abs = ref['absorption_307nm_cm1']
        if target_abs is None:
            abs_score = 1.0 if abs_val is None else 0.0
        else:
            abs_score = 1.0 if isinstance(abs_val, (int,float)) and abs_val > 0 else 0.0
        # strain sub-scores with weights
        strain_sub = (bg_score*0.25 + bg_type_score*0.2 + seeb_score*0.2 + zt_score*0.15 + abs_score*0.2)
        strain_scores.append(strain_sub)
    strain_mean = sum(strain_scores)/len(strain_scores) if strain_scores else 0.0
    # absorption trend
    abs0 = press_by_strain.get('0%', {}).get('absorption_307nm_cm1')
    abs4 = press_by_strain.get('4%', {}).get('absorption_307nm_cm1')
    trend_score = 0.0
    if isinstance(abs0, (int,float)) and isinstance(abs4, (int,float)) and abs4 > abs0:
        trend_score = 1.0
    pressure_overall = strain_mean * 0.9 + trend_score * 0.1
    # combine: top group weight 0.6, pressure weight 0.4
    return top_overall + pressure_overall * 0.4


_SCORERS = {
    'phonon_stability': score_0,
    'results_summary': score_1,
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
