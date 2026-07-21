import os
import json
import csv

# === author imports / helpers ===
import csv
import re
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
    return {}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    global outputs_dir
    outputs_dir = '/app/outputs'

    gold_zt = step['gold_peak_zt']
    gold_filler = step['gold_peak_filler']
    tol_zt = step['tolerance_zt']
    tol_filler = step['tolerance_filler']

    # artifact is a list of dicts (already parsed by the harness).
    # Iterate directly instead of wrapping with csv.DictReader.
    if not artifact:
        return 0.0
    max_zt = -1.0
    max_filler = None
    for row in artifact:
        zt = float(row['ZT'])
        if zt > max_zt:
            max_zt = zt
            max_filler = float(row['filler_vol_percent'])
    if max_filler is None:
        return 0.0

    diff_zt = abs(max_zt - gold_zt)
    if diff_zt <= tol_zt:
        zt_score = 1.0
    elif diff_zt <= 2 * tol_zt:
        zt_score = 0.8
    elif diff_zt <= 4 * tol_zt:
        zt_score = 0.5
    else:
        zt_score = 0.0

    if abs(max_filler - gold_filler) <= tol_filler:
        filler_score = 1.0
    else:
        filler_score = 0.0

    return 0.65 * zt_score + 0.35 * filler_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    # Read the shifted CSV to get the reference maximum ZT
    shifted_path = os.path.join(outputs_dir, 'step_01_zt_vs_filler.csv')
    if not os.path.exists(shifted_path):
        return 0.0
    with open(shifted_path, newline='') as f:
        shifted_rows = list(csv.DictReader(f))
    if not shifted_rows:
        return 0.0
    max_zt_shifted = max(float(r['ZT']) for r in shifted_rows)

    # artifact is a list of dicts (no-shift CSV)
    no_shift_rows = artifact  # already parsed by the harness
    if not no_shift_rows:
        return 0.0
    max_zt_noshift = max(float(r['ZT']) for r in no_shift_rows)

    if max_zt_shifted <= 0:
        return 0.0
    ratio = max_zt_noshift / max_zt_shifted
    threshold = step['max_ratio_threshold']

    if ratio <= threshold:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    # Expected CSV maxima (same extraction as step_01 and step_02)
    shifted_path = os.path.join(outputs_dir, 'step_01_zt_vs_filler.csv')
    noshift_path = os.path.join(outputs_dir, 'step_02_zt_noshift.csv')
    if not os.path.exists(shifted_path) or not os.path.exists(noshift_path):
        return 0.0
    with open(shifted_path, newline='') as f:
        srows = list(csv.DictReader(f))
    max_zt_shifted = max(float(r['ZT']) for r in srows)
    max_filler_shifted = None
    for r in srows:
        if abs(float(r['ZT']) - max_zt_shifted) < 1e-12:
            max_filler_shifted = float(r['filler_vol_percent'])
            break
    with open(noshift_path, newline='') as f:
        nrows = list(csv.DictReader(f))
    max_zt_noshift = max(float(r['ZT']) for r in nrows)
    max_filler_noshift = None
    for r in nrows:
        if abs(float(r['ZT']) - max_zt_noshift) < 1e-12:
            max_filler_noshift = float(r['filler_vol_percent'])
            break

    text = artifact  # artifact is the raw string for txt format
    lines = text.strip().splitlines()
    if len(lines) < 2:
        return 0.0

    # Parse two lines
    def parse_line(line):
        # Expected: "Peak ZT (<case>): <value> at <filler_vol_percent>"
        m = re.match(r'Peak ZT \(([^)]+)\):\s*([-+]?[\d.eE]+)\s*at\s*([-+]?[\d.eE]+)', line)
        if not m:
            return None, None, None
        case = m.group(1).strip()
        zt = float(m.group(2))
        filler = float(m.group(3))
        return case, zt, filler

    case1, zt1, filler1 = parse_line(lines[0])
    case2, zt2, filler2 = parse_line(lines[1])
    if None in (case1, case2):
        return 0.0

    # Check consistency with CSV maxima
    ok1 = (case1.lower() == 'shifted' and abs(zt1 - max_zt_shifted) <= step['tolerance_zt'] and abs(filler1 - max_filler_shifted) <= step['tolerance_filler'])
    ok2 = (case2.lower() == 'no shift' and abs(zt2 - max_zt_noshift) <= step['tolerance_zt'] and abs(filler2 - max_filler_noshift) <= step['tolerance_filler'])

    return 1.0 if (ok1 and ok2) else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
