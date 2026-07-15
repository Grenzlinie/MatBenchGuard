import os
import json
import csv

# === author imports / helpers ===
import re
try:
    import yaml
except ModuleNotFoundError:
    pass
import math
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
    return {}


# === block: score_0 (check id='s2') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, str):
        return 0.0
    text = artifact
    a = None; b = None; c = None
    for line in text.splitlines():
        if line.startswith('_cell_length_a'):
            a = float(line.split()[-1])
        elif line.startswith('_cell_length_b'):
            b = float(line.split()[-1])
        elif line.startswith('_cell_length_c'):
            c = float(line.split()[-1])
    if None in (a, b, c):
        return 0.0
    target_a = float(step.get('target_lattice_a', 2.469))
    target_b = float(step.get('target_lattice_b', 11.170))
    target_c = float(step.get('target_lattice_c', 4.802))
    tol_a = float(step.get('tolerance_a', 0.05))
    tol_b = float(step.get('tolerance_b', 0.1))
    tol_c = float(step.get('tolerance_c', 0.05))
    ok_a = abs(a - target_a) <= tol_a
    ok_b = abs(b - target_b) <= tol_b
    ok_c = abs(c - target_c) <= tol_c
    n_atoms = text.count(' C ')
    required_n = int(step.get('require_n_atoms', 24))
    ok_natoms = (n_atoms == required_n)
    score = 0.0
    if ok_a and ok_b and ok_c and ok_natoms:
        score = 1.0
    return score


# === block: score_1 (check id='s4') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    pressure_threshold = float(step.get('pressure_threshold', 6.5))
    epsilon = float(step.get('epsilon', 1e-6))
    headers = [h for h in artifact[0].keys()]
    phase_cols = [h for h in headers if h.startswith('H_') and h != 'H_C_carbon']
    pressures = [float(row['pressure_GPa']) for row in artifact]
    total_p = 0
    correct_p = 0
    for row in artifact:
        p = float(row.get('pressure_GPa', 0))
        if p < pressure_threshold - 1e-9:
            continue
        total_p += 1
        try:
            h_c = float(row['H_C_carbon'])
        except (KeyError, ValueError):
            continue
        lowest = True
        for col in phase_cols:
            try:
                h_other = float(row[col])
            except (KeyError, ValueError):
                continue
            if h_c > h_other + epsilon:
                lowest = False
                break
        if lowest:
            correct_p += 1
    if total_p == 0:
        return 0.0
    return correct_p / total_p


# === block: score_2 (check id='s5') ===
def score_2(artifact, step, ctx):
    path = os.path.join('/app/outputs', step.get('output_file', ''))
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        max_imag = float(data.get('max_imaginary_frequency', -999))
        threshold = float(step.get('max_imaginary_threshold', -1.0))
        if max_imag >= threshold:
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_3 (check id='s6') ===
def score_3(artifact, step, ctx):
    try:
        text = artifact.strip() if isinstance(artifact, str) else ''
        val = float(text.split()[0])
        target = float(step.get('target', 4.38))
        tol = float(step.get('tolerance', 0.2))
        if abs(val - target) <= tol:
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_4 (check id='s7') ===
def score_4(artifact, step, ctx):
    try:
        text = artifact.strip() if isinstance(artifact, str) else ''
        val = float(text.split()[0])
        target = float(step.get('target', 427.8))
        tol = float(step.get('tolerance', 10.0))
        if abs(val - target) <= tol:
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_5 (check id='s8') ===
def score_5(artifact, step, ctx):
    try:
        text = artifact.strip() if isinstance(artifact, str) else ''
        val = float(text.split()[0])
        target = float(step.get('target', 56.0))
        tol = float(step.get('tolerance', 5.0))
        if abs(val - target) <= tol:
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_6 (check id='s9') ===
def score_6(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = []
    for r in artifact:
        try:
            tth = float(r.get('two_theta_deg', 0))
            intens = float(r.get('intensity_arb', 0))
            rows.append((tth, intens))
        except (ValueError, TypeError):
            continue
    if not rows:
        return 0.0
    rows.sort(key=lambda x: x[0])
    max_intens = max(intens for _, intens in rows)
    if max_intens <= 0:
        return 0.0
    threshold = 0.1 * max_intens
    # Find peaks: local maxima above threshold
    peaks = []
    for i in range(1, len(rows)-1):
        if rows[i][1] > rows[i-1][1] and rows[i][1] > rows[i+1][1] and rows[i][1] >= threshold:
            peaks.append(rows[i][0])
    target_peaks = step.get('target_peaks', [8.5, 16.0, 17.0])
    tolerance = float(step.get('tolerance', 0.5))
    matched = 0
    for tp in target_peaks:
        found = any(abs(p - tp) <= tolerance for p in peaks)
        if found:
            matched += 1
    if not target_peaks:
        return 1.0
    return matched / len(target_peaks)


# === block: score_7 (check id='s10') ===
def score_7(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = []
    for r in artifact:
        try:
            rs = float(r.get('raman_shift_cm^{-1}', 0))
            intens = float(r.get('intensity_arb', 0))
            rows.append((rs, intens))
        except (ValueError, TypeError):
            continue
    if not rows:
        return 0.0
    rows.sort(key=lambda x: x[0])
    max_intens = max(intens for _, intens in rows)
    if max_intens <= 0:
        return 0.0
    threshold = 0.1 * max_intens
    peaks = []
    for i in range(1, len(rows)-1):
        if rows[i][1] > rows[i-1][1] and rows[i][1] > rows[i+1][1] and rows[i][1] >= threshold:
            peaks.append(rows[i][0])
    target_peaks = step.get('target_peaks', [950, 1200, 1300])
    tolerance = float(step.get('tolerance', 30))
    matched = 0
    for tp in target_peaks:
        found = any(abs(p - tp) <= tolerance for p in peaks)
        if found:
            matched += 1
    if not target_peaks:
        return 1.0
    return matched / len(target_peaks)


_SCORERS = {
    's2': score_0,
    's4': score_1,
    's5': score_2,
    's6': score_3,
    's7': score_4,
    's8': score_5,
    's9': score_6,
    's10': score_7,
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
