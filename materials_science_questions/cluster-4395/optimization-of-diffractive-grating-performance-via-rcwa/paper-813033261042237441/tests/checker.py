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
    return {}


# === block: score_0 (check id='simulate_polar_phase_shift') ===
def score_0(artifact, step, ctx):
    rows = artifact
    pdata = []
    for r in rows:
        try:
            angle = float(r['polar_angle'])
            shift = float(r['phase_shift'])
            pdata.append((angle, shift))
        except:
            return 0.0
    if len(pdata) != 3:
        return 0.0
    pdata.sort(key=lambda x: x[0])
    angles = [a for a,_ in pdata]
    shifts = [s for _,s in pdata]
    # monotonic increase
    if not all(x < y for x,y in zip(shifts, shifts[1:])):
        return 0.0
    # find 37 and 60 degree rows
    val37 = None
    val60 = None
    for a,s in pdata:
        if abs(a - 37.0) < 1e-6:
            val37 = s
        if abs(a - 60.0) < 1e-6:
            val60 = s
    if val37 is None or val60 is None:
        return 0.0
    ratio = val60 / val37
    if 1.15 <= ratio <= 1.45:
        return 1.0
    return 0.0


# === block: score_1 (check id='simulate_azimuth_phase_shift') ===
def score_1(artifact, step, ctx):
    rows = artifact
    data = []
    for r in rows:
        try:
            offset = float(r['azimuth_offset'])
            shift = float(r['phase_shift'])
            data.append((offset, shift))
        except:
            return 0.0
    if len(data) < 9:
        return 0.0
    # get phase_shift at offset 0
    ps0 = None
    for off, ps in data:
        if abs(off) < 1e-6:
            ps0 = ps
            break
    if ps0 is None:
        return 0.0
    # find max phase_shift and its offset
    max_ps = -1.0
    max_off = None
    for off, ps in data:
        if ps > max_ps:
            max_ps = ps
            max_off = off
    if max_off is None:
        return 0.0
    # check offset is non-zero and within allowed range
    if abs(max_off) < 0.5 or abs(max_off) > 4.0:
        return 0.0
    # enhancement ratio
    ratio = max_ps / ps0
    if 1.15 <= ratio <= 1.45:
        return 1.0
    return 0.0


_SCORERS = {
    'simulate_polar_phase_shift': score_0,
    'simulate_azimuth_phase_shift': score_1,
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
