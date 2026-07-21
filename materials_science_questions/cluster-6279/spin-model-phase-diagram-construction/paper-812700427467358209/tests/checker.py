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
    gold = {}
    for step in spec.get('steps', []):
        gold[step['id']] = step.get('expected', step.get('expected_points', None))
    return gold


# === block: score_0 (check id='sd_fixed_points') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'self_dual_fixed_points' not in artifact:
        return 0.0
    pts = artifact['self_dual_fixed_points']
    expected = step.get('expected', [])
    tol_ratios = step.get('tolerance_ratios', 0.01)
    tol_eig = step.get('tolerance_eigenvalue', 0.05)
    tol_nu = step.get('tolerance_nu', 0.1)
    matches = 0.0
    for exp in expected:
        found = False
        for p in pts:
            if p.get('name', '') != exp['name']:
                continue
            ok = True
            for key in ['h1_over_lambda1','h2_over_lambda1','lambda2_over_lambda1']:
                if abs(p.get(key, 0.0) - exp[key]) > tol_ratios:
                    ok = False; break
            if abs(p.get('thermal_eigenvalue', 0.0) - exp['thermal_eigenvalue']) > tol_eig:
                ok = False
            if abs(p.get('nu', 0.0) - exp['nu']) > tol_nu:
                ok = False
            if ok:
                found = True; break
        if found:
            matches += 1.0
    return matches / max(1, len(expected))


# === block: score_1 (check id='block_fixed_points') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'block_fixed_points' not in artifact:
        return 0.0
    pts = artifact['block_fixed_points']
    expected = step.get('expected', [])
    tol_a = step.get('tolerance_a', 0.01)
    tol_b = step.get('tolerance_b', 0.01)
    tol_xy = step.get('tolerance_xy', 0.01)
    tol_nu = step.get('tolerance_nu', 0.1)
    tol_lt2 = step.get('tolerance_lambda_t2', 0.05)
    matches = 0.0
    for exp in expected:
        found = False
        for p in pts:
            if p.get('name', '') != exp['name'] or p.get('block_size') != exp['block_size']:
                continue
            ok = True
            if exp['name'] == 'Ising':
                if 'a' in exp and abs(p.get('a', 0.0) - exp['a']) > tol_a:
                    ok = False
            else:  # Potts
                if 'b' in exp and abs(p.get('b', 0.0) - exp['b']) > tol_b:
                    ok = False
                if 'x_equal_y' in exp and abs(p.get('x_equal_y', 0.0) - exp['x_equal_y']) > tol_xy:
                    ok = False
            if abs(p.get('nu', 0.0) - exp['nu']) > tol_nu:
                ok = False
            if abs(p.get('lambda_t2', 0.0) - exp['lambda_t2']) > tol_lt2:
                ok = False
            if ok:
                found = True; break
        if found:
            matches += 1.0
    return matches / max(1, len(expected))


# === block: score_2 (check id='phase_diag') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    potts_hit = False
    direct_hit = False
    three_phase_ok = False
    potts_tol = step.get('potts_tolerance_h1', 0.02)
    direct_tol = step.get('direct_transition_tolerance', 0.01)
    l_gate = step.get('three_phase_lambda2_gate', 1.05)
    # build mapping lambda2 -> list of (h1, region)
    from collections import defaultdict
    by_l2 = defaultdict(list)
    for r in artifact:
        try:
            l2 = float(r['lambda2_lambda1'])
            h1 = float(r['h1_lambda1_critical'])
            reg = r['phase_region'].strip()
            by_l2[l2].append((h1, reg))
        except:
            pass
    # Potts point
    for h1, reg in by_l2.get(1.0, []):
        if abs(h1 - 0.25) <= potts_tol and 'Potts' in reg:
            potts_hit = True; break
    # Direct transition PM-FO at lambda2=0.0
    for h1, reg in by_l2.get(0.0, []):
        if abs(h1 - 0.25) <= direct_tol and 'PM-FO' in reg:
            direct_hit = True; break
    # Three-phase region existence: lambda2 slightly above 1 should have both PM-PO and PO-FO rows
    entries = by_l2.get(l_gate, [])
    has_PM_PO = any('PM-PO' in r for _, r in entries)
    has_PO_FO = any('PO-FO' in r for _, r in entries)
    if has_PM_PO and has_PO_FO:
        three_phase_ok = True
    score = 0.0
    if potts_hit:
        score += 0.4
    if direct_hit:
        score += 0.3
    if three_phase_ok:
        score += 0.3
    return score


# === block: score_3 (check id='nu_line') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    expected_pts = step.get('expected_points', [])
    tol = step.get('tolerance_nu', 0.05)
    # build dict of nearest lambda2 -> nu
    from collections import defaultdict
    u_map = {}
    for r in artifact:
        try:
            l2 = float(r['lambda2_lambda1'])
            nu = float(r['nu'])
            u_map[l2] = nu
        except:
            pass
    if not u_map:
        return 0.0
    hits = 0.0
    for exp in expected_pts:
        target_l2 = exp['lambda2_lambda1']
        target_nu = exp['nu']
        # find closest lambda2 in u_map
        best_key = min(u_map.keys(), key=lambda k: abs(k - target_l2), default=None)
        if best_key is None:
            continue
        if abs(best_key - target_l2) > 0.02:  # must be near the requested point
            continue
        if abs(u_map[best_key] - target_nu) <= tol:
            hits += 1.0
    return hits / max(1, len(expected_pts))


_SCORERS = {
    'sd_fixed_points': score_0,
    'block_fixed_points': score_1,
    'phase_diag': score_2,
    'nu_line': score_3,
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
