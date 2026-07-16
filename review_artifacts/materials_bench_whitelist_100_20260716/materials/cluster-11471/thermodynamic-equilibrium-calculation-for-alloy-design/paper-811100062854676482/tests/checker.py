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


# === block: score_0 (check id='check_cementite_mn') ===
def score_0(artifact, step, ctx):
    gold_table = step['gold']
    tol = step['tolerance']
    temps = list(artifact)  # artifact is list of row dicts
    scores = []
    for row in temps:
        t = float(row['temperature_C'])
        key = str(int(t))
        if key in gold_table:
            expected = gold_table[key]
            try:
                val = float(row['Mn_content_mass_pct'])
            except (ValueError, KeyError):
                score = 0.0
            else:
                diff = abs(val - expected)
                if diff <= tol:
                    score = 1.0
                else:
                    score = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='check_equilibrium_ms') ===
def score_1(artifact, step, ctx):
    gold_table = step['gold']
    tol = step['tolerance']
    check_inc = step.get('check_increasing', True)
    rows = artifact
    data = []
    for row in rows:
        try:
            t = float(row['temperature_C'])
            ms = float(row['Ms_C'])
        except (ValueError, KeyError):
            continue
        data.append((t, ms))
    if not data:
        return 0.0
    data.sort(key=lambda x: x[0])
    # monotonic increase check
    monotonic_score = 1.0
    if check_inc and len(data) >= 2:
        for i in range(1, len(data)):
            if data[i][1] <= data[i-1][1]:
                monotonic_score = 0.0
                break
    # point accuracy
    point_scores = []
    for t, ms in data:
        key = str(int(t))
        if key in gold_table:
            expected = gold_table[key]
            diff = abs(ms - expected)
            if diff <= tol:
                ps = 1.0
            else:
                ps = max(0.0, 1.0 - (diff - tol) / tol)
            point_scores.append(ps)
    if not point_scores:
        return monotonic_score if check_inc else 0.0
    point_accuracy = sum(point_scores) / len(point_scores)
    # blend: 80% point accuracy, 20% monotonic
    return 0.8 * point_accuracy + 0.2 * monotonic_score


# === block: score_2 (check id='check_paraeq_driving') ===
def score_2(artifact, step, ctx):
    gold_table = step['gold']
    tol = step['tolerance']
    check_order = step.get('check_ordering', True)
    rows = artifact
    row_scores = []
    for row in rows:
        try:
            t = float(row['temperature_C'])
            cp = float(row['driving_force_gamma_cp_J_per_mol'])
            ap = float(row['driving_force_gamma_ap_J_per_mol'])
        except (ValueError, KeyError):
            continue
        key = str(int(t))
        if key not in gold_table:
            continue
        gold_cp, gold_ap = gold_table[key]
        # ordering score
        order_score = 1.0 if cp > ap else 0.0
        # value scores
        diff_cp = abs(cp - gold_cp)
        if diff_cp <= tol:
            score_cp = 1.0
        else:
            score_cp = max(0.0, 1.0 - (diff_cp - tol) / tol)
        diff_ap = abs(ap - gold_ap)
        if diff_ap <= tol:
            score_ap = 1.0
        else:
            score_ap = max(0.0, 1.0 - (diff_ap - tol) / tol)
        force_score = (score_cp + score_ap) / 2.0
        row_score = 0.5 * order_score + 0.5 * force_score
        row_scores.append(row_score)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_3 (check id='check_paraeq_ms') ===
def score_3(artifact, step, ctx):
    gold_ms = step['gold']
    tol = step['tolerance']
    text = artifact  # artifact is a string
    val = None
    try:
        val = float(text.strip().split()[0])
    except Exception:
        return 0.0
    if val is None:
        return 0.0
    diff = abs(val - gold_ms)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


_SCORERS = {
    'check_cementite_mn': score_0,
    'check_equilibrium_ms': score_1,
    'check_paraeq_driving': score_2,
    'check_paraeq_ms': score_3,
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
