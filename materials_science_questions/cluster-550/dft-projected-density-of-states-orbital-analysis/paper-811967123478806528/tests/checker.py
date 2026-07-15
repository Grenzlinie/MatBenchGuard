import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math

def compute_energy_gap(dos_rows):
    """Return VBM-CBM gap from list of dicts with 'Energy' and 'DOS' keys."""
    energies = []
    dos = []
    for row in dos_rows:
        energies.append(float(row['Energy']))
        dos.append(float(row.get('DOS', 0.0)))
    threshold = 1e-3
    max_v = None
    min_c = None
    for e, d in zip(energies, dos):
        if d >= threshold:
            if e < 0:
                if max_v is None or e > max_v:
                    max_v = e
            else:
                if min_c is None or e < min_c:
                    min_c = e
    if max_v is None or min_c is None:
        return None
    return min_c - max_v

def compute_optical_gap(alpha_rows):
    """Return Tauc optical gap from absorption CSV (Energy,alpha)."""
    energies = []
    alpha = []
    for row in alpha_rows:
        energies.append(float(row['Energy']))
        alpha.append(float(row.get('alpha', row.get('absorption', 0.0))))
    aE2 = [(a * e) ** 2 for a, e in zip(alpha, energies)]
    max_val = max(aE2)
    thresh = 0.01 * max_val
    onset = None
    for i, val in enumerate(aE2):
        if val >= thresh and energies[i] > 1.0:
            onset = i
            break
    if onset is None:
        return None
    end = min(onset + 10, len(energies))
    if end - onset < 3:
        return None
    x = energies[onset:end]
    y = aE2[onset:end]
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_xx = sum(xi * xi for xi in x)
    denom = n * sum_xx - sum_x * sum_x
    if abs(denom) < 1e-12:
        return None
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    if slope == 0:
        return None
    return -intercept / slope

def compute_average_ti_o_ti_angle(atom_list):
    """Estimate average Ti-O-Ti bond angle from list of {'element': 'X', 'position': [x,y,z]}. Returns degrees."""
    cutoff = 2.3  # Å
    atoms = [a for a in atom_list if 'position' in a]
    ti_pos = [a['position'] for a in atoms if a.get('element') == 'Ti']
    o_pos = [a['position'] for a in atoms if a.get('element') == 'O']
    if not ti_pos or not o_pos:
        return None
    angles = []
    for op in o_pos:
        # find two nearest Ti atoms
        dists = []
        for tp in ti_pos:
            d = math.sqrt(sum((a - b) ** 2 for a, b in zip(op, tp)))
            if d <= cutoff:
                dists.append((d, tp))
        if len(dists) >= 2:
            # take two closest
            dists.sort(key=lambda x: x[0])
            ti1 = dists[0][1]
            ti2 = dists[1][1]
            v1 = [ti1[i] - op[i] for i in range(3)]
            v2 = [ti2[i] - op[i] for i in range(3)]
            dot = sum(v1[i] * v2[i] for i in range(3))
            norm1 = math.sqrt(sum(v1[i]*v1[i] for i in range(3)))
            norm2 = math.sqrt(sum(v2[i]*v2[i] for i in range(3)))
            if norm1 * norm2 == 0:
                continue
            cosang = dot / (norm1 * norm2)
            cosang = max(-1.0, min(1.0, cosang))
            angles.append(math.degrees(math.acos(cosang)))
    if not angles:
        return None
    return sum(angles) / len(angles)


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
    def prepare(outputs_dir, spec):
        ctx = {}
        base = outputs_dir
        # load DOS CSVs
        dos_files = {
            'none': 'dos_none.csv',
            'Sc': 'dos_Sc.csv',
            'Y': 'dos_Y.csv',
            'La': 'dos_La.csv',
            'Sb': 'dos_Sb.csv',
            'Bi': 'dos_Bi.csv',
        }
        ctx['dos'] = {}
        for d, f in dos_files.items():
            p = os.path.join(base, f)
            if os.path.exists(p):
                ctx['dos'][d] = list(csv.DictReader(open(p, newline='')))
            else:
                ctx['dos'][d] = None
        # load absorption CSVs
        abs_files = {
            'none': 'absorption_none.csv',
            'Sc': 'absorption_Sc.csv',
            'Y': 'absorption_Y.csv',
            'La': 'absorption_La.csv',
            'Sb': 'absorption_Sb.csv',
            'Bi': 'absorption_Bi.csv',
        }
        ctx['absorption'] = {}
        for d, f in abs_files.items():
            p = os.path.join(base, f)
            if os.path.exists(p):
                ctx['absorption'][d] = list(csv.DictReader(open(p, newline='')))
            else:
                ctx['absorption'][d] = None
        # relaxed structures
        struct_path = os.path.join(base, 'relaxed_structures.json')
        if os.path.exists(struct_path):
            ctx['structures'] = json.load(open(struct_path))
        else:
            ctx['structures'] = None
        # vacancy total energies
        vac_path = os.path.join(base, 'vacancy_total_energies.json')
        if os.path.exists(vac_path):
            ctx['vacancy'] = json.load(open(vac_path))
        else:
            ctx['vacancy'] = None
        # mu_O
        mu_path = os.path.join(base, 'mu_O.json')
        if os.path.exists(mu_path):
            ctx['mu_O'] = json.load(open(mu_path)).get('mu_O', None)
        else:
            ctx['mu_O'] = None
        return ctx


