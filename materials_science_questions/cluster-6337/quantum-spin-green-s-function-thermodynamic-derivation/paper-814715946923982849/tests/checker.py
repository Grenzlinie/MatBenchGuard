import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, pkgutil, importlib
if not pkgutil.find_loader('numpy'):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'numpy'],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
import numpy as np
import json
import os


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


# === block: score_0 (check id='fm_mag_vs_t') ===
def score_0(artifact, step, ctx):
    rows = sorted(artifact, key=lambda r: float(r['T']))
    Ts = np.array([float(r['T']) for r in rows])
    MTs = np.array([float(r['MT']) for r in rows])

    # Tc: temperature where MT drops below 1e-3
    idx = np.where(MTs < 1e-3)[0]
    if len(idx) == 0:
        Tc_agent = Ts[-1]
    else:
        Tc_agent = Ts[idx[0]]
    Tc_ref = step['params']['Tc_ref']
    Tc_tol = step['params']['Tc_tol']
    tc_ok = 1.0 if abs(Tc_agent - Tc_ref) <= Tc_tol else 0.0

    # zero-temperature magnetizations at lowest T
    min_idx = np.argmin(Ts)
    T_min = Ts[min_idx]
    if T_min > 0.1:
        zeroT_ok = 0.0
    else:
        zeroT_ref = step['params']['zeroT_ref']
        zeroT_tol = step['params']['zeroT_tol']
        fields = ['mc1','mc2','me1','me2','MT']
        vals = {f: float(rows[min_idx][f]) for f in fields}
        matches = all(abs(vals[f] - zeroT_ref[f]) <= zeroT_tol for f in fields)
        zeroT_ok = 1.0 if matches else 0.0

    score = 0.6 * tc_ok + 0.4 * zeroT_ok
    return float(score)


# === block: score_1 (check id='afm_mag_vs_t') ===
def score_1(artifact, step, ctx):
    rows = sorted(artifact, key=lambda r: float(r['T']))
    Ts = np.array([float(r['T']) for r in rows])
    MTs = np.array([float(r['MT']) for r in rows])
    Tc_ref = step['params']['Tc_ref']
    Tc_tol = step['params']['Tc_tol']
    # Tc
    idx = np.where(MTs < 1e-3)[0]
    if len(idx) == 0:
        Tc_agent = Ts[-1]
    else:
        Tc_agent = Ts[idx[0]]
    tc_ok = 1.0 if abs(Tc_agent - Tc_ref) <= Tc_tol else 0.0
    # zeroT
    min_idx = np.argmin(Ts)
    T_min = Ts[min_idx]
    zeroT_ref = step['params']['zeroT_ref']
    zeroT_tol = step['params']['zeroT_tol']
    fields = ['mc1','mc2','me1','me2','MT']
    vals = {f: float(rows[min_idx][f]) for f in fields}
    zeroT_ok = 1.0 if T_min <= 0.1 and all(abs(vals[f] - zeroT_ref[f]) <= zeroT_tol for f in fields) else 0.0
    return float(0.6 * tc_ok + 0.4 * zeroT_ok)


# === block: score_2 (check id='fm_hysteresis') ===
def score_2(artifact, step, ctx):
    ref_by_T = step['params']['coercive_ref_by_T']
    tol = step['params']['tol']
    T_set = {'1','2','3'}
    groups = {}
    for r in artifact:
        T = str(int(float(r['T'])))
        if T not in T_set:
            continue
        groups.setdefault(T, []).append((float(r['H']), float(r['MT'])))

    scores = []
    for T_str, pts in groups.items():
        pts.sort(key=lambda x: x[0])
        Hvals = np.array([p[0] for p in pts])
        Mvals = np.array([p[1] for p in pts])
        # find zero crossings
        signs = np.sign(Mvals)
        crossings = []
        for i in range(len(signs)-1):
            if signs[i] == 0 or signs[i+1] == 0 or signs[i]*signs[i+1] < 0:
                h_low, h_high = Hvals[i], Hvals[i+1]
                m_low, m_high = Mvals[i], Mvals[i+1]
                if m_high != m_low:
                    h_cross = h_low - m_low * (h_high - h_low) / (m_high - m_low)
                else:
                    h_cross = (h_low + h_high)/2.0
                crossings.append(abs(h_cross))
        if not crossings:
            scores.append(0.0)
            continue
        Hc_agent = min(crossings)  # smallest absolute H crossing
        Hc_ref = ref_by_T.get(T_str, None)
        if Hc_ref is None:
            scores.append(0.0)
        else:
            scores.append(1.0 if abs(Hc_agent - Hc_ref) <= tol else 0.0)
    if not scores:
        return 0.0
    return float(sum(scores) / len(scores))


