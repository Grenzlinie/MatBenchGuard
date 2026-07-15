import os
import json
import csv

# === author imports / helpers ===
import json, csv, math

try:
    import numpy as np_native
    np = np_native
except ImportError:
    class _np:
        @staticmethod
        def exp(x):
            return math.exp(x)
        @staticmethod
        def mean(seq):
            return sum(seq) / len(seq)
    np = _np()


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
    steps_cfg = spec.get('steps', [])
    gold_strokes = None
    gold_thickness_func = None
    for step in steps_cfg:
        if step['id'] == 'critical_punch_strokes':
            gold_strokes = step['gold']
            tol_abs = step.get('tolerance_abs', 0.5)
            tol_rel = step.get('tolerance_rel', 0.1)
        elif step['id'] == 'thickness_distribution':
            rf = step['reference_formula']
            t0 = rf['t0_mm']
            dip = rf['dip_mm']
            center = rf['center_mm']
            sigma = rf['sigma_mm']
            gold_thickness_func = lambda r: t0 - dip * np.exp(-((r - center)**2) / (2*sigma**2))
            mae_tol = step['tolerance_mae_mm']
            mae_decay = step.get('mae_decay_range_mm', 0.06)
    if gold_strokes is None or gold_thickness_func is None:
        raise ValueError('Missing gold reference in grading spec')
    return {
        'gold_strokes': gold_strokes,
        'tol_abs': tol_abs,
        'tol_rel': tol_rel,
        'gold_thickness_func': gold_thickness_func,
        'mae_tol': mae_tol,
        'mae_decay': mae_decay
    }


# === block: score_0 (check id='critical_punch_strokes') ===
def score_0(artifact, step, ctx):
    artifact_data = artifact
    if not isinstance(artifact_data, dict):
        return 0.0
    gold = ctx['gold_strokes']
    tol_abs = ctx['tol_abs']
    tol_rel = ctx['tol_rel']
    scores = []
    for cond in ['condition_i', 'condition_ii']:
        gold_val = gold.get(cond)
        if gold_val is None:
            continue
        agent_val = artifact_data.get(cond)
        if agent_val is None:
            scores.append(0.0)
            continue
        try:
            agent_val = float(agent_val)
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        error = abs(agent_val - gold_val)
        tol = max(tol_abs, tol_rel * gold_val)
        if error <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='thickness_distribution') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    gold_func = ctx['gold_thickness_func']
    mae_tol = ctx['mae_tol']
    mae_decay = ctx['mae_decay']
    abs_errors = []
    for row in rows:
        try:
            r = float(row.get('radial_position_mm', None))
            t_agent = float(row.get('thickness_mm', None))
        except (TypeError, ValueError):
            return 0.0
        if r is None or t_agent is None:
            return 0.0
        t_gold = gold_func(r)
        abs_errors.append(abs(t_agent - t_gold))
    if not abs_errors:
        return 0.0
    mae = float(np.mean(abs_errors))
    if mae <= mae_tol:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (mae - mae_tol) / mae_decay)
    return score


_SCORERS = {
    'critical_punch_strokes': score_0,
    'thickness_distribution': score_1,
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
