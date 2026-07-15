import os
import json
import csv

# === author imports / helpers ===
import json
def deep_get(d, path):
    for k in path.split('.'):
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d

def score_numeric(artifact, step):
    val = deep_get(artifact, step['field_path'])
    if val is None or not isinstance(val, (int, float)):
        return 0.0
    gold = step.get('gold')
    tol = step.get('tolerance_abs', 0.0)
    if abs(val - gold) <= tol:
        return 1.0
    return 0.0

def score_exact_string(artifact, step):
    val = deep_get(artifact, step['field_path'])
    if val is None or not isinstance(val, str):
        return 0.0
    return 1.0 if val == step['gold'] else 0.0

def check_shape(artifact, step):
    required = step.get('required_keys', []) or []
    if not isinstance(artifact, dict):
        return 0.0
    for k in required:
        if k not in artifact:
            return 0.0
    return 1.0

def check_file_exists(artifact, step):
    return 1.0

def check_fields_present(artifact, step):
    for p in step.get('required_paths', []) or []:
        if deep_get(artifact, p) is None:
            return 0.0
    return 1.0


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


# === block: score_0 (check id='s01_file_exists') ===
def score_0(artifact, step, ctx):
    return check_file_exists(artifact, step)


# === block: score_1 (check id='s01_shape') ===
def score_1(artifact, step, ctx):
    return check_shape(artifact, step)


# === block: score_2 (check id='s01_bond_length_td') ===
def score_2(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_3 (check id='s01_bond_length_c3v') ===
def score_3(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_4 (check id='s01_displacement') ===
def score_4(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_5 (check id='s01_angle') ===
def score_5(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_6 (check id='s01_stability') ===
def score_6(artifact, step, ctx):
    return score_exact_string(artifact, step)


# === block: score_7 (check id='s01_energy_diff') ===
def score_7(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_8 (check id='s01_total_energies_present') ===
def score_8(artifact, step, ctx):
    return check_fields_present(artifact, step)


# === block: score_9 (check id='s02_file_exists') ===
def score_9(artifact, step, ctx):
    return check_file_exists(artifact, step)


# === block: score_10 (check id='s02_shape') ===
def score_10(artifact, step, ctx):
    return check_shape(artifact, step)


# === block: score_11 (check id='s02_freq_t2') ===
def score_11(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_12 (check id='s02_freq_e') ===
def score_12(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_13 (check id='s02_freq_a1') ===
def score_13(artifact, step, ctx):
    return score_numeric(artifact, step)


# === block: score_14 (check id='s02_ratio') ===
def score_14(artifact, step, ctx):
    return score_numeric(artifact, step)


_SCORERS = {
    's01_file_exists': score_0,
    's01_shape': score_1,
    's01_bond_length_td': score_2,
    's01_bond_length_c3v': score_3,
    's01_displacement': score_4,
    's01_angle': score_5,
    's01_stability': score_6,
    's01_energy_diff': score_7,
    's01_total_energies_present': score_8,
    's02_file_exists': score_9,
    's02_shape': score_10,
    's02_freq_t2': score_11,
    's02_freq_e': score_12,
    's02_freq_a1': score_13,
    's02_ratio': score_14,
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
