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
        steps = spec.get('steps', [])
        mare_step = next(s for s in steps if s['id'] == 'mare_check')
        ordering_step = next(s for s in steps if s['id'] == 'ordering_check')
        return {
            "gold": mare_step.get("paper_values", {}),
            "mare_full": mare_step.get("mare_full_credit_threshold", 0.20),
            "mare_zero": mare_step.get("mare_zero_credit_threshold", 0.50),
            "expected_orders": ordering_step.get("expected_orders", {})
        }


# === block: score_0 (check id='mare_check') ===
def score_0(artifact, step, ctx):
        # Robust: return 0.0 if artifact is not a dictionary
        if not isinstance(artifact, dict):
            return 0.0
        gold = ctx["gold"]
        mare_full = ctx["mare_full"]
        mare_zero = ctx["mare_zero"]
        for key in gold:
            if key not in artifact:
                return 0.0
            try:
                float(artifact[key])
            except (ValueError, TypeError):
                return 0.0
        total_rel = 0.0
        count = 0
        for key in gold:
            try:
                val = float(artifact[key])
            except Exception:
                return 0.0
            gold_val = gold[key]
            if gold_val != 0.0:
                total_rel += abs(val - gold_val) / abs(gold_val)
            else:
                total_rel += abs(val - gold_val) / 1e-6
            count += 1
        if count == 0:
            return 0.0
        mare = total_rel / count
        if mare <= mare_full:
            return 1.0
        if mare >= mare_zero:
            return 0.0
        return max(0.0, min(1.0, (mare_zero - mare) / (mare_zero - mare_full)))


# === block: score_1 (check id='ordering_check') ===
def score_1(artifact, step, ctx):
    expected = ctx["expected_orders"]
    score = 0.0
    for compound in ["UPt3", "CeAl3"]:
        comparisons = expected.get(compound, [])
        if not comparisons:
            continue
        all_ok = True
        for cmp in comparisons:
            gkey = cmp["greater"]
            lkey = cmp["less"]
            if gkey not in artifact or lkey not in artifact:
                all_ok = False
                break
            try:
                gval = float(artifact[gkey])
                lval = float(artifact[lkey])
            except (ValueError, TypeError):
                all_ok = False
                break
            if not (gval > lval):
                all_ok = False
                break
        if all_ok:
            score += 0.5
    return score


_SCORERS = {
    'mare_check': score_0,
    'ordering_check': score_1,
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
