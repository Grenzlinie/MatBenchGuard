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


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol_rel = step["tolerance_rel"]
    items = artifact if isinstance(artifact, list) else []
    total_fields = 0
    total_score = 0.0
    for sys_name, gold_vals in gold.items():
        sys_data = next((x for x in items if x.get("system") == sys_name), None)
        if sys_data is None:
            continue
        for field, gv in gold_vals.items():
            total_fields += 1
            av = sys_data.get(field)
            if av is None:
                continue
            diff = abs(av - gv)
            denom = abs(gv) if abs(gv) > 1e-9 else 1.0
            tol = tol_rel * denom
            if diff <= tol:
                total_score += 1.0
            else:
                # partial credit linear decay up to 2*tol
                if diff >= 2*tol:
                    total_score += 0.0
                else:
                    total_score += max(0.0, 1.0 - (diff - tol) / tol)
    if total_fields == 0:
        return 0.0
    return total_score / total_fields


# === block: score_1 (check id='mechanical_properties') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tol_rel = step["tolerance_rel"]
    abs_tol_dim = step["abs_tol_dimensionless"]
    dim_fields = {"anisotropy_index_B", "anisotropy_index_G"}
    items = artifact if isinstance(artifact, list) else []
    total_fields = 0
    total_score = 0.0
    for sys_name, gold_vals in gold.items():
        sys_data = next((x for x in items if x.get("system") == sys_name), None)
        if sys_data is None:
            continue
        for field, gv in gold_vals.items():
            total_fields += 1
            av = sys_data.get(field)
            if av is None:
                continue
            if field in dim_fields:
                tol = abs_tol_dim
                diff = abs(av - gv)
                if diff <= tol:
                    total_score += 1.0
                else:
                    total_score += max(0.0, 1.0 - (diff - tol) / tol)
            else:
                diff = abs(av - gv)
                denom = abs(gv) if abs(gv) > 1e-9 else 1.0
                tol = tol_rel * denom
                if diff <= tol:
                    total_score += 1.0
                else:
                    if diff >= 2*tol:
                        total_score += 0.0
                    else:
                        total_score += max(0.0, 1.0 - (diff - tol) / tol)
    if total_fields == 0:
        return 0.0
    return total_score / total_fields


# === block: score_2 (check id='thermodynamic_properties') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tolerances = step["tolerances"]
    trends = step["trends"]
    n_w = step["numeric_weight"]
    t_w = step["trend_weight"]
    items = artifact if isinstance(artifact, list) else []

    # --- numeric scoring ---
    total_fields = 0
    total_score = 0.0
    for sys_name, gold_vals in gold.items():
        sys_data = next((x for x in items if x.get("system") == sys_name), None)
        if sys_data is None:
            continue
        for field, gv in gold_vals.items():
            total_fields += 1
            av = sys_data.get(field)
            if av is None:
                continue
            if field == "k_min" or field == "saturated_C_V":
                tol = tolerances.get(field+"_abs", 1.0)
                diff = abs(av - gv)
                if diff <= tol:
                    total_score += 1.0
                else:
                    total_score += max(0.0, 1.0 - (diff - tol) / tol)
            else:
                # velocities or Theta_D
                if field == "Theta_D":
                    tol_rel = tolerances["Theta_D_rel"].get(sys_name, 0.1)
                else:
                    tol_rel = tolerances["velocity_rel"].get(sys_name, 0.1)
                diff = abs(av - gv)
                denom = abs(gv) if abs(gv) > 1e-9 else 1.0
                tol = tol_rel * denom
                if diff <= tol:
                    total_score += 1.0
                else:
                    if diff >= 2*tol:
                        total_score += 0.0
                    else:
                        total_score += max(0.0, 1.0 - (diff - tol) / tol)
    numeric_score = total_score / total_fields if total_fields > 0 else 0.0

    # --- trend scoring ---
    def check_order(data, order, key, decreasing=True):
        vals = []
        for sys in order:
            d = next((x for x in data if x.get("system") == sys), None)
            if d is None:
                return False
            v = d.get(key)
            if v is None:
                return False
            vals.append(v)
        if decreasing:
            for i in range(len(order)-1):
                if vals[i] <= vals[i+1]:
                    return False
        else:
            for i in range(len(order)-1):
                if vals[i] >= vals[i+1]:
                    return False
        return True

    # derive expected decreasing order from gold values (overrides possibly wrong static trends)
    gold_systems = list(gold.keys())
    k_min_gold_order = sorted(gold_systems, key=lambda s: gold[s].get("k_min", 0.0), reverse=True)
    theta_D_gold_order = sorted(gold_systems, key=lambda s: gold[s].get("Theta_D", 0.0), reverse=True)
    v_m_gold_order = sorted(gold_systems, key=lambda s: gold[s].get("v_m", 0.0), reverse=True)

    trend_score = 0.0
    if check_order(items, k_min_gold_order, "k_min", decreasing=True):
        trend_score += 1.0
    if check_order(items, theta_D_gold_order, "Theta_D", decreasing=True):
        trend_score += 1.0
    if check_order(items, v_m_gold_order, "v_m", decreasing=True):
        trend_score += 1.0
    trend_score /= 3.0

    return n_w * numeric_score + t_w * trend_score


_SCORERS = {
    'elastic_constants': score_0,
    'mechanical_properties': score_1,
    'thermodynamic_properties': score_2,
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
