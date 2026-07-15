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
    bonds = {}
    tol_full = 0.005
    tol_partial = 0.01
    freq_gold = None
    intens_gold = None
    sym_gold = None
    tol_freq = 15
    intens_thresh = 1000
    for step in spec.get('steps', []):
        if step['id'] == 'step_01_bond_check':
            bonds = step['gold']['bonds']
            tol_full = step['tolerance_abs_full']
            tol_partial = step['tolerance_abs_partial']
        elif step['id'] == 'step_02_freq_check':
            g = step['gold']
            freq_gold = g['frequencies']
            intens_gold = g['intensities']
            sym_gold = g['symmetries']
            tol_freq = step['tolerance_freq_cm1']
            if 'intensity_threshold' in step:
                intens_thresh = step['intensity_threshold']
    return {
        'bonds': bonds,
        'tol_bond_full': tol_full,
        'tol_bond_partial': tol_partial,
        'freq_gold': freq_gold,
        'intens_gold': intens_gold,
        'sym_gold': sym_gold,
        'tol_freq': tol_freq,
        'intensity_threshold': intens_thresh
    }


# === block: score_0 (check id='step_01_bond_check') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dicts from CSV; expected columns: bond, value_angstrom
    agent_bonds = {}
    for row in artifact:
        agent_bonds[row['bond']] = float(row['value_angstrom'])
    max_diff = 0.0
    for name, gold_val in ctx['bonds'].items():
        if name not in agent_bonds:
            return 0.0
        diff = abs(agent_bonds[name] - gold_val)
        if diff > max_diff:
            max_diff = diff
    if max_diff <= ctx['tol_bond_full']:
        return 1.0
    elif max_diff <= ctx['tol_bond_partial']:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='step_02_freq_check') ===
def score_1(artifact, step, ctx):
    # artifact is a list of dicts; expected columns: mode, frequency_cm1, intensity_kmol, symmetry
    if len(artifact) != 7:
        return 0.0
    # build lists indexed by mode number (1..7)
    mode_map = {}
    for row in artifact:
        m = int(row['mode'])
        if not (1 <= m <= 7):
            return 0.0
        mode_map[m] = row
    freq_vals = []
    inten_vals = []
    for i in range(1, 8):
        if i not in mode_map:
            return 0.0
        row = mode_map[i]
        freq_vals.append(float(row['frequency_cm1']))
        inten_vals.append(float(row['intensity_kmol']))
    # frequency tolerance check
    passes = 0
    for i in range(7):
        if abs(freq_vals[i] - ctx['freq_gold'][i]) <= ctx['tol_freq']:
            passes += 1
    freq_ratio = passes / 7.0
    # ordering check: strictly descending
    ordering_pass = 1.0 if all(freq_vals[i] > freq_vals[i+1] for i in range(6)) else 0.0
    # intensity check: the mode with highest frequency (mode 1) must have intensity > threshold and be the largest
    intensity_pass = 0.0
    if inten_vals[0] > ctx['intensity_threshold'] and inten_vals[0] >= max(inten_vals):
        intensity_pass = 1.0
    combined = 0.7 * freq_ratio + 0.15 * ordering_pass + 0.15 * intensity_pass
    return combined


_SCORERS = {
    'step_01_bond_check': score_0,
    'step_02_freq_check': score_1,
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
