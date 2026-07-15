import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='force_constants_check') ===
def score_0(artifact, step, ctx):
    target = step["params"]["target_ratio"]
    tol = step["params"]["tolerance"]
    for row in artifact:
        if row.get("parameter_name") == "D_D_1nn":
            ratio = float(row["ratio"])
            if abs(ratio - target) <= tol:
                return 1.0
            else:
                return 0.0
    return 0.0


# === block: score_1 (check id='zone_boundary_acoustic') ===
def score_1(artifact, step, ctx):
    energies = np.array([float(r["energy_meV"]) for r in artifact])
    intensities = np.array([float(r["intensity"]) for r in artifact])
    lo, hi = step["params"]["energy_range"]
    mask = (energies >= lo) & (energies <= hi)
    if not np.any(mask):
        return 0.0
    idx = np.argmax(intensities[mask])
    peak_energy = energies[mask][idx]
    target = step["params"]["peak_energy_target"]
    delta = step["params"]["delta"]
    dist = abs(peak_energy - target)
    if dist <= delta:
        return 1.0
    elif dist <= 2*delta:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='zone_boundary_optical_broad') ===
def score_2(artifact, step, ctx):
    energies = np.array([float(r["energy_meV"]) for r in artifact])
    intensities = np.array([float(r["intensity"]) for r in artifact])
    lo, hi = step["params"]["energy_range"]
    mask = (energies >= lo) & (energies <= hi)
    if not np.any(mask):
        return 0.0
    e_sel = energies[mask]
    i_sel = intensities[mask]
    mean = np.average(e_sel, weights=i_sel)
    std = np.sqrt(np.average((e_sel - mean)**2, weights=i_sel))
    min_std = step["params"]["min_std"]
    if std >= min_std:
        return 1.0
    elif std >= min_std * 0.625:
        return 0.5
    else:
        return 0.0


# === block: score_3 (check id='zone_center_peak') ===
def score_3(artifact, step, ctx):
    energies = np.array([float(r["energy_meV"]) for r in artifact])
    intensities = np.array([float(r["intensity"]) for r in artifact])
    lo, hi = step["params"]["peak_range"]
    mask = (energies >= lo) & (energies <= hi)
    if not np.any(mask):
        return 0.0
    i_sel = intensities[mask]
    e_sel = energies[mask]
    max_idx = np.argmax(i_sel)
    peak_energy = e_sel[max_idx]
    peak_val = i_sel[max_idx]
    half_max = peak_val / 2.0
    left_idx = np.where((e_sel <= peak_energy) & (i_sel >= half_max))[0]
    right_idx = np.where((e_sel >= peak_energy) & (i_sel >= half_max))[0]
    if len(left_idx) == 0 or len(right_idx) == 0:
        return 0.0
    fwhm = e_sel[right_idx[-1]] - e_sel[left_idx[0]]
    fwhm_min = step["params"]["fwhm_min"]
    fwhm_max = step["params"]["fwhm_max"]
    if fwhm_min <= fwhm <= fwhm_max:
        return 1.0
    elif (fwhm_min - 1.0) <= fwhm <= (fwhm_max + 2.0):
        return 0.5
    else:
        return 0.0


# === block: score_4 (check id='longitudinal_broad') ===
def score_4(artifact, step, ctx):
    energies = np.array([float(r["energy_meV"]) for r in artifact])
    intensities = np.array([float(r["intensity"]) for r in artifact])
    lo, hi = step["params"]["energy_range"]
    mask = (energies >= lo) & (energies <= hi)
    if not np.any(mask):
        return 0.0
    e_sel = energies[mask]
    i_sel = intensities[mask]
    mean = np.average(e_sel, weights=i_sel)
    std = np.sqrt(np.average((e_sel - mean)**2, weights=i_sel))
    min_std = step["params"]["min_std"]
    if std >= min_std:
        return 1.0
    elif std >= min_std * 0.7:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'force_constants_check': score_0,
    'zone_boundary_acoustic': score_1,
    'zone_boundary_optical_broad': score_2,
    'zone_center_peak': score_3,
    'longitudinal_broad': score_4,
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
