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
    return {}


# === block: score_0 (check id='thermo_curves') ===
def score_0(artifact, step, ctx):
    rows = artifact
    # build per-system time series
    data = {}
    for r in rows:
        sys = r['system']
        T = float(r['temperature_K'])
        b2d = float(r['B2D_eV_Ang2'])
        alpha = float(r['alpha_1e6K'])
        data.setdefault(sys, []).append((T, b2d, alpha))
    for sys in data:
        data[sys].sort(key=lambda x: x[0])

    def get_value_at_T(series, T_target):
        # linear interpolation
        ts, vals = zip(*[(t, v) for t, v, _ in series])
        for i in range(len(ts)-1):
            if ts[i] <= T_target <= ts[i+1]:
                if ts[i+1] == ts[i]:
                    return vals[i]
                return vals[i] + (vals[i+1]-vals[i]) * (T_target - ts[i]) / (ts[i+1]-ts[i])
        return None

    def slope_at_300(series):
        # central finite difference around 300 K, using nearest points to 290 and 310
        b290 = get_value_at_T(series, 290.0)
        b310 = get_value_at_T(series, 310.0)
        if b290 is not None and b310 is not None:
            return (b310 - b290) / 20.0
        return None

    slopes = {}
    b2d_300 = {}
    b2d_0 = {}
    alpha_mean = {}
    for sys, pts in data.items():
        slopes[sys] = slope_at_300(pts)
        b2d_300[sys] = get_value_at_T(pts, 300.0)
        b2d_0[sys] = get_value_at_T(pts, 0.0)
        alphas = [a for _, _, a in pts]
        alpha_mean[sys] = sum(alphas) / len(alphas) if alphas else None

    score = 0.0
    total_checks = 6.0
    if slopes.get('Si') is not None and slopes['Si'] < 0:
        score += 1.0
    if slopes.get('Si') is not None and slopes.get('HSi') is not None and slopes['HSi'] > slopes['Si']:
        score += 1.0
    if b2d_300.get('HSi') is not None and b2d_300.get('Si') is not None and b2d_300['HSi'] < b2d_300['Si']:
        score += 1.0
    if b2d_300.get('HGe') is not None and b2d_300.get('Ge') is not None and b2d_300['HGe'] < b2d_300['Ge']:
        score += 1.0
    if alpha_mean.get('Si') is not None and alpha_mean['Si'] < 0:
        score += 1.0
    if alpha_mean.get('Ge') is not None and alpha_mean['Ge'] < 0:
        score += 1.0
    return score / total_checks


# === block: score_1 (check id='key_quantities') ===
def score_1(artifact, step, ctx):
    data = artifact
    csv_path = os.path.join('/app/outputs', 'thermodynamic_curves.csv')
    csv_rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            csv_rows.append(r)
    csv_data = {}
    for r in csv_rows:
        sys = r['system']
        T = float(r['temperature_K'])
        b2d = float(r['B2D_eV_Ang2'])
        csv_data.setdefault(sys, []).append((T, b2d))
    for sys in csv_data:
        csv_data[sys].sort(key=lambda x: x[0])

    def csv_value_at_T(series, T_target):
        ts, vals = zip(*[(t, v) for t, v in series])
        for i in range(len(ts)-1):
            if ts[i] <= T_target <= ts[i+1]:
                if ts[i+1] == ts[i]:
                    return vals[i]
                return vals[i] + (vals[i+1]-vals[i]) * (T_target - ts[i]) / (ts[i+1]-ts[i])
        return None

    def csv_slope_300(series):
        b290 = csv_value_at_T(series, 290.0)
        b310 = csv_value_at_T(series, 310.0)
        if b290 is not None and b310 is not None:
            return (b310 - b290) / 20.0
        return None

    csv_b2d_0 = {}
    csv_b2d_300 = {}
    csv_slopes = {}
    for sys, pts in csv_data.items():
        csv_b2d_0[sys] = csv_value_at_T(pts, 0.0)
        csv_b2d_300[sys] = csv_value_at_T(pts, 300.0)
        csv_slopes[sys] = csv_slope_300(pts)

    gold_anharm = step['gold_anharmonicity']
    anharm_tol = step['anharmonicity_rel_tol']
    b2d_tol = step['b2d_consistency_tol']
    slope_tol = step['slope_abs_tol']

    systems = ['Si','HSi','Ge','HGe']
    sub_scores = []
    for sys in systems:
        if sys not in data:
            sub_scores.extend([0.0,0.0,0.0,0.0])
            continue
        entry = data[sys]
        # B2D_0K
        ref = csv_b2d_0.get(sys)
        v = entry.get('B2D_0K')
        if ref is not None and v is not None and abs(v - ref) / (abs(ref)+1e-12) < b2d_tol:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.0)
        # B2D_300K
        ref = csv_b2d_300.get(sys)
        v = entry.get('B2D_300K')
        if ref is not None and v is not None and abs(v - ref) / (abs(ref)+1e-12) < b2d_tol:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.0)
        # slope
        ref = csv_slopes.get(sys)
        v = entry.get('dB2D_dT_300K')
        if ref is not None and v is not None and abs(v - ref) < slope_tol:
            sub_scores.append(1.0)
        else:
            sub_scores.append(0.0)
        # anharmonicity
        ref = gold_anharm.get(sys)
        v = entry.get('a_dB2Dstar_da')
        if v is not None and ref is not None:
            if (ref < 0 and v < 0) or (ref >= 0 and v >= 0):
                rel_err = abs(v - ref) / (abs(ref)+1e-12)
                if rel_err <= anharm_tol:
                    sub_scores.append(1.0)
                else:
                    sub_scores.append(0.0)
            else:
                sub_scores.append(0.0)
        else:
            sub_scores.append(0.0)
    return sum(sub_scores) / 16.0


_SCORERS = {
    'thermo_curves': score_0,
    'key_quantities': score_1,
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
