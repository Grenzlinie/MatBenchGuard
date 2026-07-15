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


# === block: score_0 (check id='summary_table') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_data = step['gold']
        materials = gold_data['materials']
        tolerances = gold_data['tolerances']
        rows = {}
        for r in artifact:
            mat = r.get('Material', '').strip()
            if mat:
                rows[mat] = r
        total_checks = 0
        passed = 0
        for mat, expected in materials.items():
            row = rows.get(mat)
            if not row:
                continue
            for key, val in expected.items():
                if key not in row:
                    continue
                try:
                    observed = float(row[key])
                except (ValueError, TypeError):
                    continue
                tol = tolerances.get(key, 0.05)
                if abs(observed - val) <= tol:
                    passed += 1
                total_checks += 1
        if total_checks == 0:
            return 0.0
        return passed / total_checks


# === block: score_1 (check id='band_gaps_zero_strain') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol_pbe = gold['tolerances']['PBE_gap']
        tol_hse = gold['tolerances']['HSE06_gap']
        checks = 0
        passed = 0
        for mat in ['MgS', 'MgSe']:
            mat_data = artifact.get(mat, {})
            pbe = mat_data.get('PBE_gap')
            if pbe is not None:
                try:
                    pbe = float(pbe)
                except:
                    pass
                else:
                    checks += 1
                    if abs(pbe - gold[mat]['PBE_gap']) <= tol_pbe:
                        passed += 1
            hse = mat_data.get('HSE06_gap')
            if hse is not None:
                try:
                    hse = float(hse)
                except:
                    pass
                else:
                    checks += 1
                    if abs(hse - gold[mat]['HSE06_gap']) <= tol_hse:
                        passed += 1
        if checks == 0:
            return 0.0
        return passed / checks


# === block: score_2 (check id='strain_band_gap_PBE') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = {}
        for row in artifact:
            mat = row.get('Material', '').strip()
            try:
                strain = float(row['Strain_percent'])
                gap = float(row['PBE_band_gap(eV)'])
            except:
                continue
            if mat not in data:
                data[mat] = []
            data[mat].append((strain, gap))
        def check_MgS(pairs):
            if not pairs:
                return False
            d = {s: g for s, g in pairs}
            if 0 not in d:
                return False
            gap0 = d[0]
            tol = 0.05
            for s, g in pairs:
                if g > gap0 + tol:
                    return False
            return True
        def check_MgSe(pairs):
            if not pairs:
                return False
            d = {s: g for s, g in pairs}
            if -6 not in d:
                return False
            gapm6 = d[-6]
            tol = 0.05
            for s, g in pairs:
                if g > gapm6 + tol:
                    return False
            pos = sorted([s for s in d if s >= 0])
            for i in range(len(pos)-1):
                if d[pos[i+1]] > d[pos[i]] + tol:
                    return False
            return True
        mgs_ok = check_MgS(data.get('MgS', [])) if 'MgS' in data else False
        mgse_ok = check_MgSe(data.get('MgSe', [])) if 'MgSe' in data else False
        score = 0.0
        if mgs_ok:
            score += 0.5
        if mgse_ok:
            score += 0.5
        return score


# === block: score_3 (check id='dielectric_MgS') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        static_gold = gold['static_eps1']
        static_tol = gold['static_tol']
        peaks_gold = gold['peaks_imag']
        peak_tol = gold['peak_tol']
        energies = []
        real = []
        imag = []
        for row in artifact:
            try:
                e = float(row['Energy_eV'])
                r = float(row['real_eps_ZZ'])
                i = float(row['imag_eps_ZZ'])
            except:
                continue
            energies.append(e)
            real.append(r)
            imag.append(i)
        if len(energies) == 0:
            return 0.0
        static_computed = real[0]
        static_score = 1.0 if abs(static_computed - static_gold) <= static_tol else 0.0
        n = len(imag)
        peaks_pos = []
        if n > 2:
            for i in range(1, n-1):
                if imag[i] > imag[i-1] and imag[i] > imag[i+1] and imag[i] > 0.01:
                    peaks_pos.append((energies[i], imag[i]))
        peaks_pos.sort(key=lambda x: x[0])
        first_two = [p[0] for p in peaks_pos[:2]]
        peak_score = 0.0
        if len(first_two) >= 1:
            if abs(first_two[0] - peaks_gold[0]) <= peak_tol:
                peak_score += 0.3
            if len(first_two) >= 2:
                if abs(first_two[1] - peaks_gold[1]) <= peak_tol:
                    peak_score += 0.3
        return 0.4 * static_score + peak_score


