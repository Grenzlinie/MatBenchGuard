import os
import json
import csv

# === author imports / helpers ===
import json

def score_val(val, gold, tol):
    if gold is None or val is None:
        return 0.0
    if abs(gold) < 1e-12:
        return 1.0 if abs(val) < 1e-12 else 0.0
    err = abs(val - gold)
    max_err = tol * abs(gold)
    if max_err < 1e-12:
        return 1.0 if err < 1e-12 else 0.0
    return max(0.0, 1.0 - err / max_err)


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
    gold = {
        "BaS": {
            "lattice": 6.352, "bulk": 44.60, "bulk_deriv": 5.15,
            "C11": 94.57, "C12": 19.61, "C44": 18.60,
            "shear_V": 26.152, "shear_R": 23.292, "shear_iso": 24.722,
            "anisotropy": 0.50, "poisson": 0.276,
            "vt": 2.37, "vl": 4.20, "vm": 2.64, "debye": 247
        },
        "BaSe": {
            "lattice": 6.608, "bulk": 37.21, "bulk_deriv": 3.72,
            "C11": 82.67, "C12": 14.48, "C44": 15.62,
            "shear_V": 23.010, "shear_R": 19.943, "shear_iso": 21.4765,
            "anisotropy": 0.46, "poisson": 0.258,
            "vt": 2.07, "vl": 3.64, "vm": 2.31, "debye": 208
        }
    }
    tol = {
        "lattice": 0.01, "bulk": 0.15, "bulk_deriv": 0.15,
        "C11": 0.20, "C12": 0.20, "C44": 0.20,
        "shear": 0.15, "anisotropy": 0.10, "poisson": 0.05,
        "velocity": 0.10, "debye": 0.10, "internal_b": 0.05
    }
    return {"gold": gold, "tol": tol}


# === block: score_0 (check id='BaS_all') ===
def score_0(artifact, step, ctx):
    artifact_list = artifact
    ctx_gold = ctx["gold"]
    ctx_tol = ctx["tol"]
    gold = ctx_gold["BaS"]
    tol = ctx_tol

    entry = None
    for obj in artifact_list:
        if isinstance(obj, dict) and obj.get("compound") == "BaS":
            entry = obj
            break
    if entry is None:
        return 0.0

    def get_f(key):
        return entry.get(key)

    sub = {}
    sub["lattice"] = score_val(get_f("lattice_constant_A"), gold["lattice"], tol["lattice"])
    sub["bulk"] = score_val(get_f("bulk_modulus_GPa"), gold["bulk"], tol["bulk"])
    sub["bulk_deriv"] = score_val(get_f("bulk_modulus_derivative"), gold["bulk_deriv"], tol["bulk_deriv"])
    sub["C11"] = score_val(get_f("C11_GPa"), gold["C11"], tol["C11"])
    sub["C12"] = score_val(get_f("C12_GPa"), gold["C12"], tol["C12"])
    sub["C44"] = score_val(get_f("C44_GPa"), gold["C44"], tol["C44"])

    sub["shear_V"] = score_val(get_f("shear_modulus_Voigt_GPa"), gold["shear_V"], tol["shear"])
    sub["shear_R"] = score_val(get_f("shear_modulus_Reuss_GPa"), gold["shear_R"], tol["shear"])
    sub["shear_Iso"] = score_val(get_f("shear_modulus_isotropic_GPa"), gold["shear_iso"], tol["shear"])

    sub["aniso"] = score_val(get_f("anisotropy_ratio"), gold["anisotropy"], tol["anisotropy"])
    sub["poisson"] = score_val(get_f("poisson_ratio"), gold["poisson"], tol["poisson"])
    sub["vt"] = score_val(get_f("transverse_velocity_kms"), gold["vt"], tol["velocity"])
    sub["vl"] = score_val(get_f("longitudinal_velocity_kms"), gold["vl"], tol["velocity"])
    sub["vm"] = score_val(get_f("mean_velocity_kms"), gold["vm"], tol["velocity"])
    sub["debye"] = score_val(get_f("debye_temperature_K"), gold["debye"], tol["debye"])

    # Internal consistency: B = (C11 + 2*C12)/3
    c11_val = get_f("C11_GPa")
    c12_val = get_f("C12_GPa")
    if c11_val is not None and c12_val is not None:
        b_cons = (c11_val + 2.0 * c12_val) / 3.0
        sub["internal_b"] = score_val(get_f("bulk_modulus_GPa"), b_cons, tol["internal_b"])
    else:
        sub["internal_b"] = 0.0

    weights = {
        "lattice": 0.03, "bulk": 0.14, "bulk_deriv": 0.02,
        "C11": 0.14, "C12": 0.09, "C44": 0.09,
        "shear_V": 0.05, "shear_R": 0.05, "shear_Iso": 0.05,
        "aniso": 0.05, "poisson": 0.06,
        "vt": 0.04, "vl": 0.04, "vm": 0.04,
        "debye": 0.07, "internal_b": 0.04
    }
    total = 0.0
    for k, w in weights.items():
        total += sub[k] * w
    return total


