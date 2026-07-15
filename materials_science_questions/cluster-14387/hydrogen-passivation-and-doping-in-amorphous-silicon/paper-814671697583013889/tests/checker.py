import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy", "scipy", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
import numpy as np
from scipy import signal
import csv
import json
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
    systems = {
        "slab": "dos_slab.csv",
        "isolated_H": "dos_isolated_H.csv",
        "two_H": "dos_two_H.csv",
        "three_H": "dos_three_H.csv"
    }
    steps = spec.get("steps", [])
    step_map = {}
    for step in steps:
        out = step.get("output_file", "")
        if out in systems.values():
            step_map[out] = step

    dos_features = {}

    def parse_dos_csv(path):
        energies = []
        dos_vals = []
        with open(path, newline='') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) >= 2:
                    try:
                        energies.append(float(parts[0].strip()))
                        dos_vals.append(float(parts[1].strip()))
                    except ValueError:
                        continue
        return np.array(energies), np.array(dos_vals)

    for sys, fname in systems.items():
        path = os.path.join(outputs_dir, fname)
        try:
            energies, dos_arr = parse_dos_csv(path)
            if len(energies) == 0:
                raise ValueError("empty")
        except Exception:
            dos_features[sys] = {"has_gap_states": False, "gap_states_energies_eV": [], "gap_clean": False}
            continue

        step = step_map.get(fname, {})
        params = step.get("params", {})
        gap_range = params.get("gap_energy_range", [-2, 2])
        max_gap_dos_frac = params.get("max_allowed_gap_dos_fraction", 0.01)

        global_max = np.max(dos_arr) if len(dos_arr) > 0 else 1.0
        mask = (energies >= gap_range[0]) & (energies <= gap_range[1])
        dos_gap = dos_arr[mask]
        energies_gap = energies[mask]

        if len(dos_gap) == 0:
            dos_features[sys] = {"has_gap_states": False, "gap_states_energies_eV": [], "gap_clean": False}
            continue

        threshold = 0.05 * global_max if global_max > 0 else 0.0
        peaks_idx, _ = signal.find_peaks(dos_gap, height=threshold)
        peak_energies = list(energies_gap[peaks_idx])
        has_states = len(peak_energies) > 0
        max_gap = np.max(dos_gap)
        gap_clean = (not has_states) and (max_gap <= max_gap_dos_frac * global_max)
        dos_features[sys] = {
            "has_gap_states": has_states,
            "gap_states_energies_eV": peak_energies,
            "gap_clean": gap_clean
        }

    return {"dos_features": dos_features}


# === block: score_0 (check id='check_slab_dos') ===
def score_0(artifact, step, ctx):
    import os

    def parse_dos_csv(path):
        energies = []
        dos_vals = []
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) >= 2:
                    try:
                        energies.append(float(parts[0].strip()))
                        dos_vals.append(float(parts[1].strip()))
                    except ValueError:
                        continue
        return energies, dos_vals

    def local_maxima_indices(arr):
        """Return indices of local maxima (strict > neighbors)."""
        n = len(arr)
        idx = []
        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                idx.append(i)
        return idx

    params = step.get("params", {})
    sys = params.get("system")
    if not sys:
        return 0.0

    # Directly read the DOS CSV file
    out_file = step.get("output_file", "dos_slab.csv")
    path = os.path.join("/app/outputs", out_file)
    try:
        energies, dos_arr = parse_dos_csv(path)
        if len(energies) == 0:
            return 0.0
    except Exception:
        return 0.0

    expected_has = params.get("expected_has_gap_states", False)
    gap_range = params.get("gap_energy_range", [-2, 2])
    max_gap_dos_frac = params.get("max_allowed_gap_dos_fraction", 0.01)
    tolerance = params.get("peak_tolerance", 0.2)

    # Find global max for thresholding
    global_max = max(dos_arr) if dos_arr else 1.0

    # Extract gap region
    masked_energies = []
    masked_dos = []
    for e, d in zip(energies, dos_arr):
        if gap_range[0] <= e <= gap_range[1]:
            masked_energies.append(e)
            masked_dos.append(d)

    if len(masked_dos) == 0:
        # no data in gap -> clean
        if not expected_has:
            return 1.0
        else:
            return 0.0

    threshold = 0.05 * global_max
    peak_indices = local_maxima_indices(masked_dos)
    # Filter peaks above threshold
    peak_energies = []
    for i in peak_indices:
        if masked_dos[i] >= threshold:
            peak_energies.append(masked_energies[i])

    has_states = len(peak_energies) > 0
    max_gap_dos = max(masked_dos)
    # Gap is considered clean if no significant peaks and low baseline
    gap_clean = (not has_states) and (max_gap_dos <= max_gap_dos_frac * global_max)

    if not expected_has:
        # The paper expects no gap states
        return 1.0 if gap_clean else 0.0
    else:
        expected_peaks = params.get("expected_peak_energies", [])
        if not has_states:
            return 0.0
        matched = 0
        for exp in expected_peaks:
            for p in peak_energies:
                if abs(p - exp) <= tolerance:
                    matched += 1
                    break
        score = matched / len(expected_peaks) if expected_peaks else 1.0
        return float(min(1.0, score))


