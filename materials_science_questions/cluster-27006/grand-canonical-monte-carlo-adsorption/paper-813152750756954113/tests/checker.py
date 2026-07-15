import os
import json
import csv

# === author imports / helpers ===
import zipfile, io, numpy as np, math


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
    import os as _os

    # Save original load_artifact function
    _original_load_artifact = load_artifact

    def _safe_load_artifact(path):
        if not path or not _os.path.exists(path):
            return None
        if path.endswith('.zip'):
            # Return the file path; the occupation scorer reads it directly.
            return path
        # Delegate to original for all other file types
        return _original_load_artifact(path)

    # Replace the global load_artifact with our safe version
    globals()['load_artifact'] = _safe_load_artifact

    return {}


# === block: score_0 (check id='heats_henry_numeric') ===
def score_0(artifact, step, ctx):
    expected = step.get('expected', {})
    if not expected:
        return 0.0
    tol = step.get('tolerances', {})
    abs_qst = tol.get('Qst_abs', 3.0)
    rel_qst = tol.get('Qst_rel', 0.10)
    rel_henry = tol.get('Henry_rel', 0.30)

    agent_dict = {}
    for row in artifact:
        zeo = row.get('zeolite', '').strip()
        if not zeo:
            continue
        qstS = float(row.get('Qst_SO2', 0))
        qstC = float(row.get('Qst_CO2', 0))
        qstO = float(row.get('Qst_CO', 0))
        hS = float(row.get('Henry_SO2', 0))
        hC = float(row.get('Henry_CO2', 0))
        hO = float(row.get('Henry_CO', 0))
        agent_dict[zeo] = (qstS, qstC, qstO, hS, hC, hO)

    # Each gas score based on fraction of expected zeolites that are within tolerance
    # For Qst: tolerance = max(abs_qst, rel_qst*|gold|)
    # For Henry: tolerance = rel_henry*|gold|

    good_counts = [0]*6  # Qst_SO2, Qst_CO2, Qst_CO, Henry_SO2, Henry_CO2, Henry_CO
    n_expected = 0
    for zeo, golds in expected.items():
        n_expected += 1
        vals = agent_dict.get(zeo)
        if vals is None:
            continue
        for i, (gold_val, tol_val) in enumerate([
            (golds['Qst_SO2'], max(abs_qst, rel_qst*abs(golds['Qst_SO2']))),
            (golds['Qst_CO2'], max(abs_qst, rel_qst*abs(golds['Qst_CO2']))),
            (golds['Qst_CO'],  max(abs_qst, rel_qst*abs(golds['Qst_CO']))),
            (golds['Henry_SO2'], rel_henry*abs(golds['Henry_SO2'])),
            (golds['Henry_CO2'], rel_henry*abs(golds['Henry_CO2'])),
            (golds['Henry_CO'],  rel_henry*abs(golds['Henry_CO']))]):
            agent_val = vals[i]
            if abs(agent_val - gold_val) <= tol_val + 1e-12:
                good_counts[i] += 1

    if n_expected == 0:
        return 0.0
    scores = [c / n_expected for c in good_counts]
    overall = sum(scores) / len(scores)
    return overall


# === block: score_1 (check id='loading_ternary_numeric') ===
def score_1(artifact, step, ctx):
    expected = step.get('expected', {})
    if not expected:
        return 0.0
    rel = step.get('tolerances', {}).get('loading_rel', 0.20)

    agent_dict = {}
    for row in artifact:
        zeo = row.get('zeolite', '').strip()
        if not zeo:
            continue
        lS = float(row.get('loading_SO2', 0))
        lC = float(row.get('loading_CO2', 0))
        lO = float(row.get('loading_CO', 0))
        agent_dict[zeo] = (lS, lC, lO)

    good_counts = [0,0,0]
    n_expected = 0
    for zeo, golds in expected.items():
        n_expected += 1
        vals = agent_dict.get(zeo)
        if vals is None:
            continue
        for i, key in enumerate(['loading_SO2','loading_CO2','loading_CO']):
            gold = golds[key]
            tol = rel * abs(gold) + 1e-12
            if abs(vals[i] - gold) <= tol:
                good_counts[i] += 1

    if n_expected == 0:
        return 0.0
    scores = [c / n_expected for c in good_counts]
    return sum(scores)/len(scores)


