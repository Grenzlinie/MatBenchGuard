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


# === block: score_0 (check id='step_total_energies') ===
def score_0(artifact, step, ctx):
    diff = artifact.get("binding_energy_difference_polyyne_minus_cumulene")
    bind_score = 0.0
    if diff is not None:
        threshold = step["target"]["binding_energy_difference_min_meV"]
        if diff >= threshold:
            bind_score = 1.0
        elif diff > 0:
            bind_score = max(0.0, diff / threshold)

    cum_gap = artifact.get("cumulene_band_gap_eV")
    cum_gap_score = 0.0
    if cum_gap is not None:
        tol = step["target"]["cumulene_band_gap_tolerance_eV"]
        if abs(cum_gap) <= tol:
            cum_gap_score = 1.0

    poly_gap = artifact.get("polyyne_band_gap_eV")
    poly_gap_score = 0.0
    if poly_gap is not None:
        ref = step["target"]["polyyne_band_gap_reference_eV"]
        tol = step["target"]["polyyne_band_gap_tolerance_eV"]
        if abs(poly_gap - ref) <= tol:
            poly_gap_score = 1.0

    cum_eps = artifact.get("cumulene_static_epsilon_real")
    cum_eps_score = 0.0
    if cum_eps is not None:
        ref = step["target"]["cumulene_static_epsilon_reference"]
        tol = step["target"]["cumulene_static_epsilon_tolerance"]
        if abs(cum_eps - ref) <= tol:
            cum_eps_score = 1.0

    poly_eps = artifact.get("polyyne_static_epsilon_real")
    poly_eps_score = 0.0
    if poly_eps is not None:
        ref = step["target"]["polyyne_static_epsilon_reference"]
        tol = step["target"]["polyyne_static_epsilon_tolerance"]
        if abs(poly_eps - ref) <= tol:
            poly_eps_score = 1.0

    N = artifact.get("supercell_optimal_N")
    N_score = 0.0
    if N is not None and N == step["target"]["supercell_optimal_expected"]:
        N_score = 1.0

    opt_E = artifact.get("supercell_energy_at_optimal_N_eV")
    n4_E = artifact.get("supercell_energy_at_N4_eV")
    energy_order_score = 0.0
    if opt_E is not None and n4_E is not None and opt_E < n4_E:
        energy_order_score = 1.0

    weights = {
        "bind": 0.3,
        "cum_gap": 0.15,
        "poly_gap": 0.15,
        "cum_eps": 0.1,
        "poly_eps": 0.1,
        "N": 0.1,
        "energy_order": 0.1
    }

    total = (bind_score * weights["bind"] +
             cum_gap_score * weights["cum_gap"] +
             poly_gap_score * weights["poly_gap"] +
             cum_eps_score * weights["cum_eps"] +
             poly_eps_score * weights["poly_eps"] +
             N_score * weights["N"] +
             energy_order_score * weights["energy_order"])
    return total


# === block: score_1 (check id='step_tensile_stiffness') ===
def score_1(artifact, step, ctx):
    stiff_c = artifact.get("cumulene_tensile_stiffness")
    stiff_p = artifact.get("polyyne_tensile_stiffness")
    if stiff_c is None or stiff_p is None:
        return 0.0
    target_c = step["target"]["cumulene_stiffness_eV_per_A"]
    target_p = step["target"]["polyyne_stiffness_eV_per_A"]
    tol = step["target"]["tolerance_relative"]
    err_c = abs(stiff_c - target_c) / target_c
    err_p = abs(stiff_p - target_p) / target_p
    score_c = max(0.0, 1.0 - err_c / tol)
    score_p = max(0.0, 1.0 - err_p / tol)
    average = (score_c + score_p) / 2.0
    if stiff_p <= stiff_c:
        trend_factor = 0.5
    else:
        trend_factor = 1.0
    return average * trend_factor


# === block: score_2 (check id='step_phonon') ===
def score_2(artifact, step, ctx):
    min_freq = artifact.get("minimum_frequency")
    flag = artifact.get("has_imaginary_frequencies")
    if min_freq is None or flag is None:
        return 0.0
    threshold = step["target"]["min_frequency_negative_threshold_THz"]
    if min_freq < threshold and flag is True:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_total_energies': score_0,
    'step_tensile_stiffness': score_1,
    'step_phonon': score_2,
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
