import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
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


# === block: score_0 (check id='check_01_data') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    rubric = step.get('rubric', {}).get('checks', [])
    if not rubric:
        return 1.0
    total = 0.0
    for check in rubric:
        w = check.get('weight', 0.0)
        typ = check.get('type', '')
        if typ == 'file_exists':
            # artifact already loaded, so exists
            total += w
        elif typ == 'columns_exist':
            cols = check.get('columns', [])
            if isinstance(artifact, list) and artifact:
                keys = artifact[0].keys()
                if all(c in keys for c in cols):
                    total += w
        elif typ == 'row_count_min':
            min_rows = check.get('min_rows', 1)
            if isinstance(artifact, list) and len(artifact) >= min_rows:
                total += w
        elif typ == 'numeric_columns':
            cols = check.get('columns', [])
            if isinstance(artifact, list) and artifact:
                ok = True
                for row in artifact:
                    for c in cols:
                        try:
                            float(row[c])
                        except (ValueError, TypeError, KeyError):
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    total += w
        elif typ == 'temperature_range':
            col = check.get('column', 'temperature_K')
            tmin = check.get('min')
            tmax = check.get('max')
            if isinstance(artifact, list):
                temps = [float(r.get(col, float('nan'))) for r in artifact]
                if temps and min(temps) >= tmin and max(temps) <= tmax:
                    total += w
        else:
            # unknown check type, skip
            pass
    return min(1.0, total)


# === block: score_1 (check id='check_02_gamma') ===
def score_1(artifact, step, ctx):
    import os, json, csv, numpy as np

    # Load data CSV
    cfg = step.get('config', {})
    data_file = cfg.get('data_file', 'step_01_alpha_cp_data.csv')
    x_col = cfg.get('x_column', 'Cp_over_T_J_per_mol_K2')
    y_col = cfg.get('y_column', 'alpha_ppm_per_K')
    v0 = cfg.get('v0', 0.00825)
    target = step.get('target', 7.48)
    tol = step.get('tolerance_abs', 0.3)

    data_path = os.path.join('/app/outputs', data_file)
    if not os.path.exists(data_path):
        return 0.0

    rows = []
    with open(data_path, newline='') as f:
        reader = csv.DictReader(f)
        if x_col not in reader.fieldnames or y_col not in reader.fieldnames:
            return 0.0
        for r in reader:
            try:
                x = float(r[x_col])
                y = float(r[y_col])
                rows.append((x, y))
            except (ValueError, KeyError):
                continue

    if len(rows) < 3:
        return 0.0

    xs = np.array([r[0] for r in rows])
    ys = np.array([r[1] for r in rows])

    slope, intercept = np.polyfit(xs, ys, 1)
    gamma = slope * v0

    diff = abs(gamma - target)
    if diff <= tol:
        return 1.0
    else:
        # Linear decay: full score at tol, 0 at diff >= 1.5 K/MPa
        decay = (diff - tol) / 1.2
        return max(0.0, 1.0 - decay)


# === block: score_2 (check id='check_03_beta_consistency') ===
def score_2(artifact, step, ctx):
    import os, json, csv

    cfg = step.get('config', {})
    v0 = cfg.get('v0', 0.00825)
    data_file = cfg.get('data_file', 'step_01_alpha_cp_data.csv')
    gamma_source = cfg.get('gamma_source', 'step_02_fit_results.json')
    gamma_field = cfg.get('gamma_field', 'gamma_minus')
    rel_tol = cfg.get('rel_tolerance', 0.01)

    # Load gamma
    json_path = os.path.join('/app/outputs', gamma_source)
    if not os.path.exists(json_path):
        return 0.0
    with open(json_path) as f:
        fit = json.load(f)
    if gamma_field not in fit:
        return 0.0
    gamma = float(fit[gamma_field])
    if gamma == 0:
        return 0.0

    # Load Cp/T data
    cp_data = {}
    data_path = os.path.join('/app/outputs', data_file)
    if os.path.exists(data_path):
        with open(data_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                try:
                    T = float(r['temperature_K'])
                    cpt = float(r['Cp_over_T_J_per_mol_K2'])
                    cp_data[T] = cpt
                except (ValueError, KeyError):
                    continue

    if not cp_data:
        return 0.0

    # Load beta CSV
    artifact_path = os.path.join('/app/outputs', step.get('output_file', ''))
    if artifact is None:
        return 0.0
    total = 0
    passed = 0
    if isinstance(artifact, list):
        for row in artifact:
            try:
                T = float(row['temperature_K'])
                beta = float(row['beta_GPa_minus_one'])
            except (ValueError, KeyError):
                continue
            total += 1
            cpt = cp_data.get(T, None)
            if cpt is None:
                continue
            predicted = (gamma ** 2) / v0 * cpt
            if abs(predicted) < 1e-12:
                passed += 1 if abs(beta) < 1e-12 else 0
            else:
                if abs(beta - predicted) / abs(predicted) <= rel_tol:
                    passed += 1
    return passed / total if total > 0 else 0.0


_SCORERS = {
    'check_01_data': score_0,
    'check_02_gamma': score_1,
    'check_03_beta_consistency': score_2,
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
