import os
import json
import csv

# === author imports / helpers ===
def score_array_abs_tolerance(artifact, step):
    path = step['path']
    gold = step['gold_values']
    tol = step['tolerance_abs']
    keys = path.split('.')
    val = artifact
    for k in keys:
        val = val[k]
    if len(val) != len(gold):
        return 0.0
    within = sum(1 for a,b in zip(val,gold) if abs(a-b) <= tol)
    return within / len(gold)

def score_scalar_abs_tolerance(artifact, step):
    path = step['path']
    gold = step['gold_value']
    tol = step['tolerance_abs']
    keys = path.split('.')
    val = artifact
    for k in keys:
        val = val[k]
    return 1.0 if abs(val - gold) <= tol else 0.0


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


# === block: score_0 (check id='fig1_eps0_phi') ===
def score_0(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_1 (check id='fig1_eps0_Gamma') ===
def score_1(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_2 (check id='fig1_eps0_phi_s_diff') ===
def score_2(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_3 (check id='fig1_eps0_mu_RPA') ===
def score_3(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_4 (check id='fig1_eps3_phi') ===
def score_4(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_5 (check id='fig1_eps3_Gamma') ===
def score_5(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_6 (check id='fig1_eps3_phi_s_diff') ===
def score_6(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_7 (check id='fig1_eps3_mu_RPA') ===
def score_7(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_8 (check id='fig1_eps5_phi') ===
def score_8(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_9 (check id='fig1_eps5_Gamma') ===
def score_9(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_10 (check id='fig1_eps5_phi_s_diff') ===
def score_10(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_11 (check id='fig1_eps5_mu_RPA') ===
def score_11(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_12 (check id='fig1_eps7_phi') ===
def score_12(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_13 (check id='fig1_eps7_Gamma') ===
def score_13(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_14 (check id='fig1_eps7_phi_s_diff') ===
def score_14(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_15 (check id='fig1_eps7_mu_RPA') ===
def score_15(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_16 (check id='fig2_chi_0_phi') ===
def score_16(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_17 (check id='fig2_chi_0.4_phi') ===
def score_17(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_18 (check id='fig2_chi_0.5_phi') ===
def score_18(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_19 (check id='fig2_chi_0.6_phi') ===
def score_19(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_20 (check id='fig3_phi_chi_0') ===
def score_20(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_21 (check id='fig3_phi_chi_0.4') ===
def score_21(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_22 (check id='fig3_phi_chi_0.5') ===
def score_22(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_23 (check id='fig3_phi_chi_0.6') ===
def score_23(artifact, step, ctx):
    return score_array_abs_tolerance(artifact, step)


# === block: score_24 (check id='fig5_spinodal') ===
def score_24(artifact, step, ctx):
    return score_scalar_abs_tolerance(artifact, step)


_SCORERS = {
    'fig1_eps0_phi': score_0,
    'fig1_eps0_Gamma': score_1,
    'fig1_eps0_phi_s_diff': score_2,
    'fig1_eps0_mu_RPA': score_3,
    'fig1_eps3_phi': score_4,
    'fig1_eps3_Gamma': score_5,
    'fig1_eps3_phi_s_diff': score_6,
    'fig1_eps3_mu_RPA': score_7,
    'fig1_eps5_phi': score_8,
    'fig1_eps5_Gamma': score_9,
    'fig1_eps5_phi_s_diff': score_10,
    'fig1_eps5_mu_RPA': score_11,
    'fig1_eps7_phi': score_12,
    'fig1_eps7_Gamma': score_13,
    'fig1_eps7_phi_s_diff': score_14,
    'fig1_eps7_mu_RPA': score_15,
    'fig2_chi_0_phi': score_16,
    'fig2_chi_0.4_phi': score_17,
    'fig2_chi_0.5_phi': score_18,
    'fig2_chi_0.6_phi': score_19,
    'fig3_phi_chi_0': score_20,
    'fig3_phi_chi_0.4': score_21,
    'fig3_phi_chi_0.5': score_22,
    'fig3_phi_chi_0.6': score_23,
    'fig5_spinodal': score_24,
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
