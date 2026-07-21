import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    ctx = {}
    outputs_dir = '/app/outputs'

    # recompute epsilon_u from step_01
    fpath01 = os.path.join(outputs_dir, 'step_01_stress_strain_fbc1.csv')
    if os.path.exists(fpath01):
        try:
            with open(fpath01, newline='') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            if data and all(k in data[0] for k in ('strain','stress_xx')):
                strains = [float(row['strain']) for row in data]
                stresses = [float(row['stress_xx']) for row in data]
                if len(strains) >= 100 and min(strains) <= 0.0 and max(strains) >= 0.039:
                    peak = max(stresses)
                    threshold = 0.9 * peak
                    epsilon_u = None
                    for i, s in enumerate(stresses):
                        if s < threshold:
                            later = stresses[i:i+5]
                            if later and all(x < threshold*1.05 for x in later):
                                epsilon_u = strains[i]
                                break
                    ctx['epsilon_u_recomputed'] = epsilon_u
                else:
                    ctx['epsilon_u_recomputed'] = None
            else:
                ctx['epsilon_u_recomputed'] = None
        except Exception:
            ctx['epsilon_u_recomputed'] = None
    else:
        ctx['epsilon_u_recomputed'] = None

    # recompute deltaV from step_04
    fpath04 = os.path.join(outputs_dir, 'step_04_eta_scan_energy.csv')
    if os.path.exists(fpath04):
        try:
            with open(fpath04, newline='') as f:
                reader = csv.DictReader(f)
                etadata = list(reader)
            if etadata and all(k in etadata[0] for k in ('eta','potential_energy')):
                etas = [float(row['eta']) for row in etadata]
                energies = [float(row['potential_energy']) for row in etadata]
                if len(etas) >= 21:
                    # find closest to eta=-1 and eta=0
                    idx_neg = min(range(len(etas)), key=lambda i: abs(etas[i] + 1.0))
                    idx_zero = min(range(len(etas)), key=lambda i: abs(etas[i] - 0.0))
                    dV_eV = energies[idx_zero] - energies[idx_neg]
                    ctx['deltaV_recomputed_mev'] = dV_eV * 1000.0
                else:
                    ctx['deltaV_recomputed_mev'] = None
            else:
                ctx['deltaV_recomputed_mev'] = None
        except Exception:
            ctx['deltaV_recomputed_mev'] = None
    else:
        ctx['deltaV_recomputed_mev'] = None

    return ctx


# === block: score_0 (check id='step_01_stress_strain_fbc1') ===
def score_0(artifact, step, ctx):
    import math
    gold = step.get('gold_epsilon_u', 0.0336)
    tol = step.get('tol_epsilon_u', 0.002)
    max_tol = step.get('max_tol_epsilon_u', 0.008)

    e_u = ctx.get('epsilon_u_recomputed')
    if e_u is None:
        return 0.0

    # score epsilon_u
    abs_error = abs(e_u - gold)
    if abs_error <= tol:
        eps_score = 1.0
    elif abs_error >= max_tol:
        eps_score = 0.0
    else:
        eps_score = 1.0 - (abs_error - tol) / (max_tol - tol)

    # structural audit: FBC‑1 should have a plateau above ~15 GPa and a drop after εu
    struct_ok = True
    art = artifact
    if not art or not isinstance(art, list):
        struct_ok = False
    else:
        try:
            strains = [float(r['strain']) for r in art]
            stresses = [float(r['stress_xx']) for r in art]
            peak = max(stresses)
            if peak < 15.0:
                struct_ok = False
            # check that stress after εu (e.g., strain > 0.035) is below 5 GPa
            post_unlock = [s for e,s in zip(strains, stresses) if e > 0.035]
            if not post_unlock or max(post_unlock) > 5.0:
                struct_ok = False
        except Exception:
            struct_ok = False

    struct_score = 1.0 if struct_ok else 0.0
    return 0.7 * eps_score + 0.3 * struct_score


