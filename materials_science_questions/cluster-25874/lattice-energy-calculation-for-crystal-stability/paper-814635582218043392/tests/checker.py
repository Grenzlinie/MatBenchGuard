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
    return {
        "target_energy_kj": -325.3,
        "tol_high_rel": 0.01,
        "tol_low_rel": 0.10,
        "params": {
            "A_CC": 83630.0,
            "B_CC": 3.60,
            "C_CC": 568.0,
            "A_CH": 8766.0,
            "B_CH": 3.67,
            "C_CH": 125.0,
            "A_HH": 2654.0,
            "B_HH": 3.74,
            "C_HH": 27.4,
            "q_C": -0.153,
            "q_H": 0.153
        }
    }


# === block: score_0 (check id='validate_xyz') ===
def score_0(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 158:
        return 0.0
    if lines[0].strip() != '156':
        return 0.0
    atom_count = 0
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4:
            return 0.0
        if parts[0] not in ('C', 'H'):
            return 0.0
        try:
            float(parts[1]); float(parts[2]); float(parts[3])
        except ValueError:
            return 0.0
        atom_count += 1
    if atom_count != 156:
        return 0.0
    return 1.0


# === block: score_1 (check id='recompute_energy') ===
def score_1(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 158:
        return 0.0
    try:
        num_atoms = int(lines[0].strip())
        if num_atoms != 156:
            return 0.0
    except ValueError:
        return 0.0
    coords = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4:
            return 0.0
        elem = parts[0]
        try:
            x = float(parts[1]); y = float(parts[2]); z = float(parts[3])
        except ValueError:
            return 0.0
        coords.append((elem, x, y, z))
    if len(coords) != 156:
        return 0.0

    mol_size = 12
    n_mol = 13
    molecules = []
    for i in range(n_mol):
        mol_coords = []
        for j in range(mol_size):
            idx = i * mol_size + j
            mol_coords.append(coords[idx])
        molecules.append(mol_coords)

    params = ctx["params"]
    A_CC = params["A_CC"]; B_CC = params["B_CC"]; C_CC = params["C_CC"]
    A_CH = params["A_CH"]; B_CH = params["B_CH"]; C_CH = params["C_CH"]
    A_HH = params["A_HH"]; B_HH = params["B_HH"]; C_HH = params["C_HH"]
    q_C = params["q_C"]; q_H = params["q_H"]

    coul_const = 332.0637  # kcal·Å/mol/e²
    kcal_to_kj = 4.184

    total_energy_kcal = 0.0
    for i in range(n_mol):
        for j in range(i+1, n_mol):
            for ai in range(mol_size):
                elem_i, xi, yi, zi = molecules[i][ai]
                qi = q_C if elem_i == 'C' else q_H
                for aj in range(mol_size):
                    elem_j, xj, yj, zj = molecules[j][aj]
                    qj = q_C if elem_j == 'C' else q_H
                    dx = xi - xj; dy = yi - yj; dz = zi - zj
                    r = math.sqrt(dx*dx + dy*dy + dz*dz)
                    if r < 0.001:
                        continue
                    if elem_i == 'C' and elem_j == 'C':
                        A, B, C = A_CC, B_CC, C_CC
                    elif (elem_i == 'C' and elem_j == 'H') or (elem_i == 'H' and elem_j == 'C'):
                        A, B, C = A_CH, B_CH, C_CH
                    else:
                        A, B, C = A_HH, B_HH, C_HH
                    v_rep = A * math.exp(-B * r) - C / (r**6)
                    v_coul = qi * qj * coul_const / r
                    total_energy_kcal += v_rep + v_coul

    total_energy_kj = total_energy_kcal * kcal_to_kj
    target = ctx["target_energy_kj"]
    error = abs(total_energy_kj - target)
    rel_err = error / abs(target)
    tol_high = ctx["tol_high_rel"]
    tol_low = ctx["tol_low_rel"]
    if rel_err <= tol_high:
        return 1.0
    elif rel_err >= tol_low:
        return 0.0
    else:
        return 1.0 - (rel_err - tol_high) / (tol_low - tol_high)


# === block: score_2 (check id='check_reported_energy') ===
def score_2(artifact, step, ctx):
    try:
        reported = float(artifact.strip())
    except (ValueError, TypeError):
        return 0.0
    target = ctx["target_energy_kj"]
    error = abs(reported - target)
    rel_err = error / abs(target)
    tol_high = ctx["tol_high_rel"]
    tol_low = ctx["tol_low_rel"]
    if rel_err <= tol_high:
        return 1.0
    elif rel_err >= tol_low:
        return 0.0
    else:
        return 1.0 - (rel_err - tol_high) / (tol_low - tol_high)


_SCORERS = {
    'validate_xyz': score_0,
    'recompute_energy': score_1,
    'check_reported_energy': score_2,
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
