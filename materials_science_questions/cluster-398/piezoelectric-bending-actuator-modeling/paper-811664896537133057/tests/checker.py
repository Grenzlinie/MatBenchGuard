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


# === block: score_0 (check id='damage_existence') ===
def score_0(artifact, step, ctx):
    cols = {'f','S','D11_M','D33_M','D11_E','D33_E'}
    if not artifact or not isinstance(artifact, list) or not all(k in artifact[0].keys() for k in cols):
        return 0.0
    return 1.0


# === block: score_1 (check id='damage_monotonic_f') ===
def score_1(artifact, step, ctx):
    rows = [r for r in artifact if abs(float(r['S'])-1.0) < 1e-6]
    if len(rows) < 3:
        return 0.0
    rows.sort(key=lambda r: float(r['f']))
    fractions = []
    for key in ['D11_M','D33_M']:
        vals = [float(r[key]) for r in rows]
        ok = sum(1 for i in range(len(vals)-1) if vals[i+1] >= vals[i] - 1e-8)
        fractions.append(ok / max(1, len(vals)-1))
    return sum(fractions) / len(fractions)


# === block: score_2 (check id='damage_trend_S') ===
def score_2(artifact, step, ctx):
        rows = [r for r in artifact if abs(float(r['f'])-0.0654) < 1e-9]
        if len(rows) < 3:
            return 0.0
        rows.sort(key=lambda r: float(r['S']))
        # D33_M decreasing
        vals33 = [float(r['D33_M']) for r in rows]
        decreasing_ok = sum(1 for i in range(len(vals33)-1) if vals33[i+1] <= vals33[i] + 1e-8)
        score_33 = decreasing_ok / max(1, len(vals33)-1)
        # D11_M increasing
        vals11 = [float(r['D11_M']) for r in rows]
        increasing_ok = sum(1 for i in range(len(vals11)-1) if vals11[i+1] >= vals11[i] - 1e-8)
        score_11 = increasing_ok / max(1, len(vals11)-1)
        # D11_E and D33_E nearly constant
        import math
        const_scores = []
        for k in ['D11_E','D33_E']:
            v = [float(r[k]) for r in rows]
            mu = sum(v)/len(v)
            if mu == 0:
                cv = 0
            else:
                cv = math.sqrt(sum((x-mu)**2 for x in v)/len(v)) / abs(mu)
            if cv <= 0.1:
                const_scores.append(1.0)
            elif cv <= 0.3:
                const_scores.append( max(0.0, 1.0 - (cv-0.1)/0.2) )
            else:
                const_scores.append(0.0)
        const_score = sum(const_scores)/len(const_scores) if const_scores else 0.0
        return 0.4*score_11 + 0.4*score_33 + 0.2*const_score


# === block: score_3 (check id='damage_isotropy') ===
def score_3(artifact, step, ctx):
    rows = [r for r in artifact if abs(float(r['S'])-1.0) < 1e-6]
    if not rows:
        return 0.0
    diffs = []
    for r in rows:
        d11 = float(r['D11_M'])
        d33 = float(r['D33_M'])
        if d11 == 0 and d33 == 0:
            diffs.append(0.0)
        else:
            denom = (abs(d11)+abs(d33))/2.0
            if denom == 0:
                diffs.append(0.0)
            else:
                diffs.append(abs(d11-d33)/denom)
    max_diff = max(diffs)
    if max_diff <= 0.1:
        return 1.0
    elif max_diff <= 0.3:
        return max(0.0, 1.0 - (max_diff-0.1)/0.2)
    else:
        return 0.0


# === block: score_4 (check id='piezo_existence') ===
def score_4(artifact, step, ctx):
    cols = {'f','S','e31','e33','e15'}
    if not artifact or not isinstance(artifact, list) or not all(k in artifact[0].keys() for k in cols):
        return 0.0
    return 1.0


# === block: score_5 (check id='piezo_trend_f') ===
def score_5(artifact, step, ctx):
    rows = [r for r in artifact if abs(float(r['S'])-1.0) < 1e-6]
    if len(rows) < 3:
        return 0.0
    rows.sort(key=lambda r: float(r['f']))
    trends = {
        'e31': 'increasing',
        'e33': 'decreasing',
        'e15': 'decreasing'
    }
    scores = []
    for key, direction in trends.items():
        vals = [float(r[key]) for r in rows]
        if direction == 'decreasing':
            ok = sum(1 for i in range(len(vals)-1) if vals[i+1] <= vals[i] + 1e-8)
        else:
            ok = sum(1 for i in range(len(vals)-1) if vals[i+1] >= vals[i] - 1e-8)
        scores.append(ok / max(1, len(vals)-1))
    return sum(scores) / len(scores)


# === block: score_6 (check id='piezo_trend_S') ===
def score_6(artifact, step, ctx):
    rows = [r for r in artifact if abs(float(r['f'])-0.0654) < 1e-9]
    if len(rows) < 3:
        return 0.0
    rows.sort(key=lambda r: float(r['S']))
    # e33 and e15 decreasing, e31 fairly constant
    e33_vals = [float(r['e33']) for r in rows]
    e15_vals = [float(r['e15']) for r in rows]
    e31_vals = [float(r['e31']) for r in rows]
    decreasing_score = 0
    if len(e33_vals) > 1:
        ok33 = sum(1 for i in range(len(e33_vals)-1) if e33_vals[i+1] <= e33_vals[i] + 1e-8)
        decreasing_score += ok33 / (len(e33_vals)-1)
    if len(e15_vals) > 1:
        ok15 = sum(1 for i in range(len(e15_vals)-1) if e15_vals[i+1] <= e15_vals[i] + 1e-8)
        decreasing_score += ok15 / (len(e15_vals)-1)
    decreasing_score /= 2.0 if 2 > 0 else 0.0
    # e31 constancy
    if len(e31_vals) > 1:
        mu = sum(e31_vals)/len(e31_vals)
        std = (sum((x-mu)**2 for x in e31_vals)/len(e31_vals))**0.5
        if mu == 0:
            cv = 0
        else:
            cv = abs(std/mu)
        const_score = 1.0 if cv <= 0.15 else max(0.0, 1.0 - cv)
    else:
        const_score = 0.0
    return 0.5*decreasing_score + 0.5*const_score


_SCORERS = {
    'damage_existence': score_0,
    'damage_monotonic_f': score_1,
    'damage_trend_S': score_2,
    'damage_isotropy': score_3,
    'piezo_existence': score_4,
    'piezo_trend_f': score_5,
    'piezo_trend_S': score_6,
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
