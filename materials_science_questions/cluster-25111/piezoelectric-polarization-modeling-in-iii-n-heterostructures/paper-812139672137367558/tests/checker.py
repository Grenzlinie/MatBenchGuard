import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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
    artifact_path = os.path.join(outputs_dir, 'responsivity_spectra.csv')
    data = {}
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cond = row['condition']
                try:
                    wl = int(row['wavelength_nm'])
                    resp = float(row['responsivity_A_per_W'])
                except (ValueError, KeyError):
                    continue
                data.setdefault(cond, {})[wl] = resp
    except Exception:
        data = {}
    return {'data': data}


# === block: score_0 (check id='step_1_structure') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    required_conditions = params.get('required_conditions', [])
    required_wavelengths = params.get('required_wavelengths', [])
    ok = True
    data = ctx.get('data', {})
    for cond in required_conditions:
        if cond not in data:
            ok = False
            break
        for wl in required_wavelengths:
            if wl not in data[cond]:
                ok = False
                break
        if not ok:
            break
    return 1.0 if ok else 0.0


# === block: score_1 (check id='step_2_ratio') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    cond_list = params.get('condition_list', [])
    num_wl = params.get('numerator_wavelength', 310)
    den_wl = params.get('denominator_wavelength', 365)
    min_ratio = 1000.0
    data = ctx.get('data', {})
    passed = 0
    total = len(cond_list)
    for cond in cond_list:
        entry = data.get(cond, {})
        r_num = entry.get(num_wl, None)
        r_den = entry.get(den_wl, None)
        if r_num is None or r_den is None:
            continue
        if r_den == 0:
            continue
        ratio = r_num / r_den
        if ratio >= min_ratio:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='step_3_fractional_change') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    baseline = params.get('baseline_condition', 'full_ion_polar')
    test_conds = params.get('test_conditions', [])
    wavelengths = params.get('check_wavelengths', [])
    max_allowed = float(params.get('max_allowed_fractional_change', 0.12))
    data = ctx.get('data', {})
    baseline_data = data.get(baseline, {})
    passed = 0
    total = len(test_conds)
    for test_cond in test_conds:
        test_data = data.get(test_cond, {})
        max_frac = 0.0
        ok = True
        for wl in wavelengths:
            base_val = baseline_data.get(wl, None)
            test_val = test_data.get(wl, None)
            if base_val is None or test_val is None:
                ok = False
                break
            if base_val == 0:
                if test_val != 0:
                    ok = False
                    break
                frac = 0.0
            else:
                frac = abs(test_val - base_val) / abs(base_val)
            if frac > max_frac:
                max_frac = frac
        if ok and max_frac <= max_allowed:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'step_1_structure': score_0,
    'step_2_ratio': score_1,
    'step_3_fractional_change': score_2,
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
