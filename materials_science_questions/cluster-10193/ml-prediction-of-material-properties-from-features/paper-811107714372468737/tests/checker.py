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


# === block: score_0 (check id='step_structural') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        # Safely parse rows; skip any with unparseable angle or energy
        rows = []
        for r in artifact:
            try:
                angle = float(r.get('misorientation_angle'))
                energy = float(r.get('predicted_energy'))
                rows.append((angle, energy))
            except (TypeError, ValueError):
                continue
        if len(rows) < 3:
            return 0.0
        # Sort by angle
        rows.sort(key=lambda x: x[0])
        angles = [a for a, _ in rows]
        energies = [e for _, e in rows]
        n = len(rows)

        # convexity: max energy within max_angle_window
        max_idx = max(range(n), key=lambda i: energies[i])
        max_angle = angles[max_idx]
        window = step.get('config', {}).get('max_angle_window', [40, 50])
        convex_score = 1.0 if window[0] <= max_angle <= window[1] else 0.0

        # cusp detection
        cusp_angles = step.get('config', {}).get('cusp_angles', [])
        angle_tol = step.get('config', {}).get('angle_tolerance', 2.0)
        cusp_weight = step.get('checks', {}).get('cusps', {}).get('weight', 0.6)
        convex_weight = step.get('checks', {}).get('convexity', {}).get('weight', 0.4)

        checked = 0
        passed = 0
        for ca in cusp_angles:
            nearby = [i for i in range(n) if abs(angles[i] - ca) <= angle_tol]
            if not nearby:
                continue
            closest = min(nearby, key=lambda i: abs(angles[i] - ca))
            if closest > 0 and closest < n - 1:
                if energies[closest] < energies[closest - 1] and energies[closest] < energies[closest + 1]:
                    passed += 1
                checked += 1
        cusp_score = (passed / checked) if checked > 0 else 1.0

        total = convex_weight * convex_score + cusp_weight * cusp_score
        return min(max(total, 0.0), 1.0)


# === block: score_1 (check id='step_sigma13_energy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        target = step['target']
        tol_rel = step['tolerance_relative']
        bound = step['filter']['boundary']
        for row in artifact:
            if row.get('boundary') == bound:
                energy = float(row['predicted_energy'])
                if abs(energy - target) <= target * tol_rel:
                    return 1.0
                else:
                    return 0.0
        return 0.0


# === block: score_2 (check id='step_sigma13_translation') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        target_coords = step['target']
        tol_abs = step['tolerance_abs']
        bound = step['filter']['boundary']
        cols = step['columns']
        for row in artifact:
            if row.get('boundary') == bound:
                for axis, col in zip(['X', 'Y', 'Z'], cols):
                    val = float(row[col])
                    if abs(val - target_coords[axis]) > tol_abs:
                        return 0.0
                return 1.0
        return 0.0


_SCORERS = {
    'step_structural': score_0,
    'step_sigma13_energy': score_1,
    'step_sigma13_translation': score_2,
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
