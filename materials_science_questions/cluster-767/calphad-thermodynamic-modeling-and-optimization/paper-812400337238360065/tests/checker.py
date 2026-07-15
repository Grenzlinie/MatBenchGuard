import os
import json
import csv

# === author imports / helpers ===
import os
import sys
import subprocess

def _ensure_deps():
    missing = []
    try:
        import numpy
    except ImportError:
        missing.append('numpy')
    try:
        import scipy
    except ImportError:
        missing.append('scipy')
    if missing:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '-q', '-i',
             'https://pypi.tuna.tsinghua.edu.cn/simple'] + missing,
            check=True
        )

_ensure_deps()

import numpy as np
import scipy.optimize as opt
from scipy.signal import argrelextrema
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


# === block: score_0 (check id='step_01_phase_boundary') ===
def score_0(artifact, step, ctx):
    # constants and model parameters
    R = 0.008314  # kJ/mol/K
    Omega_FeAl = -23.1
    Omega_FeCo = -16.6
    Omega_AlCo = -31.9
    T = 873.0
    T_c_Fe = 1043.0   # °T_c^m
    T_c_order_ref = 1003.0  # °T_c^°

    def deltaG_ferro_ref(T_val):
        """Magnetic reference free energy for pure Fe (eq 5) in kJ/mol."""
        return 9.0 * (T_val - 968.9 - np.sqrt((T_val - 968.9)**2 + 28832)) / 2.0

    def deltaG_ord_ref(T_val):
        """Ordering reference free energy for stoichiometric FeCo (eq 9) in kJ/mol."""
        return 5.5 * (T_val - 746.1 - np.sqrt((T_val - 746.1)**2 + 50498)) / 2.0

    def T_cm(X_Al, X_Co):
        """Ternary Curie temperature (K) using corrected expression derived from eq (4)."""
        A = 0.237 + 0.357 * np.sqrt((X_Co - 0.024)**2 + 0.028**2)
        term = -(1138.0 * X_Co + 370.0) * X_Al**2 / A
        return term + 1138.0 * X_Co + 1043.0

    def compute_f(X_Fe, X_Al, X_Co):
        """Scaling factor f (eq 8), taking the maximum of applied conditions."""
        vals = []
        if X_Co <= X_Fe:
            vals.append(2 * X_Co)
        if X_Co >= X_Fe:
            vals.append(2 * X_Fe)
        if X_Al <= 0.5:
            vals.append(2 * X_Al)
        if X_Al >= 0.5:
            vals.append(2 * (1.0 - X_Al))
        return max(vals) if vals else 0.0

    def total_G(x, X_Co):
        """Total molar Gibbs free energy (kJ/mol) as function of X_Al at fixed X_Co."""
        X_Fe = 1.0 - X_Co - x
        if X_Fe <= 1e-12 or X_Co <= 1e-12 or x <= 1e-12:
            return 1e10
        # Chemical free energy (eq 2)
        G_ideal = R * T * (X_Fe * np.log(X_Fe) + x * np.log(x) + X_Co * np.log(X_Co))
        G_excess = Omega_FeAl * X_Fe * x + Omega_FeCo * X_Fe * X_Co + Omega_AlCo * x * X_Co
        G_para = G_ideal + G_excess

        # Ferromagnetic excess (eq 3)
        sum_mX = x  # Al has m=1, Fe and Co have m=0
        T_cm_val = T_cm(x, X_Co)
        if T_cm_val <= 0:
            G_ferro = 0.0
        else:
            T_ms = T * T_c_Fe / T_cm_val
            prefactor = (1.0 - sum_mX) * T_cm_val / T_c_Fe
            G_ferro = prefactor * deltaG_ferro_ref(T_ms)

        # Ordering excess (eq 6–9)
        O12, O23, O31 = Omega_FeAl, Omega_AlCo, Omega_FeCo
        P = O12 * X_Fe * x + O23 * x * X_Co + O31 * X_Co * X_Fe
        L = O12**2 + O23**2 + O31**2 - 2.0 * (O12*O23 + O23*O31 + O31*O12)
        sqrt_arg = P + L * X_Fe * x * X_Co
        if sqrt_arg <= 0.0:
            G_ord = 0.0
        else:
            T_c_ord = (-P + np.sqrt(sqrt_arg)) / R
            T_o_star = T * T_c_order_ref / T_c_ord if T_c_ord > 1.0 else T * 10.0
            f_val = compute_f(X_Fe, x, X_Co)
            G_ord = f_val * (T_c_ord / T_c_order_ref) * deltaG_ord_ref(T_o_star)

        return G_para + G_ferro + G_ord

    def solve_equilibrium(section_X_Co):
        """Compute equilibrium X_Al values for a given X_Co section."""
        max_x = 1.0 - section_X_Co - 1e-6
        if max_x <= 0.0:
            return None
        x_vals = np.linspace(1e-6, max_x, 5000)
        G_vals = np.array([total_G(x, section_X_Co) for x in x_vals])
        min_idx = argrelextrema(G_vals, np.less)[0]
        if len(min_idx) < 2:
            return None
        # Choose the two deepest minima as initial guess
        min_G = G_vals[min_idx]
        sorted_idx = min_idx[np.argsort(min_G)]
        x1_init = x_vals[sorted_idx[0]]
        x2_init = x_vals[sorted_idx[1]]

        def eqns(vars):
            x1, x2 = vars
            if x1 <= 0 or x1 >= 1.0 - section_X_Co or x2 <= 0 or x2 >= 1.0 - section_X_Co:
                return [1e6, 1e6]
            G1 = total_G(x1, section_X_Co)
            G2 = total_G(x2, section_X_Co)
            dx = 1e-6
            dG1 = (total_G(x1 + dx, section_X_Co) - total_G(x1 - dx, section_X_Co)) / (2*dx)
            dG2 = (total_G(x2 + dx, section_X_Co) - total_G(x2 - dx, section_X_Co)) / (2*dx)
            return [dG1 - dG2, G1 - dG1*x1 - G2 + dG2*x2]

        try:
            sol = opt.fsolve(eqns, [x1_init, x2_init], maxfev=1000, xtol=1e-10)
        except Exception:
            sol = None
        if sol is None:
            # fallback to grid minima
            gold1 = x_vals[sorted_idx[0]]
            gold2 = x_vals[sorted_idx[1]]
        else:
            gold1, gold2 = min(sol[0], sol[1]), max(sol[0], sol[1])
        return [gold1, gold2]

    # --- Main scoring logic ---
    tolerance = step.get('tolerance_abs', 0.02)
    sections = step.get('sections', [])

    # Validate artifact shape
    if not isinstance(artifact, list) or len(artifact) != 10:
        return 0.0

    required_cols = {'section_X_Co', 'phase', 'X_Fe', 'X_Al', 'X_Co'}
    for row in artifact:
        try:
            s_co = float(row['section_X_Co'])
            x_fe = float(row['X_Fe'])
            x_al = float(row['X_Al'])
            x_co = float(row['X_Co'])
            if abs(x_fe + x_al + x_co - 1.0) > 0.001:
                return 0.0
        except (KeyError, ValueError):
            return 0.0

    # Group rows by section_X_Co
    import collections
    section_rows = collections.defaultdict(list)
    for row in artifact:
        sec = round(float(row['section_X_Co']), 6)
        section_rows[sec].append(row)

    good_sections = 0
    for sec in sections:
        sec_rounded = round(sec, 6)
        rows = section_rows.get(sec_rounded, [])
        if len(rows) != 2:
            continue
        agent_x_al = [float(r['X_Al']) for r in rows]

        gold = solve_equilibrium(sec)
        if gold is None:
            continue
        # Pair agent values to gold values by minimal sum of absolute differences
        diffs = []
        for a in agent_x_al:
            d1 = abs(a - gold[0])
            d2 = abs(a - gold[1])
            diffs.append((d1, d2))
        # Try both possible assignments
        assign1 = diffs[0][0] + diffs[1][1]
        assign2 = diffs[0][1] + diffs[1][0]
        min_sum = min(assign1, assign2)
        if assign1 <= assign2:
            pair_diffs = [diffs[0][0], diffs[1][1]]
        else:
            pair_diffs = [diffs[0][1], diffs[1][0]]
        if all(d <= tolerance for d in pair_diffs):
            good_sections += 1

    score = good_sections / len(sections) if sections else 1.0
    return score


_SCORERS = {
    'step_01_phase_boundary': score_0,
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
