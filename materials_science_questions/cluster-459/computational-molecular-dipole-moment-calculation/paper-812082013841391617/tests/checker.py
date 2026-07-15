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
    ctx = {}
    for step in spec.get('steps', []):
        step_id = step['id']
        targets_raw = step.get('targets', {})
        tolerance = step.get('tolerance', 1e-6)
        kind = step.get('kind')
        if kind == 'numeric_table_compare':
            key_cols = step.get('key_columns')
            value_col = step.get('value_column')
            if isinstance(key_cols, list):
                targets = {}
                for k_str, val in targets_raw.items():
                    keys = k_str.split(',')
                    keys_num = tuple(float(x) for x in keys)
                    targets[keys_num] = val
            else:
                targets = {float(k): v for k, v in targets_raw.items()}
            ctx[step_id] = {'targets': targets, 'tolerance': tolerance, 'key_cols': key_cols, 'value_col': value_col}
    return ctx


# === block: score_0 (check id='dipole_moment_function') ===
def score_0(artifact, step, ctx):
    info = ctx['dipole_moment_function']
    targets = info['targets']
    tol = info['tolerance']
    key_col = info['key_cols']
    val_col = info['value_col']
    agent_points = {}
    for row in artifact:
        try:
            r = float(row[key_col])
            dm = float(row[val_col])
            agent_points[r] = dm
        except (ValueError, KeyError):
            continue
    score_sum = 0.0
    dist_tol = 1e-5
    for target_r, target_dm in targets.items():
        best_r = None
        best_dist = float('inf')
        for ar in agent_points:
            dist = abs(ar - target_r)
            if dist < best_dist:
                best_dist = dist
                best_r = ar
        if best_r is not None and best_dist <= dist_tol:
            err = abs(agent_points[best_r] - target_dm)
            score_sum += 1.0 if err <= tol else 0.0
    return score_sum / len(targets) if targets else 0.0


# === block: score_1 (check id='dipole_matrix_elements') ===
def score_1(artifact, step, ctx):
    info = ctx['dipole_matrix_elements']
    targets = info['targets']
    tol = info['tolerance']
    key_cols = info['key_cols']
    val_col = info['value_col']
    total_score = 0.0
    for row in artifact:
        try:
            vp = int(row[key_cols[0]])
            vpp = int(row[key_cols[1]])
            val = float(row[val_col])
            key = (float(vp), float(vpp))
            if key in targets:
                err = abs(val - targets[key])
                total_score += 1.0 if err <= tol else 0.0
        except (ValueError, KeyError):
            continue
    return total_score / len(targets) if targets else 0.0


_SCORERS = {
    'dipole_moment_function': score_0,
    'dipole_matrix_elements': score_1,
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
