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


# === block: score_0 (check id='ethanol_ordering') ===
def score_0(artifact, step, ctx):
    cond = step.get('conditions', {})
    temps = cond['temperatures']
    order = cond['zif_order']
    tol = cond.get('tolerance', 1e-6)
    data = {}
    for row in artifact:
        t = float(row['Temperature (K)'])
        if t not in temps:
            continue
        p = float(row['Pressure (kPa)'])
        zif = row['ZIF']
        load = float(row['Loading (mmol/g)'])
        data.setdefault(t, {}).setdefault(p, {})[zif] = load
    temp_scores = []
    for t in temps:
        if t not in data:
            continue
        press_data = data[t]
        valid_points = [(p, loads) for p, loads in press_data.items() if all(z in loads for z in order)]
        if not valid_points:
            continue
        correct = sum(1 for p, loads in valid_points
                      if all(loads[order[i]] > loads[order[i+1]] + tol for i in range(len(order)-1)))
        temp_scores.append(correct / len(valid_points))
    return sum(temp_scores) / len(temp_scores) if temp_scores else 0.0


# === block: score_1 (check id='water_hydrophobicity') ===
def score_1(artifact, step, ctx):
    cond = step['conditions']
    low_zif = cond['zif_low']
    high_zif = cond['zif_high']
    th_low = cond['threshold_low']
    th_high = cond['threshold_high']
    data_low = {z: [] for z in low_zif}
    data_high = {z: [] for z in high_zif}
    max_p = 0.0
    for row in artifact:
        zif = row['ZIF']
        load = float(row['Loading (mmol/g)'])
        p = float(row['Pressure (kPa)'])
        max_p = max(max_p, p)
        if zif in data_low:
            data_low[zif].append(load)
        elif zif in data_high:
            data_high[zif].append(load)
    # low: all loads <= th_low
    low_score = sum(1 for z in low_zif if all(l <= th_low for l in data_low[z])) / len(low_zif) if low_zif else 1.0
    # high: at max pressure, load > th_high
    high_score = 0.0
    for z in high_zif:
        best = -1.0
        for row in artifact:
            if row['ZIF'] == z and abs(float(row['Pressure (kPa)']) - max_p) < 1e-6:
                load = float(row['Loading (mmol/g)'])
                best = max(best, load)
        if best > th_high:
            high_score += 1
    high_score = high_score / len(high_zif) if high_zif else 1.0
    return 0.5 * low_score + 0.5 * high_score


# === block: score_2 (check id='mixture_selectivity') ===
def score_2(artifact, step, ctx):
    cond = step['conditions']
    target_p = cond['pressure']
    required_temps = cond.get('temperature_list', [323, 373])
    tol_rel = cond['closeness_tol']
    pair = cond['closeness_pair']
    # collect data at target pressure (within 0.05 kPa)
    data = {}
    for row in artifact:
        p = float(row['Pressure (kPa)'])
        if abs(p - target_p) > 0.05:
            continue
        t = float(row['Temperature (K)'])
        zif = row['ZIF']
        sel = float(row['Selectivity'])
        data.setdefault(t, {})[zif] = sel
    scores = 0
    for t in required_temps:
        if t not in data:
            continue
        temp_data = data[t]
        if not all(z in temp_data for z in ['ZIF-1','ZIF-3','ZIF-7','ZIF-9']):
            continue
        s1 = temp_data['ZIF-1']
        s3 = temp_data['ZIF-3']
        s7 = temp_data['ZIF-7']
        s9 = temp_data['ZIF-9']
        if s1 <= s3:
            continue
        if s3 <= s7 or s3 <= s9:
            continue
        mx = max(s7, s9)
        if mx == 0:
            close = abs(s7 - s9) < 1e-6
        else:
            close = abs(s7 - s9) / mx <= tol_rel
        if not close:
            continue
        scores += 1
    return scores / len(required_temps) if required_temps else 0.0


_SCORERS = {
    'ethanol_ordering': score_0,
    'water_hydrophobicity': score_1,
    'mixture_selectivity': score_2,
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
