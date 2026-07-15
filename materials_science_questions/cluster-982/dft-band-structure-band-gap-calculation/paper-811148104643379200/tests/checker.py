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


# === block: score_0 (check id='dielectric_nb3o7oh') ===
def score_0(artifact, step, ctx):
    import csv, math
    rows = list(csv.DictReader(open('/app/outputs/dielectric_function_Nb3O7OH.csv')))
    if len(rows) < 2:
        return 0.0
    # static epsilon1 from first data point (energy near 0)
    first = rows[0]
    eps1_perp = float(first['epsilon1_perp'])
    eps1_par = float(first['epsilon1_par'])
    # thresholds
    thresh_perp = None
    thresh_par = None
    lo, hi = step['threshold_search_energy_range']
    for r in rows:
        e = float(r['Energy(eV)'])
        if e < lo - 0.01:
            continue
        if e > hi + 0.01:
            break
        if thresh_perp is None and float(r['epsilon2_perp']) > step['epsilon2_threshold_crossing']:
            thresh_perp = e
        if thresh_par is None and float(r['epsilon2_par']) > step['epsilon2_threshold_crossing']:
            thresh_par = e
        if thresh_perp is not None and thresh_par is not None:
            break

    def sub_score(actual, gold, tol, base=0.25):
        if actual is None:
            return 0.0
        err = abs(actual - gold)
        if err <= tol:
            return base
        return base * max(0.0, 1.0 - (err - tol) / tol)
    score = 0.0
    score += sub_score(eps1_perp, step['gold_static_epsilon1_perp'], step['tolerance_static'])
    score += sub_score(eps1_par, step['gold_static_epsilon1_par'], step['tolerance_static'])
    score += sub_score(thresh_perp, step['gold_threshold_perp_eV'], step['tolerance_threshold_eV'])
    score += sub_score(thresh_par, step['gold_threshold_par_eV'], step['tolerance_threshold_eV'])
    return min(score, 1.0)


# === block: score_1 (check id='dielectric_hnb2o5') ===
def score_1(artifact, step, ctx):
    import csv, math
    rows = list(csv.DictReader(open('/app/outputs/dielectric_function_HNb2O5.csv')))
    if len(rows) < 2:
        return 0.0
    first = rows[0]
    eps1_perp = float(first['epsilon1_perp'])
    eps1_par = float(first['epsilon1_par'])
    thresh_perp = None
    thresh_par = None
    lo, hi = step['threshold_search_energy_range']
    for r in rows:
        e = float(r['Energy(eV)'])
        if e < lo - 0.01:
            continue
        if e > hi + 0.01:
            break
        if thresh_perp is None and float(r['epsilon2_perp']) > step['epsilon2_threshold_crossing']:
            thresh_perp = e
        if thresh_par is None and float(r['epsilon2_par']) > step['epsilon2_threshold_crossing']:
            thresh_par = e
        if thresh_perp is not None and thresh_par is not None:
            break

    def sub_score(actual, gold, tol, base=0.25):
        if actual is None:
            return 0.0
        err = abs(actual - gold)
        if err <= tol:
            return base
        return base * max(0.0, 1.0 - (err - tol) / tol)
    score = 0.0
    score += sub_score(eps1_perp, step['gold_static_epsilon1_perp'], step['tolerance_static'])
    score += sub_score(eps1_par, step['gold_static_epsilon1_par'], step['tolerance_static'])
    score += sub_score(thresh_perp, step['gold_threshold_perp_eV'], step['tolerance_threshold_eV'])
    score += sub_score(thresh_par, step['gold_threshold_par_eV'], step['tolerance_threshold_eV'])
    return min(score, 1.0)


# === block: score_2 (check id='oconduct_nb3o7oh') ===
def score_2(artifact, step, ctx):
    import csv, math
    rows = list(csv.DictReader(open('/app/outputs/optical_conductivity_Nb3O7OH.csv')))
    if len(rows) < 2:
        return 0.0

    data = []
    for r in rows:
        e = float(r['Energy(eV)'])
        sp = float(r['sigma_perp'])
        spar = float(r['sigma_par'])
        data.append((e, sp, spar))

    def find_peak(data, channel_idx, window):
        low, high = window
        best_e = None
        best_val = -1.0
        for e, sp, spar in data:
            if e < low - 0.01 or e > high + 0.01:
                continue
            val = sp if channel_idx == 0 else spar
            if val > best_val:
                best_val = val
                best_e = e
        return best_e, best_val

    peaks = step['peaks']
    tol_e = step['tolerance_energy_eV']
    tol_s = step['tolerance_sigma_relative']
    total_peaks = 0
    score = 0.0
    for ch, pklist in [('perp', 0), ('par', 1)]:
        ch_idx = 0 if ch == 'perp' else 1
        for pk in peaks[ch]:
            e_found, s_found = find_peak(data, ch_idx, pk['energy_window'])
            if e_found is None:
                continue
            total_peaks += 1
            gold_e = pk['gold_energy_eV']
            gold_s = pk['gold_sigma']
            # energy score weight 0.5, sigma score weight 0.5 (base 0.25 per peak? Actually 4 peaks total, each base 0.25)
            # We'll compute sub for energy and sigma with base=0.125 each
            err_e = abs(e_found - gold_e)
            sub_e = 0.125 if err_e <= tol_e else 0.125 * max(0.0, 1.0 - (err_e - tol_e) / tol_e)
            rel_err = abs(s_found - gold_s) / gold_s if gold_s > 0 else 1.0
            sub_s = 0.125 if rel_err <= tol_s else 0.125 * max(0.0, 1.0 - (rel_err - tol_s) / tol_s)
            score += sub_e + sub_s
    if total_peaks == 0:
        return 0.0
    return min(score, 1.0)


