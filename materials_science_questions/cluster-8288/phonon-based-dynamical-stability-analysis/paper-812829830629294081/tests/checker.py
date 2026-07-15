import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    steps = spec['steps']
    for s in steps:
        sid = s.get('id')
        if sid == 'step_01':
            ctx['step_01_gold'] = s['gold']
            ctx['step_01_tol'] = s.get('tolerance', 0.02)
        elif sid == 'step_02':
            ctx['step_02_gold'] = s['gold']
        elif sid == 'step_03':
            ctx['step_03_gold'] = s['gold']
            ctx['step_03_tol_ev'] = s.get('gap_tolerance_eV', 0.05)
        elif sid == 'step_04':
            ctx['step_04'] = True
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = ctx['step_01_gold']
    tol = ctx['step_01_tol']
    max_tol = 0.10

    def rel_err(val, ref):
        return abs(val - ref) / ref if ref != 0 else float('inf')

    total_score = 0.0
    count = 0
    for entry in artifact:
        for g in gold:
            if g['compound'] == entry['compound']:
                a_err = rel_err(entry['a'], g['a'])
                b_err = rel_err(entry['b'], g['b'])
                if a_err <= tol:
                    score_a = 1.0
                else:
                    score_a = max(0.0, 1.0 - (a_err - tol) / (max_tol - tol))
                if b_err <= tol:
                    score_b = 1.0
                else:
                    score_b = max(0.0, 1.0 - (b_err - tol) / (max_tol - tol))
                total_score += (score_a + score_b)
                count += 2
                break
    return total_score / count if count > 0 else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_stable = ctx['step_02_gold']
    correct = 0
    for entry in artifact:
        for g in gold_stable:
            if g['compound'] == entry['compound']:
                stable_ok = (entry['stable'] == g['stable'])
                freq_sign_ok = (
                    (entry['stable'] and entry['min_phonon_frequency'] >= -1e-6)
                    or (not entry['stable'] and entry['min_phonon_frequency'] < 0)
                )
                if stable_ok and freq_sign_ok:
                    correct += 1
                break
    return correct / len(gold_stable) if gold_stable else 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    gold_bands = ctx['step_03_gold']
    tol_ev = ctx['step_03_tol_ev']
    earned = 0
    total = 0
    for entry in artifact:
        for g in gold_bands:
            if g['compound'] == entry['compound']:
                if abs(entry['direct_gap'] - g['direct_gap']) <= tol_ev:
                    earned += 1
                if abs(entry['indirect_gap'] - g['indirect_gap']) <= tol_ev:
                    earned += 1
                if entry['gap_type'] == g['gap_type']:
                    earned += 1
                total += 3
                break
    return earned / total if total > 0 else 0.0


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    strains = [d['strain_b'] for d in artifact]
    idx_max = strains.index(max(strains))
    idx_min = strains.index(min(strains))
    item_zero = artifact[idx_max]
    item_neg = artifact[idx_min]
    score1 = 1.0 if item_zero['indirect_gap'] < item_zero['direct_gap'] else 0.0
    score2 = 1.0 if item_neg['direct_gap'] < item_neg['indirect_gap'] else 0.0
    return (score1 + score2) / 2.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
