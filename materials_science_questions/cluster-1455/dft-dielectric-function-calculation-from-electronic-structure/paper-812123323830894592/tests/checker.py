import os
import json
import csv

# === author imports / helpers ===
import math
import csv


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


# === block: score_0 (check id='electronic') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # constants
        k_eV_ang2 = 33.55
        t_eV = 1.184
        q_VB_o_Ang = -0.12
        q_CT_o_Ang = 0.12
        delta_Ang = q_VB_o_Ang - q_CT_o_Ang
        mu_CT_D = 26.0
        mu_bar_kg = 1e-26
        me_kg = 9.10938356e-31
        hartree_to_eV = 27.211386
        Bohr_to_Ang = 0.52917721067
        au_debye = 2.541746
        eV_to_au = 1.0 / hartree_to_eV
        Ang_to_au = 1.0 / Bohr_to_Ang
        k_au = k_eV_ang2 * hartree_to_eV / (Bohr_to_Ang**2)
        t_au = t_eV * eV_to_au
        delta_au = delta_Ang * Ang_to_au
        mu_CT_au = mu_CT_D / au_debye
        mu_bar_au = mu_bar_kg / me_kg
        alpha_au_to_10m24 = 0.1481847
        beta_au_to_10m30 = 8.6392e-3
        gamma_au_to_10m33 = 5.044e-7
        tol_rel = float(step.get('tolerance_rel', 1e-4))
        tol_abs = float(step.get('tolerance_abs', 1e-10))
        cols = step.get('columns', ['mu_el','alpha_el','beta_el','gamma_el'])
        ok = 0
        total = 0
        for row in artifact:
            try:
                f = float(row['f'])
            except (ValueError, KeyError):
                continue
            if f <= 0.0:
                V_au = 1e6*t_au
            elif f >= 1.0:
                V_au = -1e6*t_au
            else:
                V_au = t_au * (1.0 - 2.0*f) / math.sqrt(f*(1.0-f))
            V2 = V_au*V_au
            t2 = t_au*t_au
            denom_el1 = V2 - 4.0*t2
            if denom_el1 <= 0.0:
                continue
            alpha_el_au = (2.0 * mu_CT_au**2 * t2) / (denom_el1**1.5)
            beta_el_au  = (6.0 * mu_CT_au**3 * t2 * V_au) / (denom_el1**2.5)
            gamma_el_au = (24.0 * mu_CT_au**4 * t2 * (V2 - t2)) / (denom_el1**3.5)
            mu_el_au = mu_CT_au * f
            mu_el_D = mu_el_au * au_debye
            alpha_el_24 = alpha_el_au * alpha_au_to_10m24
            beta_el_30  = beta_el_au * beta_au_to_10m30
            gamma_el_33 = gamma_el_au * gamma_au_to_10m33
            ref_vals = [mu_el_D, alpha_el_24, beta_el_30, gamma_el_33]
            for c, rv in zip(cols, ref_vals):
                try:
                    av = float(row[c])
                except (ValueError, KeyError):
                    continue
                total += 1
                err = abs(av - rv)
                if err <= tol_abs + tol_rel * max(abs(rv), 1e-10):
                    ok += 1
        return ok / total if total > 0 else 0.0


