import os
import json
import csv

# === author imports / helpers ===
import os, json, math


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
    outputs_dir = "/app/outputs"
    ctx = {}
    files_to_load = ["step_01_structure.json", "step_02_elastic_constants.json"]
    for fname in files_to_load:
        path = os.path.join(outputs_dir, fname)
        if os.path.exists(path):
            with open(path) as f:
                ctx[fname] = json.load(f)
        else:
            ctx[fname] = None
    return ctx


# === block: score_0 (check id='structure') ===
def score_0(artifact, step, ctx):
    gold = step["params"]["gold"]
    tols = step["params"]["tolerances"]
    score = 0.0
    n = len(gold)
    for field, gval in gold.items():
        if field not in artifact:
            continue
        tol = tols[field]
        aval = artifact[field]
        if tol["type"] == "relative":
            if gval == 0:
                within = abs(aval) < 0.01
            else:
                within = abs(aval - gval) / abs(gval) <= tol["value"]
        else:
            within = abs(aval - gval) <= tol["value"]
        if within:
            score += 1
    return score / n


# === block: score_1 (check id='formation_enthalpy') ===
def score_1(artifact, step, ctx):
    field = step["params"]["field"]
    gold = step["params"]["gold"]
    tol = step["params"]["tolerance"]
    if field not in artifact:
        return 0.0
    aval = artifact[field]
    if tol["type"] == "relative":
        if gold == 0:
            within = abs(aval) < 0.1
        else:
            within = abs(aval - gold) / abs(gold) <= tol["value"]
    else:
        within = abs(aval - gold) <= tol["value"]
    return 1.0 if within else 0.0


# === block: score_2 (check id='elastic_constants') ===
def score_2(artifact, step, ctx):
    gold = step["params"]["gold"]
    tol = step["params"]["tolerance"]
    score = 0.0
    n = len(gold)
    for field, gval in gold.items():
        if field not in artifact:
            continue
        aval = artifact[field]
        if gval == 0:
            within = abs(aval) < 0.01
        else:
            within = abs(aval - gval) / abs(gval) <= tol["value"]
        if within:
            score += 1
    return score / n


# === block: score_3 (check id='mechanical_stability') ===
def score_3(artifact, step, ctx):
    C11 = artifact.get("C11_GPa", None)
    C12 = artifact.get("C12_GPa", None)
    C13 = artifact.get("C13_GPa", None)
    C33 = artifact.get("C33_GPa", None)
    C44 = artifact.get("C44_GPa", None)
    if None in (C11, C12, C13, C33, C44):
        return 0.0
    criteria = [
        C11 > 0,
        C11 - abs(C12) > 0,
        (C11 + C12) * C33 - 2 * C13**2 > 0,
        C44 > 0
    ]
    passed = sum(criteria)
    return passed / len(criteria)


# === block: score_4 (check id='polycrystalline_moduli') ===
def score_4(artifact, step, ctx):
    gold = step["params"]["gold"]
    tols = step["params"]["tolerances"]
    score = 0.0
    n = len(gold)
    for field, gval in gold.items():
        if field not in artifact:
            continue
        tol = tols[field]
        aval = artifact[field]
        if tol["type"] == "relative":
            if gval == 0:
                within = abs(aval) < 0.01
            else:
                within = abs(aval - gval) / abs(gval) <= tol["value"]
        else:
            within = abs(aval - gval) <= tol["value"]
        if within:
            score += 1
    return score / n


# === block: score_5 (check id='debye_sound_velocities') ===
def score_5(artifact, step, ctx):
    structure = ctx.get("step_01_structure.json")
    cij = ctx.get("step_02_elastic_constants.json")
    if not structure or not cij:
        return 0.0
    M_FU = 2*55.845 + 95.95
    Z = 4
    NA = 6.02214076e23
    V_ang = structure["V_angstrom3"]
    V_cm3 = V_ang * 1e-24
    rho_gcm3 = (Z * M_FU) / (NA * V_cm3)
    rho = rho_gcm3 * 1000.0

    C11 = cij["C11_GPa"]
    C12 = cij["C12_GPa"]
    C13 = cij["C13_GPa"]
    C33 = cij["C33_GPa"]
    C44 = cij["C44_GPa"]
    C66 = cij["C66_GPa"]

    B_V = (2*(C11+C12) + 4*C13 + C33) / 9.0
    denom_BR = C11 + C12 + 2*C33 - 4*C13
    B_R = ((C11+C12)*C33 - 2*C13**2) / denom_BR if denom_BR != 0 else 0.0
    B = (B_V + B_R) / 2.0

    det = (C11 - C12) * (C33*(C11+C12) - 2*C13**2)
    if abs(det) < 1e-12:
        return 0.0
    S11 = (C11*C33 - C13**2) / det
    S12 = (C13**2 - C12*C33) / det
    S13 = C13*(C12 - C11) / det
    S33 = (C11**2 - C12**2) / det
    S44 = 1.0 / C44
    G_V = (C11 + C12 + 2*C33 - 4*C13 + 12*C44 + 12*C66) / 30.0
    sum_S = 14*S11 + 4*S33 - 8*S13 - 10*S12 + 6*S44
    G_R = 15.0 / sum_S if sum_S > 0 else 0.0
    G = (G_V + G_R) / 2.0

    v_s = math.sqrt(G * 1e9 / rho)
    v_l = math.sqrt((B + 4*G/3) * 1e9 / rho)
    V_m = (1.0/3.0 * (2.0/v_s**3 + 1.0/v_l**3)) ** (-1.0/3.0)

    h = 6.62607015e-34
    kB = 1.380649e-23
    n_atoms_formula = 3
    M_kg_per_mol = M_FU / 1000.0
    factor = ( (3*n_atoms_formula)/(4*math.pi) * (NA * rho / M_kg_per_mol) ) ** (1.0/3.0)
    theta_D = h / kB * factor * V_m

    v_l_001 = math.sqrt(C33*1e9/rho)
    v_s_001 = math.sqrt(C44*1e9/rho)
    v_l_100 = math.sqrt(C11*1e9/rho)
    v_s1_100 = math.sqrt(C66*1e9/rho)
    v_s2_100 = v_s_001

    values = {
        "theta_D_K": theta_D,
        "v_s_m_per_s": v_s,
        "v_l_m_per_s": v_l,
        "V_m_m_per_s": V_m,
        "v_l_001_m_per_s": v_l_001,
        "v_s_001_m_per_s": v_s_001,
        "v_l_100_m_per_s": v_l_100,
        "v_s1_100_m_per_s": v_s1_100,
        "v_s2_100_m_per_s": v_s2_100
    }
    gold = step["params"]["gold"]
    tols = step["params"]["tolerances"]
    score = 0.0
    n = len(gold)
    for field, gval in gold.items():
        if field not in values:
            continue
        aval = values[field]
        tol = tols[field]
        if tol["type"] == "relative":
            if gval == 0:
                within = abs(aval) < 0.01
            else:
                within = abs(aval - gval) / abs(gval) <= tol["value"]
        else:
            within = abs(aval - gval) <= tol["value"]
        if within:
            score += 1
    return score / n


_SCORERS = {
    'structure': score_0,
    'formation_enthalpy': score_1,
    'elastic_constants': score_2,
    'mechanical_stability': score_3,
    'polycrystalline_moduli': score_4,
    'debye_sound_velocities': score_5,
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
