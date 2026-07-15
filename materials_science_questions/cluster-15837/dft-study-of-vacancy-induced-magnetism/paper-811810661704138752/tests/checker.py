import os
import json
import csv

# === author imports / helpers ===
import os
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
    rows = {}
    with open(os.path.join(outputs_dir, "results.csv"), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows[row["configuration"]] = row
    return {"rows": rows}


# === block: score_0 (check id='defect_free_deltaE') ===
def score_0(artifact, step, ctx):
    config = step.get("config", "defect-free")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        efm = float(row["E_FM"])
        eafm = float(row["E_AFM"])
        mag = float(row["magnetic_moment_per_Gd"])
    except (ValueError, KeyError):
        return 0.0
    deltaE = (efm - eafm) * 1000.0
    tol = step["tol_abs_meV"]
    decay = step["decay_abs_meV"]
    target = step["target_deltaE_meV"]
    error = abs(deltaE - target)
    if error <= tol:
        delta_score = 1.0
    else:
        delta_score = max(0.0, 1.0 - (error - tol) / decay)
    # Physically-derived moment target: Gd 4f contributions give ~7 μ_B per atom.
    moment_target = 7.0
    moment_tol = 1.0
    moment_score = 1.0 if abs(mag - moment_target) <= moment_tol else 0.0
    return 0.8 * delta_score + 0.2 * moment_score


# === block: score_1 (check id='V_N_deltaE') ===
def score_1(artifact, step, ctx):
    config = step.get("config", "V_N")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        efm = float(row["E_FM"])
        eafm = float(row["E_AFM"])
    except (ValueError, KeyError):
        return 0.0
    deltaE = (efm - eafm) * 1000.0
    tol = step["tol_abs_meV"]
    decay = step["decay_abs_meV"]
    target = step["target_deltaE_meV"]
    error = abs(deltaE - target)
    if error <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (error - tol) / decay)


# === block: score_2 (check id='V_Ga_deltaE') ===
def score_2(artifact, step, ctx):
    config = step.get("config", "V_Ga")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        efm = float(row["E_FM"])
        eafm = float(row["E_AFM"])
    except (ValueError, KeyError):
        return 0.0
    deltaE = (efm - eafm) * 1000.0
    target = step["target_deltaE_meV"]
    tol_rel = step["tol_rel"]
    decay_rel = step["decay_rel"]
    if abs(target) < 1e-6:
        return 0.0
    rel_err = abs(deltaE - target) / abs(target)
    if rel_err <= tol_rel:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol_rel) / decay_rel)


# === block: score_3 (check id='V_Ga+O_deltaE') ===
def score_3(artifact, step, ctx):
    config = step.get("config", "V_Ga+O")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        efm = float(row["E_FM"])
        eafm = float(row["E_AFM"])
    except (ValueError, KeyError):
        return 0.0
    deltaE = (efm - eafm) * 1000.0
    target = step["target_deltaE_meV"]
    tol_rel = step["tol_rel"]
    decay_rel = step["decay_rel"]
    if abs(target) < 1e-6:
        return 0.0
    rel_err = abs(deltaE - target) / abs(target)
    if rel_err <= tol_rel:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol_rel) / decay_rel)


# === block: score_4 (check id='defect_free_moment') ===
def score_4(artifact, step, ctx):
    config = step.get("config", "defect-free")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        moment = float(row["magnetic_moment_per_Gd"])
    except (ValueError, KeyError):
        return 0.0
    target = step["target_moment"]
    tol = step["tol_abs"]
    return 1.0 if abs(moment - target) <= tol else 0.0


# === block: score_5 (check id='V_N_moment') ===
def score_5(artifact, step, ctx):
    config = step.get("config", "V_N")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        moment = float(row["magnetic_moment_per_Gd"])
    except (ValueError, KeyError):
        return 0.0
    target = step["target_moment"]
    tol = step["tol_abs"]
    return 1.0 if abs(moment - target) <= tol else 0.0


# === block: score_6 (check id='V_Ga_moment') ===
def score_6(artifact, step, ctx):
    config = step.get("config", "V_Ga")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        moment = float(row["magnetic_moment_per_Gd"])
    except (ValueError, KeyError):
        return 0.0
    target = step["target_moment"]
    tol = step["tol_abs"]
    return 1.0 if abs(moment - target) <= tol else 0.0


# === block: score_7 (check id='V_Ga+O_moment') ===
def score_7(artifact, step, ctx):
    config = step.get("config", "V_Ga+O")
    row = ctx["rows"].get(config)
    if row is None:
        return 0.0
    try:
        moment = float(row["magnetic_moment_per_Gd"])
    except (ValueError, KeyError):
        return 0.0
    target = step["target_moment"]
    tol = step["tol_abs"]
    return 1.0 if abs(moment - target) <= tol else 0.0


# === block: score_8 (check id='structural_ordering') ===
def score_8(artifact, step, ctx):
    required = ["V_Ga", "V_Ga+O", "V_N"]
    rows = ctx["rows"]
    deltas = {}
    for config in required:
        row = rows.get(config)
        if row is None:
            return 0.0
        try:
            efm = float(row["E_FM"])
            eafm = float(row["E_AFM"])
        except (ValueError, KeyError):
            return 0.0
        deltas[config] = (efm - eafm) * 1000.0

    # ordering: V_Ga < V_Ga+O < V_N (allowing for positive small V_N)
    if not (deltas["V_Ga"] < deltas["V_Ga+O"] < deltas["V_N"]):
        return 0.0
    # ratio check: |ΔE_V_Ga| / |ΔE_V_N| > 100
    abs_vga = abs(deltas["V_Ga"])
    abs_vn = abs(deltas["V_N"])
    if abs_vn < 1e-6:
        return 0.0
    if abs_vga / abs_vn <= 100.0:
        return 0.0
    return 1.0


_SCORERS = {
    'defect_free_deltaE': score_0,
    'V_N_deltaE': score_1,
    'V_Ga_deltaE': score_2,
    'V_Ga+O_deltaE': score_3,
    'defect_free_moment': score_4,
    'V_N_moment': score_5,
    'V_Ga_moment': score_6,
    'V_Ga+O_moment': score_7,
    'structural_ordering': score_8,
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
