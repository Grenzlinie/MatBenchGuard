import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os, re


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

    # 1. load critical length curve (public bundled resource)
    crit_path = '/app/inputs/critical_length.csv'
    if not os.path.exists(crit_path):
        # fallback inline data (digitized from paper, matching the analytic fixture)
        inline_data = [
            (6.0, 4.7), (6.5, 5.3), (7.0, 6.1), (7.5, 7.0), (8.0, 8.0),
            (8.5, 9.2), (9.0, 10.5), (10.0, 13.5), (11.0, 17.0), (12.0, 21.0), (14.0, 30.0)
        ]
        ki_crit, l_crit = zip(*inline_data)
    else:
        with open(crit_path, newline='') as f:
            rows = list(csv.DictReader(f))
        ki_crit = [float(r['KI']) for r in rows]
        l_crit = [float(r['critical_length']) for r in rows]
        # sort by KI
        pairs = sorted(zip(ki_crit, l_crit))
        ki_crit, l_crit = zip(*pairs)

    ctx['ki_crit'] = ki_crit
    ctx['l_crit'] = l_crit

    # helper: linear interpolation
    def interp(x, xs, ys):
        xs, ys = list(xs), list(ys)
        if x <= xs[0]: return ys[0]
        if x >= xs[-1]: return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1]-xs[i])
                return ys[i] + t * (ys[i+1]-ys[i])
        return ys[-1]
    ctx['interp'] = interp

    # 2. load agent's hydride growth curves
    growth_path = os.path.join(outputs_dir, 'hydride_growth_curves.csv')
    growth_data = []
    if os.path.exists(growth_path):
        with open(growth_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    ki = float(row['KI'])
                    lh = float(row['hydride_length'])
                    lbl = row.get('time_label', '')
                    # parse numeric hours
                    hours = None
                    m = re.search(r'([\d.]+)\s*h', lbl, re.IGNORECASE)
                    if m:
                        hours = float(m.group(1))
                    growth_data.append({'KI': ki, 'time_label': lbl, 'hydride_length': lh, 'time_hours': hours})
                except (ValueError, KeyError):
                    continue
    ctx['growth_data'] = growth_data

    # 3. load agent's velocity CSV
    vel_path = os.path.join(outputs_dir, 'dhc_velocity_vs_KI.csv')
    agent_vel = []
    if os.path.exists(vel_path):
        with open(vel_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    ki = float(row['KI'])
                    v = float(row['velocity'])
                    agent_vel.append({'KI': ki, 'velocity': v})
                except (ValueError, KeyError):
                    continue
    ctx['agent_vel'] = agent_vel

    ctx['recomputed_vel'] = {}
    ctx['growth_recompute_possible'] = False

    # check if growth data has enough numeric times
    from collections import defaultdict
    groups = defaultdict(list)
    for g in growth_data:
        if g['time_hours'] is not None:
            groups[g['KI']].append((g['time_hours'], g['hydride_length']))
    has_numeric = any(len(v)>=2 for v in groups.values())
    ctx['growth_recompute_possible'] = has_numeric
    ctx['growth_groups'] = groups


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if rows is None or not isinstance(rows, list):
            return 0.0
        n = len(rows)
        score = 0.0

        # check required columns
        if n>0:
            cols = set(rows[0].keys())
            for c in step.get('params',{}).get('required_columns',[]):
                if c not in cols:
                    return 0.0
            score += 0.3
        else:
            return 0.0

        # time labels count
        time_set = set()
        ki_vals = set()
        for r in rows:
            ki = r.get('KI')
            tl = r.get('time_label','')
            if ki is not None:
                ki_vals.add(float(ki))
            time_set.add(tl)
        # KI range check
        ki_min = min(ki_vals) if ki_vals else 0
        ki_max = max(ki_vals) if ki_vals else 0
        if len(ki_vals)>=5 and ki_min<=7.0 and ki_max>=12.0:
            score += 0.1
        if len(time_set)>=3:
            score += 0.2

        # monotonic increase per KI
        from collections import defaultdict
        grp = defaultdict(list)
        for r in rows:
            try:
                ki = float(r['KI'])
                lh = float(r['hydride_length'])
                th = r.get('time_hours')
                if th is not None:
                    grp[ki].append((th, lh))
            except:
                continue
        mono_ok = 0
        total_grp = 0
        for ki, vals in grp.items():
            if len(vals)>=2:
                total_grp += 1
                vals.sort()
                ok = all(vals[i][1] <= vals[i+1][1]+1e-6 for i in range(len(vals)-1))
                if ok:
                    mono_ok += 1
        if total_grp>0:
            score += 0.4 * (mono_ok/total_grp)
        else:
            # no numeric times, just check positive lengths
            if all(float(r.get('hydride_length',-1))>=0 for r in rows):
                score += 0.2
        return round(min(score,1.0), 4)
    except Exception:
        return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    vel_rows = artifact  # list of dicts with KI, velocity
    if not vel_rows:
        return 0.0

    agent_vel = ctx.get('agent_vel', [])
    recomputed_vel = ctx.get('recomputed_vel', {})
    critical = ctx['l_crit']
    ki_crit = ctx['ki_crit']
    interp = ctx['interp']
    growth_groups = ctx.get('growth_groups', {})

    score = 0.0

    if ctx['growth_recompute_possible']:
        # recompute velocities from growth curves
        recomputed = {}
        for ki, pairs in growth_groups.items():
            if len(pairs) < 2:
                continue
            pairs.sort()
            times, lengths = zip(*pairs)
            Lc = interp(ki, ki_crit, critical)
            if Lc <= 0:
                continue
            # find intersection: first time where length >= Lc
            t_frac = None
            for t, l in zip(times, lengths):
                if l >= Lc:
                    t_frac = t
                    break
            if t_frac is None:
                # extrapolate? skip
                continue
            v = Lc * 1e-6 / (t_frac * 3600)  # m/s
            recomputed[ki] = v
        ctx['recomputed_vel'] = recomputed

        # score structural properties on recomputed velocities
        ki_sorted = sorted(recomputed.keys())
        if len(ki_sorted) >= 3:
            # stage I: ratio v at KI=9 / v at KI=7
            v7 = recomputed.get(7.0)
            v9 = recomputed.get(9.0)
            if v7 and v9 and v7>0 and v9>0:
                if v9 / v7 >= step['params']['stage_I_vel_factor']:
                    score += 0.4
                elif v9 / v7 >= 1.2:
                    score += 0.2
            # stage II plateau: ratio v at KI=10 to KI=12
            v10 = recomputed.get(10.0)
            v12 = recomputed.get(12.0)
            if v10 and v12 and v10>0 and v12>0:
                ratio = max(v10,v12)/min(v10,v12)
                if ratio <= step['params']['plateau_ratio_max']:
                    score += 0.4
                else:
                    score += 0.1

        # cross-check consistency with agent's velocity (low weight)
        agent_vel_map = {v['KI']: v['velocity'] for v in vel_rows}
        match_frac = 0.0
        n_common = 0
        for ki, rec_v in recomputed.items():
            if ki in agent_vel_map:
                ag_v = agent_vel_map[ki]
                if ag_v > 0 and rec_v > 0:
                    rel = abs(rec_v - ag_v) / max(rec_v, ag_v)
                    if rel <= step['params'].get('recompute_tolerance',0.3):
                        match_frac += 1.0
                    elif rel <= 0.5:
                        match_frac += 0.5
                n_common += 1
        if n_common > 0:
            score += 0.2 * (match_frac / n_common)

    else:
        # fallback: use agent's velocity curve and check structural thresholds
        agent_vel_map = {v['KI']: v['velocity'] for v in vel_rows}
        v7 = agent_vel_map.get(7.0)
        v9 = agent_vel_map.get(9.0)
        v10 = agent_vel_map.get(10.0)
        v12 = agent_vel_map.get(12.0)
        if v7 is not None and v9 is not None:
            if v9 > step['params']['fallback_vel_KI9_min'] and v7 < step['params']['fallback_vel_KI7_max']:
                score += 0.4
            elif v9 > 1e-9:
                score += 0.2
        if v10 is not None and v12 is not None and v10>0 and v12>0:
            ratio = max(v10,v12)/min(v10,v12)
            if ratio <= step['params']['plateau_ratio_max']:
                score += 0.4
            else:
                score += 0.1

        # store empty recomputed to avoid downstream error
        ctx['recomputed_vel'] = {}

    return round(min(score,1.0), 4)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    trans = artifact  # dict
    if not isinstance(trans, dict):
        return 0.0
    params = step.get('params', {})
    trans_ki = trans.get('transition_KI')
    rp_ki = trans.get('K_I_where_rP_equals_lcrit')
    comp = trans.get('comparison')
    if trans_ki is None or rp_ki is None:
        return 0.0

    interp = ctx['interp']
    ki_crit = ctx['ki_crit']
    l_crit = ctx['l_crit']
    recomputed_vel = ctx.get('recomputed_vel', {})
    agent_vel = ctx.get('agent_vel', [])

    score = 0.0

    # 1. recompute transition KI from velocity curve
    # use agent_vel (if recomputed empty, use agent)
    vel_data = recomputed_vel if recomputed_vel else {v['KI']: v['velocity'] for v in agent_vel}
    if len(vel_data) < 3:
        vel_data = {v['KI']: v['velocity'] for v in agent_vel}
    if len(vel_data) >= 3:
        kiv = sorted(vel_data.keys())
        vv = [vel_data[k] for k in kiv]
        slopes = []
        for i in range(1, len(kiv)):
            dlogv = (math.log10(max(vv[i],1e-20)) - math.log10(max(vv[i-1],1e-20))) / (kiv[i]-kiv[i-1])
            slopes.append(dlogv)
        max_change = -1e9
        trans_idx = 0
        for i in range(1, len(slopes)):
            change = abs(slopes[i] - slopes[i-1])
            if change > max_change:
                max_change = change
                trans_idx = i
        recomputed_trans_ki = (kiv[trans_idx] + kiv[trans_idx-1]) / 2.0
    else:
        recomputed_trans_ki = None

    # 2. compute rP intersection
    sigma_ys = params.get('sigma_ys', 630)
    pi = math.pi
    best_ki = None
    best_diff = 1e9
    search_kis = [round(ki_crit[0] + i*0.01, 3) for i in range(int((ki_crit[-1]-ki_crit[0])/0.01)+1)]
    for ki in search_kis:
        lc = interp(ki, ki_crit, l_crit)  # µm
        rP = (1.0/(6*pi)) * ((ki / sigma_ys)**2) * 1e6  # µm
        diff = abs(rP - lc)
        if diff < best_diff:
            best_diff = diff
            best_ki = ki

    # 3. scoring
    tol_t = params.get('transition_KI_tolerance', 0.5)
    tol_r = params.get('rP_KI_tolerance', 0.5)

    # transition_KI
    if recomputed_trans_ki is not None:
        if abs(trans_ki - recomputed_trans_ki) <= tol_t:
            score += 0.4
        elif abs(trans_ki - recomputed_trans_ki) <= 2*tol_t:
            score += 0.2
    else:
        # just check plausible range 7-9
        if 7 <= trans_ki <= 9:
            score += 0.2

    # rP_KI
    if best_ki is not None:
        if abs(rp_ki - best_ki) <= tol_r:
            score += 0.4
        elif abs(rp_ki - best_ki) <= 2*tol_r:
            score += 0.2
    else:
        if 7 <= rp_ki <= 9:
            score += 0.2

    # comparison flag
    if comp is not None:
        diff_t = abs(trans_ki - (recomputed_trans_ki if recomputed_trans_ki else trans_ki))
        diff_r = abs(rp_ki - (best_ki if best_ki else rp_ki))
        consistent = diff_t <= tol_t and diff_r <= tol_r
        if comp == consistent:
            score += 0.2

    return round(min(score,1.0), 4)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
