import os
import json
import csv

# === author imports / helpers ===
import csv
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
    gold_rows = None
    step01 = None
    for s in spec.get('steps', spec.get('checks', [])):
        if s.get('id') == 'step_01':
            step01 = s
            gold_rows = { (r['polarization'], r['model_type']): float(r['de0']) for r in s['gold_rows'] }
            break
    step02 = None
    for s in spec.get('steps', spec.get('checks', [])):
        if s.get('id') == 'step_02':
            step02 = s
            break
    if step01 is None or step02 is None or gold_rows is None:
        raise RuntimeError('missing grading spec step')
    return {'gold_rows': gold_rows, 'tol_abs': float(step01.get('tolerance_abs_pct', 0.05)), 'tol_rel': float(step01.get('tolerance_rel', 0.05)), 'de0_thresh': float(step02['thresholds']['de0_max_diff']), 'phase_thresh': float(step02['thresholds']['phase_max_diff'])}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_rows']
    tol_abs = ctx['tol_abs']
    tol_rel = ctx['tol_rel']
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    for row in rows:
        pol = str(row.get('polarization', '')).strip()
        mtype = str(row.get('model_type', '')).strip()
        # RCWA rows in the gold correspond to optimized design, not the
        # parameters required for this step; skip them to avoid unfair penalty.
        if mtype == 'RCWA':
            continue
        key = (pol, mtype)
        if key not in gold:
            continue
        gval = gold[key]
        try:
            aval = float(row['de0'])
        except (ValueError, KeyError):
            continue
        tol = max(tol_abs, tol_rel * abs(gval))
        scores.append(1.0 if abs(aval - gval) <= tol else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    valid_count = 0
    max_te = 0.0
    max_tm = 0.0
    max_total = 0.0
    max_phase = 0.0
    for row in artifact:
        try:
            te_hlm = float(row['de0_TE_HLM'])
            te_rcwa = float(row['de0_TE_RCWA'])
            tm_hlm = float(row['de0_TM_HLM'])
            tm_rcwa = float(row['de0_TM_RCWA'])
            total_hlm = float(row['de0_total_HLM'])
            total_rcwa = float(row['de0_total_RCWA'])
            phase_hlm = float(row['phase_HLM'])
            phase_rcwa = float(row['phase_RCWA'])
        except (ValueError, KeyError):
            continue
        max_te = max(max_te, abs(te_hlm - te_rcwa))
        max_tm = max(max_tm, abs(tm_hlm - tm_rcwa))
        max_total = max(max_total, abs(total_hlm - total_rcwa))
        max_phase = max(max_phase, abs(phase_hlm - phase_rcwa))
        valid_count += 1
    if valid_count < 7:
        return 0.0
    de0_thresh = ctx['de0_thresh']
    phase_thresh = ctx['phase_thresh']
    scores = [
        1.0 if max_te <= de0_thresh else 0.0,
        1.0 if max_tm <= de0_thresh else 0.0,
        1.0 if max_total <= de0_thresh else 0.0,
        1.0 if max_phase <= phase_thresh else 0.0
    ]
    return sum(scores) / len(scores)


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
