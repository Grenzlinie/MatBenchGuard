import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import ellipk, ellipe


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
    def normal_vector(dip_dir_deg, dip_deg):
        a = np.radians(dip_dir_deg)
        b = np.radians(dip_deg)
        l = np.cos(np.radians(90) - b) * np.cos(a)
        m = np.cos(np.radians(90) - b) * np.sin(a)
        n = np.sin(b - np.radians(90))
        return l, m, n

    def stresses_on_plane(l, m, n, sx, sy, sz):
        sigma_n_ext = sx * l**2 + sy * m**2 + sz * n**2
        tau2 = (sx * l)**2 + (sy * m)**2 + (sz * n)**2 - sigma_n_ext**2
        tau = np.sqrt(max(tau2, 0.0))
        if tau < 1e-20:
            l_tau = m_tau = n_tau = 0.0
        else:
            l_tau = (sx - sigma_n_ext) * l / tau
            m_tau = (sy - sigma_n_ext) * m / tau
            n_tau = (sz - sigma_n_ext) * n / tau
        return sigma_n_ext, tau, (l_tau, m_tau, n_tau)

    def shear_angle(l_tau, m_tau, n_tau, dip_dir_deg, dip_deg):
        a = np.radians(dip_dir_deg)
        b = np.radians(dip_deg)
        lo = np.cos(b) * np.cos(a)
        mo = np.cos(b) * np.sin(a)
        no = np.sin(b)
        dot = l_tau * lo + m_tau * mo + n_tau * no
        return np.degrees(np.arccos(np.clip(dot, -1.0, 1.0)))

    def circular_sifs(phi_deg, a, sigma_eff, tau_eff, omega_deg, nu):
        phi = np.radians(phi_deg)
        om = np.radians(omega_deg)
        coef = np.sqrt(a / np.pi)
        KI = 2 * coef * sigma_eff
        KII = -4 * np.cos(phi - om) / (2 - nu) * coef * tau_eff
        KIII = 4 * (1 - nu) * np.sin(phi - om) / (2 - nu) * coef * tau_eff
        return KI, KII, KIII

    def mts_critical_angle(KI, KII):
        if abs(KII) < 1e-20:
            return 0.0
        def sig_th(th):
            return np.cos(th/2)**2 * (KI * np.cos(th/2) - 3 * KII * np.sin(th/2))
        theta1 = 2 * np.arctan2(KI - np.sqrt(KI**2 + 8*KII**2), 4*KII)
        theta2 = 2 * np.arctan2(KI + np.sqrt(KI**2 + 8*KII**2), 4*KII)
        v1 = sig_th(theta1)
        v2 = sig_th(theta2)
        theta_c = theta1 if v1 >= v2 else theta2
        return np.degrees(theta_c)

    def elliptical_sifs(phi_deg, a, b, gamma_deg, sigma_eff, tau_eff, omega_deg, nu):
        phi = np.radians(phi_deg)
        om = np.radians(omega_deg)
        if np.isclose(b, a):
            k = 0.0
            kprime = 1.0
        else:
            ratio = b / a
            k = np.sqrt(1 - ratio**2)
            kprime = ratio
        if np.isclose(k, 0.0):
            Ek = np.pi/2
            Kk = np.pi/2
        else:
            m = k**2
            Ek = ellipe(m)
            Kk = ellipk(m)
        B = (k**2 - nu) * Ek + nu * kprime**2 * Kk
        C = (k**2 + nu * kprime**2) * Ek - nu * kprime**2 * Kk
        denom = (a**2 * np.sin(phi)**2 + b**2 * np.cos(phi)**2)**0.25
        KI = sigma_eff / Ek * np.sqrt(np.pi * b / a) * denom
        common = -tau_eff * k**2 * np.sqrt(np.pi * a * b) / denom
        KII = common * (kprime / B * np.cos(om) * np.cos(phi) + 1.0 / C * np.sin(om) * np.sin(phi))
        common2 = tau_eff * k**2 * (1 - nu) * np.sqrt(np.pi * a * b) / denom
        KIII = common2 * (1.0 / B * np.cos(om) * np.sin(phi) - kprime / C * np.sin(om) * np.cos(phi))
        return KI, KII, KIII

    def phi_actual_from_apparent(phi_deg, a, b):
        phi = np.radians(phi_deg)
        acos = a * np.cos(phi)
        bsin = b * np.sin(phi)
        if np.isclose(acos, 0.0):
            return 90.0 if bsin >= 0 else 270.0
        rad = np.arctan2(bsin, acos)
        return np.degrees(rad) % 360

    def global_coords(f, g, h, alpha_deg, beta_deg):
        a_rad = np.radians(alpha_deg)
        b_rad = np.radians(beta_deg)
        x = f * np.cos(b_rad) * np.cos(a_rad) - g * np.sin(a_rad) - h * np.cos(a_rad) * np.sin(b_rad)
        y = f * np.cos(b_rad) * np.sin(a_rad) + g * np.cos(a_rad) - h * np.sin(a_rad) * np.sin(b_rad)
        z = f * np.sin(b_rad) + h * np.cos(b_rad)
        return x, y, z

    def plane_from_points(pts_global):
        p0 = pts_global[:, 0]
        p1 = pts_global[:, 1]
        p2 = pts_global[:, 2]
        v1 = p1 - p0
        v2 = p2 - p0
        normal = np.cross(v1, v2)
        norm = np.linalg.norm(normal)
        if norm < 1e-20:
            normal = np.array([0.0, 0.0, 1.0])
        else:
            normal = normal / norm
        x_n, y_n, z_n = normal
        sqrt_xy = np.sqrt(x_n**2 + y_n**2)
        if np.isclose(sqrt_xy, 0.0):
            beta_new = 0.0
        else:
            beta_new = 90.0 - np.degrees(np.arctan(np.abs(z_n) / sqrt_xy))
        if np.isclose(x_n, 0.0):
            alpha_new = 90.0 if y_n >= 0 else 270.0
        else:
            alpha_new = np.degrees(np.arctan2(y_n, x_n))
            if x_n < 0 and y_n >= 0:
                alpha_new += 180
            elif x_n < 0 and y_n < 0:
                alpha_new += 180
            elif x_n >= 0 and y_n < 0:
                alpha_new += 360
        alpha_new = alpha_new % 360
        return alpha_new, beta_new

    # ----------------- propagation -----------------
    a0 = 0.1
    sigma_x = 92e6
    sigma_y = 92e6
    sigma_z = 63e6
    P = 80e6
    nu = 0.25
    alpha = 0.0
    beta = 45.0
    inc = 0.01
    nsteps = 20
    phi_angles = np.arange(0, 360, 10)   # 0..350

    # initial gold SIFs
    l, m, n = normal_vector(alpha, beta)
    sigma_ext, tau, shear_vec = stresses_on_plane(l, m, n, sigma_x, sigma_y, sigma_z)
    sigma_eff = P - sigma_ext
    tau_eff = tau
    omega = shear_angle(*shear_vec, alpha, beta)
    gold_sifs_initial = []
    for phi in phi_angles:
        ki, kii, kiii = circular_sifs(phi, a0, sigma_eff, tau_eff, omega, nu)
        gold_sifs_initial.append([ki, kii, kiii])
    gold_sifs_initial = np.array(gold_sifs_initial)

    # propagation
    a = a0
    b = a0
    gamma = 0.0
    for step in range(nsteps):
        l, m, n = normal_vector(alpha, beta)
        sigma_ext, tau, shear_vec = stresses_on_plane(l, m, n, sigma_x, sigma_y, sigma_z)
        sigma_eff = P - sigma_ext
        tau_eff = tau
        omega = shear_angle(*shear_vec, alpha, beta)

        if step == 0:
            # ----- circular crack step -----
            KII_vals = []
            for phi in phi_angles:
                _, kii, _ = circular_sifs(phi, a, sigma_eff, tau_eff, omega, nu)
                KII_vals.append(kii)
            idx_zero = np.argmin(np.abs(KII_vals))
            phi_zero = phi_angles[idx_zero]
            phi_max = (phi_zero + 90) % 360
            ki_max, kii_max, _ = circular_sifs(phi_max, a, sigma_eff, tau_eff, omega, nu)
            theta_c_max = mts_critical_angle(ki_max, kii_max)

            theta_c_arr = []
            for phi in phi_angles:
                ki, kii, _ = circular_sifs(phi, a, sigma_eff, tau_eff, omega, nu)
                theta_c_arr.append(mts_critical_angle(ki, kii))
            theta_c_arr = np.array(theta_c_arr)

            h_arr = inc * np.sin(np.radians(theta_c_max)) * np.cos(np.radians(phi_angles - phi_max))
            length_arr = np.full_like(phi_angles, np.nan, dtype=float)
            for i, phi in enumerate(phi_angles):
                thc = theta_c_arr[i]
                if np.abs(thc) < 1e-12:
                    length_arr[i] = np.nan
                else:
                    length_arr[i] = a + h_arr[i] / np.tan(np.radians(thc))

            nan_idx = np.isnan(length_arr)
            if np.any(nan_idx):
                for i in np.where(nan_idx)[0]:
                    left = (i - 1) % len(length_arr)
                    right = (i + 1) % len(length_arr)
                    vals = []
                    if not np.isnan(length_arr[left]):
                        vals.append(length_arr[left])
                    if not np.isnan(length_arr[right]):
                        vals.append(length_arr[right])
                    length_arr[i] = np.mean(vals) if vals else a + inc * np.cos(np.radians(theta_c_max))

            R_arr = np.sqrt(length_arr**2 + h_arr**2)
            a_new = np.max(R_arr)
            b_new = np.min(R_arr)
            gamma_new = phi_angles[np.argmax(R_arr)]

            def compute_global_point(ang):
                idx = np.where(np.isclose(phi_angles, ang))[0][0]
                f_pt = length_arr[idx] * np.cos(np.radians(ang))
                g_pt = length_arr[idx] * np.sin(np.radians(ang))
                h_pt = h_arr[idx]
                return global_coords(f_pt, g_pt, h_pt, alpha, beta)

            pts = np.array([compute_global_point(ang) for ang in [0, 90, 180]]).T
            alpha_new, beta_new = plane_from_points(pts)
            a, b, gamma, alpha, beta = a_new, b_new, gamma_new, alpha_new, beta_new

        else:
            # ----- elliptical crack step -----
            ratio = b / a
            if np.isclose(b, a):
                k = 0.0
                kprime = 1.0
            else:
                k = np.sqrt(1 - ratio**2)
                kprime = ratio
            if np.isclose(k, 0.0):
                Ek = np.pi / 2
                Kk = np.pi / 2
            else:
                Ek = ellipe(k**2)
                Kk = ellipk(k**2)
            B_val = (k**2 - nu) * Ek + nu * kprime**2 * Kk
            C_val = (k**2 + nu * kprime**2) * Ek - nu * kprime**2 * Kk

            tan_om = np.tan(np.radians(omega))
            if np.isclose(B_val * tan_om, 0.0):
                phi_zero = 90.0 if -kprime * C_val >= 0 else 270.0
            else:
                phi_zero = np.degrees(np.arctan2(-kprime * C_val, B_val * tan_om)) % 360

            phi_max = (phi_zero + 90) % 360
            ki_max, kii_max, _ = elliptical_sifs(phi_max, a, b, gamma, sigma_eff, tau_eff, omega, nu)
            theta_c_max = mts_critical_angle(ki_max, kii_max)

            theta_c_arr = []
            for phi in phi_angles:
                ki, kii, _ = elliptical_sifs(phi, a, b, gamma, sigma_eff, tau_eff, omega, nu)
                theta_c_arr.append(mts_critical_angle(ki, kii))
            theta_c_arr = np.array(theta_c_arr)

            h_arr = inc * np.sin(np.radians(theta_c_max)) * np.cos(np.radians(phi_angles - phi_max))
            length_arr = np.full_like(phi_angles, np.nan, dtype=float)
            for i, phi in enumerate(phi_angles):
                phi_rad = np.radians(phi)
                gam_rad = np.radians(gamma)
                dist = np.sqrt(
                    (a * np.cos(phi_rad) * np.cos(gam_rad) - b * np.sin(phi_rad) * np.sin(gam_rad))**2 +
                    (a * np.cos(phi_rad) * np.sin(gam_rad) + b * np.sin(phi_rad) * np.cos(gam_rad))**2
                )
                thc = theta_c_arr[i]
                if np.abs(thc) < 1e-12:
                    length_arr[i] = np.nan
                else:
                    length_arr[i] = dist + h_arr[i] / np.tan(np.radians(thc))

            nan_idx = np.isnan(length_arr)
            if np.any(nan_idx):
                for i in np.where(nan_idx)[0]:
                    left = (i - 1) % len(length_arr)
                    right = (i + 1) % len(length_arr)
                    vals = []
                    if not np.isnan(length_arr[left]):
                        vals.append(length_arr[left])
                    if not np.isnan(length_arr[right]):
                        vals.append(length_arr[right])
                    phi_rad = np.radians(phi_angles[i])
                    gam_rad = np.radians(gamma)
                    dist_i = np.sqrt(
                        (a * np.cos(phi_rad) * np.cos(gam_rad) - b * np.sin(phi_rad) * np.sin(gam_rad))**2 +
                        (a * np.cos(phi_rad) * np.sin(gam_rad) + b * np.sin(phi_rad) * np.cos(gam_rad))**2
                    )
                    length_arr[i] = np.mean(vals) if vals else dist_i + inc * np.cos(np.radians(theta_c_max))

            phi_actual_arr = np.array([phi_actual_from_apparent(phi, a, b) for phi in phi_angles])
            f_arr = length_arr * np.cos(np.radians(phi_actual_arr))
            g_arr = length_arr * np.sin(np.radians(phi_actual_arr))
            R_arr = np.sqrt(f_arr**2 + g_arr**2 + h_arr**2)
            a_new = np.max(R_arr)
            b_new = np.min(R_arr)
            gamma_new = phi_angles[np.argmax(R_arr)]

            def compute_global_point(ang):
                idx = np.where(np.isclose(phi_angles, ang))[0][0]
                f_pt = f_arr[idx]
                g_pt = g_arr[idx]
                h_pt = h_arr[idx]
                return global_coords(f_pt, g_pt, h_pt, alpha, beta)

            pts = np.array([compute_global_point(ang) for ang in [0, 90, 180]]).T
            alpha_new, beta_new = plane_from_points(pts)
            a, b, gamma, alpha, beta = a_new, b_new, gamma_new, alpha_new, beta_new

    # final fitted elliptical crack front (on plane, h=0)
    gold_final_front = []
    for phi in phi_angles:
        gam_rad = np.radians(gamma)
        phi_rad = np.radians(phi)
        f_val = a * np.cos(phi_rad) * np.cos(gam_rad) - b * np.sin(phi_rad) * np.sin(gam_rad)
        g_val = a * np.cos(phi_rad) * np.sin(gam_rad) + b * np.sin(phi_rad) * np.cos(gam_rad)
        h_val = 0.0
        x, y, z = global_coords(f_val, g_val, h_val, alpha, beta)
        gold_final_front.append([x, y, z])
    gold_final_front = np.array(gold_final_front)

    return {"gold_sifs_initial": gold_sifs_initial, "gold_final_front": gold_final_front}


# === block: score_0 (check id='step_initial_sifs') ===
def score_0(artifact, step, ctx):
    tol = step.get("tolerance_abs", 1e-6)
    gold = ctx["gold_sifs_initial"]
    if artifact is None or len(artifact) != len(gold):
        return 0.0
    agent_arr = np.array([[float(r["KI"]), float(r["KII"]), float(r["KIII"])] for r in artifact])
    max_diff = np.max(np.abs(agent_arr - gold))
    return 1.0 if max_diff <= tol else 0.0


# === block: score_1 (check id='step_final_front') ===
def score_1(artifact, step, ctx):
    tol = step.get("tolerance_abs", 0.001)
    gold = ctx["gold_final_front"]
    if artifact is None or len(artifact) != len(gold):
        return 0.0
    agent_arr = np.array([[float(r["x"]), float(r["y"]), float(r["z"])] for r in artifact])
    diff = agent_arr - gold
    rmse = float(np.sqrt(np.mean(np.sum(diff**2, axis=1))))
    return 1.0 if rmse <= tol else 0.0


_SCORERS = {
    'step_initial_sifs': score_0,
    'step_final_front': score_1,
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
