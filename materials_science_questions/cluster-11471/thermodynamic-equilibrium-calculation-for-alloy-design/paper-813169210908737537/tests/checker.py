import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    required_columns = ['Temperature','Phase','Cr_wt','Mo_wt','N_wt','PREN']
    if not rows or not all(col in rows[0] for col in required_columns):
        return 0.0
    if len(rows) != 8:
        return 0.0
    expected_temps = {1050,1100,1150,1200}
    found_temps = set()
    phase_set = {'ferrite','austenite'}
    for r in rows:
        t = int(r['Temperature'])
        ph = r['Phase'].strip().lower()
        if ph not in phase_set or t not in expected_temps:
            return 0.0
        found_temps.add(t)
    if found_temps != expected_temps:
        return 0.0
    for t in expected_temps:
        phases_at_t = [r['Phase'].strip().lower() for r in rows if int(r['Temperature']) == t]
        if sorted(phases_at_t) != ['austenite','ferrite']:
            return 0.0
    return 1.0


# === block: score_1 (check id='ferrite_monotonic') ===
def score_1(artifact, step, ctx):
    ferr = [r for r in artifact if r['Phase'].strip().lower() == 'ferrite']
    if len(ferr) != 4:
        return 0.0
    ferr.sort(key=lambda x: int(x['Temperature']))
    v = [float(r['PREN']) for r in ferr]
    if all(v[i] > v[i+1] for i in range(len(v)-1)):
        return 1.0
    return 0.0


# === block: score_2 (check id='austenite_monotonic') ===
def score_2(artifact, step, ctx):
    aust = [r for r in artifact if r['Phase'].strip().lower() == 'austenite']
    if len(aust) != 4:
        return 0.0
    aust.sort(key=lambda x: int(x['Temperature']))
    v = [float(r['PREN']) for r in aust]
    if all(v[i] < v[i+1] for i in range(len(v)-1)):
        return 1.0
    return 0.0


# === block: score_3 (check id='crossing_check') ===
def score_3(artifact, step, ctx):
    def get_pren(temp, phase):
        for r in artifact:
            if int(r['Temperature']) == temp and r['Phase'].strip().lower() == phase.lower():
                return float(r['PREN'])
        return None
    ferr_1050 = get_pren(1050, 'ferrite')
    aust_1050 = get_pren(1050, 'austenite')
    ferr_1200 = get_pren(1200, 'ferrite')
    aust_1200 = get_pren(1200, 'austenite')
    if None in (ferr_1050, aust_1050, ferr_1200, aust_1200):
        return 0.0
    cond1 = ferr_1050 > aust_1050
    cond2 = ferr_1200 < aust_1200
    return 1.0 if cond1 and cond2 else 0.0


# === block: score_4 (check id='min_diff_check') ===
def score_4(artifact, step, ctx):
    temps = [1050,1100,1150,1200]
    diffs = {}
    for t in temps:
        f = None; a = None
        for r in artifact:
            if int(r['Temperature']) == t:
                ph = r['Phase'].strip().lower()
                if ph == 'ferrite': f = float(r['PREN'])
                if ph == 'austenite': a = float(r['PREN'])
        if f is None or a is None:
            return 0.0
        diffs[t] = abs(f - a)
    min_val = min(diffs.values())
    if math.isclose(diffs[1150], min_val, rel_tol=1e-9):
        return 1.0
    return 0.0


_SCORERS = {
    'shape_check': score_0,
    'ferrite_monotonic': score_1,
    'austenite_monotonic': score_2,
    'crossing_check': score_3,
    'min_diff_check': score_4,
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
