import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json
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
        # No hidden assets; return empty context.
        return {}


# === block: score_0 (check id='step_solvation') ===
def score_0(artifact, step, ctx):
            # artifact is list of dicts with keys 'effective_pore_width_nm' and 'solvation_pressure_GPa'
            # Build sorted lists of H and sigma from the CSV
            try:
                hs = []
                sigs = []
                for row in artifact:
                    hs.append(float(row['effective_pore_width_nm']))
                    sigs.append(float(row['solvation_pressure_GPa']))
                # Sort by H
                paired = sorted(zip(hs, sigs), key=lambda x: x[0])
                hs_sorted = [p[0] for p in paired]
                sigs_sorted = [p[1] for p in paired]
            except Exception:
                return 0.0

            # Helper: linear interpolation / extrapolation
            def interp(x, xs, ys):
                if x <= xs[0]:
                    return ys[0]
                if x >= xs[-1]:
                    return ys[-1]
                for i in range(len(xs)-1):
                    if xs[i] <= x <= xs[i+1]:
                        t = (x - xs[i]) / (xs[i+1] - xs[i])
                        return ys[i] + t * (ys[i+1] - ys[i])
                # fallback
                return ys[-1]

            targets = step.get('targets', {})
            checks = []

            # 1. Max at 0.23 nm
            t1 = targets.get('max_at_0.23', {})
            val = interp(t1['Heff'], hs_sorted, sigs_sorted)
            if t1['value_min'] <= val <= t1['value_max']:
                checks.append(1.0)
            else:
                # partial credit based on distance from band
                dist = max(0.0, t1['value_min'] - val, val - t1['value_max'])
                score = max(0.0, 1.0 - dist / (t1['value_max'] - t1['value_min']))
                checks.append(score)

            # 2. Zero crossing around 0.31 nm (+/- 0.02)
            t2 = targets.get('zero_crossing', {})
            val_lo = interp(t2['Heff_min'], hs_sorted, sigs_sorted)
            val_hi = interp(t2['Heff_max'], hs_sorted, sigs_sorted)
            # sign change expected between these two points, and value at Heff_min should be small (near zero)
            sign_change = (val_lo > 0 > val_hi) or (val_lo < 0 < val_hi) or (abs(val_lo) < t2['abs_tol'] and abs(val_hi) < t2['abs_tol'])
            small_val = abs(interp(0.31, hs_sorted, sigs_sorted)) < t2['abs_tol']
            checks.append(1.0 if (sign_change and small_val) else (0.5 if sign_change else 0.0))

            # 3. Secondary max near 0.54 nm
            t3 = targets.get('secondary_max', {})
            val = interp(t3['Heff'], hs_sorted, sigs_sorted)
            if t3['value_min'] <= val <= t3['value_max']:
                checks.append(1.0)
            else:
                dist = max(0.0, t3['value_min'] - val, val - t3['value_max'])
                score = max(0.0, 1.0 - dist / (t3['value_max'] - t3['value_min']))
                checks.append(score)

            # 4. Tail small for H >= 1.3 nm
            t4 = targets.get('tail_small', {})
            # check that at 1.3 nm the value is below threshold
            val13 = interp(1.3, hs_sorted, sigs_sorted)
            tail_ok = abs(val13) < t4['value_max']
            # also check at max H if >=1.3
            max_h = hs_sorted[-1]
            if max_h >= 1.3:
                val_max = sigs_sorted[-1]
                tail_ok = tail_ok and (abs(val_max) < t4['value_max'])
            checks.append(1.0 if tail_ok else 0.0)

            return sum(checks) / len(checks)


# === block: score_1 (check id='step_strain') ===
def score_1(artifact, step, ctx):
            # artifact: list of dicts with 'pressure_MPa' and 'volumetric_strain'
            try:
                pressures = []
                strains = []
                for row in artifact:
                    pressures.append(float(row['pressure_MPa']))
                    strains.append(float(row['volumetric_strain']))
                # Sort by pressure
                sorted_idx = sorted(range(len(pressures)), key=lambda i: pressures[i])
                ps = [pressures[i] for i in sorted_idx]
                es = [strains[i] for i in sorted_idx]
            except Exception:
                return 0.0

            targets = step.get('targets', {})
            checks = []

            # 1. Monotonic increase (allow tiny noise: each subsequent strain >= previous - epsilon)
            mono = True
            for i in range(1, len(es)):
                if es[i] < es[i-1] - 1e-6:
                    mono = False
                    break
            checks.append(1.0 if mono else 0.0)

            # Helper to find value closest to a given pressure
            def get_closest(press, val_array, press_array):
                idx = min(range(len(press_array)), key=lambda i: abs(press_array[i] - press))
                return val_array[idx]

            # 2. At 2.9 MPa
            t2 = targets.get('at_2.9_MPa', {})
            strain_pt = get_closest(t2['pressure'], es, ps)
            if t2['value_min'] <= strain_pt <= t2['value_max']:
                checks.append(1.0)
            else:
                dist = max(0.0, t2['value_min'] - strain_pt, strain_pt - t2['value_max'])
                score = max(0.0, 1.0 - dist / (t2['value_max'] - t2['value_min']))
                checks.append(score)

            # 3. At 27 MPa
            t3 = targets.get('at_27_MPa', {})
            strain_pt = get_closest(t3['pressure'], es, ps)
            if t3['value_min'] <= strain_pt <= t3['value_max']:
                checks.append(1.0)
            else:
                dist = max(0.0, t3['value_min'] - strain_pt, strain_pt - t3['value_max'])
                score = max(0.0, 1.0 - dist / (t3['value_max'] - t3['value_min']))
                checks.append(score)

            return sum(checks) / len(checks)


# === block: score_2 (check id='step_adsorption') ===
def score_2(artifact, step, ctx):
            # artifact: list of dicts with 'pressure_MPa' and 'loading_cm3_g'
            try:
                pressures = []
                loads = []
                for row in artifact:
                    pressures.append(float(row['pressure_MPa']))
                    loads.append(float(row['loading_cm3_g']))
                # Sort by pressure
                sorted_idx = sorted(range(len(pressures)), key=lambda i: pressures[i])
                ps = [pressures[i] for i in sorted_idx]
                ls = [loads[i] for i in sorted_idx]
            except Exception:
                return 0.0

            targets = step.get('targets', {})
            checks = []

            def get_closest(press, val_array, press_array):
                idx = min(range(len(press_array)), key=lambda i: abs(press_array[i] - press))
                return val_array[idx]

            # 1. At 2.9 MPa
            t1 = targets.get('at_2.9_MPa', {})
            ref_val = t1['value']
            tol_abs = t1['tol_rel'] * ref_val
            load_pt = get_closest(t1['pressure'], ls, ps)
            err = abs(load_pt - ref_val)
            if err <= tol_abs:
                checks.append(1.0)
            else:
                score = max(0.0, 1.0 - (err - tol_abs) / (2 * tol_abs) )
                checks.append(score)

            # 2. At 27 MPa
            t2 = targets.get('at_27_MPa', {})
            ref_val = t2['value']
            tol_abs = t2['tol_rel'] * ref_val
            load_pt = get_closest(t2['pressure'], ls, ps)
            err = abs(load_pt - ref_val)
            if err <= tol_abs:
                checks.append(1.0)
            else:
                score = max(0.0, 1.0 - (err - tol_abs) / (2 * tol_abs) )
                checks.append(score)

            return sum(checks) / len(checks)


_SCORERS = {
    'step_solvation': score_0,
    'step_strain': score_1,
    'step_adsorption': score_2,
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
