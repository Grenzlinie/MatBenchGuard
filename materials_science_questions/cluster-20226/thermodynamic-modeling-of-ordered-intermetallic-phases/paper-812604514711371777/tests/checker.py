import os
import json
import csv

# === author imports / helpers ===
import math
from collections import OrderedDict


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
    import os, csv, json

    ctx = {}
    # load formation_energies.csv
    path = os.path.join(outputs_dir, 'formation_energies.csv')
    try:
        with open(path, newline='') as f:
            ctx['formation_rows'] = list(csv.DictReader(f))
    except:
        ctx['formation_rows'] = []
    # load cluster_expansion_coefficients.json
    path = os.path.join(outputs_dir, 'cluster_expansion_coefficients.json')
    try:
        with open(path) as f:
            ctx['eci'] = json.load(f)
    except:
        ctx['eci'] = {}
    # load solubility_results.json (not used in current scorers, but for completeness)
    path = os.path.join(outputs_dir, 'solubility_results.json')
    try:
        with open(path) as f:
            ctx['solubility'] = json.load(f)
    except:
        ctx['solubility'] = {}
    return ctx


# === block: score_0 (check id='pdte_monotonic') ===
def score_0(artifact, step, ctx):
    corr_thresh = step.get('params', {}).get('correlation_threshold', 0.9)
    pdte = []
    for row in artifact:
        if row.get('phase') == 'PdTe':
            try:
                comp = float(row['composition'])
                ene = float(row['formation_energy'])
                pdte.append((comp, ene))
            except:
                pass
    if len(pdte) < 3:
        return 0.0
    xs = [x for x, y in pdte]
    ys = [y for x, y in pdte]
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
    den = math.sqrt(sum((xs[i] - mean_x) ** 2 for i in range(n)) * sum((ys[i] - mean_y) ** 2 for i in range(n)))
    if den == 0:
        return 0.0
    r = num / den
    if r >= corr_thresh:
        return 1.0
    else:
        return max(0.0, min(1.0, r / corr_thresh))


# === block: score_1 (check id='eci_r2') ===
def score_1(artifact, step, ctx):
    r2_thresh = step.get('params', {}).get('r2_threshold', 0.9)
    rows = ctx.get('formation_rows', [])
    eci = ctx.get('eci')
    if not rows or not eci:
        return 0.0
    ys = []
    y_preds = []
    for row in rows:
        phase = row.get('phase')
        if phase not in eci:
            continue
        try:
            x = float(row['composition'])
            y = float(row['formation_energy'])
        except:
            continue
        ec = eci[phase]
        t = 2 * x - 1
        pred = ec.get('J0', 0.0)
        if 'J1' in ec:
            pred += ec['J1'] * t
        if 'J2' in ec:
            pred += ec['J2'] * t ** 2
        if 'J3' in ec:
            pred += ec['J3'] * t ** 3
        ys.append(y)
        y_preds.append(pred)
    if len(ys) < 2:
        return 0.0
    mean_y = sum(ys) / len(ys)
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    ss_res = sum((ys[i] - y_preds[i]) ** 2 for i in range(len(ys)))
    if ss_tot == 0:
        all_close = all(abs(ys[i] - y_preds[i]) < 1e-12 for i in range(len(ys)))
        return 1.0 if all_close else 0.0
    r2 = 1 - ss_res / ss_tot
    if r2 >= r2_thresh:
        return 1.0
    else:
        return max(0.0, min(1.0, r2 / r2_thresh))


# === block: score_2 (check id='solubility_check') ===
def score_2(artifact, step, ctx):
    k = 8.617e-5
    T = 1000.0
    params = step.get('params', {})
    tol = params.get('consistency_tol', 1e-4)
    thresholds = params.get('thresholds', {})
    eci = ctx.get('eci')
    submitted = artifact
    if not eci or not submitted:
        return 0.0
    recomputed = {}
    for phase in ['PdTe', 'Pd20Te7', 'hcp']:
        if phase not in eci:
            continue
        ec = eci[phase]
        if 'J2' in ec:
            J1 = ec.get('J1', 0.0)
            J2 = ec.get('J2', 0.0)
            J3 = ec.get('J3', 0.0)
            b = 2 * (J1 - 2 * J2 + 3 * J3)
        else:
            J1 = ec.get('J1', 0.0)
            b = 2 * J1
        exp_arg = -b / (k * T)
        if exp_arg > 100:
            x = 0.0
        else:
            x = math.exp(exp_arg) / (1 + math.exp(exp_arg))
        recomputed[phase] = x
    keys_map = {'PdTe': 'Ru_in_PdTe_1000K', 'Pd20Te7': 'Ru_in_Pd20Te7_1000K', 'hcp': 'Pd_in_hcp_1000K'}
    for phase, key in keys_map.items():
        if phase not in recomputed:
            continue
        if key not in submitted:
            return 0.0
        try:
            sub_val = float(submitted[key])
        except:
            return 0.0
        if abs(sub_val - recomputed[phase]) > tol:
            return 0.0
    score = 0.0
    for phase, key in keys_map.items():
        if key not in submitted or phase not in recomputed:
            continue
        thresh = thresholds.get(key)
        if thresh is not None:
            if recomputed[phase] <= thresh:
                score += 1.0 / 3.0
    return min(score, 1.0)


_SCORERS = {
    'pdte_monotonic': score_0,
    'eci_r2': score_1,
    'solubility_check': score_2,
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
