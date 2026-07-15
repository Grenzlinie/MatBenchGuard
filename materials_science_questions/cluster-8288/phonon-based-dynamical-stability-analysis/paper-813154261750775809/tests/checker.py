import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='enthalpy_curves') ===
def score_0(artifact, step, ctx):
    def linear_interp(x0, y0, x1, y1, x_eval):
        return y0 + (y1 - y0) * (x_eval - x0) / (x1 - x0)

    def interpolate_curve(points, pressures):
        pts = sorted(points, key=lambda p: p["pressure"])
        x_vals = [p["pressure"] for p in pts]
        y_vals = [p["enthalpy_delta"] for p in pts]
        out = []
        idx = 0
        for x in pressures:
            while idx < len(pts) - 1 and x > x_vals[idx + 1]:
                idx += 1
            if idx == len(pts) - 1:
                # extrapolate flat last segment (or use last y)
                out.append(y_vals[-1])
            else:
                out.append(linear_interp(x_vals[idx], y_vals[idx], x_vals[idx+1], y_vals[idx+1], x))
        return out

    curves = artifact
    i4 = curves.get("I4/mcm", [])
    c2m = curves.get("C2/m", [])
    p6 = curves.get("P6/mmm", [])
    if not i4 or not c2m or not p6:
        return 0.0

    # 1. Check C2/m is reference (all deltas ≈ 0)
    c2m_delta_ok = all(abs(p.get("enthalpy_delta", 0)) <= 1e-3 for p in c2m)

    # 2. Build a common pressure grid from 0 to 100 GPa (step 0.5 GPa)
    common_p = [i * 0.5 for i in range(0, 201)]  # 0, 0.5, ..., 100.0
    i4_y = interpolate_curve(i4, common_p)
    p6_y = interpolate_curve(p6, common_p)
    c2m_y = [0.0] * len(common_p)  # by definition

    # 3. Determine stable phase at each pressure (lowest delta)
    stable = []
    for j in range(len(common_p)):
        vals = {"I4/mcm": i4_y[j], "C2/m": 0.0, "P6/mmm": p6_y[j]}
        min_phase = min(vals, key=vals.get)
        stable.append(min_phase)

    # 4. Identify contiguous regions and transition pressures
    regions = []
    current_phase = stable[0]
    start_p = common_p[0]
    for j in range(1, len(common_p)):
        if stable[j] != current_phase:
            regions.append((current_phase, start_p, common_p[j-1]))
            current_phase = stable[j]
            start_p = common_p[j]
    regions.append((current_phase, start_p, common_p[-1]))

    # Expected ordering: I4/mcm -> C2/m -> P6/mmm
    expected_order = ["I4/mcm", "C2/m", "P6/mmm"]
    if len(regions) != 3 or [r[0] for r in regions] != expected_order:
        return 0.0

    # 5. Transition pressures from region boundaries
    trans1 = regions[0][2]  # end of I4/mcm
    trans2 = regions[1][2]  # end of C2/m
    expected1 = step["target"]["transition_I4mcm_to_C2m"]
    expected2 = step["target"]["transition_C2m_to_P6mmm"]
    tol1 = step["target"]["tolerance_transition_1"]
    tol2 = step["target"]["tolerance_transition_2"]

    def trans_score(trans, expected, tol):
        dev = abs(trans - expected)
        if dev <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (dev - tol) / tol)

    score_trans1 = trans_score(trans1, expected1, tol1)
    score_trans2 = trans_score(trans2, expected2, tol2)

    # 6. Phase assignment accuracy on grid
    correct = 0
    for j, p in enumerate(common_p):
        expected_phase = None
        if p < expected1:
            expected_phase = "I4/mcm"
        elif p < expected2:
            expected_phase = "C2/m"
        else:
            expected_phase = "P6/mmm"
        if stable[j] == expected_phase:
            correct += 1
    frac_correct = correct / len(common_p)

    # 7. Combined score
    score = 0.0
    if c2m_delta_ok:
        score += 0.2
    score += 0.4 * (score_trans1 + score_trans2) / 2.0
    score += 0.4 * frac_correct

    return score


# === block: score_1 (check id='phonon_stability') ===
def score_1(artifact, step, ctx):
    freq_data = artifact
    all_freqs = []

    for freqs in freq_data.values():
        if isinstance(freqs, list):
            for f in freqs:
                if isinstance(f, (int, float)):
                    all_freqs.append(f)
        elif isinstance(freqs, (int, float)):
            all_freqs.append(freqs)

    if not all_freqs:
        return 0.0

    # Check all frequencies are above the imaginary threshold
    imag_thresh = step["target"]["imaginary_threshold"]
    if min(all_freqs) < imag_thresh:
        return 0.0

    return 1.0


_SCORERS = {
    'enthalpy_curves': score_0,
    'phonon_stability': score_1,
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
