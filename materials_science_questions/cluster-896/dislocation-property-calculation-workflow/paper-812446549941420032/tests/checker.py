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


# === block: score_0 (check id='s03') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol_abs = step.get('tolerances', {}).get('abs', 0.005)
    rel_tol = step.get('tolerances', {}).get('rel', 0.05)
    if not artifact:
        return 0.0
    agent_map = {}
    for row in artifact:
        lt = row.get('ledge_type', '').strip()
        try:
            val = float(row.get('gamma_large_spacing', 'nan'))
        except:
            continue
        agent_map[lt] = val
    total = len(gold)
    if total == 0:
        return 1.0
    matched = 0
    for lt, gval in gold.items():
        aval = agent_map.get(lt)
        if aval is None:
            continue
        allowed = tol_abs if gval == 0 else max(tol_abs, rel_tol * abs(gval))
        if abs(aval - gval) <= allowed:
            matched += 1
    return matched / total


# === block: score_1 (check id='s06') ===
def score_1(artifact, step, ctx):
    gold_rows = step['gold_rows']
    tol_delta = step.get('tolerances', {}).get('abs_delta', 0.02)
    tol_gamma = step.get('tolerances', {}).get('abs_gamma', 0.005)
    if not artifact:
        return 0.0
    agent_rows = {}
    for row in artifact:
        try:
            nc = int(float(row.get('N_c', '')))
        except:
            continue
        agent_rows[nc] = row
    total = len(gold_rows)
    if total == 0:
        return 1.0
    passed = 0
    for gr in gold_rows:
        nc = gr['N_c']
        agent_r = agent_rows.get(nc)
        if agent_r is None:
            continue
        ok = True
        if gr.get('Delta_E_ex') is not None:
            try:
                a_val = float(agent_r.get('Delta_E_ex', 'nan'))
            except:
                ok = False
            else:
                if abs(a_val - gr['Delta_E_ex']) > tol_delta:
                    ok = False
        if gr.get('gamma_l') is not None:
            try:
                a_gamma = float(agent_r.get('gamma_l', 'nan'))
            except:
                ok = False
            else:
                if abs(a_gamma - gr['gamma_l']) > tol_gamma:
                    ok = False
        if ok:
            passed += 1
    return passed / total


_SCORERS = {
    's03': score_0,
    's06': score_1,
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
