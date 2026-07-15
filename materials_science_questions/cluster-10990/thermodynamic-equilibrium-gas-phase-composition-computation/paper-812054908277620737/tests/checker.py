import os
import json
import csv

# === author imports / helpers ===
import csv, math, collections


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
        R = 8.314462618
        species = {
            'SiO2(cr)':  {'delta_Hf': -909.48, 'A': 64.973,  'B': -11.198, 'C': -37.360, 'D':17.089,  'E':-0.196, 'F':-916.265, 'G':64.801, 'H':-909.48},
            'Si(l)':     {'delta_Hf': 50.2,    'A': 27.136,  'B': 0.0,      'C': 0.0,     'D':0.0,     'E':0.0,    'F':-4.523,   'G':33.023, 'H':50.2},
            'O2':        {'delta_Hf': 0.0,     'A': 31.32234,'B':-20.23531, 'C':57.86644, 'D':-36.50624,'E':-0.007374,'F':-9.59575, 'G':246.794,'H':0.0},
            'SiO':       {'delta_Hf': -100.0,  'A': 37.071,  'B': -5.449,   'C': -3.723,  'D':3.601,   'E':0.017,   'F':-107.48,  'G':229.27, 'H':-100.0},
            'Si3N4':     {'delta_Hf': -743.5,  'A': 76.661,  'B': 45.764,   'C':-57.529,  'D':18.163,  'E':0.0,     'F':-791.640, 'G':113.344,'H':-743.5},
            'Al2O3':     {'delta_Hf': -1675.694,'A': 104.927, 'B': 11.987,   'C':-37.229,  'D':7.221,   'E':-0.882,  'F':-1711.882,'G':64.781, 'H':-1675.694},
            'AlN':       {'delta_Hf': -317.984,'A': 44.620,  'B': 13.444,   'C':-10.465,  'D':3.036,   'E':-0.218,  'F':-326.095, 'G':34.213, 'H':-317.984},
            'Al2O':      {'delta_Hf': -130.0,  'A': 59.307,  'B': 1.275,    'C': -1.063,  'D':0.301,   'E':-0.091,  'F':-136.606, 'G':284.004,'H':-130.0},
            'N2':        {'delta_Hf': 0.0,     'A': 28.98641,'B': 1.853978,'C': -9.647459,'D':16.63537,'E':0.000117,'F':-8.671914,'G':226.4168,'H':0.0},
        }

        def safe_exp(x):
            """Safe exponential to avoid OverflowError."""
            if x > 700:
                return float('inf')
            if x < -700:
                return 0.0
            return math.exp(x)

        def gibbs(spec, T):
            d = species[spec]
            t = T / 1000.0
            H_diff = (d['A']*t + d['B']*t*t/2.0 + d['C']*t*t*t/3.0 + d['D']*t*t*t*t/4.0 - d['E']/t) / 1000.0 + (d['F'] - d['H'])
            S = (d['A']*math.log(t) + d['B']*t + d['C']*t*t/2.0 + d['D']*t*t*t/3.0 - d['E']/(2.0*t*t)) + d['G']*1000.0
            G_rel = H_diff - T * S / 1000.0
            return d['delta_Hf'] + G_rel

        def compute_K(rid, T, P_N2_bar=None):
            # returns K (bar^-dnu where dnu = #gas products - #gas reactants, but we don't need that)
            # Use stoichiometry from solve.sh
            if rid == 1:
                dG = (gibbs('Si(l)', T) + gibbs('O2', T)) - gibbs('SiO2(cr)', T)
            elif rid == 2:
                dG = (gibbs('SiO', T) + 0.5*gibbs('O2', T)) - gibbs('SiO2(cr)', T)
            elif rid == 3:
                dG = (2*gibbs('SiO', T) + 2*gibbs('Si(l)', T) + 2*gibbs('N2', T)) - (gibbs('Si3N4', T) + gibbs('SiO2(cr)', T))
            elif rid == 4:
                dG = (3*gibbs('SiO', T) + 2*gibbs('AlN', T) + gibbs('N2', T)) - (gibbs('Si3N4', T) + gibbs('Al2O3', T))
            elif rid == 5:
                dG = (6*gibbs('SiO', T) + 2*gibbs('N2', T)) - (gibbs('Si3N4', T) + 3*gibbs('SiO2(cr)', T))
            elif rid == 6:
                dG = (gibbs('SiO', T) + gibbs('Al2O', T) + gibbs('N2', T)) - (2*gibbs('AlN', T) + gibbs('SiO2(cr)', T))
            else:
                raise ValueError('Unknown reaction')
            K = safe_exp(-dG * 1000.0 / (R * T))
            return K

        def expected_log10(rid, T, P_N2_bar=None):
            """Returns dict formula -> log10(partial pressure bar)"""
            if rid in (1, 2):
                K = compute_K(rid, T)
                if rid == 1:
                    return {'O2': math.log10(K) if K>0 else -99.0}
                else:
                    if K>0:
                        p_SiO = (K**2 * 2) ** (1.0/3.0)
                        p_O2 = 0.5 * p_SiO
                        return {'SiO': math.log10(p_SiO), 'O2': math.log10(p_O2)}
                    else:
                        return {'SiO': -99.0, 'O2': -99.0}
            else:
                K = compute_K(rid, T)
                if P_N2_bar is None:
                    P_N2_bar = 1.01325  # default
                if rid == 3:
                    p_SiO = math.sqrt(K) / P_N2_bar if K>0 else 0.0
                    return {'SiO': math.log10(p_SiO) if p_SiO>0 else -99.0, 'N2': math.log10(P_N2_bar)}
                elif rid == 4:
                    p_SiO = (K / P_N2_bar) ** (1.0/3.0) if K>0 else 0.0
                    return {'SiO': math.log10(p_SiO) if p_SiO>0 else -99.0, 'N2': math.log10(P_N2_bar)}
                elif rid == 5:
                    p_SiO = K ** (1.0/6.0) / (P_N2_bar ** (1.0/3.0)) if K>0 else 0.0
                    return {'SiO': math.log10(p_SiO) if p_SiO>0 else -99.0, 'N2': math.log10(P_N2_bar)}
                elif rid == 6:
                    if K>0:
                        p_SiO = math.sqrt(K / P_N2_bar)
                        p_Al2O = p_SiO
                        return {'SiO': math.log10(p_SiO), 'Al2O': math.log10(p_Al2O), 'N2': math.log10(P_N2_bar)}
                    else:
                        return {'SiO': -99.0, 'Al2O': -99.0, 'N2': math.log10(P_N2_bar)}
                else:
                    return {}

        def parse_artifact_csv(path):
            """Load CSV as list of dicts, converting numeric fields."""
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                rows = []
                for r in reader:
                    row = dict(r)
                    for k in ['reaction_id', 'temperature_K', 'N2_pressure_MPa']:
                        if k in row:
                            try:
                                row[k] = float(row[k])
                            except:
                                row[k] = None
                    for k in ['partial_pressure_bar', 'log10_partial_pressure']:
                        if k in row:
                            try:
                                row[k] = float(row[k])
                            except:
                                row[k] = None
                    rows.append(row)
            return rows

        return {'species': species, 'gibbs': gibbs, 'compute_K': compute_K, 'expected_log10': expected_log10, 'parse_artifact_csv': parse_artifact_csv, 'R': R}


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    rows = ctx['parse_artifact_csv'](os.path.join('/app/outputs', step['output_file']))
    if not rows:
        return 0.0

    P_N2_fixed = 1.01325  # bar (101.3 kPa)
    tol = float(step.get('tolerance_log10_abs', 0.15))

    # Point-value tolerance check
    total_rows = len(rows)
    if total_rows == 0:
        point_score = 0.0
    else:
        correct = 0
        for row in rows:
            try:
                rid = int(row['reaction_id'])
                T = float(row['temperature_K'])
                formula = str(row['formula']).strip()
                log10_agent = float(row['log10_partial_pressure'])
            except (ValueError, KeyError):
                continue
            expected_map = ctx['expected_log10'](rid, T, P_N2_bar = P_N2_fixed if rid >=3 else None)
            exp_log = expected_map.get(formula, None)
            if exp_log is None:
                correct += 0
            else:
                if abs(log10_agent - exp_log) <= tol:
                    correct += 1
        point_score = correct / total_rows

    # Structural check: at T=2000 K, p_SiO reaction5 > reaction3 > reaction4
    T_target = 2000
    struct_score = 0.0
    try:
        def get_log_SiO(rid):
            for r in rows:
                if (int(r.get('reaction_id', 0)) == rid
                    and abs(float(r.get('temperature_K', 0)) - T_target) < 1.0
                    and r.get('formula', '').strip() == 'SiO'):
                    return float(r['log10_partial_pressure'])
            return None
        p3 = get_log_SiO(3)
        p4 = get_log_SiO(4)
        p5 = get_log_SiO(5)
        if p5 is not None and p3 is not None and p4 is not None:
            if p5 > p3 > p4:
                struct_score = 1.0
            else:
                struct_score = 0.0
        else:
            struct_score = 0.0
    except Exception:
        struct_score = 0.0

    # Combine: 0.6 point, 0.4 struct
    return 0.6 * point_score + 0.4 * struct_score


