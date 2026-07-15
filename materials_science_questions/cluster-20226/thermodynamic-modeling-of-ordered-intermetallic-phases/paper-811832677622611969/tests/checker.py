import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import brentq

# free energy model (dimensionless)
def _phi_derivs(t, c, Pi, lam, eta_c, eta_cc):
    eps = eta_c * c + 0.5 * eta_cc * c * c
    eps_prime = eta_c + eta_cc * c
    # phi
    phi = t * (c * np.log(c) + (1 - c) * np.log(1 - c)) + 2 * c * (1 - c) - 4.5 * Pi * Pi + 3 * np.sqrt(lam) * eps * Pi
    dphi_dc = t * np.log(c / (1 - c)) + 2 * (1 - 2 * c) + 3 * np.sqrt(lam) * eps_prime * Pi
    dphi_dPi = -9 * Pi + 3 * np.sqrt(lam) * eps
    omega = phi - dphi_dc * c - dphi_dPi * Pi
    return phi, dphi_dc, dphi_dPi, omega

def _spino_t(c, lam, eta_c, eta_cc, Pi):
    return c * (1 - c) * (4 - lam * (eta_c + eta_cc * c) ** 2 - 3 * eta_cc * np.sqrt(lam) * Pi)

def _spino_dt_dc(c, lam, eta_c, eta_cc, Pi):
    # derivative of spinodal t w.r.t c
    u = c * (1 - c)
    v = 4 - lam * (eta_c + eta_cc * c) ** 2 - 3 * eta_cc * np.sqrt(lam) * Pi
    du_dc = 1 - 2 * c
    dv_dc = -2 * lam * eta_cc * (eta_c + eta_cc * c)
    return du_dc * v + u * dv_dc

def _cp_from_model(lam, eta_c, eta_cc, Pi):
    # find c where dt/dc=0 between 0 and 1
    lo, hi = 0.001, 0.999
    # ensure sign change
    f = lambda c: _spino_dt_dc(c, lam, eta_c, eta_cc, Pi)
    if f(lo) * f(hi) > 0:
        # fallback scan
        cs = np.linspace(lo, hi, 2001)
        vals = f(cs)
        sign_chg = np.where(np.diff(np.sign(vals)))[0]
        if len(sign_chg) == 0:
            return None, None
        lo = cs[sign_chg[0]]
        hi = cs[sign_chg[0] + 1]
    try:
        c_root = brentq(f, lo, hi, xtol=1e-12)
    except ValueError:
        return None, None
    t_root = _spino_t(c_root, lam, eta_c, eta_cc, Pi)
    return t_root, c_root


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


