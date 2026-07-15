import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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
    return {
        'output_dir': outputs_dir,
        'liquidus_data': spec['liquidus_data'],
        'gold_params': spec['gold_params'],
        'eutectic_gold': spec.get('eutectic_gold', {}),
        'R': 8.314,
    }


# === block: score_0 (check id='excess_gibbs_parameters') ===
def score_0(artifact, step, ctx):
    params = {}
    for row in artifact:
        p = row.get('parameter','').strip()
        v = row.get('value')
        try:
            v = float(v)
        except:
            v = None
        if p and v is not None:
            params[p] = v
    gold = ctx.get('gold_params', {})
    keys = ['A','B','C','D']
    scores = []
    for k in keys:
        v = params.get(k)
        g = gold.get(k)
        if v is None or g is None:
            scores.append(0.0)
            continue
        # for A,B tolerance is relative 5%; for C,D absolute 0.5
        if k in ('A','B'):
            tol = 0.05 * abs(g)
        else:
            tol = 0.5
        diff = abs(v - g)
        s = max(0.0, 1.0 - diff/tol) if tol > 0 else (1.0 if diff==0 else 0.0)
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='liquidus_consistency') ===
def score_1(artifact, step, ctx):
    import math

    import os
    import csv

    def bisect(f, a, b, tol=1e-6, maxiter=200):
        fa = f(a)
        fb = f(b)
        if fa * fb > 0:
            raise ValueError('Root not bracketed')
        if abs(fa) < tol:
            return a
        if abs(fb) < tol:
            return b
        for _ in range(maxiter):
            m = (a + b) / 2.0
            fm = f(m)
            if abs(fm) < tol:
                return m
            if fa * fm < 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm
        return (a + b) / 2.0

    out_dir = ctx['output_dir']
    param_file = os.path.join(out_dir, 'excess_gibbs_parameters.csv')
    if not os.path.exists(param_file):
        return 0.0
    params = {}
    with open(param_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = row['parameter'].strip()
            v = float(row['value'])
            params[p] = v
    A, B, C, D = params.get('A'), params.get('B'), params.get('C'), params.get('D')
    if None in (A, B, C, D):
        return 0.0

    gold = ctx['gold_params']
    gA, gB, gC, gD = gold['A'], gold['B'], gold['C'], gold['D']
    R = ctx.get('R', 8.314)
    exp_data = ctx['liquidus_data']
    eut_gold = ctx.get('eutectic_gold', {})
    eutectic_comp = eut_gold.get('composition_at_percent_Bi', 99.958)

    def delta_fusG_Ge(T):
        return 32940 + 23.4575*T + 3.6777e-3*T*T - 7.7613*T*math.log(T)

    def delta_fusG_Bi(T):
        return 4198 + 108.96*T + 15.234e-3*T*T - 19.9493*T*math.log(T) + 2.05e5/T

    def ex_deriv_Ge(x, a, b, c, d, T):
        L0 = a - c*T
        L1 = b - d*T
        return -((1-2*x)*(L0+L1*x) + (x-x*x)*L1)

    def ex_deriv_Bi(x, a, b, c, d, T):
        L0 = a - c*T
        L1 = b - d*T
        return (1-2*x)*(L0+L1*x) + (x-x*x)*L1

    def calc_liquidus_temp(x_bi_at_pct, a, b, c, d):
        x = x_bi_at_pct / 100.0
        if x <= 0:
            return 938.25 + 273.15
        if x >= 1:
            return 271.35 + 273.15
        if x_bi_at_pct < eutectic_comp:
            f = lambda T: delta_fusG_Ge(T) + R*T*math.log(max(1e-12, 1.0-x)) + ex_deriv_Ge(x, a, b, c, d, T)
        else:
            f = lambda T: delta_fusG_Bi(T) + R*T*math.log(max(1e-12, x)) + ex_deriv_Bi(x, a, b, c, d, T)
        try:
            T_low, T_high = 300.0, 2000.0
            for _ in range(5):
                if f(T_low)*f(T_high) < 0:
                    break
                T_high *= 1.5
            return bisect(f, T_low, T_high, tol=1e-6)
        except:
            return None

    # agent RMSD
    sq_agent = 0.0
    for pt in exp_data:
        tc = pt[0]
        comp = pt[1]
        Tp = calc_liquidus_temp(comp, A, B, C, D)
        err = 1000.0 if Tp is None else abs(Tp - 273.15 - tc)
        sq_agent += err*err
    rmsd_agent = math.sqrt(sq_agent/len(exp_data))

    # gold RMSD
    sq_gold = 0.0
    for pt in exp_data:
        tc = pt[0]
        comp = pt[1]
        Tp = calc_liquidus_temp(comp, gA, gB, gC, gD)
        err = 1000.0 if Tp is None else abs(Tp - 273.15 - tc)
        sq_gold += err*err
    rmsd_gold = math.sqrt(sq_gold/len(exp_data))

    if rmsd_agent <= rmsd_gold + 0.5:
        return 1.0
    return max(0.0, 1.0 - (rmsd_agent - rmsd_gold) / 10.0)


# === block: score_2 (check id='eutectic_point') ===
def score_2(artifact, step, ctx):
    props = {}
    for row in artifact:
        prop = row.get('property','').strip()
        val = row.get('value')
        try:
            val = float(val)
        except:
            val = None
        if prop and val is not None:
            props[prop] = val

    gold = ctx.get('eutectic_gold', {})
    # temperature
    T_agent = props.get('temperature_C')
    T_gold = gold.get('temperature_C', 271.35)
    tol_full_T = 0.1
    tol_zero_T = 1.0
    if T_agent is not None:
        diff_T = abs(T_agent - T_gold)
        if diff_T <= tol_full_T:
            sT = 1.0
        else:
            sT = max(0.0, 1.0 - (diff_T - tol_full_T)/(tol_zero_T - tol_full_T))
    else:
        sT = 0.0

    # composition
    C_agent = props.get('composition_at_percent_Bi')
    C_gold = gold.get('composition_at_percent_Bi', 99.958)
    tol_full_C = 0.005
    tol_zero_C = 0.05
    if C_agent is not None:
        diff_C = abs(C_agent - C_gold)
        if diff_C <= tol_full_C:
            sC = 1.0
        else:
            sC = max(0.0, 1.0 - (diff_C - tol_full_C)/(tol_zero_C - tol_full_C))
    else:
        sC = 0.0

    return 0.5*sT + 0.5*sC


_SCORERS = {
    'excess_gibbs_parameters': score_0,
    'liquidus_consistency': score_1,
    'eutectic_point': score_2,
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
