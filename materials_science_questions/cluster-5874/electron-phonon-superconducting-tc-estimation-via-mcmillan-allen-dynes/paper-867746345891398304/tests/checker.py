import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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
    def recompute_lambda_omega_log(energy, alpha2F):
        if len(energy) < 2: return None, None
        de = (energy[-1] - energy[0]) / (len(energy)-1) if len(energy)>1 else 0.0
        if de <= 0: return None, None
        lam = 0.0
        sum_log = 0.0
        for e, a in zip(energy, alpha2F):
            if e <= 0: continue
            lam += (a / e) * de
            sum_log += (a * math.log(e) / e) * de
        lam *= 2.0
        if lam < 1e-12: return lam, 0.0
        omega_log = math.exp((2.0/lam) * sum_log)
        return lam, omega_log

    ctx = {}

    # Load step_01 alpha2F data
    alpha2f_path = os.path.join('/app/outputs', 'step_01_alph2F_data.json')
    alpha2f_data = {}
    if os.path.exists(alpha2f_path):
        with open(alpha2f_path, 'r') as f:
            alpha2f_data = json.load(f)

    ctx['recomputed'] = {}
    for comp in ['TaB2','VB2','NbB2','TiB2','YB2']:
        comp_data = alpha2f_data.get(comp, {})
        energy = comp_data.get('energy', [])
        alpha2f = comp_data.get('alpha2F', [])
        if isinstance(energy, list) and isinstance(alpha2f, list) and len(energy)==len(alpha2f) and len(energy)>0:
            lam, wlog = recompute_lambda_omega_log(energy, alpha2f)
            ctx['recomputed'].setdefault('lambda', {})[comp] = lam
            ctx['recomputed'].setdefault('omega_log', {})[comp] = wlog
        else:
            ctx['recomputed'].setdefault('lambda', {})[comp] = None
            ctx['recomputed'].setdefault('omega_log', {})[comp] = None

    # Load step_02 CSV
    csv_path = os.path.join('/app/outputs', 'step_02_elph_params.csv')
    agent_params = []
    if os.path.exists(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                agent_params.append(row)
    ctx['agent_params'] = agent_params
    ctx['agent_tc'] = {}
    for row in agent_params:
        comp = row.get('compound', '')
        try:
            tc = float(row.get('Tc', 0))
        except:
            tc = None
        ctx['agent_tc'][comp] = tc

    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def score_with_tolerance(val, gold, rel_tol):
        if val is None or gold is None or gold == 0:
            return 0.0
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= rel_tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (rel_err - rel_tol) / (2 * rel_tol))

    lambda_gold = step.get('lambda_gold', {})
    omega_log_gold = step.get('omega_log_gold', {})
    lambda_tol = step.get('lambda_rel_tol', 0.2)
    omega_log_tol = step.get('omega_log_rel_tol', 0.15)
    compounds = ['TaB2','VB2','NbB2','TiB2','YB2']
    score_sum = 0.0
    count = 0
    for comp in compounds:
        lam = ctx['recomputed']['lambda'].get(comp)
        wlog = ctx['recomputed']['omega_log'].get(comp)
        gold_lam = lambda_gold.get(comp)
        gold_wlog = omega_log_gold.get(comp)
        s_lam = score_with_tolerance(lam, gold_lam, lambda_tol) if lam is not None else 0.0
        s_wlog = score_with_tolerance(wlog, gold_wlog, omega_log_tol) if wlog is not None else 0.0
        score_sum += (s_lam + s_wlog)
        count += 2
    if count > 0:
        return score_sum / count
    else:
        return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    tc_gold = step.get('tc_gold', {})
    tc_abs_tol = step.get('tc_abs_tol', 5.0)
    tc_rel_tol = step.get('tc_rel_tol', 0.5)
    trend_weight = step.get('trend_check_weight', 0.2)
    compounds = ['TaB2','VB2','NbB2','TiB2','YB2']
    tc_scores = []
    for comp in compounds:
        agent_tc = ctx.get('agent_tc', {}).get(comp)
        gold = tc_gold.get(comp)
        if agent_tc is None or gold is None:
            tc_scores.append(0.0)
            continue
        eff_tol = tc_abs_tol
        if gold > 0:
            eff_tol = max(tc_abs_tol, tc_rel_tol * gold)
        diff = abs(agent_tc - gold)
        if diff <= eff_tol:
            tc_scores.append(1.0)
        else:
            tc_scores.append(max(0.0, 1.0 - (diff - eff_tol) / (2*eff_tol)))
    avg_tc_score = sum(tc_scores)/len(tc_scores) if tc_scores else 0.0

    lam = ctx['recomputed']['lambda']
    tc_agent = ctx['agent_tc']
    total_ineq = 0
    trend_ok = 0
    # Check TiB2 has lowest lambda and Tc
    for other in ['TaB2','NbB2','VB2','YB2']:
        if lam.get('TiB2') is not None and lam.get(other) is not None:
            total_ineq += 1
            if lam['TiB2'] < lam[other]:
                trend_ok += 1
        if tc_agent.get('TiB2') is not None and tc_agent.get(other) is not None:
            total_ineq += 1
            if tc_agent['TiB2'] <= tc_agent[other]:
                trend_ok += 1
    # Check selected pairwise inequalities (TaB2/NbB2 higher than VB2/TiB2)
    for comp_high, comp_low in [('TaB2','TiB2'),('TaB2','VB2'),('NbB2','TiB2'),('NbB2','VB2')]:
        if lam.get(comp_high) is not None and lam.get(comp_low) is not None:
            total_ineq += 1
            if lam[comp_high] > lam[comp_low]:
                trend_ok += 1
        if tc_agent.get(comp_high) is not None and tc_agent.get(comp_low) is not None:
            total_ineq += 1
            if tc_agent[comp_high] > tc_agent[comp_low]:
                trend_ok += 1
    trend_score = trend_ok / total_ineq if total_ineq > 0 else 0.0

    total_score = (1.0 - trend_weight) * avg_tc_score + trend_weight * trend_score
    return total_score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
