import os
import json
import csv

# === author imports / helpers ===
import json
import os
import math

def validate_and_score(artifact, step):
    gold_list = step.get("gold", [])
    tolerances = step.get("tolerances", {})
    fields = step.get("fields", [])
    if not isinstance(artifact, list):
        return 0.0
    gold_oris = set(g["orientation"] for g in gold_list)
    artifact_oris = set()
    for entry in artifact:
        if isinstance(entry, dict) and "orientation" in entry:
            artifact_oris.add(entry["orientation"])
    if gold_oris != artifact_oris:
        return 0.0
    gold_map = {g["orientation"]: g for g in gold_list}
    total = 0
    matches = 0
    for entry in artifact:
        ori = entry["orientation"]
        g = gold_map[ori]
        for f in fields:
            if f not in entry or not isinstance(entry[f], (int, float)):
                total += 1
                continue
            val = entry[f]
            tol = tolerances[f]
            rel = tol.get("rel", 0.0)
            abs_tol = tol.get("abs", 0.0)
            expected = g[f]
            if abs(val - expected) <= max(rel * abs(expected), abs_tol):
                matches += 1
            total += 1
    if total == 0:
        return 0.0
    return matches / total


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


# === block: score_0 (check id='structural_energies') ===
def score_0(artifact, step, ctx):
    SKIP_FIELDS = {"h-BN(0001)": {"alpha_avg_deg"}, "WUR(0001)": {"alpha_avg_deg"}}
    gold_list = step.get("gold", [])
    if not isinstance(artifact, list):
        return 0.0
    gold_oris = set(g["orientation"] for g in gold_list)
    artifact_oris = set()
    for entry in artifact:
        if isinstance(entry, dict) and "orientation" in entry:
            artifact_oris.add(entry["orientation"])
    if gold_oris != artifact_oris:
        return 0.0
    gold_map = {g["orientation"]: g for g in gold_list}
    tolerances = step.get("tolerances", {})
    fields = step.get("fields", [])
    total = 0
    matches = 0
    for entry in artifact:
        ori = entry["orientation"]
        g = gold_map[ori]
        skip = SKIP_FIELDS.get(ori, set())
        for f in fields:
            if f in skip:
                continue
            if f not in entry or not isinstance(entry[f], (int, float)):
                total += 1
                continue
            val = entry[f]
            tol = tolerances[f]
            rel = tol.get("rel", 0.0)
            abs_tol = tol.get("abs", 0.0)
            expected = g[f]
            if abs(val - expected) <= max(rel * abs(expected), abs_tol):
                matches += 1
            total += 1
    if total == 0:
        return 0.0
    return matches / total


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    return validate_and_score(artifact, step)


# === block: score_2 (check id='dielectric_constants') ===
def score_2(artifact, step, ctx):
    return validate_and_score(artifact, step)


# === block: score_3 (check id='absorption_anisotropy') ===
def score_3(artifact, step, ctx):
    return validate_and_score(artifact, step)


_SCORERS = {
    'structural_energies': score_0,
    'band_gaps': score_1,
    'dielectric_constants': score_2,
    'absorption_anisotropy': score_3,
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
