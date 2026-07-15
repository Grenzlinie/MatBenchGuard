import os
import json
import csv

# === author imports / helpers ===
import json
import os


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


# === block: score_0 (check id='binding_energies_distances') ===
def score_0(artifact, step, ctx):
    import math
    def score(artifact, step, ctx):
        gold_list = step["gold"]
        tol = step["tolerances"]
        gold_map = {g["metal"]: g for g in gold_list}
        scored_metals = 0
        total_score = 0.0
        for entry in artifact:
            metal = entry.get("metal")
            if metal not in gold_map:
                continue
            g = gold_map[metal]
            e_score = 1.0 if abs(entry.get("E_b", 0) - g["E_b"]) <= tol["E_b"] else 0.0
            d_score = 1.0 if abs(entry.get("d_CdTe_M", 0) - g["d_CdTe_M"]) <= tol["d_CdTe_M"] else 0.0
            total_score += (e_score + d_score) / 2.0
            scored_metals += 1
        if scored_metals == 0:
            return 0.0
        avg = total_score / scored_metals
        # ordering checks
        order_E = step["expected_order_E_b"]
        order_d = step["expected_order_d"]
        vals_E = {}
        vals_d = {}
        for entry in artifact:
            m = entry.get("metal")
            if m in gold_map:
                vals_E[m] = entry.get("E_b")
                vals_d[m] = entry.get("d_CdTe_M")
        # monotonicity: non-decreasing for E_b in order_E
        inc_ok = all(vals_E.get(o, float('inf')) for o in order_E)
        if inc_ok:
            e_inc = all(vals_E[order_E[i+1]] >= vals_E[order_E[i]] for i in range(len(order_E)-1))
        else:
            e_inc = False
        # monotonicity for d: non-increasing in order_d
        inc_d_ok = all(vals_d.get(o, float('-inf')) for o in order_d)
        if inc_d_ok:
            d_inc = all(vals_d[order_d[i+1]] <= vals_d[order_d[i]] for i in range(len(order_d)-1))
        else:
            d_inc = False
        ord_score = (1.0 if e_inc else 0.0 + 1.0 if d_inc else 0.0) / 2.0
        return 0.7 * avg + 0.3 * ord_score


# === block: score_1 (check id='adsorption_classification') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = {g["metal"]: g["category"] for g in step["gold"]}
        correct = 0
        total = 0
        for entry in artifact:
            metal = entry.get("metal")
            if metal in gold:
                if entry.get("category") == gold[metal]:
                    correct += 1
                total += 1
        if total == 0:
            return 0.0
        return correct / total


# === block: score_2 (check id='schottky_barriers') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_list = step["gold"]
        tol = step["tolerances"]["SBH"]
        gold_map = {g["metal"]: g for g in gold_list}
        scored = 0
        total = 0
        for entry in artifact:
            metal = entry.get("metal")
            if metal not in gold_map:
                continue
            g = gold_map[metal]
            s_score = 1.0 if abs(entry.get("SBH", 0) - g["SBH"]) <= tol else 0.0
            c_score = 1.0 if entry.get("contact_type") == g["contact_type"] else 0.0
            total += (s_score + c_score) / 2.0
            scored += 1
        if scored == 0:
            return 0.0
        return total / scored


# === block: score_3 (check id='tunneling_barriers') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_list = step["gold"]
        tol = step["tolerances"]
        gold_map = {g["metal"]: g for g in gold_list}
        no_barrier = set(step.get("no_barrier_metals", []))
        scored = 0
        total = 0
        for entry in artifact:
            metal = entry.get("metal")
            if metal not in gold_map:
                continue
            g = gold_map[metal]
            # special handling for no-barrier metals
            if metal in no_barrier:
                dv = entry.get("Delta_V", 0)
                wb = entry.get("w_B", 0)
                tb = entry.get("T_B", 0)
                s = 1.0 if (abs(dv) <= 0.01 and abs(wb) <= 0.01 and abs(tb - 100.0) <= 0.5) else 0.0
                total += s
                scored += 1
            else:
                s_dv = 1.0 if abs(entry.get("Delta_V", 0) - g["Delta_V"]) <= tol["Delta_V"] else 0.0
                s_wb = 1.0 if abs(entry.get("w_B", 0) - g["w_B"]) <= tol["w_B"] else 0.0
                s_tb = 1.0 if abs(entry.get("T_B", 0) - g["T_B"]) <= tol["T_B"] else 0.0
                total += (s_dv + s_wb + s_tb) / 3.0
                scored += 1
        if scored == 0:
            return 0.0
        return total / scored


_SCORERS = {
    'binding_energies_distances': score_0,
    'adsorption_classification': score_1,
    'schottky_barriers': score_2,
    'tunneling_barriers': score_3,
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
