import os
import json
import csv

# === author imports / helpers ===
import math
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
    def prepare(outputs_dir, spec):
        json_path = os.path.join(outputs_dir, 'relative_energy_and_geometry.json')
        if not os.path.exists(json_path):
            return {'json_data': None}
        try:
            with open(json_path) as f:
                data = json.load(f)
            return {'json_data': data}
        except Exception:
            return {'json_data': None}


# === block: score_0 (check id='step_energy') ===
def score_0(artifact, step, ctx):
    if ctx is None:
        return 0.0
    json_data = ctx.get('json_data')
    if json_data is None:
        return 0.0
    if 'delta_E_kcal_per_mol' not in json_data:
        return 0.0
    val = json_data['delta_E_kcal_per_mol']
    target = step.get('target', -18.9)
    tol_abs = step.get('tolerance_abs', 3.0)
    abs_diff = abs(val - target)
    if abs_diff <= tol_abs:
        return 1.0
    # linear decay to zero at 2*tol_abs
    if abs_diff <= 2*tol_abs:
        return max(0.0, 1.0 - (abs_diff - tol_abs) / tol_abs)
    return 0.0


# === block: score_1 (check id='step_distances') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        json_data = ctx['json_data']
        if json_data is None:
            return 0.0
        target = step.get('target', {})
        tol_abs = step.get('tolerance_abs', 0.05)
        fe_fe_target = target.get('Fe_Fe_distance_P_Angstrom', 3.433)
        o_o_target = target.get('O_O_distance_P_Angstrom', 1.309)
        fe_o_target = target.get('Fe_O_distance_Q_Angstrom', [1.607, 1.611])

        scores = []
        # Fe-Fe
        if 'Fe_Fe_distance_P_Angstrom' in json_data:
            scores.append(1.0 if abs(json_data['Fe_Fe_distance_P_Angstrom'] - fe_fe_target) <= tol_abs else 0.0)
        else:
            scores.append(0.0)
        # O-O
        if 'O_O_distance_P_Angstrom' in json_data:
            scores.append(1.0 if abs(json_data['O_O_distance_P_Angstrom'] - o_o_target) <= tol_abs else 0.0)
        else:
            scores.append(0.0)
        # Fe-O pair
        fe_o_list = json_data.get('Fe_O_distance_Q_Angstrom', [])
        if isinstance(fe_o_list, list) and len(fe_o_list) == 2:
            # tolerance range: [min_target - tol, max_target + tol]
            lo = min(fe_o_target) - tol_abs
            hi = max(fe_o_target) + tol_abs
            ok = all(lo <= d <= hi for d in fe_o_list)
            scores.append(1.0 if ok else 0.0)
        else:
            scores.append(0.0)
        return sum(scores) / len(scores)  # average of 3 binary checks


# === block: score_2 (check id='step_P_xyz') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is file path, but our scorer receives artifact (loaded) or path? Actually the harness passes loaded artifact if json/csv, else raw string for txt/other.
        # We'll assume we get the file content as string (or we can load it again). We need path too. Safer: we get artifact_path? The contract says score(artifact, step, ctx) where artifact is loaded content (None if missing). For txt files, artifact is the file content as string (or None).
        json_data = ctx['json_data']
        if json_data is None:
            return 0.0
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        if len(lines) < 3:
            return 0.0
        try:
            natoms = int(lines[0].strip())
        except:
            return 0.0
        if natoms < 6:
            return 0.0
        atoms = []
        coords = []
        for line in lines[2:]:
            parts = line.strip().split()
            if len(parts) >= 4:
                atoms.append(parts[0])
                try:
                    coords.append([float(parts[1]), float(parts[2]), float(parts[3])])
                except:
                    coords.append([0.0,0.0,0.0])
            else:
                continue
        if len(atoms) < natoms:
            return 0.0
        o_indices = [i for i, a in enumerate(atoms) if a.upper() == 'O']
        if len(o_indices) < 2:
            return 0.0
        # compute all O-O distances, take minimum
        min_dist = float('inf')
        for i in range(len(o_indices)):
            for j in range(i+1, len(o_indices)):
                dx = coords[o_indices[i]][0] - coords[o_indices[j]][0]
                dy = coords[o_indices[i]][1] - coords[o_indices[j]][1]
                dz = coords[o_indices[i]][2] - coords[o_indices[j]][2]
                dist = math.sqrt(dx*dx + dy*dy + dz*dz)
                if dist < min_dist:
                    min_dist = dist
        ref_val = json_data.get('O_O_distance_P_Angstrom')
        if ref_val is None:
            return 0.0
        tol = step.get('tolerance_abs', 0.01)
        return 1.0 if abs(min_dist - ref_val) <= tol else 0.0


# === block: score_3 (check id='step_Q_xyz') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        json_data = ctx['json_data']
        if json_data is None:
            return 0.0
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        if len(lines) < 3:
            return 0.0
        try:
            natoms = int(lines[0].strip())
        except:
            return 0.0
        if natoms < 6:
            return 0.0
        atoms = []
        coords = []
        for line in lines[2:]:
            parts = line.strip().split()
            if len(parts) >= 4:
                atoms.append(parts[0])
                try:
                    coords.append([float(parts[1]), float(parts[2]), float(parts[3])])
                except:
                    coords.append([0.0,0.0,0.0])
            else:
                continue
        if len(atoms) < natoms:
            return 0.0
        fe_indices = [i for i, a in enumerate(atoms) if a.upper() == 'FE']
        o_indices = [i for i, a in enumerate(atoms) if a.upper() == 'O']
        if len(fe_indices) < 2 or len(o_indices) < 2:
            return 0.0
        # compute all Fe-O distances
        fe_o_distances = []
        for fi in fe_indices:
            for oi in o_indices:
                dx = coords[fi][0] - coords[oi][0]
                dy = coords[fi][1] - coords[oi][1]
                dz = coords[fi][2] - coords[oi][2]
                dist = math.sqrt(dx*dx + dy*dy + dz*dz)
                fe_o_distances.append(dist)
        fe_o_distances.sort()
        # take two smallest (should be terminal)
        terminal_dists = fe_o_distances[:2] if len(fe_o_distances) >= 2 else []
        ref_vals = json_data.get('Fe_O_distance_Q_Angstrom', [])
        if not isinstance(ref_vals, list) or len(ref_vals) != 2 or len(terminal_dists) < 2:
            return 0.0
        tol = step.get('tolerance_abs', 0.01)
        # check each ref value matches one terminal distance
        matched = 0
        for rv in ref_vals:
            for td in terminal_dists:
                if abs(rv - td) <= tol:
                    matched += 1
                    break
        return 1.0 if matched == 2 else 0.0


_SCORERS = {
    'step_energy': score_0,
    'step_distances': score_1,
    'step_P_xyz': score_2,
    'step_Q_xyz': score_3,
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
