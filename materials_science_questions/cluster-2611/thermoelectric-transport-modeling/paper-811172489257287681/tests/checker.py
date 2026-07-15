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
    import json
    with open('/app/outputs/final_results.json') as f:
        data = json.load(f)
    return {'data': data}


# === block: score_0 (check id='val_ZrSe2_kappa_l_300K') ===
def score_0(artifact, step, ctx):
    val = ctx['data'].get('ZrSe2_kappa_l_300K')
    if val is None:
        return 0.0
    gold = step['gold']
    tol = step['tolerance']
    return 1.0 if abs(val - gold) <= tol else 0.0


# === block: score_1 (check id='val_HfSe2_kappa_l_300K') ===
def score_1(artifact, step, ctx):
    val = ctx['data'].get('HfSe2_kappa_l_300K')
    if val is None: return 0.0
    return 1.0 if abs(val - 1.8) <= 0.5 else 0.0


# === block: score_2 (check id='val_ZrSe2_ZT_n_max_600K') ===
def score_2(artifact, step, ctx):
    val = ctx['data'].get('ZrSe2_ZT_n_max_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.95) <= 0.15 else 0.0


# === block: score_3 (check id='val_ZrSe2_ZT_p_max_600K') ===
def score_3(artifact, step, ctx):
    val = ctx['data'].get('ZrSe2_ZT_p_max_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.87) <= 0.15 else 0.0


# === block: score_4 (check id='val_HfSe2_ZT_n_max_600K') ===
def score_4(artifact, step, ctx):
    val = ctx['data'].get('HfSe2_ZT_n_max_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.97) <= 0.15 else 0.0


# === block: score_5 (check id='val_HfSe2_ZT_p_max_600K') ===
def score_5(artifact, step, ctx):
    val = ctx['data'].get('HfSe2_ZT_p_max_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.88) <= 0.15 else 0.0


# === block: score_6 (check id='val_n_opt_n_type_600K') ===
def score_6(artifact, step, ctx):
    val = ctx['data'].get('n_opt_n_type_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 1e19) <= 1e18 else 0.0


# === block: score_7 (check id='val_n_opt_p_type_600K') ===
def score_7(artifact, step, ctx):
    val = ctx['data'].get('n_opt_p_type_600K')
    if val is None: return 0.0
    return 1.0 if abs(val - 1e19) <= 1e18 else 0.0


# === block: score_8 (check id='val_ZrSe2_ZT_n_max_800K') ===
def score_8(artifact, step, ctx):
    val = ctx['data'].get('ZrSe2_ZT_n_max_800K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.88) <= 0.15 else 0.0


# === block: score_9 (check id='val_ZrSe2_ZT_p_max_800K') ===
def score_9(artifact, step, ctx):
    val = ctx['data'].get('ZrSe2_ZT_p_max_800K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.80) <= 0.15 else 0.0


# === block: score_10 (check id='val_HfSe2_ZT_n_max_800K') ===
def score_10(artifact, step, ctx):
    val = ctx['data'].get('HfSe2_ZT_n_max_800K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.93) <= 0.15 else 0.0


# === block: score_11 (check id='val_HfSe2_ZT_p_max_800K') ===
def score_11(artifact, step, ctx):
    val = ctx['data'].get('HfSe2_ZT_p_max_800K')
    if val is None: return 0.0
    return 1.0 if abs(val - 0.84) <= 0.15 else 0.0


# === block: score_12 (check id='struct_n_greater_p_600_ZrSe2') ===
def score_12(artifact, step, ctx):
    d = ctx['data']
    if d.get('ZrSe2_ZT_n_max_600K', -1) > d.get('ZrSe2_ZT_p_max_600K', 0):
        return 1.0
    else: return 0.0


# === block: score_13 (check id='struct_n_greater_p_600_HfSe2') ===
def score_13(artifact, step, ctx):
    d = ctx['data']
    if d.get('HfSe2_ZT_n_max_600K', -1) > d.get('HfSe2_ZT_p_max_600K', 0):
        return 1.0
    else: return 0.0


# === block: score_14 (check id='struct_n_greater_p_800_ZrSe2') ===
def score_14(artifact, step, ctx):
    d = ctx['data']
    if d.get('ZrSe2_ZT_n_max_800K', -1) > d.get('ZrSe2_ZT_p_max_800K', 0):
        return 1.0
    else: return 0.0


# === block: score_15 (check id='struct_n_greater_p_800_HfSe2') ===
def score_15(artifact, step, ctx):
    d = ctx['data']
    if d.get('HfSe2_ZT_n_max_800K', -1) > d.get('HfSe2_ZT_p_max_800K', 0):
        return 1.0
    else: return 0.0


# === block: score_16 (check id='struct_HfSe2_greater_ZrSe2_n_800') ===
def score_16(artifact, step, ctx):
    d = ctx['data']
    if d.get('HfSe2_ZT_n_max_800K', -1) > d.get('ZrSe2_ZT_n_max_800K', -1):
        return 1.0
    else: return 0.0


_SCORERS = {
    'val_ZrSe2_kappa_l_300K': score_0,
    'val_HfSe2_kappa_l_300K': score_1,
    'val_ZrSe2_ZT_n_max_600K': score_2,
    'val_ZrSe2_ZT_p_max_600K': score_3,
    'val_HfSe2_ZT_n_max_600K': score_4,
    'val_HfSe2_ZT_p_max_600K': score_5,
    'val_n_opt_n_type_600K': score_6,
    'val_n_opt_p_type_600K': score_7,
    'val_ZrSe2_ZT_n_max_800K': score_8,
    'val_ZrSe2_ZT_p_max_800K': score_9,
    'val_HfSe2_ZT_n_max_800K': score_10,
    'val_HfSe2_ZT_p_max_800K': score_11,
    'struct_n_greater_p_600_ZrSe2': score_12,
    'struct_n_greater_p_600_HfSe2': score_13,
    'struct_n_greater_p_800_ZrSe2': score_14,
    'struct_n_greater_p_800_HfSe2': score_15,
    'struct_HfSe2_greater_ZrSe2_n_800': score_16,
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
