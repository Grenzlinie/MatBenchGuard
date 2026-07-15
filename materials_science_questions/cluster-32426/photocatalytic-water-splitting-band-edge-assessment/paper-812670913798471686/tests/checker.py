import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='schema_check') ===
def score_0(artifact, step, ctx):
    import json

    def check_schema(data, schema):
        if not isinstance(data, dict):
            return False
        required = schema.get('required', [])
        if not all(f in data for f in required):
            return False
        props = schema.get('properties', {})
        for key, subschema in props.items():
            if key in data:
                if subschema.get('type') == 'object':
                    if not check_schema(data[key], subschema):
                        return False
                elif subschema.get('type') == 'array':
                    if not isinstance(data[key], list):
                        return False
                    for item in data[key]:
                        if not check_schema(item, subschema.get('items', {})):
                            return False
                elif subschema.get('type') == 'number':
                    if not isinstance(data[key], (int, float)):
                        return False
                elif subschema.get('type') == 'string':
                    if not isinstance(data[key], str):
                        return False
        return True

    output_contract = step.get('_output_contract', {})
    outputs = output_contract.get('outputs', [])
    if not outputs:
        return 0.0
    schema = outputs[0].get('schema', {})
    if not check_schema(artifact, schema):
        return 0.0

    # Water-splitting band-edge alignment: CBM > H⁺/H₂ reduction potential (−4.44 eV)
    # and VBM < O₂/H₂O oxidation potential (−5.67 eV) at pH 0.
    for het in ('mo_sse_gaN', 'mo_sse_alN'):
        data = artifact.get(het, {})
        cbm = data.get('cbm_vs_vacuum_eV')
        vbm = data.get('vbm_vs_vacuum_eV')
        if cbm is None or vbm is None:
            return 0.0
        if not (cbm > -4.44 and vbm < -5.67):
            return 0.0
    return 1.0


# === block: score_1 (check id='structural') ===
def score_1(artifact, step, ctx):
    def score_field(reported, gold, tol):
        if reported is None:
            return 0.0
        if abs(reported - gold) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(reported - gold) - tol) / (2 * tol))

    gold_dict = step['gold']
    tols = step['tolerances']
    score = 0.0
    count = 0
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        data = artifact.get(het, {})
        gold_het = gold_dict.get(het, {})
        for field, tol in tols.items():
            g = gold_het.get(field)
            if g is not None and field in data:
                v = data[field]
                score += score_field(v, g, tol)
                count += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_2 (check id='electronic') ===
def score_2(artifact, step, ctx):
    def score_field(reported, gold, tol):
        if reported is None:
            return 0.0
        if abs(reported - gold) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(reported - gold) - tol) / (2 * tol))

    gold_dict = step['gold']
    tols = step['tolerances']
    score = 0.0
    count = 0
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        data = artifact.get(het, {})
        gold_het = gold_dict.get(het, {})
        for field, tol in tols.items():
            g = gold_het.get(field)
            if g is not None and field in data:
                v = data[field]
                score += score_field(v, g, tol)
                count += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_3 (check id='mobility') ===
def score_3(artifact, step, ctx):
    gold_list = step['gold']
    tols = step['tolerances']

    # scoring helpers
    def closeness(v, g, tol):
        if v is None or g is None:
            return 0.0
        if abs(v - g) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(v - g) - tol) / (2 * tol))

    def mobility_score(v, g, tol_pct):
        if g is None or v is None:
            return 0.0
        # threshold_or_better: larger is better
        tol_abs = abs(g) * tol_pct
        if v >= g - tol_abs:
            return 1.0
        return max(0.0, 1.0 - (g - v) / (0.3 * abs(g)))

    scores = []
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        mob_list = artifact.get(het, {}).get('carrier_mobilities', [])
        gold_mob_list = gold_list.get(het, [])
        # index by direction+carrier_type
        reported_map = {}
        for entry in mob_list:
            key = (entry.get('direction',''), entry.get('carrier_type',''))
            reported_map[key] = entry

        for g_entry in gold_mob_list:
            key = (g_entry['direction'], g_entry['carrier_type'])
            repl = reported_map.get(key)
            if not repl:
                scores.append(0.0)
                continue
            eff = closeness(repl.get('effective_mass'), g_entry['effective_mass'], tols.get('effective_mass', 0.1))
            defpot = closeness(repl.get('deformation_potential_eV'), g_entry['deformation_potential_eV'], tols.get('deformation_potential_eV', 0.5))
            elast = closeness(repl.get('elastic_modulus_N_per_m'), g_entry['elastic_modulus_N_per_m'], tols.get('elastic_modulus_N_per_m', 5.0))
            mob = mobility_score(repl.get('mobility_cm2_V_s'), g_entry['mobility_cm2_V_s'], tols.get('mobility_tol_pct', 0.1))
            # average sub-scores per entry
            scores.append((eff + defpot + elast + mob) / 4.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='interfacial') ===
