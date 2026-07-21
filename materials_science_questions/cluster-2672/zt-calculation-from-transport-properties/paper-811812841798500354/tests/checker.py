import os
import json
import csv

# === author imports / helpers ===
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
        L = 0.01
        w = 500e-6
        t1 = 250e-6
        k1 = 163.0
        kz = 5.0
        h = 10000.0
        q_flux = 1.4e7  # W/m^2
        Q = q_flux * w * w

        def phi(zeta, t1_v, t2_v, k1_v, k2_v, h_v):
            # Stable formulation: avoid overflow in exponentials for large zeta
            exp_m2zt2 = np.exp(-2 * zeta * t2_v)
            exp_m4zt1 = np.exp(-4 * zeta * t1_v)
            exp_m2zt1 = np.exp(-2 * zeta * t1_v)
            psi = (zeta + h_v / k2_v) / (zeta - h_v / k2_v)
            alpha = (1 - k2_v / k1_v) / (1 + k2_v / k1_v)
            num = alpha * exp_m2zt2 - exp_m4zt1 + psi * (1 - alpha * exp_m2zt1)
            den = alpha * exp_m2zt2 + exp_m4zt1 + psi * (1 + alpha * exp_m2zt1)
            return num / den

        def excess_peak(k_xy, N=200):
            k2_eq = np.sqrt(k_xy * kz)
            t2 = 500e-6
            t2_eq = t2 / np.sqrt(kz / k_xy)
            A0 = (Q / (L*L)) * (t1/k1 + t2_eq/k2_eq + 1.0/h)
            m_max = N
            n_max = N
            sum_m = 0.0
            sum_n = 0.0
            for m_val in range(1, m_max+1):
                lam = m_val * np.pi / L
                phi_val = phi(lam, t1, t2_eq, k1, k2_eq, h)
                sin_term = np.sin((L+w)/2 * lam) - np.sin((L-w)/2 * lam)
                Am = (2.0 * Q / (L*L * w * k1 * lam*lam * phi_val)) * sin_term
                sum_m += Am
            for n_val in range(1, n_max+1):
                delta = n_val * np.pi / L
                phi_val = phi(delta, t1, t2_eq, k1, k2_eq, h)
                sin_term = np.sin((L+w)/2 * delta) - np.sin((L-w)/2 * delta)
                An = (2.0 * Q / (L*L * w * k1 * delta*delta * phi_val)) * sin_term
                sum_n += An
            sum_mn = 0.0
            for m_val in range(1, m_max+1):
                lam = m_val * np.pi / L
                cos_lamL2 = np.cos(lam * L / 2.0)
                sin_lamw2 = np.sin(lam * w / 2.0)
                for n_val in range(1, n_max+1):
                    delta = n_val * np.pi / L
                    beta = np.sqrt(lam*lam + delta*delta)
                    phi_val = phi(beta, t1, t2_eq, k1, k2_eq, h)
                    cos_deltaL2 = np.cos(delta * L / 2.0)
                    sin_deltaw2 = np.sin(delta * w / 2.0)
                    Amn = (16.0 * Q * cos_lamL2 * sin_lamw2 * cos_deltaL2 * sin_deltaw2) / (L*L * w*w * k1 * beta * lam * delta * phi_val)
                    sum_mn += Amn
            peak = A0 + sum_m + sum_n + sum_mn
            return peak

        def total_resistance(k_xy, t2_val, N=60):
            k2_eq = np.sqrt(k_xy * kz)
            t2_eq = t2_val / np.sqrt(kz / k_xy)
            R1D = (t1 / (k1 * L * L)) + (t2_eq / (k2_eq * L * L)) + (1.0 / (h * L * L))
            prefactor_single = 1.0 / (2.0 * (w/2)**2 * (L/2)**2 * k1)
            prefactor_double = 1.0 / ((w/2)**4 * (L/2)**2 * k1)
            sum_single_m = 0.0
            sum_single_n = 0.0
            pi_L = np.pi / L
            for k in range(1, N+1):
                lam = k * pi_L
                phi_lam = phi(lam, t1, t2_eq, k1, k2_eq, h)
                sin2 = np.sin(w * lam / 2) ** 2
                sum_single_m += sin2 / (lam**3 * phi_lam)
                sum_single_n += sin2 / (lam**3 * phi_lam)
            Rs_single = prefactor_single * (sum_single_m + sum_single_n)
            sum_double = 0.0
            for m_val in range(1, N+1):
                lam = m_val * pi_L
                sin2_m = np.sin(w * lam / 2) ** 2
                for n_val in range(1, N+1):
                    delta = n_val * pi_L
                    beta = np.sqrt(lam*lam + delta*delta)
                    phi_beta = phi(beta, t1, t2_eq, k1, k2_eq, h)
                    sin2_n = np.sin(w * delta / 2) ** 2
                    contrib = sin2_m * sin2_n / (lam**2 * delta**2 * beta * phi_beta)
                    sum_double += contrib
            Rs_double = prefactor_double * sum_double
            Rs = Rs_single + Rs_double
            return R1D + Rs

        ref_excess = {}
        tol_temp = 0.1
        for kxy in [5, 350, 1800]:
            ref_excess[kxy] = excess_peak(kxy, N=200)

        t2_range = np.arange(1e-6, 1000e-6, 5e-6)
        best_t2 = None
        best_R = np.inf
        for t2_val in t2_range:
            R = total_resistance(350, t2_val, N=50)
            if R < best_R:
                best_R = R
                best_t2 = t2_val
        fine_step = 0.5e-6
        fine_range = np.arange(best_t2 - 10e-6, best_t2 + 10e-6, fine_step)
        for t2_val in fine_range:
            if t2_val <= 0:
                continue
            R = total_resistance(350, t2_val, N=50)
            if R < best_R:
                best_R = R
                best_t2 = t2_val

        ref_opt_thickness = best_t2 * 1e6
        ref_opt_resistance = best_R
        return {"ref_excess": ref_excess, "opt_thickness": ref_opt_thickness, "opt_resistance": ref_opt_resistance, "tol_temp": tol_temp}


