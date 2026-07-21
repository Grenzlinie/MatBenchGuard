import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, json


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
    gamma_gold = {}
    gamma_tilde_gold = {}
    for step in spec.get('steps', []):
        if step['id'] == 'gamma_check':
            gamma_gold = {float(k): v for k, v in step.get('hidden_gold_gamma', {}).items()}
        elif step['id'] == 'gamma_tilde_check':
            gamma_tilde_gold = {float(k): v for k, v in step.get('hidden_gold_gamma_tilde', {}).items()}
    return {'gamma_gold': gamma_gold, 'gamma_tilde_gold': gamma_tilde_gold}


# === block: score_0 (check id='gamma_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = ctx['gamma_gold']
    scores = []
    for row in rows:
        t = float(row['temperature'])
        if t in gold:
            g = float(row['gamma'])
            ref = gold[t]
            if ref == 0:
                sc = 1.0 if g == 0 else max(0.0, 1.0 - abs(g) / 0.5)
            else:
                err_ratio = abs(g - ref) / abs(ref)
                sc = max(0.0, 1.0 - err_ratio)
            scores.append(sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='gamma_tilde_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold = ctx['gamma_tilde_gold']
    tol_rel = step['tolerance_rel']
    tol_rel_peak = step['tolerance_rel_peak']
    peak_temp = step['peak_temp']
    total = 0.0
    count = 0
    for row in rows:
        t = float(row['temperature'])
        if t in gold:
            gt = float(row['gamma_tilde'])
            g_gold = gold[t]
            tol = tol_rel_peak if abs(t - peak_temp) < 0.001 else tol_rel
            rel_err = abs(gt - g_gold) / (abs(g_gold) if g_gold != 0 else 1.0)
            if rel_err <= tol:
                total += 1.0
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_2 (check id='A2_structural') ===
def score_2(artifact, step, ctx):
    rows = artifact
    a2_dict = {}
    for row in rows:
        t = float(row['temperature'])
        a2 = float(row['A2'])
        a2_dict[t] = a2
    required = [0.3, 0.35, 0.4, 0.45, 0.5]
    for t in required:
        if t not in a2_dict:
            return 0.0
    a2_04 = a2_dict[0.4]
    a2_03 = a2_dict[0.3]
    a2_05 = a2_dict[0.5]
    if a2_04 < a2_dict[0.35] and a2_04 < a2_dict[0.45]:
        if a2_04 < 0.5 * min(a2_03, a2_05):
            return 1.0
    return 0.0


# === block: score_3 (check id='gamma_tilde_self_consistency') ===
def score_3(artifact, step, ctx):
    rows = artifact
    tol = step['tolerance_relative']
    total = 0.0
    count = 0
    for row in rows:
        t = float(row['temperature'])
        a2 = float(row['A2'])
        reported = float(row['gamma_tilde'])
        if a2 == 0:
            total += 0.0
            count += 1
        else:
            expected = (math.pi ** 2) * (t ** 2) / (2 * a2)
            if abs(reported - expected) / max(abs(expected), 1e-9) <= tol:
                total += 1.0
            count += 1
    if count == 0:
        return 0.0
    return total / count


_SCORERS = {
    'gamma_check': score_0,
    'gamma_tilde_check': score_1,
    'A2_structural': score_2,
    'gamma_tilde_self_consistency': score_3,
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
