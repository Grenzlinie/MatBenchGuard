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
    return {'gold_kappa': {'[100]': 10.68, '[010]': 20.78, '[001]': 12.61}}


# === block: score_0 (check id='phonon_check') ===
def score_0(artifact, step, ctx):
    import json
    artifact_path = '/app/outputs/phonon_dispersion.json'
    with open(artifact_path) as f:
        data = json.load(f)
    score = 0.0
    keys = ['Gamma-X', 'Gamma-Y', 'Gamma-Z']
    if all(k in data for k in keys):
        score += 0.2
        all_non_neg = True
        max_freq = 0
        tot_modes = 0
        acoustic_ok = True
        for key in keys:
            arr = data[key]
            if not isinstance(arr, list) or len(arr) == 0:
                score -= 0.1
                continue
            tot_modes += len(arr)
            for f in arr:
                if not isinstance(f, (int, float)) or f < 0:
                    all_non_neg = False
                if f > max_freq:
                    max_freq = f
            # check that first 3 entries (acoustic) are small
            if len(arr) >= 3:
                if any(abs(arr[i]) > 0.5 for i in range(3)):
                    acoustic_ok = False
            else:
                acoustic_ok = False
        if all_non_neg:
            score += 0.2
        if max_freq <= 30:
            score += 0.2
        else:
            score += 0.1 if max_freq <= 35 else 0
        if tot_modes >= 90:  # at least 30 modes per path
            score += 0.2
        else:
            score += 0.1 if tot_modes >= 30 else 0
        if acoustic_ok:
            score += 0.2
        else:
            # partial if only some paths ok
            pass  # already used boolean; could refine but keeping simple
    else:
        score = 0.0
    return min(1.0, score)


# === block: score_1 (check id='thermal_kappa') ===
def score_1(artifact, step, ctx):
    import json
    artifact_path = '/app/outputs/thermal_conductivity.json'
    with open(artifact_path) as f:
        data = json.load(f)
    gold = {'[100]': 10.68, '[010]': 20.78, '[001]': 12.61}
    ordering = ['[100]', '[001]', '[010]']  # increasing order
    dirs = ['[100]', '[010]', '[001]']
    values = {}
    failed = False
    for d in dirs:
        if d not in data or not isinstance(data[d], (int, float)):
            return 0.0
        values[d] = float(data[d])
    rel_err = {d: abs(values[d] - gold[d]) / gold[d] for d in dirs}
    tol = 0.20
    within_tol = sum(1 for d in dirs if rel_err[d] <= tol)
    weight_within = 0.7
    score_dir = (within_tol / 3.0) * weight_within
    # ordering check
    ordering_score = 0.0
    if values['[010]'] > values['[001]'] > values['[100]']:
        ordering_score = 0.3
    score = score_dir + ordering_score
    return score


# === block: score_2 (check id='accumulated_kappa') ===
def score_2(artifact, step, ctx):
    import csv, math
    artifact_path = '/app/outputs/accumulated_thermal_conductivity.csv'
    with open(artifact_path, newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    required = ['frequency(THz)', 'accumulated_kappa_100(W/mK)', 'accumulated_kappa_010(W/mK)', 'accumulated_kappa_001(W/mK)']
    for col in required:
        if col not in rows[0]:
            return 0.0
    score = 0.2
    freqs = []
    kappa = {'[100]': [], '[010]': [], '[001]': []}
    try:
        for row in rows:
            f = float(row['frequency(THz)'])
            freqs.append(f)
            for d, key in [('[100]', 'accumulated_kappa_100(W/mK)'), ('[010]', 'accumulated_kappa_010(W/mK)'), ('[001]', 'accumulated_kappa_001(W/mK)')]:
                k = float(row[key])
                kappa[d].append(k)
    except:
        return score
    # monotonic frequency
    freq_increasing = all(freqs[i] < freqs[i+1] for i in range(len(freqs)-1))
    if freq_increasing:
        score += 0.15
    else:
        # try non-decreasing
        if all(freqs[i] <= freqs[i+1] for i in range(len(freqs)-1)):
            score += 0.05
    # monotonic accumulated for each direction
    mono_ok = 0
    for d in ['[100]', '[010]', '[001]']:
        arr = kappa[d]
        if all(arr[i] <= arr[i+1] + 1e-9 for i in range(len(arr)-1)):  # allow tiny noise
            mono_ok += 1
    mono_fraction = mono_ok / 3.0
    score += 0.20 * mono_fraction
    gold = {'[100]': 10.68, '[010]': 20.78, '[001]': 12.61}
    tol = 0.20
    final_ok = 0
    for d in ['[100]', '[010]', '[001]']:
        if kappa[d]:
            final = kappa[d][-1]
            if abs(final - gold[d]) <= tol * gold[d]:
                final_ok += 1
    final_fraction = final_ok / 3.0
    score += 0.30 * final_fraction
    # at least 0.1 bonus if all good
    if freq_increasing and mono_ok == 3 and final_ok == 3:
        score = 1.0
    return min(1.0, score)


_SCORERS = {
    'phonon_check': score_0,
    'thermal_kappa': score_1,
    'accumulated_kappa': score_2,
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
