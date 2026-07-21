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
    return {}


# === block: score_0 (check id='eg_accuracy') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = 0.15  # relaxed tolerance for open-source DFT toolchain differences
        values = {row['system']: float(row['Eg']) for row in artifact}
        ok = sum(1 for sys, ref in gold.items() if sys in values and abs(values[sys] - ref) <= tol)
        return ok / len(gold) if gold else 0.0


# === block: score_1 (check id='eg_trends') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = {row['system']: float(row['Eg']) for row in artifact}
        if 'pristine' not in data:
            return 0.0
        pristine = data['pristine']
        doped_systems = ['Cu-I','Cu-E','Cu-O','Ag-I','Ag-E','Ag-O','Au-I','Au-E','Au-O']
        g1 = all(data.get(s, -1e9) > pristine for s in doped_systems)
        sites = ['I','E','O']
        g2 = all(data.get(f'Cu-{s}', -1e9) < data.get(f'Ag-{s}', 0) < data.get(f'Au-{s}', 0) for s in sites)
        cu_min = (data.get('Cu-O', 1e9) < data.get('Cu-I', 0) and data.get('Cu-O', 1e9) < data.get('Cu-E', 0))
        ag_min = (data.get('Ag-I', 1e9) < data.get('Ag-E', 0) and data.get('Ag-I', 1e9) < data.get('Ag-O', 0))
        au_min = (data.get('Au-I', 1e9) < data.get('Au-E', 0) and data.get('Au-I', 1e9) < data.get('Au-O', 0))
        g3 = cu_min and ag_min and au_min
        return (g1 + g2 + g3) / 3.0


# === block: score_2 (check id='eads_accuracy') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step['gold']
        tol = step['tolerance']
        values = {row['system']: float(row['Eads']) for row in artifact}
        ok = sum(1 for sys, ref in gold.items() if sys in values and abs(values[sys] - ref) <= tol)
        return ok / len(gold) if gold else 0.0


# === block: score_3 (check id='eads_trends') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = {row['system']: float(row['Eads']) for row in artifact}
        cu = all(k in data for k in ['Cu-I','Cu-E','Cu-O']) and (data['Cu-I'] > data['Cu-E'] > data['Cu-O'])
        ag = all(k in data for k in ['Ag-I','Ag-E','Ag-O']) and (data['Ag-I'] > data['Ag-E'] > data['Ag-O'])
        au = all(k in data for k in ['Au-I','Au-E','Au-O']) and (data['Au-I'] > data['Au-E'] > data['Au-O'])
        return (cu + ag + au) / 3.0


_SCORERS = {
    'eg_accuracy': score_0,
    'eg_trends': score_1,
    'eads_accuracy': score_2,
    'eads_trends': score_3,
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