# === block: score_3 (check id='oconduct_hnb2o5') ===
def score_3(artifact, step, ctx):
    import csv, math
    rows = list(csv.DictReader(open('/app/outputs/optical_conductivity_HNb2O5.csv')))
    if len(rows) < 2:
        return 0.0

    data = []
    for r in rows:
        e = float(r['Energy(eV)'])
        sp = float(r['sigma_perp'])
        spar = float(r['sigma_par'])
        data.append((e, sp, spar))

    def find_peak(data, channel_idx, window):
        low, high = window
        best_e = None
        best_val = -1.0
        for e, sp, spar in data:
            if e < low - 0.01 or e > high + 0.01:
                continue
            val = sp if channel_idx == 0 else spar
            if val > best_val:
                best_val = val
                best_e = e
        return best_e, best_val

    peaks = step['peaks']
    tol_e = step['tolerance_energy_eV']
    tol_s = step['tolerance_sigma_relative']
    total_peaks = 0
    score = 0.0
    for ch, pklist in [('perp', 0), ('par', 1)]:
        ch_idx = 0 if ch == 'perp' else 1
        for pk in peaks[ch]:
            e_found, s_found = find_peak(data, ch_idx, pk['energy_window'])
            if e_found is None:
                continue
            total_peaks += 1
            gold_e = pk['gold_energy_eV']
            gold_s = pk['gold_sigma']
            err_e = abs(e_found - gold_e)
            sub_e = 0.125 if err_e <= tol_e else 0.125 * max(0.0, 1.0 - (err_e - tol_e) / tol_e)
            rel_err = abs(s_found - gold_s) / gold_s if gold_s > 0 else 1.0
            sub_s = 0.125 if rel_err <= tol_s else 0.125 * max(0.0, 1.0 - (rel_err - tol_s) / tol_s)
            score += sub_e + sub_s
    if total_peaks == 0:
        return 0.0
    return min(score, 1.0)


# === block: score_4 (check id='summary') ===
def score_4(artifact, step, ctx):
    import json, math
    data = json.load(open('/app/outputs/summary_values.json'))
    gold = step['gold']
    tols = step['tolerances']
    # Fields per material
    field_types = [
        ('fundamental_gap', 'fundamental_gap_abs', 'abs'),
        ('optical_gap', 'optical_gap_abs', 'abs'),
        ('static_epsilon1_perp', 'static_epsilon_abs', 'abs'),
        ('static_epsilon1_par', 'static_epsilon_abs', 'abs'),
        ('electron_effective_mass', 'effective_mass_rel', 'rel'),
        ('hole_effective_mass', 'effective_mass_rel', 'rel'),
        ('thermoelectric_conductivity_300K', 'thermoelectric_conductivity_rel', 'rel')
    ]
    total_fields = len(field_types) * 2  # 2 materials
    base = 1.0 / total_fields
    score = 0.0
    for mat in ['Nb3O7(OH)', 'H-Nb2O5']:
        if mat not in data:
            continue
        mdata = data[mat]
        gmat = gold[mat]
        for fname, tol_key, mode in field_types:
            if fname not in mdata:
                continue
            actual = float(mdata[fname])
            gold_val = float(gmat[fname])
            tol_val = float(tols[tol_key])
            if mode == 'abs':
                err = abs(actual - gold_val)
                if err <= tol_val:
                    score += base
                else:
                    score += base * max(0.0, 1.0 - (err - tol_val) / tol_val)
            else: # relative
                if gold_val == 0.0:
                    rel_err = 1.0
                else:
                    rel_err = abs(actual - gold_val) / abs(gold_val)
                if rel_err <= tol_val:
                    score += base
                else:
                    score += base * max(0.0, 1.0 - (rel_err - tol_val) / tol_val)
    return min(score, 1.0)


_SCORERS = {
    'dielectric_nb3o7oh': score_0,
    'dielectric_hnb2o5': score_1,
    'oconduct_nb3o7oh': score_2,
    'oconduct_hnb2o5': score_3,
    'summary': score_4,
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
