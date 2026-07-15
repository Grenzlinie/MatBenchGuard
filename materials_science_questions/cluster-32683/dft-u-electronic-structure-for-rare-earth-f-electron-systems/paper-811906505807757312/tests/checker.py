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


# === block: score_0 (check id='dos_check') ===
def score_0(artifact, step, ctx):
    import math

    def find_local_min_near_zero(energies, dos_vals, tolerance):
        for i, e in enumerate(energies):
            if abs(e) <= tolerance:
                left_ok = (i == 0) or (dos_vals[i] <= dos_vals[i-1])
                right_ok = (i == len(energies)-1) or (dos_vals[i] <= dos_vals[i+1])
                if left_ok and right_ok:
                    return True
        return False

    def has_local_max_in_interval(energies, dos_vals, low, high):
        for i, e in enumerate(energies):
            if low < e < high:
                if i > 0 and i < len(energies)-1:
                    if dos_vals[i] > dos_vals[i-1] and dos_vals[i] > dos_vals[i+1]:
                        return True
        return False

    lines = artifact.strip().splitlines()
    points = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                e = float(parts[0])
                d = float(parts[1])
                points.append((e, d))
            except:
                pass
    if len(points) < 3:
        return 0.0

    points.sort(key=lambda x: x[0])
    energies, dos_vals = zip(*points)
    energies = list(energies)
    dos_vals = list(dos_vals)

    min_e = min(energies)
    max_e = max(energies)
    if min_e > -0.2 or max_e < 0.2:
        return 0.0

    tol = step.get("params", {}).get("ef_tolerance", 0.01)
    peak_half = step.get("params", {}).get("peak_window_half", 0.2)

    score = 0.0
    if find_local_min_near_zero(energies, dos_vals, tol):
        score += 1.0/3.0
    if has_local_max_in_interval(energies, dos_vals, -peak_half, 0):
        score += 1.0/3.0
    if has_local_max_in_interval(energies, dos_vals, 0, peak_half):
        score += 1.0/3.0

    return score


# === block: score_1 (check id='f_occ_check') ===
def score_1(artifact, step, ctx):
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    params = step.get("params", {})
    lo = params.get("min_val", 0.60)
    hi = params.get("max_val", 0.80)
    if lo <= val <= hi:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'dos_check': score_0,
    'f_occ_check': score_1,
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
