import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import math
    class np:
        @staticmethod
        def mean(iterable):
            return sum(iterable) / len(iterable)
        @staticmethod
        def clip(a, a_min, a_max):
            return max(a_min, min(a_max, a))
        @staticmethod
        def isfinite(x):
            return math.isfinite(x)
import csv
import os


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
    rows = []
    csv_path = os.path.join(outputs_dir, "results_summary.csv")
    if os.path.exists(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]
    return {"rows": rows}


# === block: score_0 (check id='step03') ===
def score_0(artifact, step, ctx):
    def safe_float(v, default=0.0):
        try:
            return float(v)
        except:
            return default

    agent_rows = ctx["rows"]
    gold_rows = step["gold"]["rows"]
    tol = step["gold"]["tolerances"]

    # Build agent lookup by (composition, phase) using case-insensitive match
    agent_lookup = {}
    for r in agent_rows:
        comp = str(r.get("composition", "")).strip()
        phase = str(r.get("phase", "")).strip().lower()
        key = (comp, phase)
        agent_lookup[key] = {
            "a": safe_float(r.get("lattice_constant_a", 0)),
            "c": safe_float(r.get("lattice_constant_c", 0)),
            "B0": safe_float(r.get("bulk_modulus", 0)),
        }

    # Pairwise scoring
    def rel_score(agent_val, gold_val, tol_frac):
        if abs(gold_val) < 1e-12:
            # if gold is zero, allow small absolute error
            return 1.0 if abs(agent_val) <= 0.05 else 0.0
        relerr = abs(agent_val - gold_val) / abs(gold_val)
        if relerr <= tol_frac:
            return 1.0
        else:
            return max(0.0, 1.0 - (relerr - tol_frac) / tol_frac)

    pair_scores = []
    for g in gold_rows:
        comp = str(g["composition"]).strip()
        phase = str(g["phase"]).strip().lower()
        key = (comp, phase)
        if key not in agent_lookup:
            pair_scores.append(0.0)
            continue
        ag = agent_lookup[key]
        sa = rel_score(ag["a"], g["a"], tol["a"])
        sc_c = rel_score(ag["c"], g["c"], tol["c"]) if g["c"] > 1e-12 else (1.0 if abs(ag["c"]) < 0.05 else 0.0)
        sb = rel_score(ag["B0"], g["B0"], tol["B0"])
        pair_scores.append((sa + sc_c + sb) / 3.0)

    pair_score = np.mean(pair_scores) if pair_scores else 0.0

    # Structural trend check: for NaCl and wurtzite separately
    # Ensure lattice constant a increases with x, B0 decreases with x
    def check_trend(phase):
        rows_phase = []
        for r in agent_rows:
            if str(r.get("phase", "")).strip().lower() == phase:
                x = safe_float(r.get("composition", 0))
                a = safe_float(r.get("lattice_constant_a", 0))
                B = safe_float(r.get("bulk_modulus", 0))
                rows_phase.append((x, a, B))
        if not rows_phase:
            return 0.0
        rows_phase.sort(key=lambda t: t[0])
        a_vals = [t[1] for t in rows_phase]
        B_vals = [t[2] for t in rows_phase]
        a_ok = all(a_vals[i+1] >= a_vals[i] - 1e-3 for i in range(len(a_vals)-1))
        B_ok = all(B_vals[i+1] <= B_vals[i] + 1e-3 for i in range(len(B_vals)-1))
        return 1.0 if a_ok and B_ok else 0.0

    trend_nacl = check_trend("nacl")
    trend_wurtz = check_trend("wurtzite")
    trend_score = 0.5 * trend_nacl + 0.5 * trend_wurtz

    # Combine
    score = 0.9 * pair_score + 0.1 * trend_score
    return float(np.clip(score, 0.0, 1.0))


