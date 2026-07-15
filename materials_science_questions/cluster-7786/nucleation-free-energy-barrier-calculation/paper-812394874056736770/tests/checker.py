import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='supersaturation_SiH4_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    silane = step['silane']
    T = step['temperature_K']
    mf = step['mole_fraction']
    gold = step['gold_supersaturation']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == silane and abs(float(r.get('temperature_K',0)) - T) < 0.5 and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            s = float(r.get('supersaturation',0))
            if s <= 0: return 0.0
            rel_err = abs(s - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_1 (check id='supersaturation_SiH2Cl2_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    silane = step['silane']
    T = step['temperature_K']
    mf = step['mole_fraction']
    gold = step['gold_supersaturation']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == silane and abs(float(r.get('temperature_K',0)) - T) < 0.5 and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            s = float(r.get('supersaturation',0))
            if s <= 0: return 0.0
            rel_err = abs(s - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_2 (check id='supersaturation_SiHCl3_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    silane = step['silane']
    T = step['temperature_K']
    mf = step['mole_fraction']
    gold = step['gold_supersaturation']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == silane and abs(float(r.get('temperature_K',0)) - T) < 0.5 and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            s = float(r.get('supersaturation',0))
            if s <= 0: return 0.0
            rel_err = abs(s - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_3 (check id='conversion_ratio_high_SiH4_check') ===
def score_3(artifact, step, ctx):
    rows = artifact
    silane = step['silane']
    T = step['temperature_K']
    mf = step['mole_fraction']
    threshold = step['threshold']
    for r in rows:
        if r.get('silane','').strip() == silane and abs(float(r.get('temperature_K',0)) - T) < 0.5 and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            cr = float(r.get('conversion_ratio',0))
            return 1.0 if cr >= threshold else 0.0
    return 0.0


# === block: score_4 (check id='supersaturation_ordering_check') ===
def score_4(artifact, step, ctx):
    rows = artifact
    T = step['temperature_K']
    mf = step['mole_fraction']
    order = step['expected_order']
    vals = {}
    for r in rows:
        if abs(float(r.get('temperature_K',0)) - T) < 0.5 and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            sil = r.get('silane','').strip()
            vals[sil] = float(r.get('supersaturation',0))
    if set(order) != set(vals.keys()): return 0.0
    for i in range(len(order)-1):
        if vals[order[i]] <= vals[order[i+1]]:
            return 0.0
    return 1.0


# === block: score_5 (check id='time_lag_mf04_check') ===
def score_5(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = step['mole_fraction']
    gold = step['gold_time_lag_s']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            val = float(r.get('time_lag_s',0))
            if val <= 0: return 0.0
            rel_err = abs(val - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_6 (check id='time_lag_mf001_check') ===
def score_6(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = step['mole_fraction']
    gold = step['gold_time_lag_s']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            val = float(r.get('time_lag_s',0))
            if val <= 0: return 0.0
            rel_err = abs(val - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_7 (check id='time_lag_mf0001_check') ===
def score_7(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = step['mole_fraction']
    gold = step['gold_time_lag_s']
    tol = step['relative_tolerance']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            val = float(r.get('time_lag_s',0))
            if val <= 0: return 0.0
            rel_err = abs(val - gold) / gold
            if rel_err <= tol: return 1.0
            if rel_err <= 2*tol: return 1.0 - (rel_err - tol)/tol
            return 0.0
    return 0.0


# === block: score_8 (check id='onset_T_pure_SiH4_check') ===
def score_8(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = step['mole_fraction']
    lo = step['lower_onset_T_min']
    hi = step['lower_onset_T_max']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            T = float(r.get('lower_onset_T',0))
            return 1.0 if lo <= T <= hi else 0.0
    return 0.0


# === block: score_9 (check id='onset_T_dilute_SiH4_check') ===
def score_9(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = 1e-5
    lo = step['lower_onset_T_min']
    hi = step['lower_onset_T_max']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-12:
            T = float(r.get('lower_onset_T',0))
            return 1.0 if lo <= T <= hi else 0.0
    return 0.0


# === block: score_10 (check id='critical_size_mf04_check') ===
def score_10(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = 0.4
    lo = step['kstar_min']
    hi = step['kstar_max']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            k = float(r.get('critical_cluster_size',0))
            return 1.0 if lo <= k <= hi else 0.0
    return 0.0


# === block: score_11 (check id='critical_size_mf001_check') ===
def score_11(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = 0.01
    lo = step['kstar_min']
    hi = step['kstar_max']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            k = float(r.get('critical_cluster_size',0))
            return 1.0 if lo <= k <= hi else 0.0
    return 0.0


# === block: score_12 (check id='critical_size_mf0001_check') ===
def score_12(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    model = step['model']
    mf = 1e-4
    lo = step['kstar_min']
    hi = step['kstar_max']
    for r in rows:
        if r.get('silane','').strip() == sil and r.get('model','').strip() == model and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            k = float(r.get('critical_cluster_size',0))
            return 1.0 if lo <= k <= hi else 0.0
    return 0.0


# === block: score_13 (check id='upper_lower_ordering_check') ===
def score_13(artifact, step, ctx):
    rows = artifact
    for r in rows:
        if float(r.get('lower_onset_T',0)) > 0 and float(r.get('upper_onset_T',0)) > float(r.get('lower_onset_T',0)):
            return 1.0
    return 0.0


# === block: score_14 (check id='nucleation_rate_peak_check') ===
def score_14(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    mf = step['mole_fraction']
    min_rate = step['min_rate_peak']
    T_min = step['peak_T_min']
    T_max = step['peak_T_max']
    subset = []
    for r in rows:
        if r.get('silane','').strip() == sil and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            T = float(r['temperature_K'])
            J = float(r['nucleation_rate_per_cm3_per_s'])
            subset.append((T, J))
    if not subset: return 0.0
    subset.sort(key=lambda x: x[0])
    max_J = max(subset, key=lambda x: x[1])
    if max_J[1] < min_rate: return 0.0
    if not (T_min <= max_J[0] <= T_max): return 0.0
    return 1.0


# === block: score_15 (check id='nucleation_rate_highT_low_check_04') ===
def score_15(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    mf = step['mole_fraction']
    T = step['temperature_K']
    max_val = step['max_rate']
    for r in rows:
        if r.get('silane','').strip() == sil and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8 and abs(float(r.get('temperature_K',0)) - T) < 0.5:
            J = float(r.get('nucleation_rate_per_cm3_per_s',0))
            return 1.0 if J <= max_val else 0.0
    return 0.0


# === block: score_16 (check id='nucleation_rate_highT_low_check_001') ===
def score_16(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    mf = 0.01
    T = step['temperature_K']
    max_val = step['max_rate']
    for r in rows:
        if r.get('silane','').strip() == sil and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8 and abs(float(r.get('temperature_K',0)) - T) < 0.5:
            J = float(r.get('nucleation_rate_per_cm3_per_s',0))
            return 1.0 if J <= max_val else 0.0
    return 0.0


# === block: score_17 (check id='nucleation_rate_ordering_check') ===
def score_17(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    T = step['temperature_K']
    mfs = step['mole_fractions']
    def get_j(mf):
        for r in rows:
            if r.get('silane','').strip() == sil and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8 and abs(float(r.get('temperature_K',0)) - T) < 0.5:
                return float(r.get('nucleation_rate_per_cm3_per_s',0))
        return None
    vals = [get_j(mf) for mf in mfs]
    if any(v is None for v in vals):
        return 0.0
    if all(v1 > v2 for v1, v2 in zip(vals[:-1], vals[1:])):
        return 1.0
    return 0.0


# === block: score_18 (check id='nucleation_rate_shape_peak_check') ===
def score_18(artifact, step, ctx):
    rows = artifact
    sil = step['silane']
    mf = step['mole_fraction']
    subset = []
    for r in rows:
        if r.get('silane','').strip() == sil and abs(float(r.get('mole_fraction',0)) - mf) < 1e-8:
            subset.append((float(r['temperature_K']), float(r['nucleation_rate_per_cm3_per_s'])))
    if len(subset) < 3: return 0.0
    subset.sort(key=lambda x: x[0])
    js = [x[1] for x in subset]
    has_increase = False
    has_decrease = False
    for i in range(1, len(js)):
        if js[i] > js[i-1]:
            has_increase = True
        if js[i] < js[i-1]:
            has_decrease = True
    return 1.0 if has_increase and has_decrease else 0.0


# === block: score_19 (check id='decomp_1e6_temp_check') ===
def score_19(artifact, step, ctx):
    rows = artifact
    rate = step['heating_rate']
    lo = step['temp_min']
    hi = step['temp_max']
    for r in rows:
        if abs(float(r.get('heating_rate_K_per_s',0)) - rate) < 0.5:
            T = float(r.get('temperature_99pct_decomposition_K',0))
            return 1.0 if lo <= T <= hi else 0.0
    return 0.0


# === block: score_20 (check id='decomp_1e0_temp_check') ===
def score_20(artifact, step, ctx):
    rows = artifact
    rate = 1.0
    lo = step['temp_min']
    hi = step['temp_max']
    for r in rows:
        if abs(float(r.get('heating_rate_K_per_s',0)) - rate) < 0.01:
            T = float(r.get('temperature_99pct_decomposition_K',0))
            return 1.0 if lo <= T <= hi else 0.0
    return 0.0


# === block: score_21 (check id='decomp_monotonicity_check') ===
def score_21(artifact, step, ctx):
    rows = artifact
    data = []
    for r in rows:
        data.append((float(r['heating_rate_K_per_s']), float(r['temperature_99pct_decomposition_K'])))
    if len(data) < 2: return 0.0
    data.sort(key=lambda x: x[0])
    for i in range(1, len(data)):
        if data[i][1] < data[i-1][1]:
            return 0.0
    return 1.0


_SCORERS = {
    'supersaturation_SiH4_check': score_0,
    'supersaturation_SiH2Cl2_check': score_1,
    'supersaturation_SiHCl3_check': score_2,
    'conversion_ratio_high_SiH4_check': score_3,
    'supersaturation_ordering_check': score_4,
    'time_lag_mf04_check': score_5,
    'time_lag_mf001_check': score_6,
    'time_lag_mf0001_check': score_7,
    'onset_T_pure_SiH4_check': score_8,
    'onset_T_dilute_SiH4_check': score_9,
    'critical_size_mf04_check': score_10,
    'critical_size_mf001_check': score_11,
    'critical_size_mf0001_check': score_12,
    'upper_lower_ordering_check': score_13,
    'nucleation_rate_peak_check': score_14,
    'nucleation_rate_highT_low_check_04': score_15,
    'nucleation_rate_highT_low_check_001': score_16,
    'nucleation_rate_ordering_check': score_17,
    'nucleation_rate_shape_peak_check': score_18,
    'decomp_1e6_temp_check': score_19,
    'decomp_1e0_temp_check': score_20,
    'decomp_monotonicity_check': score_21,
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
