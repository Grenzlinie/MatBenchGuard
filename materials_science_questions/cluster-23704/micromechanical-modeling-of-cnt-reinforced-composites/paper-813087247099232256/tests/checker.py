import os
import json
import csv


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


# === block: score_0 (check id='val_csv_mcf') ===
def score_0(artifact, step, ctx):
    import math
    forces = []
    for row in artifact:
        try:
            f = float(row['contact_force'])
            forces.append(f)
        except (ValueError, KeyError):
            pass
    if not forces:
        return 0.0
    peak_kN = max(forces) / 1000.0
    target = step.get('target', 2.8)
    tol = step.get('tolerance_pct', 0.10)
    error = abs(peak_kN - target) / target
    score = max(0.0, 1.0 - error / tol)
    return score


# === block: score_1 (check id='fg_csv_mcf') ===
def score_1(artifact, step, ctx):
    import math
    forces = []
    for row in artifact:
        try:
            f = float(row['contact_force'])
            forces.append(f)
        except (ValueError, KeyError):
            pass
    if not forces:
        return 0.0
    peak_kN = max(forces) / 1000.0
    target = step.get('target', 2.85)
    tol = step.get('tolerance_pct', 0.05)
    error = abs(peak_kN - target) / target
    score = max(0.0, 1.0 - error / tol)
    return score


# === block: score_2 (check id='val_mcf_consistency') ===
def score_2(artifact, step, ctx):
    import csv, os
    csv_path = '/app/outputs/contact_force_validation.csv'
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            forces = [float(row['contact_force']) for row in reader]
        if not forces:
            return 0.0
        csv_peak_kN = max(forces) / 1000.0
    except Exception:
        return 0.0
    val = artifact.get('validation', {}).get('MCF', None)
    if val is None:
        return 0.0
    tol = step.get('tolerance_pct', 0.02)
    diff = abs(csv_peak_kN - val) / csv_peak_kN if csv_peak_kN else 1.0
    return 1.0 if diff <= tol else 0.0


# === block: score_3 (check id='fg_mcf_consistency') ===
def score_3(artifact, step, ctx):
    import csv, os
    csv_path = '/app/outputs/contact_force_fg_cntrc.csv'
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            forces = [float(row['contact_force']) for row in reader]
        if not forces:
            return 0.0
        csv_peak_kN = max(forces) / 1000.0
    except Exception:
        return 0.0
    val = artifact.get('fg_cntrc', {}).get('MCF', None)
    if val is None:
        return 0.0
    tol = step.get('tolerance_pct', 0.02)
    diff = abs(csv_peak_kN - val) / csv_peak_kN if csv_peak_kN else 1.0
    return 1.0 if diff <= tol else 0.0


# === block: score_4 (check id='fg_alpha') ===
def score_4(artifact, step, ctx):
    import math
    field_path = step.get('field_path', 'fg_cntrc.alpha_max')
    keys = field_path.split('.')
    val = artifact
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            val = None
            break
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 0.0
    target = step.get('target', 0.160)
    tol = step.get('tolerance_pct', 0.10)
    error = abs(val - target) / target
    score = max(0.0, 1.0 - error / tol)
    return score


# === block: score_5 (check id='fg_w') ===
def score_5(artifact, step, ctx):
    import math
    field_path = step.get('field_path', 'fg_cntrc.w_max')
    keys = field_path.split('.')
    val = artifact
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            val = None
            break
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 0.0
    target = step.get('target', 0.260)
    tol = step.get('tolerance_pct', 0.10)
    error = abs(val - target) / target
    score = max(0.0, 1.0 - error / tol)
    return score


# === block: score_6 (check id='fg_T0') ===
def score_6(artifact, step, ctx):
    import math
    field_path = step.get('field_path', 'fg_cntrc.T0')
    keys = field_path.split('.')
    val = artifact
    for k in keys:
        if isinstance(val, dict):
            val = val.get(k)
        else:
            val = None
            break
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 0.0
    target = step.get('target', 408)
    tol = step.get('tolerance_pct', 0.05)
    error = abs(val - target) / target
    score = max(0.0, 1.0 - error / tol)
    return score


_SCORERS = {
    'val_csv_mcf': score_0,
    'fg_csv_mcf': score_1,
    'val_mcf_consistency': score_2,
    'fg_mcf_consistency': score_3,
    'fg_alpha': score_4,
    'fg_w': score_5,
    'fg_T0': score_6,
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