# === block: score_1 (check id='BaSe_all') ===
def score_1(artifact, step, ctx):
    artifact_list = artifact
    ctx_gold = ctx["gold"]
    ctx_tol = ctx["tol"]
    gold = ctx_gold["BaSe"]
    tol = ctx_tol

    entry = None
    for obj in artifact_list:
        if isinstance(obj, dict) and obj.get("compound") == "BaSe":
            entry = obj
            break
    if entry is None:
        return 0.0

    def get_f(key):
        return entry.get(key)

    sub = {}
    sub["lattice"] = score_val(get_f("lattice_constant_A"), gold["lattice"], tol["lattice"])
    sub["bulk"] = score_val(get_f("bulk_modulus_GPa"), gold["bulk"], tol["bulk"])
    sub["bulk_deriv"] = score_val(get_f("bulk_modulus_derivative"), gold["bulk_deriv"], tol["bulk_deriv"])
    sub["C11"] = score_val(get_f("C11_GPa"), gold["C11"], tol["C11"])
    sub["C12"] = score_val(get_f("C12_GPa"), gold["C12"], tol["C12"])
    sub["C44"] = score_val(get_f("C44_GPa"), gold["C44"], tol["C44"])

    sub["shear_V"] = score_val(get_f("shear_modulus_Voigt_GPa"), gold["shear_V"], tol["shear"])
    sub["shear_R"] = score_val(get_f("shear_modulus_Reuss_GPa"), gold["shear_R"], tol["shear"])
    sub["shear_Iso"] = score_val(get_f("shear_modulus_isotropic_GPa"), gold["shear_iso"], tol["shear"])

    sub["aniso"] = score_val(get_f("anisotropy_ratio"), gold["anisotropy"], tol["anisotropy"])
    sub["poisson"] = score_val(get_f("poisson_ratio"), gold["poisson"], tol["poisson"])
    sub["vt"] = score_val(get_f("transverse_velocity_kms"), gold["vt"], tol["velocity"])
    sub["vl"] = score_val(get_f("longitudinal_velocity_kms"), gold["vl"], tol["velocity"])
    sub["vm"] = score_val(get_f("mean_velocity_kms"), gold["vm"], tol["velocity"])
    sub["debye"] = score_val(get_f("debye_temperature_K"), gold["debye"], tol["debye"])

    c11_val = get_f("C11_GPa")
    c12_val = get_f("C12_GPa")
    if c11_val is not None and c12_val is not None:
        b_cons = (c11_val + 2.0 * c12_val) / 3.0
        sub["internal_b"] = score_val(get_f("bulk_modulus_GPa"), b_cons, tol["internal_b"])
    else:
        sub["internal_b"] = 0.0

    weights = {
        "lattice": 0.03, "bulk": 0.14, "bulk_deriv": 0.02,
        "C11": 0.14, "C12": 0.09, "C44": 0.09,
        "shear_V": 0.05, "shear_R": 0.05, "shear_Iso": 0.05,
        "aniso": 0.05, "poisson": 0.06,
        "vt": 0.04, "vl": 0.04, "vm": 0.04,
        "debye": 0.07, "internal_b": 0.04
    }
    total = 0.0
    for k, w in weights.items():
        total += sub[k] * w
    return total


_SCORERS = {
    'BaS_all': score_0,
    'BaSe_all': score_1,
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
