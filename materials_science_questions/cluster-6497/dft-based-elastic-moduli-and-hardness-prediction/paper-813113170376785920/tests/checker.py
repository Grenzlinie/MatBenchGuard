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
    import json
    gold = spec.get('gold', {})
    return {'gold': gold}


# === block: score_0 (check id='lattice') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    if artifact is None:
        return 0.0
    score_sum = 0.0
    n_total = 0

    systems = ['ISW_NT', 'BSW_NT', 'ISW_NT_C', 'ISW_NT_Si']

    def rel_check(val, gold, rel_tol):
        if gold is None:
            return 0.0
        if val is None:
            return 0.0
        if gold == 0.0:
            return 1.0 if abs(val) <= rel_tol else 0.0
        err = abs(val - gold) / abs(gold)
        return 1.0 if err <= rel_tol else 0.0

    for sys in systems:
        if sys not in artifact:
            continue
        lat = artifact[sys].get('lattice_constants', {})
        g = gold.get(sys, {}).get('lattice_constants', {})
        if not g:
            continue
        for axis in ['a', 'b', 'c']:
            if axis not in g:
                continue
            gv = g[axis]
            av = lat.get(axis)
            if gv is None:
                score = 1.0 if av is None else 0.0
            else:
                if sys in ('ISW_NT', 'ISW_NT_C', 'ISW_NT_Si') and axis in ('a','b'):
                    # Must be 30.0 A with absolute tolerance of 0.5 A
                    score = 1.0 if av is not None and abs(av - 30.0) <= 0.5 else 0.0
                else:
                    # All other lattice constants: 2% relative tolerance
                    score = rel_check(av, gv, 0.02)
            score_sum += score
            n_total += 1

    if n_total == 0:
        return 0.0
    return round(score_sum / n_total, 6)


# === block: score_1 (check id='bulk_moduli') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold']
    score_sum = 0.0
    n_total = 0

    systems = ['ISW_NT', 'BSW_NT', 'ISW_NT_C', 'ISW_NT_Si']

    def rel_check(val, gold, tol):
        if gold is None:
            return 0.0 if val is not None else 1.0  # if gold is None, agent must also be None
        if val is None:
            return 0.0
        if gold == 0.0:
            return 1.0 if abs(val) <= tol else 0.0
        err = abs(val - gold) / abs(gold)
        return 1.0 if err <= tol else 0.0

    for sys in systems:
        if sys not in artifact:
            continue
        bm = artifact[sys].get('bulk_modulus', {})
        g = gold.get(sys, {}).get('bulk_modulus', {})
        if not g:
            continue
        for axis in ['a', 'b', 'c']:
            gv = g.get(axis)
            av = bm.get(axis)
            tol = 0.05 * abs(gv) if gv and gv != 0 else 1.0
            if gv is None:
                s = 1.0 if av is None else 0.0
            else:
                s = rel_check(av, gv, tol)
            score_sum += s
            n_total += 1

    if n_total == 0:
        return 0.0
    return round(score_sum / n_total, 6)


