import os
import json
import csv

# === author imports / helpers ===
import math

def score_comp(value, target, tol_type, tol_val):
    if value is None:
        return 0.0
    if tol_type == "threshold":
        if value >= target:
            return 1.0
        elif target > 0:
            return max(0.0, value / target)
        else:
            return 1.0 if value >= target else 0.0
    elif tol_type == "abs":
        diff = abs(value - target)
        if diff <= tol_val:
            return 1.0
        else:
            return max(0.0, 1.0 - (diff - tol_val) / tol_val)
    elif tol_type == "rel":
        if target == 0:
            return 1.0 if abs(value) <= tol_val else 0.0
        rel_diff = abs(value - target) / abs(target)
        if rel_diff <= tol_val:
            return 1.0
        else:
            return max(0.0, 1.0 - (rel_diff - tol_val) / tol_val)
    else:
        return 0.0


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


# === block: score_0 (check id='Cr_energy_diff_FM_NSP') ===
def score_0(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_1 (check id='Cr_energy_diff_FM_AFM') ===
def score_1(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_2 (check id='Cr_local_magnetic_moment') ===
def score_2(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_3 (check id='Cr_spin_up_band_gap') ===
def score_3(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_4 (check id='Cr_spin_down_band_gap') ===
def score_4(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_5 (check id='Cr_Curie_temperature') ===
def score_5(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_6 (check id='Mn_energy_diff_FM_NSP') ===
def score_6(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_7 (check id='Mn_energy_diff_FM_AFM') ===
def score_7(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_8 (check id='Mn_local_magnetic_moment') ===
def score_8(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_9 (check id='Mn_spin_up_band_gap') ===
def score_9(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_10 (check id='Mn_spin_down_band_gap') ===
def score_10(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_11 (check id='Mn_Curie_temperature') ===
def score_11(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_12 (check id='Fe_energy_diff_FM_NSP') ===
def score_12(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_13 (check id='Fe_energy_diff_FM_AFM') ===
def score_13(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_14 (check id='Fe_local_magnetic_moment') ===
def score_14(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_15 (check id='Fe_spin_up_band_gap') ===
def score_15(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_16 (check id='Fe_spin_down_band_gap') ===
def score_16(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


# === block: score_17 (check id='Fe_Curie_temperature') ===
def score_17(artifact, step, ctx):
    field_path = step["field_path"]
    parts = field_path.split(".")
    val = artifact
    for p in parts:
        val = val[p]
    return score_comp(val, step["target"], step["tolerance_type"], step["tolerance_value"])


_SCORERS = {
    'Cr_energy_diff_FM_NSP': score_0,
    'Cr_energy_diff_FM_AFM': score_1,
    'Cr_local_magnetic_moment': score_2,
    'Cr_spin_up_band_gap': score_3,
    'Cr_spin_down_band_gap': score_4,
    'Cr_Curie_temperature': score_5,
    'Mn_energy_diff_FM_NSP': score_6,
    'Mn_energy_diff_FM_AFM': score_7,
    'Mn_local_magnetic_moment': score_8,
    'Mn_spin_up_band_gap': score_9,
    'Mn_spin_down_band_gap': score_10,
    'Mn_Curie_temperature': score_11,
    'Fe_energy_diff_FM_NSP': score_12,
    'Fe_energy_diff_FM_AFM': score_13,
    'Fe_local_magnetic_moment': score_14,
    'Fe_spin_up_band_gap': score_15,
    'Fe_spin_down_band_gap': score_16,
    'Fe_Curie_temperature': score_17,
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
