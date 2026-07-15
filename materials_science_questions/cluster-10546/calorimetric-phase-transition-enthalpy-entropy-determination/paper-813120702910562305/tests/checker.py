import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    def _find_ramp_boundaries(times, pz):
        """Detect ramp start and end from Pz time series.
        Returns (start_idx, end_idx) such that ramp is roughly [start_idx, end_idx)."""
        # estimate baseline from first 20 points
        nb = min(20, len(pz))
        baseline = sum(abs(pz[i]) for i in range(nb)) / nb
        # find first large drop (Pz drops by >0.03 relative to baseline)
        start = None
        for i in range(1, len(pz)):
            if abs(pz[i]) < baseline - 0.03:  # noticeable drop
                start = i - 1
                break
        if start is None:
            start = 0
        # find end: after drop, Pz stabilises (rolling std small)
        window = min(20, len(pz)-start-1)
        end = start + 1
        best_end = start
        for i in range(start+1, len(pz)-window):
            seg = pz[i:i+window]
            mu = sum(abs(v) for v in seg)/window
            var = sum((abs(v)-mu)**2 for v in seg)/window
            if var < 0.0001 and i > start+10:  # stable
                best_end = i + window
                break
        else:
            best_end = len(pz)
        return start, best_end

    data = []
    with open(os.path.join('/app/outputs', 'time_evolution.csv'), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                t = float(row['time_ps'])
                T = float(row['temperature_K'])
                px = float(row['Px'])
                py = float(row['Py'])
                pz = float(row['Pz'])
                data.append((t, T, px, py, pz))
            except:
                pass
    data.sort(key=lambda x: x[0])
    times = [d[0] for d in data]
    temp = [d[1] for d in data]
    pz = [d[4] for d in data]
    ramp_start_idx, ramp_end_idx = _find_ramp_boundaries(times, pz)
    # Initial equilibration: last 40 ps before ramp start
    n_init = min(40, ramp_start_idx)
    idx_i_start = max(0, ramp_start_idx - n_init)
    idx_i_end = ramp_start_idx
    T_i = sum(temp[idx_i_start:idx_i_end])/n_init if n_init>0 else 0.0
    # Final equilibration: last 40 ps after ramp end, or last 40 rows of data
    n_final = min(40, len(data)-ramp_end_idx)
    if n_final>0:
        idx_f_start = max(ramp_end_idx, len(data)-n_final)
        idx_f_end = len(data)
        T_f = sum(temp[idx_f_start:idx_f_end])/n_final
    else:
        T_f = T_i
    raw_dT = T_f - T_i
    scaled_dT = raw_dT / 5.0
    # Polarization characteristics: average Px,Py,Pz in initial and final windows
    init_px = sum(abs(d[2]) for d in data[idx_i_start:idx_i_end])/n_init
    init_py = sum(abs(d[3]) for d in data[idx_i_start:idx_i_end])/n_init
    init_pz = sum(abs(d[4]) for d in data[idx_i_start:idx_i_end])/n_init
    final_px = sum(abs(d[2]) for d in data[idx_f_start:idx_f_end])/n_final if n_final>0 else 0.0
    final_py = sum(abs(d[3]) for d in data[idx_f_start:idx_f_end])/n_final if n_final>0 else 0.0
    final_pz = sum(abs(d[4]) for d in data[idx_f_start:idx_f_end])/n_final if n_final>0 else 0.0
    return {
        'T_i': T_i, 'T_f': T_f, 'raw_dT': raw_dT, 'scaled_dT': scaled_dT,
        'init_px': init_px, 'init_py': init_py, 'init_pz': init_pz,
        'final_px': final_px, 'final_py': final_py, 'final_pz': final_pz,
        'n_rows': len(data),
        'ramp_start_idx': ramp_start_idx, 'ramp_end_idx': ramp_end_idx
    }


# === block: score_0 (check id='step_1_transition_signature') ===
def score_0(artifact, step, ctx):
    score = 0.0
    if ctx['n_rows'] >= 200:
        cond1 = ctx['init_pz'] > 0.2 and ctx['init_px'] < 0.05 and ctx['init_py'] < 0.05
        cond2 = ctx['final_px'] > 0.1 and ctx['final_pz'] > 0.1
        cond3 = ctx['raw_dT'] > 0.5  # raw temperature rise indicative of inverse EC
        passed = sum([cond1, cond2, cond3])
        score = min(1.0, passed / 3.0)
    return score


# === block: score_1 (check id='step_2_scaled_delta_T') ===
def score_1(artifact, step, ctx):
    scaled = ctx['scaled_dT']
    target = 1.2
    tol = 0.3
    if abs(scaled - target) <= tol:
        return 1.0
    else:
        # graded partial if outside, example linear decay
        return max(0.0, 1.0 - (abs(scaled - target) - tol) / 0.5)


_SCORERS = {
    'step_1_transition_signature': score_0,
    'step_2_scaled_delta_T': score_1,
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
