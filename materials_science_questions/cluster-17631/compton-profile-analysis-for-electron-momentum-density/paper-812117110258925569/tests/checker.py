import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    fname = "j_bond_all_models.csv"
    path = os.path.join(outputs_dir, fname)
    data_by_model = {}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row['model']
            q = float(row['q'])
            jb = float(row['J_bond'])
            data_by_model.setdefault(model, []).append((q, jb))
    for model in data_by_model:
        data_by_model[model].sort(key=lambda x: x[0])
    return {'data': data_by_model}


# === block: score_0 (check id='sign_hydration') ===
def score_0(artifact, step, ctx):
    data = ctx['data']
    neg_models = step.get('config', {}).get('negative_models', [])
    pos_models = step.get('config', {}).get('positive_models', [])
    results = []
    for m in neg_models:
        pts = data.get(m, [])
        if not pts:
            results.append(False)
            continue
        q_vals, j_vals = zip(*pts)
        idx = min(range(len(q_vals)), key=lambda i: abs(q_vals[i]))
        results.append(j_vals[idx] < 0)
    for m in pos_models:
        pts = data.get(m, [])
        if not pts:
            results.append(False)
            continue
        q_vals, j_vals = zip(*pts)
        idx = min(range(len(q_vals)), key=lambda i: abs(q_vals[i]))
        results.append(j_vals[idx] > 0)
    if not results:
        return 0.0
    return sum(results) / len(results)


# === block: score_1 (check id='extremum_pos') ===
def score_1(artifact, step, ctx):
    data = ctx['data']
    pos_models = step.get('config', {}).get('positive_models', [])
    q_min = step.get('config', {}).get('q_min', 0.5)
    q_max = step.get('config', {}).get('q_max', 1.3)
    results = []
    for m in pos_models:
        pts = data.get(m, [])
        if not pts:
            results.append(False)
            continue
        q_vals, j_vals = zip(*pts)
        pos_pts = [(q, j) for q, j in zip(q_vals, j_vals) if q > 0]
        if not pos_pts:
            results.append(False)
            continue
        q_maxpos, _ = max(pos_pts, key=lambda x: x[1])
        results.append(q_min <= q_maxpos <= q_max)
    return sum(results) / len(results) if results else 0.0


# === block: score_2 (check id='linearity_Cl') ===
def score_2(artifact, step, ctx):
    data = ctx['data']
    prefix = step.get('config', {}).get('model_prefix', 'Cl_shell_1A_n')
    ns = step.get('config', {}).get('hs', [])
    r2_thresh = step.get('config', {}).get('r2_threshold', 0.8)
    amps = []
    for n in ns:
        m = f"{prefix}{n}"
        pts = data.get(m, [])
        if not pts:
            continue
        q_vals, j_vals = zip(*pts)
        reg = [(q, j) for q, j in zip(q_vals, j_vals) if 0.5 <= q <= 1.3]
        if not reg:
            reg = [(q, j) for q, j in zip(q_vals, j_vals) if q > 0]
        if not reg:
            continue
        max_abs = max(abs(v) for _, v in reg)
        amps.append((n, max_abs))
    if len(amps) < 3:
        return 0.0
    x_vals = [a[0] for a in amps]
    y_vals = [a[1] for a in amps]
    N = len(x_vals)
    mean_x = sum(x_vals) / N
    mean_y = sum(y_vals) / N
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    den1 = sum((x - mean_x) ** 2 for x in x_vals)
    den2 = sum((y - mean_y) ** 2 for y in y_vals)
    if den1 == 0 or den2 == 0:
        return 0.0
    r2 = (num / (den1 ** 0.5 * den2 ** 0.5)) ** 2
    if r2 >= r2_thresh:
        return 1.0
    else:
        return max(0.0, (r2 - 0.5) / 0.3)


# === block: score_3 (check id='pairwise_trend') ===
def score_3(artifact, step, ctx):
    data = ctx['data']
    distances = step.get('config', {}).get('distances', [])
    ampls = []
    for d in distances:
        model = f"pair_Li_Cl_d{d:.1f}"
        pts = data.get(model, [])
        if not pts:
            continue
        q_vals, j_vals = zip(*pts)
        reg = [(q, j) for q, j in zip(q_vals, j_vals) if 0.5 <= q <= 2.5]
        if not reg:
            reg = [(q, j) for q, j in zip(q_vals, j_vals) if q > 0]
        if not reg:
            continue
        amp = max(abs(v) for _, v in reg)
        ampls.append(amp)
    if len(ampls) < 2:
        return 0.0
    monotonic = all(ampls[i] >= ampls[i+1] for i in range(len(ampls)-1))
    return 1.0 if monotonic else 0.0


# === block: score_4 (check id='ion_pair_dist') ===
def score_4(artifact, step, ctx):
    data = ctx['data']
    ssip1 = step.get('config', {}).get('ssip1', 'LiCl_3A_n10')
    ssip2 = step.get('config', {}).get('ssip2', 'LiCl_3A_n9')
    cip = step.get('config', {}).get('cip', 'LiCl_3A_n8')
    limit = step.get('config', {}).get('rms_diff_similar_frac_limit', 0.35)

    def get_q_j_range(model, qrang=(-2.0, 2.0)):
        pts = data.get(model, [])
        if not pts:
            return None, None
        qs, js = zip(*pts)
        pairs = [(q, j) for q, j in zip(qs, js) if qrang[0] <= q <= qrang[1]]
        if not pairs:
            return None, None
        qs_f, js_f = zip(*pairs)
        return qs_f, js_f

    q1, j1 = get_q_j_range(ssip1)
    q2, j2 = get_q_j_range(ssip2)
    qc, jc = get_q_j_range(cip)
    if q1 is None or q2 is None or qc is None:
        return 0.0
    if len(j1) != len(j2) or len(j1) != len(jc):
        return 0.0

    def rms_diff(jA, jB):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(jA, jB)) / len(jA))

    d_ssip = rms_diff(j1, j2)
    d_cip1 = rms_diff(j1, jc)
    d_cip2 = rms_diff(j2, jc)
    d_cip_avg = (d_cip1 + d_cip2) / 2.0
    if d_cip_avg == 0:
        return 0.0
    if d_ssip < limit * d_cip_avg:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'sign_hydration': score_0,
    'extremum_pos': score_1,
    'linearity_Cl': score_2,
    'pairwise_trend': score_3,
    'ion_pair_dist': score_4,
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
