import os
import json
import csv

# === author imports / helpers ===
# no extra imports needed; builtins only


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


# === block: score_0 (check id='lattice_constant_a') ===
def score_0(artifact, step, ctx):
    v = artifact.get('lattice_constant_a')
    if v is None:
        return 0.0
    return 1.0 if abs(v - 3.257) <= 0.02 else 0.0


# === block: score_1 (check id='lattice_constant_b') ===
def score_1(artifact, step, ctx):
    v = artifact.get('lattice_constant_b')
    if v is None:
        return 0.0
    return 1.0 if abs(v - 3.959) <= 0.02 else 0.0


# === block: score_2 (check id='band_gap') ===
def score_2(artifact, step, ctx):
    v = artifact.get('band_gap_SOC')
    if v is None:
        return 0.0
    # threshold_or_better: larger gap is better; accept any value >= paper value - tolerance
    return 1.0 if v >= 76.0 - 5.0 else 0.0


# === block: score_3 (check id='C11') ===
def score_3(artifact, step, ctx):
    v = artifact.get('C11')
    if v is None:
        return 0.0
    return 1.0 if abs((v - 130.67) / 130.67) <= 0.10 else 0.0


# === block: score_4 (check id='C22') ===
def score_4(artifact, step, ctx):
    v = artifact.get('C22')
    if v is None:
        return 0.0
    return 1.0 if abs((v - 215.81) / 215.81) <= 0.10 else 0.0


# === block: score_5 (check id='C12') ===
def score_5(artifact, step, ctx):
    v = artifact.get('C12')
    if v is None:
        return 0.0
    return 1.0 if abs((v - 17.08) / 17.08) <= 0.10 else 0.0


# === block: score_6 (check id='C66') ===
def score_6(artifact, step, ctx):
    v = artifact.get('C66')
    if v is None:
        return 0.0
    return 1.0 if abs((v - 53.45) / 53.45) <= 0.10 else 0.0


# === block: score_7 (check id='e31') ===
def score_7(artifact, step, ctx):
    v = artifact.get('e31')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.593)) <= 0.05 else 0.0


# === block: score_8 (check id='e31_electronic') ===
def score_8(artifact, step, ctx):
    v = artifact.get('e31_electronic')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.612)) <= 0.05 else 0.0


# === block: score_9 (check id='e31_ionic') ===
def score_9(artifact, step, ctx):
    v = artifact.get('e31_ionic')
    if v is None:
        return 0.0
    return 1.0 if abs(v - 0.019) <= 0.05 else 0.0


# === block: score_10 (check id='e32') ===
def score_10(artifact, step, ctx):
    v = artifact.get('e32')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.545)) <= 0.05 else 0.0


# === block: score_11 (check id='e32_electronic') ===
def score_11(artifact, step, ctx):
    v = artifact.get('e32_electronic')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.513)) <= 0.05 else 0.0


# === block: score_12 (check id='e32_ionic') ===
def score_12(artifact, step, ctx):
    v = artifact.get('e32_ionic')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.032)) <= 0.05 else 0.0


# === block: score_13 (check id='d31') ===
def score_13(artifact, step, ctx):
    v = artifact.get('d31')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.425)) <= 0.05 else 0.0


# === block: score_14 (check id='d32') ===
def score_14(artifact, step, ctx):
    v = artifact.get('d32')
    if v is None:
        return 0.0
    return 1.0 if abs(v - (-0.219)) <= 0.05 else 0.0


# === block: score_15 (check id='Z2') ===
def score_15(artifact, step, ctx):
    v = artifact.get('Z2')
    return 1.0 if v == 1 else 0.0


# === block: score_16 (check id='phonon_stable') ===
def score_16(artifact, step, ctx):
    v = artifact.get('phonon_stable')
    return 1.0 if v is True else 0.0


_SCORERS = {
    'lattice_constant_a': score_0,
    'lattice_constant_b': score_1,
    'band_gap': score_2,
    'C11': score_3,
    'C22': score_4,
    'C12': score_5,
    'C66': score_6,
    'e31': score_7,
    'e31_electronic': score_8,
    'e31_ionic': score_9,
    'e32': score_10,
    'e32_electronic': score_11,
    'e32_ionic': score_12,
    'd31': score_13,
    'd32': score_14,
    'Z2': score_15,
    'phonon_stable': score_16,
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
