import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os
import json

# ---------- helper functions ----------
outputs_dir = '/app/outputs'
def polylog_32(z, maxterms=100):
    """Compute g_{3/2}(z) by series expansion. Converges for z<=1."""
    s = 0.0
    for n in range(1, maxterms+1):
        term = z**n / (n**1.5)
        s += term
        if term < 1e-12:
            break
    return s

def ideal_gas_exact_mu(N, T_over_Tc0=1.5):
    """Return mu/(k_B T) for N-particle ideal Bose gas at T/T_c^0.
    Uses recursion with Z_1 = V/lambda_T^3 = N/(n*lambda_T^3).
    n*lambda_T^3 = 2*zeta(3/2) * (T_c0/T)^(3/2).
    """
    zeta32 = 2.612
    n_lambda3 = 2 * zeta32 * (1.0 / T_over_Tc0)**1.5
    Z1 = N / n_lambda3   # = V/lambda_T^3
    # Recursion for max N+1
    max_n = N + 2
    Z = [0.0] * (max_n)
    Z[0] = 1.0
    for n in range(1, max_n):
        total = 0.0
        for m in range(1, n+1):
            total += m**1.5 * Z1 * Z[n-m]
        Z[n] = total / n
    if Z[N] == 0:
        return 0.0
    ratio = Z[N+1] / Z[N]
    return -math.log(ratio)  # mu/(k_B T)

def hf_chemical_potential(T_over_Tc0, na3=1e-6):
    """Compute Hartree-Fock chemical potential in k_B T_c^0 for single-component
    hard-sphere gas with gas parameter na^3. Returns mu/(k_B T_c^0).
    Solves n = n_0 + n_T with n_T = (1/lambda_T^3) * g_{3/2}(exp(-beta*g*n_0)).
    """
    zeta32 = 2.612
    # n*lambda_T^3 at given T/T_c0
    n_lambda3 = 2 * zeta32 * (1.0 / T_over_Tc0)**1.5
    # g*n/(k_B T_c0) = 2*(na^3)^{1/3} * C, with C= (2*zeta32)^{2/3}
    C_const = (2*zeta32)**(2.0/3.0)  # approx 3.01
    g_n_dim = 2.0 * (na3)**(1.0/3.0) * C_const
    # solve for condensate fraction x = n_0 / n
    # equation: x + (1/n_lambda3) * g_{3/2}( e^{-B*x} ) = 1
    # where B = g_n_dim / (T_over_Tc0) * (k_B T_c0^? actually g_n_dim in k_B T_c0, so beta*g*n_0 = g_n_dim * x / (k_B T/T_c0)???
    # Need beta * g * n_0 = (g*n/(k_B T_c0)) * (n_0/n) * (k_B T_c0 / (k_B T))
    # = g_n_dim * x / (T_over_Tc0)
    B = g_n_dim / T_over_Tc0
    f = lambda x: x + (1.0 / n_lambda3) * polylog_32(math.exp(-B * x)) - 1.0
    # bracket [0,1] (if T<T_c, f(0)>0? at T<T_c, f(0) = (1/n_lambda3)*zeta32 -1 >0 => solution >0)
    lo, hi = 0.0, 1.0
    # sometimes at very low T, x=1 maybe not enough; we will binary search with tolerance
    for _ in range(100):
        mid = (lo + hi)/2.0
        fm = f(mid)
        if abs(fm) < 1e-10:
            break
        if fm > 0:
            lo = mid
        else:
            hi = mid
    x_opt = (lo+hi)/2.0
    return g_n_dim * x_opt   # mu in k_B T_c^0


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
    spec = json.loads(open('/tests/grading_spec.json').read())
    balances = spec.get('hidden_balances', {})
    return {'mu_gold': balances.get('mu_gold', {}),
            'C12_gold': balances.get('C12_gold', {})}


# === block: score_0 (check id='validate_ideal_gas') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    tol = step.get('tolerance_abs', 0.05)
    passed = 0
    for row in artifact:
        try:
            N = int(row['N'])
            mu_pimc = float(row['mu_PIMC'])
        except:
            continue
        mu_exact_recomputed = ideal_gas_exact_mu(N, T_over_Tc0=1.5)
        if abs(mu_pimc - mu_exact_recomputed) <= tol:
            passed += 1
    return passed / len(artifact)


