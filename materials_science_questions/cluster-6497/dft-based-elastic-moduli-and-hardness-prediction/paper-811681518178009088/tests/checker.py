import os
import json
import csv

# === author imports / helpers ===
import re, math, os


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


# === block: score_0 (check id='check_cif_structure') ===
def score_0(artifact, step, ctx):
    text = artifact
    params = step.get('params', {})
    a_target = params.get('a_target')
    a_tol = params.get('a_tol', 0.02)
    c_target = params.get('c_target')
    c_tol = params.get('c_tol', 0.02)
    sg_target = params.get('space_group_target', 'R-3m')
    nn_target = params.get('nn_dist_target')
    nn_tol = params.get('nn_dist_tol', 0.02)

    def extract_cell_float(pattern, text, group=1):
        m = re.search(pattern, text, re.IGNORECASE)
        if not m:
            return None
        try:
            return float(m.group(group))
        except:
            return None

    a = extract_cell_float(r'_cell_length_a\s+([\d.]+)', text)
    b = extract_cell_float(r'_cell_length_b\s+([\d.]+)', text)
    c = extract_cell_float(r'_cell_length_c\s+([\d.]+)', text)
    alpha = extract_cell_float(r'_cell_angle_alpha\s+([\d.]+)', text)
    beta  = extract_cell_float(r'_cell_angle_beta\s+([\d.]+)', text)
    gamma = extract_cell_float(r'_cell_angle_gamma\s+([\d.]+)', text)

    sg_match = re.search(r"_symmetry_space_group_name_H-M\s+'?([^']+)'?", text, re.IGNORECASE)
    sg = sg_match.group(1).strip() if sg_match else None

    def normalize_sg(s):
        # remove all non-alphanumeric (spaces, hyphens, underscores, etc.) and lower
        return re.sub(r'[^a-zA-Z0-9]+', '', s).lower()

    sg_norm = normalize_sg(sg) if sg is not None else None
    target_norm = normalize_sg(sg_target)

    # Parse atom site loop (fractional coordinates)
    atom_sites = []
    loop_match = re.search(r'loop_\s*((?:\s*_atom_site_[^\n]+\n)+)', text, re.IGNORECASE)
    if loop_match:
        header = loop_match.group(1)
        col_names = [h.strip() for h in re.findall(r'_atom_site_[^\s]+', header)]
        labels_idx = None
        x_idx = None
        y_idx = None
        z_idx = None
        for i, name in enumerate(col_names):
            if name == '_atom_site_label':
                labels_idx = i
            elif name == '_atom_site_fract_x':
                x_idx = i
            elif name == '_atom_site_fract_y':
                y_idx = i
            elif name == '_atom_site_fract_z':
                z_idx = i
        if x_idx is not None and y_idx is not None and z_idx is not None:
            data_start = text.find(header, loop_match.end()) + len(header)
            lines = text[data_start:].splitlines()
            for line in lines:
                stripped = line.strip()
                if not stripped or stripped.startswith('_') or stripped.startswith('loop_'):
                    continue
                parts = line.split()
                if len(parts) >= len(col_names):
                    try:
                        label = parts[labels_idx] if labels_idx is not None else ''
                        x = float(parts[x_idx])
                        y = float(parts[y_idx])
                        z = float(parts[z_idx])
                        atom_sites.append((label, x, y, z))
                    except (ValueError, IndexError):
                        continue

    def fractional_to_cartesian(x, y, z, a, b, c, alpha, beta, gamma):
        from math import cos, sin, sqrt, radians
        alpha = radians(alpha)
        beta  = radians(beta)
        gamma = radians(gamma)
        cos_al = cos(alpha)
        cos_be = cos(beta)
        cos_ga = cos(gamma)
        sin_ga = sin(gamma)
        v_unit = sqrt(1.0 - cos_al*cos_al - cos_be*cos_be - cos_ga*cos_ga + 2.0*cos_al*cos_be*cos_ga)
        tx = a * x + b * cos_ga * y + c * cos_be * z
        ty = (b * sin_ga) * y + c * (cos_al - cos_be*cos_ga) / sin_ga * z
        tz = (c * v_unit / sin_ga) * z
        return tx, ty, tz

    nn_dist = None
    if a and b and c and alpha is not None and beta is not None and gamma is not None:
        n_sites = [site for site in atom_sites if 'n' in site[0].lower()]
        if len(n_sites) >= 2:
            xyz1 = fractional_to_cartesian(n_sites[0][1], n_sites[0][2], n_sites[0][3], a, b, c, alpha, beta, gamma)
            xyz2 = fractional_to_cartesian(n_sites[1][1], n_sites[1][2], n_sites[1][3], a, b, c, alpha, beta, gamma)
            nn_dist = math.sqrt((xyz1[0]-xyz2[0])**2 + (xyz1[1]-xyz2[1])**2 + (xyz1[2]-xyz2[2])**2)

    scores = []

    # a parameter
    if a is not None:
        scores.append(1.0 if abs(a - a_target) <= a_tol else 0.0)
    else:
        scores.append(0.0)

    # c parameter
    if c is not None:
        scores.append(1.0 if abs(c - c_target) <= c_tol else 0.0)
    else:
        scores.append(0.0)

    # space group
    if sg_norm is not None:
        scores.append(1.0 if sg_norm == target_norm else 0.0)
    else:
        scores.append(0.0)

    # N–N distance
    if nn_dist is not None and nn_target is not None:
        scores.append(1.0 if abs(nn_dist - nn_target) <= nn_tol else 0.0)
    else:
        scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='check_properties_json') ===
