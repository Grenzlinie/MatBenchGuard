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
    return {}


# === block: score_0 (check id='simulate_chemomechanical') ===
def score_0(artifact, step, ctx):
    ref_points = step.get("reference_points", [])
    tol_rule = step.get("tolerance_rule", {})
    mono_checks = step.get("monotonicity_checks", {})
    weight_scheme = step.get("weight_scheme", {"point_accuracy": 0.8, "trend_accuracy": 0.2})

    gold_map = {}
    for p in ref_points:
        ox = float(p["oxide_thickness_nm"])
        cp = float(p["critical_pressure_GPa"])
        gold_map[(ox, cp)] = {"frac": float(p["fraction_unlithiated"]), "hoop": float(p["hoop_stress_GPa"])}

    agent_rows = []
    for row in artifact:
        try:
            ox = float(row["oxide_thickness_nm"])
            cp = float(row["critical_pressure_GPa"])
            frac = float(row["fraction_unlithiated"])
            hoop = float(row["hoop_stress_GPa"])
            agent_rows.append((ox, cp, frac, hoop))
        except (KeyError, ValueError):
            continue

    pass_count = 0
    total_req = len(ref_points)
    for p in ref_points:
        ox = float(p["oxide_thickness_nm"])
        cp = float(p["critical_pressure_GPa"])
        gold = gold_map[(ox, cp)]
        matched = None
        for ar in agent_rows:
            if abs(ar[0] - ox) < 1e-6 and abs(ar[1] - cp) < 1e-6:
                matched = ar
                break
        if matched is None:
            continue
        frac_ok = False
        hoop_ok = False
        err_frac = abs(matched[2] - gold["frac"])
        if err_frac <= tol_rule["fraction_unlithiated"]["abs_tol"]:
            frac_ok = True
        else:
            if gold["frac"] > 1e-9 and err_frac / gold["frac"] <= tol_rule["fraction_unlithiated"]["rel_tol"]:
                frac_ok = True
        err_hoop = abs(matched[3] - gold["hoop"])
        if err_hoop <= tol_rule["hoop_stress_GPa"]["abs_tol"]:
            hoop_ok = True
        else:
            if gold["hoop"] > 1e-9 and err_hoop / gold["hoop"] <= tol_rule["hoop_stress_GPa"]["rel_tol"]:
                hoop_ok = True
        if frac_ok and hoop_ok:
            pass_count += 1

    point_acc = pass_count / total_req if total_req > 0 else 0.0

    def check_mono(seq, direction, max_viol_rel):
        n = len(seq)
        if n < 2:
            return 1.0
        rng = max(seq) - min(seq)
        if rng == 0:
            return 1.0
        max_viol = max_viol_rel * rng
        viol = 0
        for i in range(n-1):
            if direction == "non_decreasing" and seq[i+1] < seq[i] - max_viol:
                viol += 1
            elif direction == "non_increasing" and seq[i+1] > seq[i] + max_viol:
                viol += 1
        return max(0.0, 1.0 - viol / (n-1))

    mono_scores = []
    cps = [2.5, 4.0]
    for cp in cps:
        thicknesses = sorted([p["oxide_thickness_nm"] for p in ref_points if abs(float(p["critical_pressure_GPa"]) - cp) < 1e-6])
        if len(thicknesses) < 2:
            continue
        frac_list = []
        hoop_list = []
        for t in thicknesses:
            found = None
            for ar in agent_rows:
                if abs(ar[0] - t) < 1e-6 and abs(ar[1] - cp) < 1e-6:
                    found = ar
                    break
            if found is None:
                continue
            frac_list.append(found[2])
            hoop_list.append(found[3])
        if len(frac_list) >= 2:
            mono_scores.append(check_mono(frac_list, mono_checks["fraction_unlithiated"]["direction"],
                                          mono_checks["fraction_unlithiated"]["max_violation_relative_range"]))
        if len(hoop_list) >= 2:
            mono_scores.append(check_mono(hoop_list, mono_checks["hoop_stress_GPa"]["direction"],
                                          mono_checks["hoop_stress_GPa"]["max_violation_relative_range"]))

    trend_score = sum(mono_scores) / len(mono_scores) if mono_scores else 0.0

    final = point_acc * weight_scheme["point_accuracy"] + trend_score * weight_scheme["trend_accuracy"]
    return max(0.0, min(1.0, final))


_SCORERS = {
    'simulate_chemomechanical': score_0,
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