# === block: score_1 (check id='vibrational') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # constants
        k_eV_ang2 = 33.55
        t_eV = 1.184
        q_VB_o_Ang = -0.12
        q_CT_o_Ang = 0.12
        delta_Ang = q_VB_o_Ang - q_CT_o_Ang
        mu_CT_D = 26.0
        mu_bar_kg = 1e-26
        me_kg = 9.10938356e-31
        hartree_to_eV = 27.211386
        Bohr_to_Ang = 0.52917721067
        au_debye = 2.541746
        eV_to_au = 1.0 / hartree_to_eV
        Ang_to_au = 1.0 / Bohr_to_Ang
        k_au = k_eV_ang2 * hartree_to_eV / (Bohr_to_Ang**2)
        t_au = t_eV * eV_to_au
        delta_au = delta_Ang * Ang_to_au
        mu_CT_au = mu_CT_D / au_debye
        mu_bar_au = mu_bar_kg / me_kg
        alpha_au_to_10m24 = 0.1481847
        beta_au_to_10m30 = 8.6392e-3
        gamma_au_to_10m33 = 5.044e-7
        tol_rel = float(step.get('tolerance_rel', 1e-4))
        tol_abs = float(step.get('tolerance_abs', 1e-10))
        cols = step.get('columns', ['mu_vib','alpha_vib','beta_vib','gamma_vib'])
        ok = 0
        total = 0
        for row in artifact:
            try:
                f = float(row['f'])
            except (ValueError, KeyError):
                continue
            if f <= 0.0:
                V_au = 1e6*t_au
            elif f >= 1.0:
                V_au = -1e6*t_au
            else:
                V_au = t_au * (1.0 - 2.0*f) / math.sqrt(f*(1.0-f))
            V2 = V_au*V_au
            t2 = t_au*t_au
            denom_el1 = V2 - 4.0*t2
            if denom_el1 <= 0.0:
                continue
            alpha_el_au = (2.0 * mu_CT_au**2 * t2) / (denom_el1**1.5)
            beta_el_au  = (6.0 * mu_CT_au**3 * t2 * V_au) / (denom_el1**2.5)
            gamma_el_au = (24.0 * mu_CT_au**4 * t2 * (V2 - t2)) / (denom_el1**3.5)
            sqrt_denom_plus = math.sqrt(V2 + 4.0*t2)
            B = (6.0 * k_au * t2 * delta_au**2) / ( (sqrt_denom_plus**3) - 2.0 * k_au * t2 * delta_au**2 )
            mu_vib_au = 0.0
            alpha_vib_au = (2.0/3.0) * B * alpha_el_au
            beta_vib_au = B * (1.0 + B/3.0 + B**2/27.0) * beta_el_au
            R = 9.0 * V2 / (8.0 * (V2 - t2))
            C_vib = 1.5 + B/3.0 + B**2/36.0
            gamma_vib_au = (2.0*B/3.0) * ( 2.0 + R + (2.0*B/3.0)*(C_vib + 2.0*R*(1.0 + B*C_vib/3.0)) ) * gamma_el_au
            mu_vib_D = mu_vib_au * au_debye
            alpha_vib_24 = alpha_vib_au * alpha_au_to_10m24
            beta_vib_30  = beta_vib_au * beta_au_to_10m30
            gamma_vib_33 = gamma_vib_au * gamma_au_to_10m33
            ref_vals = [mu_vib_D, alpha_vib_24, beta_vib_30, gamma_vib_33]
            for c, rv in zip(cols, ref_vals):
                try:
                    av = float(row[c])
                except (ValueError, KeyError):
                    continue
                total += 1
                err = abs(av - rv)
                if err <= tol_abs + tol_rel * max(abs(rv), 1e-10):
                    ok += 1
        return ok / total if total > 0 else 0.0


