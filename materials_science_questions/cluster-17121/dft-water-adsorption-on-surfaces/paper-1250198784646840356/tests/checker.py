import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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


# === block: score_0 (check id='step_01_HM_time') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is list of dicts from CSV
    threshold = step['threshold']
    tmin = step['time_min']
    tmax = step['time_max']
    max_hm = 0.0
    for row in rows:
        t = float(row['time_ps'])
        hm = float(row['HM_ratio'])
        if tmin <= t <= tmax:
            if hm > max_hm:
                max_hm = hm
    return 1.0 if max_hm >= threshold else 0.0


# === block: score_1 (check id='step_02_aCNA') ===
def score_1(artifact, step, ctx):
    rows = artifact
    threshold = step['threshold_fcc']
    if not rows:
        return 0.0

    # the quenched configuration is the last state in the time series;
    # gather all rows with the maximum time to average thermal noise
    max_t = None
    max_times = []
    for r in rows:
        t = float(r['time_ps'])
        if max_t is None or t > max_t:
            max_t = t
            max_times = [r]
        elif t == max_t:
            max_times.append(r)

    if not max_times:
        return 0.0

    fcc_vals = [float(r['fcc_frac']) for r in max_times]
    avg_fcc = sum(fcc_vals) / len(fcc_vals)
    return 1.0 if avg_fcc >= threshold else 0.0


# === block: score_2 (check id='step_03_persistence') ===
def score_2(artifact, step, ctx):
    data = artifact
    br = step['birth_range']
    dr = step['death_range']
    def has_ring(pairs):
        for b,d in pairs:
            if br[0] <= b <= br[1] and dr[0] <= d <= dr[1]:
                return True
        return False
    pairs = data.get('persistence_pairs', [])
    ref = data.get('reference_bulk_CaH4', [])
    if has_ring(pairs) and has_ring(ref):
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='step_04_HM_pressure') ===
def score_3(artifact, step, ctx):
    rows = artifact
    high = step['threshold_high']
    low = step['threshold_low']
    conditions = {}
    for r in rows:
        p = int(r['pressure_GPa'])
        t = int(r['temperature_K'])
        s = r['surface'].strip()
        hm = float(r['HM_ratio'])
        conditions.setdefault((s, t), {})[p] = hm
    if not conditions:
        return 0.0
    ok = 0
    total = 0
    for (s, t), vals in conditions.items():
        for p, hm in vals.items():
            total += 1
            if s == '100' and t == 1500:
                if p >= 30:
                    if hm > high:
                        ok += 1
                else:
                    # no strict check for lower pressures; accept any
                    ok += 1
            else:
                if hm < low:
                    ok += 1
        # also require that for (100) at 1500K, HM not decrease with pressure (optional monotonic check)
        if s == '100' and t == 1500:
            sorted_p = sorted(vals.keys())
            for i in range(len(sorted_p)-1):
                if vals[sorted_p[i]] > vals[sorted_p[i+1]]:
                    ok = max(0, ok-1)
    return (ok / max(total,1)) if total > 0 else 0.0


# === block: score_4 (check id='step_05_enthalpy') ===
def score_4(artifact, step, ctx):
    rows = artifact
    pt = step['pressure_threshold']
    passed = 0
    total = 0
    for r in rows:
        p = float(r['pressure_GPa'])
        if p >= pt:
            total += 1
            d1 = float(r['delta_H_fus'])
            d2 = float(r['delta_H_fus_plus_hyd'])
            if d2 < d1:
                passed += 1
    if total == 0:
        return 1.0  # no pressures >= threshold, consider pass
    return passed / total


_SCORERS = {
    'step_01_HM_time': score_0,
    'step_02_aCNA': score_1,
    'step_03_persistence': score_2,
    'step_04_HM_pressure': score_3,
    'step_05_enthalpy': score_4,
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