# === block: score_1 (check id='step_02_stress_strain_fbc+1') ===
def score_1(artifact, step, ctx):
    art = artifact
    if not art or not isinstance(art, list):
        return 0.0
    try:
        strains = [float(r['strain']) for r in art]
        stresses = [float(r['stress_xx']) for r in art]
        # FBC+1 must show abrupt drop: peak stress > 8 GPa, and stress after strain 0.006 falls below 1 GPa
        peak = max(stresses)
        abrupt = False
        if peak > 8.0:
            post_drop = [s for e,s in zip(strains, stresses) if e > 0.006]
            if post_drop and max(post_drop) < 1.0:
                abrupt = True
        # also peak should occur before strain 0.01
        peak_correct = False
        for e,s in zip(strains, stresses):
            if s == peak:
                if e < 0.01:
                    peak_correct = True
                break
        score = 0.0
        if abrupt: score += 0.7
        if peak_correct: score += 0.3
        return min(score, 1.0)
    except Exception:
        return 0.0


# === block: score_2 (check id='step_03_selfreported_epsilon_u') ===
def score_2(artifact, step, ctx):
    txt = artifact
    if not isinstance(txt, str):
        return 0.0
    lines = txt.strip().splitlines()
    if not lines:
        return 0.0
    try:
        self_e = float(lines[0].strip())
    except Exception:
        return 0.0

    gold = step.get('gold_epsilon_u', 0.0336)
    tol = step.get('tol_epsilon_u', 0.005)

    # compare to gold
    gold_pass = 1.0 if abs(self_e - gold) <= tol else 0.0

    # consistency with recomputed epsilon_u
    recomputed_e = ctx.get('epsilon_u_recomputed')
    if recomputed_e is None:
        consist = 0.0
    else:
        consist = 1.0 if abs(self_e - recomputed_e) <= 0.01 else 0.0

    return 0.5 * gold_pass + 0.5 * consist


# === block: score_3 (check id='step_04_eta_scan') ===
def score_3(artifact, step, ctx):
    import math
    art = artifact
    if not art or not isinstance(art, list):
        return 0.0

    try:
        etas = [float(r['eta']) for r in art]
        energies = [float(r['potential_energy']) for r in art]
        if len(etas) < 21:
            return 0.0
        idx_neg = min(range(len(etas)), key=lambda i: abs(etas[i] + 1.0))
        idx_pos = min(range(len(etas)), key=lambda i: abs(etas[i] - 1.0))
        idx_zero = min(range(len(etas)), key=lambda i: abs(etas[i] - 0.0))
        dV = energies[idx_zero] - energies[idx_neg]  # eV
        barrier_mev = dV * 1000.0
        ctx['_deltaV_recomputed'] = barrier_mev  # store for step_05
    
        gold = step.get('gold_barrier_mev', 600.0)
        tol = step.get('tol_barrier_mev', 100.0)
        error = abs(barrier_mev - gold)
        if error <= tol:
            barrier_score = 1.0
        elif error >= 2*tol:
            barrier_score = 0.0
        else:
            barrier_score = 1.0 - (error - tol) / tol

        # structural symmetry: V(η=-1) ≈ V(η=+1)
        sym_diff = abs(energies[idx_neg] - energies[idx_pos])
        sym_score = 1.0 if sym_diff < 0.05 * abs(gold/1000.0) else 0.0  # 5% of barrier
        return 0.8 * barrier_score + 0.2 * sym_score
    except Exception:
        return 0.0


# === block: score_4 (check id='step_05_selfreported_barrier') ===
def score_4(artifact, step, ctx):
    txt = artifact
    if not isinstance(txt, str):
        return 0.0
    lines = txt.strip().splitlines()
    if not lines:
        return 0.0
    try:
        self_barrier = float(lines[0].strip())
    except Exception:
        return 0.0

    gold = step.get('gold_barrier_mev', 600.0)
    tol = step.get('tol_barrier_mev', 100.0)

    gold_pass = 1.0 if abs(self_barrier - gold) <= tol else 0.0

    recomputed = ctx.get('deltaV_recomputed_mev')
    if recomputed is None:
        consist = 0.0
    else:
        consist = 1.0 if abs(self_barrier - recomputed) <= 30.0 else 0.0

    return 0.5 * gold_pass + 0.5 * consist


_SCORERS = {
    'step_01_stress_strain_fbc1': score_0,
    'step_02_stress_strain_fbc+1': score_1,
    'step_03_selfreported_epsilon_u': score_2,
    'step_04_eta_scan': score_3,
    'step_05_selfreported_barrier': score_4,
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
