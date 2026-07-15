import os
import json
import csv

# === author imports / helpers ===
import math
import json


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


# === block: score_0 (check id='step_01_validate_energies') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    required_keys = ['separated_reactants', 'ts1_cycloaddition', 'intermediate_4a-Sn', 'ts2_insertion', 'product_2a-Sn']
    for k in required_keys:
        if k not in artifact:
            return 0.0
        fields = ['E_elec_hartree', 'G_corr_hartree', 'rel_E_elec_kcal', 'rel_G_kcal']
        if not isinstance(artifact[k], dict) or not all(f in artifact[k] for f in fields):
            return 0.0
    return 1.0


# === block: score_1 (check id='step_02_validate_geometries') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    lines = artifact.strip().splitlines()
    frames = []
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        n_atoms = int(lines[i].strip())
        label = lines[i+1].strip()
        frames.append((label, n_atoms))
        i += n_atoms + 2
    expected_labels = ['reactants', 'ts1_cycloaddition', 'intermediate', 'ts2_insertion', 'product']
    if len(frames) != 5:
        return 0.0
    for (l, n), exp in zip(frames, expected_labels):
        if not l.lower().startswith(exp.lower()):
            return 0.0
    return 1.0


# === block: score_2 (check id='step_03_energy_profile') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    cond = step.get('conditions', {})
    ordering_w = cond.get('part_ordering_weight', 0.4)
    barrier_w = cond.get('part_barrier_weight', 0.3)
    dg_w = cond.get('part_overall_dG_weight', 0.3)
    barrier_th = cond.get('barrier_threshold', 15.0)
    dg_target = cond.get('overall_dG_target', -5.8)
    dg_tol = cond.get('overall_dG_tolerance', 3.0)

    try:
        reac = artifact['separated_reactants']['rel_G_kcal']
        ts1  = artifact['ts1_cycloaddition']['rel_G_kcal']
        inter= artifact['intermediate_4a-Sn']['rel_G_kcal']
        ts2  = artifact['ts2_insertion']['rel_G_kcal']
        prod = artifact['product_2a-Sn']['rel_G_kcal']
    except (KeyError, TypeError):
        return 0.0

    order_ok = (ts1 > reac and ts1 > inter and ts2 > inter and ts2 > prod)
    bar_ok  = ( (ts1 - 0.0) < barrier_th and (ts2 - inter) < barrier_th )
    dg_diff = abs(prod - dg_target)
    dg_part = 1.0 if dg_diff <= dg_tol else max(0.0, 1.0 - (dg_diff - dg_tol) / dg_tol)
    score = (ordering_w * (1.0 if order_ok else 0.0) +
             barrier_w * (1.0 if bar_ok else 0.0) +
             dg_w * dg_part)
    return score


# === block: score_3 (check id='step_04_geom_bond_lengths') ===
def score_3(artifact, step, ctx):
    if artifact is None:
        return 0.0
    ref = step.get('reference_bonds', {})
    tol = step.get('tolerance_angstrom', 0.05)
    part_weights = step.get('part_weights', {})
    w_react = part_weights.get('reactants', 0.5)
    w_prod  = part_weights.get('product', 0.5)

    def parse_xyz(text):
        frames = []
        lines = text.strip().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            n = int(line)
            label = lines[i+1].strip()
            atoms = []
            for j in range(n):
                parts = lines[i+2+j].split()
                elem = parts[0]
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                atoms.append({'element': elem, 'x': x, 'y': y, 'z': z})
            frames.append({'label': label, 'n': n, 'atoms': atoms})
            i += n + 2
        return frames

    def distance(a1, a2):
        return math.sqrt((a1['x']-a2['x'])**2 + (a1['y']-a2['y'])**2 + (a1['z']-a2['z'])**2)

    frames = parse_xyz(artifact)
    if len(frames) != 5:
        return 0.0
    react_frame = frames[0]
    prod_frame  = frames[4]

    def bond_score(frame_atoms, target_bonds):
        ok = 0
        total = len(target_bonds)
        atoms_by_elem = {}
        for a in frame_atoms:
            atoms_by_elem.setdefault(a['element'], []).append(a)
        for (pair, ref_val) in target_bonds.items():
            e1, e2 = pair.split('-')
            best = None
            for a1 in atoms_by_elem.get(e1, []):
                for a2 in atoms_by_elem.get(e2, []):
                    if a1 is a2:
                        continue
                    d = distance(a1, a2)
                    if best is None or abs(d - ref_val) < abs(best - ref_val):
                        best = d
            if best is not None and abs(best - ref_val) <= tol:
                ok += 1
        return ok / total if total > 0 else 1.0

    if react_frame['label'].lower().startswith('reactants'):
        r_score = bond_score(react_frame['atoms'], ref.get('reactants', {}))
    else:
        r_score = 0.0
    if prod_frame['label'].lower().startswith('product'):
        p_score = bond_score(prod_frame['atoms'], ref.get('product', {}))
    else:
        p_score = 0.0
    return w_react * r_score + w_prod * p_score


_SCORERS = {
    'step_01_validate_energies': score_0,
    'step_02_validate_geometries': score_1,
    'step_03_energy_profile': score_2,
    'step_04_geom_bond_lengths': score_3,
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
