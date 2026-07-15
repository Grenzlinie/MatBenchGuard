import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import json
from collections import defaultdict


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
    gold = spec.get('gold_data', {})
    return {
        'gold': gold,
        'tolerance_ads': 0.25,
        'tolerance_barrier': 0.25,
        'tolerance_eff': 0.25
    }


# === block: score_0 (check id='adsorption_accuracy') ===
def score_0(artifact, step, ctx):
    gold_rows = { (r['surface'], r['species']): float(r['adsorption_energy_eV']) for r in ctx['gold']['adsorption'] }
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    tol = ctx['tolerance_ads']
    for row in rows:
        key = (row['surface'], row['species'])
        if key not in gold_rows:
            continue
        val = float(row['adsorption_energy_eV'])
        ref = gold_rows[key]
        dev = abs(val - ref)
        if dev <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (dev - tol) / (tol * 2))
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='adsorption_trend') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ads = defaultdict(dict)
    for row in rows:
        ads[row['species']][row['surface']] = float(row['adsorption_energy_eV'])
    all_species = ['CO','H','CH3OH','H2O','CH2O']
    correct = 0
    for sp in all_species:
        if 'Pd(211)' in ads[sp] and 'Pd(211)-B' in ads[sp]:
            if ads[sp]['Pd(211)-B'] > ads[sp]['Pd(211)']:
                correct += 1
    return correct / len(all_species)


# === block: score_2 (check id='barrier_accuracy') ===
def score_2(artifact, step, ctx):
    gold_rows = { (r['surface'], r['reaction_step']): (float(r['activation_energy_eV']), float(r['reaction_energy_eV'])) for r in ctx['gold']['reaction'] }
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    tol = ctx['tolerance_barrier']
    def score_dev(dev):
        if dev <= tol:
            return 1.0
        return max(0.0, 1.0 - (dev - tol) / (tol * 2))
    for row in rows:
        key = (row['surface'], row['reaction_step'])
        if key not in gold_rows:
            continue
        act = float(row['activation_energy_eV'])
        reac = float(row['reaction_energy_eV'])
        g_act, g_reac = gold_rows[key]
        s_act = score_dev(abs(act - g_act))
        s_reac = score_dev(abs(reac - g_reac))
        scores.append((s_act + s_reac) / 2.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='effective_accuracy') ===
def score_3(artifact, step, ctx):
    gold_rows = { (r['surface'], r['product']): float(r['effective_barrier_eV']) for r in ctx['gold']['effective'] }
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    tol = ctx['tolerance_eff']
    for row in rows:
        key = (row['surface'], row['product'])
        if key not in gold_rows:
            continue
        val = float(row['effective_barrier_eV'])
        ref = gold_rows[key]
        dev = abs(val - ref)
        if dev <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (dev - tol) / (tol * 2))
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='selectivity_trend') ===
def score_4(artifact, step, ctx):
    rows = artifact
    vals = {}
    for row in rows:
        key = (row['surface'], row['product'])
        vals[key] = float(row['effective_barrier_eV'])
    if ('Pd(211)','methane') not in vals or ('Pd(211)','methanol') not in vals:
        return 0.0
    if ('Pd(211)-B','methane') not in vals or ('Pd(211)-B','methanol') not in vals:
        return 0.0
    cond1 = vals[('Pd(211)','methane')] < vals[('Pd(211)','methanol')]
    cond2 = vals[('Pd(211)-B','methanol')] < vals[('Pd(211)-B','methane')]
    return float(cond1 and cond2)


_SCORERS = {
    'adsorption_accuracy': score_0,
    'adsorption_trend': score_1,
    'barrier_accuracy': score_2,
    'effective_accuracy': score_3,
    'selectivity_trend': score_4,
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
