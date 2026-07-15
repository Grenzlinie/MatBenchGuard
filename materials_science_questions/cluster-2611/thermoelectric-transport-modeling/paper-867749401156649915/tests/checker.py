import os
import json
import csv

# === author imports / helpers ===
import math

# Physical constants (SI)
k_B = 1.380649e-23
e   = 1.602176634e-19
hbar = 1.054571817e-34
m_e = 9.1093837015e-31

# Minimal NumPy-like shim used by scorer blocks
class _NumpyStub:
    pi = math.pi
    @staticmethod
    def arange(start, stop, step):
        vals = []
        while start <= stop:
            vals.append(start)
            start += step
        return vals
np = _NumpyStub()

# Material constants for the 6.0 nm PbTe quantum well (from the paper)
m_star = 0.0565 * m_e   # kg
Eg = 0.2131              # eV
Delta_SO = 0.77          # eV
F = 1e6                  # V/m  (out-of-plane electric field)

ev_J = e                 # 1 eV in Joules
Eg_J = Eg * ev_J
Delta_J = Delta_SO * ev_J

# alpha = hbar^2 / (2 m*)
alpha = hbar**2 / (2 * m_star)

# Rashba coefficient lambda_R from Eq.15
lambda0 = (alpha * (Delta_SO / Eg) * (2*Eg_J + Delta_J)) / ((Eg_J + Delta_J) * (3*Eg_J + 2*Delta_J))
lambda_R = lambda0 * F


def compute_fermi_energies(n_spin):
    """
    Compute spin-split Fermi energies from Eq.22.
    n_spin : per-spin branch carrier density in m^-2.
    Returns (eps_up, eps_down) in Joules.
    """
    term = math.sqrt(lambda_R**2/(16*math.pi**2*alpha**3) + n_spin/(math.pi*alpha))
    eps_up = (2*math.pi*alpha * (term + lambda_R/(4*math.pi*alpha**1.5)))**2
    eps_down = (2*math.pi*alpha * (term - lambda_R/(4*math.pi*alpha**1.5)))**2
    return eps_up, eps_down


def compute_kf(eps, spin):
    """
    Fermi wave vector from Eq.23.
    spin : 'up' or 'down'.
    eps  : Fermi energy (J).
    """
    disc = math.sqrt(lambda_R**2 + 4*alpha*eps)
    if spin == 'up':
        return (disc - lambda_R) / (2*alpha)
    else:
        return (disc + lambda_R) / (2*alpha)


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


# === block: score_0 (check id='step_01_magneto_thermopower') ===
def score_0(artifact, step, ctx):
        rows = artifact
        # Build dict (B_field, spin) -> (Qxx, Qyx)
        data = {}
        for r in rows:
            B = float(r['B_field'])
            spin = r['spin'].strip().lower()
            Qxx = float(r['Qxx'])
            Qyx = float(r['Qyx'])
            data[(B, spin)] = (Qxx, Qyx)

        # Fixed conditions for magneto-thermopower
        n_total = 1.0e12   # cm^-2
        n_spin_cm2 = n_total / 2.0
        n_spin_m2 = n_spin_cm2 * 1e4   # convert cm^-2 to m^-2

        # Compute spin-split Fermi energies (J) without underflow
        k_B_local = 1.380649e-23
        e_local = 1.602176634e-19
        hbar_local = 1.054571817e-34
        m_e_local = 9.1093837015e-31
        m_star_local = 0.0565 * m_e_local
        alpha_local = hbar_local**2 / (2 * m_star_local)
        Eg_local = 0.2131 * e_local
        Delta_local = 0.77 * e_local
        F_local = 1e6   # V/m
        lambda0_local = alpha_local * (Delta_local / Eg_local) * (2*Eg_local + Delta_local) / ((Eg_local + Delta_local) * (3*Eg_local + 2*Delta_local))
        lambda_R_local = e_local * lambda0_local * F_local
        sqrt_alpha = math.sqrt(alpha_local)
        disc = math.sqrt(lambda_R_local**2 / alpha_local + 16 * math.pi * alpha_local * n_spin_m2)
        y_up = (lambda_R_local / sqrt_alpha + disc) / 2.0
        y_down = (-lambda_R_local / sqrt_alpha + disc) / 2.0
        eps_up = y_up * y_up
        eps_down = y_down * y_down

        tau = 1.0e-10
        s = 0.7
        T = 4.0

        tolerance_abs = 1.0      # 1 uV/K
        tolerance_rel = 0.01     # 1%

        # Expected magnetic field values
        B_vals = np.arange(-3.0, 3.05, 0.5)

        total = 0
        correct = 0
        for B in B_vals:
            # round B to avoid floating-point key mismatches
            Bk = round(B, 10)
            for spin, eps in [('up', eps_up), ('down', eps_down)]:
                key = (Bk, spin)
                if key not in data:
                    continue
                qxx_agent, qyx_agent = data[key]   # already in uV/K
                omega_c = e_local * B / m_star_local
                denom = 1 + (omega_c * tau)**2
                pref = (np.pi**2 * k_B_local**2 * T) / (3 * e_local)   # V/K
                qxx_calc = -pref / eps * (1 + s / denom) * 1e6   # convert to uV/K
                qyx_calc = -pref / eps * (s * omega_c * tau / denom) * 1e6
                # Check Qxx
                ok_xx = abs(qxx_agent - qxx_calc) <= max(tolerance_abs, tolerance_rel * abs(qxx_calc))
                # Check Qyx
                ok_yx = abs(qyx_agent - qyx_calc) <= max(tolerance_abs, tolerance_rel * abs(qyx_calc))
                if ok_xx and ok_yx:
                    correct += 1
                total += 1

        score_numeric = correct / total if total > 0 else 0.0

        # Structural check: spin-up Qxx > spin-down Qxx (less negative)
        ordering_ok = 0
        total_B = 0
        for B in B_vals:
            Bk = round(B, 10)
            key_up = (Bk, 'up')
            key_down = (Bk, 'down')
            if key_up in data and key_down in data:
                qxx_up = data[key_up][0]
                qxx_down = data[key_down][0]
                if qxx_up > qxx_down:
                    ordering_ok += 1
                total_B += 1
        order_score = ordering_ok / total_B if total_B > 0 else 0.0

        return 0.9 * score_numeric + 0.1 * order_score


