import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    spec = json.load(open('/tests/grading_spec.json'))
    steps = spec.get('steps', [])
    ctx = {}
    for s in steps:
        sid = s['id']
        if s['kind'] == 'table_reference':
            ctx[sid] = {'ref_rows': s['reference_rows'], 'tolerances': s['tolerances']}
        elif s['kind'] == 'json_fields':
            ctx[sid] = {'ref': s['reference'], 'tolerances': s['tolerances']}
        elif s['kind'] == 'structural_fractions':
            ctx[sid] = {'max_frac': s['max_fraction']}
    return ctx


# === block: score_0 (check id='partial_pressures_table') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    step_id = step.get('id')
    step_ctx = ctx.get(step_id, {}) if step_id else {}
    ref_rows = step_ctx.get('ref_rows', [])
    tolerances = step_ctx.get('tolerances', {})
    if len(artifact) != len(ref_rows):
        return 0.0
    total_row = 0.0
    for ag_row, ref_row in zip(artifact, ref_rows):
        col_score = 0.0
        n = 0
        for col, tol in tolerances.items():
            try:
                av = float(ag_row.get(col))
                rv = float(ref_row[col])
            except (ValueError, TypeError, KeyError):
                continue
            if rv == 0.0:
                sc = 1.0 if abs(av - rv) < 1e-12 else 0.0
            else:
                rel = abs(av - rv) / abs(rv)
                sc = 1.0 if rel <= tol else 0.0
            col_score += sc
            n += 1
        if n == 0:
            continue
        total_row += col_score / n
    nrows = len(ref_rows)
    return total_row / nrows if nrows else 0.0


# === block: score_1 (check id='thermodynamic_params') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    step_id = step.get('id')
    step_ctx = ctx.get(step_id, {}) if step_id else {}
    ref = step_ctx.get('ref', {})
    tolerances = step_ctx.get('tolerances', {})
    if not ref or not tolerances:
        return 0.0
    total = 0.0
    n = 0
    for key, tol in tolerances.items():
        if key not in ref or key not in artifact:
            continue
        try:
            av = float(artifact[key])
            rv = float(ref[key])
        except (ValueError, TypeError):
            continue
        if rv == 0.0:
            sc = 1.0 if abs(av - rv) < 1e-6 else 0.0
        else:
            rel = abs(av - rv) / abs(rv)
            sc = 1.0 if rel <= tol else 0.0
        total += sc
        n += 1
    return total / n if n else 0.0


# === block: score_2 (check id='structural_check') ===
def score_2(artifact, step, ctx):
    max_frac = ctx.get('max_frac', 0.02)
    if not isinstance(artifact, list):
        return 0.0
    for row in artifact:
        try:
            p_Yb = float(row.get('p_Yb_bar', 0))
            p_Se = float(row.get('p_Se_bar', 0))
            p_YbSe = float(row.get('p_YbSe_bar', 0))
            p_Se2 = float(row.get('p_Se2_bar', 0))
            total = p_Yb + p_Se + p_YbSe + p_Se2
            if total <= 0:
                return 0.0
            frac_YbSe = p_YbSe / total
            frac_Se2 = p_Se2 / total
            if frac_YbSe > max_frac or frac_Se2 > max_frac:
                return 0.0
        except (ValueError, TypeError, KeyError):
            return 0.0
    return 1.0


_SCORERS = {
    'partial_pressures_table': score_0,
    'thermodynamic_params': score_1,
    'structural_check': score_2,
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
