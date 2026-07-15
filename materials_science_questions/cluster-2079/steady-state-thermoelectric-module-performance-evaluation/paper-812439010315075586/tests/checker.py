import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import statistics


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
    pass


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    rows = list(artifact)
    if len(rows) < 50:
        return 0.0
    xs = [float(r['x']) for r in rows]
    tgs = [float(r['T_gas']) for r in rows]
    # sub-checks
    scores = []
    # 1. row count >= 100
    scores.append(1.0 if len(rows) >= 100 else 0.0)
    # 2. cold junction temp (nearest x=2.5) >= 300
    def nearest_idx(vals, target):
        return min(range(len(vals)), key=lambda i: abs(vals[i]-target))
    idx_cj = nearest_idx(xs, 2.5)
    cold_junction = tgs[idx_cj]
    scores.append(1.0 if cold_junction >= 300.0 else 0.0)
    # 3. center region (x 5-10 cm) is the hottest and nearly constant
    center_idxs = [i for i,x in enumerate(xs) if 5.0 <= x <= 10.0]
    center_temps = []
    center_xs = []
    if center_idxs:
        center_temps = [tgs[i] for i in center_idxs]
        center_xs = [xs[i] for i in center_idxs]
    if not center_idxs or not center_temps:
        scores.append(0.0)
    else:
        global_max = max(tgs)
        mean_ct = statistics.mean(center_temps)
        std_ct = statistics.stdev(center_temps) if len(center_temps) > 1 else 0.0
        # center must contain the global maximum (plateau is the hottest)
        plateau_max_ok = 1.0 if any(t >= global_max - 1e-9 for t in center_temps) else 0.0
        # center must be hotter than cold junction (at least 10% higher)
        rel_hot_ok = 1.0 if mean_ct > 1.1 * max(cold_junction, 300.0) else 0.0
        # center should have small relative variation (< 10%)
        const_ok = 1.0 if mean_ct == 0 or std_ct / mean_ct < 0.1 else 0.0
        scores.append((plateau_max_ok + rel_hot_ok + const_ok) / 3.0)
    # 4. gradients in TE modules steeper than center
    te1_idxs = [i for i,x in enumerate(xs) if 2.5 <= x <= 5.0]
    te2_idxs = [i for i,x in enumerate(xs) if 10.0 <= x <= 12.5]
    grads = []
    for te_idxs in [te1_idxs, te2_idxs]:
        if len(te_idxs) >= 2:
            te_temps = [tgs[i] for i in te_idxs]
            te_dx = xs[te_idxs[-1]] - xs[te_idxs[0]]
            if te_dx > 0:
                grads.append(abs(te_temps[-1] - te_temps[0]) / te_dx)
    center_dx = max(center_xs) - min(center_xs) if center_xs else 1.0
    center_grad = (max(center_temps) - min(center_temps)) / center_dx if center_dx > 0 else 0
    steeper = all(g > center_grad for g in grads) if grads else False
    scores.append(1.0 if steeper else 0.0)
    # 5. outlet temp (nearest x=12.5) < center max
    idx_out = nearest_idx(xs, 12.5)
    outlet_temp = tgs[idx_out]
    max_center = max(center_temps) if center_temps else outlet_temp
    scores.append(1.0 if outlet_temp < max_center else 0.0)
    # 6. file columns exist
    scores.append(1.0)
    weights = [0.05, 0.15, 0.25, 0.25, 0.15, 0.05]
    total = sum(w * s for w, s in zip(weights, scores))
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='step_3') ===
def score_1(artifact, step, ctx):
    rows = list(artifact)
    if len(rows) < 50:
        return 0.0
    # parse fields
    fields = ['current_density','V_Bat','u','epsilon','T_heating','T_outlet']
    data = [{k: float(r[k]) for k in fields} for r in rows]
    # group by conditions
    from collections import defaultdict
    groups = defaultdict(list)
    for d in data:
        # key: (V_Bat, u, epsilon)
        groups[(d['V_Bat'], d['u'], d['epsilon'])].append(d)
    # 1. monotonic increase of T_heating with current_density within each group
    mono_inc = 0
    for g in groups.values():
        g_sorted = sorted(g, key=lambda d: d['current_density'])
        if len(g_sorted) < 2:
            continue
        inc = all(g_sorted[i]['T_heating'] <= g_sorted[i+1]['T_heating'] for i in range(len(g_sorted)-1))
        if inc:
            mono_inc += 1
    frac_mono_inc = mono_inc / len(groups) if groups else 0.0
    # 2. for fixed V_Bat=12.036 and epsilon=0.5, T_heating decreases with u
    # gather group-level means for each u
    fixed_v, fixed_eps = 12.036, 0.5
    g_u = defaultdict(list)
    for d in data:
        if d['V_Bat'] == fixed_v and d['epsilon'] == fixed_eps:
            g_u[d['u']].append(d['T_heating'])
    u_sorted = sorted(g_u.items())
    if len(u_sorted) >= 2:
        dec_u = all(statistics.mean(u_sorted[i][1]) >= statistics.mean(u_sorted[i+1][1]) for i in range(len(u_sorted)-1))
    else:
        dec_u = True  # insufficient data, no penalty
    score_u = 1.0 if dec_u else 0.0
    # 3. for fixed V_Bat=12.036 and u=0.35, T_heating decreases with epsilon
    fixed_u = 0.35
    g_eps = defaultdict(list)
    for d in data:
        if d['V_Bat'] == fixed_v and d['u'] == fixed_u:
            g_eps[d['epsilon']].append(d['T_heating'])
    eps_sorted = sorted(g_eps.items())
    if len(eps_sorted) >= 2:
        dec_eps = all(statistics.mean(eps_sorted[i][1]) >= statistics.mean(eps_sorted[i+1][1]) for i in range(len(eps_sorted)-1))
    else:
        dec_eps = True
    score_eps = 1.0 if dec_eps else 0.0
    # 4. T_heating > T_outlet for most rows
    n_greater = sum(1 for d in data if d['T_heating'] > d['T_outlet'])
    prop_greater = n_greater / len(data) if data else 0.0
    score_greater = 1.0 if prop_greater >= 0.9 else 0.0
    # combine weights
    weights = [0.1, 0.3, 0.2, 0.2, 0.2]
    scores = [1.0 if len(rows) >= 50 else 0.0, frac_mono_inc, score_u, score_eps, score_greater]
    total = sum(w * s for w, s in zip(weights, scores))
    return max(0.0, min(1.0, total))


# === block: score_2 (check id='step_4') ===
def score_2(artifact, step, ctx):
    rows = list(artifact)
    if len(rows) < 5:
        return 0.0
    data = []
    for r in rows:
        dT = float(r['delta_T0'])
        cop = float(r['COP'])
        data.append((dT, cop))
    data.sort(key=lambda x: x[0])
    # check monotonic decrease
    mono_dec = all(data[i][1] >= data[i+1][1] for i in range(len(data)-1))
    score_mono = 1.0 if mono_dec else 0.0
    # sanity: COP values between 0 and 20
    cops = [c for _, c in data]
    score_sanity = 1.0 if all(0 <= c <= 20 for c in cops) else 0.0
    # enough rows
    score_rows = 1.0 if len(rows) >= 5 else 0.0
    weights = [0.1, 0.8, 0.1]
    scores = [score_rows, score_mono, score_sanity]
    total = sum(w * s for w, s in zip(weights, scores))
    return max(0.0, min(1.0, total))


_SCORERS = {
    'step_2': score_0,
    'step_3': score_1,
    'step_4': score_2,
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
