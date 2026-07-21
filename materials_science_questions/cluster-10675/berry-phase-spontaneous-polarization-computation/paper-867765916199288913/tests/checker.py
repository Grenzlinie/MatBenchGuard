import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import minimize
from math import isclose


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
    eV_J = 1.602176634e-19
    a_inplane = 3.846e-10
    A_cell = a_inplane**2
    epsilon0 = 8.8541878128e-12
    c_p0 = 4.009e-10
    c_s0 = 3.846e-10

    B_p = -0.17175279
    C_p =  0.16068441
    B_s =  0.21046331
    C_s =  0.30913420
    alpha_p = 1.01566146
    beta_p  = 0.03609915
    gamma_p = 0.02209009
    alpha_s = 1.0
    beta_s  = 0.06076952
    gamma_s = 0.04820368

    def U_p(P): return B_p * P**2 + C_p * P**4
    def U_s(P): return B_s * P**2 + C_s * P**4

    def E_elec(P_p, P_s, l_p, l_s):
        return (l_p * l_s / (epsilon0 * (l_p + l_s))) * (P_s - P_p)**2

    def total_energy(P_vec, n_p, n_s):
        P_p, P_s = P_vec
        l_p = n_p * c_p0
        l_s = n_s * c_s0
        E_bulk = (n_p * U_p(P_p) + n_s * U_s(P_s)) * eV_J / A_cell
        E_el = E_elec(P_p, P_s, l_p, l_s)
        return E_bulk + E_el

    def c_over_a(P, alpha, beta, gamma):
        return alpha + beta * P**2 + gamma * P**4

    n_s = 3
    ref = {}
    for n_p in range(1, 8):
        x0 = np.array([0.7, 0.0])
        res = minimize(lambda x: total_energy(x, n_p, n_s),
                       x0, method='L-BFGS-B', bounds=[(0.0, 5.0), (0.0, 5.0)])
        P_p_opt, P_s_opt = res.x
        tetra_p = c_over_a(P_p_opt, alpha_p, beta_p, gamma_p)
        tetra_s = c_over_a(P_s_opt, alpha_s, beta_s, gamma_s)
        ref[n_p] = {"P_p0": float(P_p_opt), "P_s0": float(P_s_opt),
                    "tetra_Pb": float(tetra_p), "tetra_Sr": float(tetra_s)}
    return {"ref": ref}


# === block: score_0 (check id='step_eq_model') ===
def score_0(artifact, step, ctx):
    ref_dict = ctx["ref"]
    tolerance_pol = step.get("tolerance_polarization", 0.02)
    tolerance_tet = step.get("tolerance_tetragonality", 0.002)
    max_dev_pol = step.get("max_deviation_pol", 0.1)
    max_dev_tet = step.get("max_deviation_tet", 0.01)

    expected_nps = set(range(1, 8))
    rows_by_np = {}
    for row in artifact:
        try:
            n = int(row["n_p"])
            rows_by_np[n] = row
        except:
            continue

    def field_score(val, ref, tol, max_dev):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        eff_max = max(max_dev, tol)
        return max(0.0, 1.0 - (diff - tol) / (eff_max - tol))

    total_score = 0.0
    count = 0
    for np_val in expected_nps:
        if np_val not in ref_dict:
            continue
        ref_vals = ref_dict[np_val]
        row = rows_by_np.get(np_val, {})
        # P_p0
        try:
            val = float(row.get("P_p0"))
            total_score += field_score(val, ref_vals["P_p0"], tolerance_pol, max_dev_pol)
        except:
            total_score += 0.0
        count += 1
        # P_s0
        try:
            val = float(row.get("P_s0"))
            total_score += field_score(val, ref_vals["P_s0"], tolerance_pol, max_dev_pol)
        except:
            total_score += 0.0
        count += 1
        # tetragonality_Pb
        try:
            val = float(row.get("tetragonality_Pb"))
            total_score += field_score(val, ref_vals["tetra_Pb"], tolerance_tet, max_dev_tet)
        except:
            total_score += 0.0
        count += 1
        # tetragonality_Sr
        try:
            val = float(row.get("tetragonality_Sr"))
            total_score += field_score(val, ref_vals["tetra_Sr"], tolerance_tet, max_dev_tet)
        except:
            total_score += 0.0
        count += 1

    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'step_eq_model': score_0,
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
