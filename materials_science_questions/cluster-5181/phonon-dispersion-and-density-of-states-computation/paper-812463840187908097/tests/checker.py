import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.constants import h, e
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
        N = 500
        a = 1.5e-10
        v = 2500.0
        factor = (3*N/(4*np.pi))**(1/3) - 0.5
        V = (4/3)*np.pi * factor**3 * a**3
        omega_L_m = (np.pi/2) * v * (4*np.pi/(3*V))**(1/3)
        omega_U_m = v * (2*np.pi**2 * (3*N - 6 + np.pi**2/12) / V)**(1/3)
        U_zero_m = (3/16) * V * h / (np.pi**2 * v**3) * (omega_U_m**4 - omega_L_m**4) / e
        ref_monomer = {'V': V, 'omega_L': omega_L_m, 'omega_U': omega_U_m, 'U_zero': U_zero_m}
        V_d = 2*V
        N_d = 1000
        omega_L_d = (np.pi/2) * v * (4*np.pi/(3*V_d))**(1/3)
        omega_U_d = v * (2*np.pi**2 * (3*N_d - 6 + np.pi**2/12) / V_d)**(1/3)
        U_zero_d = (3/16) * V_d * h / (np.pi**2 * v**3) * (omega_U_d**4 - omega_L_d**4) / e
        ref_dimer = {'V': V_d, 'omega_L': omega_L_d, 'omega_U': omega_U_d, 'U_zero': U_zero_d}
        delta_u_zero_base = U_zero_d - 2*U_zero_m
        v_hv = 2625.0
        omega_L_d_hv = (np.pi/2) * v_hv * (4*np.pi/(3*V_d))**(1/3)
        omega_U_d_hv = v_hv * (2*np.pi**2 * (3*N_d - 6 + np.pi**2/12) / V_d)**(1/3)
        U_zero_d_hv = (3/16) * V_d * h / (np.pi**2 * v_hv**3) * (omega_U_d_hv**4 - omega_L_d_hv**4) / e
        delta_u_zero_hv = U_zero_d_hv - 2*U_zero_m
        V_chain = V
        omega_L_1d = np.pi * v / (N*a)
        omega_U_1d = np.pi * (3*N - 6) * v / (3*N*a)
        U_zero_1d = (3 * V_chain * h / (4 * np.pi * v * a**2)) * (omega_U_1d**2 - omega_L_1d**2) / e
        ref_chain = {'omega_L': omega_L_1d, 'omega_U': omega_U_1d, 'U_zero': U_zero_1d}
        return {
            'ref_monomer': ref_monomer,
            'ref_dimer': ref_dimer,
            'ref_dim_u_zero': delta_u_zero_base,
            'ref_dim_u_zero_hv': delta_u_zero_hv,
            'ref_chain': ref_chain
        }


# === block: score_0 (check id='monomer') ===
def score_0(artifact, step, ctx):
        N = 500
        a = 1.5e-10
        v = 2500.0
        factor = (3*N/(4*np.pi))**(1/3) - 0.5
        V = (4/3)*np.pi * factor**3 * a**3
        omega_L = (np.pi/2) * v * (4*np.pi/(3*V))**(1/3)
        omega_U = v * (2*np.pi**2 * (3*N - 6 + np.pi**2/12) / V)**(1/3)
        U_zero = (3/16) * V * h / (np.pi**2 * v**3) * (omega_U**4 - omega_L**4) / e
        ref = {'V': V, 'omega_L': omega_L, 'omega_U': omega_U, 'U_zero': U_zero}
        ad = artifact.get('spherical_monomer', {})

        def to_float(x):
            if isinstance(x, str):
                try:
                    return float(x)
                except (ValueError, TypeError):
                    return None
            if isinstance(x, (int, float)):
                return x
            return None

        def check(val, ref_val, rel_tol, abs_tol):
            v = to_float(val)
            if v is None or not math.isfinite(v):
                return False
            if abs(v - ref_val) <= rel_tol * abs(ref_val):
                return True
            if abs_tol is not None and abs(v - ref_val) <= abs_tol:
                return True
            return False

        checks = [
            ('omega_L', ad.get('omega_L'), ref['omega_L'], 0.01, None),
            ('omega_U', ad.get('omega_U'), ref['omega_U'], 0.01, None),
            ('V',       ad.get('V'),       ref['V'],       0.01, 1e-28),
            ('U_zero',  ad.get('U_zero'),  ref['U_zero'],  0.05, 0.1)
        ]
        passes = sum(1 for _, val, ref_val, rel_tol, abs_tol in checks if check(val, ref_val, rel_tol, abs_tol))
        return passes / 4.0


