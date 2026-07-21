import os
import json
import csv


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
    return {
        'fit_params': spec.get('fit_params', {}),
        'shear_divergence': spec.get('shear_divergence', {})
    }


# === block: score_0 (check id='csv_sanity') ===
def score_0(artifact, step, ctx):
    expected_combos = set((o,l) for o in ['zigzag','armchair'] for l in [1,2,3,4,5,8])
    present = set()
    for row in artifact:
        ori = str(row.get('orientation','')).strip().lower()
        try:
            lay = int(row['layers'])
        except (ValueError, TypeError):
            continue
        present.add((ori, lay))
    score = 1.0 if present == expected_combos else 0.0


# === block: score_1 (check id='shear_divergence') ===
def score_1(artifact, step, ctx):
    gold = ctx['shear_divergence']
    max_diff_small = gold['layers_1_5_max_diff']
    min_diff_large = gold['layer_8_min_diff']
    mod_min = gold['modulus_min']
    mod_max = gold['modulus_max']
    data = {}
    for row in artifact:
        ori = str(row.get('orientation','')).strip().lower()
        try:
            lay = int(row['layers'])
            mod = float(row['shear_modulus_GPa'])
        except (ValueError, KeyError):
            continue
        data[(ori, lay)] = mod
    # check complete coverage
    for o in ['zigzag','armchair']:
        for l in [1,2,3,4,5,8]:
            if (o,l) not in data:
                return 0.0
    all_ok = True
    for key, mod in data.items():
        if mod < mod_min or mod > mod_max:
            all_ok = False
    for lay in [1,2,3,4,5]:
        z = data[('zigzag', lay)]
        a = data[('armchair', lay)]
        if abs(z - a) > max_diff_small:
            all_ok = False
    z8 = data[('zigzag', 8)]
    a8 = data[('armchair', 8)]
    if abs(z8 - a8) < min_diff_large:
        all_ok = False
    score = 1.0 if all_ok else 0.0


# === block: score_2 (check id='ultimate_stress_fit') ===
def score_2(artifact, step, ctx):
    def linear_fit(xs, ys):
        n = len(xs)
        sum_x = sum(xs)
        sum_y = sum(ys)
        sum_xy = sum(x*y for x,y in zip(xs, ys))
        sum_x2 = sum(x*x for x in xs)
        denom = n*sum_x2 - sum_x*sum_x
        if denom == 0:
            return 0.0, 0.0
        m = (n*sum_xy - sum_x*sum_y) / denom
        b = (sum_y - m*sum_x) / n
        return m, b

    tols = step.get('tolerances', {})
    rtol_m = tols.get('rtol_m', 0.15)
    atol_m = tols.get('atol_m', 0.2)
    rtol_n = tols.get('rtol_n', 0.1)
    atol_n = tols.get('atol_n', 10.0)
    gold_params = ctx['fit_params'].get('ultimate_stress', {})
    orientations = ['zigzag', 'armchair']
    scores = []
    for ori in orientations:
        x = []
        y = []
        for row in artifact:
            if str(row.get('orientation','')).strip().lower() == ori:
                try:
                    lay = int(row['layers'])
                    stress = float(row['ultimate_stress_GPa'])
                except (ValueError, KeyError):
                    continue
                x.append(lay)
                y.append(stress)
        if len(x) < 2:
            return 0.0
        m, b = linear_fit(x, y)
        gold = gold_params.get(ori, {})
        gm = gold.get('m', 0)
        gn = gold.get('n', 0)
        err_m = abs(m - gm)
        tol_m = max(atol_m, rtol_m * abs(gm)) if abs(gm) > 1e-9 else atol_m
        score_m = max(0.0, 1.0 - err_m / tol_m)
        err_n = abs(b - gn)
        tol_n = max(atol_n, rtol_n * abs(gn)) if abs(gn) > 1e-9 else atol_n
        score_n = max(0.0, 1.0 - err_n / tol_n)
        scores.append((score_m + score_n) / 2.0)
    score = sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='failure_strain_fit') ===
def score_3(artifact, step, ctx):
    def linear_fit(xs, ys):
        n = len(xs)
        sum_x = sum(xs)
        sum_y = sum(ys)
        sum_xy = sum(x*y for x,y in zip(xs, ys))
        sum_x2 = sum(x*x for x in xs)
        denom = n*sum_x2 - sum_x*sum_x
        if denom == 0:
            return 0.0, 0.0
        m = (n*sum_xy - sum_x*sum_y) / denom
        b = (sum_y - m*sum_x) / n
        return m, b

    tols = step.get('tolerances', {})
    rtol_m = tols.get('rtol_m', 0.2)
    atol_m = tols.get('atol_m', 0.0005)
    rtol_n = tols.get('rtol_n', 0.1)
    atol_n = tols.get('atol_n', 0.05)
    gold_params = ctx['fit_params'].get('failure_strain', {})
    orientations = ['zigzag', 'armchair']
    scores = []
    for ori in orientations:
        x = []
        y = []
        for row in artifact:
            if str(row.get('orientation','')).strip().lower() == ori:
                try:
                    lay = int(row['layers'])
                    strain = float(row['failure_strain'])
                except (ValueError, KeyError):
                    continue
                x.append(lay)
                y.append(strain)
        if len(x) < 2:
            return 0.0
        m, b = linear_fit(x, y)
        gold = gold_params.get(ori, {})
        gm = gold.get('m', 0)
        gn = gold.get('n', 0)
        err_m = abs(m - gm)
        tol_m = max(atol_m, rtol_m * abs(gm)) if abs(gm) > 1e-9 else atol_m
        score_m = max(0.0, 1.0 - err_m / tol_m)
        err_n = abs(b - gn)
        tol_n = max(atol_n, rtol_n * abs(gn)) if abs(gn) > 1e-9 else atol_n
        score_n = max(0.0, 1.0 - err_n / tol_n)
        scores.append((score_m + score_n) / 2.0)
    score = sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'csv_sanity': score_0,
    'shear_divergence': score_1,
    'ultimate_stress_fit': score_2,
    'failure_strain_fit': score_3,
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
