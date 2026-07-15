import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    # model parameters
    hollomon = {
        "ferrite": {"K": 581.0, "n": 0.30},
        "austenite": {"K": 2936.0, "n": 0.67},
        "martensite": {"K": 2652.0, "n": 0.08}
    }
    oc_params = {
        600: {"alpha": 5.75, "beta": 2.5, "m": 3},
        625: {"alpha": 18.6, "beta": 1.86, "m": 2},
        650: {"alpha": 49.5, "beta": 1.8, "m": 2}
    }
    initial_fractions = {
        600: {"austenite": 0.318, "ferrite": 0.682, "martensite": 0.0},
        625: {"austenite": 0.379, "ferrite": 0.621, "martensite": 0.0},
        650: {"austenite": 0.443, "ferrite": 0.528, "martensite": 0.029}
    }

    def compute_reference(T):
        oc = oc_params[T]
        V_a0 = initial_fractions[T]["austenite"]
        V_f0 = initial_fractions[T]["ferrite"]
        V_m0 = initial_fractions[T]["martensite"]
        # fine true-strain grid
        eps = np.linspace(0.0, 2.0, 200001)   # step ~1e-5
        f_alpha_prime = 1.0 - np.exp(-oc["beta"] * (1.0 - np.exp(-oc["alpha"] * eps)) ** oc["m"])
        V_a = V_a0 * (1.0 - f_alpha_prime)
        V_m = V_m0 + V_a0 * f_alpha_prime
        V_f = V_f0 * np.ones_like(eps)
        sigma_f = hollomon["ferrite"]["K"] * (eps ** hollomon["ferrite"]["n"])
        sigma_a = hollomon["austenite"]["K"] * (eps ** hollomon["austenite"]["n"])
        sigma_m = hollomon["martensite"]["K"] * (eps ** hollomon["martensite"]["n"])
        sigma_true = V_f * sigma_f + V_a * sigma_a + V_m * sigma_m
        dsigma = np.gradient(sigma_true, eps)
        # find where derivative >= sigma (Considere criterion)
        idx = np.where(dsigma >= sigma_true)[0]
        if len(idx) == 0:
            i = np.argmax(sigma_true)
        else:
            i = idx[0]
        eps_inst = eps[i]
        sigma_inst = sigma_true[i]
        eps_eng = np.exp(eps_inst) - 1.0
        sigma_eng = sigma_inst * np.exp(-eps_inst)
        return float(sigma_eng), float(eps_eng)

    ref = {T: compute_reference(T) for T in (600, 625, 650)}
    return {"ref": ref}


# === block: score_0 (check id='extract_predicted_properties') ===
def score_0(artifact, step, ctx):
    rows = artifact   # list of dicts
    ref = ctx["ref"]
    tol_uts = 10.0   # MPa
    tol_ue = 0.01    # strain
    scores = []
    for row in rows:
        try:
            T = int(row["annealing_temperature_C"])
            uts_a = float(row["predicted_UTS_MPa"])
            ue_a = float(row["predicted_uniform_elongation"])
        except (KeyError, ValueError):
            continue
        if T not in ref:
            continue
        uts_r, ue_r = ref[T]
        err_uts = abs(uts_a - uts_r)
        err_ue = abs(ue_a - ue_r)
        s_uts = 1.0 if err_uts <= tol_uts else max(0.0, 1.0 - (err_uts - tol_uts) / (2 * tol_uts))
        s_ue = 1.0 if err_ue <= tol_ue else max(0.0, 1.0 - (err_ue - tol_ue) / (2 * tol_ue))
        scores.append(min(s_uts, s_ue))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='extract_stress_strain_curves') ===
def score_1(artifact, step, ctx):
    records = artifact
    ref = ctx["ref"]
    tol_uts = 10.0
    tol_ue = 0.01
    scores = []
    for T in (600, 625, 650):
        subset = [r for r in records if int(r["annealing_temperature_C"]) == T]
        if not subset:
            scores.append(0.0)
            continue
        try:
            eng_strain = np.array([float(r["engineering_strain"]) for r in subset])
            eng_stress = np.array([float(r["engineering_stress_MPa"]) for r in subset])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        if len(eng_stress) < 2:
            scores.append(0.0)
            continue
        i_max = np.argmax(eng_stress)
        uts_a = eng_stress[i_max]
        ue_a = eng_strain[i_max]
        uts_r, ue_r = ref[T]
        err_uts = abs(uts_a - uts_r)
        err_ue = abs(ue_a - ue_r)
        s_uts = 1.0 if err_uts <= tol_uts else max(0.0, 1.0 - (err_uts - tol_uts) / (2 * tol_uts))
        s_ue = 1.0 if err_ue <= tol_ue else max(0.0, 1.0 - (err_ue - tol_ue) / (2 * tol_ue))
        scores.append(min(s_uts, s_ue))
    return sum(scores) / len(scores)


_SCORERS = {
    'extract_predicted_properties': score_0,
    'extract_stress_strain_curves': score_1,
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
