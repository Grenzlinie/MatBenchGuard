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
    def prepare(outputs_dir, spec):
        return {}


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = step['expected']
        tol = step['tolerance']
        keys = ['Ph-OH', 'Ph-COOH', 'Ph-CO-CH3', 'Ph-O-CH3']
        key_score = 0.0
        for k in keys:
            if k in artifact and abs(artifact[k] - expected[k]) <= tol:
                key_score += 1.0
        key_score /= len(keys)
        try:
            vals = [artifact[k] for k in keys]
            if vals[1] < vals[2] < 0 and vals[0] > 0 and vals[3] > 0:
                order_score = 1.0
            else:
                order_score = 0.0
        except:
            order_score = 0.0
        return key_score * 0.7 + order_score * 0.3


# === block: score_1 (check id='mulliken_analysis') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = step['expected']
        tol_pop = step['tolerance_population']
        tol_len = step['tolerance_length']
        total_pairs = 0
        matched_pairs = 0
        for unit, exp_pairs in expected.items():
            if unit not in artifact:
                continue
            act_pairs = artifact[unit]
            for exp in exp_pairs:
                total_pairs += 1
                for act in act_pairs:
                    if act.get('interaction') == exp['interaction']:
                        if abs(act['population'] - exp['population']) <= tol_pop and abs(act['length_Angstrom'] - exp['length_Angstrom']) <= tol_len:
                            matched_pairs += 1
                        break
        if total_pairs == 0:
            return 0.0
        return matched_pairs / total_pairs


# === block: score_2 (check id='charge_transfer') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = step['expected']
        tol = step['tolerance']
        total_atoms = 0
        matched_atoms = 0
        for unit, exp_atoms in expected.items():
            if unit not in artifact:
                continue
            act_atoms = artifact[unit]
            for exp in exp_atoms:
                total_atoms += 1
                for act in act_atoms:
                    if act.get('atom') == exp['atom']:
                        if abs(act['charge_before'] - exp['charge_before']) <= tol and abs(act['charge_after'] - exp['charge_after']) <= tol:
                            matched_atoms += 1
                        break
        if total_atoms == 0:
            return 0.0
        return matched_atoms / total_atoms


_SCORERS = {
    'adsorption_energies': score_0,
    'mulliken_analysis': score_1,
    'charge_transfer': score_2,
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
