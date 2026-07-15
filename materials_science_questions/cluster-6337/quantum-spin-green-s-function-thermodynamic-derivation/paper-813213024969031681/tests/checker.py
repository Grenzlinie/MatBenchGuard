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


# === block: score_0 (check id='thermal_curves') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 100:
        return 0.0
    T_vals = []
    M_vals = []
    A_vals = []
    C_vals = []
    for r in rows:
        try:
            t = float(r['T'])
            m = float(r['M'])
            a = float(r['A'])
            c = float(r['C'])
        except (KeyError, ValueError):
            return 0.0
        T_vals.append(t)
        M_vals.append(m)
        A_vals.append(a)
        C_vals.append(c)
    if T_vals[0] > 0.5 or T_vals[-1] < 11.5:
        return 0.0
    # Find Tc where M falls below threshold
    threshold = 0.1
    Tc_agent = None
    for i in range(len(T_vals)):
        if M_vals[i] < threshold:
            if i == 0:
                Tc_agent = T_vals[0]
            else:
                # linear interpolation
                x1, y1 = T_vals[i-1], M_vals[i-1]
                x2, y2 = T_vals[i], M_vals[i]
                if y1 > threshold and y2 <= threshold:
                    Tc_agent = x1 + (x2 - x1) * (y1 - threshold) / (y1 - y2)
                else:
                    Tc_agent = T_vals[i]
            break
    if Tc_agent is None:
        Tc_agent = T_vals[-1]
    Tc_ref = step['hidden']['Tc_ref']
    Tc_tol = step['hidden']['Tc_tol']
    tc_error = abs(Tc_agent - Tc_ref)
    tc_score = max(0.0, 1.0 - tc_error / (Tc_tol * 2))  # partial decay
    # Monotonicity of M (should generally decrease)
    non_mono = 0
    total = max(1, len(M_vals) - 1)
    for i in range(1, len(M_vals)):
        if M_vals[i] - M_vals[i-1] > 0.02:  # allow small numerical fluctuations
            non_mono += 1
    mono_score = max(0.0, 1.0 - non_mono / total)
    # A peak location
    A_max = max(A_vals)
    A_peak_idx = A_vals.index(A_max)
    A_peak_T = T_vals[A_peak_idx]
    A_dist = abs(A_peak_T - Tc_agent)
    A_score = max(0.0, 1.0 - A_dist / step['hidden']['A_peak_dist_tol'])
    # C dip location
    C_min = min(C_vals)
    C_dip_idx = C_vals.index(C_min)
    C_dip_T = T_vals[C_dip_idx]
    C_dist = abs(C_dip_T - Tc_agent)
    C_score = max(0.0, 1.0 - C_dist / step['hidden']['C_dip_dist_tol'])
    # Check initial M near 2
    init_M = M_vals[0]
    init_ok = 1.0 if init_M >= 1.8 else 0.5 if init_M >= 1.5 else 0.0
    # combine
    return 0.4 * tc_score + 0.15 * mono_score + 0.15 * A_score + 0.15 * C_score + 0.15 * init_ok


# === block: score_1 (check id='phase_boundaries') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 50:
        return 0.0
    agent_points = []
    for r in rows:
        try:
            h = float(r['h_over_zJ'])
            t = float(r['T_over_zJ'])
            typ = r['transition_type'].strip()
        except (KeyError, ValueError):
            return 0.0
        agent_points.append((h, t, typ))
    refs = step['hidden']['reference_points']
    tol_h = step['hidden']['tolerance_h']
    tol_T = step['hidden']['tolerance_T']
    matched = 0
    for ref in refs:
        ref_h, ref_t, ref_type = ref['h_over_zJ'], ref['T_over_zJ'], ref['transition_type']
        for (ah, at, atyp) in agent_points:
            if abs(ah - ref_h) <= tol_h and abs(at - ref_t) <= tol_T and atyp == ref_type:
                matched += 1
                break
    ratio = matched / len(refs)
    return max(0.0, min(1.0, ratio / step['hidden']['min_matched_ratio']))


# === block: score_2 (check id='tricritical_points') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) != 2:
        return 0.0
    refs = step['hidden']['reference_points']
    tol = step['hidden']['tolerance']
    score = 0.0
    for ref in refs:
        ref_T, ref_h = ref['T_over_zJ'], ref['h_over_zJ']
        best_dist = float('inf')
        for r in rows:
            try:
                t = float(r['T_over_zJ'])
                h = float(r['h_over_zJ'])
            except (KeyError, ValueError):
                continue
            dist = math.sqrt(((t - ref_T) * 2) ** 2 + ((h - ref_h) * 2) ** 2)  # scale to give similar weight
            if dist < best_dist:
                best_dist = dist
        if best_dist <= tol:
            score += 0.5
    return score


_SCORERS = {
    'thermal_curves': score_0,
    'phase_boundaries': score_1,
    'tricritical_points': score_2,
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