# === block: score_1 (check id='step_02_power_factor') ===
def score_1(artifact, step, ctx):
        rows = artifact
        data = {}
        for r in rows:
            nd = float(r['carrier_density'])   # cm^-2
            spin = r['spin'].strip().lower()
            pf = float(r['power_factor'])      # uW/cmK^2
            data[(nd, spin)] = pf

        # Physical constants
        k_B = 1.380649e-23
        e   = 1.602176634e-19
        hbar = 1.054571817e-34
        m_e = 9.1093837015e-31
        # Material parameters for 6.0 nm PbTe QW
        m_star = 0.0565 * m_e
        Eg = 0.2131 * e
        Delta = 0.77 * e
        F = 1e6
        alpha = hbar**2 / (2 * m_star)
        # Rashba coefficient (Eq.15) – no e factor
        lambda0 = alpha * (Delta / Eg) * (2*Eg + Delta) / ((Eg + Delta) * (3*Eg + 2*Delta))
        lambda_R = lambda0 * F

        tau = 1.0e-9
        s = 0.7
        T = 1.0

        tolerance_abs = 0.1   # uW/cmK^2
        tolerance_rel = 0.01

        def stable_fermi_energy(n_spin_m2):
            """Return (eps_up, eps_down) in Joules using numerically stable formula."""
            sqrt_alpha = math.sqrt(alpha)
            disc = math.sqrt(lambda_R**2 / alpha + 16 * math.pi * alpha * n_spin_m2)
            y_up = (lambda_R / sqrt_alpha + disc) / 2.0
            y_down = (-lambda_R / sqrt_alpha + disc) / 2.0
            return y_up * y_up, y_down * y_down

        def stable_kf(eps, spin):
            """Fermi wave vector from Eq.23."""
            disc = math.sqrt(lambda_R**2 + 4 * alpha * eps)
            if spin == 'up':
                return (disc - lambda_R) / (2 * alpha)
            else:
                return (disc + lambda_R) / (2 * alpha)

        total = 0
        correct = 0
        for (nd, spin), pf_agent in data.items():
            n_total_cm2 = nd
            n_spin_cm2 = n_total_cm2 / 2.0
            n_spin_m2 = n_spin_cm2 * 1e4
            eps_up, eps_down = stable_fermi_energy(n_spin_m2)
            kf_up = stable_kf(eps_up, 'up')
            kf_down = stable_kf(eps_down, 'down')
            if spin == 'up':
                eps = eps_up
                kf = kf_up
            else:
                eps = eps_down
                kf = kf_down

            eps_safe = max(eps, 1e-60)   # avoid division by zero
            pf_si = (math.pi**3 * k_B**4 * T**2) / (18 * m_star) * (1 + s)**2 / eps_safe**2 * kf**2 * tau   # W/(m·K^2)
            pf_calc = pf_si * 1e4   # convert to uW/(cm·K^2)

            if abs(pf_agent - pf_calc) <= max(tolerance_abs, tolerance_rel * abs(pf_calc)):
                correct += 1
            total += 1

        score_numeric = correct / total if total > 0 else 0.0

        # Structural check: PF_down > PF_up for each carrier density
        densities = sorted(set(k[0] for k in data.keys()))
        order_ok = 0
        total_dens = 0
        for d in densities:
            if (d, 'up') in data and (d, 'down') in data:
                pf_up = data[(d, 'up')]
                pf_down = data[(d, 'down')]
                if pf_down > pf_up:
                    order_ok += 1
                total_dens += 1
        order_score = order_ok / total_dens if total_dens > 0 else 0.0

        return 0.9 * score_numeric + 0.1 * order_score


_SCORERS = {
    'step_01_magneto_thermopower': score_0,
    'step_02_power_factor': score_1,
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
