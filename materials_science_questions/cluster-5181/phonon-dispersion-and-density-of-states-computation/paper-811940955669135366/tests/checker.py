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
    steps = spec.get('steps', [])
    if steps:
        step = steps[0]
        gold_rows = step.get('gold_rows', [])
        tol_mod = float(step.get('rel_tol_moduli', 0.005))
        tol_deb = float(step.get('rel_tol_debye', 0.002))
    else:
        gold_rows = []
        tol_mod = 0.005
        tol_deb = 0.002
    return dict(gold_rows=gold_rows, tol_moduli=tol_mod, tol_debye=tol_deb)


# === block: score_0 (check id='check_table_values') ===
def score_0(artifact, step, ctx):
    def norm(s):
        s = str(s).lower().strip()
        s = s.replace(chr(0x00a0), ' ')   # non-breaking space
        s = s.replace(chr(0x2011), '-').replace(chr(0x2013), '-').replace(chr(0x2014), '-')
        return s

    agent_rows = artifact  # list of dicts from CSV
    if not isinstance(agent_rows, list) or not agent_rows:
        return 0.0

    lookup = {}
    for row in agent_rows:
        g = norm(row.get('Glass', ''))
        s = norm(row.get('Screening', ''))
        key = (g, s)
        if key not in lookup:
            lookup[key] = row

    gold_rows = ctx.get('gold_rows', [])
    tol_mod = ctx.get('tol_moduli', 0.005)
    tol_deb = ctx.get('tol_debye', 0.002)

    cells_correct = 0
    cells_total = len(gold_rows) * 4  # E, B, G, Theta_D per row

    for gr in gold_rows:
        key = (norm(gr['Glass']), norm(gr['Screening']))
        agent_row = lookup.get(key)
        if agent_row is None:
            continue
        for field, gold_val, tol in [('E', gr['E'], tol_mod),
                                      ('B', gr['B'], tol_mod),
                                      ('G', gr['G'], tol_mod),
                                      ('Theta_D', gr['Theta_D'], tol_deb)]:
            try:
                aval = float(agent_row.get(field, None))
            except (TypeError, ValueError):
                continue
            if abs(gold_val) < 1e-12:
                if abs(aval) < 1e-12:
                    cells_correct += 1
                continue
            rel_diff = abs(aval - gold_val) / abs(gold_val)
            if rel_diff <= tol:
                cells_correct += 1

    score = cells_correct / max(cells_total, 1)
    return float(score)


_SCORERS = {
    'check_table_values': score_0,
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
