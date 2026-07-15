import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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


# === block: score_0 (check id='tc_vs_b0_score') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = step.get('gold', {})
        tolerance_rel = float(step.get('tolerance_rel', 0.2))
        tolerance_abs = float(step.get('tolerance_abs', 0.5))
        required_b0 = step.get('required_b0', [-0.2, -0.1, 0.0, 0.1, 0.2, 0.5])
        if not artifact:
            return 0.0
        b0_tc = {}
        for row in artifact:
            try:
                b0_val = float(row.get('b0', None))
                tc_val = float(row.get('Tc', None))
                b0_tc[b0_val] = tc_val
            except (ValueError, TypeError):
                continue
        # Check presence of all required b0
        for b0 in required_b0:
            if b0 not in b0_tc:
                return 0.0
        # Accuracy scores
        point_scores = []
        for b0 in required_b0:
            tc_val = b0_tc[b0]
            gold_tc = gold.get(str(b0), None)
            if gold_tc is None:
                point_scores.append(1.0)
                continue
            if abs(gold_tc) < 1e-12:
                score = 1.0 if abs(tc_val) <= tolerance_abs else 0.0
            else:
                rel_err = abs(tc_val - gold_tc) / abs(gold_tc)
                abs_err = abs(tc_val - gold_tc)
                if rel_err <= tolerance_rel or abs_err <= tolerance_abs:
                    score = 1.0
                else:
                    excess = max(rel_err - tolerance_rel, 0)
                    score = max(0.0, 1.0 - excess / 0.5)
                    if abs_err > tolerance_abs and score > 0:
                        score = max(score, max(0.0, 1.0 - (abs_err - tolerance_abs) / 2.0))
            point_scores.append(score)
        mean_point = sum(point_scores) / len(point_scores) if point_scores else 0.0
        # Monotonic trend: Tc should increase as b0 decreases
        sorted_req = sorted(required_b0, reverse=True)
        tcs = [b0_tc[b] for b in sorted_req if b in b0_tc]
        if len(tcs) < 2:
            trend_score = 0.0
        else:
            trend_ok = all(tcs[i] <= tcs[i+1] for i in range(len(tcs)-1))
            trend_score = 1.0 if trend_ok else 0.0
        final = 0.7 * mean_point + 0.3 * trend_score
        return final


_SCORERS = {
    'tc_vs_b0_score': score_0,
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