# === block: score_2 (check id='electronic') ===
def score_2(artifact, step, ctx):
    gold = ctx['gold']
    score_sum = 0.0
    n_total = 0

    systems = ['ISW_NT', 'BSW_NT', 'ISW_NT_C', 'ISW_NT_Si']

    def rel_check(val, gold, tol):
        if gold is None:
            if val is None:
                return 1.0
            # for band gap metallic: accept None or value < 0.1
            return 1.0 if isinstance(val, (int,float)) and val < 0.1 else 0.0
        if val is None:
            return 0.0
        if gold == 0.0:
            return 1.0 if abs(val) <= tol else 0.0
        err = abs(val - gold) / abs(gold)
        return 1.0 if err <= tol else 0.0

    def check_bandgap_type(sys, sys_data, g):
        # check band_gap_type string
        g_type = g.get('band_gap_type')
        a_type = sys_data.get('band_gap_type')
        if g_type is None:
            return 1.0 if a_type is None else 0.0
        return 1.0 if a_type and a_type.lower().strip() == g_type.lower().strip() else 0.0

    def check_transition(sys_data, g):
        g_trans = g.get('band_gap_transition')
        a_trans = sys_data.get('band_gap_transition')
        if g_trans is None:
            return 1.0 if a_trans is None else 0.0
        if not a_trans:
            return 0.0
        # Check that the transition string contains the two numeric fractions (e.g., 0.65, 0.95)
        import re
        nums = re.findall(r"[\d]+\.?[\d]*", g_trans)
        if len(nums) >= 2:
            n1, n2 = nums[0], nums[1]
            if n1 in a_trans and n2 in a_trans:
                return 1.0
            else:
                return 0.0
        return 0.5  # fallback partial

    for sys in systems:
        if sys not in artifact:
            continue
        sys_data = artifact[sys]
        g = gold.get(sys, {})
        if not g:
            continue
        # band gap
        g_bg = g.get('band_gap')
        a_bg = sys_data.get('band_gap')
        # special: Si-vacancy metallic
        if sys == 'ISW_NT_Si':
            if a_bg is None:
                score_bg = 1.0
            elif isinstance(a_bg, (int,float)) and a_bg < 0.1:
                score_bg = 1.0
            else:
                score_bg = 0.0
        else:
            tol = 0.05 * g_bg if g_bg != 0 else 0.1
            score_bg = rel_check(a_bg, g_bg, tol)
        score_sum += score_bg
        n_total += 1
        # band gap type
        score_sum += check_bandgap_type(sys, sys_data, g)
        n_total += 1
        # band gap transition
        score_sum += check_transition(sys_data, g)
        n_total += 1
        # effective mass electron
        em = sys_data.get('effective_mass', {})
        g_em = g.get('effective_mass', {})
        if sys == 'ISW_NT_Si':
            # only electron
            g_el = g_em.get('electron')
            a_el = em.get('electron')
            tol = 0.10 * abs(g_el) if g_el != 0 else 0.01
            score_sum += rel_check(a_el, g_el, tol)
            n_total += 1
        else:
            for carrier in ['electron', 'hole']:
                gv = g_em.get(carrier)
                av = em.get(carrier)
                tol = 0.10 * abs(gv) if gv and gv != 0 else 0.01
                s = rel_check(av, gv, tol)
                score_sum += s
                n_total += 1
        # velocity
        vel = sys_data.get('velocity', {})
        g_vel = g.get('velocity', {})
        if sys == 'ISW_NT_Si':
            # both electron and hole (same value 1.7442)
            for carrier in ['electron', 'hole']:
                gv = g_vel.get(carrier)
                av = vel.get(carrier)
                tol = 0.10 * abs(gv) if gv and gv != 0 else 0.01
                s = rel_check(av, gv, tol)
                score_sum += s
                n_total += 1
        else:
            for carrier in ['electron', 'hole']:
                gv = g_vel.get(carrier)
                av = vel.get(carrier)
                tol = 0.10 * abs(gv) if gv and gv != 0 else 0.01
                s = rel_check(av, gv, tol)
                score_sum += s
                n_total += 1
        # ef_minus_evbm, ecbm_minus_ef
        for field in ['ef_minus_evbm', 'ecbm_minus_ef']:
            gv = g.get(field)
            av = sys_data.get(field)
            tol = 0.10 * abs(gv) if gv and gv != 0 else 0.01
            s = rel_check(av, gv, tol)
            score_sum += s
            n_total += 1

    if n_total == 0:
        return 0.0
    return round(score_sum / n_total, 6)


# === block: score_3 (check id='structural_other') ===
def score_3(artifact, step, ctx):
    gold = ctx['gold']
    score_sum = 0.0
    n_total = 0

    systems = ['ISW_NT', 'BSW_NT', 'ISW_NT_C', 'ISW_NT_Si']

    def check_tuple(val, gold, tol_rel=None, tol_abs=None):
        if gold is None:
            return 1.0 if val is None else 0.0
        if val is None:
            return 0.0
        if tol_abs is not None:
            return 1.0 if abs(val - gold) <= tol_abs else 0.0
        if gold == 0.0:
            return 1.0 if abs(val) <= tol_rel else 0.0 if tol_rel else 0.0
        err = abs(val - gold) / abs(gold)
        return 1.0 if err <= tol_rel else 0.0

    for sys in systems:
        if sys not in artifact:
            continue
        sys_data = artifact[sys]
        g = gold.get(sys, {})
        if not g:
            continue
        # num_atoms (exact)
        g_na = g.get('num_atoms')
        a_na = sys_data.get('num_atoms')
        s = 1.0 if a_na == g_na else 0.0
        score_sum += s
        n_total += 1
        # tubular_diameter (2% rel)
        g_td = g.get('tubular_diameter')
        a_td = sys_data.get('tubular_diameter')
        s = check_tuple(a_td, g_td, tol_rel=0.02)
        score_sum += s
        n_total += 1
        # radial_buckling (abs 0.005)
        g_rb = g.get('radial_buckling')
        a_rb = sys_data.get('radial_buckling')
        s = check_tuple(a_rb, g_rb, tol_abs=0.005)
        score_sum += s
        n_total += 1
        # symmetry (exact 2)
        g_sym = g.get('symmetry')
        a_sym = sys_data.get('symmetry')
        s = 1.0 if a_sym == g_sym else 0.0
        score_sum += s
        n_total += 1

    if n_total == 0:
        return 0.0
    return round(score_sum / n_total, 6)


