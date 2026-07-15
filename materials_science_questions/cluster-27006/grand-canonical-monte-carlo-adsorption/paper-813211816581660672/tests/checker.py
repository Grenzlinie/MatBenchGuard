import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import math

def load_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def interpolate_loading(rows, gas, key_val, pressure, key_col):
    filtered = [r for r in rows if r['gas'] == gas and str(r[key_col]) == str(key_val) and r['pressure_bar']]
    if not filtered:
        return None
    filtered.sort(key=lambda x: float(x['pressure_bar']))
    ps = [float(x['pressure_bar']) for x in filtered]
    ls = [float(x['loading_molecules_per_uc']) for x in filtered]
    if len(ps) == 0:
        return None
    if pressure <= ps[0]:
        return ls[0]
    if pressure >= ps[-1]:
        return ls[-1]
    for i in range(len(ps)-1):
        if ps[i] <= pressure <= ps[i+1]:
            if ps[i+1] - ps[i] == 0:
                return ls[i]
            t = (pressure - ps[i]) / (ps[i+1] - ps[i])
            return ls[i] + t * (ls[i+1] - ls[i])
    return None


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
    for ch in spec['checks']:
        ctx[ch['id']] = ch['parameters']
    return ctx


# === block: score_0 (check id='check_isotherms') ===
def score_0(artifact, step, ctx):
    params = ctx['check_isotherms']
    tol_rel = params['tol_rel']
    tol_abs = params['tol_abs']
    conv_max = params['convergence_max_diff']
    gold_points = params['gold_points']
    rows = load_csv(os.path.join('/app/outputs','step_04_isotherms.csv'))
    if not rows:
        return 0.0
    # score each gold point
    num_points = len(gold_points)
    passed = 0
    for gp in gold_points:
        gas = gp['gas']
        sial = gp['SiAl']
        p = gp['pressure']
        e = gp['loading']
        a = interpolate_loading(rows, gas, sial, p, 'SiAl')
        if a is None:
            continue
        dev = abs(a - e)
        if dev <= max(tol_abs, tol_rel * e):
            passed += 1
    # low-pressure ordering: at P=0.001 for CO2, check that all Na-ZSM5 loadings >= 0.5 and inf < 0.5
    low_ok = True
    if 'CO2' in [r['gas'] for r in rows]:
        for sial in ['95','47','31','23','13']:
            v = interpolate_loading(rows, 'CO2', sial, 0.001, 'SiAl')
            if v is None or v < 0.3:
                low_ok = False
                break
        inf_v = interpolate_loading(rows, 'CO2', 'inf', 0.001, 'SiAl')
        if inf_v is not None and inf_v > 0.5:
            low_ok = False
    # high-pressure convergence: at P=10 for CO2, max diff from silicalite-1 <= conv_max
    high_ok = True
    inf_10 = interpolate_loading(rows, 'CO2', 'inf', 10.0, 'SiAl')
    if inf_10 is not None:
        for sial in ['95','47','31','23','13']:
            v = interpolate_loading(rows, 'CO2', sial, 10.0, 'SiAl')
            if v is not None and abs(v - inf_10) > conv_max:
                high_ok = False
                break
    # Also for N2 high-P convergence at 10 bar (using same conv_max)
    inf_10_n2 = interpolate_loading(rows, 'N2', 'inf', 10.0, 'SiAl')
    if inf_10_n2 is not None:
        for sial in ['95','47','31','23','13']:
            v = interpolate_loading(rows, 'N2', sial, 10.0, 'SiAl')
            if v is not None and abs(v - inf_10_n2) > conv_max:
                high_ok = False
                break
    score_points = passed / num_points if num_points > 0 else 0.0
    score_struct = ( (1.0 if low_ok else 0.0) + (1.0 if high_ok else 0.0) ) / 2.0
    # Combine with weights: 70% point-wise accuracy, 30% structural
    return 0.7 * score_points + 0.3 * score_struct