# === block: score_1 (check id='step02') ===
def score_1(artifact, step, ctx):
    rows = ctx['parse_artifact_csv'](os.path.join('/app/outputs', step['output_file']))
    if not rows:
        return 0.0

    tol = float(step.get('tolerance_log10_abs', 0.15))

    # Point-value tolerance check
    total_rows = len(rows)
    if total_rows == 0:
        point_score = 0.0
    else:
        correct = 0
        for row in rows:
            try:
                rid = int(row['reaction_id'])
                PN2_MPa = float(row['N2_pressure_MPa'])
                formula = str(row['formula']).strip()
                log10_agent = float(row['log10_partial_pressure'])
            except (ValueError, KeyError):
                continue
            P_N2_bar = PN2_MPa * 10.0
            T = 2000.0  # fixed temp
            expected_map = ctx['expected_log10'](rid, T, P_N2_bar = P_N2_bar)
            exp_log = expected_map.get(formula, None)
            if exp_log is None:
                continue
            if abs(log10_agent - exp_log) <= tol:
                correct += 1
        point_score = correct / total_rows

    # Structural check: for reactions (3)-(6), ratio of p_SiO at 0.1 MPa to 10 MPa.
    struct_score = 0.0
    try:
        required_rids = [3,4,5,6]
        # Find rows with N2_pressure_MPa within 0.05 of target
        def get_p_SiO(rid, target_MPa):
            for r in rows:
                if int(r.get('reaction_id',0)) == rid and abs(float(r.get('N2_pressure_MPa',0)) - target_MPa) < 0.05 and r.get('formula','').strip() == 'SiO':
                    return float(r['log10_partial_pressure'])
            return None
        checks = []
        for rid in required_rids:
            log_low = get_p_SiO(rid, 0.1)
            log_high = get_p_SiO(rid, 10.0)
            if log_low is not None and log_high is not None:
                # ratio = 10**(log_low - log_high)
                ratio = 10**(log_low - log_high)
                if rid in [5,6]:
                    # expect ratio > 10
                    if ratio > 10:
                        checks.append(1)
                    else:
                        checks.append(0)
                else:  # 3 and 4
                    # expect ratio < 10 (modest change)
                    if ratio < 10:
                        checks.append(1)
                    else:
                        checks.append(0)
            else:
                checks.append(0)
        # structural passes if all 4 checks are 1
        struct_score = 1.0 if all(checks) else 0.0
    except Exception:
        struct_score = 0.0

    return 0.6 * point_score + 0.4 * struct_score


_SCORERS = {
    'step01': score_0,
    'step02': score_1,
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
