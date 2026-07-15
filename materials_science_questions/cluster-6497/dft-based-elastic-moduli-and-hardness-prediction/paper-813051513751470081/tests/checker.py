import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    OUTDIR = '/app/outputs'
    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    ctx = {}
    try: ctx['elastic_data'] = load_csv(os.path.join(OUTDIR, 'elastic_constants.csv'))
    except: ctx['elastic_data'] = []
    try: ctx['mechanical_data'] = load_csv(os.path.join(OUTDIR, 'mechanical_properties.csv'))
    except: ctx['mechanical_data'] = []
    try: ctx['acoustic_data'] = load_csv(os.path.join(OUTDIR, 'acoustic_properties.csv'))
    except: ctx['acoustic_data'] = []
    exp = spec.get('experimental_refs', {})
    ctx['exp_elastic'] = exp.get('elastic', {})
    ctx['exp_B'] = exp.get('B')
    return ctx


# === block: score_0 (check id='elastic_shape') ===
def score_0(artifact, step, ctx):
    data = ctx.get('elastic_data', [])
    if not data:
        return 0.0
    required_cols = ['functional','C11','C22','C33','C12','C13','C23','C44','C55','C66','C15','C25','C35','C46']
    for row in data:
        if row.get('functional') in ('LDA','PBE','PL/2'):
            for col in required_cols[1:]:
                try: float(row[col])
                except: return 0.0
    funcs = {r['functional'] for r in data}
    if {'LDA','PBE','PL/2'}.issubset(funcs):
        return 1.0
    return 0.0


# === block: score_1 (check id='mechanical_consistency') ===
def score_1(artifact, step, ctx):
    import math
    def vrh_mechanical(C):
        c = {}
        for key in ['C11','C22','C33','C12','C13','C23','C44','C55','C66','C15','C25','C35','C46']:
            c[key] = float(C.get(key, 0))
        Cmat = [
            [c['C11'], c['C12'], c['C13'], 0, c['C15'], 0],
            [c['C12'], c['C22'], c['C23'], 0, c['C25'], 0],
            [c['C13'], c['C23'], c['C33'], 0, c['C35'], 0],
            [0, 0, 0, 2*c['C44'], 0, 2*c['C46']],
            [c['C15'], c['C25'], c['C35'], 0, 2*c['C55'], 0],
            [0, 0, 0, 2*c['C46'], 0, 2*c['C66']]
        ]
        def invert_6(mat):
            n=6
            a = [row[:] for row in mat]
            inv = [[float(i==j) for j in range(n)] for i in range(n)]
            for i in range(n):
                pivot = a[i][i]
                if pivot == 0:
                    return None
                for j in range(n):
                    a[i][j] /= pivot
                    inv[i][j] /= pivot
                for k in range(n):
                    if k != i:
                        factor = a[k][i]
                        for j in range(n):
                            a[k][j] -= factor * a[i][j]
                            inv[k][j] -= factor * inv[i][j]
            return inv
        Sinv = invert_6(Cmat)
        if Sinv is None:
            return None
        S = [[Sinv[i][j]/2 if (i>=3 and j>=3) else Sinv[i][j] for j in range(6)] for i in range(6)]
        BV = (c['C11']+c['C22']+c['C33'] + 2*(c['C12']+c['C13']+c['C23']))/9
        GV = (c['C11']+c['C22']+c['C33'] + 3*(c['C44']+c['C55']+c['C66']) - (c['C12']+c['C13']+c['C23']))/15
        S11, S22, S33 = S[0][0], S[1][1], S[2][2]
        S12, S13, S23 = S[0][1], S[0][2], S[1][2]
        S44, S55, S66 = S[3][3]/4, S[4][4]/4, S[5][5]/4
        denom = (S11+S22+S33) + 2*(S12+S13+S23)
        if denom==0: return None
        BR = 1/denom
        GR = 15/( 4*(S11+S22+S33) - 4*(S12+S13+S23) + 3*(S44+S55+S66) )
        B = (BV+BR)/2
        G = (GV+GR)/2
        E = 9*B*G/(3*B+G)
        mu = (3*B-2*G)/(2*(3*B+G))
        H = 0.92 * math.pow(G/B, 1.137) * math.pow(G, 0.708)
        return {'B':B, 'G':G, 'E':E, 'mu':mu, 'H':H}
    elastic_data = ctx.get('elastic_data', [])
    mech_data = artifact
    if not mech_data:
        return 0.0
    funcs = ['LDA','PBE','PL/2']
    tol = step.get('tolerance_rel', 1e-5)
    score = 0.0
    count = 0
    for func in funcs:
        erow = next((r for r in elastic_data if r.get('functional')==func), None)
        mrow = next((r for r in mech_data if r.get('functional')==func), None)
        if erow is None or mrow is None:
            continue
        ref = vrh_mechanical(erow)
        if ref is None:
            continue
        for key in ['B','G','E','mu','H']:
            try:
                val = float(mrow.get(key))
                rval = ref[key]
                if rval != 0:
                    err = abs(val - rval) / (abs(rval)+1e-12)
                else:
                    err = abs(val - rval)
                if err <= tol:
                    score += 1
            except:
                pass
            count += 1
    if count == 0:
        return 0.0
    return min(1.0, score/count)


