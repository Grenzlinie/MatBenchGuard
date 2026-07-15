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
    def prepare(outputs_dir, spec):
        step = spec["steps"][0]
        return {"gold_params": step.get("hidden_gold_params", {})}


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx.get("gold_params", {})
        tol = gold.get("tolerances", {})
        tolY = tol.get("Young_modulus_TPa", 0.05)
        tolS = tol.get("critical_stress_GPa", 5.0)
        tolE = tol.get("critical_strain_percent", 1.0)
        tolD = tol.get("threshold_Angstrom", 1.0)

        # Helper: safely get a numeric value from a dict, treating None as 0
        def safe_num(d, key, default=0.0):
            v = d.get(key)
            if v is None:
                return default
            try:
                return float(v)
            except (ValueError, TypeError):
                return default

        samples_list = artifact.get("samples", [])
        samples_by_id = {s["sample_id"]: s for s in samples_list}

        perfect_gold = gold.get("perfect", {})
        sv_gold = gold.get("SV", {})
        tv_gold = gold.get("TV", {})
        dv_params = gold.get("DV_formula_params", {})
        dv_young_params = gold.get("DV_Young_params", {})
        dv_distances = gold.get("DV_distances", [])

        def compute_DV(D):
            stress = dv_params["SV_stress"] * (1.0 - dv_params["K_sig"] / (D ** dv_params["n_sig"]))
            strain = dv_params["SV_strain"] * (1.0 - dv_params["K_eps"] / (D ** dv_params["n_eps"]))
            Y_min = dv_young_params["Y_min"]
            Y_max = dv_young_params["Y_max"]
            D_min = dv_young_params["D_min"]
            D_max = dv_young_params["D_max"]
            if D_max == D_min:
                y = Y_min
            else:
                y = Y_min + (Y_max - Y_min) * (D - D_min) / (D_max - D_min)
            return (round(y, 4), round(stress, 2), round(strain, 2))

        expected = {}
        expected["perfect"] = perfect_gold
        expected["SV"] = sv_gold
        for i, D in enumerate(dv_distances, start=1):
            y, s, e = compute_DV(D)
            expected[f"DV_{i}"] = {
                "Young_modulus_TPa": y,
                "critical_stress_GPa": s,
                "critical_strain_percent": e,
                "separation_distance_Angstrom": D
            }
        expected["TV"] = tv_gold

        total_prop = 0
        correct_prop = 0
        for sid, exp in expected.items():
            actual = samples_by_id.get(sid)
            if actual is None:
                total_prop += 3
                continue
            total_prop += 3
            actual_y = safe_num(actual, "Young_modulus_TPa", 0.0)
            exp_y = safe_num(exp, "Young_modulus_TPa", 0.0)
            if abs(actual_y - exp_y) <= tolY:
                correct_prop += 1
            actual_s = safe_num(actual, "critical_stress_GPa", 0.0)
            exp_s = safe_num(exp, "critical_stress_GPa", 0.0)
            if abs(actual_s - exp_s) <= tolS:
                correct_prop += 1
            actual_e = safe_num(actual, "critical_strain_percent", 0.0)
            exp_e = safe_num(exp, "critical_strain_percent", 0.0)
            if abs(actual_e - exp_e) <= tolE:
                correct_prop += 1
        prop_accuracy = correct_prop / total_prop if total_prop > 0 else 0.0

        thresh_gold = gold.get("threshold_gold", 46.86)
        thresh_actual = artifact.get("threshold_distance_Angstrom", None)
        thresh_pass = 0.0
        if thresh_actual is not None:
            try:
                thresh_val = float(thresh_actual)
            except (ValueError, TypeError):
                thresh_val = 0.0
            if abs(thresh_val - thresh_gold) <= tolD:
                thresh_pass = 1.0
        threshold_acc = thresh_pass

        mono_pass = 0.0
        dv_ids = [f"DV_{i}" for i in range(1, len(dv_distances)+1)]
        dv_data = []
        for did in dv_ids:
            if did in samples_by_id:
                dv_data.append(samples_by_id[did])
        if len(dv_data) >= 2:
            dv_sorted = sorted(dv_data, key=lambda s: safe_num(s, "separation_distance_Angstrom", 0.0))
            stress_vals = []
            strain_vals = []
            for s in dv_sorted:
                val_s = safe_num(s, "critical_stress_GPa")
                val_e = safe_num(s, "critical_strain_percent")
                if val_s is not None and val_e is not None:
                    stress_vals.append(val_s)
                    strain_vals.append(val_e)
            if len(stress_vals) >= 2:
                stress_mono = all(stress_vals[i-1] <= stress_vals[i] + 1e-9 for i in range(1, len(stress_vals)))
                strain_mono = all(strain_vals[i-1] <= strain_vals[i] + 1e-9 for i in range(1, len(strain_vals)))
                if stress_mono and strain_mono:
                    mono_pass = 1.0
        mono_acc = mono_pass

        total_score = 0.6 * prop_accuracy + 0.2 * threshold_acc + 0.2 * mono_acc
        return total_score


_SCORERS = {
    'step_03': score_0,
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
