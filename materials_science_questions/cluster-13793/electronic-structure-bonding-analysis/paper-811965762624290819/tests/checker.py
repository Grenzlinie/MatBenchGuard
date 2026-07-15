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
    steps = spec.get('steps', [])
    ctx = {}
    for s in steps:
        ctx[s['id']] = s
    return ctx


# === block: score_0 (check id='check_high_symmetry_points') ===
def score_0(artifact, step, ctx):
    import math
    step_obj = ctx.get('check_high_symmetry_points', {})
    if not artifact or len(artifact) == 0:
        return 0.0
    targets = step_obj.get('targets', {})
    tol = step_obj.get('tolerance_abs', 0.5)
    k_tol = step_obj.get('k_distance_tol', 0.05)

    # parse artifact: list of dicts with columns direction,kx,ky,kz,energy
    # compute distances and collect energies per symmetry point
    from collections import defaultdict
    sym_energies = defaultdict(list)
    for row in artifact:
        kx = float(row['kx'])
        ky = float(row['ky'])
        kz = float(row['kz'])
        energy = float(row['energy'])
        for sym, data in targets.items():
            kref = data['k']
            d = math.sqrt((kx - kref[0])**2 + (ky - kref[1])**2 + (kz - kref[2])**2)
            if d < k_tol:
                sym_energies[sym].append(energy)

    match_counts = []
    for sym, data in targets.items():
        ref_vals = sorted(data['energy_ref'])
        cand_vals = sorted(sym_energies.get(sym, []))
        # greedy matching: for each ref, find closest cand within tol
        used = [False] * len(cand_vals)
        matched = 0
        for ref_e in ref_vals:
            best_dist = float('inf')
            best_idx = -1
            for i, cand_e in enumerate(cand_vals):
                if not used[i]:
                    dist = abs(cand_e - ref_e)
                    if dist < best_dist:
                        best_dist = dist
                        best_idx = i
            if best_idx >= 0 and best_dist <= tol:
                used[best_idx] = True
                matched += 1
        match_counts.append((matched, len(ref_vals)))

    if not match_counts:
        return 0.0
    # compute average ratio
    ratios = [m / t if t > 0 else 0.0 for m, t in match_counts]
    avg = sum(ratios) / len(ratios)
    return min(1.0, max(0.0, avg))


# === block: score_1 (check id='check_metallic_crossing') ===
def score_1(artifact, step, ctx):
    import math
    step_obj = ctx.get('check_metallic_crossing', {})
    if not artifact or len(artifact) == 0:
        return 0.0
    threshold = step_obj.get('targets', {}).get('crossing_threshold_eV', 0.1)
    required_dirs = step_obj.get('targets', {}).get('required_directions', [])
    # for each direction, check if any energy absolute value < threshold
    crossing = {d: False for d in required_dirs}
    for row in artifact:
        direction = row['direction']
        energy = float(row['energy'])
        if direction in crossing and abs(energy) < threshold:
            crossing[direction] = True
    score = sum(1.0 for v in crossing.values() if v) / len(crossing)
    return score


_SCORERS = {
    'check_high_symmetry_points': score_0,
    'check_metallic_crossing': score_1,
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