def score_4(artifact, step, ctx):
    def score_field(reported, gold, tol):
        if reported is None or gold is None:
            return 0.0
        if abs(reported - gold) <= tol:
            return 1.0
        return max(0.0, 1.0 - (abs(reported - gold) - tol) / (2 * tol))

    gold_dict = step['gold']
    tols = step['tolerances']
    score = 0.0
    count = 0
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        data = artifact.get(het, {})
        gold_het = gold_dict.get(het, {})
        for field, tol in tols.items():
            g = gold_het.get(field)
            if g is not None and field in data:
                v = data[field]
                score += score_field(v, g, tol)
                count += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_5 (check id='optical') ===
def score_5(artifact, step, ctx):
    gold_dict = step['gold']
    tols = step['tolerances']
    wavelength_tol = tols.get('wavelength_nm', 10)
    coeff_pct = tols.get('absorption_coefficient_pct', 0.2)

    def peak_match(gold_peaks, reported_peaks):
        if not gold_peaks or not reported_peaks:
            return 0.0
        score = 0.0
        for gp in gold_peaks:
            wl_g = gp['wavelength_nm']
            coeff_g = gp['absorption_coefficient_cm1']
            best = 0.0
            for rp in reported_peaks:
                if abs(rp.get('wavelength_nm', 0) - wl_g) > wavelength_tol:
                    continue
                if coeff_g == 0:
                    continue
                coeff_r = rp.get('absorption_coefficient_cm1', 0)
                rel_err = abs(coeff_r - coeff_g) / abs(coeff_g)
                if rel_err <= coeff_pct:
                    peak_score = 1.0
                else:
                    peak_score = max(0.0, 1.0 - (rel_err - coeff_pct) / (2 * coeff_pct))
                best = max(best, peak_score)
            score += best
        return score / len(gold_peaks)

    total = 0.0
    count = 0
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        data = artifact.get(het, {})
        gold_peaks = gold_dict.get(het, [])
        reported_peaks = data.get('optical_absorption_peaks', [])
        if gold_peaks:
            total += peak_match(gold_peaks, reported_peaks)
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_6 (check id='consistency_mobility') ===
def score_6(artifact, step, ctx):
    import math

    tol = step.get('tolerances', {}).get('mobility_rel_error', 0.05)

    # Bardeen-Shockley 2D mobility formula: mu = e * hbar^3 * C / (k_B * T * m^*_e * m_d * E1^2)
    # constants SI
    hbar = 1.054571817e-34  # J*s
    e_charge = 1.602176634e-19  # C
    k_B = 1.380649e-23  # J/K
    T = 300.0
    m_e = 9.10938356e-31  # kg

    factor = e_charge * (hbar ** 3) / (k_B * T)  # SI

    # build effective mass lookup per heterostructure: direction -> m*
    def get_effective_masses(mob_list):
        result = {}
        for entry in mob_list:
            direction = entry.get('direction')
            if direction not in result:
                result[direction] = {}
            carrier = entry.get('carrier_type')
            m = entry.get('effective_mass', None)
            if m is not None:
                result[direction][carrier] = abs(m)  # use absolute, mass sign not used
        return result

    score = 0.0
    count = 0
    for het in ['mo_sse_gaN', 'mo_sse_alN']:
        mob_list = artifact.get(het, {}).get('carrier_mobilities', [])
        if not mob_list:
            continue
        masses = get_effective_masses(mob_list)
        # directions needed
        dirs = sorted(set(e['direction'] for e in mob_list))
        if len(dirs) < 2:
            # need both armchair and zigzag
            continue
        # for each entry compute expected mobility
        for entry in mob_list:
            direction = entry.get('direction')
            carrier = entry.get('carrier_type')
            m_star = entry.get('effective_mass')
            if m_star is None:
                continue
            m_star_abs = abs(m_star)
            C = entry.get('elastic_modulus_N_per_m')
            E1 = entry.get('deformation_potential_eV')
            reported_mu = entry.get('mobility_cm2_V_s')
            if C is None or E1 is None or reported_mu is None:
                continue
            # need the other direction mass for m_d = sqrt(m_x * m_y)
            other_dir = [d for d in dirs if d != direction][0]
            other_mass = masses.get(other_dir, {}).get(carrier)
            if other_mass is None:
                continue
            m_d = math.sqrt(m_star_abs * other_mass)  # use abs
            # E1 in J: eV -> J
            E1_J = abs(E1) * e_charge
            # mobility in SI units (m^2/(V*s))
            mu_SI = factor * C / (m_e * m_e * m_star_abs * m_d * (E1_J ** 2))
            # convert to cm^2/(V*s)
            expected_mu = mu_SI * 1e4
            if expected_mu == 0:
                continue
            rel_err = abs(reported_mu - expected_mu) / expected_mu
            entry_score = 1.0 if rel_err <= tol else max(0.0, 1.0 - (rel_err - tol) / (2 * tol))
            score += entry_score
            count += 1

    if count == 0:
        return 0.0
    return score / count


_SCORERS = {
    'schema_check': score_0,
    'structural': score_1,
    'electronic': score_2,
    'mobility': score_3,
    'interfacial': score_4,
    'optical': score_5,
    'consistency_mobility': score_6,
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