# === block: score_0 (check id='step_01_compute_phase_diagram_data') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    param_sets = [
        ('L100_eta_c_-0.05_eta_cc_0.04', 100, -0.05, 0.04),
        ('L100_eta_c_-0.03_eta_cc_0', 100, -0.03, 0.0),
        ('L100_eta_c_-0.01_eta_cc_-0.04', 100, -0.01, -0.04),
        ('L350_eta_c_-0.05_eta_cc_0.05', 350, -0.05, 0.05),
    ]
    sub_weights = {'cp': 0.3, 'spino': 0.15, 'tie': 0.25, 'effect': 0.2, 'struct': 0.1}
    per_pset_scores = []
    for key, lam, eta_c, eta_cc in param_sets:
        obj = data.get(key)
        if not isinstance(obj, dict):
            per_pset_scores.append(0.0)
            continue
        # 1) critical point
        cp = obj.get('critical_point')
        cp_score = 0.0
        if isinstance(cp, dict) and all(k in cp for k in ('t_c', 'c_c')):
            t_gold, c_gold = _cp_from_model(lam, eta_c, eta_cc, 0.1)
            if t_gold is not None:
                dt = abs(cp['t_c'] - t_gold)
                dc = abs(cp['c_c'] - c_gold)
                tol_t = step.get('tolerances', {}).get('critical_point_t_abs', 0.005)
                tol_c = step.get('tolerances', {}).get('critical_point_c_abs', 0.005)
                cp_score = max(0.0, 1.0 - max(dt / tol_t, dc / tol_c))
            else:
                cp_score = 1.0  # cannot check; give benefit of doubt
        # 2) spinodal at Pi=0.1
        sp = obj.get('spinodal_at_Pi_0_1')
        spino_score = 0.0
        if isinstance(sp, dict) and 't' in sp and 'c' in sp:
            t_arr = np.asarray(sp['t'], dtype=float)
            c_arr = np.asarray(sp['c'], dtype=float)
            if len(t_arr) == len(c_arr) and len(t_arr) >= 10:
                t_model = _spino_t(c_arr, lam, eta_c, eta_cc, 0.1)
                dt = np.abs(t_arr - t_model)
                tol = step.get('tolerances', {}).get('spinodal_t_abs', 0.01)
                pass_frac = np.mean(dt < tol)
                spino_score = max(0.0, pass_frac - 0.2) / 0.8 if pass_frac > 0.2 else 0.0
                spino_score = min(1.0, spino_score)
            else:
                spino_score = 0.0
        # 3) tie-lines at t=0.8, Pi_o=0.1
        ties = obj.get('tie_lines_at_t_0_8')
        tie_score = 0.0
        if isinstance(ties, list) and len(ties) >= 2:
            residuals = []
            for tl in ties:
                if not isinstance(tl, dict) or not all(k in tl for k in ('c_alpha','Pi_alpha','c_beta','Pi_beta')):
                    continue
                _, dcdc_a, dpia, omega_a = _phi_derivs(0.8, tl['c_alpha'], tl['Pi_alpha'], lam, eta_c, eta_cc)
                _, dcdc_b, dpib, omega_b = _phi_derivs(0.8, tl['c_beta'], tl['Pi_beta'], lam, eta_c, eta_cc)
                res = max(abs(dcdc_a - dcdc_b), abs(dpia - dpib), abs(omega_a - omega_b))
                residuals.append(res)
            if residuals:
                max_res = max(residuals)
                tol = step.get('tolerances', {}).get('tie_line_residual_max', 0.001)
                if max_res < tol:
                    tie_score = 1.0
                else:
                    tie_score = max(0.0, 1.0 - (max_res - tol) / tol)
            else:
                tie_score = 0.0
        else:
            tie_score = 0.0
        # 4) effect_of_Pi
        eff = obj.get('effect_of_Pi')
        effect_score = 0.0
        if isinstance(eff, dict) and 'Pi' in eff and 'gap_width' in eff:
            pi_arr = np.asarray(eff['Pi'], dtype=float)
            gw_arr = np.asarray(eff['gap_width'], dtype=float)
            if len(pi_arr) >= 4 and len(pi_arr) == len(gw_arr):
                slope = np.polyfit(pi_arr, gw_arr, 1)[0]
                if eta_cc > 0:
                    # gap should shrink -> negative slope
                    if slope < -0.001:
                        effect_score = 1.0
                    else:
                        effect_score = max(0.0, 1.0 - abs(slope) / 0.01)
                elif eta_cc < 0:
                    # gap should widen -> positive slope
                    if slope > 0.001:
                        effect_score = 1.0
                    else:
                        effect_score = max(0.0, 1.0 - abs(slope) / 0.01)
                else:  # eta_cc == 0, gap should be constant
                    if abs(slope) < step.get('tolerances', {}).get('effect_slope_tol_within_etta_cc_zero', 0.01):
                        effect_score = 1.0
                    else:
                        effect_score = max(0.0, 1.0 - abs(slope) / 0.05)
            else:
                effect_score = 0.0
        # 5) structural: spinodal maximum matches critical point
        struct_score = 0.0
        if isinstance(cp, dict) and 't_c' in cp and 'c_c' in cp and isinstance(sp, dict) and 't' in sp and 'c' in sp:
            t_arr = np.asarray(sp['t'])
            c_arr = np.asarray(sp['c'])
            if len(t_arr) > 0:
                imax = np.argmax(t_arr)
                t_max = t_arr[imax]
                c_max = c_arr[imax]
                dt_top = abs(t_max - cp['t_c'])
                dc_top = abs(c_max - cp['c_c'])
                if dt_top < 0.01 and dc_top < 0.01:
                    struct_score = 1.0
                else:
                    struct_score = max(0.0, 1.0 - max(dt_top/0.01, dc_top/0.01))
            else:
                struct_score = 0.0
        pset_score = (cp_score * sub_weights['cp'] +
                      spino_score * sub_weights['spino'] +
                      tie_score * sub_weights['tie'] +
                      effect_score * sub_weights['effect'] +
                      struct_score * sub_weights['struct'])
        per_pset_scores.append(pset_score)
    if len(per_pset_scores) == 0:
        return 0.0
    return float(np.mean(per_pset_scores))


_SCORERS = {
    'step_01_compute_phase_diagram_data': score_0,
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
