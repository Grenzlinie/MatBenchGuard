import os
import json
import csv

# === author imports / helpers ===
import re
import math


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
    ctx = {}
    ctx['conversion'] = float(spec.get('conversion_constant_G', 1455.0))
    ctx['fb_indices'] = [int(i) for i in spec.get('defect_atoms', {}).get('fb_indices', [])]
    ctx['db_indices'] = [int(i) for i in spec.get('defect_atoms', {}).get('db_indices', [])]
    return ctx


# === block: score_0 (check id='step_dos_w3') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    energies = []
    dos_vals = []
    for row in artifact:
        try:
            e = float(row['energy'])
            d = float(row['dos'])
            energies.append(e)
            dos_vals.append(d)
        except ValueError:
            continue
    if len(energies) == 0:
        return 0.0
    max_dos = max(dos_vals)
    if max_dos == 0:
        return 0.0
    threshold = 0.01 * max_dos
    pairs = sorted(zip(energies, dos_vals))
    gap_width = 0.0
    in_gap = False
    start = None
    for e, d in pairs:
        if d < threshold:
            if not in_gap:
                start = e
                in_gap = True
        else:
            if in_gap:
                gap_width = max(gap_width, e - start)
                in_gap = False
    if in_gap:
        gap_width = max(gap_width, pairs[-1][0] - start)
    if gap_width >= 0.5:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_wavefunction_data') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    conv = ctx.get('conversion', 1455.0)
    consistency_hits = 0
    total_rows = 0
    fb_deltas = []   # atoms NOT coordination 3 (includes floating‑bond neighbours)
    db_deltas = []   # atoms with coordination 3 (dangling‑bond centres)
    for row in artifact:
        try:
            idx = int(row['atom_index'])
            coord = int(row['coordination'])
            alpha_sq = float(row['alpha_squared'])
            eta_sq = float(row['eta_squared'])
            delta_agent = float(row['delta_H'])
            total_rows += 1
            delta_recomp = conv * alpha_sq * eta_sq
            if abs(delta_recomp - delta_agent) < max(0.05 * abs(delta_agent), 1e-9) + 1e-12:
                consistency_hits += 1
            if coord == 3:
                db_deltas.append(delta_recomp)
            else:
                fb_deltas.append(delta_recomp)
        except (ValueError, KeyError):
            continue
    if total_rows == 0:
        return 0.0
    score_consistency = consistency_hits / total_rows
    score_trend = 0.0
    score_fb_thresh = 0.0
    score_db_thresh = 0.0
    if fb_deltas and db_deltas:
        fb_max = max(fb_deltas)
        db_max = max(db_deltas)
        if fb_max > db_max:
            score_trend = 1.0
        if fb_max >= 25.0:
            score_fb_thresh = 1.0
        if db_max <= 35.0:
            score_db_thresh = 1.0
    elif fb_deltas:
        fb_max = max(fb_deltas)
        if fb_max >= 25.0:
            score_fb_thresh = 1.0
    total_score = 0.4 * score_consistency + 0.2 * score_trend + 0.2 * score_fb_thresh + 0.2 * score_db_thresh
    return max(0.0, min(1.0, total_score))


# === block: score_2 (check id='step_hyperfine_summary') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, str):
        return 0.0
    text = artifact
    # extract floating-bond range: look for pattern like "25 to 67", "25-67", with optional units
    pattern = r'(?i)(?:floating|five.c?oord).*?\b(\d+(?:\.\d+)?)\s*(?:-|to)\s*(\d+(?:\.\d+)?)\s*G'
    match = re.search(pattern, text)
    range_found = 0.0
    lower_ok = 0.0
    upper_ok = 0.0
    if match:
        range_found = 1.0
        lo = float(match.group(1))
        hi = float(match.group(2))
        if 0.0 <= lo <= 35.0:
            lower_ok = 1.0
        if 40.0 <= hi <= 100.0:
            upper_ok = 1.0
    # check that dangling bonds are reported as smaller
    smaller_mentioned = 0.0
    if re.search(r'(?i)(dangling|three.c?oord).*?(small(er)?|less|much lower|minor)', text):
        smaller_mentioned = 1.0
    # combine
    score = 0.3 * range_found + 0.3 * lower_ok + 0.3 * upper_ok + 0.1 * smaller_mentioned
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_dos_w3': score_0,
    'step_wavefunction_data': score_1,
    'step_hyperfine_summary': score_2,
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
