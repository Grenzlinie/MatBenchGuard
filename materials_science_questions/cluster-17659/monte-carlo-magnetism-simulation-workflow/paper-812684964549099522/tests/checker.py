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
    import math
    conditions = [(100, 0.5), (100, 1.0), (1024, 0.5), (1024, 1.0), (10000, 0.5), (10000, 1.0)]
    a_2d = 258.6
    gold = []
    for N, T_J in conditions:
        M = (1.0 / (2 * N)) ** (T_J / (8 * math.pi))
        chi = (1.0 / (2 * a_2d)) * N * (M ** 2) * T_J
        gold.append({'N': N, 'T_J': T_J, 'M_gold': M, 'chi_gold': chi})
    return {'gold_conditions': gold, 'conditions': conditions}


# === block: score_0 (check id='magnetization_accuracy') ===
def score_0(artifact, step, ctx):
    gold_cond = ctx['gold_conditions']
    rows = artifact
    reported = {}
    for row in rows:
        try:
            key = (int(row['N']), round(float(row['T_J']), 2))
            reported[key] = float(row['M_mean'])
        except (ValueError, KeyError):
            pass
    scores = []
    for g in gold_cond:
        key = (g['N'], g['T_J'])
        M_rep = reported.get(key)
        if M_rep is None:
            scores.append(0.0)
            continue
        M_gold = g['M_gold']
        if M_gold == 0.0:
            rel_err = 0.0 if M_rep == 0.0 else 1.0
        else:
            rel_err = abs(M_rep - M_gold) / abs(M_gold)
        if rel_err <= 0.01:
            s = 1.0
        elif rel_err <= 0.05:
            s = 1.0 - (rel_err - 0.01) / 0.04 * 0.3
        elif rel_err <= 0.10:
            s = 0.7 - (rel_err - 0.05) / 0.05 * 0.7
        else:
            s = 0.0
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='susceptibility_accuracy') ===
def score_1(artifact, step, ctx):
    gold_cond = ctx['gold_conditions']
    rows = artifact
    reported = {}
    for row in rows:
        try:
            key = (int(row['N']), round(float(row['T_J']), 2))
            reported[key] = float(row['chi'])
        except (ValueError, KeyError):
            pass
    scores = []
    for g in gold_cond:
        key = (g['N'], g['T_J'])
        chi_rep = reported.get(key)
        if chi_rep is None:
            scores.append(0.0)
            continue
        chi_gold = g['chi_gold']
        if chi_gold == 0.0:
            rel_err = 0.0 if chi_rep == 0.0 else 1.0
        else:
            rel_err = abs(chi_rep - chi_gold) / abs(chi_gold)
        if rel_err <= 0.02:
            s = 1.0
        elif rel_err <= 0.15:
            s = 1.0 - (rel_err - 0.02) / 0.13
        else:
            s = 0.0
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='moment_constancy') ===
def score_2(artifact, step, ctx):
    rows = artifact
    z4_list = []
    z6_list = []
    for row in rows:
        try:
            z4_list.append(float(row['z4']))
            z6_list.append(float(row['z6']))
        except (ValueError, KeyError):
            pass
    if not z4_list or not z6_list:
        return 0.0
    mean_z4 = sum(z4_list) / len(z4_list)
    mean_z6 = sum(z6_list) / len(z6_list)
    max_dev_z4 = max(abs(z - mean_z4) for z in z4_list) if z4_list else 0.0
    max_dev_z6 = max(abs(z - mean_z6) for z in z6_list) if z6_list else 0.0
    def _score_dev(d):
        if d <= 0.2:
            return 1.0
        if d <= 0.5:
            return max(0.0, 1.0 - (d - 0.2) / 0.3)
        return 0.0
    s_z4 = _score_dev(max_dev_z4)
    s_z6 = _score_dev(max_dev_z6)
    return (s_z4 + s_z6) / 2.0


_SCORERS = {
    'magnetization_accuracy': score_0,
    'susceptibility_accuracy': score_1,
    'moment_constancy': score_2,
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
