import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, collections, os


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
    return {'spec': spec}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    gold = step.get('config', {}).get('gold_vectors', {})
    tol = step.get('config', {}).get('tolerance', 0.01)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    # Build lookup
    agent_data = {}
    for row in artifact:
        comp = row.get('compound', '').strip()
        spin = row.get('spin_orientation', '').strip()
        try:
            x = float(row.get('M_Lx', 'nan'))
            y = float(row.get('M_Ly', 'nan'))
            z = float(row.get('M_Lz', 'nan'))
        except (ValueError, TypeError):
            continue
        agent_data[(comp, spin)] = (x, y, z)

    total = 0
    count = 0
    for comp, spins in gold.items():
        for spin, ref in spins.items():
            key = (comp, spin)
            if key not in agent_data:
                continue
            ax, ay, az = agent_data[key]
            ok = (abs(ax - ref[0]) <= tol and abs(ay - ref[1]) <= tol and abs(az - ref[2]) <= tol)
            total += 1.0 if ok else 0.0
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_1 (check id='step_05') ===
def score_1(artifact, step, ctx):
    cfg = step.get('config', {})
    expected_peak = float(cfg.get('expected_peak_energy_eV', 4.0))
    energy_tol = float(cfg.get('energy_tolerance_eV', 0.5))
    sign_required = cfg.get('sign', 'positive')
    ordering = cfg.get('amplitude_ordering', [])
    req_range = cfg.get('required_energy_range', [0.0, 8.0])
    max_step = float(cfg.get('max_energy_step', 0.1))

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # Group data by compound
    data = collections.defaultdict(list)
    for row in artifact:
        comp = row.get('compound', '').strip()
        try:
            e = float(row.get('energy_eV', 'nan'))
            val = float(row.get('imag_sigma_A', 'nan'))
        except (ValueError, TypeError):
            continue
        data[comp].append((e, val))

    # Check that all required compounds exist
    if not all(comp in data for comp in ordering):
        return 0.0

    # Shape gate: energy range and step check
    range_ok = True
    step_ok = True
    for comp, points in data.items():
        if not points:
            range_ok = False
            continue
        energies = sorted(p[0] for p in points)
        if energies[0] > req_range[0] + 0.05 or energies[-1] < req_range[1] - 0.05:
            range_ok = False
        # check max step
        gaps = [energies[i+1] - energies[i] for i in range(len(energies)-1)]
        if any(g > max_step + 0.001 for g in gaps):
            step_ok = False

    # Compute peak for each compound
    peak_info = {}
    for comp in ordering:
        pts = data[comp]
        if not pts:
            peak_info[comp] = (None, None)
            continue
        # find max absolute value (positive sign required)
        max_val = -float('inf')
        max_e = None
        for e, v in pts:
            if v > max_val:
                max_val = v
                max_e = e
        peak_info[comp] = (max_e, max_val)

    # Sub-scores
    score_range = 1.0 if range_ok else 0.0
    score_step = 1.0 if step_ok else 0.0

    # Peak energy check (each compound must have peak near expected)
    peak_energy_ok = all(
        peak_info[comp][0] is not None and abs(peak_info[comp][0] - expected_peak) <= energy_tol
        for comp in ordering
    )
    score_peak_energy = 1.0 if peak_energy_ok else 0.0

    # Sign check: all max values positive
    sign_ok = all(peak_info[comp][1] is not None and peak_info[comp][1] > 0 for comp in ordering)
    score_sign = 1.0 if sign_ok else 0.0

    # Amplitude ordering: check that peaks are sorted according to ordering list (max first)
    ordering_ok = True
    vals = [peak_info[comp][1] for comp in ordering]
    if any(v is None for v in vals):
        ordering_ok = False
    else:
        for i in range(len(vals)-1):
            if vals[i] <= vals[i+1]:  # strict ordering? require >
                ordering_ok = False
                break
    score_order = 1.0 if ordering_ok else 0.0

    # Weighted final score
    weights = {
        'range': 0.1,
        'step': 0.1,
        'peak_energy': 0.3,
        'sign': 0.2,
        'ordering': 0.3
    }
    final = (score_range * weights['range'] +
             score_step * weights['step'] +
             score_peak_energy * weights['peak_energy'] +
             score_sign * weights['sign'] +
             score_order * weights['ordering'])
    return min(max(final, 0.0), 1.0)


_SCORERS = {
    'step_02': score_0,
    'step_05': score_1,
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
