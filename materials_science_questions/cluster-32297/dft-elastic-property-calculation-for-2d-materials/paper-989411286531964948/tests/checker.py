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
    return {}


# === block: score_0 (check id='cs_form_en_diff') ===
def score_0(artifact, step, ctx):
    raw = artifact.get(step['field'])
    if raw is None:
        return 0.0
    try:
        val = float(raw)
    except (TypeError, ValueError):
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_1 (check id='bulk_beta_energy') ===
def score_1(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_2 (check id='bulk_gamma_energy') ===
def score_2(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_3 (check id='bulk_epsilon_energy') ===
def score_3(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_4 (check id='interface_gammaAB_energy') ===
def score_4(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_5 (check id='interface_gammaAC_energy') ===
def score_5(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_6 (check id='interface_gammaCC_energy') ===
def score_6(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_7 (check id='c_ml_bg') ===
def score_7(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_8 (check id='s_ml_bg') ===
def score_8(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_9 (check id='bulk_beta_bg') ===
def score_9(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_10 (check id='bulk_gamma_bg') ===
def score_10(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_11 (check id='bulk_epsilon_bg') ===
def score_11(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_12 (check id='interface_gammaAB_bg') ===
def score_12(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_13 (check id='interface_gammaAC_bg') ===
def score_13(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_14 (check id='interface_gammaCC_bg') ===
def score_14(artifact, step, ctx):
    val = artifact.get(step['field'])
    if val is None:
        return 0.0
    err = abs(val - step['gold'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return 1.0 - (err - tol) / tol
    else:
        return 0.0


# === block: score_15 (check id='bulk_energy_order') ===
def score_15(artifact, step, ctx):
    beta = artifact.get('bulk_beta_energy_relative_meV_fu')
    epsilon = artifact.get('bulk_epsilon_energy_relative_meV_fu')
    gamma = artifact.get('bulk_gamma_energy_relative_meV_fu')
    if None in (beta, epsilon, gamma):
        return 0.0
    return 1.0 if (beta < epsilon < gamma) else 0.0


# === block: score_16 (check id='bandgap_order') ===
def score_16(artifact, step, ctx):
    beta = artifact.get('bulk_beta_bandgap_eV')
    epsilon = artifact.get('bulk_epsilon_bandgap_eV')
    gamma = artifact.get('bulk_gamma_bandgap_eV')
    if None in (beta, epsilon, gamma):
        return 0.0
    if beta <= epsilon or beta <= gamma:
        return 0.0
    if abs(epsilon - gamma) > 0.1:
        return 0.0
    return 1.0


_SCORERS = {
    'cs_form_en_diff': score_0,
    'bulk_beta_energy': score_1,
    'bulk_gamma_energy': score_2,
    'bulk_epsilon_energy': score_3,
    'interface_gammaAB_energy': score_4,
    'interface_gammaAC_energy': score_5,
    'interface_gammaCC_energy': score_6,
    'c_ml_bg': score_7,
    's_ml_bg': score_8,
    'bulk_beta_bg': score_9,
    'bulk_gamma_bg': score_10,
    'bulk_epsilon_bg': score_11,
    'interface_gammaAB_bg': score_12,
    'interface_gammaAC_bg': score_13,
    'interface_gammaCC_bg': score_14,
    'bulk_energy_order': score_15,
    'bandgap_order': score_16,
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
