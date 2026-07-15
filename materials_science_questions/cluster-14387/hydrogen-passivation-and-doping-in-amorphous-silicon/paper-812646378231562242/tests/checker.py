import os
import json
import csv

# === author imports / helpers ===
import math


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
    d = 1.2e-10
    chi = 2.9
    eps_r = 3.9
    eps0_eV_Vcm = 5.52e5
    Nv = 2.3e22
    DeltaH0 = 1.15
    kB = 8.617333262145e-5
    Eloc_factor = (3 + chi) / 3.0

    alpha = (3 * (eps_r - 1) * eps0_eV_Vcm) / ((eps_r + 2) * Nv)

    # Ratio at E_ox = 10 MV/cm
    Eox_10 = 10.0
    Eox_SI_10 = Eox_10 * 1e8   # V/m
    Eloc_SI_10 = Eloc_factor * Eox_SI_10
    Eloc_Vcm_10 = Eloc_SI_10 * 0.01   # V/cm
    p_ecm = 3 * d * 100.0   # e*cm (p/e = 3*d)
    ratio = 0.5 * alpha * Eloc_Vcm_10 / p_ecm

    # Coefficient: eV per MV/cm
    coeff = (3 * d) * Eloc_factor * 1e8
    slope = -coeff

    # Expected delta_H for E_ox = 0..10 MV/cm
    Eox_list = [0, 2, 4, 6, 8, 10]
    enthalpy_expected = []
    for Eox in Eox_list:
        energy_eV = coeff * Eox
        delta_H = DeltaH0 - energy_eV
        enthalpy_expected.append(delta_H)

    # Expected gamma values
    gamma_expected = {}
    for T in [300, 400, 500]:
        gamma_expected[T] = coeff / (kB * T)

    return {
        "alpha": alpha,
        "ratio": ratio,
        "slope": slope,
        "enthalpy_expected": enthalpy_expected,
        "gamma_expected": gamma_expected
    }


# === block: score_0 (check id='alpha_check') ===
def score_0(artifact, step, ctx):
    agent_alpha = artifact.get("alpha")
    if agent_alpha is None:
        return 0.0
    expected_alpha = ctx["alpha"]
    if abs(agent_alpha - expected_alpha) <= 1e-3 * abs(expected_alpha) + 1e-30:
        return 1.0
    # Linear fall‑off for a bit larger error, capped at 0
    rel_err = abs(agent_alpha - expected_alpha) / (abs(expected_alpha) + 1e-30)
    if rel_err > 0.1:
        return 0.0
    return 1.0 - rel_err / 0.1  # 0..1, zero at 10% error


# === block: score_1 (check id='ratio_check') ===
def score_1(artifact, step, ctx):
    agent_ratio = artifact.get("quadratic_to_linear_ratio")
    if agent_ratio is None:
        return 0.0
    expected_ratio = ctx["ratio"]
    if abs(agent_ratio - expected_ratio) <= 1e-5:
        return 1.0
    # partial credit up to 0.01 error
    err = abs(agent_ratio - expected_ratio)
    if err > 0.01:
        return 0.0
    return 1.0 - err / 0.01


# === block: score_2 (check id='slope_check') ===
def score_2(artifact, step, ctx):
    agent_slope = artifact.get("activation_enthalpy_slope")
    if agent_slope is None:
        return 0.0
    expected_slope = ctx["slope"]
    if abs(agent_slope - expected_slope) <= 1e-6:
        return 1.0
    err = abs(agent_slope - expected_slope)
    if err > 0.001:
        return 0.0
    return 1.0 - err / 0.001


# === block: score_3 (check id='enthalpy_data_check') ===
def score_3(artifact, step, ctx):
    data = artifact.get("activation_enthalpy_data")
    if not isinstance(data, list) or len(data) != 6:
        return 0.0
    expected = ctx["enthalpy_expected"]
    scores = []
    for idx, entry in enumerate(data):
        agent_dh = entry.get("delta_H")
        if agent_dh is None:
            scores.append(0.0)
            continue
        exp_dh = expected[idx]
        if abs(agent_dh - exp_dh) <= 1e-5:
            scores.append(1.0)
        else:
            err = abs(agent_dh - exp_dh)
            if err > 0.01:
                scores.append(0.0)
            else:
                scores.append(1.0 - err / 0.01)
    return sum(scores) / len(scores)


# === block: score_4 (check id='gamma_data_check') ===
def score_4(artifact, step, ctx):
    data = artifact.get("field_acceleration_data")
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    gold = ctx["gamma_expected"]
    scores = []
    for entry in data:
        T = entry.get("T")
        agent_gamma = entry.get("gamma")
        if T is None or agent_gamma is None or T not in gold:
            scores.append(0.0)
            continue
        exp_gamma = gold[T]
        if abs(agent_gamma - exp_gamma) <= 1e-5:
            scores.append(1.0)
        else:
            err = abs(agent_gamma - exp_gamma)
            if err > 0.1:
                scores.append(0.0)
            else:
                scores.append(1.0 - err / 0.1)
    return sum(scores) / len(scores)


_SCORERS = {
    'alpha_check': score_0,
    'ratio_check': score_1,
    'slope_check': score_2,
    'enthalpy_data_check': score_3,
    'gamma_data_check': score_4,
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
