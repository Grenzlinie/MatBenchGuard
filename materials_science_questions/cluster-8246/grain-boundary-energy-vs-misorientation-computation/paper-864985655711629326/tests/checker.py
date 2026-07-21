import os
import json
import csv

# === author imports / helpers ===
import math, io, csv


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


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    def parse_xyz(data):
        lines = data.strip().splitlines()
        if len(lines) < 3:
            return None
        try:
            natoms = int(lines[0].strip())
        except:
            return None
        atoms = []
        for line in lines[2:]:
            if len(atoms) >= natoms:
                break
            parts = line.split()
            if len(parts) < 4:
                continue
            elem = parts[0]
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            except:
                continue
            atoms.append((elem, x, y, z))
        return atoms

    ref_atoms = step["reference_atoms"]
    tol = step["tolerance_abs"]
    agent_atoms = parse_xyz(artifact)
    if not agent_atoms:
        return 0.0
    if abs(len(agent_atoms) - len(ref_atoms)) > 1e-3:
        return 0.0

    # centroid alignment to remove rigid translations
    ref_cx = sum(r[0] for r in ref_atoms) / len(ref_atoms)
    ref_cy = sum(r[1] for r in ref_atoms) / len(ref_atoms)
    ref_cz = sum(r[2] for r in ref_atoms) / len(ref_atoms)
    agent_cx = sum(x for _, x, y, z in agent_atoms) / len(agent_atoms)
    agent_cy = sum(y for _, x, y, z in agent_atoms) / len(agent_atoms)
    agent_cz = sum(z for _, x, y, z in agent_atoms) / len(agent_atoms)
    offset_x = ref_cx - agent_cx
    offset_y = ref_cy - agent_cy
    offset_z = ref_cz - agent_cz

    matched = 0
    unmatched_ref = set(range(len(ref_atoms)))
    for elem, x, y, z in agent_atoms:
        ax = x + offset_x
        ay = y + offset_y
        az = z + offset_z
        best_dist = float('inf')
        best_idx = -1
        for j in unmatched_ref:
            rx, ry, rz = ref_atoms[j]
            d = math.sqrt((ax-rx)**2 + (ay-ry)**2 + (az-rz)**2)
            if d < best_dist:
                best_dist = d
                best_idx = j
        if best_dist <= tol:
            matched += 1
            unmatched_ref.remove(best_idx)
    return matched / len(ref_atoms)


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    def parse_xyz(data):
        lines = data.strip().splitlines()
        if len(lines) < 3:
            return None
        try:
            natoms = int(lines[0].strip())
        except:
            return None
        atoms = []
        for line in lines[2:]:
            if len(atoms) >= natoms:
                break
            parts = line.split()
            if len(parts) < 4:
                continue
            elem = parts[0]
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            except:
                continue
            atoms.append((elem, x, y, z))
        return atoms

    ref_atoms = step["reference_atoms"]
    tol = step["tolerance_abs"]
    agent_atoms = parse_xyz(artifact)
    if not agent_atoms:
        return 0.0
    if abs(len(agent_atoms) - len(ref_atoms)) > 1e-3:
        return 0.0
    matched = 0
    unmatched_ref = set(range(len(ref_atoms)))
    for elem, x, y, z in agent_atoms:
        best_dist = float('inf')
        best_idx = -1
        for j in unmatched_ref:
            rx, ry, rz = ref_atoms[j]
            d = math.sqrt((x-rx)**2 + (y-ry)**2 + (z-rz)**2)
            if d < best_dist:
                best_dist = d
                best_idx = j
        if best_dist <= tol:
            matched += 1
            unmatched_ref.remove(best_idx)
    return matched / len(ref_atoms)


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    gold_rows = step["gold_rows"]
    tolerances = step["tolerances"]
    rows = artifact
    found = {"domino": None, "pearl": None}
    for row in rows:
        sid = row.get("structure_id", "").strip().lower()
        if sid == "domino" and found["domino"] is None:
            found["domino"] = row
        elif sid == "pearl" and found["pearl"] is None:
            found["pearl"] = row
    if not found["domino"] or not found["pearl"]:
        return 0.0
    total_fields = 0
    passed_fields = 0
    for phase in ["domino", "pearl"]:
        row = found[phase]
        gold = gold_rows[phase]
        for field, gt_val in gold.items():
            if field not in row:
                continue
            try:
                val = float(row[field])
            except:
                continue
            tol = tolerances.get(field, 0.01)
            total_fields += 1
            if abs(val - gt_val) <= tol:
                passed_fields += 1
    if total_fields == 0:
        return 0.0
    return passed_fields / total_fields


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    rows = artifact
    min_extra = step.get("min_additional_structures", 10)
    found_domino = False
    found_pearl = False
    domino_label = None
    pearl_label = None
    extra = 0
    for row in rows:
        sid = row.get("structure_id", "").strip().lower()
        label = row.get("cluster_label")
        if label is None:
            continue
        try:
            label = int(label)
        except:
            continue
        if sid == "domino":
            found_domino = True
            domino_label = label
        elif sid == "pearl":
            found_pearl = True
            pearl_label = label
        else:
            extra += 1
    if not (found_domino and found_pearl):
        return 0.0
    if domino_label == pearl_label:
        return 0.0
    if extra < min_extra:
        return 0.0
    return 1.0


# === block: score_4 (check id='step_07') ===
def score_4(artifact, step, ctx):
    rows = artifact
    if not rows or not all(col in rows[0] for col in ["T", "gamma_domino", "gamma_pearl"]):
        return 0.0
    ts = []
    gd = []
    gp = []
    for row in rows:
        try:
            t = float(row["T"])
            d = float(row["gamma_domino"])
            p = float(row["gamma_pearl"])
            ts.append(t)
            gd.append(d)
            gp.append(p)
        except:
            continue
    if len(ts) < 2:
        return 0.0
    sorted_idx = sorted(range(len(ts)), key=lambda i: ts[i])
    ts_sorted = [ts[i] for i in sorted_idx]
    max_step = max(ts_sorted[j]-ts_sorted[j-1] for j in range(1,len(ts_sorted))) if len(ts_sorted)>1 else 999
    shape_valid = (min(ts) <= 0.1 and max(ts) >= 799) and max_step <= 51
    crossing_found = False
    crossing_T = None
    for i in range(1, len(ts_sorted)):
        idx1 = sorted_idx[i-1]
        idx2 = sorted_idx[i]
        diff1 = gd[idx1] - gp[idx1]
        diff2 = gd[idx2] - gp[idx2]
        if diff1 * diff2 < 0:
            t1 = ts[idx1]
            t2 = ts[idx2]
            denom = abs(diff1) + abs(diff2)
            if denom != 0:
                ratio = abs(diff1) / denom
                crossing_T = t1 + ratio * (t2 - t1)
            else:
                crossing_T = (t1 + t2) / 2.0
            crossing_found = True
            break
    crossing_score = 0.0
    if crossing_found and crossing_T is not None:
        if 400 <= crossing_T <= 520:
            crossing_score = 1.0
    shape_score = 1.0 if shape_valid else 0.0
    return 0.9 * crossing_score + 0.1 * shape_score


_SCORERS = {
    'step_03': score_0,
    'step_04': score_1,
    'step_05': score_2,
    'step_06': score_3,
    'step_07': score_4,
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
