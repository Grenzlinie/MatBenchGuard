import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import fresnel
from scipy.integrate import quad
import math

# Physical constants for unit conversion
_hbar_eVs = 6.582119569e-16      # eV*s
_m0_kg = 9.10938356e-31          # kg
_e_C = 1.602176634e-19           # C
# Atomic units
_Hartree_eV = 27.21138456937
_a0_m = 5.29177210903e-11
_E_atom_Vm = 5.142206747e11      # V/m (e/(4*pi*eps0*a0^2))

def _compute_icfe_k(P_eV, Q_eV2):
    # P, Q in eV and eV^2
    if abs(Q_eV2) < 1e-30:
        return 0.0, 0.0  # avoid division by zero
    P2 = P_eV * P_eV
    Q_abs = abs(Q_eV2)
    # Fresnel argument: x = P*Q / (2*|Q|^3)^(1/2)
    # = (P / sqrt(2*|Q|))
    arg = P_eV / math.sqrt(2.0 * Q_abs)
    # Use scipy.special.fresnel returns S, C (both normalized)
    S, C = fresnel(arg)
    # The paper uses C(x) and S(x) defined with sqrt(2/pi) prefactor, which matches scipy's fresnel (returns normalized integrals).
    # Equation (11): K = sqrt(pi/|Q|) * { cos(P^2/(2|Q|)) * [1 - 2*C] + sin(P^2/(2|Q|)) * [1 - 2*S] }
    phi = P2 / (2.0 * Q_abs)
    K_exact = math.sqrt(math.pi / Q_abs) * (math.cos(phi) * (1.0 - 2.0*C) + math.sin(phi) * (1.0 - 2.0*S))
    # Lorentzian (eq. 15): K = 2*(|Q|/(2*pi))^(1/2) / ( |Q|/(2*pi) + [ -P - Q/((2/pi)*|Q|)^(1/2) ]^2 )
    term = math.sqrt( (2.0/math.pi) * Q_abs )
    denom = Q_abs/(2.0*math.pi) + ( -P_eV - Q_eV2/term )**2
    K_lorentz = 2.0 * math.sqrt(Q_abs/(2.0*math.pi)) / denom if denom > 1e-30 else 0.0
    return K_exact, K_lorentz

def _compute_cb_K(eps_init_eV, eps_final_eV, omega0_eV=0.04, gamma2_eV=0.0011):
    # eq. (23) dimensionless
    xi = eps_init_eV / gamma2_eV
    xf = eps_final_eV / gamma2_eV
    x0 = omega0_eV / gamma2_eV
    # integration range: x from 2*x0 to infinity
    def integrand(x):
        term1 = np.sqrt(x - x0) * np.sqrt(x - 2.0*x0)
        denom1 = (x - xi)**2 + (x - x0)
        denom2 = (x - x0 - xf)**2 + (x - 2.0*x0)
        return term1 / (denom1 * denom2)
    # numerical integration
    integral_val, _ = quad(integrand, 2.0*x0, np.inf, limit=200)
    # Theta functions: only include integral if both xi > x0 and xf > x0
    factor = 0.0
    if xi > x0 and xf > x0:
        factor += integral_val
    # Second term: pi * sqrt(xf) * theta(xi-x0)*theta(x0-xf)*theta(xf) / ((x0+xf-xi)^2 + xf)
    if xi > x0 and xf >= 0 and xf <= x0:
        factor += math.pi * math.sqrt(max(xf, 0)) / ((x0 + xf - xi)**2 + xf)
    # Third delta term: pi^2 * delta(x0+xf-xi) * theta(x0-xi)*theta(x0-xf)
    if abs(x0 + xf - xi) < 1e-12 and xi <= x0 and xf <= x0:
        factor += math.pi**2 * 1e10  # delta approximated by large peak? Not used in practice.
    K = (2.0 / (math.pi * gamma2_eV**2)) * factor
    return K

