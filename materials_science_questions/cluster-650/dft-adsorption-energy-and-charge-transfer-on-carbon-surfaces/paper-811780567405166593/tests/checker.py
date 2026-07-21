import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    return {'output_dir': '/app/outputs'}


# === block: score_0 (check id='step_values') ===
def score_0(artifact, step, ctx):
    gold_table = step.get('gold_table', [])
    tolerances = step.get('tolerances', {})
    total_cells = len(gold_table)*4
    if total_cells == 0:
        return 0.0
    gold_lookup = {}
    for row in gold_table:
        key = (row['atom'].strip().upper(), row['site'].strip().upper())
        gold_lookup[key] = row
    matched_cells = 0
    for row in artifact:
        atom = row.get('atom','').strip().upper()
        site = row.get('site','').strip().upper()
        key = (atom, site)
        if key not in gold_lookup:
            continue
        gold = gold_lookup[key]
        for col, tol in tolerances.items():
            if col not in row or col not in gold:
                continue
            try:
                agent_val = float(row[col])
                gold_val = float(gold[col])
            except (ValueError, TypeError):
                continue
            if abs(agent_val - gold_val) <= tol:
                matched_cells += 1
    return min(matched_cells / total_cells, 1.0)


# === block: score_1 (check id='step_ordering') ===
def score_1(artifact, step, ctx):
    rules = step.get('ordering_rules', [])
    if not rules:
        return 1.0
    data = {}
    for row in artifact:
        atom = row.get('atom','').strip().upper()
        site = row.get('site','').strip().upper()
        try:
            e_ad = float(row.get('E_ad', 0))
        except:
            continue
        if atom not in data:
            data[atom] = {}
        data[atom][site] = e_ad
    correct = 0
    total = len(rules)
    for rule in rules:
        atom = rule['atom'].strip().upper()
        if atom not in data:
            continue
        vals = data[atom]
        if rule.get('strict'):
            order = rule['expected_order']
            mags = []
            for s in order:
                if s in vals:
                    mags.append(-vals[s])
                else:
                    break
            if len(mags) == len(order):
                if all(mags[i] > mags[i+1] for i in range(len(mags)-1)):
                    correct += 1
        else:
            required = rule.get('required_sites', ['T','B','H'])
            if not all(s in vals for s in required):
                continue
            t = -vals.get('T', 0)
            b = -vals.get('B', 0)
            h = -vals.get('H', 0)
            margin = rule.get('margin', 0.01)
            if t > h + margin and b > h + margin:
                correct += 1
    return correct / total if total > 0 else 1.0


_SCORERS = {
    'step_values': score_0,
    'step_ordering': score_1,
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
