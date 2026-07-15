import os
import json
import csv

# === author imports / helpers ===
import math
from typing import Any, Dict, List, Optional, Union


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


# === block: score_0 (check id='step_lattice') ===
def score_0(artifact, step, ctx):
    def score_numeric(value: float, target: float, tol: float) -> float:
        if target == 0:
            v = abs(value - target)
            if tol <= 0:
                return 0.0
            return max(0.0, 1.0 - v / tol)
        v = abs(value - target)
        return max(0.0, 1.0 - v / tol)

    lattice = artifact
    poly110 = lattice.get('pseudocubic_110', {})
    poly111 = lattice.get('pseudocubic_111', {})
    ortho  = lattice.get('orthorhombic', {})

    scores = []

    # pseudocubic_110 structural check: a,b,c not all equal and angles not all 90
    if poly110:
        a,b,c = poly110.get('a'), poly110.get('b'), poly110.get('c')
        alpha,beta,gamma = poly110.get('alpha'), poly110.get('beta'), poly110.get('gamma')
        if a is not None and b is not None and c is not None:
            # 0.1 Å difference required
            if max(abs(a-b), abs(b-c), abs(a-c)) >= 0.05:
                scores.append(1.0)
            else:
                scores.append(0.5)
        else:
            scores.append(0.0)
        if alpha is not None and beta is not None and gamma is not None:
            if abs(alpha-90)>1 or abs(beta-90)>1 or abs(gamma-90)>1:
                scores.append(1.0)
            else:
                scores.append(0.5)
        else:
            scores.append(0.0)
    else:
        scores.extend([0.0, 0.0])

    # pseudocubic_111: compare to paper gold
    step_gold = step.get('gold', {})
    g111 = step_gold.get('pseudocubic_111', {})
    tl = g111.get('tolerance_lattice', 0.1)
    ta = g111.get('tolerance_angle', 2.0)
    for key in ('a','b','c'):
        if poly111 and key in poly111 and key in g111:
            scores.append(score_numeric(float(poly111[key]), g111[key], tl))
        else:
            scores.append(0.0)
    for key in ('alpha','beta','gamma'):
        if poly111 and key in poly111 and key in g111:
            scores.append(score_numeric(float(poly111[key]), g111[key], ta))
        else:
            scores.append(0.0)
    # volume consistency: recompute from a,b,c and angles and compare to reported volume
    if poly111 and all(k in poly111 for k in ('a','b','c','alpha','beta','gamma','volume')):
        a = float(poly111['a']); b = float(poly111['b']); c = float(poly111['c'])
        al = math.radians(float(poly111['alpha'])); be = math.radians(float(poly111['beta'])); ga = math.radians(float(poly111['gamma']))
        V_calc = a*b*c*math.sqrt(1 - math.cos(al)**2 - math.cos(be)**2 - math.cos(ga)**2 + 2*math.cos(al)*math.cos(be)*math.cos(ga))
        diff = abs(V_calc - float(poly111['volume']))
        if V_calc > 0:
            scores.append(max(0.0, 1.0 - diff/(0.05*V_calc)))
        else:
            scores.append(0.0)
    else:
        scores.append(0.0)

    # orthorhombic structural: angles must be 90±2°, a,b,c not all equal
    if ortho:
        a,b,c = ortho.get('a'), ortho.get('b'), ortho.get('c')
        alpha = ortho.get('alpha'); beta = ortho.get('beta'); gamma = ortho.get('gamma')
        angle_score = 0.0
        if alpha is not None and beta is not None and gamma is not None:
            if all(abs(v-90) <= 2.0 for v in (float(alpha), float(beta), float(gamma))):
                angle_score = 1.0
            else:
                angle_score = 0.0
        else:
            angle_score = 0.0
        dim_score = 0.0
        if a is not None and b is not None and c is not None:
            if max(abs(float(a)-float(b)), abs(float(b)-float(c)), abs(float(a)-float(c))) >= 0.05:
                dim_score = 1.0
            else:
                dim_score = 0.0
        scores.append(angle_score)
        scores.append(dim_score)
        # volume positive
        if 'volume' in ortho and ortho['volume'] is not None and float(ortho['volume']) > 0:
            scores.append(1.0)
        else:
            scores.append(0.0)
    else:
        scores.extend([0.0, 0.0, 0.0])

    # average over sub-checks
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_bandgaps') ===
def score_1(artifact, step, ctx):
    def score_numeric(value: float, target: float, tol: float) -> float:
        v = abs(value - target)
        if tol <= 0:
            return 0.0 if v > 1e-12 else 1.0
        return max(0.0, 1.0 - v / tol)

    bg = artifact
    step_gold = step.get('gold', {})
    tol_Eg = step.get('tolerances', {}).get('Eg', 0.2)
    tol_Rashba_E = step.get('tolerances', {}).get('Rashba_energy', 0.005)
    tol_k0 = step.get('tolerances', {}).get('k0', 0.01)

    all_scores = []
    for poly_name in ('pseudocubic_110', 'pseudocubic_111', 'orthorhombic'):
        poly = bg.get(poly_name, {})
        gold_poly = step_gold.get(poly_name, {})
        if not isinstance(poly, dict) or not isinstance(gold_poly, dict):
            all_scores.append(0.0)
            continue
        # bandgap energies
        for soc_tag in ('nonSOC', 'SOC'):
            key_Eg = f'Eg_{soc_tag}'
            key_nat = f'nature_{soc_tag}'
            if key_Eg in poly and key_Eg in gold_poly:
                all_scores.append(score_numeric(float(poly[key_Eg]), float(gold_poly[key_Eg]), tol_Eg))
            else:
                all_scores.append(0.0)
            # nature: exact string match
            if key_nat in poly and key_nat in gold_poly:
                all_scores.append(1.0 if str(poly[key_nat]).strip().lower() == str(gold_poly[key_nat]).strip().lower() else 0.0)
            else:
                all_scores.append(0.0)
        # Rashba parameters
        for field in ('Rashba_CB_splitting', 'Rashba_VB_splitting', 'k0_CB', 'k0_VB'):
            val = poly.get(field)
            gold_val = gold_poly.get(field)
            # orthorhombic must be null
            if poly_name == 'orthorhombic':
                all_scores.append(1.0 if val is None else 0.0)
                continue
            if val is None or gold_val is None:
                all_scores.append(0.0)
                continue
            if field in ('k0_CB', 'k0_VB'):
                all_scores.append(score_numeric(float(val), float(gold_val), tol_k0))
            else:
                # energy in eV
                all_scores.append(score_numeric(float(val), float(gold_val), tol_Rashba_E))

    if not all_scores:
        return 0.0
    return sum(all_scores) / len(all_scores)


