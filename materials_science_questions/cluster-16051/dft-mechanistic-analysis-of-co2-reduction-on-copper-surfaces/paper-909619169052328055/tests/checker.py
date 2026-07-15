import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    # Extract gold values and trends from the grading spec step
    ctx = {}
    for step in spec.get("steps", []):
        if step.get("id") == "free_energies":
            gold = step.get("gold", {})
            ctx["gold_entries"] = gold.get("values", [])
            ctx["trends"] = gold.get("trends", [])
            ctx["sub_weights"] = gold.get("sub_weights", {"value_errors": 0.7, "trends": 0.3})
            break
    return ctx


# === block: score_0 (check id='free_energies') ===
def score_0(artifact, step, ctx):
    # Validate artifact shape
    if not isinstance(artifact, list):
        return 0.0
    # Build lookup {(surface, intermediate): free_energy_eV}
    lookup = {}
    for item in artifact:
        if not isinstance(item, dict):
            continue
        surf = str(item.get("surface", "")).strip()
        inter = str(item.get("intermediate", "")).strip()
        val = item.get("free_energy_eV")
        if isinstance(val, (int, float)):
            lookup[(surf, inter)] = val

    # Score absolute value errors
    gold_entries = ctx["gold_entries"]
    value_scores = []
    for entry in gold_entries:
        key = (entry["surface"], entry["intermediate"])
        actual = lookup.get(key)
        if actual is None:
            value_scores.append(0.0)
            continue
        err = abs(actual - entry["free_energy_eV"])
        tol = entry["tolerance"]
        if err <= tol:
            value_scores.append(1.0)
        else:
            excess = err - tol
            # linear decay to 0 over 0.3 eV beyond tolerance
            score = max(0.0, 1.0 - excess / 0.3)
            value_scores.append(score)
    avg_val = sum(value_scores) / len(value_scores) if value_scores else 0.0

    # Score trends
    trends_data = ctx["trends"]
    trend_scores = []
    for tr in trends_data:
        key1 = (tr["surface1"], tr["intermediate"])
        key2 = (tr["surface2"], tr["intermediate"])
        val1 = lookup.get(key1)
        val2 = lookup.get(key2)
        if val1 is None or val2 is None:
            trend_scores.append(0.0)
            continue
        relation = tr["relation"]
        if relation == "<":
            ok = val1 < val2
        elif relation == ">":
            ok = val1 > val2
        else:
            ok = False
        trend_scores.append(1.0 if ok else 0.0)
    avg_trends = sum(trend_scores) / len(trend_scores) if trend_scores else 0.0

    sub = ctx["sub_weights"]
    combined = sub["value_errors"] * avg_val + sub["trends"] * avg_trends
    return combined


_SCORERS = {
    'free_energies': score_0,
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