# === block: score_1 (check id='check_heats') ===
def score_1(artifact, step, ctx):
    params = ctx['check_heats']
    rows = load_csv(os.path.join('/app/outputs','step_05_isosteric_heats.csv'))
    if not rows:
        return 0.0
    # group by gas and SiAl
    def get_groups(rows):
        groups = {}
        for r in rows:
            key = (r['gas'], r['SiAl'])
            groups.setdefault(key, []).append((float(r['loading_molecules_per_uc']), float(r['Qst_kJ_per_mol'])))
        for k in groups:
            groups[k].sort()
        return groups
    groups = get_groups(rows)
    # silicalite-1 constant check
    sil_ok_CO2 = True
    sil_ok_N2 = True
    for (gas, sial), pts in groups.items():
        if sial == 'inf':
            vals = [q for _, q in pts]
            if not vals:
                continue
            avg = sum(vals)/len(vals)
            if gas == 'CO2':
                if abs(avg - params['CO2_sil_Qst']) > params['CO2_sil_tol']:
                    sil_ok_CO2 = False
            elif gas == 'N2':
                if abs(avg - params['N2_sil_Qst']) > params['N2_sil_tol']:
                    sil_ok_N2 = False
    # low-loading elevation for Na-ZSM5
    low_ok = True
    for (gas, sial), pts in groups.items():
        if sial != 'inf':
            if not pts:
                continue
            low_qst = pts[0][1]
            if gas == 'CO2' and low_qst < params['CO2_low_Qst_min']:
                low_ok = False
            elif gas == 'N2' and low_qst < params['N2_low_Qst_min']:
                low_ok = False
    # high-loading convergence: at highest loading, Qst should be within high_convergence_tol of silicalite-1 avg (if available)
    sil_co2_qst = []
    sil_n2_qst = []
    for (gas, sial), pts in groups.items():
        if sial == 'inf':
            for _, q in pts:
                if gas == 'CO2':
                    sil_co2_qst.append(q)
                elif gas == 'N2':
                    sil_n2_qst.append(q)
    sil_avg_CO2 = sum(sil_co2_qst)/len(sil_co2_qst) if sil_co2_qst else params['CO2_sil_Qst']
    sil_avg_N2 = sum(sil_n2_qst)/len(sil_n2_qst) if sil_n2_qst else params['N2_sil_Qst']
    high_ok = True
    for (gas, sial), pts in groups.items():
        if sial != 'inf':
            high = pts[-1][0]
            q_high = pts[-1][1]
            if gas == 'CO2' and high >= params['CO2_high_loading_min']:
                if abs(q_high - sil_avg_CO2) > params['high_convergence_tol']:
                    high_ok = False
            elif gas == 'N2' and high >= params['N2_high_loading_min']:
                if abs(q_high - sil_avg_N2) > params['high_convergence_tol']:
                    high_ok = False
    score_sil = ( (1.0 if sil_ok_CO2 else 0.0) + (1.0 if sil_ok_N2 else 0.0) ) / 2.0
    score_low = 1.0 if low_ok else 0.0
    score_high = 1.0 if high_ok else 0.0
    return 0.4 * score_sil + 0.3 * score_low + 0.3 * score_high


# === block: score_2 (check id='check_charge') ===
def score_2(artifact, step, ctx):
    params = ctx['check_charge']
    rows = load_csv(os.path.join('/app/outputs','step_07_charge_comparison.csv'))
    if not rows:
        return 0.0
    def mape_for_charge(gas, charge, exp_points):
        # exp_points: list of {pressure, loading}
        pred_vals = []
        exp_vals = []
        for ep in exp_points:
            a = interpolate_loading(rows, gas, charge, ep['pressure'], 'Na_charge_e')
            if a is not None and ep['loading'] > 0:
                pred_vals.append(a)
                exp_vals.append(ep['loading'])
        if not pred_vals:
            return float('inf')
        ape = [abs(p-e)/e for p,e in zip(pred_vals, exp_vals)]
        return sum(ape)/len(ape)
    co2_exp = params['CO2_exp_points']
    n2_exp = params['N2_exp_points']
    charges = ['1.0','0.7','0.4']
    co2_mapes = {}
    n2_mapes = {}
    for c in charges:
        co2_mapes[c] = mape_for_charge('CO2', c, co2_exp)
        n2_mapes[c] = mape_for_charge('N2', c, n2_exp)
    # determine best charge for each gas
    best_co2 = min(co2_mapes, key=co2_mapes.get) if co2_mapes else None
    best_n2 = min(n2_mapes, key=n2_mapes.get) if n2_mapes else None
    score_co2 = 1.0 if best_co2 == '0.7' else 0.0
    score_n2 = 1.0 if best_n2 == '0.4' else 0.0
    # also check low-pressure ordering: at a low pressure, loading(1.0) > loading(0.7) > loading(0.4)
    low_p_co2 = 0.001
    low_p_n2 = 0.01
    order_ok = True
    v_co2_1 = interpolate_loading(rows, 'CO2', '1.0', low_p_co2, 'Na_charge_e')
    v_co2_07 = interpolate_loading(rows, 'CO2', '0.7', low_p_co2, 'Na_charge_e')
    v_co2_04 = interpolate_loading(rows, 'CO2', '0.4', low_p_co2, 'Na_charge_e')
    if not (v_co2_1 is not None and v_co2_07 is not None and v_co2_04 is not None and v_co2_1 > v_co2_07 > v_co2_04):
        order_ok = False
    v_n2_1 = interpolate_loading(rows, 'N2', '1.0', low_p_n2, 'Na_charge_e')
    v_n2_07 = interpolate_loading(rows, 'N2', '0.7', low_p_n2, 'Na_charge_e')
    v_n2_04 = interpolate_loading(rows, 'N2', '0.4', low_p_n2, 'Na_charge_e')
    if not (v_n2_1 is not None and v_n2_07 is not None and v_n2_04 is not None and v_n2_1 > v_n2_07 > v_n2_04):
        order_ok = False
    score_order = 1.0 if order_ok else 0.0
    return 0.3 * score_co2 + 0.3 * score_n2 + 0.4 * score_order


_SCORERS = {
    'check_isotherms': score_0,
    'check_heats': score_1,
    'check_charge': score_2,
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