# === block: score_2 (check id='acoustic_consistency') ===
def score_2(artifact, step, ctx):
    import math
    mech_data = ctx.get('mechanical_data', [])
    acoustic_data = artifact
    if not mech_data or not acoustic_data:
        return 0.0
    funcs = ['LDA','PBE','PL/2']
    tol = step.get('tolerance_rel', 1e-5)
    M = 0.12817
    NA = 6.02214076e23
    hbar = 1.054571817e-34
    kB = 1.380649e-23
    score = 0.0
    count = 0
    for func in funcs:
        mrow = next((r for r in mech_data if r.get('functional')==func), None)
        arow = next((r for r in acoustic_data if r.get('functional')==func), None)
        if mrow is None or arow is None:
            continue
        try:
            B = float(mrow['B']) * 1e9
            G = float(mrow['G']) * 1e9
            v_s = float(arow['v_s'])
            v_p = float(arow['v_p'])
            v_avg_reported = float(arow['v_avg'])
            TD_reported = float(arow['Theta_D'])
            gamma_a_reported = float(arow['gamma_a'])
        except:
            continue
        rho = G / (v_s**2)
        v_p_pred = math.sqrt((B + 4*G/3) / rho) if rho>0 else 0
        v_avg_pred = ((1/3)*(2/(v_s**3) + 1/(v_p**3)))**(-1/3) if v_s>0 and v_p>0 else 0
        n = 18
        TD_pred = (hbar/kB) * (6*math.pi**2 * n * (NA * rho / M))**(1/3) * v_avg_pred
        gamma_pred = 9*(v_p_pred**2 - 4*v_s**2/3) / (2*(v_p_pred**2 + 2*v_s**2))
        for (pred, rep) in [(v_p_pred, v_p), (v_avg_pred, v_avg_reported), (TD_pred, TD_reported), (gamma_pred, gamma_a_reported)]:
            if pred != 0:
                err = abs(pred - rep) / abs(pred)
            else:
                err = abs(pred - rep)
            if err <= tol:
                score += 1
            count += 1
    if count == 0:
        return 0.0
    return min(1.0, score/count)


# === block: score_3 (check id='elastic_trend') ===
def score_3(artifact, step, ctx):
    elastic_data = ctx.get('elastic_data', [])
    exp = ctx.get('exp_elastic', {})
    if not exp or not elastic_data:
        return 0.0
    funcs = ['LDA','PBE','PL/2']
    eps = step.get('eps', 0.01)
    min_better = step.get('min_better_count', 10)
    keys = ['C11','C22','C33','C12','C13','C23','C44','C55','C66','C15','C25','C35','C46']
    rows = {f: None for f in funcs}
    for r in elastic_data:
        if r.get('functional') in rows:
            rows[r['functional']] = r
    if any(v is None for v in rows.values()):
        return 0.0
    better_count = 0
    for key in keys:
        try:
            e = exp.get(key)
            if e is None: continue
            vL = float(rows['LDA'][key])
            vP = float(rows['PBE'][key])
            vPL = float(rows['PL/2'][key])
            errL = abs(vL - e)
            errP = abs(vP - e)
            errPL = abs(vPL - e)
            if errPL < errL - eps and errPL < errP - eps:
                better_count += 1
        except:
            pass
    if better_count >= min_better:
        return 1.0
    else:
        return better_count / len(keys)


