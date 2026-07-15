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
    return {}


# === block: score_0 (check id='step_defect_formation_energies') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact  # list of dicts from CSV
        gold = step['gold']
        tol = step['tolerance']
        defects = list(gold.keys())
        data = {}
        for r in rows:
            name = r.get('defect', '').strip()
            try:
                val = float(r.get('formation_energy_eV'))
                data[name] = val
            except (ValueError, TypeError):
                continue
        scores = []
        for d in defects:
            ref = gold[d]
            agent_val = data.get(d, None)
            if agent_val is None:
                scores.append(0.0)
                continue
            diff = abs(agent_val - ref)
            if diff <= tol:
                score = 1.0
            else:
                score = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


# === block: score_1 (check id='step_formation_order') ===
def score_1(artifact, step, ctx):
    try:
        rows = artifact
        data = {}
        for r in rows:
            name = r.get('defect', '').strip()
            try:
                val = float(r.get('formation_energy_eV'))
                data[name] = val
            except (ValueError, TypeError):
                continue
        required = ['AsV','As2V','As3V','As4V','V2','As2V2','As4V2','As6V2','As2I','As4I']
        # Check all required defects exist
        for d in required:
            if d not in data:
                return 0.0
        # Evaluate rules
        def lt(a,b):
            return data.get(a, float('inf')) < data.get(b, float('-inf'))
        rules = [
            lt('As4V','As3V') and lt('As3V','As2V') and lt('As2V','AsV'),
            lt('As4V2','As2V2') and lt('As2V2','V2'),
            lt('As6V2','As4V2'),
            lt('As4I','As2I')
        ]
        if all(rules):
            return 1.0
        return 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='step_migration_barriers') ===
def score_2(artifact, step, ctx):
    try:
        data = artifact  # dict
        gold = step['gold']
        tol = step['tolerance']
        keys = list(gold.keys())
        scores = []
        for k in keys:
            if k not in data:
                scores.append(0.0)
                continue
            ref = gold[k]['activation_energy_eV']
            try:
                agent_val = float(data[k].get('activation_energy_eV'))
            except (ValueError, TypeError, AttributeError):
                scores.append(0.0)
                continue
            diff = abs(agent_val - ref)
            if diff <= tol:
                score = 1.0
            else:
                score = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


_SCORERS = {
    'step_defect_formation_energies': score_0,
    'step_formation_order': score_1,
    'step_migration_barriers': score_2,
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
