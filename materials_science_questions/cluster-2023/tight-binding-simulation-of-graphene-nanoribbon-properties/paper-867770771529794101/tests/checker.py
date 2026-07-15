import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    gold = {}
    for step in spec.get("steps", []):
        pts = step.get("gold_points")
        if pts:
            gold[step["output_file"]] = pts
    return {"gold": gold}


# === block: score_0 (check id='check_occupancy') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    points = []
    for r in rows:
        try:
            eps = float(r['epsilon_d'])
            nd = float(r['N_d'])
            points.append((eps, nd))
        except:
            pass
    if len(points) < 5:
        return 0.0
    gold_points = ctx['gold']['occupancy.csv']
    xp = sorted([g['epsilon_d'] for g in gold_points])
    fp = [g['N_d'] for g in sorted(gold_points, key=lambda x: x['epsilon_d'])]
    def interp(x, xp, fp):
        if x <= xp[0]:
            return fp[0]
        if x >= xp[-1]:
            return fp[-1]
        i = 0
        while i < len(xp) - 1 and x > xp[i+1]:
            i += 1
        t = (x - xp[i]) / (xp[i+1] - xp[i])
        return fp[i] + t * (fp[i+1] - fp[i])
    tol = 0.05
    score_sum = 0.0
    for eps, nd in points:
        gold_nd = interp(eps, xp, fp)
        err = abs(nd - gold_nd)
        if err <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (err - tol) / 0.15)
        score_sum += s
    avg_acc = score_sum / len(points)
    pts_sorted = sorted(points, key=lambda x: x[0])
    nd_vals = [p[1] for p in pts_sorted]
    is_mono = all(nd_vals[i] >= nd_vals[i-1] for i in range(1, len(nd_vals)))
    mono = 1.0 if is_mono and len(nd_vals) >= 2 else 0.0
    return 0.8 * avg_acc + 0.2 * mono


# === block: score_1 (check id='check_mae_peakpos') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    points = []
    for r in rows:
        try:
            eps = float(r['epsilon_d'])
            peak = float(r['peak_position'])
            mae = float(r['MAE'])
            points.append((eps, peak, mae))
        except:
            pass
    if len(points) < 5:
        return 0.0
    gold_points = ctx['gold']['mae_peakpos.csv']
    xp = sorted([g['epsilon_d'] for g in gold_points])
    fp_peak = [g['peak_position'] for g in sorted(gold_points, key=lambda x: x['epsilon_d'])]
    fp_mae = [g['MAE'] for g in sorted(gold_points, key=lambda x: x['epsilon_d'])]
    def interp(x, xp, fp):
        if x <= xp[0]:
            return fp[0]
        if x >= xp[-1]:
            return fp[-1]
        i = 0
        while i < len(xp) - 1 and x > xp[i+1]:
            i += 1
        t = (x - xp[i]) / (xp[i+1] - xp[i])
        return fp[i] + t * (fp[i+1] - fp[i])
    tol_peak = 10.0
    tol_mae = 1.0
    peak_scores = []
    mae_scores = []
    for eps, peak, mae in points:
        g_peak = interp(eps, xp, fp_peak)
        g_mae = interp(eps, xp, fp_mae)
        err_peak = abs(peak - g_peak)
        if err_peak <= tol_peak:
            s_p = 1.0
        else:
            s_p = max(0.0, 1.0 - (err_peak - tol_peak) / 20.0)
        peak_scores.append(s_p)
        err_mae = abs(mae - g_mae)
        if err_mae <= tol_mae:
            s_m = 1.0
        else:
            s_m = max(0.0, 1.0 - (err_mae - tol_mae) / 2.0)
        mae_scores.append(s_m)
    avg_peak = sum(peak_scores) / len(peak_scores)
    avg_mae = sum(mae_scores) / len(mae_scores)
    pts_sorted = sorted(points, key=lambda x: x[0])
    peak_vals = [p[1] for p in pts_sorted]
    mae_vals = [p[2] for p in pts_sorted]
    is_peak_mono = all(peak_vals[i] <= peak_vals[i-1] for i in range(1, len(peak_vals)))
    is_mae_mono = all(mae_vals[i] <= mae_vals[i-1] for i in range(1, len(mae_vals)))
    mono = 1.0 if (is_peak_mono and is_mae_mono and len(peak_vals) >= 2) else 0.0
    return 0.45 * avg_peak + 0.45 * avg_mae + 0.1 * mono


_SCORERS = {
    'check_occupancy': score_0,
    'check_mae_peakpos': score_1,
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