# === block: score_0 (check id='excess_temp_kxy5') ===
def score_0(artifact, step, ctx):
        val = float(artifact.get("kxy5_excess_temp"))
        return 1.0 if abs(val - ctx["ref_excess"][5]) <= ctx["tol_temp"] else 0.0


# === block: score_1 (check id='excess_temp_kxy350') ===
def score_1(artifact, step, ctx):
        val = float(artifact.get("kxy350_excess_temp"))
        return 1.0 if abs(val - ctx["ref_excess"][350]) <= ctx["tol_temp"] else 0.0


# === block: score_2 (check id='excess_temp_kxy1800') ===
def score_2(artifact, step, ctx):
        val = float(artifact.get("kxy1800_excess_temp"))
        return 1.0 if abs(val - ctx["ref_excess"][1800]) <= ctx["tol_temp"] else 0.0


# === block: score_3 (check id='opt_thickness') ===
def score_3(artifact, step, ctx):
        val = float(artifact.get("kxy350_opt_thickness"))
        return 1.0 if abs(val - ctx["opt_thickness"]) <= 1.0 else 0.0


# === block: score_4 (check id='opt_resistance') ===
def score_4(artifact, step, ctx):
        val = float(artifact.get("kxy350_total_thermal_resistance"))
        return 1.0 if abs(val - ctx["opt_resistance"]) <= 0.01 else 0.0


# === block: score_5 (check id='trend_check') ===
def score_5(artifact, step, ctx):
        v5 = float(artifact.get("kxy5_excess_temp"))
        v350 = float(artifact.get("kxy350_excess_temp"))
        v1800 = float(artifact.get("kxy1800_excess_temp"))
        return 1.0 if (v350 < v5 and v1800 < v5) else 0.0


_SCORERS = {
    'excess_temp_kxy5': score_0,
    'excess_temp_kxy350': score_1,
    'excess_temp_kxy1800': score_2,
    'opt_thickness': score_3,
    'opt_resistance': score_4,
    'trend_check': score_5,
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
