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
    L = 0.25
    ha = 0.001
    k = 5.0/6.0
    mu_vals = {
        'S-S': math.pi,
        'C-C': 2*math.pi,
        'C-S': 4.49341,
        'C-R': math.pi,
        'S-R': math.pi/2
    }

    # Aluminium
    E_al = 72.4e9
    nu_al = 0.3
    G_al = E_al/(2*(1+nu_al))
    Q11_al = E_al/(1-nu_al**2)
    alpha_al = 22.5e-6

    # PZT-5A
    E_a = 63e9
    nu_a = 0.3
    G_a = 24.2e9
    Q11_a = E_a/(1-nu_a**2)
    alpha_a = 0.9e-6
    d31 = 2.54e-10

    # Glass-epoxy
    E11 = 50e9
    E22 = 15.2e9
    nu12 = 0.254
    nu21 = (E22/E11)*nu12
    denom = 1 - nu12*nu21
    Q11_0 = E11/denom
    Q22 = E22/denom
    G13 = 4.7e9
    G23 = 3.28e9
    alpha1 = 6e-6
    alpha2 = 23.3e-6

    ctx = {
        'L': L,
        'ha': ha,
        'k': k,
        'mu_vals': mu_vals,
        'al': {'Q11': Q11_al, 'G': G_al, 'alpha': alpha_al},
        'pzt': {'Q11': Q11_a, 'G': G_a, 'alpha': alpha_a, 'd31': d31},
        'glass0': {'Q11': Q11_0, 'Q55': G13, 'alpha': alpha1},
        'glass90': {'Q11': Q22, 'Q55': G23, 'alpha': alpha2}
    }
    return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    tol = float(step.get('tolerance_abs', 0.2))
    L = ctx['L']
    ha = ctx['ha']
    k_shear = ctx['k']
    mu_vals = ctx['mu_vals']

    # core thicknesses from the paper (beam h, without actuator layers)
    CORE_THICKNESSES = {
        'aluminium': 0.01,
        'three-layer-cross-ply': 0.0045,
        'four-layer-antisymmetric-1piezo': 0.004,
        'four-layer-antisymmetric-2piezo': 0.004,
    }

    def get_core_thickness(beam_type, h_base):
        """Return the structural core thickness (m) for the given beam_type.
        For the thickness-study beam, use the submitted thickness_m as the core."""
        if 'thickness-study' in beam_type:
            return h_base
        return CORE_THICKNESSES.get(beam_type, h_base)

    def get_materials(beam_type, core_h):
        if beam_type == 'aluminium':
            seq = [
                ('pzt', ha),
                ('al', core_h),
                ('pzt', ha)
            ]
        elif 'three-layer-cross-ply' in beam_type:
            t_layer = core_h / 3.0
            seq = [
                ('pzt', ha),
                ('glass0', t_layer),
                ('glass90', t_layer),
                ('glass0', t_layer),
                ('pzt', ha)
            ]
        elif beam_type == 'four-layer-antisymmetric-1piezo':
            t_layer = core_h / 4.0
            seq = [
                ('glass0', t_layer),
                ('glass90', t_layer),
                ('glass0', t_layer),
                ('glass90', t_layer),
                ('pzt', ha)
            ]
        elif beam_type == 'four-layer-antisymmetric-2piezo':
            t_layer = core_h / 4.0
            seq = [
                ('pzt', ha),
                ('glass0', t_layer),
                ('glass90', t_layer),
                ('glass0', t_layer),
                ('glass90', t_layer),
                ('pzt', ha)
            ]
        else:
            raise ValueError('Unknown beam_type')
        return seq

    def compute_expected(beam_type, bc, V, core_h):
        mat = get_materials(beam_type, core_h)
        total_h = sum(t for _, t in mat)
        z_bot = -total_h/2.0
        A11 = B11 = D11 = A55 = 0.0
        sum_QA = 0.0
        sum_piezo = 0.0
        for mat_id, t in mat:
            prop = ctx[mat_id]
            z_top = z_bot + t
            z_mid = z_bot + t/2.0
            q11 = prop['Q11']
            q55 = prop.get('Q55', prop['G'])
            A11 += q11 * t
            B11 += q11 * z_mid * t
            D11 += q11 * (z_top**3 - z_bot**3) / 3.0
            A55 += k_shear * q55 * t
            sum_QA += q11 * prop['alpha'] * t
            if mat_id == 'pzt':
                sum_piezo += q11 * prop['d31']
            z_bot = z_top
        mu_min = mu_vals[bc]
        mu = mu_min / L
        rhs_num = mu**2 * (D11 - B11**2/A11)
        rhs_den = 1.0 + (mu**2 / A55) * (D11 - B11**2/A11)
        rhs = rhs_num / rhs_den
        N_E = V * sum_piezo
        if abs(sum_QA) < 1e-15:
            return None
        delta_T_cr = (rhs - N_E) / sum_QA
        return delta_T_cr

    def safe_float(s):
        try:
            return float(s)
        except (TypeError, ValueError):
            return None

    correct = 0
    total = 0
    for row in artifact:
        total += 1
        bc = row.get('boundary_condition', '').strip()
        V = safe_float(row.get('voltage_V', 0))
        h_base = safe_float(row.get('thickness_m', 0))
        beam_type = str(row.get('beam_type', '')).strip()
        reported = safe_float(row.get('delta_T_cr_C', None))
        if None in (V, h_base, reported) or not beam_type:
            continue
        try:
            core_h = get_core_thickness(beam_type, h_base)
            expected = compute_expected(beam_type, bc, V, core_h)
            if expected is None:
                continue
            if abs(reported - expected) <= tol:
                correct += 1
        except Exception:
            pass
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'step_02': score_0,
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
