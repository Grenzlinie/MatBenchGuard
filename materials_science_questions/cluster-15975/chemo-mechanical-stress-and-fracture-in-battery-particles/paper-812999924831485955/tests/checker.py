import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, os


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


# === block: score_0 (check id='stress_strain') ===
def score_0(artifact, step, ctx):
        import math

        # ---- Uniaxial compression stress recompute ----
        def compute_stress(material, strain, strain_rate):
            G = material['G']
            K = material['K']
            eps0 = material['eps0']
            m = material['m']
            S0 = material['S0']
            H0 = material['H0']
            S_star = material['S_star']
            a_exp = material['a']

            # Diagonal ansatz  --  F = diag(exp(-strain), lambda_lat, lambda_lat)
            # F^p = diag(lambda_p_ax, lambda_p_lat, lambda_p_lat)  with det(F^p)=1 => lambda_p_ax = 1/lambda_p_lat^2
            # State variables
            S = S0
            lambda_p_lat = 1.0

            # Integration step size
            dt_min = 1e-4
            nsteps = max(1, int(strain / (strain_rate * dt_min)))
            d_strain = strain_rate * dt_min
            # adjust dt so that exact nsteps*d_strain = strain
            dt = strain / (nsteps * strain_rate)
            d_strain = strain_rate * dt

            for _ in range(nsteps):
                # current total strain
                eps_current = d_strain * (_ + 1)
                f11 = math.exp(-eps_current)
                lambda_p_ax = 1.0 / (lambda_p_lat * lambda_p_lat)

                # --- solve for lateral stretch (lambda) such that T22 = 0 ---
                lambda_guess = math.exp(d_strain / 2.0)  # approximate
                for it in range(10):
                    lambda_e_ax = f11 / lambda_p_ax
                    lambda_e_lat = lambda_guess / lambda_p_lat
                    # logarithmic elastic strains
                    ee_ax = math.log(lambda_e_ax)
                    ee_lat = math.log(lambda_e_lat)
                    tr_ee = ee_ax + 2.0 * ee_lat
                    ee0_ax = ee_ax - tr_ee / 3.0
                    ee0_lat = ee_lat - tr_ee / 3.0
                    # M^e diagonal
                    M_ax = 2.0 * G * ee0_ax + K * tr_ee
                    M_lat = 2.0 * G * ee0_lat + K * tr_ee
                    # Cauchy stress components (Je = lambda_e_ax * lambda_e_lat^2)
                    Je = lambda_e_ax * lambda_e_lat * lambda_e_lat
                    T_ax = M_ax / Je
                    T_lat = M_lat / Je
                    # residual
                    if abs(T_lat) < 1e-4:
                        break
                    # simple secant update
                    lambda_guess *= (1.0 - 0.5 * T_lat / (G / Je + 1e-12))
                    # keep guess positive
                    if lambda_guess <= 0:
                        lambda_guess = 1e-6
                # after convergence
                lambda_e_ax = f11 / lambda_p_ax
                lambda_e_lat = lambda_guess / lambda_p_lat
                ee_ax = math.log(max(lambda_e_ax, 1e-12))
                ee_lat = math.log(max(lambda_e_lat, 1e-12))
                tr_ee = ee_ax + 2.0 * ee_lat
                ee0_ax = ee_ax - tr_ee / 3.0
                ee0_lat = ee_lat - tr_ee / 3.0
                M_ax = 2.0 * G * ee0_ax + K * tr_ee
                M_lat = 2.0 * G * ee0_lat + K * tr_ee
                # deviatoric part
                trM = M_ax + 2.0 * M_lat
                M0_ax = M_ax - trM / 3.0
                M0_lat = M_lat - trM / 3.0
                sigma_bar = math.sqrt(3.0 * (M0_ax * M0_ax + 2.0 * M0_lat * M0_lat) / 2.0)
                # plastic shear strain rate
                dot_eps_p = eps0 * (sigma_bar / max(S, 1e-12)) ** (1.0 / m)
                # plastic stretching components (principal)
                Dp_ax = (3.0 / 2.0) * dot_eps_p * (M0_ax / max(sigma_bar, 1e-12))
                Dp_lat = (3.0 / 2.0) * dot_eps_p * (M0_lat / max(sigma_bar, 1e-12))
                # update F^p: exponential map approximation (I + Dp*dt) and then normalize det=1
                # Because Dp is deviatoric (trace zero), the determinant of exp(Dp dt) ≈ 1 + O(dt^2)
                # We'll simply use the diagonal update and rescale.
                lambda_p_lat *= (1.0 + Dp_lat * dt)
                lambda_p_lat = abs(lambda_p_lat)
                if lambda_p_lat < 1e-12:
                    lambda_p_lat = 1e-12
                # enforce det(F^p) = 1 by adjusting lambda_p_ax (we only track lambda_p_lat; lambda_p_ax is derived at next step)
                # S update
                S_dot = H0 * (1.0 - S / S_star) ** a_exp * dot_eps_p
                S += S_dot * dt
                S = max(S, 1e-12)

            # After all steps, compute final stress from state
            f11 = math.exp(-strain)
            # solve lambda again for final strain
            lambda_guess = 1.0
            lambda_p_ax = 1.0 / (lambda_p_lat * lambda_p_lat)
            for it in range(20):
                lambda_e_ax = f11 / lambda_p_ax
                lambda_e_lat = lambda_guess / lambda_p_lat
                ee_ax = math.log(max(lambda_e_ax, 1e-12))
                ee_lat = math.log(max(lambda_e_lat, 1e-12))
                tr_ee = ee_ax + 2.0 * ee_lat
                ee0_ax = ee_ax - tr_ee / 3.0
                ee0_lat = ee_lat - tr_ee / 3.0
                M_ax = 2.0 * G * ee0_ax + K * tr_ee
                M_lat = 2.0 * G * ee0_lat + K * tr_ee
                Je = lambda_e_ax * lambda_e_lat * lambda_e_lat
                T_lat = M_lat / Je
                if abs(T_lat) < 1e-4:
                    break
                lambda_guess *= (1.0 - 0.2 * T_lat / (G / Je + 1e-12))
                if lambda_guess <= 0:
                    lambda_guess = 1e-6
            T_ax = M_ax / Je
            return -T_ax   # compression stress positive

        # ---- scoring logic ----
        rows = artifact
        if not rows or len(rows) < 10:
            return 0.0
        try:
            _ = [float(r['strain']) for r in rows]
        except Exception:
            return 0.0

        mp = step['material_params']
        E = mp['E']
        nu = mp['nu']
        G_val = E / (2.0 * (1.0 + nu))
        K_val = E / (3.0 * (1.0 - 2.0 * nu))
        mat = {'G': G_val, 'K': K_val,
               'eps0': mp['eps0'], 'm': mp['m'],
               'S0': mp['S0'], 'H0': mp['H0'],
               'S_star': mp['S_star'], 'a': mp['a']}
        strain_rates = step['strain_rates']
        stress_cols = step['stress_columns']
        tol = step.get('tolerance_abs_mpa', 10.0)

        max_err = 0.0
        n_pts = 0
        for sr in strain_rates:
            col = stress_cols.get(str(sr))
            if col is None or col not in rows[0]:
                continue
            for row in rows:
                try:
                    eps_val = float(row['strain'])
                    stress_agent = float(row[col])
                except Exception:
                    continue
                if eps_val < 0.0 or eps_val > 1.0:
                    continue
                stress_expected = compute_stress(mat, eps_val, sr)
                err = abs(stress_agent - stress_expected)
                if err > max_err:
                    max_err = err
                n_pts += 1

        if n_pts == 0:
            return 0.0
        if max_err <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (max_err - tol) / (2.0 * tol))


