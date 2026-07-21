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


# === block: score_0 (check id='cluster_peak') ===
def score_0(artifact, step, ctx):
    def compute_peak_scores(artifact):
        groups = {}
        for row in artifact:
            key = (int(float(row['Temperature'])), int(float(row['Dose'])), row['Species'].strip().lower())
            size = int(float(row['ClusterSize']))
            conc = float(row['Concentration'])
            if key not in groups:
                groups[key] = {'max_conc': -1.0, 'max_size': None}
            if conc > groups[key]['max_conc']:
                groups[key]['max_conc'] = conc
                groups[key]['max_size'] = size
        total = 0
        correct = 0
        for (T, dose, species), data in groups.items():
            if species == 'interstitial':
                total += 1
                if data['max_size'] == 10:
                    correct += 1
        if total == 0:
            return 0.0
        return correct / total

    return compute_peak_scores(artifact)


# === block: score_1 (check id='cluster_tail_ordering') ===
def score_1(artifact, step, ctx):
    def tail_ratio(group_rows, threshold):
        tail = 0.0
        total = 0.0
        for row in group_rows:
            size = int(float(row['ClusterSize']))
            conc = float(row['Concentration'])
            if size >= threshold:
                tail += conc
            total += conc
        if total == 0:
            return 0.0
        return tail / total

    T_threshold = step['params']['tail_threshold_size']
    doses = step['params']['check_doses']
    temps = step['params']['check_temperatures']
    # Build lookup: (T, dose, species) -> list of rows
    data = {}
    for row in artifact:
        T = int(float(row['Temperature']))
        dose = int(float(row['Dose']))
        species = row['Species'].strip().lower()
        key = (T, dose, species)
        data.setdefault(key, []).append(row)
    checks = 0
    passed = 0
    for T in temps:
        for d in doses:
            rows_i = data.get((T, d, 'interstitial'), [])
            rows_v = data.get((T, d, 'vacancy'), [])
            if not rows_i or not rows_v:
                continue
            ri = tail_ratio(rows_i, T_threshold)
            rv = tail_ratio(rows_v, T_threshold)
            checks += 1
            if T == 600:
                if ri > rv:
                    passed += 1
            else:  # T == 660
                if rv > ri:
                    passed += 1
    if checks == 0:
        return 0.0
    return passed / checks


# === block: score_2 (check id='diffusion_ordering') ===
def score_2(artifact, step, ctx):
    def check_row(row, expect_Di_gt_Dv):
        D_total = float(row['D_total'])
        D_v = float(row['D_vacancy'])
        D_i = float(row['D_interstitial'])
        minD = step['params']['min_D']
        maxD = step['params']['max_D']
        # magnitude plausibility
        mag_ok = (D_total >= minD) and (D_total <= maxD) and (D_v >= 0) and (D_i >= 0)
        if expect_Di_gt_Dv:
            order_ok = D_i > D_v
        else:
            order_ok = D_v > D_i
        return 1.0 if (mag_ok and order_ok) else 0.0

    temp_low = step['params']['temp_low']
    temp_high = step['params']['temp_high']
    dose = step['params']['dose']
    low_row = None
    high_row = None
    for row in artifact:
        T = int(float(row['Temperature']))
        D = int(float(row['Dose']))
        if D != dose:
            continue
        if T == temp_low:
            low_row = row
        elif T == temp_high:
            high_row = row
    score = 0.0
    if low_row:
        score += 0.5 * check_row(low_row, True)   # at 500K expect D_i > D_v
    if high_row:
        score += 0.5 * check_row(high_row, False)  # at 660K expect D_v > D_i
    return score


_SCORERS = {
    'cluster_peak': score_0,
    'cluster_tail_ordering': score_1,
    'diffusion_ordering': score_2,
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
