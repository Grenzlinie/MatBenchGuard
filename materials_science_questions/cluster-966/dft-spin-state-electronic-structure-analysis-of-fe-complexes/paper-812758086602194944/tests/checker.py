import os
import json
import csv

# === author imports / helpers ===
import math
import json
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
        xyz_path = os.path.join(outputs_dir, 'step_01_optimized_structures.xyz')
        ctx = {}
        if not os.path.exists(xyz_path):
            ctx['xyz_structs'] = None
            return ctx
        with open(xyz_path) as f:
            lines = f.readlines()
        structs = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            try:
                natoms = int(line)
            except:
                break
            if i+1 >= len(lines):
                break
            comment = lines[i+1].strip()
            atoms = []
            for j in range(natoms):
                if i+2+j >= len(lines):
                    break
                parts = lines[i+2+j].split()
                if len(parts) >= 4:
                    sym = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                    atoms.append((sym, x, y, z))
            if len(atoms) == natoms:
                structs.append((comment, atoms))
            i += 2 + natoms
        ctx['xyz_structs'] = structs
        return ctx


# === block: score_0 (check id='step_01_xyz_valid') ===
def score_0(artifact, step, ctx):
        if not artifact:
            return 0.0
        expected = {
            'deprotonated A1': {'Fe':2, 'C':12, 'H':16, 'N':18},
            'deprotonated A2': {'Fe':4, 'C':24, 'H':32, 'N':36},
            'deprotonated A3': {'Fe':6, 'C':36, 'H':48, 'N':54},
            'undeprotonated A1': {'Fe':2, 'C':12, 'H':18, 'N':18},
            'undeprotonated A2': {'Fe':4, 'C':24, 'H':36, 'N':36},
            'undeprotonated A3': {'Fe':6, 'C':36, 'H':54, 'N':54},
        }
        lines = artifact.strip().splitlines()
        structs = []
        i = 0
        while i < len(lines):
            try:
                natoms = int(lines[i].strip())
            except:
                i += 1
                continue
            if i+1 >= len(lines):
                break
            comment = lines[i+1].strip()
            atoms = lines[i+2:i+2+natoms]
            if len(atoms) != natoms:
                break
            counts = {}
            for a in atoms:
                sym = a.split()[0]
                counts[sym] = counts.get(sym, 0) + 1
            structs.append((comment, counts))
            i += 2 + natoms
        found = {name: False for name in expected}
        for comment, counts in structs:
            if comment in expected:
                if counts == expected[comment]:
                    found[comment] = True
        n_correct = sum(found.values())
        if n_correct == 6:
            return 1.0
        else:
            return max(0.0, (n_correct - 3) / 3.0)


# === block: score_1 (check id='step_02_fe_fe_trend') ===
def score_1(artifact, step, ctx):
        xyz_structs = ctx.get('xyz_structs', None)
        if not xyz_structs or not artifact:
            return 0.0
        deprot = artifact.get('deprotonated', {})
        undpr = artifact.get('undeprotonated', {})
        name_to_json = {}
        for model in ('A1','A2','A3'):
            if model in deprot:
                name_to_json[f'deprotonated {model}'] = deprot[model]
            if model in undpr:
                name_to_json[f'undeprotonated {model}'] = undpr[model]
        def compute_fe_fe(atoms):
            fe_indices = [i for i, (sym, x, y, z) in enumerate(atoms) if sym == 'Fe']
            if len(fe_indices) < 2:
                return []
            sorted_fe = sorted(fe_indices, key=lambda i: atoms[i][1])
            dists = []
            for j in range(len(sorted_fe)-1):
                i1, i2 = sorted_fe[j], sorted_fe[j+1]
                x1, y1, z1 = atoms[i1][1], atoms[i1][2], atoms[i1][3]
                x2, y2, z2 = atoms[i2][1], atoms[i2][2], atoms[i2][3]
                d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
                dists.append(d)
            return dists
        consistency_ok = True
        size_dep = {}
        size_und = {}
        for comment, atoms in xyz_structs:
            if comment not in name_to_json:
                continue
            json_dists = name_to_json[comment]
            computed_dists = compute_fe_fe(atoms)
            if len(json_dists) != len(computed_dists):
                consistency_ok = False
            else:
                for jd, cd in zip(json_dists, computed_dists):
                    if abs(jd - cd) > 1e-4:
                        consistency_ok = False
                        break
            if not json_dists:
                continue
            fe_count = sum(1 for _, sym, _, _, _ in atoms if sym == 'Fe')
            mean = sum(json_dists) / len(json_dists)
            if 'deprotonated' in comment:
                size_dep[fe_count] = mean
            else:
                size_und[fe_count] = mean
        if not consistency_ok or len(size_dep) != 3 or len(size_und) != 3:
            return 0.0
        trend_ok = True
        for fe_count in (2, 4, 6):
            if fe_count in size_dep and fe_count in size_und:
                if size_dep[fe_count] >= size_und[fe_count]:
                    trend_ok = False
                    break
        return 1.0 if trend_ok else 0.0


# === block: score_2 (check id='step_03_fe_n_trend') ===
def score_2(artifact, step, ctx):
        if not artifact:
            return 0.0
        deprot = artifact.get('deprotonated', {})
        undpr = artifact.get('undeprotonated', {})
        total_checks = 0
        passed = 0
        for model in ('A2', 'A3'):
            if model not in deprot:
                continue
            deprot_rings = deprot[model].get('deprot_ring', [])
            undeprot_rings = deprot[model].get('undeprot_ring', [])
            if deprot_rings and undeprot_rings:
                total_checks += 1
                if sum(deprot_rings) / len(deprot_rings) < sum(undeprot_rings) / len(undeprot_rings):
                    passed += 1
            if model in undpr and deprot_rings and undeprot_rings:
                all_deprot = deprot_rings + undeprot_rings
                all_undpr = undpr[model]
                if all_deprot and all_undpr:
                    total_checks += 1
                    if sum(all_deprot) / len(all_deprot) < sum(all_undpr) / len(all_undpr):
                        passed += 1
        if total_checks == 0:
            return 0.0
        return passed / total_checks


# === block: score_3 (check id='step_04_energy_trend') ===
def score_3(artifact, step, ctx):
        if not artifact:
            return 0.0
        deprot = artifact.get('deprotonated', {})
        undpr = artifact.get('undeprotonated', {})
        checks = 0
        passed = 0
        for model in ('A1', 'A2', 'A3'):
            d = deprot.get(model)
            u = undpr.get(model)
            if d is not None and u is not None:
                checks += 1
                if d < u:
                    passed += 1
        if checks == 0:
            return 0.0
        return passed / checks


_SCORERS = {
    'step_01_xyz_valid': score_0,
    'step_02_fe_fe_trend': score_1,
    'step_03_fe_n_trend': score_2,
    'step_04_energy_trend': score_3,
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
