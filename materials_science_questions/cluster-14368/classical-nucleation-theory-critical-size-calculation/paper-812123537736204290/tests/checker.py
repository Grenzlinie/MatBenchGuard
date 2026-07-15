import os
import json
import csv

# === author imports / helpers ===
import math, csv


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
    const = spec['physics_constants']
    stars = spec.get('star_data', [])

    def compute_gold(Rsun, v_km):
        logR = math.log10(Rsun)
        logV = math.log10(v_km / 100.0)
        logA_caseA = 1.03 * logR + 1.97 * logV - 1.29
        A_caseA = 10.0 ** logA_caseA
        logA_caseB = 1.07 * logR + 1.94 * logV - 1.03
        A_caseB = 10.0 ** logA_caseB
        return A_caseA, A_caseB

    stars_gold = {}
    for s in stars:
        name = s['Star']
        Aa, Ab = compute_gold(s['R0_Rsun'], s['v0_kms'])
        stars_gold[name] = {'caseA': Aa, 'caseB': Ab}

    ctx = {
        'constants': const,
        'stars_gold': stars_gold,
        'star_names': [s['Star'] for s in stars]
    }
    return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    if len(artifact) == 0:
        return 0.0

    const = ctx['constants']
    k_B = const['k_B']
    m_C = const['m_C']
    Omega = const['Omega']
    sigma = const['sigma']
    X_C = const['X_C']
    alpha = const['alpha']
    gamma_v = const['gamma_v']
    delta_v = const['delta_v']

    rel_tol = 1e-5
    huge = 1e98

    total = 0.0
    n_rows = len(artifact)
    for row in artifact:
        try:
            T = float(row['T'])
            rho = float(row['rho'])
            tau_sub = float(row['tau_n'])
        except Exception:
            continue

        # recompute tau_n
        n_C = rho * X_C / m_C
        P_C = n_C * k_B * T
        log10_Pv = -gamma_v / T + delta_v
        P_v = 10.0 ** log10_Pv
        S = P_C / P_v
        if S <= 1.0:
            tau_exp = huge
        else:
            lnS = math.log(S)
            r_star = 2.0 * sigma * Omega / (k_B * T * lnS)
            dG_kT = (16.0 * math.pi / 3.0) * (Omega**2 * sigma**3) / ((k_B * T)**3 * (lnS**2))
            Z = Omega * math.sqrt(4.0 * sigma / (k_B * T)) / (4.0 * math.pi * r_star**2)
            f = P_C / math.sqrt(2.0 * math.pi * m_C * k_B * T)
            try:
                exp_term = math.exp(-dG_kT)
            except OverflowError:
                exp_term = 0.0
            J = alpha * Z * 4.0 * math.pi * r_star**2 * f * n_C * exp_term
            g_star = (4.0 * math.pi / 3.0) * r_star**3 / Omega
            denom = g_star * J
            if denom == 0.0:
                tau_exp = huge
            else:
                tau_exp = n_C / denom

        # compare
        if tau_exp >= huge:
            if tau_sub >= huge:
                total += 1.0
        else:
            if tau_exp == 0.0:
                continue
            rel_err = abs(tau_sub - tau_exp) / abs(tau_exp)
            if rel_err <= rel_tol:
                total += 1.0

    score = total / n_rows if n_rows > 0 else 0.0
    return score


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    stars_gold = ctx['stars_gold']
    tol_log = 0.05

    star_rows = {}
    for row in artifact:
        name = row.get('Star', '').strip()
        if name:
            star_rows[name] = row

    total_score = 0.0
    n_stars = len(stars_gold)
    if n_stars == 0:
        return 0.0

    for name, gold in stars_gold.items():
        row = star_rows.get(name)
        if not row:
            continue
        try:
            A_sub_A = float(row['A_required_caseA_1e-7Msun_per_yr'])
            A_sub_B = float(row['A_required_caseB_1e-7Msun_per_yr'])
        except Exception:
            continue

        # score per star as average of two case scores
        sc = 0.0
        # Case A
        if gold['caseA'] > 0 and A_sub_A > 0:
            diffA = abs(math.log10(A_sub_A) - math.log10(gold['caseA']))
            if diffA <= tol_log:
                sc += 0.5
        # Case B
        if gold['caseB'] > 0 and A_sub_B > 0:
            diffB = abs(math.log10(A_sub_B) - math.log10(gold['caseB']))
            if diffB <= tol_log:
                sc += 0.5

        total_score += sc

    final = total_score / n_stars
    return final


_SCORERS = {
    'step_02': score_0,
    'step_04': score_1,
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
