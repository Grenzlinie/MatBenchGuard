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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.1)
    keys = gold.keys()
    scores = []
    for k in keys:
        v = artifact.get(k)
        if v is None or not isinstance(v, (int, float)):
            scores.append(0.0)
            continue
        if abs(v - gold[k]) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_4') ===
def score_1(artifact, step, ctx):
    gold_em = step['gold_Em']
    tol_em = step['tolerance_Em']
    em_keys = gold_em.keys()
    em_scores = []
    for k in em_keys:
        v = artifact.get(k)
        if v is None or not isinstance(v, (int, float)):
            em_scores.append(0.0)
            continue
        if abs(v - gold_em[k]) <= tol_em:
            em_scores.append(1.0)
        else:
            em_scores.append(0.0)
    em_avg = sum(em_scores) / len(em_scores) if em_scores else 0.0

    gold_do = step['gold_Do']
    do_rel = step['Do_rel_tol']
    do_keys = gold_do.keys()
    do_scores = []
    for k in do_keys:
        v = artifact.get(k)
        g = gold_do[k]
        if v is None or not isinstance(v, (int, float)):
            do_scores.append(0.0)
            continue
        if g == 0:
            do_scores.append(0.0)
        else:
            ratio = v / g
            if (1 - do_rel) <= ratio <= (1 + do_rel):
                do_scores.append(1.0)
            else:
                do_scores.append(0.0)
    do_avg = sum(do_scores) / len(do_scores) if do_scores else 0.0

    p = artifact.get('p_factor')
    p_score = 0.0
    if isinstance(p, (int, float)):
        plo, phi = step['p_factor_range']
        if plo <= p <= phi:
            p_score = 1.0

    j1 = artifact.get('J1_Em')
    j2 = artifact.get('J2_Em')
    j3 = artifact.get('J3_Em')
    j4 = artifact.get('J4_Em')
    struct_score = 0.0
    if isinstance(j1, (int, float)) and isinstance(j2, (int, float)) and isinstance(j3, (int, float)) and isinstance(j4, (int, float)):
        conds = [
            j1 < j3,
            j1 < j4,
            abs(j3 - j4) <= 0.05,
            j3 < j2,
            j4 < j2
        ]
        struct_score = sum(1.0 for c in conds if c) / len(conds)

    sub_w = step['sub_weights']
    total = sub_w['Em'] * em_avg + sub_w['Do'] * do_avg + sub_w['p_factor'] * p_score + sub_w['structural'] * struct_score
    return total


_SCORERS = {
    'step_1': score_0,
    'step_4': score_1,
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