# === block: score_2 (check id='step_masses') ===
def score_2(artifact, step, ctx):
    def score_numeric(value: float, target: float, tol: float) -> float:
        v = abs(value - target)
        if tol <= 0:
            return 0.0 if v > 1e-12 else 1.0
        return max(0.0, 1.0 - v / tol)

    masses = artifact
    step_gold = step.get('gold', {})
    tol = step.get('tolerance_mass', 0.1)

    all_scores = []
    for poly_name in ('pseudocubic_110', 'pseudocubic_111', 'orthorhombic'):
        p = masses.get(poly_name, {})
        g = step_gold.get(poly_name, {})
        if not isinstance(p, dict) or not isinstance(g, dict):
            all_scores.append(0.0)
            continue
        for key in ('mh_star_nonSOC', 'me_star_nonSOC', 'mh_star_SOC', 'me_star_SOC'):
            if key in p and key in g:
                all_scores.append(score_numeric(float(p[key]), float(g[key]), tol))
            else:
                all_scores.append(0.0)

    if not all_scores:
        return 0.0
    return sum(all_scores) / len(all_scores)


# === block: score_3 (check id='step_binding') ===
def score_3(artifact, step, ctx):
    def score_numeric(value: float, target: float, tol: float) -> float:
        v = abs(value - target)
        if tol <= 0:
            return 0.0 if v > 1e-12 else 1.0
        return max(0.0, 1.0 - v / tol)

    bindings = artifact
    if not isinstance(bindings, list):
        return 0.0
    step_gold = step.get('gold', {})
    expected = step_gold.get('expected_blocks', [])
    tol_kcal = step_gold.get('tolerance_kcal', 10.0)
    tol_ev_conv = step_gold.get('tolerance_eV_conversion', 0.001)

    # map expected by (system, block_label)
    exp_map = {}
    for blk in expected:
        exp_map[(blk['system'], blk['block_label'])] = blk

    scores = []
    found_keys = set()
    for entry in bindings:
        if not isinstance(entry, dict):
            continue
        sys = entry.get('system')
        lbl = entry.get('block_label')
        kcal = entry.get('ΔE_BSSE_kcal_per_mol')
        ev   = entry.get('ΔE_BSSE_eV')
        if sys is None or lbl is None:
            continue
        key = (sys, lbl)
        found_keys.add(key)
        if key not in exp_map:
            scores.append(0.0)
            continue
        gold_blk = exp_map[key]
        # compare kcal
        if isinstance(kcal, (int, float)) and 'ΔE_BSSE_kcal_per_mol' in gold_blk:
            scores.append(score_numeric(float(kcal), gold_blk['ΔE_BSSE_kcal_per_mol'], tol_kcal))
        else:
            scores.append(0.0)
        # cross-check eV vs kcal conversion
        if isinstance(kcal, (int, float)) and isinstance(ev, (int, float)) and abs(float(kcal)) > 1e-12:
            expected_ev = float(kcal) / 23.060548
            scores.append(score_numeric(float(ev), expected_ev, tol_ev_conv))
        else:
            scores.append(0.0)

    # penalise missing expected blocks
    for key in exp_map:
        if key not in found_keys:
            scores.append(0.0)
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_lattice': score_0,
    'step_bandgaps': score_1,
    'step_masses': score_2,
    'step_binding': score_3,
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
