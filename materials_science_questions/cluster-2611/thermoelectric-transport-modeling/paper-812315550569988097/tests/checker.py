import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve


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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        tol = step.get('tolerance_rel', 0.01)
        total = 0
        good = 0
        for row in rows:
            try:
                ZTc = float(row['ZTc'])
                r = float(row['alpha_over_beta'])
                agent_val = float(row['ZDeltaT_max'])
            except (ValueError, TypeError, KeyError):
                continue
            if ZTc <= 0 or r <= 0:
                continue
            if ZTc >= r:
                # No optimum exists; skip row
                continue
            xi = -np.log(1 - ZTc / r)
            expected = r**2 * (xi + np.exp(-xi) - 1)
            if not np.isfinite(agent_val) or not np.isfinite(expected):
                continue
            rel_err = abs(agent_val - expected) / max(abs(expected), 1e-8)
            total += 1
            if rel_err <= tol:
                good += 1
        return good / total if total > 0 else 1.0


# === block: score_1 (check id='step3') ===
def score_1(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        tol = step.get('tolerance_rel', 0.01)
        total = 0
        good = 0
        for row in rows:
            try:
                z = float(row['ZTh_beta_over_alpha'])
                agent_val = float(row['Nmax_star'])
            except (ValueError, TypeError, KeyError):
                continue
            if z <= 0:
                continue
            def eq(x):
                denom = 1 - np.exp(x)
                return 1 + (2*x**2)/denom + (x**2*np.exp(x))/(denom**2) - z
            xi_guess = 0.1
            try:
                xi_sol = fsolve(eq, xi_guess)[0]
                if xi_sol <= 0:
                    continue
                denom = 1 - np.exp(xi_sol)
                expected = (2*xi_sol**2)/denom * (1 + xi_sol*np.exp(xi_sol)/denom)
            except Exception:
                continue
            if not np.isfinite(agent_val) or not np.isfinite(expected):
                continue
            rel_err = abs(agent_val - expected) / max(abs(expected), 1e-8)
            total += 1
            if rel_err <= tol:
                good += 1
        return good / total if total > 0 else 1.0


# === block: score_2 (check id='step4') ===
def score_2(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        tol_abs = step.get('tolerance_abs', 2.0)
        # Fixed example parameters (SI units)
        sigma = 1e5          # S/m  (0.1 (μΩm)⁻¹)
        lam = 1.6            # W/(m·K)
        A = 0.01e-6          # m²
        L = 1e-3             # m
        K = lam * A / L
        R = L / (sigma * A)
        alpha = 185e-6       # V/K
        alpha_pN = 2 * alpha
        beta = 200e-6        # V/K
        Tc = 250.0           # K
        Tinf = 300.0         # K
        gamma = 50.0         # W/(m²·K)
        P = 0.4e-3           # m
        Pstar = P * gamma * L / K
        def deltaT_for_I(I):
            xi = beta * I / K
            disc = np.sqrt(xi**2 + 4*Pstar)
            k1 = (xi + disc) / 2
            k2 = (xi - disc) / 2
            expk1 = np.exp(k1)
            expk2 = np.exp(k2)
            denom = expk1 - expk2
            f = (k1 - k2) / denom
            g = (k1*expk2 - k2*expk1) / denom - f
            h = -g / (k1 * k2)
            K_tot = 2 * K * f
            H_tot = 2 * K * g
            R_tot = 2 * R * h
            num = alpha_pN * I * Tc - H_tot * (Tinf - Tc) - I**2 * R_tot
            if K_tot == 0:
                return 0.0
            return num / K_tot
        total = 0
        good = 0
        for row in rows:
            try:
                I = float(row['I_A'])
                agent_dT = float(row['DeltaT_K'])
            except (ValueError, TypeError, KeyError):
                continue
            if I < 0 or not np.isfinite(I):
                continue
            expected = deltaT_for_I(I)
            if not np.isfinite(expected):
                continue
            abs_err = abs(agent_dT - expected)
            total += 1
            if abs_err <= tol_abs:
                good += 1
        return good / total if total > 0 else 1.0


# === block: score_3 (check id='step5') ===
def score_3(artifact, step, ctx):
        obj = artifact
        if not isinstance(obj, dict):
            return 0.0
        key = 'beta_200_max_delta_T_K'
        agent_max = obj.get(key)
        if agent_max is None:
            return 0.0
        try:
            agent_max = float(agent_max)
        except (ValueError, TypeError):
            return 0.0
        tol_abs = step.get('tolerance_abs', 3.0)
        # recompute the maximum ΔT via a fine grid search
        sigma = 1e5; lam = 1.6; A = 0.01e-6; L = 1e-3; K = lam*A/L; R = L/(sigma*A)
        alpha = 185e-6; alpha_pN = 2*alpha; beta = 200e-6; Tc = 250.0; Tinf = 300.0
        gamma = 50.0; P = 0.4e-3; Pstar = P*gamma*L/K
        def deltaT_for_I(I):
            xi = beta*I/K
            disc = np.sqrt(xi**2 + 4*Pstar)
            k1 = (xi+disc)/2; k2 = (xi-disc)/2
            expk1 = np.exp(k1); expk2 = np.exp(k2)
            denom = expk1 - expk2
            f = (k1 - k2)/denom
            g = (k1*expk2 - k2*expk1)/denom - f
            h = -g/(k1*k2)
            K_tot = 2*K*f; H_tot = 2*K*g; R_tot = 2*R*h
            num = alpha_pN*I*Tc - H_tot*(Tinf - Tc) - I**2*R_tot
            if K_tot == 0:
                return 0.0
            return num/K_tot
        best = -1e9
        for I in np.linspace(0, 0.1, 200):
            dT = deltaT_for_I(I)
            if np.isfinite(dT) and dT > best:
                best = dT
        if best <= 0:
            return 0.0
        return 1.0 if abs(agent_max - best) <= tol_abs else 0.0


_SCORERS = {
    'step2': score_0,
    'step3': score_1,
    'step4': score_2,
    'step5': score_3,
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
