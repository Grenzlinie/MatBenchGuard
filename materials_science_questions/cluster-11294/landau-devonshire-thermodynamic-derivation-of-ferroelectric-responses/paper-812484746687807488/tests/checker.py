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
    gold_data = {}
    tol_data = {}
    structural = {}
    for step in spec.get("steps", []):
        if step.get("output_file") == "results_at_stress_points.json":
            gold_data = step.get("reference_values", {}).get("gold", {})
            tol_data = step.get("tolerances", {})
            structural = step.get("structural_checks", {})
            break
    return {"gold": gold_data, "tolerances": tol_data, "structural": structural}


# === block: score_0 (check id='verify_results') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold = ctx["gold"]
    tol = ctx["tolerances"]
    structural = ctx.get("structural", {})

    stress_points = data.get("stress_points", [])
    results = data.get("results", [])
    if len(stress_points) != len(results):
        return 0.0

    res_by_stress = {sp: res for sp, res in zip(stress_points, results)}

    # Polarization sub-score (weight 0.35)
    pol_score = 0.0
    n_pol = 0
    for sp_str, g in gold.items():
        sp = float(sp_str)
        if sp not in res_by_stress:
            continue
        res = res_by_stress[sp]
        gp = (g.get("P1"), g.get("P2"), g.get("P3"))
        rp = (res.get("P1"), res.get("P2"), res.get("P3"))
        if any(v is None for v in gp) or any(v is None for v in rp):
            continue
        n_pol += 1
        pol_tol = tol.get("P", 0.01)
        ok = all(abs(gp[i] - rp[i]) <= pol_tol for i in range(3))
        if ok:
            pol_score += 1.0
        else:
            pol_score += sum(1 for i in range(3) if abs(gp[i] - rp[i]) <= pol_tol) / 3.0
    if n_pol > 0:
        pol_score /= n_pol

    # Strain sub-score (S3, S4) (weight 0.25)
    strain_score = 0.0
    n_strain = 0
    for sp_str, g in gold.items():
        sp = float(sp_str)
        if sp not in res_by_stress:
            continue
        res = res_by_stress[sp]
        for key in ["S3", "S4"]:
            gv = g.get(key)
            rv = res.get(key)
            if gv is None or rv is None:
                continue
            n_strain += 1
            t = tol.get(key, 0.001)
            diff = abs(gv - rv)
            if diff <= t:
                strain_score += 1.0
            else:
                strain_score += max(0.0, 1.0 - diff / t)
    if n_strain > 0:
        strain_score /= n_strain

    # Response sub-score (d33, epsilon33) (weight 0.25)
    resp_score = 0.0
    n_resp = 0
    target_sp = -4.65
    if target_sp in res_by_stress:
        res = res_by_stress[target_sp]
        g = gold.get(str(target_sp), {})
        for key, tol_spec in [("d33", tol.get("d33", "relative 0.1 or absolute 5")), ("epsilon33", tol.get("epsilon33", "relative 0.2"))]:
            gv = g.get(key)
            rv = res.get(key)
            if gv is None or rv is None:
                continue
            n_resp += 1
            if key == "d33":
                rel = 0.1 * abs(gv)
                abs_lim = 5.0
                t_val = max(rel, abs_lim)
            else:
                t_val = 0.2 * abs(gv)
            diff = abs(gv - rv)
            if diff <= t_val:
                resp_score += 1.0
            else:
                resp_score += max(0.0, 1.0 - diff / t_val)
    if n_resp > 0:
        resp_score /= n_resp

    # Structural sub-score (weight 0.15)
    struct_score = 0.0
    n_struct = 0
    if structural.get("monotonic_P_mag"):
        n_struct += 1
        pmags = [math.sqrt(res.get("P1",0)**2+res.get("P2",0)**2+res.get("P3",0)**2) for res in results]
        if len(pmags) >= 2 and all(pmags[i] >= pmags[i+1] for i in range(len(pmags)-1)):
            struct_score += 1.0
    if structural.get("S4_sign_negative"):
        n_struct += 1
        if all(res.get("S4", 0) <= 0 for res in results):
            struct_score += 1.0
    if structural.get("phase_sequence_MA_II_at_neg4_565"):
        n_struct += 1
        sp = -4.565
        if sp in res_by_stress:
            res = res_by_stress[sp]
            if res.get("P1", 0) < 0 and res.get("P2", 0) < 0 and res.get("P3", 0) > 0:
                struct_score += 1.0
    if n_struct > 0:
        struct_score /= n_struct

    # Combine with weights
    final = 0.35 * pol_score + 0.25 * strain_score + 0.25 * resp_score + 0.15 * struct_score
    return min(1.0, max(0.0, final))


_SCORERS = {
    'verify_results': score_0,
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
