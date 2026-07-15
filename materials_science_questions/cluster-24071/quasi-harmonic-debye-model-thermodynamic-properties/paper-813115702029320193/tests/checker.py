import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math
import subprocess
import sys

def _ensure_numpy_and_scipy():
    try:
        import numpy
        from scipy.optimize import curve_fit
    except ImportError:
        subprocess.check_call([
            sys.executable, '-m', 'pip', '-q', 'install', '--no-cache-dir',
            '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple',
            'numpy', 'scipy'
        ])
        import numpy
        from scipy.optimize import curve_fit
    return numpy, curve_fit

_np, _curve_fit = _ensure_numpy_and_scipy()
import numpy as np  # now available
from scipy.optimize import curve_fit  # now available


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


# === block: score_0 (check id='step5_results') ===
def score_0(artifact, step, ctx):
        # multi-stage recompute scorer
        output_dir = '/app/outputs'
        w_eos = 0.20
        w_el0 = 0.15
        w_moduli = 0.15
        w_thermo = 0.25
        w_pressure = 0.15
        w_stability = 0.05
        w_bcons = 0.05
        ref = step.get('ref_values', {})
        tols = step.get('tolerances', {})

        def rel_err(val, ref, tol_type):
            if ref == 0:
                return abs(val) < 1e-6
            return abs(val - ref) / abs(ref) <= tol_type

        def murnaghan(V, V0, B0, B0p, E0):
            if B0p == 1:
                return E0 + B0*V0*np.log(V/V0) - B0*(V-V0)
            return E0 + (B0*V/(B0p)) * ( (V0/V)**B0p / (B0p-1) + 1 ) - B0*V0/(B0p-1)

        # --- EOS fitting ---
        eos_score = 0.0
        B0_fit = None
        try:
            csv_file = os.path.join(output_dir, 'e_v.csv')
            if os.path.isfile(csv_file):
                with open(csv_file) as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                col_map = {}
                for key in rows[0].keys():
                    k_lower = key.lower().strip()
                    if k_lower in ('volume', 'v'):
                        col_map['V'] = key
                    elif k_lower in ('energy', 'e', 'total_energy'):
                        col_map['E'] = key
                if 'V' in col_map and 'E' in col_map:
                    V_arr = np.array([float(r[col_map['V']]) for r in rows])
                    E_arr = np.array([float(r[col_map['E']]) for r in rows])
                    idx_min = np.argmin(E_arr)
                    V0_guess = V_arr[idx_min]
                    E0_guess = E_arr[idx_min]
                    B0_guess = 10.0
                    B0p_guess = 4.0
                    popt, pcov = curve_fit(lambda V, V0, B0, B0p, E0: murnaghan(V, V0, B0, B0p, E0),
                                           V_arr, E_arr, p0=[V0_guess, B0_guess, B0p_guess, E0_guess],
                                           maxfev=8000)
                    V0_fit, B0_fit, B0p_fit, E0_fit = popt
                    a0_fit = V0_fit ** (1.0/3.0)
                    s_a0 = 1.0 if rel_err(a0_fit, ref.get('a0_angstrom', 8.603), tols.get('a0_angstrom', 0.05)) else 0.0
                    s_B0 = 1.0 if rel_err(B0_fit, ref.get('B0_GPa', 11.465), tols.get('B0_GPa', 0.15)) else 0.0
                    s_B0p = 1.0 if rel_err(B0p_fit, ref.get('B0_prime', 4.193), tols.get('B0_prime', 0.15)) else 0.0
                    eos_score = (s_a0 + s_B0 + s_B0p) / 3.0
        except Exception as e:
            pass

        # --- elastic constants zero ---
        el0_score = 0.0
        c11 = c12 = c44 = None
        try:
            el_file = os.path.join(output_dir, 'elastic_zero.json')
            if os.path.isfile(el_file):
                with open(el_file) as f:
                    el_data = json.load(f)
                c11 = float(el_data.get('C11_GPa', el_data.get('C11')))
                c12 = float(el_data.get('C12_GPa', el_data.get('C12')))
                c44 = float(el_data.get('C44_GPa', el_data.get('C44')))
                s_c11 = 1.0 if rel_err(c11, ref.get('C11_GPa', 22.12), tols.get('C11_GPa', 0.15)) else 0.0
                s_c12 = 1.0 if rel_err(c12, ref.get('C12_GPa', 10.19), tols.get('C12_GPa', 0.15)) else 0.0
                s_c44 = 1.0 if rel_err(c44, ref.get('C44_GPa', 7.923), tols.get('C44_GPa', 0.15)) else 0.0
                el0_score = (s_c11 + s_c12 + s_c44) / 3.0
        except:
            pass

        # --- derived moduli ---
        moduli_score = 0.0
        if c11 is not None and c12 is not None and c44 is not None:
            try:
                B_el = (c11 + 2*c12) / 3.0
                Gv = (c11 - c12 + 3*c44) / 5.0
                Gr = (5.0 * (c11 - c12) * c44) / (4.0 * c44 + 3.0 * (c11 - c12))
                G = (Gv + Gr) / 2.0
                E_val = (9.0 * B_el * G) / (3.0 * B_el + G)
                nu_val = (3.0 * B_el - 2.0 * G) / (6.0 * B_el + 2.0 * G)
                A_val = (2.0 * c44) / (c11 - c12) if (c11 - c12) != 0 else 0.0
                B_over_G_val = B_el / G if G != 0 else 0.0
                s_G = 1.0 if rel_err(G, ref.get('G_GPa', 7.07), tols.get('G_GPa', 0.15)) else 0.0
                s_E = 1.0 if rel_err(E_val, ref.get('E_GPa', 18.19), tols.get('E_GPa', 0.15)) else 0.0
                s_nu = 1.0 if rel_err(nu_val, ref.get('nu', 0.28), tols.get('nu', 0.15)) else 0.0
                s_A = 1.0 if rel_err(A_val, ref.get('A', 1.32), tols.get('A', 0.15)) else 0.0
                s_BG = 1.0 if rel_err(B_over_G_val, ref.get('B_over_G', 2.0), tols.get('B_over_G', 0.15)) else 0.0
                moduli_score = (s_G + s_E + s_nu + s_A + s_BG) / 5.0
            except:
                pass

        # --- thermodynamic at 300K 0GPa ---
        thermo_score = 0.0
        try:
            deb_file = os.path.join(output_dir, 'debye_output.csv')
            if os.path.isfile(deb_file):
                with open(deb_file) as f:
                    reader = csv.DictReader(f)
                    row_found = None
                    for row in reader:
                        try:
                            T_val = float(row.get('T', row.get('Temperature', row.get('temperature', 0))))
                            P_val = float(row.get('P', row.get('Pressure', row.get('pressure', 0))))
                        except:
                            continue
                        if abs(T_val - 300) < 1 and abs(P_val - 0) < 0.1:
                            row_found = row
                            break
                if row_found:
                    Cv_val = float(row_found.get('Cv', row_found.get('Cv_JmolK', 0)))
                    Cp_val = float(row_found.get('Cp', row_found.get('Cp_JmolK', 0)))
                    alpha_val = float(row_found.get('alpha', row_found.get('alpha_K-1', 0)))
                    Debye_val = float(row_found.get('Debye_T', row_found.get('Debye_T_K', row_found.get('debye', 0))))
                    s_Cv = 1.0 if rel_err(Cv_val, ref.get('Cv_300K_JmolK', 73.21), tols.get('Cv_300K_JmolK', 0.10)) else 0.0
                    s_Cp = 1.0 if rel_err(Cp_val, ref.get('Cp_300K_JmolK', 76.52), tols.get('Cp_300K_JmolK', 0.10)) else 0.0
                    s_alpha = 1.0 if rel_err(alpha_val, ref.get('alpha_300K_K-1', 6.79e-5), tols.get('alpha_300K_K-1', 0.10)) else 0.0
                    s_Debye = 1.0 if rel_err(Debye_val, ref.get('Debye_T_300K_K', 194.87), tols.get('Debye_T_300K_K', 0.10)) else 0.0
                    thermo_score = (s_Cv + s_Cp + s_alpha + s_Debye) / 4.0
        except:
            pass

        # --- pressure elastic ---
        pressure_score = 0.0
        try:
            pres_file = os.path.join(output_dir, 'elastic_pressure.json')
            if os.path.isfile(pres_file):
                with open(pres_file) as f:
                    pres_data = json.load(f)
                checks = 0
                passes = 0
                zero_entry = None
                for entry in pres_data:
                    if abs(float(entry.get('pressure_GPa', -1)) - 0) < 0.1:
                        zero_entry = entry
                        break
                if zero_entry:
                    c11_0 = float(zero_entry.get('C11', 0))
                    c12_0 = float(zero_entry.get('C12', 0))
                    c44_0 = float(zero_entry.get('C44', 0))
                    if rel_err(c11_0, ref.get('C11_GPa', 22.12), tols.get('C11_GPa', 0.15)): passes += 1
                    checks += 1
                    if rel_err(c12_0, ref.get('C12_GPa', 10.19), tols.get('C12_GPa', 0.15)): passes += 1
                    checks += 1
                    if rel_err(c44_0, ref.get('C44_GPa', 7.923), tols.get('C44_GPa', 0.15)): passes += 1
                    checks += 1
                else:
                    checks += 3
                sorted_data = sorted(pres_data, key=lambda x: float(x.get('pressure_GPa', 0)))
                c11_prev = c12_prev = c44_prev = None
                for entry in sorted_data:
                    c11_cur = float(entry.get('C11', 0))
                    c12_cur = float(entry.get('C12', 0))
                    c44_cur = float(entry.get('C44', 0))
                    if c11_prev is not None:
                        if c11_cur >= c11_prev * 0.999:
                            passes += 1
                        checks += 1
                        if c12_cur >= c12_prev * 0.999:
                            passes += 1
                        checks += 1
                        if c44_cur >= c44_prev * 0.999:
                            passes += 1
                        checks += 1
                    c11_prev, c12_prev, c44_prev = c11_cur, c12_cur, c44_cur
                if checks > 0:
                    pressure_score = passes / checks
        except:
            pass

        # --- stability ---
        stab_score = 0.0
        if c11 is not None and c12 is not None and c44 is not None:
            try:
                cond1 = c44 > 0
                cond2 = c11 > 0
                cond3 = (c11 - c12) > 0
                cond4 = (c11 + 2*c12) > 0
                stab_score = 1.0 if all([cond1, cond2, cond3, cond4]) else 0.0
            except:
                pass

        # --- bulk modulus consistency ---
        bcons_score = 0.0
        if c11 is not None and c12 is not None:
            try:
                B_el = (c11 + 2*c12) / 3.0
                B0_val = artifact.get('B0_GPa', None)
                if B0_val is None and B0_fit is not None:
                    B0_val = B0_fit
                if B0_val is not None and abs(B_el - B0_val) <= 3.0:
                    bcons_score = 1.0
            except:
                pass

        composite = (w_eos * eos_score + w_el0 * el0_score + w_moduli * moduli_score +
                     w_thermo * thermo_score + w_pressure * pressure_score +
                     w_stability * stab_score + w_bcons * bcons_score)
        return min(max(composite, 0.0), 1.0)


_SCORERS = {
    'step5_results': score_0,
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
