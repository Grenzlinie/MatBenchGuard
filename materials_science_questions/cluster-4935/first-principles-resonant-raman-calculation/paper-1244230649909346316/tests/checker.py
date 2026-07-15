import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import os
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


# === block: score_0 (check id='step_02_dsf') ===
def score_0(artifact, step, ctx):
    import numpy as np
    import os

    def find_lowest_energy_peak(omega, S, threshold_frac=0.1):
        """Return frequency of the lowest-energy peak in S above a fraction of global max."""
        if len(omega) < 3:
            return None
        omega = np.asarray(omega, dtype=float)
        S = np.asarray(S, dtype=float)
        maxS = np.max(S)
        if maxS <= 0:
            return None
        threshold = threshold_frac * maxS
        for i in range(1, len(omega)-1):
            if S[i] > S[i-1] and S[i] > S[i+1] and S[i] > threshold:
                return omega[i]
        return None

    artifact_csv = artifact   # artifact is list of dicts from CSV
    npz_path = os.path.join('/app/outputs', 'dsf_M_curves.npz')
    if not os.path.exists(npz_path):
        return 0.0
    try:
        data = np.load(npz_path, allow_pickle=True)
        J3_vals = data['J3_vals'].tolist()
        curves = data['curves'].tolist()  # list of dicts
    except Exception:
        return 0.0
    # Build dict J3->(omega,S) 
    npz_gaps = {}
    for j, curve in zip(J3_vals, curves):
        omega = np.asarray(curve['omega'], dtype=float)
        S = np.asarray(curve['S'], dtype=float)
        if len(omega) < 3 or len(S) < 3:
            continue
        gap = find_lowest_energy_peak(omega, S)
        if gap is not None:
            npz_gaps[j] = gap
    # Build CSV dict
    csv_gaps = {}
    for row in artifact_csv:
        try:
            j3 = float(row['J3'])
            gap = float(row['gap_energy'])
        except (ValueError, KeyError):
            continue
        csv_gaps[j3] = gap
    if not npz_gaps:
        return 0.0
    # Consistency: compare common J3
    common = set(npz_gaps.keys()) & set(csv_gaps.keys())
    if not common:
        consist_score = 0.0
    else:
        tol = step.get('tolerances', {}).get('gap_consistency_abs', 0.008)
        matches = [abs(npz_gaps[j] - csv_gaps[j]) <= tol for j in common]
        consist_score = sum(matches) / len(matches)
    # Monotonic: check gaps from npz_gaps sorted by J3
    sorted_keys = sorted(npz_gaps.keys())
    gaps_sorted = [npz_gaps[k] for k in sorted_keys]
    eps = step.get('tolerances', {}).get('monotonic_epsilon', 0.0005)
    mono_violations = any(gaps_sorted[i] - gaps_sorted[i+1] > eps for i in range(len(gaps_sorted)-1))
    mono_score = 0.0 if mono_violations else 1.0
    # Gap closure at largest J3
    max_j3 = max(npz_gaps.keys(), key=float)
    gap_maxJ3 = npz_gaps[max_j3]
    closure_max = step.get('tolerances', {}).get('gap_closure_max', 0.01)
    closure_score = 1.0 if gap_maxJ3 <= closure_max else 0.0
    # Combine: consist*0.4 + mono*0.3 + closure*0.3
    score = 0.4*consist_score + 0.3*mono_score + 0.3*closure_score
    return float(min(max(score, 0.0), 1.0))


# === block: score_1 (check id='step_03_raman') ===
def score_1(artifact, step, ctx):
    import numpy as np
    rows = artifact  # list of dicts
    omegas = []
    I_total = []
    I_2v = []
    I_4v = []
    for row in rows:
        try:
            omegas.append(float(row['omega']))
            I_total.append(float(row['I_total']))
            I_2v.append(float(row['I_2v']))
            I_4v.append(float(row['I_4v']))
        except (ValueError, KeyError):
            continue
    if len(omegas) < 2:
        return 0.0
    omega = np.array(omegas)
    I_4v_arr = np.array(I_4v)
    I_2v_arr = np.array(I_2v)
    # 1) I_4v peak position
    idx4 = np.argmax(I_4v_arr)
    peak4 = omega[idx4]
    peak_range = step.get('tolerances', {}).get('peak_4v_range', [0.39, 0.49])
    peak_ok = 1.0 if peak_range[0] <= peak4 <= peak_range[1] else 0.0
    # 2) I_2v onset and peak
    max2 = np.max(I_2v_arr)
    if max2 <= 0:
        return 0.0
    onset_frac = 0.05
    idx_onset = None
    for i in range(len(I_2v_arr)):
        if I_2v_arr[i] > onset_frac * max2:
            idx_onset = i
            break
    if idx_onset is None:
        return 0.0
    onset_omega = omega[idx_onset]
    onset_min = step.get('tolerances', {}).get('onset_2v_min', 0.25)
    onset_ok = 1.0 if onset_omega >= onset_min else 0.0
    # 3) I_2v max omega
    idx_max2 = np.argmax(I_2v_arr)
    max2_omega = omega[idx_max2]
    max2_min = step.get('tolerances', {}).get('max_2v_omega_min', 1.5)
    max2_ok = 1.0 if max2_omega >= max2_min else 0.0
    # 4) Shape: from onset to max should be increasing (slope > 0)
    if idx_onset >= idx_max2:
        shape_ok = 0.0
    else:
        seg = I_2v_arr[idx_onset:idx_max2+1]
        # simple check: max occurs after onset and values never drop below onset value
        if np.min(seg) >= I_2v_arr[idx_onset] * 0.8:
            shape_ok = 1.0
        else:
            shape_ok = 0.0
    score = 0.4*peak_ok + 0.3*onset_ok + 0.2*max2_ok + 0.1*shape_ok
    return float(min(max(score, 0.0), 1.0))


_SCORERS = {
    'step_02_dsf': score_0,
    'step_03_raman': score_1,
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
