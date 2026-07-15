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


# === block: score_0 (check id='structural_elastic') ===
def score_0(artifact, step, ctx):
    tol = step.get("tolerances", {})
    gold = step.get("gold", {})
    a_tol = tol.get("a", 0.03)
    b_tol = tol.get("B", 0.10)
    bp_tol = tol.get("Bp", 0.10)
    ecoh_tol = tol.get("Ecoh", 0.10)
    cij_tol = tol.get("Cij", 0.10)
    derived_tol = tol.get("derived", 0.05)
    total_score = 0
    total_count = 0
    for comp in ["HoAs", "HoP"]:
        if comp not in artifact:
            continue
        a = artifact[comp]
        g = gold.get(comp, {})
        raw_fields = [
            ("lattice_constant_A", a_tol, g.get("lattice_constant_A", 0)),
            ("bulk_modulus_GPa", b_tol, g.get("bulk_modulus_GPa", 0)),
            ("pressure_derivative", bp_tol, g.get("pressure_derivative", 0)),
            ("cohesive_energy_eV_per_atom", ecoh_tol, g.get("cohesive_energy_eV_per_atom", 0)),
            ("C11_GPa", cij_tol, g.get("C11_GPa", 0)),
            ("C12_GPa", cij_tol, g.get("C12_GPa", 0)),
            ("C44_GPa", cij_tol, g.get("C44_GPa", 0)),
        ]
        for field, t, gold_val in raw_fields:
            val = a.get(field)
            if val is None or gold_val is None:
                continue
            rel_err = abs(val - gold_val) / (abs(gold_val) if gold_val != 0 else 1.0)
            total_score += 1.0 if rel_err <= t else 0.0
            total_count += 1
        C11 = a.get("C11_GPa")
        C12 = a.get("C12_GPa")
        C44 = a.get("C44_GPa")
        B_ = a.get("bulk_modulus_GPa")
        if None not in (C11, C12, C44, B_):
            denom = C11 - C12
            A = 2 * C44 / denom if denom != 0 else float('inf')
            Gv = (C11 - C12 + 3 * C44) / 5.0
            Gr = 5.0 / (4.0 / (C11 - C12) + 3.0 / C44) if C44 != 0 else 0.0
            G = (Gv + Gr) / 2.0
            nu = 0.5 * (B_ - (2.0/3.0)*G) / (B_ + (1.0/3.0)*G) if (B_ + (1.0/3.0)*G) != 0 else 0.5
            E = 9 * G * B_ / (G + 3 * B_) if (G + 3 * B_) != 0 else 0.0
            derived = [
                ("Zener_anisotropy_A", A, g.get("Zener_anisotropy_A", 0)),
                ("Poisson_ratio_nu", nu, g.get("Poisson_ratio_nu", 0)),
                ("Young_modulus_E_GPa", E, g.get("Young_modulus_E_GPa", 0)),
                ("shear_modulus_G_GPa", G, g.get("shear_modulus_G_GPa", 0)),
            ]
            for field, comp_val, gold_val in derived:
                if gold_val is None or comp_val is None:
                    continue
                rel_err = abs(comp_val - gold_val) / (abs(gold_val) if gold_val != 0 else 1.0)
                total_score += 1.0 if rel_err <= derived_tol else 0.0
                total_count += 1
    return total_score / total_count if total_count > 0 else 0.0


# === block: score_1 (check id='phonon_stability') ===
def score_1(artifact, step, ctx):
    threshold = step.get("threshold", -1.0)
    passed = 0
    for comp in ["HoAs", "HoP"]:
        entry = artifact.get(comp)
        if not entry:
            continue
        freq = entry.get("lowest_phonon_frequency_cm-1")
        flag = entry.get("has_imaginary_modes")
        if freq is not None and isinstance(flag, bool):
            if freq >= threshold and flag is False:
                passed += 1
    return passed / 2.0 if passed > 0 else 0.0


