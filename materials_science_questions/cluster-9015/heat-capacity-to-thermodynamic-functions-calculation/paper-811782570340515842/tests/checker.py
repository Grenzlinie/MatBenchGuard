import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, csv, math

def _install(pkg):
    try:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir',
             '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', pkg],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

_install('numpy')
_install('scipy')

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
    # ---------- constants ----------
    Tc = 561.75
    rhoc = 3.90
    R = 8.3145
    Tt = 278.680
    rt_t = 11.4766          # triple-point liquid density
    sigma_t = rt_t / rhoc   # reduced density at triple point

    # vapor pressure eq (2) coefficients
    vp_a = -10.655375280
    vp_b = 23.941912372
    vp_c = -22.388714756
    vp_d = 20.208593271
    vp_e = -7.219556515
    vp_f = 4.847283265
    vp_p = 1.70

    # liquid orthobaric density eq (3) coefficients
    rl_a = 1.9600182
    rl_b = 1.0628812
    rl_c = -1.5856640
    rl_d = 2.0926704
    beta_l = 0.35

    # vapour Z-factor eq (4) coefficients
    Zc = 0.26767
    Zv_A1 = -0.992134044
    Zv_A2 = -3.848838300
    Zv_A3 = 0.426708100
    Zv_A4 = -19.955562000
    Zv_beta = 0.35

    # EOS parameters
    alpha = 0.20
    gamma = 0.50
    delta = 5.0
    eta = 1.10
    A1 = 0.743559507
    A2_ = 0.397531574
    A3 = -0.765372414
    A4 = 0.504701641
    A5 = 0.620969008

    # ---------- helper functions ----------
    def P_sigma(T):
        x = T / Tc
        lnP = vp_a/x + vp_b + vp_c*x + vp_d*x**2 + vp_e*x**3 + vp_f*(1-x)**vp_p
        return math.exp(lnP)

    def rho_l(T):
        u = 1.0 - T/Tc
        return rhoc * (1.0 + rl_a*u**beta_l + rl_b*u + rl_c*u**2 + rl_d*u**3)

    def Z_sigma(T):
        x = T/Tc
        u = 1.0 - x
        gx = 1.0   # n=0 at T>=Tt, but for T<Tt it's (T/Tt)^3; we are far above Tt
        f = Zv_A1*u**Zv_beta + Zv_A2*u + Zv_A3*u**2 + Zv_A4*u**3
        return 1.0 + (Zc - 1.0)*gx*math.exp(f)

    def rho_g(T):
        Ps = P_sigma(T)
        Z = Z_sigma(T)
        return Ps / (Z * R * T)

    def T_sigma(rho):
        if abs(rho - rhoc) < 1e-10:
            return Tc
        if rho > rhoc:
            # liquid branch
            if rho >= rho_l(Tt):
                # bracket between Tt and Tc
                def f(T):
                    if T <= Tt or T >= Tc:
                        return 1e10
                    return rho_l(T) - rho
                try:
                    T_guess = Tt + (Tc - Tt) * 0.8
                    sol = fsolve(f, T_guess, maxfev=1000, xtol=1e-10)
                    return float(sol[0])
                except:
                    return None
            else:
                return None   # should not happen
        else:
            # vapour branch
            def f(T):
                if T <= Tt or T >= Tc:
                    return 1e10
                return rho_g(T) - rho
            try:
                T_guess = Tt + (Tc - Tt) * 0.99
                sol = fsolve(f, T_guess, maxfev=1000, xtol=1e-10)
                return float(sol[0])
            except:
                return None

    def theta_rho(rho, T_sig):
        sigma = rho/rhoc
        g = abs(sigma - 1.0)**3 / (sigma_t - 1.0)**3
        return T_sig * math.exp(-alpha * g)

    def omega(rho, T, T_sig):
        th = theta_rho(rho, T_sig)
        return 1.0 - th / T

    def psi(rho, T, T_sig):
        w = omega(rho, T, T_sig)
        return w - w**eta / eta

    def F_func(rho, T, T_sig):
        u = T / T_sig
        f2 = math.log((1.0 + u*u) / 2.0)
        f3 = math.log(1.0 + delta * (u - 1.0)) / delta
        psi_T = psi(rho, T, T_sig)
        psi_sig = psi(rho, T_sig, T_sig)
        f4 = (psi_sig - psi_T) * eta / (eta - 1.0)
        D = A3 + A4 * rho
        E = A5 * (rho - 1.0) * math.exp(-gamma * rho * rho)
        return A1*(u-1) + A2_*rho*f2 + D*f3 + E*f4

    def P_EOS(rho, T):
        T_sig = T_sigma(rho)
        if T_sig is None:
            return None
        Ps = P_sigma(T_sig) if T_sig > 0 else 0.0
        sigma = rho/rhoc
        F = F_func(rho, T, T_sig) if T_sig > 0 else 0.0
        return Ps + rho*R*(T - T_sig) + sigma*(rho*R*Tc)*F

    # ---------- compute references ----------
    reduced_densities = [0.50, 0.70, 0.90, 1.00, 1.10, 1.30, 1.50]
    ref = {}
    for sigma in reduced_densities:
        rho = sigma * rhoc
        if abs(sigma - 1.0) < 1e-12:
            # critical point – T_sigma = Tc, P = Pc
            T_sig = Tc
            Ps = P_sigma(Tc)
            # EOS at critical point: compute directly
            F = F_func(rho, Tc, Tc)  # should be ~0
            P = Ps + rho*R*(Tc - Tc) + sigma*(rho*R*Tc)*F
            ref[sigma] = (P, 'abs')
        else:
            T_sig = T_sigma(rho)
            if T_sig is None:
                ref[sigma] = (None, None)
                continue
            P = P_EOS(rho, Tc)
            ref[sigma] = (P, 'rel')

    ctx = {'ref': ref}
    return ctx


# === block: score_0 (check id='critical_isotherm') ===
def score_0(artifact, step, ctx):
    ref_map = ctx['ref']
    pts = 0
    total = 0
    for row in artifact:
        try:
            sigma = float(row.get('reduced_density', None))
            P_agent = float(row.get('P_bar', None))
        except (ValueError, TypeError):
            continue
        entry = ref_map.get(sigma)
        if entry is None or entry[0] is None:
            continue
        P_ref, kind = entry
        total += 1
        if kind == 'rel':
            rel_err = abs((P_agent - P_ref) / P_ref) if P_ref != 0 else abs(P_agent - P_ref)
            if rel_err <= 0.005:
                pts += 1
        else:  # abs at critical point
            if abs(P_agent - P_ref) <= 0.01:
                pts += 1
    # score = fraction of valid points that pass
    if total == 0:
        # fallback: if no matching rows, score 0
        score = 0.0
    else:
        score = pts / total
    return score


_SCORERS = {
    'critical_isotherm': score_0,
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
