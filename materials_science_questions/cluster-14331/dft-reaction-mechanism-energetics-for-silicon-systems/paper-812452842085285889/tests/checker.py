import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import os
import csv
import json


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
    return {"outputs_dir": outputs_dir, "spec": spec}


# === block: score_0 (check id='sif4_binding_scan') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) < 2:
        return 0.0
    r_vals = []
    e_vals = []
    for row in data:
        try:
            r = float(row["r_Si_F"])
            e = float(row["total_energy"])
            r_vals.append(r)
            e_vals.append(e)
        except (ValueError, KeyError):
            continue
    if not e_vals:
        return 0.0
    min_idx = np.argmin(e_vals)
    r_min = r_vals[min_idx]
    target = step.get("target", 1.635)
    tol = step.get("tolerance", 0.05)
    diff = abs(r_min - target)
    if diff <= tol:
        return 1.0
    # linear decay up to 2*tol
    if diff <= 2*tol:
        return 1.0 - (diff - tol) / tol
    return 0.0


# === block: score_1 (check id='hf2_dissociation') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) < 2:
        return 0.0
    rows_r1 = []
    rows_r2 = []
    energies = []
    for row in data:
        try:
            r1 = float(row["r_FH_Fminus"])
            r2 = float(row["r_Fminus_HF"])
            e = float(row["total_energy"])
            rows_r1.append(r1)
            rows_r2.append(r2)
            energies.append(e)
        except (ValueError, KeyError):
            continue
    if not energies:
        return 0.0
    # find saddle as point where r1 and r2 are closest to equal, and its energy
    r1_arr = np.array(rows_r1)
    r2_arr = np.array(rows_r2)
    e_arr = np.array(energies)
    diff_arr = np.abs(r1_arr - r2_arr)
    # take the point with smallest absolute difference, among those with r1>0.8, r2>0.8
    mask = (r1_arr > 0.8) & (r2_arr > 0.8)
    if not np.any(mask):
        return 0.0
    idx_candidates = np.where(mask)[0]
    saddle_idx = idx_candidates[np.argmin(diff_arr[idx_candidates])]
    saddle_energy = e_arr[saddle_idx]
    saddle_r = (r1_arr[saddle_idx] + r2_arr[saddle_idx]) / 2.0
    # valley: point where one distance near HF equilibrium (0.92) and the other at max
    # find valley as min energy where r1 within 0.02 of 0.92 and r2 >= max(r2)-0.1, or symmetric
    max_r2 = np.max(r2_arr)
    valley_mask = (np.abs(r1_arr - 0.92) < 0.02) & (r2_arr > max_r2 - 0.1)
    if not np.any(valley_mask):
        max_r1 = np.max(r1_arr)
        valley_mask = (np.abs(r2_arr - 0.92) < 0.02) & (r1_arr > max_r1 - 0.1)
    if not np.any(valley_mask):
        return 0.0
    valley_energy = np.min(e_arr[valley_mask])
    barrier = saddle_energy - valley_energy
    if barrier < 0:
        barrier = 0.0  # avoid negative
    barrier_target = step.get("barrier_target", 0.38)
    barrier_tol = step.get("barrier_tolerance", 0.05)
    barrier_diff = abs(barrier - barrier_target)
    barrier_score = 1.0 if barrier_diff <= barrier_tol else max(0.0, 1.0 - (barrier_diff - barrier_tol) / barrier_tol)
    # saddle geometry
    saddle_r_target = step.get("saddle_r_target", 1.20)
    saddle_r_tol = step.get("saddle_r_tolerance", 0.10)
    r_diff = abs(saddle_r - saddle_r_target)
    r_score = 1.0 if r_diff <= saddle_r_tol else max(0.0, 1.0 - (r_diff - saddle_r_tol) / saddle_r_tol)
    return 0.7 * barrier_score + 0.3 * r_score


# === block: score_2 (check id='desorption_without_h') ===
def score_2(artifact, step, ctx):
    data_without = artifact
    ref_file = step.get("reference_file", "desorption_energy_surface_with_Hplus.csv")
    out_dir = ctx["outputs_dir"]
    ref_path = os.path.join(out_dir, ref_file)
    if not os.path.exists(ref_path):
        return 0.0
    with open(ref_path, newline='') as f:
        reader = csv.DictReader(f)
        ref_data = list(reader)
    if not isinstance(ref_data, list) or not ref_data:
        return 0.0
    # build dict for with_h
    with_h_map = {}
    for row in ref_data:
        try:
            r_o = float(row["r_O_Si"])
            r_f = float(row["r_Si_Fminus"])
            e = float(row["total_energy"])
            with_h_map[(r_o, r_f)] = e
        except (ValueError, KeyError):
            continue
    if not with_h_map:
        return 0.0
    tol = step.get("energy_tolerance", 0.1)
    violations = 0
    compared = 0
    for row in data_without:
        try:
            r_o = float(row["r_O_Si"])
            r_f = float(row["r_Si_Fminus"])
            e_wo = float(row["total_energy"])
            if (r_o, r_f) in with_h_map:
                e_with = with_h_map[(r_o, r_f)]
                if e_wo + tol < e_with:
                    violations += 1
                compared += 1
        except (ValueError, KeyError):
            continue
    if compared == 0:
        return 0.0
    viol_ratio = violations / compared
    score = max(0.0, 1.0 - 2 * viol_ratio)
    return score


