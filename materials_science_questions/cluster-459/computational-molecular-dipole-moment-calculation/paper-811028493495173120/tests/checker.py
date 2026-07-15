import os
import json
import csv

# === author imports / helpers ===
import math
import json

def fit_min_z(z, E):
    """Refine minimum position using quadratic fit on three points around the minimum."""
    i_min = min(range(len(E)), key=E.__getitem__)
    if i_min == 0 or i_min == len(E) - 1:
        return z[i_min]
    z0, z1, z2 = z[i_min-1], z[i_min], z[i_min+1]
    e0, e1, e2 = E[i_min-1], E[i_min], E[i_min+1]
    d10 = (e1 - e0) / (z1 - z0)
    d21 = (e2 - e1) / (z2 - z1)
    a = (d21 - d10) / (z2 - z0)
    b = d10 - a * (z0 + z1)
    if abs(a) < 1e-12:
        return z1
    return -b / (2 * a)


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


# === block: score_0 (check id='structural_params') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol_re = step["tol_re_A"]
    tol_nu = step["tol_nu_cm1"]
    tol_be = step["tol_BE_kJmol"]
    halogens = ["Cl", "Br", "I"]
    states = ["2A1", "2A2"]
    halogen_mass = {"Cl": 35.453, "Br": 79.904, "I": 126.904}
    c_cm_s = 2.99792458e10
    N_A = 6.02214076e23
    total_pass = 0
    total_cnt = 0
    for hal in halogens:
        for state in states:
            if hal not in artifact or state not in artifact[hal]:
                total_cnt += 3
                continue
            entry = artifact[hal][state]
            z = entry["z"]
            E = entry["E"]
            if len(z) < 3 or len(E) < 3:
                total_cnt += 3
                continue
            # Unit detection
            min_val = min(E)
            unit_factor = 1.0  # assume kJ/mol
            if abs(min_val) < 1.0:
                unit_factor = 2625.4996394749  # Hartree -> kJ/mol
            re_hat = fit_min_z(z, E)
            # Asymptotic energy
            idx_asy = [i for i in range(len(z)) if z[i] > re_hat + 1.5]
            if len(idx_asy) < 2:
                idx_asy = list(range(max(0, len(z)-3), len(z)))
            E_iso = sum(E[i] for i in idx_asy) / len(idx_asy) * unit_factor
            min_E_kj = min(E) * unit_factor
            BE_hat = E_iso - min_E_kj
            # Curvature for frequency
            i_min = min(range(len(E)), key=E.__getitem__)
            if i_min == 0 or i_min == len(E) - 1:
                total_cnt += 3
                continue
            dz1 = z[i_min] - z[i_min-1]
            dz2 = z[i_min+1] - z[i_min]
            if dz1 == 0 or dz2 == 0:
                total_cnt += 3
                continue
            d2E = 2 * (E[i_min+1]/(dz2*(dz1+dz2)) + E[i_min-1]/(dz1*(dz1+dz2)) - E[i_min]/(dz1*dz2))
            d2E_kj = d2E * unit_factor
            nu_hat = 0.0
            if d2E_kj > 0:
                mu_kg = halogen_mass[hal] * 1.66053906660e-27
                k_Npm = d2E_kj * (1000 / N_A) * 1e20
                if k_Npm > 0:
                    omega = math.sqrt(k_Npm / mu_kg)
                    nu_hat = omega / (2 * math.pi * c_cm_s)
            gold_re = gold[hal][state]["re"]
            gold_nu = gold[hal][state]["nu"]
            gold_BE = gold[hal][state]["BE"]
            if abs(re_hat - gold_re) <= tol_re:
                total_pass += 1
            if abs(nu_hat - gold_nu) <= tol_nu:
                total_pass += 1
            if abs(BE_hat - gold_BE) <= tol_be:
                total_pass += 1
            total_cnt += 3
    score = total_pass / total_cnt if total_cnt else 0.0
    return score


# === block: score_1 (check id='dipole_coeffs') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tol_M0 = step["tol_M0"]
    tol_M1 = step["tol_M1"]
    tol_M2 = step["tol_M2"]
    halogens = ["Cl", "Br", "I"]
    states = ["2A1", "2A2"]
    total_pass = 0
    total_cnt = 0
    for hal in halogens:
        for state in states:
            if hal not in artifact or state not in artifact[hal]:
                total_cnt += 3
                continue
            entry = artifact[hal][state]
            z = entry["z"]
            mu = entry["mu"]
            E = entry["E"]
            if len(z) < 3 or len(mu) < 3:
                total_cnt += 3
                continue
            re_hat = fit_min_z(z, E)
            # Pick three points closest to re_hat
            i_nearest = min(range(len(z)), key=lambda i: abs(z[i]-re_hat))
            if i_nearest == 0 or i_nearest == len(z) - 1:
                total_cnt += 3
                continue
            x = [z[i] - re_hat for i in (i_nearest-1, i_nearest, i_nearest+1)]
            y = [mu[i] for i in (i_nearest-1, i_nearest, i_nearest+1)]
            x0, x1, x2 = x[0], x[1], x[2]
            y0, y1, y2 = y[0], y[1], y[2]
            dx10 = x1 - x0
            dx21 = x2 - x1
            dx20 = x2 - x0
            if dx10 == 0 or dx21 == 0 or dx20 == 0:
                total_cnt += 3
                continue
            dy10 = y1 - y0
            dy21 = y2 - y1
            a = (dy21/dx21 - dy10/dx10) / dx20
            b = dy10/dx10 - a * (x0 + x1)
            c = y0 - a*x0*x0 - b*x0
            M0_hat, M1_hat, M2_hat = c, b, a
            gold_M0 = gold[hal][state]["M0"]
            gold_M1 = gold[hal][state]["M1"]
            gold_M2 = gold[hal][state]["M2"]
            if abs(M0_hat - gold_M0) <= tol_M0:
                total_pass += 1
            if abs(M1_hat - gold_M1) <= tol_M1:
                total_pass += 1
            if abs(M2_hat - gold_M2) <= tol_M2:
                total_pass += 1
            total_cnt += 3
    score = total_pass / total_cnt if total_cnt else 0.0
    return score


