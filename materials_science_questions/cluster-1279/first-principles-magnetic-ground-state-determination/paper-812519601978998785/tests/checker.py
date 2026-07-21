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


# === block: score_0 (check id='plateaus') ===
def score_0(artifact, step, ctx):
    refs = step.get("reference", {}).get("plateau_definitions", {})
    if not artifact or not isinstance(artifact, list):
        return 0.0
    groups = {}
    for row in artifact:
        r1 = str(row.get("R1"))
        ds = float(row.get("d_s", 0))
        m_plus = float(row.get("M_Mn_plus", 0))
        m_minus = float(row.get("M_Mn_minus", 0))
        if r1 not in groups:
            groups[r1] = []
        groups[r1].append((ds, m_plus, m_minus))
    total_regions = 0
    passed_regions = 0
    for r1_str, roi_defs in refs.items():
        if r1_str not in groups:
            continue
        points = groups[r1_str]
        for roi in roi_defs:
            dmin = roi["d_min"]
            dmax = roi["d_max"]
            expected_plus = roi["M_plus"]
            expected_minus = roi["M_minus"]
            tol = roi.get("tol", 0.15)
            roi_plus = []
            roi_minus = []
            for ds, mp, mn in points:
                if dmin <= ds <= dmax:
                    roi_plus.append(mp)
                    roi_minus.append(mn)
            if len(roi_plus) == 0:
                total_regions += 1
                continue
            avg_plus = sum(roi_plus) / len(roi_plus)
            avg_minus = sum(roi_minus) / len(roi_minus)
            total_regions += 1
            if abs(avg_plus - expected_plus) <= tol and abs(avg_minus - expected_minus) <= tol:
                passed_regions += 1
    if total_regions == 0:
        return 0.0
    return passed_regions / total_regions


# === block: score_1 (check id='critical_ds') ===
def score_1(artifact, step, ctx):
    ref = step.get("reference", {})
    if not artifact or not isinstance(artifact, str):
        return 0.0
    lines = artifact.strip().splitlines()
    if len(lines) < 2:
        return 0.0
    try:
        vals1 = [float(v.strip()) for v in lines[0].split(",")]
        vals2 = [float(v.strip()) for v in lines[1].split(",")]
    except:
        return 0.0
    gold1 = ref.get("0.5", [])
    gold2 = ref.get("5.0", [])
    tol = step.get("tolerance", 1.0)
    total = len(gold1) + len(gold2)
    if total == 0:
        return 0.0
    correct = 0
    for i, g in enumerate(gold1):
        if i < len(vals1) and abs(vals1[i] - g) <= tol:
            correct += 1
    for i, g in enumerate(gold2):
        if i < len(vals2) and abs(vals2[i] - g) <= tol:
            correct += 1
    return correct / total


# === block: score_2 (check id='rcp_field') ===
def score_2(artifact, step, ctx):
    ref = step.get("reference", {})
    param_col = ref.get("param_column")
    direction = ref.get("direction")
    expected_count = ref.get("expected_row_count")
    if not artifact or not isinstance(artifact, list):
        return 0.0
    if expected_count is not None and len(artifact) != expected_count:
        return 0.0
    if len(artifact) < 2:
        return 1.0
    try:
        values = [(float(row.get(param_col, 0)), float(row.get("RCP", 0))) for row in artifact]
    except:
        return 0.0
    values.sort(key=lambda x: x[0])
    rcp_vals = [v[1] for v in values]
    correct = 0
    total = len(rcp_vals) - 1
    for i in range(total):
        if direction == "increasing":
            if rcp_vals[i+1] >= rcp_vals[i] - 1e-9:
                correct += 1
        else:
            if rcp_vals[i+1] <= rcp_vals[i] + 1e-9:
                correct += 1
    if total == 0:
        return 1.0
    return correct / total


# === block: score_3 (check id='rcp_ds') ===
def score_3(artifact, step, ctx):
    ref = step.get("reference", {})
    param_col = ref.get("param_column")
    direction = ref.get("direction")
    expected_count = ref.get("expected_row_count")
    if not artifact or not isinstance(artifact, list):
        return 0.0
    if expected_count is not None and len(artifact) != expected_count:
        return 0.0
    if len(artifact) < 2:
        return 1.0
    try:
        values = [(float(row.get(param_col, 0)), float(row.get("RCP", 0))) for row in artifact]
    except:
        return 0.0
    values.sort(key=lambda x: x[0])
    rcp_vals = [v[1] for v in values]
    correct = 0
    total = len(rcp_vals) - 1
    for i in range(total):
        if direction == "increasing":
            if rcp_vals[i+1] >= rcp_vals[i] - 1e-9:
                correct += 1
        else:
            if rcp_vals[i+1] <= rcp_vals[i] + 1e-9:
                correct += 1
    if total == 0:
        return 1.0
    return correct / total


# === block: score_4 (check id='rcp_R1') ===
def score_4(artifact, step, ctx):
    ref = step.get("reference", {})
    param_col = ref.get("param_column")
    direction = ref.get("direction")
    expected_count = ref.get("expected_row_count")
    if not artifact or not isinstance(artifact, list):
        return 0.0
    if expected_count is not None and len(artifact) != expected_count:
        return 0.0
    if len(artifact) < 2:
        return 1.0
    try:
        values = [(float(row.get(param_col, 0)), float(row.get("RCP", 0))) for row in artifact]
    except:
        return 0.0
    values.sort(key=lambda x: x[0])
    rcp_vals = [v[1] for v in values]
    correct = 0
    total = len(rcp_vals) - 1
    for i in range(total):
        if direction == "increasing":
            if rcp_vals[i+1] >= rcp_vals[i] - 1e-9:
                correct += 1
        else:
            if rcp_vals[i+1] <= rcp_vals[i] + 1e-9:
                correct += 1
    if total == 0:
        return 1.0
    return correct / total


# === block: score_5 (check id='rcp_R2') ===
def score_5(artifact, step, ctx):
    ref = step.get("reference", {})
    param_col = ref.get("param_column")
    direction = ref.get("direction")
    expected_count = ref.get("expected_row_count")
    if not artifact or not isinstance(artifact, list):
        return 0.0
    if expected_count is not None and len(artifact) != expected_count:
        return 0.0
    if len(artifact) < 2:
        return 1.0
    try:
        values = [(float(row.get(param_col, 0)), float(row.get("RCP", 0))) for row in artifact]
    except:
        return 0.0
    values.sort(key=lambda x: x[0])
    rcp_vals = [v[1] for v in values]
    correct = 0
    total = len(rcp_vals) - 1
    for i in range(total):
        if direction == "increasing":
            if rcp_vals[i+1] >= rcp_vals[i] - 1e-9:
                correct += 1
        else:
            if rcp_vals[i+1] <= rcp_vals[i] + 1e-9:
                correct += 1
    if total == 0:
        return 1.0
    return correct / total


_SCORERS = {
    'plateaus': score_0,
    'critical_ds': score_1,
    'rcp_field': score_2,
    'rcp_ds': score_3,
    'rcp_R1': score_4,
    'rcp_R2': score_5,
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