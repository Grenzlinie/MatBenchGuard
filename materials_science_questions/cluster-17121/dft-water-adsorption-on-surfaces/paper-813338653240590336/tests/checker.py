import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json


def load_artifact(path):
    if not os.path.exists(path):
        return None
    if path.endswith('.json'):
        with open(path) as f:
            return json.load(f)
    if path.endswith('.csv') or path.endswith('.tsv'):
        delim = '\t' if path.endswith('.tsv') else ','
        with open(path, newline='') as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def validate_artifact_against_contract(contract_output, artifact_path, spec):
    fmt = contract_output.get('format', '')
    schema = contract_output.get('schema', {}) or {}
    artifact = load_artifact(artifact_path)
    if artifact is None:
        return False
    if fmt == 'json':
        if not isinstance(artifact, dict):
            return False
        required = schema.get('required', {})
        fields = required.keys() if isinstance(required, dict) else (required or [])
        return all(field in artifact for field in fields)
    if fmt in ('csv', 'tsv'):
        if not isinstance(artifact, list) or not artifact:
            return not (schema.get('required_columns') or [])
        cols = set(artifact[0].keys())
        for col in schema.get('required_columns', []) or []:
            name = col.get('name') if isinstance(col, dict) else col
            if name and name not in cols:
                return False
        return True
    if fmt == 'txt':
        return isinstance(artifact, str) and len(artifact) > 0
    return True


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
    return {}


# === block: score_0 (check id='step3') ===
def score_0(artifact, step, ctx):
    csv_data = artifact
    if not csv_data:
        return 0.0

    def _norm(s):
        """Normalize a string for robust matching across character variants."""
        s = s.strip()
        # Greek mu / micro sign -> Latin mu
        s = s.replace('\u03bc', 'mu')
        s = s.replace('\u00b5', 'mu')
        # Subscript / superscript
        s = s.replace('\u2083', '3')   # subscript 3
        s = s.replace('\u1d63', 'r')   # subscript r
        # Ellipsis variants
        s = s.replace('\u2026', '...')
        s = s.replace('\u22ef', '...')
        # Dash variants
        s = s.replace('\u2013', '-')
        s = s.replace('\u2014', '-')
        # Comma -> underscore (e.g. μ₃,ᵣ -> mu3_r)
        s = s.replace(',', '_')
        # Plane parentheses: "lepidocrocite (010)" -> "lepidocrocite_010"
        s = s.replace(' (', '_')
        s = s.replace(')', '')
        return s.lower()

    targets = step.get('targets', [])
    if not targets:
        return 1.0

    lookup = {}
    for row in csv_data:
        try:
            plane = _norm(row.get('plane', ''))
            species = _norm(row.get('species_or_interaction', ''))
            prop = _norm(row.get('property', ''))
            val = float(row.get('value', ''))
            lookup[(plane, species, prop)] = val
        except (ValueError, TypeError):
            continue

    num_ok = 0
    for t in targets:
        key = (_norm(t['plane']), _norm(t['species_or_interaction']), _norm(t['property']))
        if key not in lookup:
            continue
        agent_val = lookup[key]
        if abs(agent_val - t['value']) <= t['tolerance']:
            num_ok += 1

    return num_ok / len(targets) if targets else 1.0


# === block: score_1 (check id='step4') ===
def score_1(artifact, step, ctx):
    text = artifact
    if not isinstance(text, str) or not text.strip():
        return 0.0
    lower = text.lower()
    required = step.get('required_strings', [])
    if not required:
        return 1.0
    for s in required:
        if s.lower() not in lower:
            return 0.0
    return 1.0


_SCORERS = {
    'step3': score_0,
    'step4': score_1,
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