# === block: score_2 (check id='field_shifts') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tol_shift = step["tol_shift_A"]
    halogens = ["Cl", "Br", "I"]
    states = ["2A1", "2A2"]
    total_pass = 0
    total_cnt = 0
    for hal in halogens:
        for state in states:
            if hal not in artifact or state not in artifact[hal]:
                total_cnt += 2
                continue
            entry = artifact[hal][state]
            z = entry["z"]
            E = entry["E"]
            if len(z) < 3 or len(E) < 3:
                total_cnt += 2
                continue
            re_hat = fit_min_z(z, E)
            field_re = entry.get("field_optimized_re")
            if not field_re:
                total_cnt += 2
                continue
            fplus_re = field_re.get("F_plus_0.01")
            fminus_re = field_re.get("F_minus_0.01")
            if fplus_re is None or fminus_re is None:
                total_cnt += 2
                continue
            shift_plus = fplus_re - re_hat
            shift_minus = fminus_re - re_hat
            gold_plus = gold[hal][state]["dFplus"]
            gold_minus = gold[hal][state]["dFminus"]
            if abs(shift_plus - gold_plus) <= tol_shift:
                total_pass += 1
            if abs(shift_minus - gold_minus) <= tol_shift:
                total_pass += 1
            total_cnt += 2
    score = total_pass / total_cnt if total_cnt else 0.0
    return score


# === block: score_3 (check id='structural_trends') ===
def score_3(artifact, step, ctx):
    halogens = ["Cl", "Br", "I"]
    states = ["2A1", "2A2"]
    mass_map = {"Cl":35.453,"Br":79.904,"I":126.904}
    N_A = 6.02214076e23
    c_cm_s = 2.99792458e10
    total_pass = 0
    total_checks = 0
    computed = {}
    for hal in halogens:
        computed[hal] = {}
        for state in states:
            if hal not in artifact or state not in artifact[hal]:
                continue
            entry = artifact[hal][state]
            z = entry["z"]
            E = entry["E"]
            if len(z) < 3:
                continue
            re_hat = fit_min_z(z, E)
            i_min = min(range(len(E)), key=E.__getitem__)
            if i_min == 0 or i_min == len(E)-1:
                continue
            dz1 = z[i_min] - z[i_min-1]
            dz2 = z[i_min+1] - z[i_min]
            if dz1 <= 0 or dz2 <= 0:
                continue
            d2E = 2*(E[i_min+1]/(dz2*(dz1+dz2)) + E[i_min-1]/(dz1*(dz1+dz2)) - E[i_min]/(dz1*dz2))
            min_val = min(E)
            unit_factor = 1.0 if abs(min_val) > 1.0 else 2625.4996394749
            d2E_kj = d2E * unit_factor
            nu_hat = 0.0
            if d2E_kj > 0:
                mu_kg = mass_map[hal] * 1.66053906660e-27
                k_Npm = d2E_kj * (1000/N_A) * 1e20
                if k_Npm > 0:
                    omega = math.sqrt(k_Npm / mu_kg)
                    nu_hat = omega / (2*math.pi*c_cm_s)
            field_re = entry.get("field_optimized_re", {})
            fplus = field_re.get("F_plus_0.01")
            fminus = field_re.get("F_minus_0.01")
            shift_plus = (fplus - re_hat) if fplus is not None else None
            shift_minus = (fminus - re_hat) if fminus is not None else None
            computed[hal][state] = {"re": re_hat, "nu": nu_hat, "shift_plus": shift_plus, "shift_minus": shift_minus}
    for hal in halogens:
        if "2A1" in computed[hal] and "2A2" in computed[hal]:
            a1 = computed[hal]["2A1"]
            a2 = computed[hal]["2A2"]
            if a1.get("re") is not None and a2.get("re") is not None:
                total_checks += 1
                if a2["re"] > a1["re"]:
                    total_pass += 1
            if a1.get("nu") is not None and a2.get("nu") is not None:
                total_checks += 1
                if a2["nu"] < a1["nu"]:
                    total_pass += 1
            for st in ["2A1","2A2"]:
                if st in computed[hal]:
                    s = computed[hal][st]
                    if s.get("shift_plus") is not None:
                        total_checks += 1
                        if s["shift_plus"] < 0:
                            total_pass += 1
                    if s.get("shift_minus") is not None:
                        total_checks += 1
                        if s["shift_minus"] > 0:
                            total_pass += 1
    score = total_pass / total_checks if total_checks else 0.0
    return score


_SCORERS = {
    'structural_params': score_0,
    'dipole_coeffs': score_1,
    'field_shifts': score_2,
    'structural_trends': score_3,
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
