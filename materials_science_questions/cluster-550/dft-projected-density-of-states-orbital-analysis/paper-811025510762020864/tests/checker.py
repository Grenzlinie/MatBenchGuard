import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import math

def compute_integrated_dos(rows, energy_window):
    e0, e1 = energy_window
    compos = {}
    for row in rows:
        c = int(row['composition'])
        e = float(row['energy_ev'])
        d = float(row['dos'])
        if e0 <= e <= e1:
            compos.setdefault(c, []).append((e, d))
    integrals = {}
    for c, points in compos.items():
        points.sort(key=lambda x: x[0])
        total = 0.0
        for i in range(len(points)-1):
            e1_val, d1_val = points[i]
            e2_val, d2_val = points[i+1]
            total += (e2_val - e1_val) * (d1_val + d2_val) / 2.0
        integrals[c] = total
    return integrals

def fwhm(energy, dos):
    n = len(energy)
    if n == 0:
        return None
    max_idx = max(range(n), key=lambda i: dos[i])
    max_val = dos[max_idx]
    if max_val <= 0:
        return None
    half = max_val / 2.0
    # left crossing
    left_e = None
    i = max_idx
    while i > 0 and dos[i-1] > half:
        i -= 1
    if i == 0:
        left_e = energy[0]
    else:
        e_low = energy[i-1]
        d_low = dos[i-1]
        e_high = energy[i]
        d_high = dos[i]
        if d_high == d_low:
            left_e = (e_low + e_high) / 2.0
        else:
            left_e = e_low + (half - d_low) / (d_high - d_low) * (e_high - e_low)
    # right crossing
    right_e = None
    i = max_idx
    while i < n-1 and dos[i+1] > half:
        i += 1
    if i == n-1:
        right_e = energy[-1]
    else:
        e_low = energy[i]
        d_low = dos[i]
        e_high = energy[i+1]
        d_high = dos[i+1]
        if d_high == d_low:
            right_e = (e_low + e_high) / 2.0
        else:
            right_e = e_low + (half - d_low) / (d_high - d_low) * (e_high - e_low)
    return right_e - left_e


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


# === block: score_0 (check id='co3d_trend') ===
def score_0(artifact, step, ctx):
    window = step.get('energy_window', [-0.5, 0.0])
    factor = step.get('threshold_factor', 1.5)
    integrals = compute_integrated_dos(artifact, window)
    expected = {0, 25, 50, 75}
    if not expected.issubset(integrals.keys()):
        return 0.0
    int_25 = integrals[25]
    other_max = max(integrals[c] for c in (0, 50, 75))
    if int_25 >= factor * other_max and other_max >= 0:
        return 1.0
    return 0.0


# === block: score_1 (check id='pd4d_trend') ===
def score_1(artifact, step, ctx):
    compos = {}
    for row in artifact:
        c = int(row['composition'])
        e = float(row['energy_ev'])
        d = float(row['dos'])
        compos.setdefault(c, []).append((e, d))
    fw_dict = {}
    for c, points in compos.items():
        points.sort(key=lambda x: x[0])
        energy = [p[0] for p in points]
        dos = [p[1] for p in points]
        fw = fwhm(energy, dos)
        if fw is None:
            return 0.0
        fw_dict[c] = fw
    expected = {0, 25, 50, 75}
    if not expected.issubset(fw_dict.keys()):
        return 0.0
    if fw_dict[0] < fw_dict[25] < fw_dict[50] < fw_dict[75]:
        return 1.0
    return 0.0


_SCORERS = {
    'co3d_trend': score_0,
    'pd4d_trend': score_1,
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
