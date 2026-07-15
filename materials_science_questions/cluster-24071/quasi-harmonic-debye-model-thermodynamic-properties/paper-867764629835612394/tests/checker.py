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
    return {"gold": spec["gold"], "tolerances": spec["tolerances"]}


# === block: score_0 (check id='step_04_postprocess') ===
def score_0(artifact, step, ctx):
    import math

    artifact_obj = artifact
    if not isinstance(artifact_obj, dict):
        return 0.0

    required_pressures = ["100_GPa", "125_GPa", "150_GPa", "175_GPa", "200_GPa"]
    if not all(p in artifact_obj for p in required_pressures):
        return 0.0

    gold = ctx["gold"]
    tolerances = ctx["tolerances"]

    # field groups with tolerance mapping
    # base fields that are simple scalars (not nested)
    base_fields = [
        ("lattice_a", "lattice"),
        ("lattice_b", "lattice"),
        ("lattice_c", "lattice"),
        ("bulk_modulus_B", "bulk_modulus_B"),
        ("shear_modulus_G", "shear_modulus_G"),
        ("Youngs_modulus_Y", "Youngs_modulus_Y"),
        ("Poisson_ratio_v", "Poisson_ratio_v"),
        ("Pugh_ratio_GB", "Pugh_ratio_GB"),
        ("sound_velocity_t", "sound_velocity"),
        ("sound_velocity_l", "sound_velocity"),
        ("sound_velocity_m", "sound_velocity"),
        ("debye_temperature", "debye_temperature"),
        ("gruneisen_parameter", "gruneisen_parameter"),
        ("melting_temperature", "melting_temperature"),
        ("thermal_expansion_coefficient", "thermal_expansion_coefficient"),
        ("min_thermal_conductivity", "min_thermal_conductivity"),
        ("hardness_Teter", "hardness"),
        ("hardness_Tian", "hardness"),
        ("hardness_Chen", "hardness"),
        ("hardness_micro", "hardness"),
        ("N_EF", "N_EF"),
        ("mu_star", "mu_star"),
        ("lambda", "lambda"),
        ("T_c", "T_c"),
    ]

    elastic_fields = ["C11", "C22", "C33", "C44", "C55", "C66", "C12", "C13", "C23"]

    field_accuracy_weights = {
        "T_c": 0.20,
        "debye_temperature": 0.10,
        "bulk_modulus_B": 0.05,
        "shear_modulus_G": 0.05,
        "Youngs_modulus_Y": 0.05,
        "Poisson_ratio_v": 0.05,
        "Pugh_ratio_GB": 0.05,
        "sound_velocity_t": 0.03,
        "sound_velocity_l": 0.03,
        "sound_velocity_m": 0.03,
        "gruneisen_parameter": 0.05,
        "melting_temperature": 0.05,
        "thermal_expansion_coefficient": 0.05,
        "min_thermal_conductivity": 0.05,
        "hardness_Teter": 0.02,
        "hardness_Tian": 0.02,
        "hardness_Chen": 0.02,
        "hardness_micro": 0.02,
        "N_EF": 0.05,
        "mu_star": 0.05,
        "lambda": 0.03,
        "lattice_a": 0.005,
        "lattice_b": 0.005,
        "lattice_c": 0.005,
    }
    for cf in elastic_fields:
        field_accuracy_weights[cf] = 0.004  # 9*0.004=0.036 total

    def within_tolerance(candidate, gold_val, tol_cfg):
        if candidate is None:
            return False
        if "abs" in tol_cfg:
            if abs(candidate - gold_val) <= tol_cfg["abs"] + 1e-12:
                return True
        if "rel" in tol_cfg:
            if gold_val == 0:
                if abs(candidate) <= 1e-9:
                    return True
            else:
                if abs((candidate - gold_val) / gold_val) <= tol_cfg["rel"] + 1e-12:
                    return True
        return False

    # Field accuracy score (weighted average across pressures and fields)
    field_total = 0.0
    field_weight_sum = 0.0
    for pressure in required_pressures:
        data = artifact_obj[pressure]
        gold_p = gold[pressure]
        for field_name, tol_name in base_fields:
            if field_name not in data or field_name not in gold_p:
                continue
            val = data[field_name]
            g = gold_p[field_name]
            if not isinstance(val, (int, float)):
                continue
            w = field_accuracy_weights.get(field_name, 0.0)
            if w == 0:
                continue
            ok = within_tolerance(val, g, tolerances.get(tol_name, {}))
            field_total += w * ok
            field_weight_sum += w
        # elastic constants
        ec = data.get("elastic_constants", {})
        gold_ec = gold_p.get("elastic_constants", {})
        for cf in elastic_fields:
            if cf not in ec or cf not in gold_ec:
                continue
            val = ec[cf]
            g = gold_ec[cf]
            if not isinstance(val, (int, float)):
                continue
            w = field_accuracy_weights.get(cf, 0.0)
            ok = within_tolerance(val, g, tolerances.get("elastic_constant", {}))
            field_total += w * ok
            field_weight_sum += w

    field_accuracy_score = field_total / field_weight_sum if field_weight_sum > 0 else 0.0

    # Trend scores: Tc decreasing, B increasing
    pressures_vals = [("100_GPa","125_GPa","150_GPa","175_GPa","200_GPa")]
    tc_values = []
    b_values = []
    for p in required_pressures:
        data = artifact_obj[p]
        if "T_c" in data and isinstance(data["T_c"], (int, float)):
            tc_values.append(data["T_c"])
        else:
            tc_values.append(None)
        if "bulk_modulus_B" in data and isinstance(data["bulk_modulus_B"], (int, float)):
            b_values.append(data["bulk_modulus_B"])
        else:
            b_values.append(None)

    tc_trend_ok = True
    for i in range(len(tc_values)-1):
        a = tc_values[i]
        b_ = tc_values[i+1]
        if a is None or b_ is None:
            tc_trend_ok = False
            break
        if a <= b_:  # should be decreasing, so a > b_
            # allow a small plateau? we require strict decrease; if equal, fail
            tc_trend_ok = False
            break

    b_trend_ok = True
    for i in range(len(b_values)-1):
        a = b_values[i]
        b_ = b_values[i+1]
        if a is None or b_ is None:
            b_trend_ok = False
            break
        if a >= b_:  # should be increasing
            b_trend_ok = False
            break

    # Internal consistency: recompute Tc from reported theta_D, lambda, mu* and McMillan formula
    consistency_score = 0.0
    consistency_count = 0
    for pressure in required_pressures:
        data = artifact_obj[pressure]
        if not all(k in data for k in ["debye_temperature", "lambda", "mu_star", "T_c"]):
            continue
        theta = data["debye_temperature"]
        lam = data["lambda"]
        mustar = data["mu_star"]
        tc_reported = data["T_c"]
        if not all(isinstance(x, (int, float)) for x in [theta, lam, mustar, tc_reported]):
            continue
        if lam <= 0 or theta <= 0:
            continue
        try:
            exponent = -1.04 * (1 + lam) / (1 - mustar * (1 + 0.62 * lam))
            if exponent >= 0:  # should be negative for superconductivity
                tc_calc = theta / 1.45 * math.exp(exponent)
            else:
                tc_calc = theta / 1.45 * math.exp(exponent)
            if abs(tc_calc - tc_reported) <= 1.0:
                consistency_score += 1.0
        except (OverflowError, ValueError):
            pass
        consistency_count += 1

    if consistency_count > 0:
        consistency_norm = consistency_score / consistency_count
    else:
        consistency_norm = 0.0

    # Combine sub-scores with weights: shape 0.01, field_accuracy 0.80, tc_trend 0.10, b_trend 0.05, consistency 0.04
    shape_score = 1.0  # we already checked dict and keys existence; shape gate passed in harness
    final = 0.01 * shape_score + 0.80 * field_accuracy_score + 0.10 * tc_trend_ok + 0.05 * b_trend_ok + 0.04 * consistency_norm
    return max(0.0, min(1.0, final))


_SCORERS = {
    'step_04_postprocess': score_0,
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