# === block: score_4 (check id='dielectric_MgSe') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        static_gold = gold['static_eps1']
        static_tol = gold['static_tol']
        peaks_gold = gold['peaks_imag']
        peak_tol = gold['peak_tol']
        energies = []
        real = []
        imag = []
        for row in artifact:
            try:
                e = float(row['Energy_eV'])
                r = float(row['real_eps_ZZ'])
                i = float(row['imag_eps_ZZ'])
            except:
                continue
            energies.append(e)
            real.append(r)
            imag.append(i)
        if len(energies) == 0:
            return 0.0
        static_computed = real[0]
        static_score = 1.0 if abs(static_computed - static_gold) <= static_tol else 0.0
        n = len(imag)
        peaks_pos = []
        if n > 2:
            for i in range(1, n-1):
                if imag[i] > imag[i-1] and imag[i] > imag[i+1] and imag[i] > 0.01:
                    peaks_pos.append((energies[i], imag[i]))
        peaks_pos.sort(key=lambda x: x[0])
        first_two = [p[0] for p in peaks_pos[:2]]
        peak_score = 0.0
        if len(first_two) >= 1:
            if abs(first_two[0] - peaks_gold[0]) <= peak_tol:
                peak_score += 0.3
            if len(first_two) >= 2:
                if abs(first_two[1] - peaks_gold[1]) <= peak_tol:
                    peak_score += 0.3
        return 0.4 * static_score + peak_score


# === block: score_5 (check id='absorption_reflectivity_MgS') ===
def score_5(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        vis_low, vis_high = gold['visible_range']
        abs_thresh = gold['abs_threshold']
        abs_peak_pos = gold['main_abs_peak_pos']
        abs_tol = gold['main_abs_peak_tol']
        ref_peak_pos = gold['main_ref_peak_pos']
        ref_tol = gold['main_ref_peak_tol']
        energies = []
        abs_coeff = []
        reflect = []
        for row in artifact:
            try:
                e = float(row['Energy_eV'])
                a = float(row['absorption_coeff_cm-1'])
                r = float(row['reflectivity_fraction'])
            except:
                continue
            energies.append(e)
            abs_coeff.append(a)
            reflect.append(r)
        n = len(energies)
        if n == 0:
            return 0.0
        vis_vals = [a for e, a in zip(energies, abs_coeff) if vis_low <= e <= vis_high]
        visible_ok = True
        if vis_vals:
            avg_vis = sum(vis_vals) / len(vis_vals)
            if avg_vis > abs_thresh:
                visible_ok = False
        max_abs_idx = max(range(n), key=lambda i: abs_coeff[i])
        max_abs_e = energies[max_abs_idx]
        abs_peak_ok = abs(max_abs_e - abs_peak_pos) <= abs_tol
        max_ref_idx = max(range(n), key=lambda i: reflect[i])
        max_ref_e = energies[max_ref_idx]
        ref_peak_ok = abs(max_ref_e - ref_peak_pos) <= ref_tol
        score = 0.2 * (1.0 if visible_ok else 0.0) + 0.4 * (1.0 if abs_peak_ok else 0.0) + 0.4 * (1.0 if ref_peak_ok else 0.0)
        return score


# === block: score_6 (check id='absorption_reflectivity_MgSe') ===
def score_6(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        vis_low, vis_high = gold['visible_range']
        abs_thresh = gold['abs_threshold']
        abs_peak_pos = gold['main_abs_peak_pos']
        abs_tol = gold['main_abs_peak_tol']
        ref_peak_pos = gold['main_ref_peak_pos']
        ref_tol = gold['main_ref_peak_tol']
        energies = []
        abs_coeff = []
        reflect = []
        for row in artifact:
            try:
                e = float(row['Energy_eV'])
                a = float(row['absorption_coeff_cm-1'])
                r = float(row['reflectivity_fraction'])
            except:
                continue
            energies.append(e)
            abs_coeff.append(a)
            reflect.append(r)
        n = len(energies)
        if n == 0:
            return 0.0
        vis_vals = [a for e, a in zip(energies, abs_coeff) if vis_low <= e <= vis_high]
        visible_ok = True
        if vis_vals:
            avg_vis = sum(vis_vals) / len(vis_vals)
            if avg_vis > abs_thresh:
                visible_ok = False
        max_abs_idx = max(range(n), key=lambda i: abs_coeff[i])
        max_abs_e = energies[max_abs_idx]
        abs_peak_ok = abs(max_abs_e - abs_peak_pos) <= abs_tol
        max_ref_idx = max(range(n), key=lambda i: reflect[i])
        max_ref_e = energies[max_ref_idx]
        ref_peak_ok = abs(max_ref_e - ref_peak_pos) <= ref_tol
        score = 0.2 * (1.0 if visible_ok else 0.0) + 0.4 * (1.0 if abs_peak_ok else 0.0) + 0.4 * (1.0 if ref_peak_ok else 0.0)
        return score


_SCORERS = {
    'summary_table': score_0,
    'band_gaps_zero_strain': score_1,
    'strain_band_gap_PBE': score_2,
    'dielectric_MgS': score_3,
    'dielectric_MgSe': score_4,
    'absorption_reflectivity_MgS': score_5,
    'absorption_reflectivity_MgSe': score_6,
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
