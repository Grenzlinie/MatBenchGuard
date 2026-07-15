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


# === block: score_0 (check id='step1_relax_h') ===
def score_0(artifact, step, ctx):
    import math
    lines = artifact.strip().split('\n')
    if len(lines) < 3:
        return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    atoms = []
    for line in lines[2:]:
        parts = line.strip().split()
        if not parts:
            continue
        elem = parts[0]
        try:
            x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
        except:
            continue
        atoms.append((elem, x, y, z))
    if len(atoms) != natoms:
        # still proceed but warn
        pass
    # find H atoms
    h_coords = []
    metal_coords = []
    for elem, x, y, z in atoms:
        if elem.lower().startswith('h'):
            h_coords.append((elem, x, y, z))
        elif elem in ('In', 'Ga', 'Zn'):
            metal_coords.append((elem, x, y, z))
    if len(h_coords) != 2:
        return 0.0
    CUTOFF = 2.5
    def get_metal_types(hx, hy, hz):
        result = set()
        for elem, mx, my, mz in metal_coords:
            d = math.hypot(hx-mx, hy-my, hz-mz)
            if d <= CUTOFF:
                result.add(elem)
        return result
    h1 = h_coords[0]
    h2 = h_coords[1]
    set1 = get_metal_types(h1[1], h1[2], h1[3])
    set2 = get_metal_types(h2[1], h2[2], h2[3])
    if set1 == set2:
        return 0.0
    if (('In' in set1 and 'Ga' in set1 and 'Zn' in set1) and ('Ga' in set2 and 'Zn' in set2 and 'In' not in set2)) or (('In' in set2 and 'Ga' in set2 and 'Zn' in set2) and ('Ga' in set1 and 'Zn' in set1 and 'In' not in set1)):
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step2_vib_dos') ===
def score_1(artifact, step, ctx):
    import json
    try:
        data = json.loads(artifact) if isinstance(artifact, str) else artifact
    except:
        return 0.0
    if not isinstance(data, dict):
        return 0.0
    required = ['M_H_stretching_frequencies_cm-1', 'mode_characters', 'gas_phase_hydride_frequencies_cm-1', 'red_shifts_cm-1', 'subgap_energy_above_VBM_eV']
    if not all(k in data for k in required):
        return 0.0
    freqs = data['M_H_stretching_frequencies_cm-1']
    shifts = data['red_shifts_cm-1']
    subgap = data['subgap_energy_above_VBM_eV']
    modes = data['mode_characters']
    if not isinstance(freqs, list) or len(freqs) != 2:
        return 0.0
    if not isinstance(shifts, list) or len(shifts) != 2:
        return 0.0
    if not isinstance(modes, list) or len(modes) != 2:
        return 0.0
    gold = step.get('gold', {})
    freq_targets = gold.get('freq_targets', [1389, 1524])
    freq_tol = gold.get('freq_tol', 75)
    shift_range = gold.get('shift_range', [60, 120])
    subgap_range = gold.get('subgap_range', [0.2, 0.6])
    mode_expected = gold.get('mode_characters_expected', ['In-H stretch', 'Zn-H stretch'])
    # frequency matching
    try:
        f = [float(freqs[0]), float(freqs[1])]
    except:
        return 0.0
    dists = [[abs(f[0]-t) for t in freq_targets], [abs(f[1]-t) for t in freq_targets]]
    perm1_max = max(dists[0][0], dists[1][1])
    perm2_max = max(dists[0][1], dists[1][0])
    best_max = min(perm1_max, perm2_max)
    if best_max <= freq_tol:
        freq_score = 1.0
    else:
        freq_score = 0.0
    # red shifts
    try:
        s = [float(shifts[0]), float(shifts[1])]
    except:
        shift_score = 0.0
    else:
        in_range = [1.0 if shift_range[0] <= v <= shift_range[1] else 0.0 for v in s]
        shift_score = sum(in_range) / 2.0  # 0, 0.5, or 1.0
    # subgap
    try:
        sg = float(subgap)
    except:
        sg = None
    if sg is not None and subgap_range[0] <= sg <= subgap_range[1]:
        subgap_score = 1.0
    else:
        subgap_score = 0.0
    # mode characters check
    mode_score = 0.0
    if len(modes) >= 2:
        if ('in-h' in modes[0].lower()) and ('zn-h' in modes[1].lower()):
            mode_score = 1.0
    # combine sub-scores
    score = freq_score * 0.4 + shift_score * 0.3 + subgap_score * 0.2 + mode_score * 0.1
    return score


_SCORERS = {
    'step1_relax_h': score_0,
    'step2_vib_dos': score_1,
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
