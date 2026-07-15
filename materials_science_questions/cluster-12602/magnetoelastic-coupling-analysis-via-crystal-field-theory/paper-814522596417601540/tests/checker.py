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


# === block: score_0 (check id='step_results_table') ===
def score_0(artifact, step, ctx):
    artifact_path = '/app/outputs/results_table.csv'
    import csv, os, math
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    data = {}
    for r in rows:
        try:
            x = float(r['x'])
            elp = float(r['ELP'])
            mag = float(r['magnetization'])
            data[x] = (elp, mag)
        except:
            pass

    params = step.get('params', {})
    gold = params.get('gold_values', {})
    gold_x = gold.get('x', [])
    gold_ELP = gold.get('ELP', [])
    gold_mag = gold.get('magnetization', [])
    if len(gold_x) != len(gold_ELP) or len(gold_x) != len(gold_mag):
        return 0.0

    errors = []
    for i, x in enumerate(gold_x):
        if x not in data:
            return 0.0
        agent_elp, agent_mag = data[x]
        errors.append((agent_elp - gold_ELP[i], agent_mag - gold_mag[i]))

    elp_diffs = [e[0] for e in errors]
    mag_diffs = [e[1] for e in errors]
    if len(elp_diffs) == 0:
        return 0.0
    rmsd_ELP = math.sqrt(sum(d*d for d in elp_diffs)/len(elp_diffs))
    rmsd_mag = math.sqrt(sum(d*d for d in mag_diffs)/len(mag_diffs))

    tol_ELP = params.get('ELP_tolerance_rmsd', 0.03)
    tol_mag = params.get('mag_tolerance_rmsd', 0.5)

    def rmsd_score(val, tol):
        if val <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (val - tol) / tol)

    score_ELP = rmsd_score(rmsd_ELP, tol_ELP)
    score_mag = rmsd_score(rmsd_mag, tol_mag)

    jump_params = params.get('jump_conditions', {})
    x_before = jump_params.get('x_before')
    x_after = jump_params.get('x_after')
    min_ELP_diff = jump_params.get('min_ELP_diff', 0.015)
    min_mag_diff = jump_params.get('min_mag_diff', 0.5)
    if x_before is not None and x_after is not None and x_before in data and x_after in data:
        elp_jump = data[x_after][0] - data[x_before][0]
        mag_jump = data[x_after][1] - data[x_before][1]
        jump_ok = (elp_jump >= min_ELP_diff) and (mag_jump >= min_mag_diff)
        jump_score = 1.0 if jump_ok else 0.0
    else:
        jump_score = 0.0

    combined = 0.5*score_ELP + 0.5*score_mag
    return 0.8 * combined + 0.2 * jump_score


# === block: score_1 (check id='step_dos_critical') ===
def score_1(artifact, step, ctx):
    artifact_path = '/app/outputs/dos_critical.json'
    import json, os, math
    with open(artifact_path) as f:
        dos_data = json.load(f)

    params = step.get('params', {})
    energy_window = params.get('energy_window', [-1.0, 0.5])
    expected_pattern = params.get('expected_pattern', {})
    check_columns = params.get('check_columns', ['Co_spin_down', 'Fe4b_spin_down'])
    split_threshold = params.get('split_threshold_peaks', 2)
    merged_max = params.get('merged_max_peaks', 1)

    def find_peaks(energies, doss):
        peaks = []
        n = len(energies)
        for i in range(1, n-1):
            if energies[i] < energy_window[0] or energies[i] > energy_window[1]:
                continue
            if doss[i] > doss[i-1] and doss[i] > doss[i+1]:
                peaks.append((energies[i], doss[i]))
        return peaks

    total_checks = 0
    passed = 0
    for case_key, expected in expected_pattern.items():
        if case_key not in dos_data:
            continue
        case_obj = dos_data[case_key]
        for col in check_columns:
            if col not in case_obj:
                continue
            data_pts = case_obj[col]
            if not data_pts:
                continue
            energies = [p[0] for p in data_pts]
            doss = [p[1] for p in data_pts]
            peaks = find_peaks(energies, doss)
            n_peaks = len(peaks)
            if expected == 'split':
                ok = (n_peaks >= split_threshold)
            else:
                ok = (n_peaks <= merged_max)
            total_checks += 1
            if ok:
                passed += 1

    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'step_results_table': score_0,
    'step_dos_critical': score_1,
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
