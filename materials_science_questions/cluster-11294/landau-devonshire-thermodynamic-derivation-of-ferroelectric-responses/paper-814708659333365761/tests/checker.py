import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    ctx = {}
    ctx['step_configs'] = {}
    for step in steps:
        ctx['step_configs'][step['id']] = step
    return ctx


# === block: score_0 (check id='si') ===
def score_0(artifact, step, ctx):
    step_cfg = ctx['step_configs']['si']
    tg_pts = step_cfg['tg_points']
    targets = step_cfg['target']
    tols = step_cfg['tolerance']
    trends = step_cfg['trend_config']
    rows = artifact  # list of dicts from CSV
    if not rows:
        return 0.0
    cols = ['TG', 'P', 'epsilon33', 'd33', 'phi', 'phi_prime']
    # check columns
    for c in cols:
        if c not in rows[0]:
            return 0.0
    # map TG to row
    row_by_tg = {}
    for r in rows:
        try:
            tg = float(r['TG'])
            row_by_tg[tg] = r
        except:
            continue
    # value scoring
    value_scores = []
    for pt in tg_pts:
        best_key = min(row_by_tg.keys(), key=lambda k: abs(k - pt))
        r = row_by_tg[best_key]
        for q in ['P', 'epsilon33', 'd33', 'phi', 'phi_prime']:
            ref = targets[str(pt)][q]
            tol = tols[q]
            try:
                val = float(r[q])
            except:
                return 0.0
            rel_err = abs(val - ref) / (abs(ref) + 1e-12)
            if rel_err <= tol:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (rel_err - tol) / (tol * 5))
            value_scores.append(score_q)
    value_score = np.mean(value_scores) if value_scores else 0.0
    # trend scoring
    tg_all = sorted(row_by_tg.keys())
    if len(tg_all) < 2:
        return value_score
    trend_scores = []
    for q, direction in trends.items():
        vals = []
        for tg in tg_all:
            try:
                vals.append(float(row_by_tg[tg][q]))
            except:
                trend_scores.append(0.0)
                break
        else:
            diffs = np.diff(vals)
            if len(diffs) == 0:
                trend_scores.append(0.0)
                continue
            if direction == 'increasing':
                monotonic = np.all(diffs >= 0)
            else:  # decreasing
                monotonic = np.all(diffs <= 0)
            trend_scores.append(1.0 if monotonic else 0.0)
    trend_score = np.mean(trend_scores) if trend_scores else 0.0
    combined = 0.8 * value_score + 0.2 * trend_score
    return float(np.clip(combined, 0.0, 1.0))


# === block: score_1 (check id='c_sapphire') ===
def score_1(artifact, step, ctx):
    step_cfg = ctx['step_configs']['c_sapphire']
    tg_pts = step_cfg['tg_points']
    targets = step_cfg['target']
    tols = step_cfg['tolerance']
    trends = step_cfg['trend_config']
    rows = artifact
    if not rows:
        return 0.0
    cols = ['TG', 'P', 'epsilon33', 'd33', 'phi', 'phi_prime']
    for c in cols:
        if c not in rows[0]:
            return 0.0
    row_by_tg = {}
    for r in rows:
        try:
            tg = float(r['TG'])
            row_by_tg[tg] = r
        except:
            continue
    value_scores = []
    for pt in tg_pts:
        best_key = min(row_by_tg.keys(), key=lambda k: abs(k - pt))
        r = row_by_tg[best_key]
        for q in ['P', 'epsilon33', 'd33', 'phi', 'phi_prime']:
            ref = targets[str(pt)][q]
            tol = tols[q]
            try:
                val = float(r[q])
            except:
                return 0.0
            rel_err = abs(val - ref) / (abs(ref) + 1e-12)
            if rel_err <= tol:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (rel_err - tol) / (tol * 5))
            value_scores.append(score_q)
    value_score = np.mean(value_scores) if value_scores else 0.0
    tg_all = sorted(row_by_tg.keys())
    if len(tg_all) < 2:
        return value_score
    trend_scores = []
    for q, direction in trends.items():
        vals = []
        for tg in tg_all:
            try:
                vals.append(float(row_by_tg[tg][q]))
            except:
                trend_scores.append(0.0)
                break
        else:
            diffs = np.diff(vals)
            if len(diffs) == 0:
                trend_scores.append(0.0)
                continue
            if direction == 'increasing':
                monotonic = np.all(diffs >= 0)
            else:
                monotonic = np.all(diffs <= 0)
            trend_scores.append(1.0 if monotonic else 0.0)
    trend_score = np.mean(trend_scores) if trend_scores else 0.0
    combined = 0.8 * value_score + 0.2 * trend_score
    return float(np.clip(combined, 0.0, 1.0))


