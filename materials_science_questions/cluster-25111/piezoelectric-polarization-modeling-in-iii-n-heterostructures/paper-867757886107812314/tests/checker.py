import os
import json
import csv

# === author imports / helpers ===
import math
import bisect


def find_peaks_simple(energies, intensities, prominence_ratio=0.01):
    """Return list of (energy, intensity) for local maxima that are at least prominence_ratio * max."""
    n = len(intensities)
    max_val = max(intensities) if intensities else 0.0
    threshold = max_val * prominence_ratio
    peaks = []
    for i in range(1, n - 1):
        if intensities[i] > intensities[i-1] and intensities[i] > intensities[i+1] and intensities[i] >= threshold:
            peaks.append((energies[i], intensities[i]))
    return peaks


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    fields = step.get('fields', [])
    expected = step.get('expected', {})
    tol = float(step.get('tolerance', 0.0))
    n = len(fields)
    if n == 0:
        return 1.0
    score = 0.0
    for f in fields:
        val = artifact.get(f)
        if val is not None and isinstance(val, (int, float)):
            ref = expected.get(f)
            if ref is not None and abs(val - ref) <= tol:
                score += 1.0 / n
    return score


# === block: score_1 (check id='step_04') ===
def score_1(artifact, step, ctx):
    data = artifact  # list of dict-like rows from CSV
    energy_col = step.get('energy_column', 'energy(meV)')
    dp_col = step.get('dp_only_column', 'DOS_DP_only')
    e_ref = float(step.get('electron_peak_energy', -108))
    h_ref = float(step.get('hole_peak_energy', 24))
    tol = float(step.get('peak_tolerance', 20.0))

    energies = []
    dp_vals = []
    for row in data:
        try:
            e = float(row[energy_col])
            d = float(row[dp_col])
            energies.append(e)
            dp_vals.append(d)
        except (ValueError, KeyError):
            continue

    if not energies:
        return 0.0

    # Simple peak detection on dp_vals (may be zero elsewhere, fine)
    # We'll find the maxima in separate energy ranges: negative and positive
    # For electron: energy < 0, find index of max dp_val
    # For hole: energy > 0, similar
    neg_mask = [i for i, e in enumerate(energies) if e < 0 and dp_vals[i] > 0]
    pos_mask = [i for i, e in enumerate(energies) if e > 0 and dp_vals[i] > 0]

    score = 0.0
    electron_ok = False
    if neg_mask:
        idx_max = max(neg_mask, key=lambda i: dp_vals[i])
        peak_e = energies[idx_max]
        if abs(peak_e - e_ref) <= tol:
            electron_ok = True
    else:
        # if no negative energy region, consider failed
        pass

    hole_ok = False
    if pos_mask:
        idx_max = max(pos_mask, key=lambda i: dp_vals[i])
        peak_e = energies[idx_max]
        if abs(peak_e - h_ref) <= tol:
            hole_ok = True

    if electron_ok:
        score += 0.5
    if hole_ok:
        score += 0.5
    return score


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    data = artifact
    energy_col = step.get('energy_column', 'energy(eV)')
    int_col = step.get('intensity_column', 'intensity')
    ref_energies = step.get('reference_energies_eV', [])
    tol = float(step.get('peak_tolerance_eV', 0.005))

    if not ref_energies:
        return 0.0

    energies = []
    intensities = []
    for row in data:
        try:
            e = float(row[energy_col])
            i = float(row[int_col])
            energies.append(e)
            intensities.append(i)
        except (ValueError, KeyError):
            continue

    if len(energies) < 3:
        return 0.0

    # Sort by energy increasing
    es_sorted_idx = sorted(range(len(energies)), key=lambda i: energies[i])
    es_sorted = [energies[i] for i in es_sorted_idx]
    int_sorted = [intensities[i] for i in es_sorted_idx]

    peaks = find_peaks_simple(es_sorted, int_sorted, prominence_ratio=0.02)
    if not peaks:
        return 0.0

    # Match each reference energy to the closest peak within tolerance
    matched = []
    used = [False] * len(peaks)
    for ref in ref_energies:
        best_idx = -1
        best_dist = float('inf')
        for j, (pe, pi) in enumerate(peaks):
            if used[j]:
                continue
            d = abs(pe - ref)
            if d < best_dist:
                best_dist = d
                best_idx = j
        if best_idx != -1 and best_dist <= tol:
            matched.append({'ref': ref, 'peak_e': peaks[best_idx][0], 'peak_i': peaks[best_idx][1], 'idx': best_idx})
            used[best_idx] = True

    pos_score = len(matched) / len(ref_energies)
    return pos_score


_SCORERS = {
    'step_02': score_0,
    'step_04': score_1,
    'step_05': score_2,
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
