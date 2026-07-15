import os
import json
import csv

# === author imports / helpers ===
import math


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
    compound_params = spec.get('compound_params', {})
    if not compound_params:
        return {'expected': {}}
    expected = {}
    for comp, par in compound_params.items():
        C11 = par['C11']
        C12 = par['C12']
        C44 = par['C44']
        b_ang = par['b']
        d_ang = par['d']
        rho_gcm3 = par['rho_gcm3']
        M_gmol = par['M']
        n_atoms = par['n']

        # units conversions
        C11_pa = C11 * 1e9
        C12_pa = C12 * 1e9
        C44_pa = C44 * 1e9
        rho_kgm3 = rho_gcm3 * 1000.0

        # fundamental constants
        h = 6.62607015e-34
        k = 1.380649e-23
        NA = 6.02214076e23

        # VRH bulk modulus
        B = (C11 + 2 * C12) / 3.0
        # Voigt shear modulus
        Gv = (C11 - C12 + 3 * C44) / 5.0
        # Reuss shear modulus
        Gr = (5 * C44 * (C11 - C12)) / (4 * C44 + 3 * (C11 - C12))
        # Hill average
        G = (Gv + Gr) / 2.0
        E = (9 * B * G) / (3 * B + G)
        nu = (3 * B - 2 * G) / (2 * (3 * B + G))
        B_over_G = B / G
        A = (2 * C44) / (C11 - C12)
        Cauchy = C12 - C44

        # Peierls stress
        b_m = b_ang * 1e-10
        d_m = d_ang * 1e-10
        G_pa = G * 1e9
        sigma_P_pa = (G_pa / (1 - nu)) * math.exp(-(2 * math.pi * d_m) / (b_m * (1 - nu)))
        sigma_P_GPa = sigma_P_pa / 1e9

        # sound velocities
        vt = math.sqrt(G_pa / rho_kgm3)
        B_pa = B * 1e9
        vl = math.sqrt((B_pa + (4.0/3.0) * G_pa) / rho_kgm3)
        vm = ( (1.0/3.0) * (2.0/(vt**3) + 1.0/(vl**3)) ) ** (-1.0/3.0)

        # Debye temperature
        M_kgmol = M_gmol / 1000.0
        atom_density = NA * rho_kgm3 / M_kgmol
        factor = (3 * n_atoms) / (4 * math.pi)
        inside = factor * atom_density
        thetaD = (h / k) * (inside ** (1.0/3.0)) * vm

        expected[comp] = {
            'B': B,
            'G': G,
            'E': E,
            'nu': nu,
            'B_over_G': B_over_G,
            'A': A,
            'Cauchy_pressure': Cauchy,
            'sigma_P': sigma_P_GPa,
            'rho': rho_gcm3,
            'v_t': vt,
            'v_l': vl,
            'v_m': vm,
            'theta_D': thetaD
        }
    return {'expected': expected}


# === block: score_0 (check id='step_elastic_properties') ===
def score_0(artifact, step, ctx):
    # paper gold values for derived properties
    paper_gold = {
        'CuRh2S4': {
            'B': 106.20, 'G': 25.05, 'E': 69.67, 'nu': 0.39, 'B_over_G': 4.23,
            'A': 1.74, 'Cauchy_pressure': 64.44, 'sigma_P': 0.47, 'rho': 4.91,
            'v_t': 5332.14, 'v_l': 2258.72, 'v_m': 2553.63, 'theta_D': 294.23
        },
        'CuRh2Se4': {
            'B': 94.60, 'G': 19.53, 'E': 54.81, 'nu': 0.40, 'B_over_G': 4.84,
            'A': 0.99, 'Cauchy_pressure': 62.04, 'sigma_P': 0.35, 'rho': 6.55,
            'v_t': 4291.65, 'v_l': 1726.75, 'v_m': 1955.63, 'theta_D': 215.57
        }
    }

    rtol_moduli = 0.05
    rtol_velocity = 0.10
    fields_moduli = ['B','G','E','nu','B_over_G','A','Cauchy_pressure','sigma_P']
    fields_velocity = ['v_t','v_l','v_m','theta_D']
    all_fields = fields_moduli + fields_velocity + ['rho']
    compounds = ['CuRh2S4','CuRh2Se4']
    eps = 1e-6

    total_checks = 0
    passed = 0

    for comp in compounds:
        if comp not in artifact:
            continue
        comp_data = artifact[comp]
        has_cij = all(k in comp_data for k in ['C11','C12','C44'])
        if has_cij:
            C11 = comp_data['C11']
            C12 = comp_data['C12']
            C44 = comp_data['C44']
            B_recomp = (C11 + 2*C12) / 3.0
            Gv = (C11 - C12 + 3*C44) / 5.0
            Gr = (5*C44*(C11-C12)) / (4*C44 + 3*(C11-C12))
            G_recomp = (Gv + Gr) / 2.0
            E_recomp = (9*B_recomp*G_recomp) / (3*B_recomp + G_recomp)
            nu_recomp = (3*B_recomp - 2*G_recomp) / (2*(3*B_recomp + G_recomp))
            A_recomp = (2*C44) / (C11 - C12)
            Cauchy_recomp = C12 - C44
            B_over_G_recomp = B_recomp / G_recomp
            recomputed = {
                'B': B_recomp, 'G': G_recomp, 'E': E_recomp,
                'nu': nu_recomp, 'B_over_G': B_over_G_recomp,
                'A': A_recomp, 'Cauchy_pressure': Cauchy_recomp
            }
            for field in recomputed:
                if field not in comp_data:
                    continue
                total_checks += 1
                if abs(comp_data[field] - recomputed[field]) <= eps:
                    passed += 1

        gold = paper_gold.get(comp, {})
        for field in all_fields:
            if field not in comp_data or field not in gold:
                continue
            tol = rtol_moduli if field != 'rho' and field in fields_moduli else rtol_velocity
            total_checks += 1
            if abs(float(comp_data[field]) - gold[field]) <= tol * abs(gold[field]) + 1e-12:
                passed += 1

        if 'B_over_G' in comp_data:
            total_checks += 1
            if comp_data['B_over_G'] > 1.75 + eps:
                passed += 1
        if 'nu' in comp_data:
            total_checks += 1
            if comp_data['nu'] > 0.33 + eps:
                passed += 1

    if total_checks == 0:
        return 0.0
    return passed / float(total_checks)


_SCORERS = {
    'step_elastic_properties': score_0,
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