# === block: score_2 (check id='thermodynamics') ===
def score_2(artifact, step, ctx):
    gold = step.get("gold", {})
    req = step.get("required_points", {})
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    # Build dict compound -> list of rows
    comp_data = {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        c = r.get("compound")
        if c not in comp_data:
            comp_data[c] = []
        comp_data[c].append(r)

    def find_row(data, T, P):
        for r in data:
            if abs(float(r.get("temperature_K", 0)) - T) < 0.1 and abs(float(r.get("pressure_GPa", 0)) - P) < 0.1:
                return r
        return None

    score = 0.0
    # 1. Completeness of required points (0.1)
    req_0GPa = req.get("0_GPa", [])
    req_0K = req.get("0_K", [])
    exist_score = 0.0
    for comp in ["HoAs", "HoP"]:
        d = comp_data.get(comp, [])
        if not d:
            continue
        all_found = True
        for T in req_0GPa:
            if find_row(d, T, 0) is None:
                all_found = False
                break
        for P in req_0K:
            if find_row(d, 0, P) is None:
                all_found = False
                break
        if all_found:
            exist_score += 0.5
    score += exist_score * 0.1

    # 2. Trends (0.4 total => 0.4 weight, sub-parts 0.2 + 0.2)
    def get_val(data, T, P, field):
        r = find_row(data, T, P)
        if r:
            try:
                return float(r[field])
            except:
                return None
        return None

    trend_score = 0.0
    for comp in ["HoAs", "HoP"]:
        d = comp_data.get(comp, [])
        if not d:
            continue
        # a. Cv at 2000K, 0GPa >= 45
        cv2000 = get_val(d, 2000, 0, "Cv_J_molK")
        if cv2000 is not None and cv2000 >= 45:
            trend_score += 0.05
        # b. Debye temperature decreasing: Theta0K > Theta2000K
        theta0 = get_val(d, 0, 0, "Debye_temperature_K")
        theta2000 = get_val(d, 2000, 0, "Debye_temperature_K")
        if theta0 is not None and theta2000 is not None and theta0 > theta2000:
            trend_score += 0.05
        # c. Thermal expansion coefficient increasing: alpha400 > alpha0 and alpha2000 > alpha400
        alpha0 = get_val(d, 0, 0, "thermal_expansion_coefficient_K-1")
        alpha400 = get_val(d, 400, 0, "thermal_expansion_coefficient_K-1")
        alpha2000 = get_val(d, 2000, 0, "thermal_expansion_coefficient_K-1")
        if (alpha0 is not None and alpha400 is not None and alpha400 >= alpha0 and 
            alpha2000 is not None and alpha2000 >= alpha400):
            trend_score += 0.1
    score += trend_score * 0.4

    # 3. Reference point values (0.5)
    ref_score = 0.0
    cv_tol = gold.get("Cv_tol", 0.10)
    debye_tol = gold.get("Debye_tol", 0.05)
    for comp, gold_cv in gold.get("Cv_300K", {}).items():
        d = comp_data.get(comp, [])
        val = get_val(d, 300, 0, "Cv_J_molK")
        if val is not None and gold_cv > 0:
            rel_err = abs(val - gold_cv) / gold_cv
            if rel_err <= cv_tol:
                ref_score += 0.15
        # other? no
    for comp, gold_debye in gold.get("Debye_0K_0GPa", {}).items():
        d = comp_data.get(comp, [])
        val = get_val(d, 0, 0, "Debye_temperature_K")
        if val is not None and gold_debye > 0:
            rel_err = abs(val - gold_debye) / gold_debye
            if rel_err <= debye_tol:
                ref_score += 0.15
    score += ref_score * 0.5
    return min(score, 1.0)


_SCORERS = {
    'structural_elastic': score_0,
    'phonon_stability': score_1,
    'thermodynamics': score_2,
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