# === block: score_3 (check id='afm_hysteresis') ===
def score_3(artifact, step, ctx):
    T_target = step['params']['T']
    ref_vals = step['params']['coercive_ref']
    tol = step['params']['tol']
    pts = []
    for r in artifact:
        if abs(float(r['T']) - T_target) < 0.01:
            pts.append((float(r['H']), float(r['MT'])))
    if len(pts) < 10:
        return 0.0
    pts.sort(key=lambda x: x[0])
    Hvals = np.array([p[0] for p in pts])
    Mvals = np.array([p[1] for p in pts])
    signs = np.sign(Mvals)
    crossings = []
    for i in range(len(signs)-1):
        if signs[i] == 0 or signs[i+1] == 0 or signs[i]*signs[i+1] < 0:
            h_low, h_high = Hvals[i], Hvals[i+1]
            m_low, m_high = Mvals[i], Mvals[i+1]
            if m_high != m_low:
                h_cross = h_low - m_low * (h_high - h_low) / (m_high - m_low)
            else:
                h_cross = (h_low + h_high)/2.0
            crossings.append(abs(h_cross))
    crossings = sorted(set(round(c, 5) for c in crossings))
    matches = 0
    for key, ref in ref_vals.items():
        for c in crossings:
            if abs(c - ref) <= tol:
                matches += 1
                break
    return float(matches / len(ref_vals))


# === block: score_4 (check id='afm_central_t1') ===
def score_4(artifact, step, ctx):
    pts = [(float(r['H']), float(r['mc1']), float(r['mc2'])) for r in artifact]
    if len(pts) < 20:
        return 0.0
    pts.sort(key=lambda x: x[0])
    Hvals = np.array([p[0] for p in pts])
    mc1 = np.array([p[1] for p in pts])
    mc2 = np.array([p[2] for p in pts])

    # Use absolute magnetization magnitude for central atoms: |mc1|+|mc2|/2
    mag = (np.abs(mc1) + np.abs(mc2)) / 2.0

    # coercive fields from mag crossing zero (sign change)
    signs = np.sign(mc1)  # use mc1 sign changes
    ref_coer = step['params']['coercive_ref']
    tol = step['params']['tol']
    crossings = []
    for i in range(len(signs)-1):
        if signs[i] == 0 or signs[i+1] == 0 or signs[i]*signs[i+1] < 0:
            h_low, h_high = Hvals[i], Hvals[i+1]
            m_low, m_high = mc1[i], mc1[i+1]
            if m_high != m_low:
                h_cross = h_low - m_low * (h_high - h_low) / (m_high - m_low)
            else:
                h_cross = (h_low + h_high)/2.0
            crossings.append(abs(h_cross))
    crossings = sorted(set(round(c, 5) for c in crossings))
    coer_match = 0
    for key, ref in ref_coer.items():
        for c in crossings:
            if abs(c - ref) <= tol:
                coer_match += 1
                break
    coer_score = coer_match / len(ref_coer) if len(ref_coer) > 0 else 0.0

    # peak effect
    H_range = step['params']['peak_effect_H_range']
    H_min, H_max = H_range[0], H_range[1]
    mask = (Hvals >= H_min) & (Hvals <= H_max)
    if np.sum(mask) < 4:
        peak_score = 0.0
    else:
        dM = np.abs(np.gradient(mag, Hvals))
        region_dM = dM[mask]
        region_H = Hvals[mask]
        max_idx = np.argmax(region_dM)
        peak_H = region_H[max_idx]
        margin = 0.02
        left_mask = (Hvals >= H_min) & (Hvals <= H_min + margin)
        right_mask = (Hvals >= H_max - margin) & (Hvals <= H_max)
        if np.sum(left_mask) > 0 and np.sum(right_mask) > 0:
            left_val = np.max(dM[left_mask])
            right_val = np.max(dM[right_mask])
            if region_dM[max_idx] > left_val and region_dM[max_idx] > right_val:
                peak_score = 1.0
            else:
                peak_score = 0.0
        else:
            peak_score = 0.0

    score = 0.5 * coer_score + 0.5 * peak_score
    return float(score)