# === block: score_1 (check id='check_isolated_H_dos') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    sys = params.get("system")
    if not sys:
        return 0.0
    ref = ctx.get("dos_features", {}).get(sys)
    if ref is None:
        return 0.0
    expected_has = params.get("expected_has_gap_states", False)
    if not expected_has:
        return 1.0 if ref.get("gap_clean", False) else 0.0
    expected_peaks = params.get("expected_peak_energies", [])
    tolerance = params.get("peak_tolerance", 0.0)
    if not ref["has_gap_states"]:
        return 0.0
    peaks = ref["gap_states_energies_eV"]
    matched = sum(1 for exp in expected_peaks if any(abs(p - exp) <= tolerance for p in peaks))
    score = matched / len(expected_peaks) if expected_peaks else 1.0
    return float(min(1.0, score))


# === block: score_2 (check id='check_two_H_dos') ===
def score_2(artifact, step, ctx):
    params = step.get("params", {})
    sys = params.get("system")
    if not sys:
        return 0.0
    ref = ctx.get("dos_features", {}).get(sys)
    if ref is None:
        return 0.0
    expected_has = params.get("expected_has_gap_states", False)
    if not expected_has:
        return 1.0 if ref.get("gap_clean", False) else 0.0
    expected_peaks = params.get("expected_peak_energies", [])
    tolerance = params.get("peak_tolerance", 0.0)
    if not ref["has_gap_states"]:
        return 0.0
    peaks = ref["gap_states_energies_eV"]
    matched = sum(1 for exp in expected_peaks if any(abs(p - exp) <= tolerance for p in peaks))
    score = matched / len(expected_peaks) if expected_peaks else 1.0
    return float(min(1.0, score))


# === block: score_3 (check id='check_three_H_dos') ===
def score_3(artifact, step, ctx):
    params = step.get("params", {})
    sys = params.get("system")
    if not sys:
        return 0.0
    ref = ctx.get("dos_features", {}).get(sys)
    if ref is None:
        return 0.0
    expected_has = params.get("expected_has_gap_states", False)
    if not expected_has:
        return 1.0 if ref.get("gap_clean", False) else 0.0
    expected_peaks = params.get("expected_peak_energies", [])
    tolerance = params.get("peak_tolerance", 0.0)
    if not ref["has_gap_states"]:
        return 0.0
    peaks = ref["gap_states_energies_eV"]
    matched = sum(1 for exp in expected_peaks if any(abs(p - exp) <= tolerance for p in peaks))
    score = matched / len(expected_peaks) if expected_peaks else 1.0
    return float(min(1.0, score))


# === block: score_4 (check id='check_summary') ===
def score_4(artifact, step, ctx):
    dos_features = ctx.get("dos_features", {})
    if not isinstance(artifact, dict):
        return 0.0
    systems = ["slab", "isolated_H", "two_H", "three_H"]
    score_sum = 0.0
    for sys in systems:
        if sys not in artifact or sys not in dos_features:
            continue
        art = artifact[sys]
        ref = dos_features[sys]
        # check has_gap_states match
        has_match = (art.get("has_gap_states", None) == ref["has_gap_states"])
        if not has_match:
            continue
        # check energies
        art_energies = art.get("gap_states_energies_eV", [])
        ref_energies = ref.get("gap_states_energies_eV", [])
        tol = 0.15
        energy_ok = True
        if ref["has_gap_states"]:
            if len(art_energies) != len(ref_energies):
                energy_ok = False
            else:
                art_sorted = sorted(art_energies)
                ref_sorted = sorted(ref_energies)
                for a, b in zip(art_sorted, ref_sorted):
                    if abs(a - b) > tol:
                        energy_ok = False
                        break
        else:
            if art_energies and len(art_energies) > 0:
                energy_ok = False
        if energy_ok:
            score_sum += 1.0
    return score_sum / 4.0


_SCORERS = {
    'check_slab_dos': score_0,
    'check_isolated_H_dos': score_1,
    'check_two_H_dos': score_2,
    'check_three_H_dos': score_3,
    'check_summary': score_4,
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
