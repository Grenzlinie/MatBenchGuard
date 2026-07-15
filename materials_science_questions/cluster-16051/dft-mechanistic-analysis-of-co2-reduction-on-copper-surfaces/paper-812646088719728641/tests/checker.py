import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    return {"gold_table": spec.get("gold_table", [])}


# === block: score_0 (check id='energy_accuracy') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold_table"]
    tol = step.get("tolerance", 0.15)
    if not artifact:
        return 0.0
    rows_by_key = {}
    for row in artifact:
        key = (str(int(float(row["pH"]))), str(round(float(row["voltage_V_RHE"]), 6)), row["site"])
        rows_by_key[key] = row
    total = len(gold)
    if total == 0:
        return 1.0
    within = 0
    for g in gold:
        key = (str(int(g["pH"])), str(round(g["voltage_V_RHE"], 6)), g["site"])
        row = rows_by_key.get(key)
        if row is None:
            continue
        val = float(row["delta_G_b_eV"])
        err = abs(val - g["delta_G_b_eV"])
        if err <= tol:
            within += 1
    score = within / total if total > 0 else 1.0
    return score


# === block: score_1 (check id='structural') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    from collections import defaultdict
    conds = defaultdict(list)
    for row in artifact:
        ph = int(round(float(row["pH"])))
        v = round(float(row["voltage_V_RHE"]), 6)
        site = row["site"]
        val = float(row["delta_G_b_eV"])
        conds[(ph, v)].append((site, val))
    gold = ctx["gold_table"]
    expected_strongest = {}
    for g in gold:
        ph = int(round(g["pH"]))
        v = round(g["voltage_V_RHE"], 6)
        if (ph, v) not in expected_strongest:
            gold_rows = [r for r in gold if int(round(r["pH"])) == ph and round(r["voltage_V_RHE"], 6) == v]
            if gold_rows:
                best = min(gold_rows, key=lambda r: r["delta_G_b_eV"])
                expected_strongest[(ph, v)] = best["site"]
    ordering_correct = 0
    proximity_correct = 0
    total = 0
    for (ph, v), site_list in conds.items():
        if len(site_list) != 3:
            continue
        min_site = min(site_list, key=lambda x: x[1])[0]
        expected = expected_strongest.get((ph, v))
        if expected is not None and min_site == expected:
            ordering_correct += 1
        b = next((x[1] for x in site_list if x[0] == "bridge"), None)
        h = next((x[1] for x in site_list if x[0] == "hollow"), None)
        if b is not None and h is not None and abs(b - h) <= 0.1:
            proximity_correct += 1
        total += 1
    if total == 0:
        return 0.0
    ord_score = ordering_correct / total
    prox_score = proximity_correct / total
    return 0.6 * ord_score + 0.4 * prox_score


_SCORERS = {
    'energy_accuracy': score_0,
    'structural': score_1,
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