# === block: score_2 (check id='curvature') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        k_eV_ang2 = 33.55
        t_eV = 1.184
        q_VB_o_Ang = -0.12
        q_CT_o_Ang = 0.12
        delta_Ang = q_VB_o_Ang - q_CT_o_Ang
        mu_CT_D = 26.0
        mu_bar_kg = 1e-26
        me_kg = 9.10938356e-31
        hartree_to_eV = 27.211386
        Bohr_to_Ang = 0.52917721067
        au_debye = 2.541746
        eV_to_au = 1.0 / hartree_to_eV
        Ang_to_au = 1.0 / Bohr_to_Ang
        k_au = k_eV_ang2 * hartree_to_eV / (Bohr_to_Ang**2)
        t_au = t_eV * eV_to_au
        delta_au = delta_Ang * Ang_to_au
        mu_CT_au = mu_CT_D / au_debye
        mu_bar_au = mu_bar_kg / me_kg
        alpha_au_to_10m24 = 0.1481847
        beta_au_to_10m30 = 8.6392e-3
        gamma_au_to_10m33 = 5.044e-7
        tol_rel = float(step.get('tolerance_rel', 1e-4))
        tol_abs = float(step.get('tolerance_abs', 1e-10))
        cols = step.get('columns', ['mu_cur','alpha_cur','beta_cur','gamma_cur'])
        ok = 0
        total = 0
        for row in artifact:
            try:
                f = float(row['f'])
            except (ValueError, KeyError):
                continue
            if f <= 0.0:
                V_au = 1e6*t_au
            elif f >= 1.0:
                V_au = -1e6*t_au
            else:
                V_au = t_au * (1.0 - 2.0*f) / math.sqrt(f*(1.0-f))
            V2 = V_au*V_au
            t2 = t_au*t_au
            sqrt_denom_plus = math.sqrt(V2 + 4.0*t2)
            K_au = k_au * (1.0 - (2.0 * k_au * t2 * delta_au**2) / (sqrt_denom_plus**3))
            C_au = k_au * delta_au / mu_CT_au
            B = (6.0 * k_au * t2 * delta_au**2) / ( (sqrt_denom_plus**3) - 2.0 * k_au * t2 * delta_au**2 )
            denom_el1 = V2 - 4.0*t2
            if denom_el1 <= 0.0 or K_au <= 0.0:
                continue
            alpha_el_au = (2.0 * mu_CT_au**2 * t2) / (denom_el1**1.5)
            beta_el_au  = (6.0 * mu_CT_au**3 * t2 * V_au) / (denom_el1**2.5)
            gamma_el_au = (24.0 * mu_CT_au**4 * t2 * (V2 - t2)) / (denom_el1**3.5)
            delta_el_au = (120.0 * mu_CT_au**5 * t2 * V_au * (V2 - 3.0*t2)) / (denom_el1**4.5)
            chi_el_au   = (720.0 * mu_CT_au**6 * t2 * (V2**2 - 6.0*V2*t2 + 2.0*t2*t2)) / ((V2 + 4.0*t2)**5.5)
            pref = 1.0 / (4.0 * math.sqrt(mu_bar_au * K_au))
            mu_cur_au = pref * C_au**2 * (1.0 + B/3.0) * beta_el_au
            term_alpha = (1.0 + B/3.0)**2 * ( gamma_el_au + (beta_el_au**2) * ( B/(3.0*alpha_el_au) + C_au**2/(2.0*K_au) ) )
            alpha_cur_au = pref * C_au**2 * term_alpha
            term_beta  = (1.0 + B/3.0)**3 * ( delta_el_au
                    + (11.0 * B * C_au**2 * beta_el_au * gamma_el_au) / (6.0 * alpha_el_au)
                    + (7.0 * B**2 * beta_el_au**3) / (12.0 * alpha_el_au**2) )
            beta_cur_au = pref * C_au**2 * term_beta
            term_gamma = (1.0 + B/3.0)**4 * ( chi_el_au
                    + (8.0 * B * beta_el_au * delta_el_au) / (3.0 * alpha_el_au)
                    + (11.0 * B * gamma_el_au**2) / (6.0 * alpha_el_au)
                    + (122.0 * B**2 * beta_el_au**2 * gamma_el_au) / (36.0 * alpha_el_au**2)
                    + (37.0 * B**3 * beta_el_au**4) / (72.0 * alpha_el_au**3) )
            gamma_cur_au = pref * C_au**2 * term_gamma
            mu_cur_D = mu_cur_au * au_debye
            alpha_cur_24 = alpha_cur_au * alpha_au_to_10m24
            beta_cur_30  = beta_cur_au * beta_au_to_10m30
            gamma_cur_33 = gamma_cur_au * gamma_au_to_10m33
            ref_vals = [mu_cur_D, alpha_cur_24, beta_cur_30, gamma_cur_33]
            for c, rv in zip(cols, ref_vals):
                try:
                    av = float(row[c])
                except (ValueError, KeyError):
                    continue
                total += 1
                err = abs(av - rv)
                if err <= tol_abs + tol_rel * max(abs(rv), 1e-10):
                    ok += 1
        return ok / total if total > 0 else 0.0


_SCORERS = {
    'electronic': score_0,
    'vibrational': score_1,
    'curvature': score_2,
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