# === block: score_3 (check id='desorption_with_h') ===
def score_3(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) < 4:
        return 0.0
    # parse grid into arrays
    r_o_vals = []
    r_f_vals = []
    energies = []
    for row in data:
        try:
            r_o = float(row["r_O_Si"])
            r_f = float(row["r_Si_Fminus"])
            e = float(row["total_energy"])
            r_o_vals.append(r_o)
            r_f_vals.append(r_f)
            energies.append(e)
        except (ValueError, KeyError):
            continue
    if not energies:
        return 0.0
    # unique sorted axes
    unique_o = sorted(set(r_o_vals))
    unique_f = sorted(set(r_f_vals))
    if len(unique_o) < 2 or len(unique_f) < 2:
        return 0.0
    # create mapping from coordinate to index
    idx_o = {val: i for i, val in enumerate(unique_o)}
    idx_f = {val: i for i, val in enumerate(unique_f)}
    energy_grid = np.full((len(unique_o), len(unique_f)), np.inf)
    for roi, rfi, e in zip(r_o_vals, r_f_vals, energies):
        energy_grid[idx_o[roi], idx_f[rfi]] = e
    # find start: global minimum energy point
    flat_idx = np.argmin(energy_grid)
    start_o_idx, start_f_idx = np.unravel_index(flat_idx, energy_grid.shape)
    start_energy = energy_grid[start_o_idx, start_f_idx]
    # find end: corner with maximum r_O_Si and minimum r_Si_Fminus
    end_o_idx = len(unique_o) - 1
    end_f_idx = 0  # smallest r_f
    # DP path minimizing maximum energy along path
    rows, cols = energy_grid.shape
    dp = np.full_like(energy_grid, np.inf, dtype=float)
    dp[start_o_idx, start_f_idx] = energy_grid[start_o_idx, start_f_idx]
    import heapq
    pq = [(dp[start_o_idx, start_f_idx], start_o_idx, start_f_idx)]
    visited = set()
    while pq:
        val, i, j = heapq.heappop(pq)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == end_o_idx and j == end_f_idx:
            break
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and not np.isinf(energy_grid[ni, nj]):
                    new_max = max(val, energy_grid[ni, nj])
                    if new_max < dp[ni, nj]:
                        dp[ni, nj] = new_max
                        heapq.heappush(pq, (new_max, ni, nj))
    transition_energy = dp[end_o_idx, end_f_idx]
    if np.isinf(transition_energy):
        return 0.0
    activation = transition_energy - start_energy
    if activation < 0:
        activation = 0.0
    act_target = step.get("activation_target", 0.8)
    act_tol = step.get("activation_tolerance", 0.1)
    diff = abs(activation - act_target)
    if diff <= act_tol:
        return 1.0
    # linear decay up to 2*tol
    if diff <= 2 * act_tol:
        return 1.0 - (diff - act_tol) / act_tol
    return 0.0


