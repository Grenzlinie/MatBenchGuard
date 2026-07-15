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
    ctx = {}
    for step in spec['steps']:
        if step['id'] == 'check_binding_energies':
            ctx['gold_binding'] = {g['n']: g['binding_energy'] for g in step['gold_values']}
            ctx['tol_binding'] = step['tolerance']
            ctx['gold_pentamer'] = step['pentamer_diff_gold']
            ctx['tol_pentamer'] = step['tolerance_pentamer']
    return ctx


# === block: score_0 (check id='check_binding_energies') ===
def score_0(artifact, step, ctx):
    import math
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    gold = ctx['gold_binding']
    tol = ctx['tol_binding']
    gold_pent = ctx['gold_pentamer']
    tol_pent = ctx['tol_pentamer']
    entries = data.get('binding_energies')
    if not isinstance(entries, list):
        return 0.0
    by_n = {}
    for e in entries:
        if isinstance(e, dict) and 'n' in e and 'binding_energy_per_molecule' in e:
            by_n[e['n']] = e['binding_energy_per_molecule']
    total_score = 0.0
    n_items = 0
    for n, gv in gold.items():
        val = by_n.get(n)
        if val is None:
            sub = 0.0
        else:
            diff = abs(val - gv)
            if diff <= tol:
                sub = 1.0
            else:
                sub = max(0.0, 1.0 - (diff - tol) / (2 * tol))
        total_score += sub
        n_items += 1
    # pentamer energy difference
    pent_val = data.get('pentamer_orthogonal_energy_difference')
    if pent_val is None:
        p_sub = 0.0
    else:
        diff = abs(pent_val - gold_pent)
        if diff <= tol_pent:
            p_sub = 1.0
        else:
            p_sub = max(0.0, 1.0 - (diff - tol_pent) / (2 * tol_pent))
    total_score += p_sub
    n_items += 1
    return total_score / n_items if n_items > 0 else 0.0


# === block: score_1 (check id='check_tetramer') ===
def score_1(artifact, step, ctx):
    def point_in_polygon(px, py, poly):
        # poly: list of (x,y) in order
        n = len(poly)
        inside = False
        j = n - 1
        for i in range(n):
            xi, yi = poly[i]
            xj, yj = poly[j]
            if ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
                inside = not inside
            j = i
        return inside

    lines = artifact.strip().splitlines()
    if len(lines) < 3:
        return 0.0
    atoms = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4:
            continue
        elem = parts[0]
        try:
            x = float(parts[1])
            y = float(parts[2])
            z = float(parts[3])
        except ValueError:
            continue
        atoms.append((elem, x, y, z))
    ca_positions = [(x,y,z) for (e,x,y,z) in atoms if e == 'Ca']
    o_positions = [(x,y,z) for (e,x,y,z) in atoms if e == 'O']
    h_positions = [(x,y,z) for (e,x,y,z) in atoms if e == 'H']
    if not ca_positions or not o_positions:
        return 0.0
    # Identify hydroxyl groups: surface O with a nearby H (distance < 1.5 Å)
    hydroxyls = []
    for ox, oy, oz in o_positions:
        # surface oxygens have z around 0 (tolerance ±1.0? we use abs(z) < 1.0)
        if abs(oz) > 1.0:
            continue
        for hx, hy, hz in h_positions:
            dist = ((ox-hx)**2 + (oy-hy)**2 + (oz-hz)**2)**0.5
            if dist < 1.5:
                hydroxyls.append((ox, oy, oz))
                break
    if len(hydroxyls) < 2:
        return 0.0
    # Find Ca squares: look for four Ca forming a square with side ~3.4 Å
    target = 3.4
    tol_side = 0.5
    ca_pairs = []
    n_ca = len(ca_positions)
    for i in range(n_ca):
        for j in range(i+1, n_ca):
            xi, yi, zi = ca_positions[i]
            xj, yj, zj = ca_positions[j]
            if abs(zi - zj) > 0.5:
                continue
            d = ((xi-xj)**2 + (yi-yj)**2)**0.5
            if abs(d - target) <= tol_side:
                ca_pairs.append((i, j, d))
    # For simplicity, we'll look for squares among a regular grid by rounding coordinates
    grid = {}
    for idx, (x, y, z) in enumerate(ca_positions):
        gx = round(x / target)
        gy = round(y / target)
        grid.setdefault((gx, gy), []).append(idx)
    # Find a 2x2 block that forms a square
    found_inside = False
    found_outside = False
    for (gx, gy), ids in grid.items():
        # check if there are Ca at (gx,gy), (gx+1,gy), (gx,gy+1), (gx+1,gy+1)
        needed = [(gx, gy), (gx+1, gy), (gx, gy+1), (gx+1, gy+1)]
        if all(g in grid for g in needed):
            # get actual coordinates
            sq_indices = []
            for g in needed:
                sq_indices.extend(grid[g])
            if len(sq_indices) < 4:
                continue
            # Get the four points by taking any representative
            pts = [ca_positions[i] for i in sq_indices[:4]]
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            poly = list(zip(xs, ys))
            inside_count = 0
            outside_count = 0
            for hx, hy, hz in hydroxyls:
                if point_in_polygon(hx, hy, poly):
                    inside_count += 1
                    # once found, we don't need to check more
                    found_inside = True
                else:
                    outside_count += 1
                    found_outside = True
            if found_inside and found_outside:
                return 1.0
    return 0.0


_SCORERS = {
    'check_binding_energies': score_0,
    'check_tetramer': score_1,
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
