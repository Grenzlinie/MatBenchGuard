import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math

try:
    import numpy as np
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'])
    import numpy as np


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
    import csv, os, json
    import numpy as np

    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    order_path = '/app/outputs/order_params_p06.csv'
    if not os.path.exists(order_path):
        return {'T_peak_chi_T': None, 'T_peak_chi_6': None}
    rows = load_csv(order_path)
    T = np.array([float(r['T']) for r in rows])
    chi_T = np.array([float(r['chi_T']) for r in rows])
    chi_6 = np.array([float(r['chi_6']) for r in rows])
    T_peak_chi_T = float(T[np.argmax(chi_T)])
    T_peak_chi_6 = float(T[np.argmax(chi_6)])
    return {'T_peak_chi_T': T_peak_chi_T, 'T_peak_chi_6': T_peak_chi_6}


# === block: score_0 (check id='order_params_p06') ===
def score_0(artifact, step, ctx):
    import numpy as np

    T = np.array([float(r['T']) for r in artifact])
    psi_T = np.array([float(r['psi_T']) for r in artifact])
    chi_T = np.array([float(r['chi_T']) for r in artifact])
    psi_6 = np.array([float(r['psi_6']) for r in artifact])
    chi_6 = np.array([float(r['chi_6']) for r in artifact])

    T1 = float(T[np.argmax(chi_T)])
    T2 = float(T[np.argmax(chi_6)])
    sep = T2 - T1
    params = step.get('hidden_params', {})
    tol_sep = params.get('tolerance_separation_min', 0.00002)
    T_lo, T_hi = params.get('plausible_T_range', [0.0050, 0.0065])
    psi_T_drop = params.get('psi_T_drop_threshold', 0.1)
    psi_6_sustain = params.get('psi_6_sustain_threshold', 0.2)

    score = 0.0

    # 1) distinct peaks and separation
    if sep > tol_sep:
        score += 0.3
    elif sep > 0:
        score += 0.1

    # 2) T1 and T2 within plausible range
    both_in_range = (T_lo <= T1 <= T_hi) and (T_lo <= T2 <= T_hi)
    one_in_range = (T_lo <= T1 <= T_hi) or (T_lo <= T2 <= T_hi)
    if both_in_range:
        score += 0.3
    elif one_in_range:
        score += 0.15

    # 3) psi_T drops near T1 and psi_6 stays high until T2
    # find median psi_T after T1+2*tol_sep
    mask_after_T1 = T >= T1 + 2*tol_sep
    if np.any(mask_after_T1):
        avg_psi_T_after = np.mean(psi_T[mask_after_T1])
        if avg_psi_T_after < psi_T_drop:
            score += 0.2
    else:
        if T1 == max(T):  # can't evaluate
            pass

    # find median psi_6 in region between T1+sep/4 and T2
    mask_between = (T > T1 + sep*0.1) & (T < T2)
    if np.any(mask_between):
        avg_psi_6_between = np.mean(psi_6[mask_between])
        if avg_psi_6_between > psi_6_sustain:
            score += 0.2
    else:
        if T2 > T1 + sep:
            pass

    return min(score, 1.0)


# === block: score_1 (check id='ocf_data_p06') ===
def score_1(artifact, step, ctx):
    import numpy as np

    T_peak_chi_T = ctx.get('T_peak_chi_T')
    T_peak_chi_6 = ctx.get('T_peak_chi_6')
    if T_peak_chi_T is None or T_peak_chi_6 is None:
        return 0.0

    # group rows by T
    from collections import defaultdict
    groups = defaultdict(list)
    for row in artifact:
        T = float(row['T'])
        r = float(row['r'])
        h = float(row['h6(r)'])
        groups[T].append((r, h))

    # sort by T
    Ts = sorted(groups.keys())

    params = step.get('hidden_params', {})
    tail_r_min = params.get('tail_r_min', 3.0)
    eta_max = params.get('eta_max_hexatic', 0.25)

    # classify temperatures based on order_params peaks
    # solid: T < T_peak_chi_T - 0.00005, hexatic: T_peak_chi_T+0.00005 < T < T_peak_chi_6-0.00005, fluid: T > T_peak_chi_6+0.00005
    def classify(Tval):
        if Tval < T_peak_chi_T - 5e-5:
            return 'solid'
        elif T_peak_chi_T + 5e-5 < Tval < T_peak_chi_6 - 5e-5:
            return 'hexatic'
        elif Tval > T_peak_chi_6 + 5e-5:
            return 'fluid'
        else:
            return 'unknown'

    solid_pts = []
    hexatic_pts = []
    fluid_pts = []
    for Tval in Ts:
        cat = classify(Tval)
        if cat == 'solid':
            solid_pts.append(Tval)
        elif cat == 'hexatic':
            hexatic_pts.append(Tval)
        elif cat == 'fluid':
            fluid_pts.append(Tval)

    score = 0.0

    # at least one hexatic temperature where exponent < 0.25
    hexatic_ok = False
    for Tval in hexatic_pts:
        data = groups[Tval]
        r_vals = np.array([d[0] for d in data])
        h_vals = np.array([d[1] for d in data])
        mask = r_vals >= tail_r_min
        if np.sum(mask) < 4:
            continue
        r_tail = r_vals[mask]
        h_tail = h_vals[mask]
        if np.any(h_tail <= 0) or np.any(r_tail <= 0):
            continue
        log_r = np.log(r_tail)
        log_h = np.log(h_tail)
        slope, _ = np.polyfit(log_r, log_h, 1)
        eta = -slope
        if 0 < eta <= eta_max:
            hexatic_ok = True
            break

    if hexatic_ok:
        score += 0.5

    # at least one solid temperature with nearly flat (h >= 0.8 for r up to tail_r_min)
    solid_ok = False
    for Tval in solid_pts:
        data = groups[Tval]
        r_vals = np.array([d[0] for d in data])
        h_vals = np.array([d[1] for d in data])
        mask = r_vals <= tail_r_min
        if mask.sum() == 0:
            continue
        if np.mean(h_vals[mask]) > 0.8:
            solid_ok = True
            break
    if solid_ok:
        score += 0.2

    # at least one fluid temperature with exponential-like decay (h < 0.05 for r > tail_r_min)
    fluid_ok = False
    for Tval in fluid_pts:
        data = groups[Tval]
        r_vals = np.array([d[0] for d in data])
        h_vals = np.array([d[1] for d in data])
        mask = r_vals > tail_r_min
        if mask.sum() == 0:
            continue
        if np.max(h_vals[mask]) < 0.05:
            fluid_ok = True
            break
    if fluid_ok:
        score += 0.3

    return min(score, 1.0)


