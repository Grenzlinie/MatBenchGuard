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


# === block: score_0 (check id='csv_check') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is list of dicts from CSV
    def _float_or_none(v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return None

    rows = [r for r in rows if r.get('strain') is not None and r.get('bandgap_ev') is not None]
    if not rows:
        return 0.0

    # Find row closest to strain=0 and strain=-0.0134
    def find_row(strain_target, tol=0.001):
        best = None
        best_diff = float('inf')
        for r in rows:
            strain_val = _float_or_none(r.get('strain'))
            if strain_val is not None:
                diff = abs(strain_val - strain_target)
                if diff < best_diff and diff <= tol:
                    best = r
                    best_diff = diff
        return best

    row_0 = find_row(0.0)
    row_134 = find_row(-0.0134)

    score_bg = 0.0
    if row_0 is not None and row_134 is not None:
        bg0 = _float_or_none(row_0.get('bandgap_ev'))
        bg1 = _float_or_none(row_134.get('bandgap_ev'))
        if bg0 is not None and bg1 is not None:
            reduction = bg0 - bg1
            delta = abs(reduction - 0.06)
            if delta <= 0.01:
                score_bg = 1.0
            elif delta <= 0.02:
                score_bg = 0.5

    score_stress = 0.0
    if row_134 is not None:
        stress_val = _float_or_none(row_134.get('stress_gpa'))
        if stress_val is not None:
            delta_s = abs(stress_val - 0.78)
            if delta_s <= 0.15:
                score_stress = 1.0
            elif delta_s <= 0.25:
                score_stress = 0.5

    # monotonic trend: Pearson r between strain and bandgap
    def pearson_r(x, y):
        n = len(x)
        if n < 2:
            return 0.0
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(a*b for a,b in zip(x,y))
        sum_x2 = sum(a*a for a in x)
        sum_y2 = sum(b*b for b in y)
        denom = math.sqrt((n*sum_x2 - sum_x*sum_x)*(n*sum_y2 - sum_y*sum_y))
        if denom == 0:
            return 0.0
        return (n*sum_xy - sum_x*sum_y) / denom

    strains = []
    bandgaps = []
    for r in rows:
        s = _float_or_none(r.get('strain'))
        b = _float_or_none(r.get('bandgap_ev'))
        if s is not None and b is not None:
            strains.append(s)
            bandgaps.append(b)

    score_trend = 0.0
    if len(strains) >= 2:
        r_val = pearson_r(strains, bandgaps)
        if r_val > 0.95:
            score_trend = 1.0

    return 0.4*score_bg + 0.4*score_stress + 0.2*score_trend


# === block: score_1 (check id='bond_lengths_check') ===
def score_1(artifact, step, ctx):
    data = artifact  # dict
    if not isinstance(data, dict):
        return 0.0
    equil = data.get('equilibrium')
    strained = data.get('strained_1.34')
    if not isinstance(equil, dict) or not isinstance(strained, dict):
        return 0.0

    try:
        pbi0 = float(equil['pb_i_A'])
        pbi1 = float(strained['pb_i_A'])
        pbr0 = float(equil['pb_br_A'])
        pbr1 = float(strained['pb_br_A'])
    except (KeyError, ValueError, TypeError):
        return 0.0

    delta_pbi = pbi1 - pbi0
    delta_pbr = pbr1 - pbr0

    s_pbi = 0.0
    if abs(delta_pbi - 0.006) <= 0.01:
        s_pbi = 1.0
    elif abs(delta_pbi - 0.006) <= 0.02:
        s_pbi = 0.5

    s_pbr = 0.0
    if abs(delta_pbr - (-0.040)) <= 0.01:
        s_pbr = 1.0
    elif abs(delta_pbr - (-0.040)) <= 0.02:
        s_pbr = 0.5

    return (s_pbi + s_pbr) / 2.0


_SCORERS = {
    'csv_check': score_0,
    'bond_lengths_check': score_1,
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
