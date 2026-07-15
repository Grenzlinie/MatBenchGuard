import os
import json
import csv

# === author imports / helpers ===
import re, os, math
from typing import Any, Dict, List, Optional, Tuple


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


# === block: score_0 (check id='step_01_structure_relaxation') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    a_target = params['a_target']
    b_target = params['b_target']
    tol = params['tolerance']
    ctext = artifact
    match_a = re.search(r'_cell_length_a\s+([\d\.]+)', ctext)
    match_b = re.search(r'_cell_length_b\s+([\d\.]+)', ctext)
    if not match_a or not match_b:
        return 0.0
    a_val = float(match_a.group(1))
    b_val = float(match_b.group(1))
    a_ok = abs(a_val - a_target) <= tol
    b_ok = abs(b_val - b_target) <= tol
    score = (int(a_ok) + int(b_ok)) / 2.0
    return score


# === block: score_1 (check id='step_03_cohesive_energy') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    target = params['target']
    tol = params['tolerance']
    lines = artifact.strip().split('\n')
    try:
        val = float(lines[0].strip())
    except (ValueError, IndexError):
        return 0.0
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step_04_phonon_gamma') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    threshold = params.get('imaginary_threshold', -0.5)
    lines = artifact.strip().split('\n')
    freqs = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            f = float(line)
            freqs.append(f)
        except ValueError:
            return 0.0
    if any(f < threshold for f in freqs):
        return 0.0
    return 1.0


# === block: score_3 (check id='step_05_elastic_constants') ===
def score_3(artifact, step, ctx):
    params = step.get('params', {})
    targets = [params['C11_target'], params['C22_target'], params['C12_target'], params['C66_target']]
    tolerances = [params['C11_tol'], params['C22_tol'], params['C12_tol'], params['C66_tol']]
    line = artifact.strip()
    parts = line.split()
    if len(parts) < 4:
        return 0.0
    vals = []
    for p in parts[:4]:
        try:
            vals.append(float(p))
        except ValueError:
            return 0.0
    count = 0
    for v, tgt, tol in zip(vals, targets, tolerances):
        if abs(v - tgt) <= tol:
            count += 1
    return count / 4.0


# === block: score_4 (check id='step_06_young_modulus') ===
def score_4(artifact, step, ctx):
    params = step.get('params', {})
    Ymin_target = params['Ymin_target']
    Ymax_target = params['Ymax_target']
    Ymin_tol = params['Ymin_tol']
    Ymax_tol = params['Ymax_tol']
    line = artifact.strip()
    parts = line.split()
    if len(parts) < 2:
        return 0.0
    try:
        ymin = float(parts[0])
        ymax = float(parts[1])
    except ValueError:
        return 0.0
    ok_min = abs(ymin - Ymin_target) <= Ymin_tol
    ok_max = abs(ymax - Ymax_target) <= Ymax_tol
    return (int(ok_min) + int(ok_max)) / 2.0


# === block: score_5 (check id='step_07_band_structure') ===
def score_5(artifact, step, ctx):
    params = step.get('params', {})
    eps = params.get('crossing_eps', 0.001)
    lines = artifact.strip().split('\n')
    bands = {}
    # assume each line has at least 5 columns (k_index,kx,ky,kz, then energies)
    for li, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        for bi, tok in enumerate(parts[4:]):
            try:
                e = float(tok)
            except ValueError:
                continue
            if bi not in bands:
                bands[bi] = []
            bands[bi].append(e)
    if not bands:
        return 0.0
    # check if any band has both negative and positive values
    for bi, energies in bands.items():
        if not energies:
            continue
        emin = min(energies)
        emax = max(energies)
        if emin <= -eps and emax >= eps:
            return 1.0
    return 0.0


# === block: score_6 (check id='step_08a_optical_xx') ===
def score_6(artifact, step, ctx):
    params = step.get('params', {})
    energy_range = params['energy_range']
    min_peak = params['min_peak_absorption']
    lines = artifact.strip().split('\n')
    data = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            e = float(parts[0])
            a = float(parts[1])
        except ValueError:
            continue
        data.append((e, a))
    if not data:
        return 0.0
    peak_e = None
    peak_a = -1e9
    for e, a in data:
        if a > peak_a:
            peak_a = a
            peak_e = e
    if peak_e is not None and energy_range[0] <= peak_e <= energy_range[1] and peak_a >= min_peak:
        return 1.0
    return 0.0


# === block: score_7 (check id='step_08b_optical_yy') ===
def score_7(artifact, step, ctx):
    params = step.get('params', {})
    energy_range = params['energy_range']
    min_peak = params['min_peak_absorption']
    lines = artifact.strip().split('\n')
    data = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            e = float(parts[0])
            a = float(parts[1])
        except ValueError:
            continue
        data.append((e, a))
    if not data:
        return 0.0
    peak_e = None
    peak_a = -1e9
    for e, a in data:
        if a > peak_a:
            peak_a = a
            peak_e = e
    if peak_e is not None and energy_range[0] <= peak_e <= energy_range[1] and peak_a >= min_peak:
        return 1.0
    return 0.0


_SCORERS = {
    'step_01_structure_relaxation': score_0,
    'step_03_cohesive_energy': score_1,
    'step_04_phonon_gamma': score_2,
    'step_05_elastic_constants': score_3,
    'step_06_young_modulus': score_4,
    'step_07_band_structure': score_5,
    'step_08a_optical_xx': score_6,
    'step_08b_optical_yy': score_7,
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