# === block: score_4 (check id='activation_report') ===
def score_4(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    checks = step.get("checks", {})
    if not checks:
        return 1.0
    scores = []
    for key, cfg in checks.items():
        target = cfg.get("target")
        tol = cfg.get("tolerance")
        if target is None or tol is None:
            scores.append(1.0)
            continue
        # handle nested list keys
        if key == "angle_range" or key == "bond_population_range":
            val_list = artifact.get(key, [])
            if isinstance(val_list, list) and len(val_list) == 2:
                min_val, max_val = float(val_list[0]), float(val_list[1])
                # For angle_range_min / max, we check each separately
                if key == "angle_range":
                    min_target = step["checks"]["angle_range_min"]["target"]
                    max_target = step["checks"]["angle_range_max"]["target"]
                    min_tol = step["checks"]["angle_range_min"]["tolerance"]
                    max_tol = step["checks"]["angle_range_max"]["tolerance"]
                    diff_min = abs(min_val - min_target)
                    diff_max = abs(max_val - max_target)
                    s_min = 1.0 if diff_min <= min_tol else max(0.0, 1.0 - (diff_min - min_tol) / min_tol)
                    s_max = 1.0 if diff_max <= max_tol else max(0.0, 1.0 - (diff_max - max_tol) / max_tol)
                    scores.append(0.5 * s_min + 0.5 * s_max)
                elif key == "bond_population_range":
                    max_target_bp = step["checks"]["bond_population_max"]["target"]
                    min_target_bp = step["checks"]["bond_population_min"]["target"]
                    max_tol_bp = step["checks"]["bond_population_max"]["tolerance"]
                    min_tol_bp = step["checks"]["bond_population_min"]["tolerance"]
                    diff_max_ = abs(max_val - max_target_bp)
                    diff_min_ = abs(min_val - min_target_bp)
                    s_max_ = 1.0 if diff_max_ <= max_tol_bp else max(0.0, 1.0 - (diff_max_ - max_tol_bp) / max_tol_bp)
                    s_min_ = 1.0 if diff_min_ <= min_tol_bp else max(0.0, 1.0 - (diff_min_ - min_tol_bp) / min_tol_bp)
                    scores.append(0.5 * s_max_ + 0.5 * s_min_)
            else:
                scores.append(0.0)
            continue
        # scalar key
        val = artifact.get(key)
        if val is None:
            scores.append(0.0)
            continue
        try:
            val = float(val)
        except (ValueError, TypeError):
            scores.append(0.0)
            continue
        diff = abs(val - target)
        if diff <= tol:
            scores.append(1.0)
        else:
            s = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(s)
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_5 (check id='angle_population_trend') ===
def score_5(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 4:
        return 0.0
    # group by case
    cases = {}
    for row in artifact:
        case = row.get("case", "")
        if case not in ("with_Hplus", "without_Hplus"):
            continue
        try:
            rc = float(row["reaction_coordinate_rc"])
            angle = float(row["optimized_O_Si_F_angle"])
            pop = float(row["Si_O_bond_population"])
            cases.setdefault(case, []).append((rc, angle, pop))
        except (ValueError, KeyError):
            continue
    if not cases or "with_Hplus" not in cases or "without_Hplus" not in cases:
        return 0.0
    def assess_trend(points, angle_start, angle_end, angle_tol, pop_start_min, pop_end_max):
        # points sorted by rc
        sorted_pts = sorted(points, key=lambda x: x[0])
        angles = [p[1] for p in sorted_pts]
        pops = [p[2] for p in sorted_pts]
        # start/end angle check
        diff_start = abs(angles[0] - angle_start) if angles else 100
        diff_end = abs(angles[-1] - angle_end) if angles else 100
        s_start = 1.0 if diff_start <= angle_tol else max(0.0, 1.0 - (diff_start - angle_tol) / (angle_tol * 2))
        s_end = 1.0 if diff_end <= angle_tol else max(0.0, 1.0 - (diff_end - angle_tol) / (angle_tol * 2))
        # monotonic decrease: allow small positive increments (0.5 deg)
        mono_violations = 0
        for i in range(1, len(angles)):
            if angles[i] - angles[i-1] > 0.5:
                mono_violations += 1
        s_mono = max(0.0, 1.0 - mono_violations / max(1, len(angles)-1))
        # bond pop: start > pop_start_min, end < pop_end_max
        s_pop_start = 1.0 if pops[0] >= pop_start_min else 0.0
        s_pop_end = 1.0 if pops[-1] <= pop_end_max else 0.0
        # pop decreasing roughly
        pop_violations = 0
        for i in range(1, len(pops)):
            if pops[i] - pops[i-1] > 0.05:
                pop_violations += 1
        s_pop_mono = max(0.0, 1.0 - pop_violations / max(1, len(pops)-1))
        return (s_start + s_end + s_mono + s_pop_start + s_pop_end + s_pop_mono) / 6.0
    angle_start = step.get("angle_start_deg", 109.47)
    angle_end = step.get("angle_end_deg", 70.53)
    angle_tol = step.get("angle_tolerance_deg", 5.0)
    pop_start_min = step.get("pop_start_min", 0.2)
    pop_end_max = step.get("pop_end_max", 0.1)
    with_h_score = assess_trend(cases["with_Hplus"], angle_start, angle_end, angle_tol, pop_start_min, pop_end_max)
    without_h_score = assess_trend(cases["without_Hplus"], angle_start, angle_end, angle_tol, pop_start_min, pop_end_max)
    # additional check: with_Hplus angles lower than without at same rc (steeper collapse)
    # only if both have same rc points
    with_dict = {p[0]: (p[1], p[2]) for p in cases["with_Hplus"]}
    without_dict = {p[0]: (p[1], p[2]) for p in cases["without_Hplus"]}
    compared = 0
    steep_violations = 0
    for rc in sorted(set(with_dict).intersection(without_dict)):
        a_with, _ = with_dict[rc]
        a_wo, _ = without_dict[rc]
        if a_with > a_wo + 0.5:
            steep_violations += 1
        compared += 1
    steep_score = 1.0 if compared == 0 else max(0.0, 1.0 - steep_violations / compared)
    return 0.6 * with_h_score + 0.2 * without_h_score + 0.2 * steep_score


_SCORERS = {
    'sif4_binding_scan': score_0,
    'hf2_dissociation': score_1,
    'desorption_without_h': score_2,
    'desorption_with_h': score_3,
    'activation_report': score_4,
    'angle_population_trend': score_5,
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
