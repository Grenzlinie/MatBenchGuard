import os
import json
import csv

# === author imports / helpers ===
import sys, subprocess

def _ensure(package):
    try:
        __import__(package)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', package])

_ensure('numpy')
_ensure('scipy')

import numpy as np
from scipy.optimize import curve_fit


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


# === block: score_0 (check id='step3_lattice') ===
def score_0(artifact, step, ctx):
    import csv, os
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader]
    if not rows or not all(col in rows[0] for col in ['phase','a_Angstrom','c_Angstrom','c_a_ratio']):
        return 0.0
    expected = {
        'fcc': {'a': 15.50, 'c': None, 'c_a_ratio': None},
        'hex1': {'a': 10.50, 'c': 18.42, 'c_a_ratio': 1.754},
        'hex2': {'a': 10.93, 'c': 17.50, 'c_a_ratio': 1.601}
    }
    tols = {'a': 0.15, 'c': 0.2, 'c_a_ratio': 0.03}
    weight_phase = {'fcc': 0.5, 'hex2': 0.4, 'hex1': 0.1}
    def score_val(exp, val, tol):
        if val is None or val == '' or exp is None:
            return 0.0
        try:
            diff = abs(float(val) - exp)
        except:
            return 0.0
        return max(0.0, 1.0 - diff / tol)
    total = 0.0
    for row in rows:
        phase = row['phase'].strip()
        if phase not in expected:
            continue
        exp = expected[phase]
        wt = weight_phase.get(phase, 0.0)
        scores = []
        a_val = row.get('a_Angstrom')
        c_val = row.get('c_Angstrom')
        ca_val = row.get('c_a_ratio')
        scores.append(score_val(exp['a'], a_val, tols['a']))
        if exp['c'] is not None:
            scores.append(score_val(exp['c'], c_val, tols['c']))
            scores.append(score_val(exp['c_a_ratio'], ca_val, tols['c_a_ratio']))
        else:
            # fcc: ignore c and ratio, only a scored
            pass
        total += wt * (np.mean(scores) if scores else 0)
    return min(total, 1.0)


# === block: score_1 (check id='step4_ca_ratio') ===
def score_1(artifact, step, ctx):
    import csv, os
    import numpy as np
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader]
    if not rows or not all(col in rows[0] for col in ['phase','T_K','c_a_ratio']):
        return 0.0
    data_by_phase = {}
    for r in rows:
        phase = r['phase'].strip()
        T = float(r['T_K'])
        ca = float(r['c_a_ratio'])
        data_by_phase.setdefault(phase, []).append((T, ca))
    for phase in data_by_phase:
        data_by_phase[phase].sort(key=lambda x: x[0])
    expected = {
        'hex2': {'onset': 500.0, 'sat': 350.0, 'high_plat': 1.633, 'low_plat': 1.599, 'direction': 'decrease'},
        'hex1': {'onset': 400.0, 'sat': 100.0, 'high_plat': 1.633, 'low_plat': 1.673, 'direction': 'increase'}
    }
    weight_phase = {'hex2': 0.6, 'hex1': 0.4}
    def score_temperature(T_detected, T_expected, tol=40):
        diff = abs(T_detected - T_expected)
        return max(0.0, 1.0 - diff / tol)
    def smooth(y, window=5):
        if window >= len(y):
            return y
        kernel = np.ones(window)/window
        return np.convolve(y, kernel, mode='same')
    def detect_transitions(Ts, cas, direction, eps=0.01):
        cas_sm = smooth(cas, window=5)
        T_onset = None
        T_sat = None
        if direction == 'decrease':
            for i in range(len(Ts)):
                if cas_sm[i] < 1.633 - eps and T_onset is None:
                    T_onset = Ts[i]
                if cas_sm[i] < 1.599 + eps and T_onset is not None and T_sat is None:
                    T_sat = Ts[i]
        else:
            for i in range(len(Ts)):
                if cas_sm[i] > 1.633 + eps and T_onset is None:
                    T_onset = Ts[i]
                if cas_sm[i] > 1.673 - eps and T_onset is not None and T_sat is None:
                    T_sat = Ts[i]
        return T_onset, T_sat
    total = 0.0
    for phase, exp in expected.items():
        if phase not in data_by_phase:
            continue
        Ts, cas = zip(*data_by_phase[phase])
        Ts = np.array(Ts)
        cas = np.array(cas)
        T_onset, T_sat = detect_transitions(Ts, cas, exp['direction'])
        score_phase = 0.0
        if T_onset is not None and T_sat is not None:
            s_on = score_temperature(T_onset, exp['onset'], tol=40)
            s_sat = score_temperature(T_sat, exp['sat'], tol=40)
            score_phase = 0.4*s_on + 0.4*s_sat
        # plateau checks
        T_high = np.max(Ts)
        T_low = np.min(Ts)
        ca_high = cas[np.argmax(Ts)]
        ca_low = cas[np.argmin(Ts)]
        s_ph = 1.0 if abs(ca_high - exp['high_plat']) <= 0.02 else max(0.0, 1.0 - abs(ca_high - exp['high_plat'])/0.04)
        s_pl = 1.0 if abs(ca_low - exp['low_plat']) <= 0.02 else max(0.0, 1.0 - abs(ca_low - exp['low_plat'])/0.04)
        score_phase += 0.1*s_ph + 0.1*s_pl
        total += weight_phase[phase] * score_phase
    return min(total, 1.0)