# === block: score_0 (check id='undoped_energy_gap') ===
def score_0(artifact, step, ctx):
    dos = ctx['dos'].get('none')
    if not dos:
        return 0.0
    gap = compute_energy_gap(dos)
    if gap is None:
        return 0.0
    gold = step.get('gold_value')
    tol = step.get('tolerance', 0.2)
    if abs(gap - gold) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='undoped_optical_gap') ===
def score_1(artifact, step, ctx):
    abs_data = ctx['absorption'].get('none')
    if not abs_data:
        return 0.0
    gap = compute_optical_gap(abs_data)
    if gap is None:
        return 0.0
    gold = step.get('gold_value')
    tol = step.get('tolerance', 0.2)
    if abs(gap - gold) <= tol:
        return 1.0
    return 0.0


# === block: score_2 (check id='bond_angles_all') ===
def score_2(artifact, step, ctx):
    structs = ctx.get('structures')
    if not structs:
        return 0.0
    gold_vals = step.get('gold_values', {})
    tol = step.get('tolerance', 1.0)
    scores = []
    # structs assumed to be dict: {"systems": [{"dopant": "...", "atoms": [...]}, ...]}
    systems = structs.get('systems', [structs]) if isinstance(structs, dict) else structs
    if not isinstance(systems, list):
        return 0.0
    for sys in systems:
        dop = sys.get('dopant', sys.get('name', ''))
        atoms = sys.get('atoms', sys.get('positions', []))
        if not isinstance(atoms, list) or not atoms:
            continue
        angle = compute_average_ti_o_ti_angle(atoms)
        if angle is None or dop not in gold_vals:
            continue
        if abs(angle - gold_vals[dop]) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    # store for trend checks
    ctx['_bond_angles'] = {dop: compute_average_ti_o_ti_angle(sys.get('atoms')) for sys in systems for dop in [sys.get('dopant')]}
    return sum(scores) / len(scores)


# === block: score_3 (check id='formation_energies_all') ===
def score_3(artifact, step, ctx):
    vac = ctx.get('vacancy')
    mu = ctx.get('mu_O')
    if not vac or mu is None:
        return 0.0
    gold_vals = step.get('gold_values', {})
    tol = step.get('tolerance', 0.1)
    # expect vac: {"systems": [{"dopant": "...", "E_perfect": ..., "E_defect": ...}, ...]}
    systems = vac.get('systems', [])
    scores = []
    for sys in systems:
        dop = sys.get('dopant')
        E_perf = sys.get('E_perfect')
        E_def = sys.get('E_defect')
        if dop is None or E_perf is None or E_def is None:
            continue
        E_f = E_def - E_perf + mu
        if dop not in gold_vals:
            continue
        if abs(E_f - gold_vals[dop]) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='trend_iiia_gaps') ===
def score_4(artifact, step, ctx):
    dopants = step.get('dopants', [])
    dos_map = ctx['dos']
    gaps = {}
    for d in dopants:
        dos = dos_map.get(d)
        if not dos:
            return 0.0
        g = compute_energy_gap(dos)
        if g is None:
            return 0.0
        gaps[d] = g
    if gaps.get('Sc') > gaps.get('Y') > gaps.get('La'):
        return 1.0
    return 0.0


# === block: score_5 (check id='trend_vb_gaps') ===
def score_5(artifact, step, ctx):
    dopants = step.get('dopants', [])
    dos_map = ctx['dos']
    gaps = {}
    for d in dopants:
        dos = dos_map.get(d)
        if not dos:
            return 0.0
        g = compute_energy_gap(dos)
        if g is None:
            return 0.0
        gaps[d] = g
    if gaps.get('Sb') > gaps.get('Bi'):
        return 1.0
    return 0.0


# === block: score_6 (check id='trend_iiia_angle') ===
def score_6(artifact, step, ctx):
    angles = ctx.get('_bond_angles', {})
    if not angles:
        return 0.0
    a = angles.get('Sc')
    b = angles.get('Y')
    c = angles.get('La')
    if None in (a,b,c):
        return 0.0
    if c > b > a:
        return 1.0
    return 0.0


# === block: score_7 (check id='trend_iiia_opt_gaps') ===
def score_7(artifact, step, ctx):
    dopants = step.get('dopants', [])
    abs_map = ctx['absorption']
    gaps = {}
    for d in dopants:
        abs_data = abs_map.get(d)
        if not abs_data:
            return 0.0
        g = compute_optical_gap(abs_data)
        if g is None:
            return 0.0
        gaps[d] = g
    if gaps.get('Sc') > gaps.get('Y') > gaps.get('La'):
        return 1.0
    return 0.0


# === block: score_8 (check id='trend_vb_opt_gaps') ===
def score_8(artifact, step, ctx):
    dopants = step.get('dopants', [])
    abs_map = ctx['absorption']
    gaps = {}
    for d in dopants:
        abs_data = abs_map.get(d)
        if not abs_data:
            return 0.0
        g = compute_optical_gap(abs_data)
        if g is None:
            return 0.0
        gaps[d] = g
    if gaps.get('Sb') > gaps.get('Bi'):
        return 1.0
    return 0.0


_SCORERS = {
    'undoped_energy_gap': score_0,
    'undoped_optical_gap': score_1,
    'bond_angles_all': score_2,
    'formation_energies_all': score_3,
    'trend_iiia_gaps': score_4,
    'trend_vb_gaps': score_5,
    'trend_iiia_angle': score_6,
    'trend_iiia_opt_gaps': score_7,
    'trend_vb_opt_gaps': score_8,
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
