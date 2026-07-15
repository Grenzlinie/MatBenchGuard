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
    return {'spec': spec}


# === block: score_0 (check id='energy_match') ===
def score_0(artifact, step, ctx):
    gold = step['gold_energies']
    tol = step.get('tolerance', 0.1)
    gold_map = {g['boundary_name']: g for g in gold}
    total = 0.0
    count = 0
    for row in artifact:
        bname = row.get('boundary_name')
        if bname not in gold_map:
            continue
        g = gold_map[bname]
        try:
            angle = float(row.get('misorientation_angle_deg'))
            energy = float(row.get('predicted_energy_Jm2'))
        except:
            continue
        if abs(angle - g['misorientation_angle_deg']) > 0.5:
            score_i = 0.0
        else:
            diff = abs(energy - g['predicted_energy_Jm2'])
            if diff <= tol:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (diff - tol) / tol)
        total += score_i
        count += 1
    if count == 0:
        return 0.0
    base_score = total / 13.0 if count < 13 else total / count
    return min(1.0, max(0.0, base_score))


# === block: score_1 (check id='structure_audit') ===
def score_1(artifact, step, ctx):
    points = []
    for row in artifact:
        try:
            angle = float(row['misorientation_angle_deg'])
            energy = float(row['predicted_energy_Jm2'])
        except:
            return 0.0
        points.append((angle, energy))
    if len(points) < 13:
        return 0.0
    points.sort(key=lambda x: x[0])
    angles = [p[0] for p in points]
    energies = [p[1] for p in points]
    max_idx = max(range(len(energies)), key=lambda i: energies[i])
    max_angle = angles[max_idx]
    max_angle_ok = 1.0 if 40 <= max_angle <= 50 else 0.0
    inc_viol = 0
    for i in range(max_idx):
        if energies[i] > energies[i+1] + 0.02:
            inc_viol += 1
    dec_viol = 0
    for i in range(max_idx, len(energies)-1):
        if energies[i] < energies[i+1] - 0.02:
            dec_viol += 1
    mono_score = max(0.0, 1.0 - 0.2 * (inc_viol + dec_viol))
    cusp_angles = [16.26, 67.38]
    cusp_ok = True
    for ca in cusp_angles:
        best_idx = None
        best_dist = 1.0
        for i, a in enumerate(angles):
            if abs(a - ca) <= best_dist:
                best_dist = abs(a - ca)
                best_idx = i
        if best_idx is None or best_dist > 1.0:
            cusp_ok = False
            break
        if best_idx > 0 and energies[best_idx] > energies[best_idx-1] + 0.01:
            cusp_ok = False
            break
        if best_idx < len(energies)-1 and energies[best_idx] > energies[best_idx+1] + 0.01:
            cusp_ok = False
            break
    cusp_score = 1.0 if cusp_ok else 0.0
    return max_angle_ok * 0.4 + mono_score * 0.3 + cusp_score * 0.3


_SCORERS = {
    'energy_match': score_0,
    'structure_audit': score_1,
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
