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


# === block: score_0 (check id='step_01_chi_peak') ===
def score_0(artifact, step, ctx):
    refs = step['reference_values']
    tolerance = step.get('tolerance_relative', 0.20)
    trend_weight = step.get('trend_score_weight', 0.3)
    acc_weight = 1.0 - trend_weight
    # numeric accuracy
    acc = 0.0
    count = 0
    for entry in artifact:
        ut = entry.get('U_t')
        n = entry.get('n')
        chi = entry.get('chi_pi_pi')
        gold = None
        for ref in refs:
            if ref['U_t'] == ut and ref['n'] == n:
                gold = ref['chi_pi_pi']
                break
        if gold is None:
            continue
        rel_err = abs(chi - gold) / (abs(gold) + 1e-12)
        acc += max(0.0, 1.0 - rel_err / tolerance)
        count += 1
    if count > 0:
        acc /= count
    else:
        acc = 0.0
    # trend checks
    ut_vals = sorted(list({e['U_t'] for e in artifact}))
    n_vals = sorted(list({e['n'] for e in artifact}))
    chi_map = {}
    for e in artifact:
        chi_map[(e['U_t'], e['n'])] = e['chi_pi_pi']
    trend_violations = 0
    # for each n, check chi increases with U
    for n in n_vals:
        for i in range(len(ut_vals)-1):
            u1 = ut_vals[i]; u2 = ut_vals[i+1]
            if (u1,n) in chi_map and (u2,n) in chi_map:
                if chi_map[(u1,n)] > chi_map[(u2,n)]:
                    trend_violations += 1
    # for each U, check chi increases as n decreases (i.e., lower n gives larger chi)
    for u in ut_vals:
        for i in range(len(n_vals)-1):
            n1 = n_vals[i]; n2 = n_vals[i+1]
            if (u,n1) in chi_map and (u,n2) in chi_map:
                if chi_map[(u,n1)] > chi_map[(u,n2)]:
                    trend_violations += 1
    trend_score = max(0.0, 1.0 - 0.2 * trend_violations)
    return acc_weight * acc + trend_weight * trend_score


# === block: score_1 (check id='step_02_pairing_suscept') ===
def score_1(artifact, step, ctx):
    refs = step['reference_entries']
    tolerance = step.get('tolerance_relative', 0.30)
    trend_weight = step.get('trend_score_weight', 0.5)
    acc_weight = 1.0 - trend_weight
    # numeric accuracy for P and P_eff
    acc = 0.0
    count = 0
    for entry in artifact:
        temp = entry.get('temperature')
        sym = entry.get('symmetry')
        n = entry.get('n')
        p = entry.get('P')
        p_eff = entry.get('P_eff')
        gold = None
        for ref in refs:
            if (ref['temperature'] == temp and ref['symmetry'] == sym and ref['n'] == n):
                gold = ref
                break
        if gold is None:
            continue
        rel_err_P = abs(p - gold['P_target']) / (abs(gold['P_target']) + 1e-12)
        rel_err_eff = abs(p_eff - gold['P_eff_target']) / (abs(gold['P_eff_target']) + 1e-12)
        entry_score = (max(0.0, 1.0 - rel_err_P / tolerance) + max(0.0, 1.0 - rel_err_eff / tolerance)) / 2.0
        acc += entry_score
        count += 1
    if count > 0:
        acc /= count
    else:
        acc = 0.0
    # trend checks
    trend_score = 0.0
    if artifact:
        # Find lowest temperature for each n
        temps = sorted(list({e['temperature'] for e in artifact}))
        if temps:
            lowest_T = temps[-1]
            # For each n at lowest T, verify dxy has max P_eff
            ns = set(e['n'] for e in artifact)
            dxy_largest = True
            for n_val in ns:
                subset = [e for e in artifact if e['temperature'] == lowest_T and e['n'] == n_val]
                if not subset:
                    continue
                p_effs = {e['symmetry']: e['P_eff'] for e in subset}
                if 'dxy' not in p_effs:
                    dxy_largest = False
                    break
                max_val = max(p_effs.values())
                if p_effs['dxy'] < max_val - 1e-9:
                    dxy_largest = False
                    break
            # check dxy P_eff positivity
            dxy_pos = all(e['P_eff'] > -1e-9 for e in artifact if e['symmetry'] == 'dxy')
            # check dxy P_eff increases as temperature decreases
            dxy_entries = sorted([e for e in artifact if e['symmetry'] == 'dxy'], key=lambda x: x['temperature'])
            if len(dxy_entries) >= 2:
                increasing = all(dxy_entries[i]['P_eff'] <= dxy_entries[i+1]['P_eff'] + 1e-9 for i in range(len(dxy_entries)-1))
            else:
                increasing = True
            trend_score = (int(dxy_largest) + int(dxy_pos) + int(increasing)) / 3.0
    return acc_weight * acc + trend_weight * trend_score


# === block: score_2 (check id='step_03_AFM_structure_factor') ===
def score_2(artifact, step, ctx):
    refs = step['reference_values']
    tolerance = step.get('tolerance_relative', 0.30)
    trend_weight = step.get('trend_score_weight', 0.4)
    acc_weight = 1.0 - trend_weight
    # filter entries with beta=10
    subset = [e for e in artifact if e.get('beta') == 10.0]
    if not subset:
        return 0.0
    # numeric accuracy
    acc = 0.0
    count = 0
    for entry in subset:
        L = entry['L']
        safm = entry['S_AFM']
        gold = None
        for ref in refs:
            if ref['L'] == L:
                gold = ref['S_AFM']
                break
        if gold is None:
            continue
        rel_err = abs(safm - gold) / (abs(gold) + 1e-12)
        acc += max(0.0, 1.0 - rel_err / tolerance)
        count += 1
    if count > 0:
        acc /= count
    else:
        acc = 0.0
    # trend: check monotonic decrease with L
    sorted_subset = sorted(subset, key=lambda x: x['L'])
    if len(sorted_subset) >= 2:
        trend_ok = all(sorted_subset[i]['S_AFM'] >= sorted_subset[i+1]['S_AFM'] - 1e-9 for i in range(len(sorted_subset)-1))
    else:
        trend_ok = True
    trend_score = 1.0 if trend_ok else 0.0
    return acc_weight * acc + trend_weight * trend_score


# === block: score_3 (check id='step_04_CDW_charge_correlation') ===
def score_3(artifact, step, ctx):
    tolerance = step.get('tolerance_relative', 0.30)
    gold_val = step['gold_value']['C_pi_pi']
    agent_val = artifact.get('C_pi_pi', None)
    if agent_val is None:
        return 0.0
    rel_err = abs(agent_val - gold_val) / (abs(gold_val) + 1e-12)
    return max(0.0, 1.0 - rel_err / tolerance)


_SCORERS = {
    'step_01_chi_peak': score_0,
    'step_02_pairing_suscept': score_1,
    'step_03_AFM_structure_factor': score_2,
    'step_04_CDW_charge_correlation': score_3,
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
