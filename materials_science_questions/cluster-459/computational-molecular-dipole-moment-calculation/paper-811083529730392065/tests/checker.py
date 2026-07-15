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
    gold = spec.get('hidden_gold', {})
    tolerances = spec.get('tolerances', {})
    return {'gold': gold, 'tolerances': tolerances}


# === block: score_0 (check id='shg_results_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0

    gold = ctx['gold']
    tols = ctx['tolerances']

    def within(val, target, abs_tol):
        try:
            return abs(float(val) - float(target)) <= abs_tol
        except (TypeError, ValueError):
            return False

    # 1. table1_CT_gaps (weight 0.25)
    w1 = 0.25
    score1 = 0.0
    ct_data = artifact.get('table1_CT_gaps')
    gold_ct = gold.get('table1_CT_gaps', [])
    if isinstance(ct_data, list) and len(ct_data) == len(gold_ct):
        hits = 0
        for i, (entry, g) in enumerate(zip(ct_data, gold_ct)):
            if not isinstance(entry, dict) or not isinstance(g, dict):
                continue
            if entry.get('N') == g['N'] and abs(entry.get('epsilon', 0) - g['epsilon']) < 1e-6:
                if within(entry.get('CT_gap'), g['CT_gap'], tols.get('CT_gap_abs', 0.01)):
                    hits += 1
        score1 = hits / len(gold_ct) if gold_ct else 0.0
    else:
        score1 = 0.0

    # 2. table2_position_dependence (weight 0.25)
    w2 = 0.25
    score2 = 0.0
    pos_data = artifact.get('table2_position_dependence')
    gold_pos = gold.get('table2_position_dependence', [])
    if isinstance(pos_data, list) and len(pos_data) == len(gold_pos):
        hits = 0
        total = 0
        for i, (entry, g) in enumerate(zip(pos_data, gold_pos)):
            if not isinstance(entry, dict) or not isinstance(g, dict):
                continue
            if entry.get('position') != g['position']:
                continue
            if within(entry.get('beta_x_exact'), g['beta_x_exact'], tols.get('beta_abs', 0.5)):
                hits += 1
            total += 1
            if within(entry.get('mu_gr'), g['mu_gr'], tols.get('dipole_abs', 0.05)):
                hits += 1
            total += 1
            if within(entry.get('mu_ex'), g['mu_ex'], tols.get('dipole_abs', 0.05)):
                hits += 1
            total += 1
        score2 = hits / total if total else 0.0
    else:
        score2 = 0.0

    # 3. table4_beta_exact (weight 0.25)
    w3 = 0.25
    score3 = 0.0
    beta_tab = artifact.get('table4_beta_exact')
    gold_tab = gold.get('table4_beta_exact', {})
    if isinstance(beta_tab, dict):
        hits = 0
        total = 0
        for N in ('4','6','8','10'):
            gN = gold_tab.get(N)
            aN = beta_tab.get(N)
            if not isinstance(gN, dict) or not isinstance(aN, dict):
                continue
            for eps_key in ('eps0.6','eps2.0'):
                geps = gN.get(eps_key)
                aeps = aN.get(eps_key)
                if not isinstance(geps, dict) or not isinstance(aeps, dict):
                    continue
                # beta_exact
                tgt = geps.get('beta_exact')
                val = aeps.get('beta_exact')
                abs_tol = tols.get('beta_abs_large', 1.0) if (tgt and tgt >= 500) else tols.get('beta_abs', 0.5)
                if within(val, tgt, abs_tol):
                    hits += 1
                total += 1
                # beta_CT
                tgt_ct = geps.get('beta_CT')
                val_ct = aeps.get('beta_CT')
                abs_tol_ct = tols.get('beta_abs_large', 1.0) if (tgt_ct and tgt_ct >= 500) else tols.get('beta_abs', 0.5)
                if within(val_ct, tgt_ct, abs_tol_ct):
                    hits += 1
                total += 1
        score3 = hits / total if total else 0.0
    else:
        score3 = 0.0

    # 4. twist_dependence (weight 0.15) evaluated only by structural checks
    w4 = 0.15
    twist_data = artifact.get('twist_dependence')
    twist_map = {}
    if isinstance(twist_data, list):
        for entry in twist_data:
            if isinstance(entry, dict) and 'theta' in entry:
                twist_map[entry['theta']] = entry.get('beta_x_exact')

    score4 = 0.0
    if twist_map:
        b90 = twist_map.get(90)
        b75 = twist_map.get(75)
        b105 = twist_map.get(105)
        hits = 0
        total = 3
        # beta_x at 90° must be a deep minimum; expect < 30 a.u.
        if b90 is not None and b90 < 30:
            hits += 1
        # beta_x near 75° must be a strong peak; expect > 500 a.u.
        if b75 is not None and b75 > 500:
            hits += 1
        if b105 is not None and b105 > 500:
            hits += 1
        score4 = hits / total

    # 5. alpha_exponent (weight 0.10)
    w5 = 0.10
    alpha = artifact.get('alpha_exponent')
    gold_alpha = gold.get('alpha_exponent', {})
    if isinstance(alpha, dict) and isinstance(gold_alpha, dict):
        hits = 0
        total = 0
        for key in ('0.6','2.0'):
            tgt = gold_alpha.get(key)
            val = alpha.get(key)
            if tgt is not None and val is not None:
                if within(val, tgt, tols.get('alpha_abs', 0.1)):
                    hits += 1
                total += 1
        score5 = hits / total if total else 0.0
    else:
        score5 = 0.0

    final = w1*score1 + w2*score2 + w3*score3 + w4*score4 + w5*score5
    return max(0.0, min(1.0, final))


_SCORERS = {
    'shg_results_check': score_0,
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
