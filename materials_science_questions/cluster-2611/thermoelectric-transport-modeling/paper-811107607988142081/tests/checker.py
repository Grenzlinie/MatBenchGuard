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


# === block: score_0 (check id='step_02_extract_lattice_constants') ===
def score_0(artifact, step, ctx):
    target = step["target"]
    tol = step["tolerance"]
    s_a = max(0.0, 1.0 - abs(artifact["a_nm"] - target["a_nm"]) / tol["a_nm"])
    s_c = max(0.0, 1.0 - abs(artifact["c_nm"] - target["c_nm"]) / tol["c_nm"])
    return 0.5 * s_a + 0.5 * s_c


# === block: score_1 (check id='step_04_compute_band_gap') ===
def score_1(artifact, step, ctx):
    target = step["target"]
    tol = step["tolerance"]
    return max(0.0, 1.0 - abs(artifact["band_gap_eV"] - target["band_gap_eV"]) / tol["band_gap_eV"])


# === block: score_2 (check id='step_06_transport_properties') ===
def score_2(artifact, step, ctx):
    target = step["target"]
    tol = step["tolerance"]

    def rel_score(val, tgt, tol_rel):
        if tgt == 0:
            return 1.0 if abs(val - tgt) < 1e-6 else 0.0
        err = abs(val - tgt) / abs(tgt)
        return max(0.0, 1.0 - err / tol_rel)

    def abs_score(val, tgt, tol_abs):
        err = abs(val - tgt)
        return max(0.0, 1.0 - err / tol_abs)

    score = 0.0
    # relaxation time
    score += 0.10 * abs_score(artifact["relaxation_time_s"], target["relaxation_time_s"], tol["relaxation_time_s_abs"])
    # Seebeck peaks
    score += 0.10 * rel_score(artifact["n_type_600K"]["Seebeck_peak_uVK"], target["n_type_600K"]["Seebeck_peak_uVK"], tol["Seebeck_rel"])
    score += 0.10 * rel_score(artifact["p_type_600K"]["Seebeck_peak_uVK"], target["p_type_600K"]["Seebeck_peak_uVK"], tol["Seebeck_rel"])
    # n-type 900K
    n900 = artifact["900K"]["n_type"]
    n900_tgt = target["900K"]["n_type"]
    score += 0.02 * rel_score(n900["chem_pot_eV"], n900_tgt["chem_pot_eV"], tol["other_rel"])
    score += 0.02 * rel_score(n900["carrier_conc_cm3"], n900_tgt["carrier_conc_cm3"], tol["other_rel"])
    score += 0.05 * rel_score(n900["Seebeck_uVK"], n900_tgt["Seebeck_uVK"], tol["Seebeck_rel"])
    score += 0.05 * rel_score(n900["sigma_Ohmm"], n900_tgt["sigma_Ohmm"], tol["conductivity_rel"])
    score += 0.05 * rel_score(n900["power_factor_WmK2"], n900_tgt["power_factor_WmK2"], tol["power_factor_rel"])
    score += 0.05 * rel_score(n900["ZT_e"], n900_tgt["ZT_e"], tol["ZT_e_rel"])
    # p-type 900K
    p900 = artifact["900K"]["p_type"]
    p900_tgt = target["900K"]["p_type"]
    score += 0.02 * rel_score(p900["chem_pot_eV"], p900_tgt["chem_pot_eV"], tol["other_rel"])
    score += 0.02 * rel_score(p900["carrier_conc_cm3"], p900_tgt["carrier_conc_cm3"], tol["other_rel"])
    score += 0.05 * rel_score(p900["Seebeck_uVK"], p900_tgt["Seebeck_uVK"], tol["Seebeck_rel"])
    score += 0.05 * rel_score(p900["sigma_Ohmm"], p900_tgt["sigma_Ohmm"], tol["conductivity_rel"])
    score += 0.05 * rel_score(p900["power_factor_WmK2"], p900_tgt["power_factor_WmK2"], tol["power_factor_rel"])
    score += 0.05 * rel_score(p900["ZT_e"], p900_tgt["ZT_e"], tol["ZT_e_rel"])
    # normalize: total raw weight = 0.78
    return min(1.0, score / 0.78)


_SCORERS = {
    'step_02_extract_lattice_constants': score_0,
    'step_04_compute_band_gap': score_1,
    'step_06_transport_properties': score_2,
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