# === block: score_5 (check id='fm_extracted') ===
def score_5(artifact, step, ctx):
    data = artifact
    Tc_ref = step['params']['Tc_ref']
    Tc_tol = step['params']['Tc_tol']
    zeroT_ref = step['params']['zeroT_ref']
    zeroT_tol = step['params']['zeroT_tol']
    coer_ref = step['params']['coercive_ref']
    coer_tol = step['params']['coercive_tol']
    remanence_expected = step['params']['remanence_expected']

    score = 0.0
    checks = []
    # Tc
    if 'Tc' in data and isinstance(data['Tc'], (int,float)):
        checks.append(1.0 if abs(float(data['Tc']) - Tc_ref) <= Tc_tol else 0.0)
    else:
        checks.append(0.0)
    # zeroT
    if 'zeroT_magnetizations' in data and isinstance(data['zeroT_magnetizations'], dict):
        zt = data['zeroT_magnetizations']
        fields = ['mc1','mc2','me1','me2','MT']
        ok = all(f in zt and abs(float(zt[f]) - zeroT_ref[f]) <= zeroT_tol for f in fields)
        checks.append(1.0 if ok else 0.0)
    else:
        checks.append(0.0)
    # coercive fields
    coer_keys = ['coercive_fields_T1','coercive_fields_T2','coercive_fields_T3']
    coer_map = {'coercive_fields_T1':'T1','coercive_fields_T2':'T2','coercive_fields_T3':'T3'}
    for k in coer_keys:
        if k in data and isinstance(data[k], (int,float)):
            checks.append(1.0 if abs(float(data[k]) - coer_ref[coer_map[k]]) <= coer_tol else 0.0)
        else:
            checks.append(0.0)
    # remanence
    if 'remanence_central_greater_than_edge' in data and isinstance(data['remanence_central_greater_than_edge'], bool):
        checks.append(1.0 if data['remanence_central_greater_than_edge'] == remanence_expected else 0.0)
    else:
        checks.append(0.0)
    if not checks:
        return 0.0
    return float(sum(checks) / len(checks))


# === block: score_6 (check id='afm_extracted') ===
def score_6(artifact, step, ctx):
    data = artifact
    Tc_ref = step['params']['Tc_ref']
    Tc_tol = step['params']['Tc_tol']
    zeroT_ref = step['params']['zeroT_ref']
    zeroT_tol = step['params']['zeroT_tol']
    total_ref = step['params']['coercive_total_T1_ref']
    central_ref = step['params']['coercive_central_T1_ref']
    coer_tol = step['params']['coercive_tol']
    peak_expected = step['params']['peak_effect_expected']

    checks = []
    # Tc
    if 'Tc' in data and isinstance(data['Tc'], (int,float)):
        checks.append(1.0 if abs(float(data['Tc']) - Tc_ref) <= Tc_tol else 0.0)
    else:
        checks.append(0.0)
    # zeroT
    if 'zeroT_magnetizations' in data and isinstance(data['zeroT_magnetizations'], dict):
        zt = data['zeroT_magnetizations']
        fields = ['mc1','mc2','me1','me2','MT']
        ok = all(f in zt and abs(float(zt[f]) - zeroT_ref[f]) <= zeroT_tol for f in fields)
        checks.append(1.0 if ok else 0.0)
    else:
        checks.append(0.0)
    # coercive total
    if 'coercive_fields_total_T1' in data and isinstance(data['coercive_fields_total_T1'], dict):
        ct = data['coercive_fields_total_T1']
        tk = ['Hc1','Hc2','Hc3']
        ok = all(k in ct and abs(float(ct[k]) - total_ref[k]) <= coer_tol for k in tk)
        checks.append(1.0 if ok else 0.0)
    else:
        checks.append(0.0)
    # coercive central
    if 'coercive_fields_central_T1' in data and isinstance(data['coercive_fields_central_T1'], dict):
        cc = data['coercive_fields_central_T1']
        ok = all(k in cc and abs(float(cc[k]) - central_ref[k]) <= coer_tol for k in tk)
        checks.append(1.0 if ok else 0.0)
    else:
        checks.append(0.0)
    # peak effect
    if 'peak_effect_present_T1' in data and isinstance(data['peak_effect_present_T1'], bool):
        checks.append(1.0 if data['peak_effect_present_T1'] == peak_expected else 0.0)
    else:
        checks.append(0.0)
    if not checks:
        return 0.0
    return float(sum(checks) / len(checks))


_SCORERS = {
    'fm_mag_vs_t': score_0,
    'afm_mag_vs_t': score_1,
    'fm_hysteresis': score_2,
    'afm_hysteresis': score_3,
    'afm_central_t1': score_4,
    'fm_extracted': score_5,
    'afm_extracted': score_6,
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
