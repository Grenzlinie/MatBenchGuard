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
    return {}


# === block: score_0 (check id='step_pl_shifts') ===
def score_0(artifact, step, ctx):
    import math

    def strains(e_par, e_perp):
        e_h = (2.0 * e_par + e_perp) / 3.0
        e_u = 2.0 * (e_perp - e_par)
        return e_h, e_u

    def delta_Eg(ag, d5, e_h, e_u):
        return 3.0 * ag * e_h - 1.5 * (d5 / math.sqrt(6.0)) * e_u

    const = step['constants']
    a_GaN = const['a_GaN']
    a_InN = const['a_InN']
    C13_GaN = const['C13_GaN']
    C33_GaN = const['C33_GaN']
    C13_InN = const['C13_InN']
    C33_InN = const['C33_InN']
    ag_GaN = const['ag_GaN']
    d5_GaN = const['d5_GaN']
    ag_InN = const['ag_InN']
    d5_InN = const['d5_InN']
    e31_GaN = const['e31_GaN']
    e33_GaN = const['e33_GaN']
    e31_InN = const['e31_InN']
    e33_InN = const['e33_InN']
    Psp_GaN = const['Psp_GaN']
    Psp_InN = const['Psp_InN']
    kappa_GaN = const['kappa_GaN']
    kappa_InN = const['kappa_InN']
    eps_pre = const['eps_pre']
    d_w = const['d_w']
    L_b = const['L_b']
    eps0 = const['eps0']
    tol = step['tolerance_meV']

    in_contents = [0.025, 0.085, 0.119]
    strain_values = [0.0, 2e-4, 4e-4, 6e-4, 8e-4]

    expected = {}
    for x in in_contents:
        a_w = a_GaN + x * (a_InN - a_GaN)
        C13_w = C13_GaN + x * (C13_InN - C13_GaN)
        C33_w = C33_GaN + x * (C33_InN - C33_GaN)
        ag_w = ag_GaN + x * (ag_InN - ag_GaN)
        d5_w = d5_GaN + x * (d5_InN - d5_GaN)
        e31_w = e31_GaN + x * (e31_InN - e31_GaN)
        e33_w = e33_GaN + x * (e33_InN - e33_GaN)
        Psp_w = Psp_GaN + x * (Psp_InN - Psp_GaN)
        kappa_w = kappa_GaN + x * (kappa_InN - kappa_GaN)
        emis = (a_GaN - a_w) / a_w

        e_par_b0 = eps_pre
        e_perp_b0 = -2.0 * (C13_GaN / C33_GaN) * e_par_b0
        e_par_w0 = emis + eps_pre
        e_perp_w0 = -2.0 * (C13_w / C33_w) * e_par_w0
        P_b0 = Psp_GaN + 2.0 * e31_GaN * e_par_b0 + e33_GaN * e_perp_b0
        P_w0 = Psp_w + 2.0 * e31_w * e_par_w0 + e33_w * e_perp_w0
        denom0 = eps0 * (kappa_w + kappa_GaN * d_w / L_b)
        E_w0 = (P_b0 - P_w0) / denom0
        e_h_w0, e_u_w0 = strains(e_par_w0, e_perp_w0)
        Eg_w0 = delta_Eg(ag_w, d5_w, e_h_w0, e_u_w0)
        QCSE0 = E_w0 * d_w

        for eps in strain_values:
            e_par_b = eps_pre + eps
            e_perp_b = -2.0 * (C13_GaN / C33_GaN) * e_par_b
            e_par_w = emis + eps_pre + eps
            e_perp_w = -2.0 * (C13_w / C33_w) * e_par_w
            e_h_w, e_u_w = strains(e_par_w, e_perp_w)
            Eg_w = delta_Eg(ag_w, d5_w, e_h_w, e_u_w)
            P_b = Psp_GaN + 2.0 * e31_GaN * e_par_b + e33_GaN * e_perp_b
            P_w = Psp_w + 2.0 * e31_w * e_par_w + e33_w * e_perp_w
            denom = eps0 * (kappa_w + kappa_GaN * d_w / L_b)
            E_w = (P_b - P_w) / denom
            dEg = Eg_w - Eg_w0
            dQCSE = (E_w - E_w0) * d_w
            net_shift_meV = (dEg + dQCSE) * 1000.0
            expected[(x, eps)] = net_shift_meV

    row_dict = {}
    for row in artifact:
        try:
            x = float(row['In_content'])
            eps = float(row['strain'])
            row_dict[(x, eps)] = float(row['PL_shift_meV'])
        except Exception:
            continue

    total = len(in_contents) * len(strain_values)
    correct = 0
    for x in in_contents:
        for eps in strain_values:
            key = (x, eps)
            if key in row_dict and abs(row_dict[key] - expected[key]) <= tol:
                correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_corrected_coefficients') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']
    score = 0.0
    if isinstance(artifact, dict):
        if abs(artifact.get('linear_delta_PPZ1', 0) - gold['linear_delta_PPZ1']) <= tol['linear_delta_PPZ1']:
            score += 0.5
        if abs(artifact.get('cubic_delta_PPZ3', 0) - gold['cubic_delta_PPZ3']) <= tol['cubic_delta_PPZ3']:
            score += 0.5
    return score


_SCORERS = {
    'step_pl_shifts': score_0,
    'step_corrected_coefficients': score_1,
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
