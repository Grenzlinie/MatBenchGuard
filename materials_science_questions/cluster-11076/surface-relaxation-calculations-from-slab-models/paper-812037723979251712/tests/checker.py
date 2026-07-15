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


# === block: score_0 (check id='step_04_mag_moments') ===
def score_0(artifact, step, ctx):
    gold = step["params"]["gold_table"]
    tol = step["params"]["tolerance_abs_muB"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    # index rows by (termination, a, atom, layer) ignoring string/float representation
    agent_rows = {}
    for row in artifact:
        key = (str(row.get("termination","")).strip(),
               str(row.get("lattice_constant_A","")).strip(),
               str(row.get("atom","")).strip(),
               str(row.get("layer","")).strip())
        try:
            val = float(row.get("magnetic_moment_muB", math.nan))
        except (ValueError, TypeError):
            val = math.nan
        agent_rows[key] = val

    num_match = 0
    total = len(gold)
    for g in gold:
        key = (g["termination"], str(g["lattice_constant_A"]), g["atom"], g["layer"])
        gold_val = g["magnetic_moment_muB"]
        agent_val = agent_rows.get(key, math.nan)
        if math.isnan(agent_val):
            continue
        if abs(agent_val - gold_val) <= tol:
            num_match += 1
    return num_match / total if total > 0 else 0.0


# === block: score_1 (check id='step_05_dos_cr_azb') ===
def score_1(artifact, step, ctx):
    params = step["params"]
    threshold = params["dos_threshold"]
    sigma = params.get("sigma_smooth_eV", 0.05)
    target_gap = params["target_minority_gap_width_eV"]
    tol_gap = params["gap_tolerance_eV"]
    target_exch = params["exchange_splitting_target_eV"]
    tol_exch = params["exchange_tolerance_eV"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    energies = []
    dos_down = []
    dos_up = []
    for row in artifact:
        try:
            e = float(row["energy_eV"])
            du = float(row["dos_up"])
            dd = float(row["dos_down"])
        except (ValueError, KeyError):
            continue
        energies.append(e)
        dos_up.append(du)
        dos_down.append(dd)
    n = len(energies)
    if n < 2:
        return 0.0
    # smooth with Gaussian convolution
    def gaussian_smooth(x, y, sigma):
        n = len(x)
        if n == 0:
            return []
        if sigma <= 0:
            return y[:]
        # approximate convolution over ±3 sigma
        out = [0.0]*n
        dx = (x[-1]-x[0])/(n-1) if n>1 else 1.0
        kernel_radius = int(math.ceil(3*sigma/dx)) + 1
        for i in range(n):
            num = 0.0
            den = 0.0
            for j in range(max(0,i-kernel_radius), min(n,i+kernel_radius+1)):
                w = math.exp(-((x[i]-x[j])**2)/(2*sigma*sigma))
                num += y[j]*w
                den += w
            out[i] = num / den if den > 0 else y[i]
        return out
    dos_down_smooth = gaussian_smooth(energies, dos_down, sigma)
    # find largest interval with dos_down < threshold
    best_start = best_end = 0
    best_len = 0.0
    curr_start = None
    for i in range(n):
        if dos_down_smooth[i] < threshold:
            if curr_start is None:
                curr_start = i
        else:
            if curr_start is not None:
                curr_end = i-1
                L = energies[curr_end] - energies[curr_start]
                if L > best_len:
                    best_len = L
                    best_start = curr_start
                    best_end = curr_end
                curr_start = None
    if curr_start is not None:
        L = energies[-1] - energies[curr_start]
        if L > best_len:
            best_len = L
            best_start = curr_start
            best_end = n-1
    if best_len == 0:
        return 0.0
    # compute gap width and surface state check
    gap_width = best_len
    within_interval_max = max(dos_down_smooth[best_start:best_end+1], default=0.0)
    gap_ok = (abs(gap_width - target_gap) <= tol_gap) and (within_interval_max < threshold)
    # exchange splitting
    def find_peak(x, y, indices, prefer_highest=False):
        best_idx = -1
        best_y = -float('inf')
        for i in indices:
            if i < 0 or i >= n:
                continue
            if y[i] > best_y:
                best_y = y[i]
                best_idx = i
        return best_idx, best_y
    # majority peak below EF (E<0)
    majority_indices = [i for i, e in enumerate(energies) if e < 0.0]
    majority_peak_idx, _ = find_peak(energies, dos_up, majority_indices, prefer_highest=True)
    # minority peak above gap: energies above gap upper edge (energies[best_end])
    minority_indices = [i for i, e in enumerate(energies) if e > energies[best_end]]
    minority_peak_idx, _ = find_peak(energies, dos_down, minority_indices, prefer_highest=True)
    exch_ok = False
    if majority_peak_idx >= 0 and minority_peak_idx >= 0:
        exch_splitting = energies[minority_peak_idx] - energies[majority_peak_idx]
        if abs(exch_splitting - target_exch) <= tol_exch:
            exch_ok = True
    # combine sub-scores equally
    sub_score = 0.0
    if gap_ok:
        sub_score += 0.5
    if exch_ok:
        sub_score += 0.5
    return sub_score


# === block: score_2 (check id='step_06_dos_cr_ainp') ===
def score_2(artifact, step, ctx):
    # identical logic to step_05, but on dos_cr_term_aInP.csv
    params = step["params"]
    threshold = params["dos_threshold"]
    sigma = params.get("sigma_smooth_eV", 0.05)
    target_gap = params["target_minority_gap_width_eV"]
    tol_gap = params["gap_tolerance_eV"]
    target_exch = params["exchange_splitting_target_eV"]
    tol_exch = params["exchange_tolerance_eV"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    energies = []
    dos_down = []
    dos_up = []
    for row in artifact:
        try:
            e = float(row["energy_eV"])
            du = float(row["dos_up"])
            dd = float(row["dos_down"])
        except (ValueError, KeyError):
            continue
        energies.append(e)
        dos_up.append(du)
        dos_down.append(dd)
    n = len(energies)
    if n < 2:
        return 0.0
    def gaussian_smooth(x, y, sigma):
        n = len(x)
        if n == 0:
            return []
        if sigma <= 0:
            return y[:]
        dx = (x[-1]-x[0])/(n-1) if n>1 else 1.0
        kernel_radius = int(math.ceil(3*sigma/dx)) + 1
        out = [0.0]*n
        for i in range(n):
            num = 0.0
            den = 0.0
            for j in range(max(0,i-kernel_radius), min(n,i+kernel_radius+1)):
                w = math.exp(-((x[i]-x[j])**2)/(2*sigma*sigma))
                num += y[j]*w
                den += w
            out[i] = num / den if den > 0 else y[i]
        return out
    dos_down_smooth = gaussian_smooth(energies, dos_down, sigma)
    best_start = best_end = 0
    best_len = 0.0
    curr_start = None
    for i in range(n):
        if dos_down_smooth[i] < threshold:
            if curr_start is None:
                curr_start = i
        else:
            if curr_start is not None:
                curr_end = i-1
                L = energies[curr_end] - energies[curr_start]
                if L > best_len:
                    best_len = L
                    best_start = curr_start
                    best_end = curr_end
                curr_start = None
    if curr_start is not None:
        L = energies[-1] - energies[curr_start]
        if L > best_len:
            best_len = L
            best_start = curr_start
            best_end = n-1
    if best_len == 0:
        return 0.0
    gap_width = best_len
    within_interval_max = max(dos_down_smooth[best_start:best_end+1], default=0.0)
    gap_ok = (abs(gap_width - target_gap) <= tol_gap) and (within_interval_max < threshold)
    def find_peak(x, y, indices, prefer_highest=False):
        best_idx = -1
        best_y = -float('inf')
        for i in indices:
            if i < 0 or i >= n:
                continue
            if y[i] > best_y:
                best_y = y[i]
                best_idx = i
        return best_idx, best_y
    majority_indices = [i for i, e in enumerate(energies) if e < 0.0]
    majority_peak_idx, _ = find_peak(energies, dos_up, majority_indices, prefer_highest=True)
    minority_indices = [i for i, e in enumerate(energies) if e > energies[best_end]]
    minority_peak_idx, _ = find_peak(energies, dos_down, minority_indices, prefer_highest=True)
    exch_ok = False
    if majority_peak_idx >= 0 and minority_peak_idx >= 0:
        exch_splitting = energies[minority_peak_idx] - energies[majority_peak_idx]
        if abs(exch_splitting - target_exch) <= tol_exch:
            exch_ok = True
    sub_score = 0.0
    if gap_ok:
        sub_score += 0.5
    if exch_ok:
        sub_score += 0.5
    return sub_score


# === block: score_3 (check id='step_07_dos_p_azb') ===
def score_3(artifact, step, ctx):
    params = step["params"]
    threshold = params["dos_threshold"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    # find the row closest to energy_eV = 0 (Fermi level)
    best_row = None
    best_dist = float('inf')
    for row in artifact:
        try:
            e = float(row["energy_eV"])
            dd = float(row["dos_down"])
        except (ValueError, KeyError):
            continue
        d = abs(e - 0.0)
        if d < best_dist:
            best_dist = d
            best_row = (e, dd)
    if best_row is None:
        return 0.0
    _, dd_at_ef = best_row
    # metallic if dos_down > threshold
    return 1.0 if dd_at_ef > threshold else 0.0


# === block: score_4 (check id='step_08_dos_p_ainp') ===
def score_4(artifact, step, ctx):
    params = step["params"]
    threshold = params["dos_threshold"]
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    best_row = None
    best_dist = float('inf')
    for row in artifact:
        try:
            e = float(row["energy_eV"])
            dd = float(row["dos_down"])
        except (ValueError, KeyError):
            continue
        d = abs(e - 0.0)
        if d < best_dist:
            best_dist = d
            best_row = (e, dd)
    if best_row is None:
        return 0.0
    _, dd_at_ef = best_row
    return 1.0 if dd_at_ef > threshold else 0.0


_SCORERS = {
    'step_04_mag_moments': score_0,
    'step_05_dos_cr_azb': score_1,
    'step_06_dos_cr_ainp': score_2,
    'step_07_dos_p_azb': score_3,
    'step_08_dos_p_ainp': score_4,
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
