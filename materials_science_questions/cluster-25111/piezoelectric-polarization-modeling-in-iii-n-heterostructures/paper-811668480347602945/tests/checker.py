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
    return {}


# === block: score_0 (check id='step_gaaln') ===
def score_0(artifact, step, ctx):
    gold_dE = {6:36, 10:33, 16:30, 24:27, 32:24}
    gold_field_0 = {32:0.66}
    gold_field_10 = {32:0.87}
    tol_dE = 5.0
    tol_field = 0.05
    wells = [6,10,16,24,32]
    row_map = {row['well_width_ML']: row for row in artifact if row.get('well_width_ML') is not None}

    def check_val(ml):
        row = row_map.get(ml)
        if row is None:
            return 0.0
        dE = row.get('dE_dP_meV_per_GPa')
        if dE is None:
            return 0.0
        return 1.0 if abs(dE - gold_dE[ml]) <= tol_dE else 0.0

    dE_scores = [check_val(ml) for ml in wells]
    score_dE = sum(dE_scores) / len(dE_scores) * 0.6

    field_scores = []
    row32 = row_map.get(32)
    if row32:
        f0 = row32.get('field_0_GPa_MV_per_cm')
        f10 = row32.get('field_10_GPa_MV_per_cm')
        if f0 is not None and abs(f0 - 0.66) <= tol_field:
            field_scores.append(1.0)
        else:
            field_scores.append(0.0)
        if f10 is not None and abs(f10 - 0.87) <= tol_field:
            field_scores.append(1.0)
        else:
            field_scores.append(0.0)
    else:
        field_scores = [0.0, 0.0]
    score_field = sum(field_scores) / 2 * 0.3

    dE_vals = [row_map.get(ml, {}).get('dE_dP_meV_per_GPa') for ml in wells]
    trend_ok = True
    for i in range(len(wells)-1):
        a = dE_vals[i]
        b = dE_vals[i+1]
        if a is None or b is None:
            trend_ok = False
            break
        if a < b + 1e-12:
            trend_ok = False
            break
    score_trend = 0.1 if trend_ok else 0.0

    sc = score_dE + score_field + score_trend
    return min(sc, 1.0)


# === block: score_1 (check id='step_ingan_wurtzite') ===
def score_1(artifact, step, ctx):
    gold_5nm = -30.0
    tol_5nm = 5.0
    widths_expected = [1.0, 2.0, 2.5, 3.5, 4.0, 5.0]

    row_map = {}
    for row in artifact:
        w = row.get('well_width_nm')
        if w is not None:
            w = round(w, 1)
            row_map[w] = row

    dE_vals = []
    found_5nm = None
    for w in widths_expected:
        row = row_map.get(w)
        if row and row.get('dE_dP_meV_per_GPa') is not None:
            dE_vals.append(row['dE_dP_meV_per_GPa'])
        else:
            dE_vals.append(None)
        if w == 5.0:
            found_5nm = row.get('dE_dP_meV_per_GPa') if row else None

    # 5 nm value check (paper states model gives -30 meV/GPa)
    if found_5nm is not None and abs(found_5nm - gold_5nm) <= tol_5nm:
        score_5nm = 0.4
    else:
        score_5nm = 0.0

    # Strictly decreasing trend with well width
    valid_vals = [(w, v) for w, v in zip(widths_expected, dE_vals) if v is not None]
    trend_ok = True
    for i in range(len(valid_vals)-1):
        if valid_vals[i][1] <= valid_vals[i+1][1] + 1e-12:
            trend_ok = False
            break

    # 1 nm should be positive (QCSE still weak, no field-induced red shift dominates)
    positive_1nm = False
    row1 = row_map.get(1.0)
    if row1 and row1.get('dE_dP_meV_per_GPa') is not None:
        positive_1nm = row1['dE_dP_meV_per_GPa'] > 0

    score_trend = 0.4 if (trend_ok and positive_1nm) else 0.0

    # Crossing zero between 2 and 3 nm (low-weight consistency check)
    cross_zero = any(v is not None and v <= 0 for v in dE_vals[1:]) and any(v is not None and v >= 0 for v in dE_vals[:3])
    score_zero = 0.2 if cross_zero else 0.0

    total = score_5nm + score_trend + score_zero
    return min(total, 1.0)


# === block: score_2 (check id='step_ingan_cubic') ===
def score_2(artifact, step, ctx):
    gold = 28.5
    widths = [0.6, 1.0, 2.0, 3.0, 4.0, 5.0]
    tol = 3.0
    row_map = {}
    for row in artifact:
        w = row.get('well_width_nm')
        if w is not None:
            w = round(w, 1)
            row_map[w] = row

    dE_vals = []
    scores = []
    for w in widths:
        row = row_map.get(w)
        if row is None:
            scores.append(0.0)
            dE_vals.append(None)
            continue
        d = row.get('dE_dP_meV_per_GPa')
        if d is None:
            scores.append(0.0)
            dE_vals.append(None)
            continue
        dE_vals.append(d)
        scores.append(1.0 if abs(d - gold) <= tol else 0.0)

    score_dE = sum(scores) / len(scores) * 0.8

    # near-constant check
    if all(v is not None for v in dE_vals):
        spread = max(dE_vals) - min(dE_vals)
        const_ok = spread <= 2.0
    else:
        const_ok = False
    score_const = 0.2 if const_ok else 0.0

    return score_dE + score_const


_SCORERS = {
    'step_gaaln': score_0,
    'step_ingan_wurtzite': score_1,
    'step_ingan_cubic': score_2,
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
