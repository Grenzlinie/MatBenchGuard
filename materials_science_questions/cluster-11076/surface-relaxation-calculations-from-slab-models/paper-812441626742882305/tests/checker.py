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
    return {'gold': spec.get('gold_data', {}) }


# === block: score_0 (check id='step_04_gsf_energy') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts from csv reader
    if not rows:
        return 0.0
    gold = ctx.get('gold', {})
    # group by metal
    from collections import defaultdict
    by_metal = defaultdict(list)
    for r in rows:
        try:
            metal = r['metal'].strip()
            q = float(r['q'])
            relaxed = float(r['relaxed_energy'])
            by_metal[metal].append((q, relaxed))
        except:
            continue

    scores = []
    for metal in gold:
        if metal not in by_metal:
            scores.append(0.0)
            continue
        points = by_metal[metal]
        # find row closest to q=1.0
        best_q1 = min(points, key=lambda x: abs(x[0]-1.0))
        sfe_computed = best_q1[1]
        max_unstable = max(p[1] for p in points)
        gold_sfe = gold[metal].get('SFE')
        gold_unsfe = gold[metal].get('unstable_SFE')
        tol_sfe = gold[metal].get('SFE_tol_abs', 50)
        tol_unsfe = gold[metal].get('unstable_SFE_tol_abs', 60)
        ok_sfe = 0.0
        if gold_sfe is not None and abs(sfe_computed - gold_sfe) <= tol_sfe:
            ok_sfe = 0.5
        ok_unsfe = 0.0
        if gold_unsfe is not None and abs(max_unstable - gold_unsfe) <= tol_unsfe:
            ok_unsfe = 0.5
        scores.append(ok_sfe + ok_unsfe)
    if not scores:
        return 0.0
    return sum(scores) / (len(scores) * 1.0)


# === block: score_1 (check id='step_05_interlayer_spacings') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # define required trends: metal -> list of (layer_number, sign_required, condition)
    # sign_required: -1 for contraction (relaxed < unrelaxed), +1 for expansion, 0 for sign_change
    # condition: all_q (all rows for that layer must satisfy), sign_change (at least one negative and one positive)
    required = {
        'Pd': [
            (1, -1, 'all_q'),
            (2, 0, 'sign_change'),
            (3, 1, 'all_q')
        ],
        'Pt': [
            (1, -1, 'all_q'),
            (2, -1, 'all_q'),
            (3, 1, 'all_q')
        ]
    }
    # index rows by (metal, layer_number)
    by_key = {}
    for r in rows:
        metal = r.get('metal', '').strip()
        layer = int(r.get('layer_number', -1))
        if metal and layer >= 1:
            by_key.setdefault((metal, layer), []).append((float(r['relaxed_spacing']), float(r['unrelaxed_spacing'])))

    scores_per_metal = []
    for metal, checks in required.items():
        if metal not in by_key:
            scores_per_metal.append(0.0)
            continue
        ok = 0
        total = len(checks)
        for layer, sign, cond in checks:
            key = (metal, layer)
            if key not in by_key:
                continue
            deltas = [relaxed - unrel for relaxed, unrel in by_key[key]]
            if not deltas:
                continue
            if cond == 'all_q':
                if sign == -1 and all(d < -0.001 for d in deltas):
                    ok += 1
                elif sign == 1 and all(d > 0.001 for d in deltas):
                    ok += 1
            elif cond == 'sign_change':
                has_neg = any(d < -0.001 for d in deltas)
                has_pos = any(d > 0.001 for d in deltas)
                if has_neg and has_pos:
                    ok += 1
        scores_per_metal.append(ok / total if total > 0 else 0.0)
    if not scores_per_metal:
        return 0.0
    return sum(scores_per_metal) / len(scores_per_metal)


# === block: score_2 (check id='step_06_summary') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold = ctx.get('gold', {})
    num_checks = 0
    passed = 0
    for r in rows:
        metal = r.get('metal', '').strip()
        if metal not in gold:
            continue
        g = gold[metal]
        sfe = float(r.get('SFE', None))
        unsfe = float(r.get('unstable_SFE', None))
        coa = float(r.get('c_over_a', None))
        # SFE
        if g.get('SFE') is not None:
            num_checks += 1
            if abs(sfe - g['SFE']) <= g.get('SFE_tol_abs', 50):
                passed += 1
        # unstable SFE
        if g.get('unstable_SFE') is not None:
            num_checks += 1
            if abs(unsfe - g['unstable_SFE']) <= g.get('unstable_SFE_tol_abs', 60):
                passed += 1
        # c/a
        if g.get('c_over_a') is not None:
            num_checks += 1
            if abs(coa - g['c_over_a']) <= g.get('c_over_a_tol', 0.02):
                passed += 1
    if num_checks == 0:
        return 1.0
    return passed / num_checks


_SCORERS = {
    'step_04_gsf_energy': score_0,
    'step_05_interlayer_spacings': score_1,
    'step_06_summary': score_2,
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
