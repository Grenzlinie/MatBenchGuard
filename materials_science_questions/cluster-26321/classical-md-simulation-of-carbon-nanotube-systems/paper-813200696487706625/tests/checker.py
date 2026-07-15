import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

try:
    import numpy as np
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '--no-cache-dir', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'])
    import numpy as np


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


# === block: score_0 (check id='filling_energy_decrease') ===
def score_0(artifact, step, ctx):
    artifact = locals().get('artifact')
    params = step.get('params', {})
    early_start = params.get('early_start_ps', 0.0)
    early_end = params.get('early_end_ps', 2.0)
    late_start = params.get('late_start_ps', 38.0)
    late_end = params.get('late_end_ps', 40.0)
    required = params.get('required_decrease', 30.0)
    if not artifact or len(artifact) < 2:
        return 0.0
    times, energies = [], []
    for row in artifact:
        try:
            t = float(row['time_ps'])
            e = float(row['interaction_energy_kcal_per_mol'])
            times.append(t); energies.append(e)
        except: continue
    if not energies: return 0.0
    early_vals = [e for t,e in zip(times, energies) if early_start <= t <= early_end]
    late_vals = [e for t,e in zip(times, energies) if late_start <= t <= late_end]
    if not early_vals or not late_vals: return 0.0
    early_avg = sum(early_vals)/len(early_vals)
    late_avg = sum(late_vals)/len(late_vals)
    decrease = early_avg - late_avg
    score = min(1.0, max(0.0, decrease / required)) if required > 0 else 1.0
    return score


# === block: score_1 (check id='wrapping_energy_decrease') ===
def score_1(artifact, step, ctx):
    artifact = locals().get('artifact')
    params = step.get('params', {})
    early_start = params.get('early_start_ps', 0.0)
    early_end = params.get('early_end_ps', 2.0)
    late_start = params.get('late_start_ps', 98.0)
    late_end = params.get('late_end_ps', 100.0)
    required = params.get('required_decrease', 15.0)
    if not artifact or len(artifact) < 2:
        return 0.0
    times, energies = [], []
    for row in artifact:
        try:
            t = float(row['time_ps'])
            e = float(row['interaction_energy_kcal_per_mol'])
            times.append(t); energies.append(e)
        except: continue
    if not energies: return 0.0
    early_vals = [e for t,e in zip(times, energies) if early_start <= t <= early_end]
    late_vals = [e for t,e in zip(times, energies) if late_start <= t <= late_end]
    if not early_vals or not late_vals: return 0.0
    early_avg = sum(early_vals)/len(early_vals)
    late_avg = sum(late_vals)/len(late_vals)
    decrease = early_avg - late_avg
    score = min(1.0, max(0.0, decrease / required)) if required > 0 else 1.0
    return score


# === block: score_2 (check id='final_structures') ===
def score_2(artifact, step, ctx):
    text = locals().get('artifact', '')
    def parse_xyz(txt):
        frames = []
        lines = txt.strip().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line: i+=1; continue
            try: natoms = int(line)
            except: i+=1; continue
            i += 1
            if i >= len(lines): break
            comment = lines[i].strip()
            i += 1
            atoms = []
            for _ in range(natoms):
                if i >= len(lines): break
                parts = lines[i].split()
                if len(parts) >= 4:
                    el = parts[0]
                    try: x,y,z = float(parts[1]), float(parts[2]), float(parts[3])
                    except: continue
                    atoms.append((el,x,y,z))
                i += 1
            if len(atoms) == natoms:
                frames.append((comment, atoms))
        return frames

    def fit_tube(carbon_atoms):
        coords = np.array([[x,y,z] for _,x,y,z in carbon_atoms])
        if len(coords) < 5: return None, None, None
        centroid = np.mean(coords, axis=0)
        centered = coords - centroid
        cov = np.cov(centered.T)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        axis_idx = np.argmax(eigenvalues)
        axis = eigenvectors[:, axis_idx]
        axis = axis / np.linalg.norm(axis)
        dists = np.linalg.norm(centered - np.dot(centered, axis)[:,None]*axis, axis=1)
        radius = np.median(dists)
        return axis, centroid, radius

    def separate_atoms(atoms, axis, centroid, radius):
        tube, resin = [], []
        for el, x,y,z in atoms:
            pos = np.array([x,y,z])
            vec = pos - centroid
            axial = np.dot(vec, axis)
            radial = np.linalg.norm(vec - axial*axis)
            if el == 'H':
                tube.append((el,x,y,z, axial, radial))
            else:
                if 0.8*radius <= radial <= 1.2*radius:
                    tube.append((el,x,y,z, axial, radial))
                else:
                    resin.append((el,x,y,z, axial, radial))
        return tube, resin

    frames = parse_xyz(text)
    if len(frames) != 2:
        return 0.0
    (_, fill_atoms), (_, wrap_atoms) = frames

    carbon_fill = [a for a in fill_atoms if a[0] == 'C']
    if not carbon_fill: return 0.0
    axis_f, cent_f, rad_f = fit_tube(carbon_fill)
    if axis_f is None: return 0.0
    tube_f, resin_f = separate_atoms(fill_atoms, axis_f, cent_f, rad_f)
    fill_score = 0.0
    if resin_f:
        resin_coords = np.array([[x,y,z] for _,x,y,z,_,_ in resin_f])
        res_cent = np.mean(resin_coords, axis=0)
        vec = res_cent - cent_f
        ax_pos = np.dot(vec, axis_f)
        rad_pos = np.linalg.norm(vec - ax_pos*axis_f)
        tube_axial = [a[-2] for a in tube_f]
        if tube_axial:
            zmin, zmax = min(tube_axial), max(tube_axial)
            if rad_pos <= 7.0 and zmin-5 <= ax_pos <= zmax+5:
                fill_score = 1.0

    carbon_wrap = [a for a in wrap_atoms if a[0] == 'C']
    wrap_score = 0.0
    if carbon_wrap:
        axis_w, cent_w, rad_w = fit_tube(carbon_wrap)
        if axis_w is not None:
            tube_w, resin_w = separate_atoms(wrap_atoms, axis_w, cent_w, rad_w)
            if resin_w:
                coords_w = np.array([[x,y,z] for _,x,y,z,_,_ in resin_w])
                vecs = coords_w - cent_w
                axial_w = np.dot(vecs, axis_w)
                radial_w = np.linalg.norm(vecs - np.outer(axial_w, axis_w), axis=1)
                outside_ratio = np.mean(radial_w > rad_w*1.2)
                perp_vecs = vecs - np.outer(axial_w, axis_w)
                angles = np.arctan2(perp_vecs[:, 1], perp_vecs[:, 0])
                angles_sorted = np.sort(angles)
                max_gap = 0.0
                for i in range(len(angles_sorted)-1):
                    max_gap = max(max_gap, angles_sorted[i+1]-angles_sorted[i])
                max_gap = max(max_gap, angles_sorted[0] - angles_sorted[-1] + 2*np.pi)
                spread = 2*np.pi - max_gap
                if spread >= np.pi and outside_ratio >= 0.6:
                    wrap_score = 1.0
                elif spread >= 0.5*np.pi and outside_ratio >= 0.3:
                    wrap_score = 0.5

    return (fill_score + wrap_score) / 2.0


_SCORERS = {
    'filling_energy_decrease': score_0,
    'wrapping_energy_decrease': score_1,
    'final_structures': score_2,
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
