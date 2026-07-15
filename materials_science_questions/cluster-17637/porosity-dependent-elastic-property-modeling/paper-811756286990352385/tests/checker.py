import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    kelvin_data = []
    gibson_data = []
    for row in artifact:
        try:
            m = row['model'].strip()
            s = float(row['strain'])
            stress = float(row['stress'])
        except (ValueError, KeyError):
            continue
        if m == 'Kelvin':
            kelvin_data.append((s, stress))
        elif m == 'Gibson-Ashby':
            gibson_data.append((s, stress))
    if not kelvin_data or not gibson_data:
        return 0.0
    kelvin_data.sort(key=lambda x: x[0])
    gibson_data.sort(key=lambda x: x[0])
    strain_tol = step.get('params', {}).get('strain_tolerance', 1e-4)
    rel_tol = step.get('params', {}).get('relative_tolerance', 0.05)
    total_pairs = 0
    valid_pairs = 0
    for k_strain, k_stress in kelvin_data:
        lo, hi = 0, len(gibson_data)-1
        best_idx = None
        best_delta = float('inf')
        while lo <= hi:
            mid = (lo+hi)//2
            g_strain, g_stress = gibson_data[mid]
            delta = abs(g_strain - k_strain)
            if delta < best_delta:
                best_delta = delta
                best_idx = mid
            if g_strain < k_strain:
                lo = mid+1
            else:
                hi = mid-1
        if best_delta <= strain_tol:
            g_strain, g_stress = gibson_data[best_idx]
            total_pairs += 1
            max_val = max(abs(k_stress), abs(g_stress))
            if k_stress > g_stress - rel_tol * max_val and k_stress > 0 and g_stress > 0:
                valid_pairs += 1
    if total_pairs == 0:
        return 0.0
    score = valid_pairs / total_pairs
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='s2') ===
def score_1(artifact, step, ctx):
    groups = {}
    for row in artifact:
        try:
            p = float(row['porosity'])
            s = float(row['strain'])
            stress = float(row['stress'])
        except (ValueError, KeyError):
            continue
        groups.setdefault(p, []).append((s, stress))
    porosities = step.get('params', {}).get('porosities', [89,92,95,97])
    for p in porosities:
        if p not in groups or len(groups[p]) == 0:
            return 0.0
    sanity_fail = False
    for p in porosities:
        data = groups[p]
        data.sort(key=lambda x: x[0])
        for i in range(1, len(data)):
            if data[i][0] <= data[i-1][0] or data[i][1] <= 0 or data[i-1][1] <= 0:
                sanity_fail = True
                break
        if sanity_fail:
            break
    sanity_weight = step.get('params', {}).get('sanity_checks_weight', 0.1)
    sanity_score = 0.0 if sanity_fail else 1.0
    ref_data = groups[porosities[0]]
    strain_tol = step.get('params', {}).get('strain_tolerance', 1e-4)
    rel_tol = step.get('params', {}).get('relative_tolerance', 0.05)
    total_points = 0
    ordered_points = 0
    for ref_strain, ref_stress in ref_data:
        others = []
        for p in porosities[1:]:
            other_data = groups[p]
            best_idx = None
            best_delta = float('inf')
            for idx, (s, stress) in enumerate(other_data):
                delta = abs(s - ref_strain)
                if delta < best_delta:
                    best_delta = delta
                    best_idx = idx
            if best_delta > strain_tol:
                break
            others.append(other_data[best_idx][1])
        if len(others) == len(porosities)-1:
            total_points += 1
            stresses = [ref_stress] + others
            ordered = True
            for i in range(len(stresses)-1):
                s1 = stresses[i]
                s2 = stresses[i+1]
                max_val = max(abs(s1), abs(s2))
                if s1 <= s2 - rel_tol * max_val:
                    ordered = False
                    break
            if ordered:
                ordered_points += 1
    order_score = ordered_points / total_points if total_points > 0 else 0.0
    final_score = (1 - sanity_weight) * order_score + sanity_weight * sanity_score
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    's1': score_0,
    's2': score_1,
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