def _recompute_row(row):
    typ = row.get('type', '').strip().upper()
    model = row.get('model', '').strip().lower()
    if typ == 'ICFE':
        field_kVcm = float(row.get('field_kVcm', 0))
        P_eV = float(row.get('P_eV', 0))
        # initial_energy_eV is 1 eV per paper
        eps_init = 1.0  # fixed
        omega0 = 0.04
        # compute final kinetic energy: epsilon' = P + eps_init + omega0 (emission, eta=+1)
        eps_final = P_eV + eps_init + omega0
        m_eff = 0.3  # m0
        # Compute q magnitude (maximum alignment) for given energies
        m_eff_SI = m_eff * _m0_kg
        # kinetic energy in Joules
        eps_J = eps_init * _e_C
        epsf_J = eps_final * _e_C
        # k = sqrt(2*m*E) / hbar
        k_i = math.sqrt(2.0 * m_eff_SI * eps_J) / (_hbar_eVs * _e_C)  # k in 1/m
        k_f = math.sqrt(2.0 * m_eff_SI * epsf_J) / (_hbar_eVs * _e_C) if eps_final > 0 else 0.0
        q_max = k_i + k_f  # 1/m
        # Electric field in V/m
        E_Vm = float(field_kVcm) * 1e5   # kV/cm -> V/m
        # Q_eV2 = hbar * q_max * E_Vm / (m_eff_SI) but need conversion to eV^2
        # q * E has units (1/m)*(V/m) = V/m^2
        # Q_SI = (hbar * q * E) / m_eff  (units: J? Actually hbar*q: kg*m/s, times E: kg*m^2/s^3?)
        # Let's derive: Q = eta (q·E)/m. In SI, q has kg*m/s, E has V/m = J/(C*m) = N/C.
        # So q*E has (kg*m/s)*(N/C) = (kg*m/s)*(kg*m/s^2 / C) = kg^2 * m^2 / (s^3 C)
        # m has kg, result units: kg * m^2 / (s^3 C). Not energy squared.
        # There is confusion; using SI units may not be straightforward.
        # Instead, we rely on atomic units in the scoring; we assume both agent and checker use the same practical eV-based formulation.
        # The paper's Q is in units of energy^2. We'll compute Q in eV^2 using a standard conversion.
        # In semiconductors, often use: k = sqrt(2*m*epsilon) / hbar, q in 1/m, E in V/m, Q = hbar * e * q·E / (m) maybe?
        # The original equation: Q = η (q·E)/m (with hbar=1). To get Q in eV^2, we need to include hbar and e.
        # Typically, Q = (hbar * q * e * E) / (m) in SI yields units of J*s * 1/m * C * V/m / kg = J*s * C/m^2 * J/C / kg = J^2*s/kg.
        # Not eV^2.
        # Given the difficulty, we approximate Q using the maximum possible value in eV^2 by scaling.
        # For the paper's figure, they used maximum of B, which likely corresponds to q aligned with E.
        # We'll compute a scale: use effective field in atomic units.
        # To avoid unit headache, we will match the agent's numbers only if the unit conversion matches our implementation.
        # For the purpose of this checker, we use a simplified consistent atomic-unit conversion:
        # Convert epsilon to Hartree, m to m0 (dimensionless), E to atomic field.
        # 1 Hartree = 27.2114 eV
        eps_init_au = eps_init / _Hartree_eV
        eps_final_au = eps_final / _Hartree_eV
        m_au = m_eff
        # k_au = sqrt(2*m*eps_init_au)
        k_i_au = math.sqrt(2.0 * m_au * eps_init_au)
        k_f_au = math.sqrt(2.0 * m_au * eps_final_au) if eps_final_au > 0 else 0.0
        q_max_au = k_i_au + k_f_au
        # Electric field in atomic units: E_at = E_SI / E_at_SI
        E_Vm = float(field_kVcm) * 1e5
        E_at = E_Vm / _E_atom_Vm
        # Q in atomic units: Q_at = η (q·E)/m, with η=1. Energy in Hartree, length in Bohr, time in hbar/Hartree.
        # Q has units Hartree^2. Then convert to eV^2: multiply by Hartree_eV^2.
        Q_au = (q_max_au * E_at) / m_au
        Q_eV2 = Q_au * (_Hartree_eV**2)
    else:
        Q_eV2 = 0.0
        P_eV = float(row.get('P_eV', 0)) if row.get('P_eV') else 0.0
    if typ == 'ICFE':
        K_exact, K_lorentz = _compute_icfe_k(P_eV, Q_eV2)
        if model == 'exact':
            return K_exact
        elif model == 'lorentzian':
            return K_lorentz
        else:
            return None
    elif typ == 'CB':
        eps_init = float(row.get('initial_energy_eV', 0))
        eps_final = float(row.get('final_energy_eV', 0))
        return _compute_cb_K(eps_init, eps_final, 0.04, 0.0011)
    else:
        return None


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


