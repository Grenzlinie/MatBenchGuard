import os
import json
import csv

# === author imports / helpers ===
import os
import csv
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
    def prepare(outputs_dir, spec):
        peaks_path = os.path.join(outputs_dir, 'dos_peaks.csv')
        peaks = []
        if os.path.exists(peaks_path):
            with open(peaks_path, newline='') as f:
                reader = csv.DictReader(f)
                peaks = list(reader)
        return {'spec': spec, 'dos_peaks': peaks}


# === block: score_0 (check id='structural_params') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = step.get('targets', {})
        tolerances = step.get('tolerances', {})
        if not artifact:
            return 0.0
        total = 0
        correct = 0
        for row in artifact:
            sys = row.get('system', '').strip()
            if sys in targets:
                t = targets[sys]
                for field in t:
                    if field == 'system':
                        continue
                    try:
                        val = float(row.get(field, 0))
                    except (ValueError, TypeError):
                        val = None
                    tol = tolerances.get(field, 0.0)
                    total += 1
                    if val is not None and abs(val - t[field]) <= tol:
                        correct += 1
        return correct / total if total > 0 else 0.0


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = step.get('targets', {})
        tolerances = step.get('tolerances', {})
        if not artifact:
            return 0.0
        total = 0
        correct = 0
        for row in artifact:
            sys = row.get('system', '').strip()
            if sys in targets:
                t = targets[sys]
                # check gap_type (exact)
                if 'gap_type' in t:
                    total += 1
                    if row.get('gap_type', '').strip().lower() == t['gap_type'].lower():
                        correct += 1
                # check value_eV within tolerance
                if 'value_eV' in t:
                    try:
                        val = float(row.get('value_eV', 0))
                    except (ValueError, TypeError):
                        val = 0.0
                    tol = tolerances.get('value_eV', 0.1)
                    total += 1
                    if abs(val - t['value_eV']) <= tol:
                        correct += 1
        return correct / total if total > 0 else 0.0


# === block: score_2 (check id='dos_peaks') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = step.get('expected_peaks', {})
        tolerances = step.get('tolerances', {})
        if not artifact:
            return 0.0
        peaks_by_sys = {}
        for row in artifact:
            sys = row.get('system', '').strip()
            peaks_by_sys.setdefault(sys, []).append(row)
        total_expected = 0
        matched = 0
        for sys, exp_peaks in expected.items():
            submitted = peaks_by_sys.get(sys, [])
            for exp in exp_peaks:
                total_expected += 1
                e_energy = exp.get('peak_energy_eV', 0.0)
                e_type = exp.get('peak_type', '').strip().lower()
                found = False
                for sub in submitted:
                    try:
                        s_energy = float(sub.get('peak_energy_eV', 0))
                    except:
                        s_energy = 0.0
                    s_type = sub.get('peak_type', '').strip().lower()
                    if abs(s_energy - e_energy) <= tolerances.get('peak_energy_eV', 0.1) and s_type == e_type:
                        try:
                            s_intensity = float(sub.get('intensity', 0))
                        except:
                            s_intensity = 0.0
                        if s_intensity > 0:
                            found = True
                            break
                if found:
                    matched += 1
        return matched / total_expected if total_expected > 0 else 0.0


# === block: score_3 (check id='linear_fit') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        # Recompute slopes from dos_peaks intensities
        dos_peaks = ctx.get('dos_peaks', [])
        x_map = step.get('concentration_map', {})
        gold_slopes = step.get('gold_slopes', {})
        tol = step.get('tolerance_slope', 0.2)
        if not dos_peaks:
            return 0.0
        # Build data for H_related (all systems) and delta (top only)
        h_x_vals = []
        h_y_vals = []
        delta_x_vals = []
        delta_y_vals = []
        for row in dos_peaks:
            sys = row.get('system', '').strip()
            ptype = row.get('peak_type', '').strip().lower()
            x = x_map.get(sys)
            if x is None:
                continue
            try:
                intensity = float(row.get('intensity', 0))
            except:
                intensity = 0.0
            if ptype == 'h_related':
                h_x_vals.append(x)
                h_y_vals.append(intensity)
            elif ptype == 'delta':
                delta_x_vals.append(x)
                delta_y_vals.append(intensity)
        def slope_through_origin(xlist, ylist):
            if not xlist or len(xlist) == 0:
                return 0.0
            sum_xy = sum(x*y for x,y in zip(xlist, ylist))
            sum_xx = sum(x*x for x in xlist)
            return sum_xy / sum_xx if sum_xx != 0 else 0.0
        h_slope = slope_through_origin(h_x_vals, h_y_vals)
        d_slope = slope_through_origin(delta_x_vals, delta_y_vals)
        h_target = gold_slopes.get('H_peak', 1.6)
        d_target = gold_slopes.get('delta', 1.3)
        def slope_score(computed, target, tolerance):
            if tolerance <= 0:
                return 1.0 if computed == target else 0.0
            diff = abs(computed - target)
            return max(0.0, 1.0 - diff / tolerance)
        s1 = slope_score(h_slope, h_target, tol)
        s2 = slope_score(d_slope, d_target, tol)
        # Simple average of the two slope scores
        return (s1 + s2) / 2.0


_SCORERS = {
    'structural_params': score_0,
    'band_gaps': score_1,
    'dos_peaks': score_2,
    'linear_fit': score_3,
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