# === block: score_2 (check id='a_sapphire') ===
def score_2(artifact, step, ctx):
    step_cfg = ctx['step_configs']['a_sapphire']
    tg_pts = step_cfg['tg_points']
    targets = step_cfg['target']
    tols = step_cfg['tolerance']
    trends = step_cfg['trend_config']
    rows = artifact
    if not rows:
        return 0.0
    cols = ['TG', 'P', 'epsilon33', 'd33', 'phi', 'phi_prime']
    for c in cols:
        if c not in rows[0]:
            return 0.0
    row_by_tg = {}
    for r in rows:
        try:
            tg = float(r['TG'])
            row_by_tg[tg] = r
        except:
            continue
    value_scores = []
    for pt in tg_pts:
        best_key = min(row_by_tg.keys(), key=lambda k: abs(k - pt))
        r = row_by_tg[best_key]
        for q in ['P', 'epsilon33', 'd33', 'phi', 'phi_prime']:
            ref = targets[str(pt)][q]
            tol = tols[q]
            try:
                val = float(r[q])
            except:
                return 0.0
            rel_err = abs(val - ref) / (abs(ref) + 1e-12)
            if rel_err <= tol:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (rel_err - tol) / (tol * 5))
            value_scores.append(score_q)
    value_score = np.mean(value_scores) if value_scores else 0.0
    tg_all = sorted(row_by_tg.keys())
    if len(tg_all) < 2:
        return value_score
    trend_scores = []
    for q, direction in trends.items():
        vals = []
        for tg in tg_all:
            try:
                vals.append(float(row_by_tg[tg][q]))
            except:
                trend_scores.append(0.0)
                break
        else:
            diffs = np.diff(vals)
            if len(diffs) == 0:
                trend_scores.append(0.0)
                continue
            if direction == 'increasing':
                monotonic = np.all(diffs >= 0)
            else:
                monotonic = np.all(diffs <= 0)
            trend_scores.append(1.0 if monotonic else 0.0)
    trend_score = np.mean(trend_scores) if trend_scores else 0.0
    combined = 0.8 * value_score + 0.2 * trend_score
    return float(np.clip(combined, 0.0, 1.0))


# === block: score_3 (check id='mgo') ===
def score_3(artifact, step, ctx):
    step_cfg = ctx['step_configs']['mgo']
    tg_pts = step_cfg['tg_points']
    targets = step_cfg['target']
    tols = step_cfg['tolerance']
    trends = step_cfg['trend_config']
    rows = artifact
    if not rows:
        return 0.0
    cols = ['TG', 'P', 'epsilon33', 'd33', 'phi', 'phi_prime']
    for c in cols:
        if c not in rows[0]:
            return 0.0
    row_by_tg = {}
    for r in rows:
        try:
            tg = float(r['TG'])
            row_by_tg[tg] = r
        except:
            continue
    value_scores = []
    for pt in tg_pts:
        best_key = min(row_by_tg.keys(), key=lambda k: abs(k - pt))
        r = row_by_tg[best_key]
        for q in ['P', 'epsilon33', 'd33', 'phi', 'phi_prime']:
            ref = targets[str(pt)][q]
            tol = tols[q]
            try:
                val = float(r[q])
            except:
                return 0.0
            rel_err = abs(val - ref) / (abs(ref) + 1e-12)
            if rel_err <= tol:
                score_q = 1.0
            else:
                score_q = max(0.0, 1.0 - (rel_err - tol) / (tol * 5))
            value_scores.append(score_q)
    value_score = np.mean(value_scores) if value_scores else 0.0
    tg_all = sorted(row_by_tg.keys())
    if len(tg_all) < 2:
        return value_score
    trend_scores = []
    for q, direction in trends.items():
        vals = []
        for tg in tg_all:
            try:
                vals.append(float(row_by_tg[tg][q]))
            except:
                trend_scores.append(0.0)
                break
        else:
            diffs = np.diff(vals)
            if len(diffs) == 0:
                trend_scores.append(0.0)
                continue
            if direction == 'increasing':
                monotonic = np.all(diffs >= 0)
            else:
                monotonic = np.all(diffs <= 0)
            trend_scores.append(1.0 if monotonic else 0.0)
    trend_score = np.mean(trend_scores) if trend_scores else 0.0
    combined = 0.8 * value_score + 0.2 * trend_score
    return float(np.clip(combined, 0.0, 1.0))


_SCORERS = {
    'si': score_0,
    'c_sapphire': score_1,
    'a_sapphire': score_2,
    'mgo': score_3,
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
