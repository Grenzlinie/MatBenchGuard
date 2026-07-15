import os
import json
import csv

# === author imports / helpers ===
import math
import csv
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


# === block: score_0 (check id='static_properties_shape') ===
def score_0(artifact, step, ctx):
    data = artifact
    step_cfg = step  # step dict from grading_spec
    expected_count = step_cfg.get("expected_count", 5)
    count_tol = step_cfg.get("entry_count_tolerance", 0)
    if not isinstance(data, list) or not (expected_count - count_tol <= len(data) <= expected_count + count_tol):
        return 0.0
    required_keys = step_cfg.get("required_keys", ["strain", "Eg_HSE06", "epsilon1x0", "epsilon1y0"])
    expected_strains = set(step_cfg.get("expected_strains", ["-7%", "-3%", "0%", "3%", "7%"]))
    for entry in data:
        if not isinstance(entry, dict):
            return 0.0
        if set(entry.keys()) != set(required_keys):
            return 0.0
        if entry["strain"] not in expected_strains:
            return 0.0
        for k in ["Eg_HSE06", "epsilon1x0", "epsilon1y0"]:
            if not isinstance(entry[k], (int, float)):
                return 0.0
            if entry[k] < 0:
                return 0.0
    return 1.0


# === block: score_1 (check id='band_gap_agreement') ===
def score_1(artifact, step, ctx):
    targets = {
        "-7%": (0.331, 0.15),
        "-3%": (1.087, 0.15),
        "0%":  (1.509, 0.15),
        "3%":  (1.845, 0.15),
        "7%":  (1.5375, 0.15)
    }
    score = 0.0
    for entry in artifact:
        strain = entry["strain"]
        if strain in targets:
            val = entry["Eg_HSE06"]
            tval, tol = targets[strain]
            if abs(val - tval) <= tol:
                score += 1.0
    return score / 5.0


# === block: score_2 (check id='epsilon2_shape') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 100:
        return 0.0
    try:
        energies = [float(r["energy_eV"]) for r in rows]
        eps_x = [float(r["epsilon2_x"]) for r in rows]
        eps_y = [float(r["epsilon2_y"]) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    if any(energies[i] >= energies[i+1] for i in range(len(energies)-1)):
        return 0.0
    if energies[0] < 0 or energies[-1] < 11.9:
        return 0.0
    if any(v < 0 for v in eps_x) or any(v < 0 for v in eps_y):
        return 0.0
    return 1.0


# === block: score_3 (check id='epsilon2_recompute_static') ===
def score_3(artifact, step, ctx):
    rows = artifact
    energies = [float(r["energy_eV"]) for r in rows]
    eps_x = [float(r["epsilon2_x"]) for r in rows]
    eps_y = [float(r["epsilon2_y"]) for r in rows]
    def kk_static(e_vals, e2_vals):
        integ = 0.0
        for i in range(1, len(e_vals)):
            if e_vals[i] > 0:
                f_i = e2_vals[i] / e_vals[i]
                f_prev = e2_vals[i-1] / e_vals[i-1] if e_vals[i-1] > 0 else 0.0
                integ += (f_i + f_prev) * (e_vals[i] - e_vals[i-1]) / 2.0
        return 1.0 + (2.0 / math.pi) * integ
    eps1x = kk_static(energies, eps_x)
    eps1y = kk_static(energies, eps_y)
    # store for consistency check (if needed later)
    ctx["eps1x_recomp"] = eps1x
    ctx["eps1y_recomp"] = eps1y
    score_x = 1.0 if abs(eps1x - 3.41) <= 0.2 else 0.0
    score_y = 1.0 if abs(eps1y - 3.13) <= 0.2 else 0.0
    return (score_x + score_y) / 2.0


# === block: score_4 (check id='epsilon2_peak_positions') ===
def score_4(artifact, step, ctx):
    rows = artifact
    energies = [float(r["energy_eV"]) for r in rows]
    eps_x = [float(r["epsilon2_x"]) for r in rows]
    eps_y = [float(r["epsilon2_y"]) for r in rows]
    def detect_peaks(e_vals, e2_vals):
        peaks = []
        for i in range(1, len(e2_vals)-1):
            if e2_vals[i] > e2_vals[i-1] and e2_vals[i] > e2_vals[i+1]:
                peaks.append(e_vals[i])
        return peaks
    peaks_x = detect_peaks(energies, eps_x)
    peaks_y = detect_peaks(energies, eps_y)
    targets = [(2.05, 0.2), (5.51, 0.2), (5.94, 0.2)]
    matched_x = sum(1 for tv, tol in targets if any(abs(p - tv) <= tol for p in peaks_x))
    matched_y = sum(1 for tv, tol in targets if any(abs(p - tv) <= tol for p in peaks_y))
    return (matched_x + matched_y) / 6.0


# === block: score_5 (check id='static_dielectric_consistency') ===
def score_5(artifact, step, ctx):
    # this scorer re-computes static epsilon from CSV and compares with JSON values
    csv_path = os.path.join("/app/outputs", "epsilon2_0pct.csv")
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    energies = [float(r["energy_eV"]) for r in rows]
    eps_x = [float(r["epsilon2_x"]) for r in rows]
    eps_y = [float(r["epsilon2_y"]) for r in rows]
    def kk_static(e_vals, e2_vals):
        integ = 0.0
        for i in range(1, len(e_vals)):
            if e_vals[i] > 0:
                f_i = e2_vals[i] / e_vals[i]
                f_prev = e2_vals[i-1] / e_vals[i-1] if e_vals[i-1] > 0 else 0.0
                integ += (f_i + f_prev) * (e_vals[i] - e_vals[i-1]) / 2.0
        return 1.0 + (2.0 / math.pi) * integ
    eps1x_recomp = kk_static(energies, eps_x)
    eps1y_recomp = kk_static(energies, eps_y)
    # find 0% strain entry in static_properties.json
    for entry in artifact:
        if entry["strain"] == "0%":
            diff_x = abs(entry["epsilon1x0"] - eps1x_recomp)
            diff_y = abs(entry["epsilon1y0"] - eps1y_recomp)
            if diff_x <= 0.1 and diff_y <= 0.1:
                return 1.0
            break
    return 0.0


_SCORERS = {
    'static_properties_shape': score_0,
    'band_gap_agreement': score_1,
    'epsilon2_shape': score_2,
    'epsilon2_recompute_static': score_3,
    'epsilon2_peak_positions': score_4,
    'static_dielectric_consistency': score_5,
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