# === block: score_2 (check id='step5_potential_energy') ===
def score_2(artifact, step, ctx):
    import csv, os
    import numpy as np
    from scipy.optimize import curve_fit
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader]
    if not rows or not all(col in rows[0] for col in ['phase','T_K','potential_energy_per_mol_J']):
        return 0.0
    data_by_phase = {}
    for r in rows:
        phase = r['phase'].strip()
        T = float(r['T_K'])
        E = float(r['potential_energy_per_mol_J'])
        data_by_phase.setdefault(phase, []).append((T, E))
    for phase in data_by_phase:
        data_by_phase[phase].sort(key=lambda x: x[0])
    def piecewise_linear(x, a1, b1, a2, b2, x0):
        return np.where(x < x0, a1*x + b1, a2*x + b2)
    def fit_breakpoint(Ts, Es):
        idx = len(Ts)//2
        x0_guess = Ts[idx]
        popt, _ = curve_fit(piecewise_linear, Ts, Es, p0=[0.0, np.mean(Es[:idx]), 0.0, np.mean(Es[idx:]), x0_guess], maxfev=10000)
        return popt[-1]
    def score_temperature(T_detected, T_expected, tol=40):
        diff = abs(T_detected - T_expected)
        return max(0.0, 1.0 - diff / tol)
    weight_phase = {'fcc': 0.5, 'hex2': 0.3, 'hex1': 0.2}
    total = 0.0
    # fcc
    if 'fcc' in data_by_phase:
        Ts, Es = zip(*data_by_phase['fcc'])
        Ts = np.array(Ts)
        Es = np.array(Es)
        try:
            T0 = fit_breakpoint(Ts, Es)
            score_fcc = score_temperature(T0, 200.0, tol=40)
        except:
            score_fcc = 0.0
        total += weight_phase['fcc'] * score_fcc
    # hex2
    if 'hex2' in data_by_phase:
        Ts, Es = zip(*data_by_phase['hex2'])
        Ts = np.array(Ts)
        Es = np.array(Es)
        high_mask = Ts > 500
        mid_mask = (Ts >= 350) & (Ts <= 500)
        low_mask = Ts < 350
        slopes = []
        for mask in [high_mask, mid_mask, low_mask]:
            if np.sum(mask) >= 2:
                fit = np.polyfit(Ts[mask], Es[mask], 1)
                slopes.append(fit[0])
            else:
                slopes.append(np.nan)
        score_hex2 = 0.0
        if len(slopes)==3 and not np.isnan(slopes[1]):
            if slopes[1] < -0.01 and abs(slopes[0]) < 0.1 and abs(slopes[2]) < 0.1:
                score_hex2 = 1.0
            elif slopes[1] < -0.005:
                score_hex2 = 0.5
        total += weight_phase['hex2'] * score_hex2
    # hex1
    if 'hex1' in data_by_phase:
        Ts, Es = zip(*data_by_phase['hex1'])
        Ts = np.array(Ts)
        Es = np.array(Es)
        high_mask = Ts > 400
        mid_mask = (Ts >= 100) & (Ts <= 400)
        low_mask = Ts < 100
        slopes = []
        for mask in [high_mask, mid_mask, low_mask]:
            if np.sum(mask) >= 2:
                fit = np.polyfit(Ts[mask], Es[mask], 1)
                slopes.append(fit[0])
            else:
                slopes.append(np.nan)
        score_hex1 = 0.0
        if len(slopes)==3 and not np.isnan(slopes[1]):
            if abs(slopes[1]) > max(abs(slopes[0]) if not np.isnan(slopes[0]) else 0, abs(slopes[2]) if not np.isnan(slopes[2]) else 0) + 0.01:
                score_hex1 = 1.0
            else:
                score_hex1 = 0.5
        total += weight_phase['hex1'] * score_hex1
    return min(total, 1.0)


_SCORERS = {
    'step3_lattice': score_0,
    'step4_ca_ratio': score_1,
    'step5_potential_energy': score_2,
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