# === block: score_2 (check id='melting_line') ===
def score_2(artifact, step, ctx):
    import numpy as np

    # ctx contains T_peak_chi_T, T_peak_chi_6 from order_params
    T_peak_chi_T = ctx.get('T_peak_chi_T')
    T_peak_chi_6 = ctx.get('T_peak_chi_6')

    # parse melting_line artifact
    rows = artifact
    melting = {}
    for r in rows:
        P = r['P']
        T1 = r.get('T_solid_hexatic', '').strip()
        T2 = r.get('T_hexatic_fluid', '').strip()
        try:
            t1 = float(T1) if T1 != '' else None
        except:
            t1 = None
        try:
            t2 = float(T2) if T2 != '' else None
        except:
            t2 = None
        melting[P] = (t1, t2)

    params = step.get('hidden_params', {})
    tol_P6 = params.get('tolerance_P6', 0.0002)
    score = 0.0

    # 1) P=0.6 consistency with order_params
    if '0.6' in melting and T_peak_chi_T is not None and T_peak_chi_6 is not None:
        t1, t2 = melting['0.6']
        if t1 is not None and abs(t1 - T_peak_chi_T) <= tol_P6:
            score += 0.15
        if t2 is not None and abs(t2 - T_peak_chi_6) <= tol_P6:
            score += 0.15

    # 2) Monotonic ordering: T_solid_hexatic(0.05) < T_solid_hexatic(0.2) > T_solid_hexatic(0.6)
    vals = {}
    for P in ['0.05', '0.2', '0.6']:
        if P in melting:
            t1, _ = melting[P]
            if t1 is not None:
                vals[P] = t1
    if '0.05' in vals and '0.2' in vals and '0.6' in vals:
        if vals['0.2'] > vals['0.05'] and vals['0.2'] > vals['0.6']:
            score += 0.3
        elif vals['0.2'] > vals['0.05'] or vals['0.2'] > vals['0.6']:
            score += 0.15

    # 3) Hexatic-fluid present at P=0.2 and 0.6, may be missing at 0.05
    for P in ['0.2', '0.6']:
        if P in melting:
            t2 = melting[P][1]
            if t2 is not None:
                score += 0.1

    # bonus for P=0.05 hexatic-fluid missing or very close (indistinguishable)
    if '0.05' in melting:
        t1, t2 = melting['0.05']
        if t2 is None or (t1 is not None and t2 is not None and abs(t2-t1) < 0.0004):
            score += 0.1

    return min(score, 1.0)


# === block: score_3 (check id='structural_anomaly') ===
def score_3(artifact, step, ctx):
    import numpy as np

    rho = np.array([float(r['rho']) for r in artifact])
    S = np.array([float(r['S_pair']) for r in artifact])
    if len(rho) < 3:
        return 0.0

    # find maximum of S_pair
    idx = np.argmax(S)
    rho_max = rho[idx]
    S_max = S[idx]

    params = step.get('hidden_params', {})
    rho_lo, rho_hi = params.get('allowable_rho_range', [0.60, 0.85])

    score = 0.0
    # Check that maximum exists and is not at boundaries (optional)
    is_max_well_defined = (idx > 0 and idx < len(rho)-1) or (S_max > np.max(np.delete(S, idx)) if len(rho)>1 else True)

    if rho_lo <= rho_max <= rho_hi:
        score += 0.7
        if is_max_well_defined:
            score += 0.3
    else:
        # partial if within broader range
        if rho_max > 0.5 and rho_max < 1.0:
            score += 0.3

    return min(score, 1.0)


_SCORERS = {
    'order_params_p06': score_0,
    'ocf_data_p06': score_1,
    'melting_line': score_2,
    'structural_anomaly': score_3,
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
