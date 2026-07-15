import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='shape_valid') ===
def score_0(artifact, step, ctx):
    required_top = ['isomers', 'T30', 'T_series']
    if not isinstance(artifact, dict):
        return 0.0
    if not all(k in artifact for k in required_top):
        return 0.0

    expected_isomers = ['(5|0)', '(5|5)', '(22|0)']
    isomers = artifact.get('isomers')
    if not isinstance(isomers, list) or isomers != expected_isomers:
        return 0.0

    T30 = artifact.get('T30', {})
    if not isinstance(T30, dict):
        return 0.0
    for iso in expected_isomers:
        block = T30.get(iso)
        if not isinstance(block, dict):
            return 0.0
        shift = block.get('shift_cm-1')
        gamma = block.get('Gamma_cm-1')
        gamma_tilde = block.get('Gamma_tilde_cm-1')
        if not isinstance(shift, (int, float)) or not isinstance(gamma, (int, float)) or not isinstance(gamma_tilde, (int, float)):
            return 0.0
        if math.isnan(shift) or math.isinf(shift) or math.isnan(gamma) or math.isinf(gamma) or math.isnan(gamma_tilde) or math.isinf(gamma_tilde):
            return 0.0
        if shift >= 0.0:   # red shifts must be strictly negative
            return 0.0
        if gamma <= 0.0 or gamma_tilde <= 0.0:
            return 0.0

    expected_T_K = [5, 10, 15, 20, 30, 40]
    T_series = artifact.get('T_series', {})
    if not isinstance(T_series, dict):
        return 0.0
    for iso in expected_isomers:
        item = T_series.get(iso)
        if not isinstance(item, dict):
            return 0.0
        T_K = item.get('T_K')
        if not isinstance(T_K, list) or T_K != expected_T_K:
            return 0.0
        n = len(expected_T_K)
        for field in ['shift_cm-1', 'Gamma_cm-1', 'Gamma_tilde_cm-1']:
            lst = item.get(field)
            if not isinstance(lst, list) or len(lst) != n:
                return 0.0
            for v in lst:
                if not isinstance(v, (int, float)):
                    return 0.0
                if math.isnan(v) or math.isinf(v):
                    return 0.0
                if field == 'shift_cm-1' and v >= 0.0:
                    return 0.0
                if field in ('Gamma_cm-1', 'Gamma_tilde_cm-1') and v <= 0.0:
                    return 0.0

    return 1.0


# === block: score_1 (check id='T30_shifts') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance', 5)
    T30 = artifact.get('T30', {})
    isomers = ['(5|0)', '(5|5)', '(22|0)']
    count = 0
    for iso in isomers:
        val = (T30.get(iso) or {}).get('shift_cm-1')
        g = gold.get(iso)
        if val is not None and g is not None and abs(val - g) <= tol:
            count += 1
    return count / len(isomers)


# === block: score_2 (check id='T30_Gamma') ===
def score_2(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance', 2)
    T30 = artifact.get('T30', {})
    isomers = ['(5|0)', '(5|5)', '(22|0)']
    count = 0
    for iso in isomers:
        val = (T30.get(iso) or {}).get('Gamma_cm-1')
        g = gold.get(iso)
        if val is not None and g is not None and abs(val - g) <= tol:
            count += 1
    return count / len(isomers)


# === block: score_3 (check id='T30_Gamma_tilde') ===
def score_3(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance', 2)
    T30 = artifact.get('T30', {})
    isomers = ['(5|0)', '(5|5)', '(22|0)']
    count = 0
    for iso in isomers:
        val = (T30.get(iso) or {}).get('Gamma_tilde_cm-1')
        g = gold.get(iso)
        if val is not None and g is not None and abs(val - g) <= tol:
            count += 1
    return count / len(isomers)


# === block: score_4 (check id='temp_trend') ===
def score_4(artifact, step, ctx):
    T_series = artifact.get('T_series', {})
    score_parts = []

    # shift constancy: std <= 6 cm-1
    for iso in ['(5|0)', '(5|5)', '(22|0)']:
        s = T_series.get(iso, {})
        shifts = s.get('shift_cm-1', [])
        if len(shifts) >= 2:
            mean_sh = sum(shifts) / len(shifts)
            var = sum((x - mean_sh)**2 for x in shifts) / len(shifts)
            std = math.sqrt(var)
            if std <= 6.0:
                score_parts.append(1.0)
            else:
                score_parts.append(max(0.0, 1.0 - (std - 6.0)/2.0))
        else:
            score_parts.append(0.0)

    # linewidth trends for (5|0) and (5|5): no large drop, value at 40K not too low
    def get_val_at_T(series, field, T):
        TK = series.get('T_K', [])
        vals = series.get(field, [])
        if T in TK:
            idx = TK.index(T)
            if idx < len(vals):
                return vals[idx]
        return None

    for iso in ['(5|0)', '(5|5)']:
        series = T_series.get(iso, {})
        for field in ['Gamma_cm-1', 'Gamma_tilde_cm-1']:
            v30 = get_val_at_T(series, field, 30)
            v40 = get_val_at_T(series, field, 40)
            if v30 is not None and v40 is not None:
                if v40 >= v30 * 0.9:
                    score_parts.append(1.0)
                else:
                    score_parts.append(0.5)
            else:
                score_parts.append(0.5)   # partial credit if data missing

    # (22|0) abrupt increase: Gamma_tilde at 40K >= 1.3 * at 20K
    series22 = T_series.get('(22|0)', {})
    for field in ['Gamma_tilde_cm-1']:
        v20 = get_val_at_T(series22, field, 20)
        v40 = get_val_at_T(series22, field, 40)
        if v20 is not None and v40 is not None:
            if v40 >= 1.3 * v20:
                score_parts.append(1.0)
            else:
                score_parts.append(0.0)
        else:
            score_parts.append(0.0)

    if score_parts:
        return sum(score_parts) / len(score_parts)
    return 0.0


_SCORERS = {
    'shape_valid': score_0,
    'T30_shifts': score_1,
    'T30_Gamma': score_2,
    'T30_Gamma_tilde': score_3,
    'temp_trend': score_4,
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