# === block: score_1 (check id='dimer') ===
def score_1(artifact, step, ctx):
        ref = ctx['ref_dimer']
        ad = artifact.get('spherical_dimer', {})
        checks = {
            'omega_L': (ad.get('omega_L'), ref['omega_L'], 0.01),
            'omega_U': (ad.get('omega_U'), ref['omega_U'], 0.01),
            'V': (ad.get('V'), ref['V'], 0.01),
            'U_zero': (ad.get('U_zero'), ref['U_zero'], 0.05)
        }
        passes = 0
        for name, (val, ref_val, rel_tol) in checks.items():
            if val is None or not isinstance(val, (int, float)) or not math.isfinite(val):
                continue
            if ref_val != 0 and abs(val - ref_val) / abs(ref_val) <= rel_tol:
                passes += 1
        return passes / len(checks)


# === block: score_2 (check id='dim_baseline') ===
def score_2(artifact, step, ctx):
        data = artifact.get('dimerization', {})
        if not data:
            return 0.0
        delta_u_zero = data.get('Delta_U_zero')
        if delta_u_zero is None or not math.isfinite(delta_u_zero):
            return 0.0
        ref_duz = ctx['ref_dim_u_zero']
        duz_score = 1.0 if abs(delta_u_zero - ref_duz) <= 0.1*abs(ref_duz) else 0.0
        arr = data.get('Delta_U_temperature_dependent')
        if not isinstance(arr, list) or len(arr) != 4:
            return duz_score * 0.5
        expected_Ts = [0,100,200,300]
        arr_cons = 0
        sign_ok = True
        for i, entry in enumerate(arr):
            if entry.get('T') != expected_Ts[i]:
                break
            U_mono = entry.get('U_mono')
            U_dimer = entry.get('U_dimer')
            Delta_U = entry.get('Delta_U')
            if None in (U_mono, U_dimer, Delta_U) or not all(isinstance(v, (int,float)) and math.isfinite(v) for v in (U_mono, U_dimer, Delta_U)):
                continue
            expected = U_dimer - 2*U_mono + delta_u_zero
            if abs(Delta_U - expected) < 1e-6:
                arr_cons += 1
            if Delta_U > 0:
                sign_ok = False
        arr_cons_score = arr_cons / 4.0
        sign_score = 1.0 if sign_ok else 0.0
        return duz_score*0.5 + arr_cons_score*0.3 + sign_score*0.2


# === block: score_3 (check id='dim_higher_v') ===
def score_3(artifact, step, ctx):
        data = artifact.get('dimerization_5pct_higher_v', {})
        if not data:
            return 0.0
        delta_u_zero = data.get('Delta_U_zero')
        if delta_u_zero is None or not math.isfinite(delta_u_zero):
            return 0.0
        ref_duz = ctx['ref_dim_u_zero_hv']
        duz_score = 1.0 if abs(delta_u_zero - ref_duz) <= 0.1*abs(ref_duz) else 0.0
        arr = data.get('Delta_U_temperature_dependent')
        if not isinstance(arr, list) or len(arr) != 4:
            return duz_score * 0.5
        expected_Ts = [0,100,200,300]
        arr_cons = 0
        sign_ok = True
        for i, entry in enumerate(arr):
            if entry.get('T') != expected_Ts[i]:
                break
            U_mono = entry.get('U_mono')
            U_dimer = entry.get('U_dimer')
            Delta_U = entry.get('Delta_U')
            if None in (U_mono, U_dimer, Delta_U) or not all(isinstance(v, (int,float)) and math.isfinite(v) for v in (U_mono, U_dimer, Delta_U)):
                continue
            expected = U_dimer - 2*U_mono + delta_u_zero
            if abs(Delta_U - expected) < 1e-6:
                arr_cons += 1
            if Delta_U < 0:
                sign_ok = False
        arr_cons_score = arr_cons / 4.0
        sign_score = 1.0 if sign_ok else 0.0
        return duz_score*0.5 + arr_cons_score*0.3 + sign_score*0.2


# === block: score_4 (check id='chain_1d') ===
def score_4(artifact, step, ctx):
        ref = ctx['ref_chain']
        ad = artifact.get('oneD_chain', {})
        checks = {
            'omega_L': (ad.get('omega_L'), ref['omega_L'], 0.01),
            'omega_U': (ad.get('omega_U'), ref['omega_U'], 0.01),
            'U_zero': (ad.get('U_zero'), ref['U_zero'], 0.05)
        }
        passes = 0
        for name, (val, ref_val, rel_tol) in checks.items():
            if val is None or not isinstance(val, (int, float)) or not math.isfinite(val):
                continue
            if ref_val != 0 and abs(val - ref_val) / abs(ref_val) <= rel_tol:
                passes += 1
        return passes / len(checks)


_SCORERS = {
    'monomer': score_0,
    'dimer': score_1,
    'dim_baseline': score_2,
    'dim_higher_v': score_3,
    'chain_1d': score_4,
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
