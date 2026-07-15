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
    gold_enthalpies = {}
    gold_rrkm = []
    for step in spec.get('steps', []):
        if step['id'] == 'step_01':
            gold_enthalpies = {row['species']: row['Delta_H_kJ_mol'] for row in step['gold']}
        if step['id'] == 'step_02':
            gold_rrkm = [(row['product'], row['pressure_Torr'], row['log_k_over_k_inf']) for row in step['gold']]
    return {'gold_enthalpies': gold_enthalpies, 'gold_rrkm': gold_rrkm}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold_enthalpies = ctx['gold_enthalpies']
    tol = step.get('tolerance', 5.0)
    required_species = set(gold_enthalpies.keys())
    found_species = set()
    correct = 0
    for row in artifact:
        species = row.get('species', '').strip()
        if species in required_species:
            found_species.add(species)
            try:
                delta = float(row['Delta_H_kJ_mol'])
                if abs(delta - gold_enthalpies[species]) <= tol:
                    correct += 1
            except:
                pass
    missing = required_species - found_species
    # missing species count as incorrect (could also treat as zero correct, but consistent with total count)
    total = len(required_species)
    score = correct / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_rrkm = ctx['gold_rrkm']  # list of (product, press, log_value)
    log_tol = step.get('log_tolerance', 0.3)
    perc_tol = step.get('percent_tolerance', 1.0)
    # build lookup
    gold_lookup = {}
    for prod, press, logv in gold_rrkm:
        gold_lookup[(prod, press)] = logv
    total = len(gold_rrkm)
    log_correct = 0
    perc_correct = 0
    for row in artifact:
        prod = row.get('product', '').strip()
        try:
            press = int(row['pressure_Torr'])
        except:
            continue
        key = (prod, press)
        if key not in gold_lookup:
            continue
        log_gold = gold_lookup[key]
        try:
            log_agent = float(row['log_k_over_k_inf'])
        except:
            continue
        if abs(log_agent - log_gold) <= log_tol:
            log_correct += 1
        # percent_stabilization consistency check
        try:
            percent_agent = float(row['percent_stabilization'])
        except:
            continue
        expected_percent = 100.0 * (1.0 - 10.0 ** log_agent)
        if abs(percent_agent - expected_percent) <= max(perc_tol, abs(expected_percent)*0.02):
            perc_correct += 1
    log_score = log_correct / total if total > 0 else 0.0
    perc_score = perc_correct / total if total > 0 else 0.0
    return 0.9 * log_score + 0.1 * perc_score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
