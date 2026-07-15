import os
import json
import csv

# === author imports / helpers ===
import os, math, bisect


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
    artifacts = {}
    fnames = ['ideal_dry_isotherm.csv', 'defect1_dry_isotherm.csv', 'defect1_low_water_isotherm.csv', 'defect1_intermediate_water_isotherm.csv', 'defect2_dry_isotherm.csv', 'defect2_low_water_isotherm.csv', 'defect2_intermediate_water_isotherm.csv']
    for fname in fnames:
        path = os.path.join(outputs_dir, fname)
        if os.path.exists(path):
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                for row in rows:
                    row['CO2_pressure_kPa'] = float(row['CO2_pressure_kPa'])
                    row['CO2_loading_mol_kg'] = float(row['CO2_loading_mol_kg'])
                artifacts[fname] = rows
        else:
            artifacts[fname] = None
    gold = spec.get('hidden_gold_isotherms', {})
    return {'artifacts': artifacts, 'gold': gold, 'outputs_dir': outputs_dir}


# === block: score_0 (check id='numeric_ideal_dry') ===
def score_0(artifact, step, ctx):
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0

    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    return _calc_mape(artifact, gold_entries)


# === block: score_1 (check id='numeric_defect1_dry') ===
def score_1(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_2 (check id='numeric_defect1_low') ===
def score_2(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_3 (check id='numeric_defect1_int') ===
def score_3(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_4 (check id='numeric_defect2_dry') ===
def score_4(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_5 (check id='numeric_defect2_low') ===
def score_5(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_6 (check id='numeric_defect2_int') ===
def score_6(artifact, step, ctx):
    fname = step['output_file']
    gold_entries = ctx['gold'].get(fname, [])
    def _calc_mape(artifact, gold_entries):
        gold_dict = {entry['pressure']: entry['loading'] for entry in gold_entries}
        ref_pressures = sorted(gold_dict.keys())
        if not artifact:
            return 0.0
        sorted_data = sorted(artifact, key=lambda r: r['CO2_pressure_kPa'])
        pressures = [r['CO2_pressure_kPa'] for r in sorted_data]
        loadings = [r['CO2_loading_mol_kg'] for r in sorted_data]
        def interp(p):
            if p <= pressures[0]:
                return loadings[0]
            if p >= pressures[-1]:
                return loadings[-1]
            i = bisect.bisect_left(pressures, p)
            if i == 0:
                return loadings[0]
            if pressures[i] == p:
                return loadings[i]
            frac = (p - pressures[i-1]) / (pressures[i] - pressures[i-1])
            return loadings[i-1] + frac * (loadings[i] - loadings[i-1])
        apes = []
        for p in ref_pressures:
            gold_loading = gold_dict[p]
            if abs(gold_loading) < 1e-9:
                ape = 0.0 if abs(interp(p)) < 1e-9 else 100.0
            else:
                ape = abs(interp(p) - gold_loading) / abs(gold_loading) * 100.0
            apes.append(ape)
        mape = sum(apes) / len(apes) if apes else 100.0
        if mape <= 20.0:
            return 1.0
        elif mape <= 40.0:
            return (40.0 - mape) / 20.0
        else:
            return 0.0
    return _calc_mape(artifact, gold_entries)


# === block: score_7 (check id='trend_defect1_enhancement') ===
def score_7(artifact, step, ctx):
    dry = ctx['artifacts'].get('defect1_dry_isotherm.csv')
    low = ctx['artifacts'].get('defect1_low_water_isotherm.csv')
    if dry is None or low is None:
        return 0.0
    pressures_dry = set()
    loading_by_p_dry = {}
    for r in dry:
        p = r['CO2_pressure_kPa']
        if p <= 1.0:
            pressures_dry.add(p)
            loading_by_p_dry[p] = r['CO2_loading_mol_kg']
    pressures_low = set()
    loading_by_p_low = {}
    for r in low:
        p = r['CO2_pressure_kPa']
        if p <= 1.0:
            pressures_low.add(p)
            loading_by_p_low[p] = r['CO2_loading_mol_kg']
    common = pressures_dry & pressures_low
    if not common:
        return 0.0
    for p in common:
        if loading_by_p_low[p] + 1e-9 < loading_by_p_dry[p]:
            return 0.0
    return 1.0


# === block: score_8 (check id='trend_defect1_reduction') ===
def score_8(artifact, step, ctx):
    dry = ctx['artifacts'].get('defect1_dry_isotherm.csv')
    mid = ctx['artifacts'].get('defect1_intermediate_water_isotherm.csv')
    if dry is None or mid is None:
        return 0.0
    pressures_dry = set()
    loading_by_p_dry = {}
    for r in dry:
        p = r['CO2_pressure_kPa']
        pressures_dry.add(p)
        loading_by_p_dry[p] = r['CO2_loading_mol_kg']
    pressures_mid = set()
    loading_by_p_mid = {}
    for r in mid:
        p = r['CO2_pressure_kPa']
        pressures_mid.add(p)
        loading_by_p_mid[p] = r['CO2_loading_mol_kg']
    common = pressures_dry & pressures_mid
    if not common:
        return 0.0
    for p in common:
        if loading_by_p_mid[p] > loading_by_p_dry[p] + 1e-9:
            return 0.0
    return 1.0


# === block: score_9 (check id='trend_defect2_no_enhancement') ===
def score_9(artifact, step, ctx):
    dry2 = ctx['artifacts'].get('defect2_dry_isotherm.csv')
    low2 = ctx['artifacts'].get('defect2_low_water_isotherm.csv')
    if dry2 is None or low2 is None:
        return 0.0
    pressures_dry2 = set()
    loading_by_p_dry2 = {}
    for r in dry2:
        p = r['CO2_pressure_kPa']
        if p <= 1.0:
            pressures_dry2.add(p)
            loading_by_p_dry2[p] = r['CO2_loading_mol_kg']
    pressures_low2 = set()
    loading_by_p_low2 = {}
    for r in low2:
        p = r['CO2_pressure_kPa']
        if p <= 1.0:
            pressures_low2.add(p)
            loading_by_p_low2[p] = r['CO2_loading_mol_kg']
    common = pressures_dry2 & pressures_low2
    if not common:
        return 0.0
    for p in common:
        if loading_by_p_low2[p] > loading_by_p_dry2[p] + 1e-9:
            return 0.0
    return 1.0


# === block: score_10 (check id='trend_defect1_dry_gt_ideal') ===
def score_10(artifact, step, ctx):
    d1 = ctx['artifacts'].get('defect1_dry_isotherm.csv')
    ideal = ctx['artifacts'].get('ideal_dry_isotherm.csv')
    if d1 is None or ideal is None:
        return 0.0
    pressures_d1 = set()
    loading_by_p_d1 = {}
    for r in d1:
        p = r['CO2_pressure_kPa']
        pressures_d1.add(p)
        loading_by_p_d1[p] = r['CO2_loading_mol_kg']
    pressures_ideal = set()
    loading_by_p_ideal = {}
    for r in ideal:
        p = r['CO2_pressure_kPa']
        pressures_ideal.add(p)
        loading_by_p_ideal[p] = r['CO2_loading_mol_kg']
    common = pressures_d1 & pressures_ideal
    if not common:
        return 0.0
    for p in common:
        if loading_by_p_d1[p] <= loading_by_p_ideal[p] + 1e-9:
            return 0.0
    return 1.0


_SCORERS = {
    'numeric_ideal_dry': score_0,
    'numeric_defect1_dry': score_1,
    'numeric_defect1_low': score_2,
    'numeric_defect1_int': score_3,
    'numeric_defect2_dry': score_4,
    'numeric_defect2_low': score_5,
    'numeric_defect2_int': score_6,
    'trend_defect1_enhancement': score_7,
    'trend_defect1_reduction': score_8,
    'trend_defect2_no_enhancement': score_9,
    'trend_defect1_dry_gt_ideal': score_10,
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
