import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    step01_gold = None
    step02_gold = None
    step03_gold = None
    step04_gold = None
    step04_tol = 20.0
    for step in spec.get("steps", []):
        if step["id"] == "step_01":
            step01_gold = step.get("gold_params")
        elif step["id"] == "step_02":
            step02_gold = step.get("gold_table")
            step02_tol = step.get("tolerances", {})
        elif step["id"] == "step_03":
            step03_gold = step.get("gold_table")
            step03_tol = step.get("tolerances", {})
        elif step["id"] == "step_04":
            step04_gold = step.get("gold_temp")
            step04_tol = step.get("tolerance_K", 20.0)
    return {
        "step01_gold": step01_gold,
        "step02_gold": step02_gold,
        "step02_tol": step02_tol or {},
        "step03_gold": step03_gold,
        "step03_tol": step03_tol or {},
        "step04_gold": step04_gold,
        "step04_tol": step04_tol
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = ctx.get("step01_gold")
    if not gold:
        return 0.0
    required = ["p1","p2","rho1","rho2","rho3","rho4","rho5","rho6","rho7","rho8","rho9","a1","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","m","n","eps","d","alpha","cutoff"]
    for key in required:
        if key not in artifact:
            return 0.0
        try:
            if abs(float(artifact[key]) - float(gold[key])) > 0.0001:
                return 0.0
        except (ValueError, TypeError):
            return 0.0
    return 1.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_table = ctx.get("step02_gold")
    tolerances = ctx.get("step02_tol", {})
    if not gold_table:
        return 0.0
    fields = ["density_gcm3", "U_pot_kJmol", "K_T_GPa", "D_cm2s", "viscosity_cP"]
    gold_by_T = {}
    for row in gold_table:
        k = row["T_K"]
        gold_by_T[k] = row
    agent_by_T = {}
    for row in artifact:
        t = row.get("T_K", "").strip()
        if t:
            agent_by_T[t] = row
    num_fields = len(fields)
    scores = []
    for field in fields:
        matched = 0
        total = len(gold_by_T)
        tol = float(tolerances.get(field, 1e9))
        for t, gold_row in gold_by_T.items():
            agent_row = agent_by_T.get(t)
            if not agent_row:
                continue
            try:
                val = float(agent_row.get(field, 0))
                gold_val = float(gold_row[field])
                if abs(val - gold_val) <= tol:
                    matched += 1
            except (ValueError, TypeError):
                pass
        field_score = matched / total if total > 0 else 0.0
        scores.append(field_score)
    return sum(scores) / num_fields if num_fields > 0 else 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    gold_table = ctx.get("step03_gold")
    tolerances = ctx.get("step03_tol", {})
    if not gold_table:
        return 0.0
    fields = ["Z", "T_model_K", "P_GPa", "U_kJmol"]
    agent_rows = artifact   # list of dicts
    agent_by_Z = {}
    for row in agent_rows:
        z_str = row.get("Z", "").strip()
        try:
            z = float(z_str)
        except:
            continue
        agent_by_Z.setdefault(z, []).append(row)
    num_fields = len(fields)
    scores = []
    for field in fields:
        matched = 0
        total = len(gold_table)
        tol = float(tolerances.get(field, 1e9))
        for gold_row in gold_table:
            gold_z_str = gold_row["Z"]
            gold_z = float(gold_z_str)
            # find closest agent row within Z tolerance
            best_diff = float('inf')
            best_val = None
            for agent_z, rows in agent_by_Z.items():
                if abs(agent_z - gold_z) <= tolerances.get("Z", 0.01):
                    # use first matched row
                    candidate = rows[0]
                    try:
                        val = float(candidate.get(field, 0))
                        best_val = val
                        break
                    except:
                        pass
            if best_val is not None:
                try:
                    gold_val = float(gold_row[field])
                    if abs(best_val - gold_val) <= tol:
                        matched += 1
                except (ValueError, TypeError):
                    pass
        field_score = matched / total if total > 0 else 0.0
        scores.append(field_score)
    return sum(scores) / num_fields if num_fields > 0 else 0.0


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    gold = ctx.get("step04_gold")
    tol = ctx.get("step04_tol", 20.0)
    if gold is None:
        return 0.0
    raw = artifact  # string
    import re
    nums = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", raw)
    if not nums:
        return 0.0
    try:
        val = float(nums[0])
        if abs(val - float(gold)) <= tol:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