# === block: score_1 (check id='validate_interacting_gas') ===
def score_1(artifact, step, ctx):
    artifact = load_artifact(os.path.join(outputs_dir, 'validation_interacting_gas.csv'))
    if not artifact:
        return 0.0
    tol = step.get('tolerance_abs', 0.1)
    passed = 0
    for row in artifact:
        try:
            TovTc = float(row['T_over_Tc0'])
            mu_pimc = float(row['mu_PIMC'])
        except:
            continue
        mu_hf = hf_chemical_potential(TovTc, na3=1e-6)
        if abs(mu_pimc - mu_hf) <= tol:
            passed += 1
    if not artifact:
        return 0.0
    return passed / len(artifact)


# === block: score_2 (check id='mixture_polarization_scan') ===
def score_2(artifact, step, ctx):
    artifact = load_artifact(os.path.join(outputs_dir, 'chemical_potentials.csv'))
    if not artifact:
        return 0.0
    # structural check: mu1 > mu2 for p > 0
    struct_ok = True
    for row in artifact:
        try:
            p = float(row['polarization'])
            mu1 = float(row['mu1'])
            mu2 = float(row['mu2'])
            if p > 0 and mu1 <= mu2:
                struct_ok = False
                break
        except:
            continue
    struct_score = 1.0 if struct_ok else 0.0

    # slope check from free energy vs p^2
    # find p and free_energy_per_particle
    p_list = []
    f_list = []
    for row in artifact:
        try:
            p_list.append(float(row['polarization']))
            f_list.append(float(row['free_energy_per_particle']))
        except:
            pass
    if len(p_list) < 2:
        return 0.0
    # find baseline p=0
    baseline = None
    for i, p in enumerate(p_list):
        if abs(p) < 1e-9:
            baseline = f_list[i]
            break
    if baseline is None:
        return 0.0
    # compute Delta f = f(p) - f(0) and p^2
    p2_vals = []
    df_vals = []
    for i, p in enumerate(p_list):
        if p > 0:
            p2_vals.append(p*p)
            df_vals.append(f_list[i] - baseline)
    if len(p2_vals) == 0:
        slope_score = 0.0
    else:
        # linear fit without intercept: slope = sum(df*p2) / sum(p2^2)
        num = sum(df*p2 for df,p2 in zip(df_vals, p2_vals))
        den = sum(p2*p2 for p2 in p2_vals)
        if den == 0:
            slope_score = 0.0
        else:
            slope_fit = num / den
            # expected slope = (g - g12)*n / 4, with g_n_dim for na^3=1e-4
            na3 = 1e-4
            zeta32 = 2.612
            C_const = (2*zeta32)**(2.0/3.0)
            g_n_dim = 2.0 * (na3)**(1.0/3.0) * C_const
            m_expected = (g_n_dim * 0.07) / 4.0   # (g-g12)n/4 = 0.07*g_n_dim/4
            rel_err = abs(slope_fit - m_expected) / m_expected if m_expected else 0.0
            tol_rel = step.get('slope_tolerance_rel', 0.20)
            slope_score = 1.0 if rel_err <= tol_rel else 0.0
    # combined weight
    w_struct = 0.3
    w_slope = 0.7
    return w_struct * struct_score + w_slope * slope_score


# === block: score_3 (check id='balanced_mixture_temperatures') ===
def score_3(artifact, step, ctx):
    artifact = load_artifact(os.path.join(outputs_dir, 'balanced_mixture.csv'))
    if not artifact:
        return 0.0
    mu_gold_map = ctx.get('mu_gold', {})
    C12_gold_map = ctx.get('C12_gold', {})
    tol_mu = step.get('tolerance_mu_abs', 0.05)
    tol_C12_rel = step.get('tolerance_C12_rel', 0.20)
    rows_ok = 0
    total = 0
    for row in artifact:
        try:
            T_key = f"{float(row['T_over_Tc0']):.1f}"
            mu_reported = float(row['chemical_potential'])
            C12_reported = float(row['interspecies_contact_C12'])
        except:
            continue
        if T_key not in mu_gold_map or T_key not in C12_gold_map:
            continue
        total += 1
        mu_gold = mu_gold_map[T_key]
        C12_gold = C12_gold_map[T_key]
        mu_pass = abs(mu_reported - mu_gold) <= tol_mu
        C12_pass = abs(C12_reported - C12_gold) <= tol_C12_rel * abs(C12_gold) if C12_gold !=0 else abs(C12_reported - C12_gold) <= 0.02
        if mu_pass and C12_pass:
            rows_ok += 1
    if total == 0:
        return 0.0
    return rows_ok / total


_SCORERS = {
    'validate_ideal_gas': score_0,
    'validate_interacting_gas': score_1,
    'mixture_polarization_scan': score_2,
    'balanced_mixture_temperatures': score_3,
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