# === block: score_4 (check id='charges') ===
def score_4(artifact, step, ctx):
    gold = ctx['gold']
    score_sum = 0.0
    n_total = 0

    systems = ['ISW_NT', 'BSW_NT', 'ISW_NT_C', 'ISW_NT_Si']

    def rel_check(val, gold, tol):
        if gold is None:
            return 0.0 if val is not None else 1.0
        if val is None:
            return 0.0
        if gold == 0.0:
            return 1.0 if abs(val) <= tol else 0.0
        err = abs(val - gold) / abs(gold)
        return 1.0 if err <= tol else 0.0

    for sys in systems:
        if sys not in artifact:
            continue
        sys_data = artifact[sys]
        g = gold.get(sys, {})
        if not g:
            continue
        for field in ['charge_s_C', 'charge_s_Si', 'charge_p_C', 'charge_p_Si', 'total_charge']:
            gv = g.get(field)
            av = sys_data.get(field)
            tol = 0.01 * abs(gv) if gv and gv != 0 else 0.01
            s = rel_check(av, gv, tol)
            score_sum += s
            n_total += 1

    if n_total == 0:
        return 0.0
    return round(score_sum / n_total, 6)


# === block: score_5 (check id='trends') ===
def score_5(artifact, step, ctx):
    gold = ctx['gold']
    def get_val(sys, field):
        if sys not in artifact:
            return None
        return artifact[sys].get(field)

    def get_lat_c(sys):
        lat = get_val(sys, 'lattice_constants')
        if lat is None:
            return None
        return lat.get('c')

    checks = 0
    success = 0

    # 1. c ordering: ISW > C-vac > Si-vac
    c_isw = get_lat_c('ISW_NT')
    c_c = get_lat_c('ISW_NT_C')
    c_si = get_lat_c('ISW_NT_Si')
    if None not in (c_isw, c_c, c_si):
        checks += 1
        if c_isw > c_c > c_si:
            success += 1

    # 2. tubular diameter ordering: ISW > C-vac > Si-vac
    d_isw = get_val('ISW_NT', 'tubular_diameter')
    d_c = get_val('ISW_NT_C', 'tubular_diameter')
    d_si = get_val('ISW_NT_Si', 'tubular_diameter')
    if None not in (d_isw, d_c, d_si):
        checks += 1
        if d_isw > d_c > d_si:
            success += 1

    # 3. radial buckling ordering: ISW < BSW < C-vac < Si-vac
    rb_isw = get_val('ISW_NT', 'radial_buckling')
    rb_bsw = get_val('BSW_NT', 'radial_buckling')
    rb_c = get_val('ISW_NT_C', 'radial_buckling')
    rb_si = get_val('ISW_NT_Si', 'radial_buckling')
    if None not in (rb_isw, rb_bsw, rb_c, rb_si):
        checks += 1
        if rb_isw < rb_bsw < rb_c < rb_si:
            success += 1

    # 4. band gap hierarchy: ISW > BSW > C-vac (Si-vac metallic)
    bg_isw = get_val('ISW_NT', 'band_gap')
    bg_bsw = get_val('BSW_NT', 'band_gap')
    bg_c = get_val('ISW_NT_C', 'band_gap')
    bg_si = get_val('ISW_NT_Si', 'band_gap')
    if None not in (bg_isw, bg_bsw, bg_c):
        checks += 1
        if bg_isw > bg_bsw > bg_c:
            success += 1
    # metallic check: Si-vac gap None or < 0.1
    if bg_si is None or (isinstance(bg_si, (int,float)) and bg_si < 0.1):
        checks += 1
        success += 1

    if checks == 0:
        return 0.0
    return round(success / checks, 6)


_SCORERS = {
    'lattice': score_0,
    'bulk_moduli': score_1,
    'electronic': score_2,
    'structural_other': score_3,
    'charges': score_4,
    'trends': score_5,
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
