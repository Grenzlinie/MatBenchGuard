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
        sid = step["id"]
        if sid == "check_formula":
            ctx["formula_target"] = step.get("target", "x1 = m(m+1)A/(n\u03c3)")
        elif sid == "check_table1":
            ctx["gold_table1"] = step.get("gold_values", {}).get("table1", [])
            ctx["tol_table1"] = step.get("tolerance_relative", 0.02)
        elif sid == "check_table2":
            ctx["gold_table2"] = step.get("gold_values", {}).get("table2", [])
            ctx["tol_table2"] = step.get("tolerance_relative", 0.02)
    return ctx


# === block: score_0 (check id='check_formula') ===
def score_0(artifact, step, ctx):
    agent_formula = artifact.get("asymptotic_formula", "") if isinstance(artifact, dict) else ""
    target = ctx["formula_target"]
    return 1.0 if agent_formula.strip() == target.strip() else 0.0


# === block: score_1 (check id='check_table1') ===
def score_1(artifact, step, ctx):
    agent_table1 = artifact.get("table1", []) if isinstance(artifact, dict) else []
    gold_list = ctx["gold_table1"]
    tol = ctx["tol_table1"]
    if not gold_list or not agent_table1:
        return 0.0
    gold_dict = {(g["p"], g["m"]): g["x1_approx"] for g in gold_list}
    correct = 0
    total = 0
    for entry in agent_table1:
        key = (entry.get("p"), entry.get("m"))
        if key in gold_dict:
            gold_val = gold_dict[key]
            agent_val = entry.get("x1_approx")
            if agent_val is not None:
                rel_err = abs(agent_val - gold_val) / gold_val if gold_val != 0 else abs(agent_val - gold_val)
                if rel_err <= tol:
                    correct += 1
                total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='check_table2') ===
def score_2(artifact, step, ctx):
    agent_table2 = artifact.get("table2", []) if isinstance(artifact, dict) else []
    gold_list = ctx["gold_table2"]
    tol = ctx["tol_table2"]
    if not gold_list or not agent_table2:
        return 0.0
    gold_dict = {(g["p"], g["m"], g.get("n", 10)): g["x1_approx"] for g in gold_list}
    correct = 0
    total = 0
    for entry in agent_table2:
        key = (entry.get("p"), entry.get("m"), entry.get("n"))
        if key in gold_dict:
            gold_val = gold_dict[key]
            agent_val = entry.get("x1_approx")
            if agent_val is not None:
                rel_err = abs(agent_val - gold_val) / gold_val if gold_val != 0 else abs(agent_val - gold_val)
                if rel_err <= tol:
                    correct += 1
                total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='check_structural') ===
def score_3(artifact, step, ctx):
    agent_table1 = artifact.get("table1", []) if isinstance(artifact, dict) else []
    agent_table2 = artifact.get("table2", []) if isinstance(artifact, dict) else []
    score = 0.0
    count_checks = 0
    # For fixed m, x1_approx should decrease with p (table1)
    for m in [0.5, 1.0, 2.0]:
        entries = [e for e in agent_table1 if e.get("m") == m]
        entries.sort(key=lambda x: x.get("p"))
        if len(entries) < 2:
            continue
        prev = entries[0].get("x1_approx")
        for e in entries[1:]:
            curr = e.get("x1_approx")
            if prev is not None and curr is not None and curr <= prev + 1e-12:
                score += 1.0
            count_checks += 1
            prev = curr
    # Table2 same
    for m in [0.5, 1.0, 2.0]:
        entries = [e for e in agent_table2 if e.get("m") == m]
        entries.sort(key=lambda x: x.get("p"))
        if len(entries) < 2:
            continue
        prev = entries[0].get("x1_approx")
        for e in entries[1:]:
            curr = e.get("x1_approx")
            if prev is not None and curr is not None and curr <= prev + 1e-12:
                score += 1.0
            count_checks += 1
            prev = curr
    # For fixed p, x1_approx should increase with m (table1)
    for p in range(1, 10):
        entries = [e for e in agent_table1 if e.get("p") == p]
        vals = {}
        for e in entries:
            vals[e.get("m")] = e.get("x1_approx")
        prev_v = vals.get(0.5)
        for m in [1.0, 2.0]:
            cur_v = vals.get(m)
            if prev_v is not None and cur_v is not None and cur_v >= prev_v - 1e-12:
                score += 1.0
            count_checks += 1
            prev_v = cur_v
    # Table2 same for p=1,2,3
    for p in [1, 2, 3]:
        entries = [e for e in agent_table2 if e.get("p") == p]
        vals = {}
        for e in entries:
            vals[e.get("m")] = e.get("x1_approx")
        prev_v = vals.get(0.5)
        for m in [1.0, 2.0]:
            cur_v = vals.get(m)
            if prev_v is not None and cur_v is not None and cur_v >= prev_v - 1e-12:
                score += 1.0
            count_checks += 1
            prev_v = cur_v
    if count_checks == 0:
        return 1.0
    return score / count_checks


_SCORERS = {
    'check_formula': score_0,
    'check_table1': score_1,
    'check_table2': score_2,
    'check_structural': score_3,
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
