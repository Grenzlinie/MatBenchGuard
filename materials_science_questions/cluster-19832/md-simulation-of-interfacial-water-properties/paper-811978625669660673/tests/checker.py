import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import jv


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


# === block: score_0 (check id='check_pe_energies') ===
def score_0(artifact, step, ctx):
    eps_s = 78.3
    eps_star = 6.0
    eps1 = 4.0
    L = 5.0
    tol = 0.05
    n = len(artifact)
    if n == 0:
        return 0.0
    passed = 0
    for row in artifact:
        R = float(row['R'])
        Z = float(row['Z'])
        Z0 = float(row['Z0'])
        r12 = math.sqrt(R**2 + (Z - Z0)**2)
        def integrand(x):
            if x == 0:
                # x=0 analytic limit handled by quad
                return 0.0
            xL = x * L
            inv_term = 1.0 / math.sqrt(1.0 + 1.0/(xL**2))
            num1 = (1.0 - eps_star/eps_s) * inv_term
            a1 = num1 * math.exp(-Z0 * math.sqrt(x**2 + 1.0/L**2)) + math.exp(-x * Z0) * (eps_star/eps_s)
            a2 = num1 * math.exp(-Z * math.sqrt(x**2 + 1.0/L**2)) + math.exp(-x * Z) * (eps_star/eps_s)
            Delta = num1 + eps_star/eps_s + eps_star/eps1
            return jv(0, x * R) * a1 * a2 / Delta
        Phi, _ = quad(integrand, 0, np.inf, limit=200, epsabs=1e-10, epsrel=1e-10)
        term1 = (1.0 - eps_star/eps_s) * math.exp(-r12 / L) + eps_star/eps_s
        Rpp = math.sqrt(R**2 + (Z + Z0)**2)
        term2 = r12 / Rpp * ((1.0 - eps_star/eps_s) * math.exp(-Rpp / L) + eps_star/eps_s)
        inv_eps_eff = (term1 + term2 - 2.0 * Phi * r12) / eps_star
        eps_eff_recomp = 1.0 / inv_eps_eff
        U_recomp = 1.0 / (eps_eff_recomp * r12)
        agent_U = float(row['U12_NL'])
        agent_eps = float(row['epsilon_eff_NL'])
        err_U = abs(agent_U - U_recomp) / (abs(U_recomp) + 1e-12)
        err_eps = abs(agent_eps - eps_eff_recomp) / (abs(eps_eff_recomp) + 1e-12)
        if err_U <= tol and err_eps <= tol:
            passed += 1
    return passed / n if n else 0.0


# === block: score_1 (check id='check_cpe_energies') ===
def score_1(artifact, step, ctx):
    eps_s = 78.3
    eps_star = 6.0
    eps1 = 4.0
    L = 5.0
    tol = 0.05
    n = len(artifact)
    if n == 0:
        return 0.0
    passed = 0
    for row in artifact:
        R = float(row['R'])
        Z = float(row['Z'])
        Z0 = float(row['Z0'])
        absZ = abs(Z)
        r13 = math.sqrt(R**2 + (Z0 + absZ)**2)
        def integrand(x):
            if x == 0:
                return 0.0
            xL = x * L
            inv_term = 1.0 / math.sqrt(1.0 + 1.0/(xL**2))
            Delta1 = 1.0 + eps_s/eps1 + (eps_s/eps_star - 1.0) * inv_term
            Delta2 = 1.0 + (eps_star/eps1) * ((eps_s + eps1)/(eps_s - eps_star)) * math.sqrt(1.0 + xL**2)
            term = (1.0/Delta1) * math.exp(-x * Z0) + (1.0/Delta2) * math.exp(-(Z0/L) * math.sqrt(1.0 + xL**2))
            return jv(0, x*R) * math.exp(-x * absZ) * term
        Psi, _ = quad(integrand, 0, np.inf, limit=200, epsabs=1e-10, epsrel=1e-10)
        U_recomp = 2.0 * Psi / eps1
        # avoid division by zero if Psi extremely small
        if Psi < 1e-15:
            eps_eff_recomp = float('inf')
        else:
            eps_eff_recomp = eps1 / (2.0 * r13 * Psi)
        agent_U = float(row['U13_NL_cross'])
        agent_eps = float(row['epsilon_eff_NL_cross'])
        err_U = abs(agent_U - U_recomp) / (abs(U_recomp) + 1e-12)
        err_eps = abs(agent_eps - eps_eff_recomp) / (abs(eps_eff_recomp) + 1e-12) if eps_eff_recomp != float('inf') else (0.0 if agent_eps == float('inf') else 1.0)
        if err_U <= tol and err_eps <= tol:
            passed += 1
    return passed / n if n else 0.0


# === block: score_2 (check id='check_slab_energies') ===
def score_2(artifact, step, ctx):
    eps1 = 4.0
    d = 6.0
    Z = 11.0
    tol_abs = 0.5
    tol_rel = 0.05
    n = len(artifact)
    if n == 0:
        return 0.0
    passed = 0
    for row in artifact:
        eps_slab = float(row['epsilon_slab'])
        def integrand(x):
            alpha = (eps_slab - eps1) / (eps_slab + eps1)
            D = 1.0 - alpha**2 * math.exp(-2 * x * d)
            return math.exp(-x * Z) / D
        I, _ = quad(integrand, 0, np.inf, limit=200, epsabs=1e-10, epsrel=1e-10)
        U_recomp = 560.0 * 4.0 * eps_slab / ((eps1 + eps_slab)**2) * I
        agent_U = float(row['U_slab_12'])
        err_rel = abs(agent_U - U_recomp) / (abs(U_recomp) + 1e-12)
        err_abs = abs(agent_U - U_recomp)
        if err_abs <= tol_abs or err_rel <= tol_rel:
            passed += 1
    return passed / n if n else 0.0


_SCORERS = {
    'check_pe_energies': score_0,
    'check_cpe_energies': score_1,
    'check_slab_energies': score_2,
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
