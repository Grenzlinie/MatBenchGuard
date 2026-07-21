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
    for step in spec.get("steps", []):
        sid = step.get("id")
        if "gold_rows" in step:
            ctx[sid + "_gold_rows"] = step["gold_rows"]
        if "ordering_constraints" in step:
            ctx[sid + "_ordering"] = step["ordering_constraints"]
        if "tolerance" in step:
            ctx[sid + "_tol"] = step["tolerance"]
        # also add output_file for reference if needed
        ctx[sid + "_output_file"] = step.get("output_file", "")
    return ctx


# === block: score_0 (check id='adsorption_values') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx.get("adsorption_values_gold_rows", [])
    tol = ctx.get("adsorption_values_tol", 0.03)
    rows = artifact
    agent_map = {}
    for row in rows:
        key = (row.get("cluster","").strip(), row.get("facet","").strip(), row.get("site","").strip())
        try:
            val = float(row["energy_eV"])
        except (KeyError, ValueError):
            continue
        agent_map[key] = val
    correct = 0
    total = len(gold_rows)
    for gold in gold_rows:
        key = (gold["cluster"].strip(), gold["facet"].strip(), gold["site"].strip())
        if key in agent_map and abs(agent_map[key] - gold["energy_eV"]) <= tol:
            correct += 1
    score = correct / total if total > 0 else 1.0
    return score


# === block: score_1 (check id='adsorption_ordering') ===
def score_1(artifact, step, ctx):
    ordering_constraints = ctx.get("adsorption_ordering_ordering", [])
    rows = artifact
    emap = {}
    for row in rows:
        key = (row.get("cluster","").strip(), row.get("facet","").strip(), row.get("site","").strip())
        try:
            emap[key] = float(row["energy_eV"])
        except (KeyError, ValueError):
            continue
    violations = 0
    total = len(ordering_constraints)
    for c in ordering_constraints:
        cluster = c["cluster"].strip()
        low = (cluster, c["lower_energy"]["facet"].strip(), c["lower_energy"]["site"].strip())
        high = (cluster, c["higher_energy"]["facet"].strip(), c["higher_energy"]["site"].strip())
        if low in emap and high in emap:
            if emap[low] > emap[high]:
                violations += 1
    score = 1.0 - (violations / total) if total > 0 else 1.0
    if score < 0:
        score = 0.0
    return score


# === block: score_2 (check id='barrier_values') ===
def score_2(artifact, step, ctx):
    gold_rows = ctx.get("barrier_values_gold_rows", [])
    tol = ctx.get("barrier_values_tol", 0.03)
    agent_map = {}
    for row in artifact:
        key = (row.get("cluster","").strip(), row.get("process","").strip())
        try:
            val = float(row["barrier_eV"])
        except (KeyError, ValueError):
            continue
        agent_map[key] = val
    correct = 0
    total = len(gold_rows)
    for gold in gold_rows:
        key = (gold["cluster"].strip(), gold["process"].strip())
        if key in agent_map and abs(agent_map[key] - gold["barrier_eV"]) <= tol:
            correct += 1
    score = correct / total if total > 0 else 1.0
    return score


_SCORERS = {
    'adsorption_values': score_0,
    'adsorption_ordering': score_1,
    'barrier_values': score_2,
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
