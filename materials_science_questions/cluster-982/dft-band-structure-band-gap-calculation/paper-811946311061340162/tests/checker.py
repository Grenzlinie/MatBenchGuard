import os
import json
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


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step.get('target_values', {})
    tol = step.get('tolerance_bandgap_abs', 0.2)
    correct = 0
    # indirect gap
    ia = artifact.get('indirect_gap_eV')
    gi = gold.get('indirect_gap_eV')
    if ia is not None and gi is not None and abs(ia - gi) <= tol:
        correct += 1
    # direct gap
    da = artifact.get('direct_gap_Gamma_eV')
    gd = gold.get('direct_gap_Gamma_eV')
    if da is not None and gd is not None and abs(da - gd) <= tol:
        correct += 1
    # band_gap_type
    if artifact.get('band_gap_type') == gold.get('band_gap_type'):
        correct += 1
    return correct / 3.0


# === block: score_1 (check id='step_phonon') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    expected_rows = step.get('expected_rows', 25)
    if len(artifact) != expected_rows:
        return 0.0
    gold_table = step.get('gold_table', [])
    if len(gold_table) != expected_rows:
        return 0.0
    valid_sym = step.get('valid_symmetries', [])
    tol_to = step.get('tolerances', {}).get('TO_cm1', 8.0)
    tol_lo = step.get('tolerances', {}).get('LO_cm1', 12.0)
    tol_z = step.get('tolerances', {}).get('Z_star', 0.5)
    tol_eps_rel = step.get('tolerances', {}).get('epsilon_relative', 0.15)

    # Parse agent rows, filtering invalid ones
    agent_rows = []
    for row in artifact:
        try:
            to_val = float(row.get('TO_cm1'))
            lo_val = float(row.get('LO_cm1'))
            sym = str(row.get('symmetry', ''))
            z_val = float(row.get('Z_star'))
            eps_val = float(row.get('epsilon'))
        except (ValueError, TypeError):
            continue
        if sym not in valid_sym:
            continue
        agent_rows.append((to_val, lo_val, sym, z_val, eps_val))

    if len(agent_rows) != expected_rows:
        return 0.0

    # Build list of gold rows as tuples: (TO, LO, Z, eps, symmetry, index)
    gold_list = []
    for i, gold_row in enumerate(gold_table):
        g_to = float(gold_row.get('TO_cm1'))
        g_lo = float(gold_row.get('LO_cm1'))
        g_sym = str(gold_row.get('symmetry', ''))
        g_z = float(gold_row.get('Z_star'))
        g_eps = float(gold_row.get('epsilon'))
        gold_list.append((g_to, g_lo, g_sym, g_z, g_eps, i))

    # Pair each gold row with the best matching agent row by symmetry and minimal TO difference
    import math
    assigned_gold = set()
    assigned_agent = [False] * len(agent_rows)
    pairs = []
    for g_to, g_lo, g_sym, g_z, g_eps, g_idx in sorted(gold_list, key=lambda x: (x[2], x[0])):  # sort by sym,TO for reproducibility
        best = None
        best_dist = math.inf
        for a_idx, (a_to, a_lo, a_sym, a_z, a_eps) in enumerate(agent_rows):
            if a_sym != g_sym:
                continue
            if assigned_agent[a_idx]:
                continue
            dist = abs(a_to - g_to)
            if dist < best_dist:
                best_dist = dist
                best = (a_idx, a_to, a_lo, a_sym, a_z, a_eps)
        if best is not None:
            assigned_agent[best[0]] = True
            pairs.append((g_to, g_lo, g_sym, g_z, g_eps, best[1], best[2], best[3], best[4], best[5]))

    if len(pairs) != expected_rows:
        return 0.0

    correct_rows = 0
    for g_to, g_lo, g_sym, g_z, g_eps, a_to, a_lo, a_sym, a_z, a_eps in pairs:
        if a_sym != g_sym:
            continue
        if abs(a_to - g_to) > tol_to or abs(a_lo - g_lo) > tol_lo or abs(a_z - g_z) > tol_z:
            continue
        if g_eps != 0.0:
            eps_threshold = max(0.01, tol_eps_rel * abs(g_eps))
            if abs(a_eps - g_eps) <= eps_threshold:
                correct_rows += 1
        else:
            if abs(a_eps) <= tol_z:
                correct_rows += 1
    return correct_rows / expected_rows


# === block: score_2 (check id='step_dielectric') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step.get('gold_dielectric', {})
    tol_rel = step.get('tolerances_dielectric', {}).get('relative', 0.10)
    tol_abs = step.get('tolerances_dielectric', {}).get('absolute', 1.0)
    components = []
    for part in ['electronic', 'ionic', 'static']:
        gpart = gold.get(part, {})
        apart = artifact.get(part, {})
        if not isinstance(apart, dict):
            continue
        for key in ['xx', 'yy', 'zz', 'average']:
            gval = gpart.get(key)
            aval = apart.get(key)
            if gval is not None and aval is not None:
                try:
                    gval = float(gval)
                    aval = float(aval)
                except (ValueError, TypeError):
                    continue
                components.append((aval, gval))
    if len(components) == 0:
        return 0.0
    passed = 0
    for aval, gval in components:
        if aval == 0 and gval == 0:
            passed += 1
            continue
        diff = abs(aval - gval)
        threshold = max(tol_abs, tol_rel * abs(gval))
        if diff <= threshold:
            passed += 1
    return passed / len(components)


_SCORERS = {
    'step_bandgap': score_0,
    'step_phonon': score_1,
    'step_dielectric': score_2,
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
