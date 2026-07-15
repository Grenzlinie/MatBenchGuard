import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math, sys


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


# === block: score_0 (check id='exchange_parameters') ===
def score_0(artifact, step, ctx):
    import json, csv, os

    kB_eV_K = 8.617333262145e-5   # eV/K conversion factor
    # Compute J in eV first, then convert to K: J_K = J_eV / kB_eV_K
    def gauss_solve_4(A, b):
        """Solve 4x4 linear system A x = b via Gaussian elimination with partial pivoting."""
        n = 4
        a = [row[:] for row in A]
        b = b[:]
        for i in range(n):
            # find pivot
            max_row = i
            max_val = abs(a[i][i])
            for j in range(i+1, n):
                if abs(a[j][i]) > max_val:
                    max_val = abs(a[j][i])
                    max_row = j
            if max_val < 1e-15:
                raise ValueError("Singular matrix")
            # swap rows
            if max_row != i:
                a[i], a[max_row] = a[max_row], a[i]
                b[i], b[max_row] = b[max_row], b[i]
            # eliminate
            for j in range(i+1, n):
                factor = a[j][i] / a[i][i]
                for k in range(i, n):
                    a[j][k] -= factor * a[i][k]
                b[j] -= factor * b[i]
        # back substitution
        x = [0.0]*4
        for i in range(n-1, -1, -1):
            s = sum(a[i][j]*x[j] for j in range(i+1, n))
            x[i] = (b[i] - s) / a[i][i]
        return x

    def compute_J_from_energies(energies_eV):
        """Given dict of total energies (eV) for FM, AF1, AF2, AF3, AF4, return [J1,J2,J3,J4] in Kelvin."""
        E_FM = energies_eV['FM']
        E_AF1 = energies_eV['AF1']
        E_AF2 = energies_eV['AF2']
        E_AF3 = energies_eV['AF3']
        E_AF4 = energies_eV['AF4']
        dE1 = E_AF1 - E_FM
        dE2 = E_AF2 - E_FM
        dE3 = E_AF3 - E_FM
        dE4 = E_AF4 - E_FM
        # Coefficient matrix (see paper Eqs. 3)
        A = [
            [0, 0, 2, 2],
            [0, 4, 0, 2],
            [2, 2, 1, 0],
            [0, 4, 2, 0]
        ]
        b = [dE1, dE2, dE3, dE4]
        J_vec_eV = gauss_solve_4(A, b)
        J_vec_K = [j / kB_eV_K for j in J_vec_eV]
        return J_vec_K

    gold = step['gold_values']
    tol_Cs = step['tolerance_Cs_K']
    tol_others = step['tolerance_others_K']
    trend_tol = step['trend_tolerance_J2J4_K']

    # Load energies.json
    energies_path = os.path.join('/app/outputs', 'energies.json')
    if not os.path.exists(energies_path):
        return 0.0
    with open(energies_path) as f:
        all_energies = json.load(f)

    compounds = ['Cs2CuCl4', 'Rb2CuCl4', 'K2CuCl4', 'Na2CuCl4']
    # Score components
    val_scores = []
    for comp in compounds:
        if comp not in all_energies:
            # missing compound -> zero for that group
            val_scores.extend([0.0]*4)
            continue
        try:
            J_K = compute_J_from_energies(all_energies[comp])
        except Exception:
            J_K = [0.0]*4
        gold_comp = gold[comp]
        J_names = ['J1','J2','J3','J4']
        tolerance = tol_Cs if comp=='Cs2CuCl4' else tol_others
        for i, name in enumerate(J_names):
            diff = abs(J_K[i] - gold_comp[name])
            if diff <= tolerance:
                val_scores.append(1.0)
            else:
                # partial credit: linear decay from tolerance to 2*tolerance
                if diff <= 2*tolerance:
                    val_scores.append(1.0 - (diff - tolerance)/tolerance)
                else:
                    val_scores.append(0.0)

    val_score = sum(val_scores) / len(val_scores) if val_scores else 0.0

    # Trend check: extract J1,J2,J3,J4 arrays
    J1 = []
    J2 = []
    J3 = []
    J4 = []
    for comp in compounds:
        if comp not in all_energies:
            trend_score = 0.0
            break
        try:
            J_K = compute_J_from_energies(all_energies[comp])
            J1.append(J_K[0])
            J2.append(J_K[1])
            J3.append(J_K[2])
            J4.append(J_K[3])
        except:
            trend_score = 0.0
            break
    else:
        # monotonic: J1 and J3 must become more negative (decreasing)
        ok = True
        for i in range(len(compounds)-1):
            if J1[i] >= J1[i+1] - 0.1:   # need strictly more negative
                ok = False
            if J3[i] >= J3[i+1] - 0.1:
                ok = False
        # J2, J4 constant: range <= trend_tol
        if max(J2) - min(J2) > trend_tol:
            ok = False
        if max(J4) - min(J4) > trend_tol:
            ok = False
        trend_score = 1.0 if ok else 0.0

    # Combine: 0.7 * val_score + 0.3 * trend_score
    final = 0.7 * val_score + 0.3 * trend_score
    return round(final, 6)


# === block: score_1 (check id='dos_ratio') ===
def score_1(artifact, step, ctx):
    import json, os

    pdos_path = os.path.join('/app/outputs', 'pdos_cs.json')
    if not os.path.exists(pdos_path):
        return 0.0
    with open(pdos_path) as f:
        data = json.load(f)
    energy = data['energy']
    cs6p = data['Cs_6p_DOS']
    cs6s = data['Cs_6s_DOS']

    def integrate(x, y, xmin, xmax):
        total = 0.0
        for i in range(len(x)-1):
            if x[i] >= xmin and x[i+1] <= xmax:
                dx = x[i+1] - x[i]
                total += 0.5 * (y[i] + y[i+1]) * dx
        return total

    p_area = integrate(energy, cs6p, -5.0, 0.0)
    s_area = integrate(energy, cs6s, -5.0, 0.0)
    if s_area == 0.0:
        return 0.0
    ratio = p_area / s_area
    lo = step['target_ratio_min']
    hi = step['target_ratio_max']
    return 1.0 if lo <= ratio <= hi else 0.0


_SCORERS = {
    'exchange_parameters': score_0,
    'dos_ratio': score_1,
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
