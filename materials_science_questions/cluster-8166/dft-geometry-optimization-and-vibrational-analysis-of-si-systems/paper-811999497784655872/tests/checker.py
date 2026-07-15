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
    energies_path = os.path.join(outputs_dir, "total_energies.json")
    ctx = {}
    if os.path.exists(energies_path):
        with open(energies_path) as f:
            ctx['energies'] = json.load(f)
    return ctx


# === block: score_0 (check id='struct_check') ===
def score_0(artifact, step, ctx):
    fields = step.get("fields", [])
    score = 0
    n = len(fields)
    if n == 0:
        return 0.0
    for fdef in fields:
        path = fdef["path"]
        target = fdef["target"]
        tol = fdef["tolerance"]
        val = artifact
        for key in path.split("."):
            if not isinstance(val, dict) or key not in val:
                val = None
                break
            val = val[key]
        if val is not None and abs(val - target) <= tol:
            score += 1
    return score / n


# === block: score_1 (check id='bond_check') ===
def score_1(artifact, step, ctx):
    list_fields = step.get("list_fields", [])
    total = 0
    n_lists = len(list_fields)
    if n_lists == 0:
        return 0.0
    for ldef in list_fields:
        path = ldef["path"]
        expected = ldef["expected_list"]
        tol = ldef["tolerance"]
        parts = path.split(".")
        val = artifact
        for p in parts:
            if not isinstance(val, dict) or p not in val:
                val = None
                break
            val = val[p]
        if not isinstance(val, list):
            list_score = 0.0
        else:
            count = 0
            for i, ev in enumerate(expected):
                if i < len(val) and abs(val[i] - ev) <= tol:
                    count += 1
            list_score = count / len(expected) if expected else 1.0
        total += list_score
    return total / n_lists


# === block: score_2 (check id='energy_check') ===
def score_2(artifact, step, ctx):
    fields = step.get("fields", [])
    score = 0
    n = len(fields)
    if n == 0:
        return 0.0
    for fdef in fields:
        path = fdef["path"]
        target = fdef["target"]
        tol = fdef["tolerance"]
        val = artifact
        for key in path.split("."):
            if not isinstance(val, dict) or key not in val:
                val = None
                break
            val = val[key]
        if val is not None and abs(val - target) <= tol:
            score += 1
    return score / n


# === block: score_3 (check id='voltage_check') ===
def score_3(artifact, step, ctx):
    energies = ctx.get('energies')
    if not energies:
        return 0.0
    try:
        E_LiSi = energies['LiSi_per_fu']
        E_Li   = energies['Li_per_atom']
        E_Si   = energies['Si_per_atom']
        V = -(E_LiSi - E_Li - E_Si)
    except (KeyError, TypeError):
        return 0.0
    target = step.get('voltage_target', 0.405)
    tol = step.get('voltage_tolerance', 0.05)
    diff = abs(V - target)
    if diff <= tol:
        return 1.0
    else:
        scale = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
        return scale


# === block: score_4 (check id='electron_check') ===
def score_4(artifact, step, ctx):
    fields = step.get("fields", [])
    score = 0
    n = len(fields)
    if n == 0:
        return 0.0
    for fdef in fields:
        path = fdef["path"]
        target = fdef["target"]
        tol = fdef["tolerance"]
        val = artifact
        for key in path.split("."):
            if not isinstance(val, dict) or key not in val:
                val = None
                break
            val = val[key]
        if val is not None and abs(val - target) <= tol:
            score += 1
    return score / n


_SCORERS = {
    'struct_check': score_0,
    'bond_check': score_1,
    'energy_check': score_2,
    'voltage_check': score_3,
    'electron_check': score_4,
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