# === block: score_1 (check id='step04') ===
def score_1(artifact, step, ctx):
    agent_json = artifact   # already parsed dict
    rows = ctx["rows"]
    gold = step["gold"]
    tol_alpha = gold["tolerances"]["alpha"]
    tol_beta = gold["tolerances"]["beta"]

    def safe_float(v, default=0.0):
        try:
            return float(v)
        except:
            return default

    # Helper to compute bowing from rows for a given phase
    def compute_bowing(phase, comp_field='lattice_constant_a', mod_field='bulk_modulus'):
        # filter rows for phase
        ph_rows = []
        for r in rows:
            if str(r.get("phase", "")).strip().lower() == phase.lower():
                x = safe_float(r.get("composition", 0))
                a_val = safe_float(r.get(comp_field))
                b_val = safe_float(r.get(mod_field))
                ph_rows.append({"x": x, "a": a_val, "B": b_val})
        # Ensure we have x=0 and x=1
        x0 = next((r for r in ph_rows if abs(r['x'] - 0.0) < 0.001), None)
        x1 = next((r for r in ph_rows if abs(r['x'] - 1.0) < 0.001), None)
        if not x0 or not x1:
            return None  # cannot compute
        a0, a1 = x0['a'], x1['a']
        B0, B1 = x0['B'], x1['B']
        alpha_list = []
        beta_list = []
        for r in ph_rows:
            x = r['x']
            if 0.001 < x < 0.999:
                a_lin = x * a1 + (1 - x) * a0
                d_a = a_lin - r['a']
                denom = x * (1 - x)
                if abs(denom) > 1e-12:
                    alpha_list.append(d_a / denom)
                B_lin = x * B1 + (1 - x) * B0
                d_B = B_lin - r['B']
                beta_list.append(d_B / denom)
        if not alpha_list:
            return None
        alpha = np.mean(alpha_list)
        beta  = np.mean(beta_list)
        return {'alpha': float(alpha), 'beta': float(beta)}

    bowing_NaCl = compute_bowing('NaCl', comp_field='lattice_constant_a', mod_field='bulk_modulus')
    bowing_wurtz = compute_bowing('wurtzite', comp_field='lattice_constant_a', mod_field='bulk_modulus')

    # Score based on reported JSON vs gold, and recomputed vs gold
    def score_param(reported_val, recomputed_val, gold_val, tol_val, metric_weight=0.5):
        # reported vs gold
        if np.isfinite(gold_val):
            rel_err_rep = abs(reported_val - gold_val) / max(abs(gold_val), 1e-12)
            score_rep = 1.0 if rel_err_rep <= tol_val else max(0.0, 1.0 - (rel_err_rep - tol_val) / tol_val)
        else:
            score_rep = 0.0
        # recomputed vs gold
        if recomputed_val is not None and np.isfinite(gold_val):
            rel_err_rec = abs(recomputed_val - gold_val) / max(abs(gold_val), 1e-12)
            score_rec = 1.0 if rel_err_rec <= tol_val else max(0.0, 1.0 - (rel_err_rec - tol_val) / tol_val)
        else:
            score_rec = 0.0
        return 0.3 * score_rep + 0.7 * score_rec   # recomputed heavier

    score_total = 0.0
    count = 0

    for phase_key in ['NaCl', 'wurtzite']:
        reported = agent_json.get(phase_key, {})
        reported_alpha = safe_float(reported.get('alpha_lattice_bowing_parameter', 0))
        reported_beta  = safe_float(reported.get('beta_bulk_modulus_bowing_parameter', 0))
        gold_phase = gold.get(phase_key, {})
        gold_alpha = gold_phase.get('alpha')
        gold_beta  = gold_phase.get('beta')
        recomputed = bowing_NaCl if phase_key == 'NaCl' else bowing_wurtz
        rec_alpha = recomputed['alpha'] if recomputed else None
        rec_beta  = recomputed['beta'] if recomputed else None
    
        if gold_alpha is not None:
            score_total += score_param(reported_alpha, rec_alpha, gold_alpha, tol_alpha)
            count += 1
        if gold_beta is not None:
            score_total += score_param(reported_beta, rec_beta, gold_beta, tol_beta)
            count += 1

    if count == 0:
        return 0.0
    score = score_total / count
    return float(np.clip(score, 0.0, 1.0))


# === block: score_2 (check id='step05') ===
def score_2(artifact, step, ctx):
    agent_json = artifact
    rows = ctx["rows"]
    gold = step["gold"]

    def safe_float(v, default=0.0):
        try:
            return float(v)
        except:
            return default

    # Build list of (composition, phase, energy)
    energies = []
    for r in rows:
        x = safe_float(r.get("composition", 0))
        phase = str(r.get("phase", "")).strip().lower()
        e = safe_float(r.get("total_energy", 0))
        energies.append((x, phase, e))

    # Group by composition
    from collections import defaultdict
    by_x = defaultdict(dict)
    for x, phase, e in energies:
        by_x[x][phase] = e

    # Score pattern: for each x, NaCl ("nacl") should be lower energy (more negative) for x<0.5, wurtzite for x>=0.5
    pattern_ok = True
    for x, phases in by_x.items():
        if 'nacl' not in phases or 'wurtzite' not in phases:
            continue
        e_NaCl = phases['nacl']
        e_wurtz = phases['wurtzite']
        if x < 0.5:
            if e_NaCl > e_wurtz + 1e-3:
                pattern_ok = False
        else:
            if e_wurtz > e_NaCl + 1e-3:
                pattern_ok = False

    # If we have x=0.5, allow nearly degenerate energies (< 1.0 eV difference) to count as pattern OK
    # already handled by tolerance in inequalities

    score_pattern = 1.0 if pattern_ok else 0.0

    # Score reported crossover_x
    reported_x = safe_float(agent_json.get("crossover_x", -999))
    target_x = gold["crossover_x"]
    tol_x = gold["tolerance"]
    if abs(reported_x - target_x) <= tol_x:
        score_cross = 1.0
    else:
        score_cross = max(0.0, 1.0 - abs(reported_x - target_x) / tol_x)  # falloff

    # Score stable range strings (basic presence)
    str_a = str(agent_json.get("stable_NaCl_range", ""))
    str_b = str(agent_json.get("stable_wurtzite_range", ""))
    score_strings = 1.0 if (str_a and str_b) else 0.0

    score = 0.4 * score_pattern + 0.4 * score_cross + 0.2 * score_strings
    return float(np.clip(score, 0.0, 1.0))


_SCORERS = {
    'step03': score_0,
    'step04': score_1,
    'step05': score_2,
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
