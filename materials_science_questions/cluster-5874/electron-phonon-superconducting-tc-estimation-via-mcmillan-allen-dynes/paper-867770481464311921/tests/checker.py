import os
import json
import csv

# === author imports / helpers ===
import re, math, os


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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    try:
        content = artifact
        floats = [float(x) for x in content.strip().split()]
        if len(floats) != 3:
            return 0.0
        E1, E2, E3 = floats
        threshold = step.get('stability_threshold', 0.0)
        # K2C6H6 (x=2) must be the STRICTLY most stable phase, with a meaningful energy margin
        if not (E2 < E1 and E2 < E3 and (E1 - E2) > threshold and (E3 - E2) > threshold):
            return 0.0
        gold = step.get('gold_formation_energies', None)
        if gold is not None and len(gold) == 3:
            tol = step.get('tolerance_abs', 5.0)
            if all(abs(floats[i] - gold[i]) <= tol for i in range(3)):
                return 1.0
            else:
                return 0.5  # correct ordering but magnitudes off
        return 1.0
    except Exception:
        return 0.0


# === block: score_1 (check id='lattice_constants') ===
def score_1(artifact, step, ctx):
    try:
        content = artifact
        floats = [float(x) for x in content.strip().split()]
        if len(floats) != 3:
            return 0.0
        gold = step.get('gold_lattice_constants', [8.605, 10.705, 6.415])
        tol = step.get('tolerance_abs', 0.1)
        scores = []
        for val, g in zip(floats, gold):
            diff = abs(val - g)
            s = max(0.0, 1.0 - diff / tol) if tol > 0 else 1.0
            scores.append(s)
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


# === block: score_2 (check id='volume_expansion') ===
def score_2(artifact, step, ctx):
    try:
        content = artifact
        exp = float(content.strip())
        gold = step.get('gold_volume_expansion', 26.9)
        tol = step.get('tolerance_abs', 2.0)
        diff = abs(exp - gold)
        return max(0.0, 1.0 - diff / tol) if tol > 0 else 1.0
    except Exception:
        return 0.0


# === block: score_3 (check id='tc') ===
def score_3(artifact, step, ctx):
    try:
        content = artifact
        Tc = float(content.strip())
        gold = step.get('gold_tc', 6.2)
        tol = step.get('tolerance_abs', 1.0)
        diff = abs(Tc - gold)
        return max(0.0, 1.0 - diff / tol) if tol > 0 else 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'formation_energies': score_0,
    'lattice_constants': score_1,
    'volume_expansion': score_2,
    'tc': score_3,
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
