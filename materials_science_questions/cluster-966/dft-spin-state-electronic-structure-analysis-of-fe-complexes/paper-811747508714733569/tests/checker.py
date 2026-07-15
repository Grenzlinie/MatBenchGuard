import os
import json
import csv

# === author imports / helpers ===
import math, json, csv, os


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
    spec = json.loads(open('/tests/grading_spec.json').read())
    hidden = spec.get('hidden_data', {})
    exp_list = hidden.get('experimental_ratios', [])
    return {'experimental_ratios': exp_list}


# === block: score_0 (check id='fit_parameters') ===
def score_0(artifact, step, ctx):
    params = artifact
    m1 = params.get('M1', {})
    m2 = params.get('M2', {})
    dist = params.get('site_distribution', {})
    fe_per = params.get('Fe_per_site', {})

    def score_val(val, target, tol, partial_tol_factor=2.0):
        if val is None: return 0.0
        err = abs(val - target)
        if err <= tol: return 1.0
        partial_limit = tol * partial_tol_factor
        if err <= partial_limit: return 0.5
        return 0.0

    eta1 = m1.get('eta')
    eta2 = m2.get('eta')
    sign1 = (m1.get('sign_q') or '').lower()
    sign2 = (m2.get('sign_q') or '').lower()
    f1 = dist.get('M1_fraction')
    f2 = dist.get('M2_fraction')
    m1fe = fe_per.get('M1')
    m2fe = fe_per.get('M2')
    tfe = params.get('total_Fe_per_formula')

    s_eta1 = score_val(eta1, 0.2, 0.05)
    s_eta2 = score_val(eta2, 0.4, 0.1, 2.0)
    s_sign = 1.0 if sign1 == 'positive' and sign2 == 'positive' else 0.0

    occ_parts = []
    if f1 is not None and f2 is not None:
        occ_parts.append(1.0 if abs(f1 - 0.081) <= 0.02 else 0.0)
        occ_parts.append(1.0 if abs(f2 - 0.081) <= 0.02 else 0.0)
    if m1fe is not None and m2fe is not None:
        occ_parts.append(1.0 if abs(m1fe - 0.081) <= 0.02 else 0.0)
        occ_parts.append(1.0 if abs(m2fe - 0.081) <= 0.02 else 0.0)
    if tfe is not None:
        occ_parts.append(1.0 if abs(tfe - 0.163) <= 0.01 else 0.0)
    s_occ = sum(occ_parts) / len(occ_parts) if occ_parts else 0.0

    # direction cosines sanity: check that each Vzz, Vxx, Vyy are unit vectors and orthogonal
    s_orient = 1.0
    for site in [m1, m2]:
        for comp in ['Vzz_direction','Vxx_direction','Vyy_direction']:
            d = site.get(comp, {})
            if isinstance(d, dict):
                dc = d.get('direction_cosines', {})
                cx, cy, cz = dc.get('cx'), dc.get('cy'), dc.get('cz')
                if None not in (cx,cy,cz):
                    norm = math.sqrt(cx*cx + cy*cy + cz*cz)
                    if abs(norm - 1.0) > 0.01:
                        s_orient = min(s_orient, 0.8)
        # check orthogonality
        for pair in [('Vzz_direction','Vxx_direction'), ('Vzz_direction','Vyy_direction'), ('Vxx_direction','Vyy_direction')]:
            d1 = site.get(pair[0], {}).get('direction_cosines', {})
            d2 = site.get(pair[1], {}).get('direction_cosines', {})
            a = d1.get('cx'); b = d1.get('cy'); c = d1.get('cz')
            x = d2.get('cx'); y = d2.get('cy'); z = d2.get('cz')
            if None not in (a,b,c,x,y,z):
                dot = a*x + b*y + c*z
                if abs(dot) > 0.02:
                    s_orient = min(s_orient, 0.8)

    score = 0.3*s_eta1 + 0.3*s_eta2 + 0.1*s_sign + 0.25*s_occ + 0.05*s_orient
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='compute_ratios') ===
def score_1(artifact, step, ctx):
    rows = artifact
    exp_list = ctx.get('experimental_ratios', [])
    if not rows or not exp_list: return 0.0
    # Build lookup from (theta, phi) to AH_AL_combined
    agent_map = {}
    for r in rows:
        try:
            th = float(r['theta'])
            ph = float(r['phi'])
            val = float(r['AH_AL_combined'])
            agent_map[(th, ph)] = val
        except:
            continue
    sq_sum = 0.0
    N = 0
    for e in exp_list:
        key = (e['theta'], e['phi'])
        if key in agent_map:
            diff = agent_map[key] - e['AH_AL']
            sq_sum += diff * diff
            N += 1
    if N == 0: return 0.0
    rms = math.sqrt(sq_sum / N)
    thresh = 0.05
    if rms <= thresh:
        return 1.0
    else:
        decay = (rms - thresh) / 0.05
        return max(0.0, 1.0 - decay)


_SCORERS = {
    'fit_parameters': score_0,
    'compute_ratios': score_1,
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
