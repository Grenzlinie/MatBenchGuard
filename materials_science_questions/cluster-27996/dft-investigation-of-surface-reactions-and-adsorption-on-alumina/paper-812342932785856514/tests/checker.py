import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.interpolate import UnivariateSpline
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


# === block: score_0 (check id='scan_analysis') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from scipy.interpolate import UnivariateSpline

    data = artifact
    angles = np.array([float(row["out_of_plane_angle"]) for row in data])
    energies = np.array([float(row["relative_energy_kJmol"]) for row in data])

    # sort by angle for proper spline
    idx_order = np.argsort(angles)
    angles = angles[idx_order]
    energies = energies[idx_order]

    if len(angles) < 5:
        return 0.0

    try:
        spl = UnivariateSpline(angles, energies, s=0)
    except Exception:
        return 0.0

    # find derivative zero crossings from negative to positive (local minima)
    fprime = spl.derivative(1)
    xs = np.linspace(angles[0], angles[-1], 1000)
    dvals = fprime(xs)
    signs = np.sign(dvals)
    cross = ((signs[:-1] < 0) & (signs[1:] > 0))
    minima_xs = xs[:-1][cross]

    if len(minima_xs) < 2:
        return 0.0

    # evaluate energy at each candidate minimum
    minima_energies = [spl(x) for x in minima_xs]
    minima_angles = [x for x in minima_xs]

    # sort by energy ascending
    pairs = sorted(zip(minima_energies, minima_angles), key=lambda p: p[0])
    global_energy, global_angle = pairs[0]
    meta_energy, meta_angle = pairs[1]

    gold_min_angles = step.get("gold_minima_angles", [35.7, -39.5])
    tol_angle = step.get("tolerance_angle_deg", 3.0)
    global_correct = abs(global_angle - gold_min_angles[0]) <= tol_angle
    meta_correct = abs(meta_angle - gold_min_angles[1]) <= tol_angle
    minima_score = 0.4 if (global_correct and meta_correct) else 0.0

    gold_ediff = step.get("gold_energy_diff_kjmol", 6.30)
    tol_ediff = step.get("tolerance_energy_diff_kjmol", 2.0)
    ediff = meta_energy - global_energy
    ediff_correct = abs(ediff - gold_ediff) <= tol_ediff
    ediff_score = 0.6 if ediff_correct else 0.0

    return minima_score + ediff_score


# === block: score_1 (check id='properties_comparison') ===
def score_1(artifact, step, ctx):
    data = artifact
    acid_sites = data.get("acid_sites", [])
    if not acid_sites:
        return 0.0

    gold_values = {
        "O1": {"deprotonation_energy_kJmol": 1178.7, "oh_stretch_frequency_cm1": 3578, "ammonia_adsorption_energy_kJmol": 149.3},
        "O2": {"deprotonation_energy_kJmol": 1180.9, "oh_stretch_frequency_cm1": 3541, "ammonia_adsorption_energy_kJmol": 142.9},
        "O3": {"deprotonation_energy_kJmol": 1174.6, "oh_stretch_frequency_cm1": 3514, "ammonia_adsorption_energy_kJmol": 144.5},
        "O4": {"deprotonation_energy_kJmol": 1179.1, "oh_stretch_frequency_cm1": 3532, "ammonia_adsorption_energy_kJmol": 135.7},
    }
    tolerances = {
        "deprotonation_energy_kJmol": 20.0,
        "oh_stretch_frequency_cm1": 50.0,
        "ammonia_adsorption_energy_kJmol": 15.0,
    }

    total = 0
    count = 0
    for site_obj in acid_sites:
        site = site_obj.get("site")
        if site not in gold_values:
            continue
        for key, gold_val in gold_values[site].items():
            agent_val = site_obj.get(key)
            if agent_val is None:
                continue
            tol = tolerances[key]
            if abs(agent_val - gold_val) <= tol:
                total += 1
            count += 1

    if count == 0:
        return 0.0
    return total / count


_SCORERS = {
    'scan_analysis': score_0,
    'properties_comparison': score_1,
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
