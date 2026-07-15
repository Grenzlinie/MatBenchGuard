import os
import json
import csv

# === author imports / helpers ===
import math, json


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
    gold = spec.get('gold', {})
    return {'gold': gold}


# === block: score_0 (check id='structure') ===
def score_0(artifact, step, ctx):
    import json, math
    data = artifact
    if not isinstance(data, dict) or not all(k in data for k in ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']):
        return 0.0
    gold = ctx['gold']
    compounds = ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']
    tol_a = step.get('tolerances',{}).get('a_rel',0.01)
    tol_c = step.get('tolerances',{}).get('c_rel',0.02)
    tol_V = step.get('tolerances',{}).get('V_rel',0.02)

    def score_param(val, gold_val, tol):
        if gold_val == 0: return 1.0 if abs(val) < 1e-9 else 0.0
        rel_err = abs(val - gold_val) / abs(gold_val)
        if rel_err <= tol: return 1.0
        # linear decay to 0 at 3*tol
        over = rel_err - tol
        return max(0.0, 1.0 - over/(2*tol))

    compound_scores = []
    for comp in compounds:
        g = gold.get(comp)
        if not g: return 0.0
        d = data.get(comp)
        if not d: return 0.0
        a_score = score_param(d.get('a'), g['a'], tol_a)
        c_score = score_param(d.get('c'), g['c'], tol_c)
        # recompute V_per_fu consistency check: V_calc = a^2 * c / 8
        a_val = d.get('a'); c_val = d.get('c')
        if a_val is not None and c_val is not None:
            V_calc = a_val**2 * c_val / 8.0
            V_score = score_param(d.get('V_per_fu'), g['V'], tol_V)
            # also check internal consistency between V_calc and reported V
            # but just use reported V score; internal consistency can be extra small bonus
        else:
            V_score = 0.0
        comp_score = (a_score + c_score + V_score) / 3.0
        compound_scores.append(comp_score)

    numeric_score = sum(compound_scores) / len(compound_scores)

    # monotonic volume increase
    vols = [gold[c]['V'] for c in compounds]
    # but we should check the agent's volumes, not gold
    agent_vols = []
    for c in compounds:
        d = data.get(c)
        if d and 'V_per_fu' in d:
            agent_vols.append(d['V_per_fu'])
        else:
            agent_vols.append(0)
    monotonic_pairs = 0
    for i in range(1, len(agent_vols)):
        if agent_vols[i] > agent_vols[i-1]:
            monotonic_pairs += 1
    mono_score = monotonic_pairs / (len(compounds)-1) if len(compounds)>1 else 1.0

    # abrupt c jump: c(Na) to c(K) > 20% increase
    c_Na = data.get('NaBSi2',{}).get('c')
    c_K = data.get('KBSi2',{}).get('c')
    c_jump_score = 0.0
    if c_Na is not None and c_K is not None and c_Na > 0:
        if c_K > c_Na * 1.20:
            c_jump_score = 1.0

    return 0.6 * numeric_score + 0.2 * mono_score + 0.2 * c_jump_score


# === block: score_1 (check id='electronic') ===
def score_1(artifact, step, ctx):
    import json, math
    data = artifact
    if not isinstance(data, dict) or not all(k in data for k in ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']):
        return 0.0
    gold = ctx['gold']
    compounds = ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']
    tol_gap = step.get('tolerances',{}).get('gap_abs',0.2)

    def dos_pass(comp, d, is_metal):
        s = str(d.get('dos_fermi_character','')).lower()
        if is_metal:
            # must mention si and p (simplistic check)
            return ('si' in s and 'p' in s) and (s != 'n/a' and s != 'n/a (semiconductor)')
        else:
            return ('semiconductor' in s or s.startswith('n/a'))

    compound_scores = []
    for comp in compounds:
        g = gold.get(comp)
        d = data.get(comp)
        if not g or not d:
            compound_scores.append(0.0)
            continue
        # classification
        classif = 1.0 if d.get('is_metal') == g['is_metal'] else 0.0
        # gap
        if g['is_metal']:
            gap_score = 1.0 if d.get('band_gap_eV') is None else 0.0
        else:
            gap_val = d.get('band_gap_eV')
            if gap_val is None:
                gap_score = 0.0
            else:
                diff = abs(gap_val - g['band_gap'])
                if diff <= tol_gap:
                    gap_score = 1.0
                else:
                    gap_score = max(0.0, 1.0 - (diff - tol_gap)/(tol_gap))
        # dos character
        dos = 1.0 if dos_pass(comp, d, g['is_metal']) else 0.0
        comp_score = 0.6*classif + 0.3*gap_score + 0.1*dos
        compound_scores.append(comp_score)

    return sum(compound_scores)/len(compound_scores)


# === block: score_2 (check id='phonon') ===
def score_2(artifact, step, ctx):
    text = artifact.strip() if isinstance(artifact, str) else ''
    expected = step.get('expected','')
    return 1.0 if text == expected else 0.0


# === block: score_3 (check id='elastic') ===
def score_3(artifact, step, ctx):
    import json, math
    data = artifact
    if not isinstance(data, dict) or not all(k in data for k in ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']):
        return 0.0
    gold = ctx['gold']
    compounds = ['BSi2','LiBSi2','NaBSi2','KBSi2','RbBSi2']
    tol_rel = step.get('tolerances',{}).get('rel',0.10)
    fields = ['C11','C33','C44','C66','C12','C13','B','G','B/G']

    def score_val(val, gold_val):
        if gold_val == 0:
            return 1.0 if abs(val) < 1e-6 else 0.0
        rel_err = abs(val - gold_val) / abs(gold_val)
        if rel_err <= tol_rel: return 1.0
        over = rel_err - tol_rel
        return max(0.0, 1.0 - over/(3*tol_rel))

    def stability_check(d):
        try:
            c11 = d['C11']; c33 = d['C33']; c44 = d['C44']; c66 = d['C66'];
            c12 = d['C12']; c13 = d['C13'];
            if not (c11>0 and c33>0 and c44>0 and c66>0): return False
            if not (c11 - c12 > 0): return False
            if not (c11 + c33 - 2*c13 > 0): return False
            if not (2*(c11+c12) + c33 + 4*c13 > 0): return False
            return True
        except:
            return False

    def ductile_ok(comp, d):
        bg = d.get('B/G')
        if bg is None: return False
        if comp == 'BSi2':
            return bg > 1.75
        else:
            return bg < 1.75

    compound_scores = []
    for comp in compounds:
        g = gold.get(comp)
        d = data.get(comp)
        if not g or not d:
            compound_scores.append(0.0)
            continue
        # numeric accuracy
        numeric = []
        for f in fields:
            numeric.append(score_val(d.get(f), g['elastic'][f]))
        num_score = sum(numeric) / len(numeric)
        stab = 1.0 if stability_check(d) else 0.0
        duct = 1.0 if ductile_ok(comp, d) else 0.0
        comp_score = 0.7 * num_score + 0.2 * stab + 0.1 * duct
        compound_scores.append(comp_score)

    return sum(compound_scores) / len(compound_scores)


_SCORERS = {
    'structure': score_0,
    'electronic': score_1,
    'phonon': score_2,
    'elastic': score_3,
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
