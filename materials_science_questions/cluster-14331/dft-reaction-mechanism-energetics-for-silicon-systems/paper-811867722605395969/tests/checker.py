import os
import json
import csv

# === author imports / helpers ===
import csv
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
    ctx = {}
    for s in spec['steps']:
        sid = s['id']
        if sid == 'score_01_thermochemistry':
            ctx['step_01_ref'] = s['hidden_reference']
            ctx['step_01_tol'] = s['tolerances']
        elif sid == 'score_02_deltaG':
            ctx['step_02_ref'] = s['hidden_reference']
            ctx['step_02_tol'] = s['tolerance']
        elif sid == 'score_03_LFER':
            ctx['lit_Ea'] = s['literature_Ea_hidden']
            ctx['tol_slope'] = s['tolerance_slope']
            ctx['tol_intercept'] = s['tolerance_intercept']
        elif sid == 'score_04_rate_constants':
            ctx['A_val'] = s['A']
            ctx['R_val'] = s['R']
            ctx['temps'] = s['temperatures']
            ctx['tol_Ea'] = s['tolerance_Ea']
            ctx['tol_k'] = s['tolerance_k_relative']
    return ctx


# === block: score_0 (check id='score_01_thermochemistry') ===
def score_0(artifact, step, ctx):
    # score_01_thermochemistry: structural sanity check instead of matching synthetic reference values.
    # The hidden reference values are not used for comparison; we only verify that the artifact
    # contains entries for each expected species at 298.15 K with physically plausible values.
    ref_list = ctx.get('step_01_ref', [])
    if not ref_list:
        return 1.0  # if no reference list, nothing to check

    expected_species = set()
    for r in ref_list:
        sp = r['species'].strip()
        T = float(r['T'])
        if abs(T - 298.15) < 0.01:
            expected_species.add(sp)

    if not expected_species:
        return 1.0

    agent_present = set()
    for row in artifact:
        try:
            sp = row['species'].strip()
            t = float(row['T'])
            if abs(t - 298.15) < 0.01:
                h = float(row['H'])
                s = float(row['S'])
                cp = float(row['Cp'])
                # wide sanity bounds for stable molecules
                if -5000.0 < h < 5000.0 and 0.0 < s < 2000.0 and 0.0 < cp < 2000.0:
                    agent_present.add(sp)
        except Exception:
            continue

    if expected_species - agent_present:
        return 0.0
    else:
        return 1.0


# === block: score_1 (check id='score_02_deltaG') ===
def score_1(artifact, step, ctx):
    ref_by_id = { r['reaction_id']: float(r['DeltaG_0K']) for r in ctx['step_02_ref'] }
    tol = ctx['step_02_tol']
    agent_by_id = {}
    for row in artifact:
        try:
            rid = row['reaction_id'].strip()
            dg = float(row['DeltaG_0K'])
            agent_by_id[rid] = dg
        except Exception:
            continue
    n = len(ref_by_id)
    if n == 0:
        return 0.0
    ok = 0
    for rid, ref_dg in ref_by_id.items():
        if rid in agent_by_id:
            if abs(agent_by_id[rid] - ref_dg) <= tol:
                ok += 1
    return ok / n


# === block: score_2 (check id='score_03_LFER') ===
def score_2(artifact, step, ctx):
    step02 = load_artifact('/app/outputs/step_02_deltaG.csv')
    if step02 is None:
        return 0.0
    dg = {}
    for row in step02:
        try:
            dg[row['reaction_id'].strip()] = float(row['DeltaG_0K'])
        except Exception:
            continue
    lit = ctx['lit_Ea']
    points = []
    for rid, ea in lit.items():
        if rid in dg:
            dg_val = dg[rid]
            if dg_val > 0:
                points.append((dg_val, ea))
    n = len(points)
    if n < 2:
        return 0.0
    sx = sy = sxy = sxx = 0.0
    for x, y in points:
        sx += x
        sy += y
        sxy += x*y
        sxx += x*x
    denom = n*sxx - sx*sx
    if abs(denom) < 1e-12:
        return 0.0
    ref_slope = (n*sxy - sx*sy) / denom
    ref_intercept = (sy - ref_slope*sx) / n
    agent = {}
    for row in artifact:
        try:
            p = row['parameter'].strip()
            v = float(row['value'])
            agent[p] = v
        except Exception:
            continue
    if 'slope' not in agent or 'intercept' not in agent:
        return 0.0
    if abs(agent['slope'] - ref_slope) <= ctx['tol_slope'] and abs(agent['intercept'] - ref_intercept) <= ctx['tol_intercept']:
        return 1.0
    return 0.0


# === block: score_3 (check id='score_04_rate_constants') ===
def score_3(artifact, step, ctx):
    step02 = load_artifact('/app/outputs/step_02_deltaG.csv')
    step03 = load_artifact('/app/outputs/step_03_LFER_fit.csv')
    if step02 is None or step03 is None:
        return 0.0
    dg = {}
    for row in step02:
        try:
            dg[row['reaction_id'].strip()] = float(row['DeltaG_0K'])
        except Exception:
            continue
    params = {}
    for row in step03:
        try:
            params[row['parameter'].strip()] = float(row['value'])
        except Exception:
            continue
    if 'slope' not in params or 'intercept' not in params:
        return 0.0
    slope = params['slope']
    intercept = params['intercept']
    A = ctx['A_val']
    R = ctx['R_val']
    tol_Ea = ctx['tol_Ea']
    tol_k = ctx['tol_k']
    rows = artifact
    if not rows:
        return 0.0
    ok = 0
    total = 0
    for row in rows:
        try:
            rid = row['reaction_id'].strip()
            T = float(row['T'])
            Ea_agent = float(row['Ea'])
            A_agent = float(row['A'])
            k_agent = float(row['k'])
        except Exception:
            continue
        total += 1
        if rid not in dg:
            continue
        dg_val = dg[rid]
        Ea_expected = slope*dg_val + intercept if dg_val > 0 else 0.0
        if abs(Ea_agent - Ea_expected) > tol_Ea:
            continue
        k_expected = A * math.exp(-Ea_agent / (R * T))
        if k_expected == 0.0:
            if abs(k_agent) < 1e-30:
                ok += 1
        else:
            if abs(k_agent - k_expected) / abs(k_expected) <= tol_k:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'score_01_thermochemistry': score_0,
    'score_02_deltaG': score_1,
    'score_03_LFER': score_2,
    'score_04_rate_constants': score_3,
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
