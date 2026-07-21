import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='barriers_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    for mat in ['Fe', 'Co']:
        if mat not in artifact:
            return 0.0
        sub = artifact[mat]
        if not isinstance(sub, dict):
            return 0.0
        if not all(k in sub for k in ['E1', 'E2', 'E3']):
            return 0.0
        if not all(isinstance(sub[k], (int, float)) for k in ['E1', 'E2', 'E3']):
            return 0.0
    return 1.0


# === block: score_1 (check id='barriers_values') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold = step['gold']
        tol_abs = step['tolerance']['abs']
        tol_rel = step['tolerance']['relative']
        correct = 0
        total = 0
        for mat in ['Fe','Co']:
            if mat not in artifact:
                continue
            for key in ['E1','E2','E3']:
                total += 1
                val = artifact[mat].get(key)
                ref = gold[mat][key]
                if val is None:
                    continue
                diff = abs(val - ref)
                if ref > 0.1:
                    if diff <= tol_abs:
                        correct += 1
                else:
                    if ref == 0.0:
                        if diff < 1e-9:
                            correct += 1
                    else:
                        if diff / ref <= tol_rel:
                            correct += 1
        if total == 0:
            return 0.0
        return correct / total


# === block: score_2 (check id='fe_csv_check') ===
def score_2(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        import os, json, math
        nu0 = step['nu0']
        kB = step['kB_meV']
        n_imp = step['n_improved']
        conditions = step['conditions']
        tol_ana = step['tolerance_analytical']
        tol_kMC = step['tolerance_kMC_rel']
        barriers_path = '/app/outputs/barriers.json'
        if not os.path.exists(barriers_path):
            return 0.0
        try:
            with open(barriers_path) as f:
                barriers = json.load(f)
            fe_bar = barriers['Fe']
        except Exception:
            return 0.0
        def tau_analytical(E1, E2, E3, T, N, n):
            exp1 = math.exp(-E1/(kB*T))
            exp2 = math.exp(-E2/(kB*T))
            exp3 = math.exp(-E3/(kB*T))
            nu1 = nu0 * exp1
            nu2 = nu0 * exp2
            nu3 = nu0 * exp3
            if nu2 + nu3 == 0:
                return None
            a = nu3 / (nu2 + nu3)
            if a <= 0 or a >= 1:
                return None
            term1 = (a / nu3) * ((N-1)/2.0) * (N - 2*(1-2*a)/(1-a))
            term2 = (1.0 / nu1) * (N*(1-a) - 2*(1-2*a))
            tau = (1.0 / (n * a)) * (term1 + term2)
            return tau
        row_map = {}
        for row in artifact:
            try:
                t = float(row['temperature_K'])
                n = int(row['chain_length_N'])
            except (KeyError, ValueError):
                continue
            row_map[(t,n)] = row
        row_scores = []
        for cond in conditions:
            t = cond['temperature_K']
            n = cond['chain_length_N']
            row = row_map.get((t, n))
            if row is None:
                row_scores.append(0.0)
                continue
            sc = []
            tau_a_exp = tau_analytical(fe_bar['E1'], fe_bar['E2'], fe_bar['E3'], t, n, n_imp)
            try:
                tau_a_agent = float(row['tau_analytical'])
            except:
                tau_a_agent = None
            if tau_a_exp is not None and tau_a_agent is not None and tau_a_exp > 0:
                if abs(tau_a_agent - tau_a_exp) / tau_a_exp <= tol_ana:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            tau_i_exp = tau_analytical(fe_bar['E1'], fe_bar['E2'], fe_bar['E3'], t, n, n_imp)
            try:
                tau_i_agent = float(row['tau_improvedI'])
            except:
                tau_i_agent = None
            if tau_i_exp is not None and tau_i_agent is not None and tau_i_exp > 0:
                ratio_i = tau_i_agent / tau_i_exp
                if 1.0/tol_kMC <= ratio_i <= tol_kMC:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            try:
                tau_s_agent = float(row['tau_simple'])
            except:
                tau_s_agent = None
            if (tau_s_agent is not None and tau_i_agent is not None
                    and tau_s_agent > 0 and tau_i_agent > 0):
                if tau_s_agent > tau_i_agent:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            row_scores.append(sum(sc) / len(sc) if sc else 0.0)
        if not row_scores:
            return 0.0
        return sum(row_scores) / len(row_scores)


# === block: score_3 (check id='co_csv_check') ===
def score_3(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        import os, json, math
        nu0 = step['nu0']
        kB = step['kB_meV']
        n_imp = step['n_improved']
        n_simp = step['n_simple']
        J_Co = step['J_Co']
        K_Co = step['K_Co']
        conditions = step['conditions']
        tol_ana = step['tolerance_analytical']
        tol_kMC = step['tolerance_kMC_rel']
        barriers_path = '/app/outputs/barriers.json'
        if not os.path.exists(barriers_path):
            return 0.0
        try:
            with open(barriers_path) as f:
                barriers = json.load(f)
            co_bar = barriers['Co']
        except Exception:
            return 0.0
        def tau_analytical_from_rates(nu1, nu2, nu3, N, n):
            if nu2 + nu3 == 0:
                return None
            a = nu3 / (nu2 + nu3)
            if a <= 0 or a >= 1:
                return None
            term1 = (a / nu3) * ((N-1)/2.0) * (N - 2*(1-2*a)/(1-a))
            term2 = (1.0 / nu1) * (N*(1-a) - 2*(1-2*a))
            tau = (1.0 / (n * a)) * (term1 + term2)
            return tau
        def tau_improved(E1, E2, E3, T, N, n):
            exp1 = math.exp(-E1/(kB*T))
            exp2 = math.exp(-E2/(kB*T))
            exp3 = math.exp(-E3/(kB*T))
            nu1 = nu0 * exp1
            nu2 = nu0 * exp2
            nu3 = nu0 * exp3
            return tau_analytical_from_rates(nu1, nu2, nu3, N, n)
        def tau_simple_co(T, N):
            exp2J = math.exp(-2*J_Co/(kB*T))
            nu1 = nu0 * exp2J
            nu2 = nu0
            nu3 = nu0 * math.exp(-K_Co/(kB*T))
            return tau_analytical_from_rates(nu1, nu2, nu3, N, n_simp)
        row_map = {}
        for row in artifact:
            try:
                t = float(row['temperature_K'])
                n = int(row['chain_length_N'])
            except (KeyError, ValueError):
                continue
            row_map[(t,n)] = row
        row_scores = []
        for cond in conditions:
            t = cond['temperature_K']
            n = cond['chain_length_N']
            row = row_map.get((t, n))
            if row is None:
                row_scores.append(0.0)
                continue
            sc = []
            N_eff = n - 10
            if N_eff <= 0:
                N_eff = 1
            tau_a_exp = tau_improved(co_bar['E1'], co_bar['E2'], co_bar['E3'], t, N_eff, n_imp)
            try:
                tau_a_agent = float(row['tau_analytical'])
            except:
                tau_a_agent = None
            if tau_a_exp is not None and tau_a_agent is not None and tau_a_exp > 0:
                if abs(tau_a_agent - tau_a_exp) / tau_a_exp <= tol_ana:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            tau_s_exp = tau_simple_co(t, n)
            try:
                tau_s_agent = float(row['tau_simple'])
            except:
                tau_s_agent = None
            if tau_s_exp is not None and tau_s_agent is not None and tau_s_exp > 0:
                ratio = tau_s_agent / tau_s_exp
                if 1.0/tol_kMC <= ratio <= tol_kMC:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            tau_i_exp = tau_improved(co_bar['E1'], co_bar['E2'], co_bar['E3'], t, N_eff, n_imp)
            try:
                tau_i_agent = float(row['tau_improvedII'])
            except:
                tau_i_agent = None
            if tau_i_exp is not None and tau_i_agent is not None and tau_i_exp > 0:
                ratio_i = tau_i_agent / tau_i_exp
                if 1.0/tol_kMC <= ratio_i <= tol_kMC:
                    sc.append(1.0)
                else:
                    sc.append(0.0)
            else:
                sc.append(0.0)
            row_scores.append(sum(sc) / len(sc) if sc else 0.0)
        if not row_scores:
            return 0.0
        return sum(row_scores) / len(row_scores)


_SCORERS = {
    'barriers_shape': score_0,
    'barriers_values': score_1,
    'fe_csv_check': score_2,
    'co_csv_check': score_3,
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
