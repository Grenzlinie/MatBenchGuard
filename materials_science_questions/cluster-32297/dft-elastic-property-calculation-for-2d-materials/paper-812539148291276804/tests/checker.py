import os
import json
import csv

# === author imports / helpers ===
import json
import os

def deep_get(d, path):
    keys = path.split('.')
    for k in keys:
        if not isinstance(d, dict): return None
        if k not in d: return None
        d = d[k]
    return d


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


# === block: score_0 (check id='J_LiCrS2') ===
def score_0(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='J_LiCrSe2') ===
def score_1(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='J_LiCrTe2') ===
def score_2(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_3 (check id='J_NaCrS2') ===
def score_3(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_4 (check id='J_NaCrSe2') ===
def score_4(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_5 (check id='J_NaCrTe2') ===
def score_5(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_6 (check id='TcI_LiCrS2') ===
def score_6(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_7 (check id='TcI_LiCrSe2') ===
def score_7(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_8 (check id='TcI_LiCrTe2') ===
def score_8(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_9 (check id='TcI_NaCrS2') ===
def score_9(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_10 (check id='TcI_NaCrSe2') ===
def score_10(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_11 (check id='TcI_NaCrTe2') ===
def score_11(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_12 (check id='TcH_LiCrS2') ===
def score_12(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_13 (check id='TcH_LiCrSe2') ===
def score_13(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_14 (check id='TcH_LiCrTe2') ===
def score_14(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_15 (check id='TcH_NaCrS2') ===
def score_15(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_16 (check id='TcH_NaCrSe2') ===
def score_16(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_17 (check id='TcH_NaCrTe2') ===
def score_17(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_18 (check id='bg_LiCrSe2_woSOC') ===
def score_18(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_19 (check id='bg_LiCrSe2_wSOC') ===
def score_19(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_20 (check id='bg_NaCrSe2_woSOC') ===
def score_20(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_21 (check id='bg_NaCrSe2_wSOC') ===
def score_21(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_22 (check id='bg_NaCrTe2_woSOC') ===
def score_22(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_23 (check id='bg_NaCrTe2_wSOC') ===
def score_23(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_24 (check id='mob_NaCrS2_x') ===
def score_24(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    # For NaCrS2 hole mobilities, the paper only guarantees > 1e3 cm^2/V s.
    # Convert to a threshold check: >= 1000 cm^2/V s earns full credit.
    if 'NaCrS2' in step.get('field_path', ''):
        return 1.0 if val >= 1000 else 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_25 (check id='mob_NaCrS2_y') ===
def score_25(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    # For NaCrS2 hole mobilities, the paper only guarantees > 1e3 cm^2/V s.
    # Convert to a threshold check: >= 1000 cm^2/V s earns full credit.
    if 'NaCrS2' in step.get('field_path', ''):
        return 1.0 if val >= 1000 else 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_26 (check id='mob_NaCrSe2_x') ===
def score_26(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_27 (check id='mob_NaCrSe2_y') ===
def score_27(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_28 (check id='mob_NaCrTe2_x') ===
def score_28(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


# === block: score_29 (check id='mob_NaCrTe2_y') ===
def score_29(artifact, step, ctx):
    val = deep_get(artifact, step.get('field_path',''))
    if val is None: return 0.0
    target = step.get('target')
    tol = step.get('tolerance', 0.0)
    tol_type = step.get('tolerance_type', 'absolute')
    try:
        if tol_type == 'relative':
            denom = abs(target) if target != 0 else 1.0
            err = abs(val - target) / denom
        else:
            err = abs(val - target)
        return 1.0 if err <= tol else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'J_LiCrS2': score_0,
    'J_LiCrSe2': score_1,
    'J_LiCrTe2': score_2,
    'J_NaCrS2': score_3,
    'J_NaCrSe2': score_4,
    'J_NaCrTe2': score_5,
    'TcI_LiCrS2': score_6,
    'TcI_LiCrSe2': score_7,
    'TcI_LiCrTe2': score_8,
    'TcI_NaCrS2': score_9,
    'TcI_NaCrSe2': score_10,
    'TcI_NaCrTe2': score_11,
    'TcH_LiCrS2': score_12,
    'TcH_LiCrSe2': score_13,
    'TcH_LiCrTe2': score_14,
    'TcH_NaCrS2': score_15,
    'TcH_NaCrSe2': score_16,
    'TcH_NaCrTe2': score_17,
    'bg_LiCrSe2_woSOC': score_18,
    'bg_LiCrSe2_wSOC': score_19,
    'bg_NaCrSe2_woSOC': score_20,
    'bg_NaCrSe2_wSOC': score_21,
    'bg_NaCrTe2_woSOC': score_22,
    'bg_NaCrTe2_wSOC': score_23,
    'mob_NaCrS2_x': score_24,
    'mob_NaCrS2_y': score_25,
    'mob_NaCrSe2_x': score_26,
    'mob_NaCrSe2_y': score_27,
    'mob_NaCrTe2_x': score_28,
    'mob_NaCrTe2_y': score_29,
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
