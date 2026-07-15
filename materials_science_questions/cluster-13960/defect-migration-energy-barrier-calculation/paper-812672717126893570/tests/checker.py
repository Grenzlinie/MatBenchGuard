import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='step_charge_transfer') ===
def score_0(artifact, step, ctx):
    try:
        artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
        if not isinstance(artifact, dict):
            return 0.0
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.02)
        count = 0
        total = len(gold)
        for key in gold:
            if key in artifact and isinstance(artifact[key], (int, float)):
                if abs(artifact[key] - gold[key]) <= tol:
                    count += 1
        return count / total if total > 0 else 0.0
    except:
        return 0.0


# === block: score_1 (check id='step_h_barrier') ===
def score_1(artifact, step, ctx):
    try:
        artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
        if not isinstance(artifact, dict):
            return 0.0
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.1)
        expected = sum(len(gold[cond]) for cond in gold)
        count = 0
        for cond in gold:
            if cond not in artifact:
                continue
            cond_art = artifact[cond]
            if not isinstance(cond_art, dict):
                continue
            for field in gold[cond]:
                if field in cond_art and isinstance(cond_art[field], (int, float)):
                    if abs(cond_art[field] - gold[cond][field]) <= tol:
                        count += 1
        return count / expected if expected > 0 else 0.0
    except:
        return 0.0


# === block: score_2 (check id='step_pdos_integrated') ===
def score_2(artifact, step, ctx):
    try:
        rows = artifact
        gold = step.get('gold', {})
        tol = step.get('tolerance', 0.15)
        expected_vals = len(gold)
        count = 0
        seen = set()
        for row in rows:
            x = str(row.get('x', '')).strip()
            area_str = row.get('integrated_area', '')
            if not x or not area_str:
                continue
            try:
                area = float(area_str)
            except ValueError:
                continue
            if x in gold and x not in seen:
                g = gold[x]
                if g != 0:
                    if abs(area - g) <= tol * abs(g):
                        count += 1
                else:
                    if abs(area) <= tol:
                        count += 1
                seen.add(x)
        return count / expected_vals if expected_vals > 0 else 0.0
    except:
        return 0.0


_SCORERS = {
    'step_charge_transfer': score_0,
    'step_h_barrier': score_1,
    'step_pdos_integrated': score_2,
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
