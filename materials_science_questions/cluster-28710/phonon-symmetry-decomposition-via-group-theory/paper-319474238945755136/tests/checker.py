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


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    def canonical_star(entry):
        stars = sorted([entry['star1'], entry['star2']])
        decomp = frozenset((d['star'], d['multiplicity']) for d in entry['decomposition'])
        return (tuple(stars), decomp)
    def canonical_ir(entry):
        irs = sorted([entry['ir1'], entry['ir2']])
        decomp = frozenset((d['ir'], d['multiplicity']) for d in entry['decomposition'])
        return (tuple(irs), decomp)
    expected_sel = step['expected_selection_rules']
    art = artifact
    if not isinstance(art, dict) or 'star_products' not in art or 'ir_products' not in art:
        return 0.0
    expected_star = set()
    for e in expected_sel['star_products']:
        expected_star.add(canonical_star(e))
    agent_star = set()
    for e in art.get('star_products', []):
        agent_star.add(canonical_star(e))
    matches_star = expected_star & agent_star
    expected_ir = set()
    for e in expected_sel['ir_products']:
        expected_ir.add(canonical_ir(e))
    agent_ir = set()
    for e in art.get('ir_products', []):
        agent_ir.add(canonical_ir(e))
    matches_ir = expected_ir & agent_ir
    total = len(expected_star) + len(expected_ir)
    if total == 0:
        return 1.0
    return (len(matches_star) + len(matches_ir)) / total


# === block: score_1 (check id='step02') ===
def score_1(artifact, step, ctx):
    import re
    def norm(s):
        return s.strip().replace(' ', '')
    expected_rows = step['expected_cgc_table']
    art = artifact
    if not isinstance(art, list):
        return 0.0
    exp_lookup = {}
    for row in expected_rows:
        key = (row['i'].strip(), row['j'].strip())
        exp = {k: norm(row[k]) for k in row if k not in ('i','j')}
        exp_lookup[key] = exp
    matches = 0
    for row in art:
        key = (row.get('i','').strip(), row.get('j','').strip())
        if key in exp_lookup:
            agent_entries = {k: norm(row.get(k, '')) for k in exp_lookup[key]}
            if agent_entries == exp_lookup[key]:
                matches += 1
    return matches / len(expected_rows) if expected_rows else 1.0


_SCORERS = {
    'step01': score_0,
    'step02': score_1,
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