def score_1(artifact, step, ctx):
    import json
    params = step.get('params', {})
    fields = params.get('fields', {})
    cross_check = params.get('cross_check_cif', False)

    def load_cif():
        cif_path = '/app/outputs/relaxed_structure.cif'
        if not os.path.exists(cif_path):
            return None
        with open(cif_path, 'r') as f:
            return f.read()

    def extract_cif_values(cif_text):
        a = None
        c = None
        a_match = re.search(r'_cell_length_a\s+(\S+)', cif_text)
        c_match = re.search(r'_cell_length_c\s+(\S+)', cif_text)
        if a_match:
            try:
                a = float(a_match.group(1))
            except:
                pass
        if c_match:
            try:
                c = float(c_match.group(1))
            except:
                pass
        # compute N-N distance as before
        n_sites_z = []
        loop_match = re.search(r'loop_\s*((?:\s*_atom_site_[^\n]+\n)+)', cif_text, re.IGNORECASE)
        if loop_match and c:
            header = loop_match.group(1)
            headers = [h.strip() for h in re.findall(r'_atom_site_[^\s]+', header)]
            data_start = cif_text.find(header, loop_match.end())
            lines = cif_text[data_start + len(header):].splitlines()
            for line in lines:
                if not line.strip() or line.startswith('_') or line.startswith('loop_'):
                    continue
                parts = line.split()
                if len(parts) >= len(headers):
                    site = {}
                    for i, h in enumerate(headers):
                        val = parts[i]
                        try:
                            val = float(val)
                        except ValueError:
                            pass
                        site[h] = val
                    if '_atom_site_fract_z' in site and ('N' in str(site.get('_atom_site_label','')) or 'n' in str(site.get('_atom_site_label',''))):
                        n_sites_z.append(site['_atom_site_fract_z'])
        nn_dist = None
        if len(n_sites_z) == 2:
            nn_dist = c * abs(n_sites_z[0] - n_sites_z[1])
        return a, c, nn_dist

    cif_text = None
    if cross_check:
        cif_text = load_cif()
        if cif_text is None:
            # cannot cross-check; proceed without
            cif_text = None
        else:
            a_cif, c_cif, nn_cif = extract_cif_values(cif_text)
    else:
        a_cif = c_cif = nn_cif = None

    score_parts = []
    for key, spec in fields.items():
        if key not in artifact:
            score_parts.append(0.0)
            continue
        val = artifact[key]
        target = spec.get('target')
        tol = spec.get('tol')
        if tol is not None:
            # numeric exact_match with tolerance
            try:
                if abs(float(val) - float(target)) <= tol:
                    score_parts.append(1.0)
                else:
                    score_parts.append(0.0)
            except:
                score_parts.append(0.0)
        else:
            # string exact match
            if str(val).strip().lower() == str(target).strip().lower():
                score_parts.append(1.0)
            else:
                score_parts.append(0.0)

    # cross-check against CIF
    if cross_check and cif_text is not None:
        if a_cif is not None and 'lattice_a_A' in artifact:
            try:
                if abs(float(artifact['lattice_a_A']) - a_cif) <= 1e-6:
                    pass  # consistent
                else:
                    score_parts.append(0.0)  # penalize inconsistency
            except:
                pass
        if c_cif is not None and 'lattice_c_A' in artifact:
            try:
                if abs(float(artifact['lattice_c_A']) - c_cif) <= 1e-6:
                    pass
                else:
                    score_parts.append(0.0)
            except:
                pass
        if nn_cif is not None and 'N_N_bond_length_A' in artifact:
            try:
                if abs(float(artifact['N_N_bond_length_A']) - nn_cif) <= 1e-6:
                    pass
                else:
                    score_parts.append(0.0)
            except:
                pass

    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


# === block: score_2 (check id='check_transition_pressure_csv') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    target_pressure = params.get('target_pressure', 17.0)
    tolerance = params.get('tolerance', 4.0)
    if not artifact or len(artifact) < 2:
        return 0.0
    pressures = []
    deltaGs = []
    for row in artifact:
        try:
            p = float(row.get('pressure_GPa', 0.0))
            dg = float(row.get('deltaG_kJ_mol', 0.0))
            pressures.append(p)
            deltaGs.append(dg)
        except:
            return 0.0
    # find sign change
    cross_pressure = None
    for i in range(len(pressures)-1):
        if deltaGs[i] * deltaGs[i+1] <= 0:
            # linear interpolation
            p1, p2 = pressures[i], pressures[i+1]
            dg1, dg2 = deltaGs[i], deltaGs[i+1]
            if abs(dg2 - dg1) < 1e-12:
                cross_pressure = (p1 + p2) / 2.0
            else:
                cross_pressure = p1 - dg1 * (p2 - p1) / (dg2 - dg1)
            break
    if cross_pressure is None:
        return 0.0
    # score: 1 within tolerance, else 0
    return 1.0 if abs(cross_pressure - target_pressure) <= tolerance else 0.0


_SCORERS = {
    'check_cif_structure': score_0,
    'check_properties_json': score_1,
    'check_transition_pressure_csv': score_2,
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
