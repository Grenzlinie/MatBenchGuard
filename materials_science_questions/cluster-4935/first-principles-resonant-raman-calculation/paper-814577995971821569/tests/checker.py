import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='t2_norm') ===
def score_0(artifact, step, ctx):
        if artifact is None: return 0.0
        ref_cfg = step['reference']
        col = ref_cfg['column']
        ref_dict = {row['polarization']: row['value'] for row in ref_cfg['values']}
        tol = ref_cfg['tolerance_relative']
        max_margin = ref_cfg.get('tolerance_max_relative_margin', tol*4)
        scores = []
        for row in artifact:
            pol = row.get('polarization', '')
            if pol not in ref_dict:
                continue
            try:
                val = float(row[col])
            except:
                scores.append(0.0)
                continue
            exp = ref_dict[pol]
            if exp == 0:
                scores.append(1.0 if abs(val) < 1e-8 else 0.0)
                continue
            rel_err = abs(val - exp) / abs(exp)
            if rel_err <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (rel_err - tol) / max_margin)
            scores.append(s)
        return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='t2_abs') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None: return 0.0
        ref_cfg = step['reference']
        col = ref_cfg['column']
        ref_dict = {row['polarization']: row['value'] for row in ref_cfg['values']}
        tol = ref_cfg['tolerance_relative']
        max_margin = ref_cfg.get('tolerance_max_relative_margin', tol*4)
        scores = []
        for row in artifact:
            pol = row.get('polarization', '')
            if pol not in ref_dict:
                continue
            try:
                val = float(row[col])
            except:
                scores.append(0.0)
                continue
            exp = ref_dict[pol]
            if exp == 0:
                scores.append(1.0 if abs(val) < 1e-8 else 0.0)
                continue
            rel_err = abs(val - exp) / abs(exp)
            if rel_err <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (rel_err - tol) / max_margin)
            scores.append(s)
        return sum(scores)/len(scores) if scores else 0.0


# === block: score_2 (check id='t3_mass') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None: return 0.0
        ref_cfg = step['reference']
        cols = ref_cfg['columns']
        ref_lookup = {}
        for row in ref_cfg['values']:
            key = (row['polarization'], row['sheet'])
            ref_lookup[key] = (row['bare'], row['screened'])
        tol = ref_cfg['tolerance_absolute']
        max_margin = ref_cfg.get('tolerance_max_absolute_margin', tol*4)
        row_scores = []
        for row in artifact:
            pol = row.get('polarization', '')
            sheet = row.get('sheet', '')
            key = (pol, sheet)
            if key not in ref_lookup:
                continue
            try:
                bare_val = float(row['bare'])
                screened_val = float(row['screened'])
            except:
                row_scores.append(0.0)
                continue
            bare_exp, screened_exp = ref_lookup[key]
            bare_diff = abs(bare_val - bare_exp)
            screened_diff = abs(screened_val - screened_exp)
            bare_s = 1.0 if bare_diff <= tol else max(0.0, 1.0 - (bare_diff - tol) / max_margin)
            screened_s = 1.0 if screened_diff <= tol else max(0.0, 1.0 - (screened_diff - tol) / max_margin)
            row_scores.append((bare_s + screened_s) / 2.0)
        return sum(row_scores)/len(row_scores) if row_scores else 0.0


_SCORERS = {
    't2_norm': score_0,
    't2_abs': score_1,
    't3_mass': score_2,
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