# === block: score_4 (check id='bulk_trend') ===
def score_4(artifact, step, ctx):
    from checker_blocks import vrh_mechanical  # not available; we'll inline a helper
    def _vrh_mechanical(C):
        c = {}
        for key in ['C11','C22','C33','C12','C13','C23','C44','C55','C66','C15','C25','C35','C46']:
            c[key] = float(C.get(key, 0))
        Cmat = [
            [c['C11'], c['C12'], c['C13'], 0, c['C15'], 0],
            [c['C12'], c['C22'], c['C23'], 0, c['C25'], 0],
            [c['C13'], c['C23'], c['C33'], 0, c['C35'], 0],
            [0,0,0,2*c['C44'],0,2*c['C46']],
            [c['C15'],c['C25'],c['C35'],0,2*c['C55'],0],
            [0,0,0,2*c['C46'],0,2*c['C66']]
        ]
        def inv(mat):
            n=6
            a=[row[:] for row in mat]
            inv=[[float(i==j) for j in range(n)] for i in range(n)]
            for i in range(n):
                piv=a[i][i]
                if piv==0: return None
                for j in range(n): a[i][j]/=piv; inv[i][j]/=piv
                for k in range(n):
                    if k!=i:
                        f=a[k][i]
                        for j in range(n): a[k][j]-=f*a[i][j]; inv[k][j]-=f*inv[i][j]
            return inv
        SI=inv(Cmat)
        if SI is None: return None
        S=[[SI[i][j]/2 if (i>=3 and j>=3) else SI[i][j] for j in range(6)] for i in range(6)]
        BV=(c['C11']+c['C22']+c['C33']+2*(c['C12']+c['C13']+c['C23']))/9
        GV=(c['C11']+c['C22']+c['C33']+3*(c['C44']+c['C55']+c['C66'])-(c['C12']+c['C13']+c['C23']))/15
        S11,S22,S33=S[0][0],S[1][1],S[2][2]
        S12,S13,S23=S[0][1],S[0][2],S[1][2]
        S44,S55,S66=S[3][3]/4,S[4][4]/4,S[5][5]/4
        BR=1/((S11+S22+S33)+2*(S12+S13+S23))
        GR=15/(4*(S11+S22+S33)-4*(S12+S13+S23)+3*(S44+S55+S66))
        B=(BV+BR)/2
        return B
    elastic_data = ctx.get('elastic_data', [])
    mech_data = artifact
    exp_B = ctx.get('exp_B')
    if exp_B is None or not elastic_data:
        return 0.0
    rows={}
    for r in elastic_data:
        if r.get('functional') in ('LDA','PBE','PL/2'):
            rows[r['functional']]=r
    if not {'LDA','PBE','PL/2'}.issubset(rows.keys()):
        return 0.0
    BL=_vrh_mechanical(rows['LDA']); BP=_vrh_mechanical(rows['PBE']); BPL=_vrh_mechanical(rows['PL/2'])
    if BL is None or BP is None or BPL is None: return 0.0
    eps=step.get('eps',0.01)
    errL=abs(BL-exp_B); errP=abs(BP-exp_B); errPL=abs(BPL-exp_B)
    if errPL < errL - eps and errPL < errP - eps:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'elastic_shape': score_0,
    'mechanical_consistency': score_1,
    'acoustic_consistency': score_2,
    'elastic_trend': score_3,
    'bulk_trend': score_4,
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
