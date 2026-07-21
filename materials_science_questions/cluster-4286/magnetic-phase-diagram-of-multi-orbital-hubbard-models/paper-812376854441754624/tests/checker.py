import os
import json
import csv

# === author imports / helpers ===
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
    path = os.path.join(outputs_dir, 'thermodynamic_properties.csv')
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return {'data': data}


# === block: score_0 (check id='peak_position') ===
def score_0(artifact, step, ctx):
    data = ctx['data']
    rows = [r for r in data if float(r['T']) < 1.0 and r['h_model'] in ('AHM_asym','XXZ_asym')]
    peaks = {}
    for r in rows:
        m = r['h_model']
        cv = float(r['C_V'])
        if m not in peaks or cv > peaks[m][0]:
            peaks[m] = (cv, float(r['T']))
    if 'AHM_asym' not in peaks or 'XXZ_asym' not in peaks:
        return 0.0
    t_a = peaks['AHM_asym'][1]
    t_x = peaks['XXZ_asym'][1]
    # Hidden gold peak temperature (digitized from Fig. 1 for t↑/t↓ = 0.3, U^{fd}=8)
    GOLD = 0.155
    if abs(t_a - GOLD) > 0.05:
        return 0.0
    if abs(t_a - t_x) > 0.05:
        return 0.0
    return 1.0


# === block: score_1 (check id='peak_ordering') ===
def score_1(artifact, step, ctx):
    data = ctx['data']
    rows_s = [r for r in data if float(r['T']) < 1.0 and r['h_model'] == 'AHM_sym']
    rows_a = [r for r in data if float(r['T']) < 1.0 and r['h_model'] == 'AHM_asym']
    if not rows_s or not rows_a:
        return 0.0
    t_s = max(rows_s, key=lambda r: float(r['C_V']))['T']
    t_a = max(rows_a, key=lambda r: float(r['C_V']))['T']
    return 1.0 if float(t_s) > float(t_a) else 0.0


# === block: score_2 (check id='peak_sharpness') ===
def score_2(artifact, step, ctx):
    data = ctx['data']
    def fwhm(rows):
        xs = sorted([(float(r['T']), float(r['C_V'])) for r in rows], key=lambda x: x[0])
        if len(xs) < 3:
            return None
        max_cv = max(v for _,v in xs)
        half = max_cv/2.0
        left, right = None, None
        for i in range(len(xs)-1):
            v1 = xs[i][1]
            v2 = xs[i+1][1]
            if (v1 < half <= v2) or (v1 > half >= v2):
                frac = (half - v1) / (v2 - v1) if v2 != v1 else 0.5
                t_cross = xs[i][0] + frac * (xs[i+1][0] - xs[i][0])
                if left is None:
                    left = t_cross
                else:
                    right = t_cross
        if left is None or right is None:
            return None
        return right - left
    rows_s = [r for r in data if r['h_model'] == 'AHM_sym']
    rows_a = [r for r in data if r['h_model'] == 'AHM_asym']
    w_s = fwhm(rows_s)
    w_a = fwhm(rows_a)
    if w_s is None or w_a is None:
        return 0.0
    return 1.0 if w_s > w_a else 0.0


# === block: score_3 (check id='magnetization') ===
def score_3(artifact, step, ctx):
    data = ctx['data']
    check_t = [0.05, 0.10, 0.15]
    for r in data:
        if r['h_model'] in ('AHM_sym','AHM_asym') and abs(float(r['T']) - 0.05) < 1e-6:
            if abs(float(r['M'])) >= 0.1:
                return 0.0
        # general check for all low-T points
    for r in data:
        if r['h_model'] in ('AHM_sym','AHM_asym') and float(r['T']) <= 0.15:
            if abs(float(r['M'])) >= 0.1:
                return 0.0
    return 1.0


_SCORERS = {
    'peak_position': score_0,
    'peak_ordering': score_1,
    'peak_sharpness': score_2,
    'magnetization': score_3,
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
