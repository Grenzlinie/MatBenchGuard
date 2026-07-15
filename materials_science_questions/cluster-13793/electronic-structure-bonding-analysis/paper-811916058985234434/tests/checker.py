import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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
    ev_path = os.path.join(outputs_dir, 'ev_data.csv')
    ev_data = []
    if os.path.exists(ev_path):
        with open(ev_path, newline='') as f:
            reader = csv.DictReader(f)
            ev_data = list(reader)
    return {'ev_data': ev_data, 'ev_data_loaded': len(ev_data) > 0}


# === block: score_0 (check id='step_02_energy_volume_scan') ===
def score_0(artifact, step, ctx):
    artifact = [row for row in artifact if row.get('phase') and row.get('volume_A3') and row.get('total_energy_eV')]
    if not artifact or len(artifact) < 2:
        return 0.0

    # Separate by phase
    phases = {}
    for row in artifact:
        p = row['phase'].strip()
        try:
            vol = float(row['volume_A3'])
            ene = float(row['total_energy_eV'])
        except (ValueError, KeyError):
            continue
        phases.setdefault(p, []).append((vol, ene))

    if len(phases) != 2 or 'PPV' not in phases or 'PV' not in phases:
        return 0.0

    targets = {'PPV': step['target_V0_PPV'], 'PV': step['target_V0_PV']}
    tol = step['volume_tolerance_relative']
    min_n = step.get('min_points_per_phase', 5)

    scores = []
    for p in ('PPV', 'PV'):
        pts = phases[p]
        # find minimum energy point
        min_ene = min(pts, key=lambda x: x[1])
        V_min = min_ene[0]
        target = targets[p]
        rel_err = abs(V_min - target) / target
        # score volume match
        if rel_err <= tol:
            vol_score = 1.0
        elif rel_err >= 0.05:
            vol_score = 0.0
        else:
            vol_score = 1.0 - (rel_err - tol) / (0.05 - tol)

        # check that there are points on both sides of minimum with higher energy
        vols = [v for v, e in pts]
        min_energy_val = min_ene[1]
        higher_left = any(v < V_min and e > min_energy_val + 1e-6 for v, e in pts)
        higher_right = any(v > V_min and e > min_energy_val + 1e-6 for v, e in pts)
        physical_minimum = 1.0 if (higher_left and higher_right) else 0.0

        # enough points
        enough_points = 1.0 if len(pts) >= min_n else 0.0

        # combine per-phase: vol_match dominate
        phase_score = 0.7 * vol_score + 0.2 * physical_minimum + 0.1 * enough_points
        scores.append(phase_score)

    return (scores[0] + scores[1]) / 2.0


# === block: score_1 (check id='step_04_summary') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    phases_list = artifact.get('phases', [])
    if not phases_list or len(phases_list) != 2:
        return 0.0

    ev_data = ctx.get('ev_data', [])
    frac = 0.0

    # extract phase data
    phase_dict = {}
    for ph in phases_list:
        name = ph.get('phase')
        if name in ('PPV', 'PV'):
            phase_dict[name] = ph
    if len(phase_dict) != 2:
        return 0.0

    # 1. energy_difference_eV check
    deltaE = artifact.get('energy_difference_eV', None)
    target_dE = step['target_deltaE_eV']
    tol_dE = step['deltaE_tolerance_eV']
    if deltaE is not None and isinstance(deltaE, (int, float)):
        err = abs(deltaE - target_dE)
        if err <= tol_dE:
            frac += 0.25
        else:
            frac += max(0.0, 1.0 - (err - tol_dE)/(0.1))
    else:
        pass

    # 2. band gap checks
    for p, target_gap in [('PPV', step['target_bandgap_PPV_eV']), ('PV', step['target_bandgap_PV_eV'])]:
        ph = phase_dict.get(p, {})
        gap = ph.get('band_gap_eV', None)
        tol_g = step['bandgap_tolerance_eV']
        if gap is not None and isinstance(gap, (int, float)):
            err = abs(gap - target_gap)
            if err <= tol_g:
                frac += 0.1
            else:
                frac += max(0.0, (1.0 - (err - tol_g)/(0.5)) * 0.1)
        else:
            pass

    # 3. volume checks (against paper gold)
    vol_tol = step['volume_tolerance_relative']
    for p, target_vol in [('PPV', 212.14), ('PV', 214.75)]:
        ph = phase_dict.get(p, {})
        v0 = ph.get('equilibrium_volume_A3', None)
        if v0 is not None and isinstance(v0, (int, float)):
            rel_e = abs(v0 - target_vol) / target_vol
            if rel_e <= vol_tol:
                frac += 0.1
            else:
                frac += max(0.0, (1.0 - (rel_e - vol_tol)/(0.05)) * 0.1)
        else:
            pass

    # 4. trend checks
    ppv = phase_dict.get('PPV', {})
    pv = phase_dict.get('PV', {})
    trend_score = 0.0
    # V0_PPV < V0_PV
    v_ppv = ppv.get('equilibrium_volume_A3')
    v_pv = pv.get('equilibrium_volume_A3')
    if v_ppv is not None and v_pv is not None and v_ppv < v_pv:
        trend_score += 0.025
    # deltaE < 0 (already checked but sign)
    if deltaE is not None and deltaE < 0:
        trend_score += 0.025
    # B0_PPV > B0_PV
    b_ppv = ppv.get('bulk_modulus_GPa')
    b_pv = pv.get('bulk_modulus_GPa')
    if b_ppv is not None and b_pv is not None and b_ppv > b_pv:
        trend_score += 0.025
    # Eg_PPV > Eg_PV
    eg_ppv = ppv.get('band_gap_eV')
    eg_pv = pv.get('band_gap_eV')
    if eg_ppv is not None and eg_pv is not None and eg_ppv > eg_pv:
        trend_score += 0.025
    frac += trend_score

    # 5. consistency with ev_data
    if ev_data:
        # find minimum energy volume for each phase from raw data
        cons_fact = 0.15
        for p in ('PPV', 'PV'):
            ph_rows = [(float(r['volume_A3']), float(r['total_energy_eV'])) for r in ev_data if r.get('phase') == p]
            if not ph_rows:
                continue
            min_en = min(ph_rows, key=lambda x: x[1])
            v_min_data = min_en[0]
            en_min_data = min_en[1]
            # compare to reported equilibrium volume
            v_rep = phase_dict[p].get('equilibrium_volume_A3')
            en_rep = phase_dict[p].get('equilibrium_energy_eV_per_fu')
            if v_rep is not None and en_rep is not None:
                v_match = 1.0 if abs(v_rep - v_min_data) <= max(0.01, v_min_data*0.005) else 0.0
                en_match = 1.0 if abs(en_rep - en_min_data) <= 0.001 else 0.0
                frac += (cons_fact/2) * (v_match + en_match)
    else:
        frac += 0.0

    return min(frac, 1.0)


_SCORERS = {
    'step_02_energy_volume_scan': score_0,
    'step_04_summary': score_1,
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
