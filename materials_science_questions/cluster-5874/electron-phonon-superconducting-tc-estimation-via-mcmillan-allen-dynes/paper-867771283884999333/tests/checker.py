import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os


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
    spec = globals().get('spec', None)
    if spec is None:
        # grading_spec.json may be missing or null; return safe defaults
        ctx = {}
        ctx['gold_table'] = []
        ctx['Tc_rel'] = 0.0
        ctx['dM_abs'] = 0.0
        ctx['aM_abs'] = 0.0
        ctx['diff_abs'] = 0.0
        return ctx
    ctx = {}
    ctx['gold_table'] = spec.get('gold_table', [])
    tols = spec.get('tolerances', {})
    ctx['Tc_rel'] = tols.get('Tc_rel', 0.02)
    ctx['dM_abs'] = tols.get('dM_abs', 2.0)
    ctx['aM_abs'] = tols.get('aM_abs', 2.0)
    ctx['diff_abs'] = tols.get('diff_abs', 4.0)
    return ctx


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) != 9:
        return 0.0
    required = {'Pressure','Tc','dM','aM','dM_minus_aM'}
    if not required.issubset(set(rows[0].keys())):
        return 0.0
    # Check no empty values
    for r in rows:
        for col in required:
            if r.get(col) is None or str(r.get(col)).strip() == '':
                return 0.0
    return 1.0


# === block: score_1 (check id='values_check') ===
def score_1(artifact, step, ctx):
    gold = [
        {"Pressure": 155, "Tc": 203.0, "dM": 121.7, "aM": 126.8, "dM_minus_aM": 5.1},
        {"Pressure": 160, "Tc": 197.4, "dM": 113.9, "aM": 128.7, "dM_minus_aM": 14.8},
        {"Pressure": 165, "Tc": 191.388, "dM": 115.5, "aM": 132.1, "dM_minus_aM": 16.6},
        {"Pressure": 170, "Tc": 186.263, "dM": 112.8, "aM": 132.0, "dM_minus_aM": 19.2},
        {"Pressure": 175, "Tc": 181.438, "dM": 110.2, "aM": 134.3, "dM_minus_aM": 24.1},
        {"Pressure": 185, "Tc": 169.3, "dM": 103.6, "aM": 139.5, "dM_minus_aM": 35.9},
        {"Pressure": 195, "Tc": 158.67, "dM": 98.0, "aM": 147.1, "dM_minus_aM": 49.1},
        {"Pressure": 205, "Tc": 147.305, "dM": 91.8, "aM": 152.7, "dM_minus_aM": 60.9},
        {"Pressure": 215, "Tc": 138.258, "dM": 86.9, "aM": 166.1, "dM_minus_aM": 79.2},
    ]
    rel_tol = 0.02
    abs_dM = 2.0
    abs_aM = 2.0
    abs_diff = 4.0
    rows = artifact
    if not rows or len(rows) < 9:
        return 0.0
    agent_lookup = {}
    for r in rows:
        try:
            p = float(r['Pressure'])
        except:
            continue
        agent_lookup[p] = r
    fields = [('Tc', rel_tol, True), ('dM', abs_dM, False), ('aM', abs_aM, False), ('dM_minus_aM', abs_diff, False)]
    total_cells = len(gold) * len(fields)
    ok = 0
    for g in gold:
        p = g['Pressure']
        ar = agent_lookup.get(p)
        if ar is None:
            continue
        for fld, tol, is_rel in fields:
            try:
                val = float(ar[fld])
                gold_val = float(g[fld])
            except:
                continue
            if is_rel:
                if abs(val - gold_val) <= tol * abs(gold_val):
                    ok += 1
            else:
                if abs(val - gold_val) <= tol:
                    ok += 1
    return ok / total_cells if total_cells > 0 else 0.0


# === block: score_2 (check id='trends_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0
    # Sort by Pressure ascending
    sorted_rows = sorted(rows, key=lambda x: float(x.get('Pressure', 0)))
    # Extract values
    pres = []
    Tc = []
    diff = []
    for r in sorted_rows:
        try:
            pres.append(float(r['Pressure']))
            Tc.append(float(r['Tc']))
            diff.append(float(r['dM_minus_aM']))
        except:
            return 0.0
    if len(pres) < 2:
        return 0.0

    # Check Tc strictly decreasing (or non-increasing)
    violations_tc = sum(1 for i in range(1,len(Tc)) if Tc[i] > Tc[i-1])
    # Check diff strictly increasing (or non-decreasing)
    violations_diff = sum(1 for i in range(1,len(diff)) if diff[i] < diff[i-1])
    total_pairs = len(pres)-1
    # Score as fraction of correct sequential pairs
    correct_tc = total_pairs - violations_tc
    correct_diff = total_pairs - violations_diff
    avg_correct = (correct_tc + correct_diff) / (2 * total_pairs) if total_pairs > 0 else 0.0
    return max(0.0, min(1.0, avg_correct))


_SCORERS = {
    'shape_check': score_0,
    'values_check': score_1,
    'trends_check': score_2,
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
