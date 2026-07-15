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
    steps = spec.get('steps', [])
    ctx = {'steps': steps}
    return ctx


# === block: score_0 (check id='defect_energy_diff') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # parse rows
    pressures = []
    vals_283 = []
    vals_732 = []
    for r in rows:
        try:
            p = float(r['pressure_GPa'])
            dg = float(r['delta_G_eV'])
            c = r['concentration'].strip()
        except (KeyError, ValueError):
            continue
        if c == '283_ppb':
            pressures.append(p)
            vals_283.append((p, dg))
        elif c == '732_ppm':
            vals_732.append((p, dg))
    sort283 = sorted(vals_283, key=lambda x: x[0])
    sort732 = sorted(vals_732, key=lambda x: x[0])
    # reject constant (flat) submissions: delta_G must vary with pressure
    min_range = 0.01  # eV
    if len(sort283) >= 2:
        r283 = sort283[-1][1] - sort283[0][1]
    else:
        r283 = 0.0
    if len(sort732) >= 2:
        r732 = sort732[-1][1] - sort732[0][1]
    else:
        r732 = 0.0
    if abs(r283) < min_range or abs(r732) < min_range:
        return 0.0
    # sign check: for 283_ppb, all delta_G must be negative (since P >= 25 GPa, above crossover)
    if sort283:
        sign_ok = 0
        sign_total = len(sort283)
        for _, dg in sort283:
            if dg < 0:
                sign_ok += 1
        sign_score = sign_ok / sign_total if sign_total > 0 else 1.0
    else:
        sign_score = 1.0
    # monotonicity for each concentration
    mono_score = 0.5
    if len(sort283) >= 2:
        dec = all(sort283[i][1] <= sort283[i-1][1] for i in range(1, len(sort283)))
        mono_score += 0.25 if dec else 0.0
    if len(sort732) >= 2:
        dec2 = all(sort732[i][1] <= sort732[i-1][1] for i in range(1, len(sort732)))
        mono_score += 0.25 if dec2 else 0.0
    # concentration ordering: at same pressure, 732 <= 283
    ord_cnt = 0
    ord_total = 0
    for p1, dg283 in sort283:
        for p2, dg732 in sort732:
            if abs(p1 - p2) < 0.1:
                ord_total += 1
                if dg732 <= dg283 + 1e-9:
                    ord_cnt += 1
    ord_score = ord_cnt / max(1, ord_total) if ord_total > 0 else 1.0
    total_score = 0.4 * sign_score + 0.3 * mono_score + 0.3 * ord_score
    return min(max(total_score, 0.0), 1.0)


# === block: score_1 (check id='partition_coeff') ===
def score_1(artifact, step, ctx):
    rows = artifact
    step = ctx.get('current_step', {})
    gold_list = step.get('gold_log10', [])
    if not gold_list:
        return 0.0
    # index gold by (P,T)
    gold_dict = {}
    for g in gold_list:
        gold_dict[(g['P'], g['T'])] = g['log10']
    # collect submitted values
    submitted = {}
    for r in rows:
        try:
            p = float(r['pressure_GPa'])
            t = float(r['temperature_K'])
            d = float(r['D_Hf'])
        except (KeyError, ValueError):
            continue
        if d <= 0:
            continue
        submitted[(p, t)] = math.log10(d)
    # compare each gold point
    tol_max = step.get('log10_tolerance_max', 0.3)
    tol_zero = step.get('log10_tolerance_zero', 1.0)
    if tol_zero <= tol_max:
        tol_zero = tol_max + 0.01
    n = len(gold_dict)
    if n == 0:
        return 0.0
    acc = 0.0
    for key, gold_log in gold_dict.items():
        sub_log = submitted.get(key)
        if sub_log is None:
            continue
        diff = abs(sub_log - gold_log)
        if diff <= tol_max:
            acc += 1.0
        else:
            # linear decay to zero at tol_zero
            frac = max(0.0, (tol_zero - diff) / (tol_zero - tol_max))
            acc += frac
    tol_score = acc / n
    # monotonicity trend within each temperature
    temps = sorted(set(t for _,t in gold_dict.keys()))
    trend_ok = 0
    trend_total = 0
    for T in temps:
        pts = sorted([p for p,t in gold_dict.keys() if t==T])
        if len(pts) < 2:
            continue
        vals = [10**submitted.get((p,T), math.nan) for p in pts]
        if any(math.isnan(v) for v in vals):
            continue
        trend_total += 1
        if all(vals[i] >= vals[i-1] for i in range(1, len(vals))):
            trend_ok += 1
    trend_score = trend_ok / max(1, trend_total) if trend_total > 0 else 1.0
    final = 0.75 * tol_score + 0.25 * trend_score
    return min(max(final, 0.0), 1.0)


# === block: score_2 (check id='tungsten_anomaly') ===
def score_2(artifact, step, ctx):
    rows = artifact
    step = ctx.get('current_step', {})
    gold_ts = step.get('gold_timeseries', {})
    if not gold_ts:
        return 0.0
    tol_frac = step.get('relative_tolerance', 0.3)
    # parse rows into time-indexed dict
    index = {}
    for r in rows:
        try:
            t = float(r['time_Myr'])
            s = float(r['mu182W_solid_ppm'])
            l = float(r['mu182W_liquid_ppm'])
        except (KeyError, ValueError):
            continue
        index[t] = (s, l)
    # check sampled gold times
    sample_times = sorted([float(k) for k in gold_ts.keys()])
    n = len(sample_times)
    if n == 0:
        return 0.0
    total_err = 0.0
    count = 0
    for t in sample_times:
        if t not in index:
            continue
        g = gold_ts[str(int(t)) if t == int(t) else str(t)]
        gold_s = float(g['solid'])
        gold_l = float(g['liquid'])
        comp_s, comp_l = index[t]
        # relative error (avoid division by zero)
        if abs(gold_s) < 1e-9:
            err_s = abs(comp_s - gold_s)
        else:
            err_s = abs(comp_s - gold_s) / (abs(gold_s) + 1e-9)
        if abs(gold_l) < 1e-9:
            err_l = abs(comp_l - gold_l)
        else:
            err_l = abs(comp_l - gold_l) / (abs(gold_l) + 1e-9)
        # score for this point: 1 if within tolerance, linear decay
        score_s = max(0.0, 1.0 - err_s / tol_frac) if tol_frac > 0 else 1.0 if err_s == 0 else 0.0
        score_l = max(0.0, 1.0 - err_l / tol_frac)
        total_err += (score_s + score_l) / 2.0
        count += 1
    if count == 0:
        return 0.0
    final = total_err / count
    return min(max(final, 0.0), 1.0)


_SCORERS = {
    'defect_energy_diff': score_0,
    'partition_coeff': score_1,
    'tungsten_anomaly': score_2,
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