# === block: score_2 (check id='diffusion_coefficients_numeric') ===
def score_2(artifact, step, ctx):
    expected = step.get('expected', {})
    if not expected:
        return 0.0
    rel = step.get('tolerances', {}).get('D_rel', 0.40)

    agent_dict = {}
    for row in artifact:
        zeo = row.get('zeolite', '').strip()
        if not zeo:
            continue
        dS = float(row.get('D_SO2', 0))
        dC = float(row.get('D_CO2', 0))
        agent_dict[zeo] = (dS, dC)

    good_counts = [0,0]
    n_expected = 0
    for zeo, golds in expected.items():
        n_expected += 1
        vals = agent_dict.get(zeo)
        if vals is None:
            continue
        for i, key in enumerate(['D_SO2','D_CO2']):
            gold = golds[key]
            tol = rel * abs(gold) + 1e-12
            if abs(vals[i] - gold) <= tol:
                good_counts[i] += 1

    if n_expected == 0:
        return 0.0
    scores = [c / n_expected for c in good_counts]
    return sum(scores)/len(scores)


# === block: score_3 (check id='occupation_profiles_structural') ===
def score_3(artifact, step, ctx):
    expected_names = set(step.get('expected_entries', []))
    if not expected_names:
        return 0.0

    # artifact is the loaded ZIP file as a string? Actually the loader returns the file content as string for txt, but for zip it returns the path? 
    # The scaffold's load_artifact for other returns the raw file content read as string. For binary zip, we need to handle it. 
    # We'll assume the scorer receives the file path? In the scaffold, score_step(artifact, step) where artifact is the result of load_artifact for that output_file.
    # For occupation_profiles.zip, the loading function for 'other' format returns the raw file content as string (but it's binary). 
    # That would break. Instead, we need to modify the loading to handle zip. But the scaffold is fixed; we cannot change it.
    # However, we can add a special case in the imports or prepare that patches load_artifact for zip files. But we can't change scaffold.
    # Simpler: in the grader, we directly read the file path from /app/outputs/occupation_profiles.zip, bypassing the passed artifact. 
    # The artifact argument may be useless. We'll use the file path directly.
    import os, zipfile, io
    zip_path = os.path.join('/app/outputs', 'occupation_profiles.zip')
    if not os.path.exists(zip_path):
        return 0.0

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            names = set(zf.namelist())
            if not expected_names.issubset(names):
                # missing required files
                return 0.0
            for fname in expected_names:
                with zf.open(fname) as f:
                    lines = f.read().decode('utf-8').strip().splitlines()
                if len(lines) < 2:
                    return 0.0
                # first line: zeolite gas
                # second line: n_x n_y x_min x_max y_min y_max
                parts = lines[1].split()
                if len(parts) != 6:
                    return 0.0
                nx, ny = int(parts[0]), int(parts[1])
                if nx <= 0 or ny <= 0:
                    return 0.0
                # remaining lines: density values
                data_lines = lines[2:2+nx]
                if len(data_lines) != nx:
                    return 0.0
                max_val = -1.0
                for dl in data_lines:
                    vals = [float(v) for v in dl.split()]
                    if len(vals) != ny:
                        return 0.0
                    for v in vals:
                        if v < 0.0 or v > 1.0001:  # tiny overflow allowed
                            return 0.0
                        if v > max_val:
                            max_val = v
                # maximum must be 1.0
                if abs(max_val - 1.0) > 1e-3:
                    return 0.0
    except Exception:
        return 0.0

    return 1.0


_SCORERS = {
    'heats_henry_numeric': score_0,
    'loading_ternary_numeric': score_1,
    'diffusion_coefficients_numeric': score_2,
    'occupation_profiles_structural': score_3,
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
