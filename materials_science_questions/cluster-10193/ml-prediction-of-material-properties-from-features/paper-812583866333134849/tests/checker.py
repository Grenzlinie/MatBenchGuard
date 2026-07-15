import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math

def accuracy_score(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true) if y_true else 0.0

def f1_score(y_true, y_pred, label):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == label and p == label)
    fp = sum(1 for p in y_pred if p == label) - tp
    fn = sum(1 for t in y_true if t == label) - tp
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0

def r2_score(y_true, y_pred):
    mean = sum(y_true) / len(y_true)
    ss_res = sum((t - p) ** 2 for t, p in zip(y_true, y_pred))
    ss_tot = sum((t - mean) ** 2 for t in y_true)
    return 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

def mae_score(y_true, y_pred):
    return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true) if y_true else 0.0

def group_by_metal(rows):
    groups = {}
    for row in rows:
        metal = row['metal']
        groups.setdefault(metal, []).append(row)
    return groups


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


# === block: score_0 (check id='scored_predictions_coordination') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not all(k in rows[0] for k in ['metal','true_coordination','predicted_coordination']):
        return 0.0
    metal_groups = group_by_metal(rows)
    thresholds = step['thresholds']
    metals = list(thresholds['accuracy'].keys())
    checks = []
    for metal in metals:
        group = metal_groups.get(metal, [])
        if not group:
            checks.append(0)
            continue
        y_true = [int(r['true_coordination']) for r in group]
        y_pred = [int(r['predicted_coordination']) for r in group]
        acc = accuracy_score(y_true, y_pred)
        thr_acc = thresholds['accuracy'].get(metal, 1.0)
        checks.append(1.0 if acc >= thr_acc - 1e-9 else 0.0)
        for cl in [4,5,6]:
            f1 = f1_score(y_true, y_pred, cl)
            thr = thresholds['f1_'+str(cl)].get(metal, 1.0)
            checks.append(1.0 if f1 >= thr - 1e-9 else 0.0)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_1 (check id='scored_predictions_distance') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or not all(k in rows[0] for k in ['metal','true_distance','predicted_distance']):
        return 0.0
    metal_groups = group_by_metal(rows)
    thresholds = step['thresholds']
    metals = list(thresholds['R2'].keys())
    checks = []
    for metal in metals:
        group = metal_groups.get(metal, [])
        if not group:
            checks.append(0)
            continue
        y_true = [float(r['true_distance']) for r in group]
        y_pred = [float(r['predicted_distance']) for r in group]
        r2 = r2_score(y_true, y_pred)
        thr_r2 = thresholds['R2'].get(metal, 1.0)
        checks.append(1.0 if r2 >= thr_r2 - 1e-9 else 0.0)
        mae = mae_score(y_true, y_pred)
        thr_mae = thresholds['MAE'].get(metal, 0.0)
        checks.append(1.0 if mae <= thr_mae + 1e-9 else 0.0)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_2 (check id='scored_predictions_charge') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or not all(k in rows[0] for k in ['metal','true_charge','predicted_charge']):
        return 0.0
    metal_groups = group_by_metal(rows)
    thresholds = step['thresholds']
    metals = list(thresholds['R2'].keys())
    checks = []
    for metal in metals:
        group = metal_groups.get(metal, [])
        if not group:
            checks.append(0)
            continue
        y_true = [float(r['true_charge']) for r in group]
        y_pred = [float(r['predicted_charge']) for r in group]
        r2 = r2_score(y_true, y_pred)
        thr_r2 = thresholds['R2'].get(metal, 1.0)
        checks.append(1.0 if r2 >= thr_r2 - 1e-9 else 0.0)
        mae = mae_score(y_true, y_pred)
        thr_mae = thresholds['MAE'].get(metal, 0.0)
        checks.append(1.0 if mae <= thr_mae + 1e-9 else 0.0)
    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_3 (check id='scored_metrics_json') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    import os
    # Recompute all metrics from the three prediction CSVs
    base = '/app/outputs'
    coord_path = os.path.join(base, 'predictions_coordination.csv')
    dist_path = os.path.join(base, 'predictions_distance.csv')
    charge_path = os.path.join(base, 'predictions_charge.csv')
    def load_csv(p):
        with open(p, newline='') as f:
            return list(csv.DictReader(f))
    coord_rows = load_csv(coord_path)
    dist_rows = load_csv(dist_path)
    charge_rows = load_csv(charge_path)
    def compute_coord_metrics(rows):
        metals = sorted(set(r['metal'] for r in rows))
        out = {}
        for m in metals:
            g = [r for r in rows if r['metal']==m]
            if not g: continue
            yt = [int(r['true_coordination']) for r in g]
            yp = [int(r['predicted_coordination']) for r in g]
            acc = accuracy_score(yt, yp)
            f1s = {cl: f1_score(yt, yp, cl) for cl in [4,5,6]}
            out[m] = {'accuracy': acc, 'f1_4': f1s[4], 'f1_5': f1s[5], 'f1_6': f1s[6]}
        return out
    def compute_reg_metrics(rows, true_col, pred_col):
        metals = sorted(set(r['metal'] for r in rows))
        out = {}
        for m in metals:
            g = [r for r in rows if r['metal']==m]
            if not g: continue
            yt = [float(r[true_col]) for r in g]
            yp = [float(r[pred_col]) for r in g]
            out[m] = {'R2': r2_score(yt, yp), 'MAE': mae_score(yt, yp)}
        return out
    recomputed = {
        'coordination': compute_coord_metrics(coord_rows),
        'distance': compute_reg_metrics(dist_rows, 'true_distance', 'predicted_distance'),
        'charge': compute_reg_metrics(charge_rows, 'true_charge', 'predicted_charge')
    }
    # Compare with submitted metrics.json
    sub = artifact
    for prop in ['coordination','distance','charge']:
        if prop not in sub:
            return 0.0
        if prop == 'coordination':
            for m in recomputed[prop]:
                if m not in sub[prop]: return 0.0
                for k in ['accuracy','f1_4','f1_5','f1_6']:
                    if abs(sub[prop][m].get(k,0) - recomputed[prop][m][k]) > step['tolerance']:
                        return 0.0
        else:
            for m in recomputed[prop]:
                if m not in sub[prop]: return 0.0
                for k in ['R2','MAE']:
                    if abs(sub[prop][m].get(k,0) - recomputed[prop][m][k]) > step['tolerance']:
                        return 0.0
    return 1.0


_SCORERS = {
    'scored_predictions_coordination': score_0,
    'scored_predictions_distance': score_1,
    'scored_predictions_charge': score_2,
    'scored_metrics_json': score_3,
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
