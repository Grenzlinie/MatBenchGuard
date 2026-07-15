import os
import json
import csv

# === author imports / helpers ===
import math


def get_float(row, key, default=None):
    try:
        v = row.get(key)
        if v is None or v == '':
            return default
        return float(v)
    except (ValueError, TypeError):
        return default


def score_closeness_rel(value, target, tol_rel):
    if target == 0:
        return 1.0 if abs(value) < 1e-9 else 0.0
    rel_err = abs(value - target) / abs(target)
    return max(0.0, min(1.0, 1.0 - (rel_err / tol_rel)))


def score_closeness_abs(value, target, tol_abs):
    abs_err = abs(value - target)
    return max(0.0, min(1.0, 1.0 - (abs_err / tol_abs)))


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


# === block: score_0 (check id='step_equilibrium') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    structures = ["ZB", "RS", "CsCl", "WZ"]
    gold_a0 = step["gold_a0"]
    gold_B = step["gold_B"]
    gold_Bprime = step["gold_Bprime"]
    tol_a0 = step.get("tol_a0_pct", 0.02)
    tol_B = step.get("tol_B_pct", 0.10)
    tol_Bprime_abs = step.get("tol_Bprime_abs", 0.3)

    rows_by_struct = {r["structure"].strip(): r for r in artifact if "structure" in r}

    struct_scores = []
    for s in structures:
        row = rows_by_struct.get(s)
        if not row:
            struct_scores.append(0.0)
            continue
        a0 = get_float(row, "a0", None)
        if a0 is None:
            struct_scores.append(0.0)
            continue
        ref_a0 = gold_a0[s]
        score_a0 = score_closeness_rel(a0, ref_a0, tol_a0)

        B = get_float(row, "B", None)
        if B is None:
            struct_scores.append(0.0)
            continue
        ref_B = gold_B[s]
        score_B = score_closeness_rel(B, ref_B, tol_B)

        Bprime = get_float(row, "Bprime", None)
        if Bprime is None:
            struct_scores.append(0.0)
            continue
        ref_Bprime = gold_Bprime[s]
        score_Bprime = score_closeness_abs(Bprime, ref_Bprime, tol_Bprime_abs)

        struct_scores.append((score_a0 + score_B + score_Bprime) / 3.0)

    # energy ordering
    ordering_score = 0.0
    zb_row = rows_by_struct.get("ZB")
    if zb_row:
        e_zb = get_float(zb_row, "energy_above_ground", None)
        if e_zb is not None and abs(e_zb) < 1e-6:
            ordering_score += 0.2
        else:
            ordering_score += 0.0
    else:
        ordering_score = 0.0

    wz_row = rows_by_struct.get("WZ")
    if wz_row:
        e_wz = get_float(wz_row, "energy_above_ground", None)
        if e_wz is not None and e_wz > 0 and e_wz <= step.get("energy_above_ground_max", 0.68):
            ordering_score += 0.4
        elif e_wz is not None and e_wz > 0:
            ordering_score += 0.2

    other_positive = True
    for s in ["RS", "CsCl"]:
        row = rows_by_struct.get(s)
        if row:
            e = get_float(row, "energy_above_ground", None)
            if e is None or e <= 0:
                other_positive = False
                break
        else:
            other_positive = False
            break
    if other_positive:
        ordering_score += 0.4

    wz_extra = 0.0
    if wz_row:
        c0 = get_float(wz_row, "c0", None)
        if c0 is not None:
            s_c0 = score_closeness_rel(c0, step["gold_WZ_c0"], step.get("tol_WZ_c0_pct", 0.02))
            wz_extra += s_c0 * 0.3
        u = get_float(wz_row, "u", None)
        if u is not None:
            s_u = score_closeness_abs(u, step["gold_WZ_u"], step.get("tol_WZ_u_abs", 0.02))
            wz_extra += s_u * 0.3
        ca = get_float(wz_row, "c_a", None)
        if ca is not None:
            s_ca = score_closeness_abs(ca, step["gold_WZ_ca"], step.get("tol_WZ_ca_abs", 0.02))
            wz_extra += s_ca * 0.3
        ordering_score += 0.1 * min(1.0, wz_extra)

    avg_struct = sum(struct_scores) / len(struct_scores) if struct_scores else 0.0
    total = 0.7 * avg_struct + 0.3 * min(1.0, ordering_score)
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='step_elastic') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    C11 = get_float(row, "C11", None)
    C12 = get_float(row, "C12", None)
    C44 = get_float(row, "C44", None)
    B_agent = get_float(row, "B", None)
    if any(x is None for x in [C11, C12, C44, B_agent]):
        return 0.0

    gold = step["gold"]
    tol_cij_rel = step.get("tol_Cij_rel", 0.10)
    tol_cij_abs = step.get("tol_Cij_abs", 20.0)
    tol_der_rel = step.get("tol_derived_rel", 0.15)
    tol_der_abs_gpa = step.get("tol_derived_abs", 5.0)
    tol_nu_abs = step.get("tol_nu_abs", 0.15)
    tol_A_abs = step.get("tol_A_abs", 0.1)
    tol_zeta_abs = step.get("tol_zeta_abs", 0.1)
    tol_v_abs = step.get("tol_v_abs", 500.0)
    tol_theta_abs = step.get("tol_theta_abs", 50.0)

    def cij_score(val, target):
        rel = score_closeness_rel(val, target, tol_cij_rel) if target != 0 else 1.0
        abs_err = abs(val - target)
        abs_score = max(0.0, 1.0 - abs_err / tol_cij_abs)
        return max(rel, abs_score)

    s_C11 = cij_score(C11, gold["C11"])
    s_C12 = cij_score(C12, gold["C12"])
    s_C44 = cij_score(C44, gold["C44"])
    s_B_cij = cij_score(B_agent, gold["B"])

    # recompute derived
    G_v = (C11 - C12 + 3*C44) / 5.0
    denom_gr = 4.0 / (C11 - C12) + 3.0 / C44 if (C11 - C12) != 0 and C44 != 0 else 0.0
    G_r = 5.0 / denom_gr if denom_gr != 0 else 0.0
    G = (G_v + G_r) / 2.0
    E = 9*G*B_agent / (G + 3*B_agent) if (G + 3*B_agent) != 0 else 0.0
    nu = 0.5 * ((B_agent - (2/3)*G) / (B_agent + (1/3)*G)) if (B_agent + (1/3)*G) != 0 else 0.0
    A = 2*C44 / (C11 - C12) if (C11 - C12) != 0 else 0.0
    zeta = (C11 + 8*C12) / (7*C11 + 2*C12) if (7*C11 + 2*C12) != 0 else 0.0
    lambda_ = nu * E / ((1 + nu) * (1 - 2*nu)) if (1 + nu) != 0 and (1 - 2*nu) != 0 else 0.0
    mu = E / (2 * (1 + nu)) if (1 + nu) != 0 else 0.0

    # density from a0=4.67 Angstrom, M=120.43 g/mol, 4 atoms/unit cell
    a0_zb = 4.67e-10
    M = 120.43e-3
    N_A = 6.02214076e23
    rho = (4 * M) / (N_A * (a0_zb ** 3))  # kg/m3

    vl = math.sqrt((3*B_agent + 4*G) / (3*rho)) if rho > 0 else 0.0
    vt = math.sqrt(G / rho) if rho > 0 else 0.0
    vm = ((1/3) * (2/(vt**3) + 1/(vl**3))) ** (-1/3) if vl > 0 and vt > 0 else 0.0

    h = 6.62607015e-34
    k_B = 1.380649e-23
    n = 2
    theta_D = (h/k_B) * ((3*n)/(4*math.pi) * (N_A * rho / M)) ** (1/3) * vm if vm > 0 else 0.0

    def derived_score(val, target, tol_abs=None):
        if target == 0:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel = score_closeness_rel(val, target, tol_der_rel)
        if tol_abs is not None:
            abs_score = max(0.0, 1.0 - abs(val - target) / tol_abs)
            return max(rel, abs_score)
        return rel

    s_G = derived_score(G, gold["G"], tol_der_abs_gpa)
    s_E = derived_score(E, gold["E"], tol_der_abs_gpa)
    s_nu = derived_score(nu, gold["nu"], tol_nu_abs)
    s_A = derived_score(A, gold["A"], tol_A_abs)
    s_zeta = derived_score(zeta, gold["zeta"], tol_zeta_abs)
    s_lambda = derived_score(lambda_, gold["lambda"], tol_der_abs_gpa)
    s_mu = derived_score(mu, gold["mu"], tol_der_abs_gpa)
    s_vl = derived_score(vl, gold["vl"], tol_v_abs)
    s_vt = derived_score(vt, gold["vt"], tol_v_abs)
    s_vm = derived_score(vm, gold["vm"], tol_v_abs)
    s_theta = derived_score(theta_D, gold["theta_D"], tol_theta_abs)

    cij_scores = [s_C11, s_C12, s_C44, s_B_cij]
    mean_cij = sum(cij_scores) / len(cij_scores)
    der_scores = [s_G, s_E, s_nu, s_A, s_zeta, s_lambda, s_mu, s_vl, s_vt, s_vm, s_theta]
    mean_der = sum(der_scores) / len(der_scores)
    total = 0.4 * mean_cij + 0.6 * mean_der
    return max(0.0, min(1.0, total))


_SCORERS = {
    'step_equilibrium': score_0,
    'step_elastic': score_1,
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