# === block: score_1 (check id='indentation') ===
def score_1(artifact, step, ctx):
    def score_indentation(artifact, step, ctx):
        rows = artifact
        if not rows or len(rows) < step['min_rows']:
            return 0.0
        try:
            d = [float(r[step['displacement_column']]) for r in rows]
            p = [float(r[step['load_column']]) for r in rows]
        except:
            return 0.0
        n = len(d)
        # Qualitative checks
        max_load = max(p) if p else 0.0
        max_depth = max(d) if d else 0.0
        qual_ok = 1.0
        if max_depth < step['qualitative_checks']['max_depth_min']:
            qual_ok *= 0.8
        target_load = step['qualitative_checks']['max_load_target']
        if abs(max_load - target_load) / target_load > step['qualitative_checks']['max_load_tol_rel']:
            qual_ok *= 0.9
        # phases: check load increases then roughly constant then decreases
        # simply check max load > 0 and final load < max_load * 0.2
        if p[-1] > 0.2 * max_load:
            qual_ok *= 0.9
        # reference checkpoints
        checkpoints = step['reference_checkpoints']
        err_sum = 0.0
        count = 0
        for cp in checkpoints:
            d_ref = cp['displacement_nm']
            p_ref = cp['load_mN']
            tol_frac = cp['tol_rel']
            # find nearest displacement in agent data
            idx = min(range(n), key=lambda i: abs(d[i]-d_ref))
            p_agent = p[idx]
            if p_ref > 0:
                rel_err = abs(p_agent - p_ref) / p_ref
            else:
                rel_err = abs(p_agent - p_ref)
            if rel_err > tol_frac:
                err_sum += rel_err - tol_frac
            count += 1
        if count == 0:
            return qual_ok
        avg_excess = err_sum / count
        checkpoint_score = max(0.0, 1.0 - avg_excess * 0.5)
        return qual_ok * checkpoint_score


_SCORERS = {
    'stress_strain': score_0,
    'indentation': score_1,
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
