import os
import json
import csv


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
    step = spec['steps'][0]  # single step
    ctx = {
        'gold': step['hidden_gold'],
        'tols': step['tolerances'],
        'weights': step['sub_weights']
    }
    return ctx


# === block: score_0 (check id='energetics') ===
def score_0(artifact, step, ctx):
    data = artifact   # list of dicts
    gold = ctx['gold']
    tols = ctx['tols']
    w = ctx['weights']

    HARTREE_TO_KCAL = 627.509

    def find_H(system, substrate):
        for d in data:
            if d['system'] == system and d['substrate'] == substrate:
                return d['H']
        return None

    # parent quantities
    react_H = find_H('react_4_and_silane', 'parent')
    ts1_H = find_H('TS1', 'parent')
    hyd_silane_H = find_H('hydride_and_silane', 'parent')   # entry point for step2
    ts2_H = find_H('TS2', 'parent')
    caPh_H = find_H('CaPh', 'parent')
    silane_H = find_H('Ph(Me)SiH2', 'parent')   # H=0
    ts3_H = find_H('TS3', 'parent')
    prod_H = find_H('products', 'parent')

    # pCF3 quantities
    ts3_pCF3_H = find_H('TS3', 'pCF3')
    react_pCF3_H = find_H('react_4_and_silane', 'pCF3')

    if any(v is None for v in [react_H, ts1_H, hyd_silane_H, ts2_H, caPh_H, silane_H, ts3_H, prod_H, ts3_pCF3_H, react_pCF3_H]):
        return 0.0

    barrier1 = (ts1_H - react_H) * HARTREE_TO_KCAL
    barrier2 = (ts2_H - hyd_silane_H) * HARTREE_TO_KCAL
    # step3 reactant is CaPh + silane; entry 'CaPh_and_MeSiH3' is after step2, not the reactant
    # but we can compute: CaPh + silane = caPh_H + silane_H (silane_H is 0)
    step3_react = caPh_H + silane_H
    barrier3 = (ts3_H - step3_react) * HARTREE_TO_KCAL
    exothermicity = (prod_H - react_H) * HARTREE_TO_KCAL

    # substituent TS energy difference (absolute TS3 heights relative to reactants)
    ts3_parent_abs = (ts3_H - react_H) * HARTREE_TO_KCAL
    ts3_pCF3_abs = (ts3_pCF3_H - react_pCF3_H) * HARTREE_TO_KCAL
    subst_diff = ts3_parent_abs - ts3_pCF3_abs

    def score_val(val, gold, tol):
        if abs(val - gold) <= tol + 1e-9:
            return 1.0
        return 0.0

    scores = []
    scores.append(score_val(barrier1, gold['barrier1_kcalmol'], tols['barrier1_kcalmol']))
    scores.append(score_val(barrier2, gold['barrier2_kcalmol'], tols['barrier2_kcalmol']))
    scores.append(score_val(barrier3, gold['barrier3_kcalmol'], tols['barrier3_kcalmol']))
    scores.append(score_val(exothermicity, gold['exothermicity_kcalmol'], tols['exothermicity_kcalmol']))
    scores.append(score_val(subst_diff, gold['subst_diff_kcalmol'], tols['subst_diff_kcalmol']))

    total = 0.0
    for i, key in enumerate(['barrier1','barrier2','barrier3','exothermicity','subst_diff']):
        total += w[key] * scores[i]
    return total


_SCORERS = {
    'energetics': score_0,
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