# === block: score_0 (check id='step_jsd') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts
    if not artifact or len(artifact)==0:
        return 0.0
    tol_rel = step.get('tol_rel', 0.001)
    tol_abs = step.get('tol_abs', 1e-6)
    passed = 0
    total = 0
    for row in artifact:
        try:
            K_agent = float(row.get('K', float('nan')))
            K_comp = _recompute_row(row)
            if K_comp is None:
                continue
            total += 1
            if abs(K_comp) > 1e-9:
                err = abs(K_agent - K_comp) / abs(K_comp)
            else:
                err = abs(K_agent - K_comp)
            if err <= tol_rel or abs(K_agent - K_comp) <= tol_abs:
                passed += 1
        except Exception:
            continue
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='step_dist') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts
    if not artifact:
        return 0.0
    # separate rows by condition
    data_wo = []
    data_wi = []
    for row in artifact:
        cond = row.get('condition','').strip()
        if cond == 'without_CB':
            data_wo.append((float(row['energy_eV']), float(row['probability_density'])))
        elif cond == 'with_CB':
            data_wi.append((float(row['energy_eV']), float(row['probability_density'])))
    if not data_wo or not data_wi:
        return 0.0

    # helper: find nearest bin
    def find_nearest(data, target):
        best = None
        for e, p in data:
            if best is None or abs(e-target) < abs(best[0]-target):
                best = (e, p)
        return best[0], best[1] if best else (None, None)

    sub_score = 0.0
    # 1. without_CB shape: prob at ~1 eV should be > prob at ~2 eV (decay)
    e1, p1 = find_nearest(data_wo, 1.0)
    e2, p2 = find_nearest(data_wo, 2.0)
    if p1 is not None and p2 is not None and p1 > p2:
        sub_score += 0.3

    # 2. Tail enhancement: average prob for energy >= 2.0 eV should be higher for with_CB
    wo_tail = [p for e,p in data_wo if e >= 2.0]
    wi_tail = [p for e,p in data_wi if e >= 2.0]
    if wo_tail and wi_tail:
        avg_wo = sum(wo_tail)/len(wo_tail)
        avg_wi = sum(wi_tail)/len(wi_tail)
        if avg_wi > avg_wo:
            sub_score += 0.4

    # 3. Normalization: integral ~1
    def check_norm(data):
        if len(data) < 2:
            return False
        # assume uniform bin widths
        diffs = [data[i+1][0] - data[i][0] for i in range(len(data)-1)]
        bw = sum(diffs)/len(diffs) if diffs else 0.0
        area = sum(p * bw for e,p in data)
        return abs(area - 1.0) < 0.01

    if check_norm(data_wo) and check_norm(data_wi):
        sub_score += 0.3

    return min(sub_score, 1.0)


# === block: score_2 (check id='step_vd') ===
def score_2(artifact, step, ctx):
    # artifact list of dicts with condition, drift_velocity_cm_s
    v_without = None
    v_with = None
    for row in artifact:
        cond = row.get('condition','').strip()
        vel = float(row.get('drift_velocity_cm_s', 0))
        if cond == 'without_CB':
            v_without = vel
        elif cond == 'with_CB':
            v_with = vel
    if v_without is None or v_with is None:
        return 0.0
    if v_without <= 0 or v_with <= 0:
        return 0.0
    if v_with >= v_without * 1.1 and v_without >= 5e6:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_jsd': score_0,
    'step_dist': score_1,
    'step_vd': score_2,
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
