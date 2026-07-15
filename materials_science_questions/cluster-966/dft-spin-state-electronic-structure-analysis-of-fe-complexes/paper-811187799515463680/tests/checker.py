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
    steps = spec.get("steps", [])
    ref = {}
    tol = {}
    for step in steps:
        if step.get("id") == "check_populations":
            ref = step.get("reference_values", {})
            tol = step.get("tolerances", {})
            break
    return {"ref": ref, "tol": tol}


# === block: score_0 (check id='check_populations') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    ref = ctx["ref"]
    tol = ctx["tol"]
    if not ref or not tol:
        return 0.0
    data = {}
    for row in artifact:
        dimer = row.get("dimer") or row.get("Dimer")
        if dimer:
            data[dimer] = row
    total = 0.0
    cnt = 0
    for dimer, gold in ref.items():
        row = data.get(dimer)
        if not row:
            continue
        for col in ["s_bonding", "d_shielding", "d_bonding"]:
            try:
                val = float(row[col])
                gv = gold[col]
            except (KeyError, ValueError, TypeError):
                continue
            if col == "d_bonding":
                abs_err = abs(val - gv)
                lim = tol.get(col, {}).get("value", 0.001)
                if abs_err <= lim:
                    score = 1.0
                else:
                    score = max(0.0, 1.0 - (abs_err - lim) / lim)
            else:
                if gv == 0:
                    abs_err = abs(val - gv)
                    lim = tol.get(col, {}).get("value", 0.1)
                    if abs_err <= 0.001:
                        score = 1.0
                    else:
                        score = 0.0
                else:
                    rel_err = abs(val - gv) / abs(gv)
                    lim = tol.get(col, {}).get("value", 0.1)
                    if rel_err <= lim:
                        score = 1.0
                    else:
                        score = max(0.0, 1.0 - (rel_err - lim) / lim)
            total += score
            cnt += 1
    if cnt == 0:
        return 0.0
    return total / cnt


# === block: score_1 (check id='check_ordering') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    s_vals = {}
    for row in artifact:
        dimer = row.get("dimer") or row.get("Dimer")
        if dimer:
            try:
                s_vals[dimer] = float(row["s_bonding"])
            except (KeyError, ValueError, TypeError):
                continue
    order = ["FeCu", "FeMn", "Fe2", "FeCo", "FeNi"]
    correct = 0
    total_pairs = len(order) - 1
    if total_pairs == 0:
        return 0.0
    for i in range(total_pairs):
        a = order[i]
        b = order[i+1]
        if a not in s_vals or b not in s_vals:
            continue
        sa = s_vals[a]
        sb = s_vals[b]
        if sa > sb or abs(sa - sb) < 0.01:
            correct += 1
    return correct / total_pairs


_SCORERS = {
    'check_populations': score_0,
    'check_ordering': score_1,
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
