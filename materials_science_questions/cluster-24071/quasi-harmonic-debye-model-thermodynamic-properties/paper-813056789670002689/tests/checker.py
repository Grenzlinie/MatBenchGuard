import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
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
    ctx = {}

    # --- step_01 E-V data ---
    ev_path = os.path.join(outputs_dir, 'step_01_e_v_data.csv')
    if os.path.exists(ev_path):
        with open(ev_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                volumes = []
                energies = []
                for r in rows:
                    v = float(r['volume'])
                    e = float(r['energy'])
                    volumes.append(v)
                    energies.append(e)
                # equilibrium volume at minimum energy
                idx = energies.index(min(energies))
                v0_bohr3 = volumes[idx]
                # convert to Å^3 (1 bohr = 0.529177 Å, so 1 bohr^3 = 0.529177^3 = 0.1482 ≈ 1/6.748)
                ctx['v0_ang3_fitted'] = v0_bohr3 / 6.748

    # --- step_02 dielectric data ---
    diel_path = os.path.join(outputs_dir, 'step_02_dielectric_function.csv')
    if os.path.exists(diel_path):
        with open(diel_path, newline='') as f:
            reader = csv.DictReader(f)
            diel_rows = list(reader)
            if diel_rows:
                def find_peak(rows, col):
                    best_val = -1
                    best_e = 0.0
                    for r in rows:
                        e = float(r['energy_eV'])
                        if e <= 5.0:
                            v = float(r[col])
                            if v > best_val:
                                best_val = v
                                best_e = e
                    return best_val, best_e
                ctx['peak_xx'], ctx['peak_e_xx'] = find_peak(diel_rows, 'eps2_xx')
                ctx['peak_yy'], ctx['peak_e_yy'] = find_peak(diel_rows, 'eps2_yy')
                ctx['peak_zz'], ctx['peak_e_zz'] = find_peak(diel_rows, 'eps2_zz')

    # --- step_03 thermal data ---
    therm_path = os.path.join(outputs_dir, 'step_03_thermal_properties.csv')
    if os.path.exists(therm_path):
        with open(therm_path, newline='') as f:
            reader = csv.DictReader(f)
            therm_rows = list(reader)
            # Debye temp at 300 K, 0 GPa (nearest)
            debye_at_300 = None
            cv_high = []
            for r in therm_rows:
                T = float(r['temperature_K'])
                P = float(r['pressure_GPa'])
                cv = float(r['cv_J_molK'])
                if abs(P) < 0.01:
                    if abs(T - 300.0) < 0.5:
                        debye_at_300 = float(r['debye_temp_K'])
                    if T >= 4000.0:
                        cv_high.append(cv)
            if debye_at_300 is not None:
                ctx['debye_300K'] = debye_at_300
            if cv_high:
                ctx['cv_asymptote'] = sum(cv_high) / len(cv_high)

    return ctx


# === block: score_0 (check id='valid_step01') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 8:
        return 0.0
    cols = set(artifact[0].keys())
    if 'volume' not in cols or 'energy' not in cols:
        return 0.0
    return 1.0


# === block: score_1 (check id='eos_fit') ===
def score_1(artifact, step, ctx):
    v0 = ctx.get('v0_ang3_fitted')
    if v0 is None:
        return 0.0
    target = float(step['params']['target_v0_ang3'])
    tol = float(step['params']['tolerance_fraction'])
    if abs(v0 - target) / target <= tol:
        return 1.0
    return 0.0


# === block: score_2 (check id='valid_step02') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 10:
        return 0.0
    cols = set(artifact[0].keys())
    for c in ['energy_eV','eps2_xx','eps2_yy','eps2_zz']:
        if c not in cols:
            return 0.0
    return 1.0


# === block: score_3 (check id='eps2_peaks') ===
def score_3(artifact, step, ctx):
    params = step['params']
    energy_tol = float(params['energy_tol'])
    val_tol_frac = float(params['val_tol_frac'])
    components = [
        ('xx', ctx.get('peak_xx'), ctx.get('peak_e_xx'),
         float(params['xx_peak_val']), float(params['xx_peak_energy'])),
        ('yy', ctx.get('peak_yy'), ctx.get('peak_e_yy'),
         float(params['yy_peak_val']), float(params['yy_peak_energy'])),
        ('zz', ctx.get('peak_zz'), ctx.get('peak_e_zz'),
         float(params['zz_peak_val']), float(params['zz_peak_energy'])),
    ]
    scores = []
    for name, peak_val, peak_e, gold_val, gold_e in components:
        if peak_val is None or peak_e is None:
            scores.append(0.0)
            continue
        e_ok = abs(peak_e - gold_e) <= energy_tol
        v_ok = abs(peak_val - gold_val) / gold_val <= val_tol_frac
        scores.append(1.0 if (e_ok and v_ok) else 0.0)
    return sum(scores) / len(scores)


# === block: score_4 (check id='valid_step03') ===
def score_4(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 10:
        return 0.0
    cols = set(artifact[0].keys())
    required = ['temperature_K','pressure_GPa','cv_J_molK','debye_temp_K','volume_bohr3','bulk_modulus_GPa','alpha_1e5_perK','cp_J_molK','entropy_J_molK','internal_energy_kJ_mol']
    for c in required:
        if c not in cols:
            return 0.0
    return 1.0


# === block: score_5 (check id='cv_asymptote') ===
def score_5(artifact, step, ctx):
    cv = ctx.get('cv_asymptote')
    if cv is None:
        return 0.0
    target = float(step['params']['target_cv'])
    tol = float(step['params']['tolerance_fraction'])
    if abs(cv - target) / target <= tol:
        return 1.0
    return 0.0


# === block: score_6 (check id='results_valid') ===
def score_6(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    fields = step['params']['required_fields']
    for f in fields:
        if f not in artifact:
            return 0.0
    return 1.0


# === block: score_7 (check id='results_consistency') ===
def score_7(artifact, step, ctx):
    params = step['params']
    res = artifact
    # lattice comparison
    lat = res.get('lattice_params')
    lat_ok = True
    if not lat or not isinstance(lat, dict):
        lat_ok = False
    else:
        a = float(lat.get('a', 0))
        b = float(lat.get('b', 0))
        c = float(lat.get('c', 0))
        tol_frac = float(params['lattice_tol_frac'])
        a_target = float(params['lattice_a_target'])
        b_target = float(params['lattice_b_target'])
        c_target = float(params['lattice_c_target'])
        a_good = abs(a - a_target) / a_target <= tol_frac
        b_good = abs(b - b_target) / b_target <= tol_frac
        c_good = abs(c - c_target) / c_target <= tol_frac
        lat_ok = a_good and b_good and c_good
    lattice_score = 0.4 if lat_ok else 0.0

    # epsilon2 peak consistency with raw recompute
    ep = res.get('epsilon2_peaks')
    eps_ok = True
    if not ep or not isinstance(ep, dict):
        eps_ok = False
    else:
        energy_tol = float(params['eps2_energy_tol'])
        val_tol_frac = float(params['eps2_val_tol_frac'])
        comps = [
            (ep.get('xx_peak_val'), ep.get('xx_peak_energy'),
             ctx.get('peak_xx'), ctx.get('peak_e_xx'),
             float(params.get('xx_peak_val', 0)), float(params.get('xx_peak_energy', 0))),
            (ep.get('yy_peak_val'), ep.get('yy_peak_energy'),
             ctx.get('peak_yy'), ctx.get('peak_e_yy'),
             float(params.get('yy_peak_val', 0)), float(params.get('yy_peak_energy', 0))),
            (ep.get('zz_peak_val'), ep.get('zz_peak_energy'),
             ctx.get('peak_zz'), ctx.get('peak_e_zz'),
             float(params.get('zz_peak_val', 0)), float(params.get('zz_peak_energy', 0))),
        ]
        for reported_val, reported_e, raw_val, raw_e, paper_val, paper_e in comps:
            if reported_val is None or reported_e is None or raw_val is None:
                eps_ok = False
                break
            # must match raw recompute within tight tolerance (to guarantee consistency)
            if abs(float(reported_e) - raw_e) > 0.02:
                eps_ok = False
                break
            if abs(float(reported_val) - raw_val) / (abs(raw_val) + 1e-12) > 0.01:
                eps_ok = False
                break
    eps_score = 0.3 if eps_ok else 0.0

    # plasma frequency
    pf = res.get('plasma_frequency')
    pf_ok = False
    if pf is not None:
        pf_target = float(params['plasma_frequency_target'])
        pf_tol = float(params['plasma_tol_ev'])
        if abs(float(pf) - pf_target) <= pf_tol:
            pf_ok = True
    pf_score = 0.2 if pf_ok else 0.0

    # Cv Dulong-Petit
    cv_reported = res.get('cv_dulong_petit')
    cv_ok = False
    if cv_reported is not None:
        cv_target = float(params['cv_target'])
        cv_tol_frac = float(params['cv_tol_frac'])
        if abs(float(cv_reported) - cv_target) / cv_target <= cv_tol_frac:
            cv_ok = True
    cv_score = 0.05 if cv_ok else 0.0

    # Debye temperature cross-check
    debye_reported = res.get('debye_temperature_0GPa_300K')
    debye_ok = False
    if debye_reported is not None:
        debye_raw = ctx.get('debye_300K')
        if debye_raw is not None:
            if abs(float(debye_reported) - debye_raw) <= float(params['debye_temp_tol_k']):
                debye_ok = True
    debye_score = 0.05 if debye_ok else 0.0

    return lattice_score + eps_score + pf_score + cv_score + debye_score


_SCORERS = {
    'valid_step01': score_0,
    'eos_fit': score_1,
    'valid_step02': score_2,
    'eps2_peaks': score_3,
    'valid_step03': score_4,
    'cv_asymptote': score_5,
    'results_valid': score_6,
    'results_consistency': score_7,
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
