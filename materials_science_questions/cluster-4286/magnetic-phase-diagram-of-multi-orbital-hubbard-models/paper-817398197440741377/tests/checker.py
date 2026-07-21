import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='step_01_order_params') ===
def score_0(artifact, step, ctx):
    import csv
    import math

    def eval_condition(row, cond):
        try:
            w = float(row["W"])
        except:
            return False
        if " <= " in cond and " and " not in cond:
            parts = cond.split(" <= ")
            if len(parts) == 3:
                # compound condition like "1.06 <= W <= 1.64"
                try:
                    lower = float(parts[0].strip())
                    upper = float(parts[2].strip())
                    return lower <= w <= upper
                except:
                    return False
            elif len(parts) == 2:
                var = parts[0].strip()
                val_str = parts[1].strip()
                if var == "W":
                    return w <= float(val_str.strip())
                else:
                    # var is value, W is right-hand side? Not expected but handle generic
                    try:
                        left_val = float(var)
                        return left_val <= w
                    except:
                        return False
        elif " >= " in cond:
            var, val_str = cond.split(" >= ")
            if var.strip() == "W":
                return w >= float(val_str.strip())
        elif " == " in cond:
            var, val_str = cond.split(" == ")
            if var.strip() == "W":
                return w == float(val_str.strip())
        elif " <= " in cond and " and " in cond:
            parts = cond.split(" and ")
            if len(parts) == 2:
                lower_part = parts[0].strip()
                upper_part = parts[1].strip()
                # evaluate lower_part: "1.06 <= W"
                if " <= " in lower_part:
                    lv, _ = lower_part.split(" <= ")
                    lv = lv.strip()
                    lower_val = float(lv) if lv.replace('.','',1).isdigit() else w
                else:
                    return False
                # evaluate upper_part: "W <= 1.64"
                if " <= " in upper_part:
                    _, uv = upper_part.split(" <= ")
                    uv = uv.strip()
                    upper_val = float(uv) if uv.replace('.','',1).isdigit() else w
                else:
                    return False
                return lower_val <= w <= upper_val
        return False

    params = step.get("params", {})
    required_columns = params.get("required_columns", [])
    min_rows = params.get("min_rows", 20)
    ordering_rules = params.get("ordering_rules", [])
    reference_points = params.get("reference_points", [])
    discontinuity_check = params.get("discontinuity_check", {})
    scoring_weights = step.get("scoring", {})

    shape_w = scoring_weights.get("shape_weight", 0.0)
    ord_w = scoring_weights.get("ordering_weight", 0.0)
    ref_w = scoring_weights.get("reference_weight", 0.0)
    disc_w = scoring_weights.get("discontinuity_weight", 0.0)
    total_w = shape_w + ord_w + ref_w + disc_w
    if total_w == 0:
        return 0.0

    # shape check
    shape_ok = True
    if len(artifact) < min_rows:
        shape_ok = False
    for col in required_columns:
        if col not in artifact[0]:
            shape_ok = False
            break
    for row in artifact:
        if any(v == "" or v is None for v in (row.get("W"), row.get("m_alpha"), row.get("m_beta"))):
            shape_ok = False
            break
    shape_score = 1.0 if shape_ok else 0.0

    # ordering check
    ordering_scores = []
    for rule in ordering_rules:
        cond = rule["condition"]
        relation = rule["relation"]
        region_rows = []
        for row in artifact:
            if eval_condition(row, cond):
                region_rows.append(row)
        if not region_rows:
            ordering_scores.append(0.0)
        else:
            satisfied = 0
            total = len(region_rows)
            for row in region_rows:
                if relation == "m_beta > m_alpha":
                    try:
                        ma = float(row["m_alpha"])
                        mb = float(row["m_beta"])
                        if mb > ma:
                            satisfied += 1
                    except:
                        total -= 1
                elif relation.startswith("m_alpha == 0 and m_beta == 0"):
                    tol = rule.get("tolerance", 0.001)
                    try:
                        ma = float(row["m_alpha"])
                        mb = float(row["m_beta"])
                        if abs(ma) <= tol and abs(mb) <= tol:
                            satisfied += 1
                    except:
                        total -= 1
                elif relation == "m_alpha > m_beta":
                    try:
                        ma = float(row["m_alpha"])
                        mb = float(row["m_beta"])
                        if ma > mb:
                            satisfied += 1
                    except:
                        total -= 1
                else:
                    satisfied += 1
            ordering_scores.append(satisfied / total if total > 0 else 0.0)
    ord_score = sum(ordering_scores) / len(ordering_scores) if ordering_scores else 0.0

    # reference points
    ref_score = 0.0
    if reference_points:
        hits = 0
        for rp in reference_points:
            w_ref = rp["W"]
            tol_m = rp.get("tol_m", 0.02)
            m_alpha_ref = rp["m_alpha"]
            m_beta_ref = rp["m_beta"]
            best_diff = float('inf')
            best_row = None
            for row in artifact:
                try:
                    w = float(row["W"])
                except:
                    continue
                diff = abs(w - w_ref)
                if diff < best_diff:
                    best_diff = diff
                    best_row = row
            if best_row is not None and best_diff <= 0.01:
                try:
                    ma = float(best_row["m_alpha"])
                    mb = float(best_row["m_beta"])
                    if abs(ma - m_alpha_ref) <= tol_m and abs(mb - m_beta_ref) <= tol_m:
                        hits += 1
                except:
                    pass
        ref_score = hits / len(reference_points)

    # discontinuity check
    disc_score = 0.0
    before_vals = {"m_alpha": [], "m_beta": []}
    after_vals = {"m_alpha": [], "m_beta": []}
    for row in artifact:
        try:
            w = float(row["W"])
            ma = float(row["m_alpha"])
            mb = float(row["m_beta"])
        except:
            continue
        if discontinuity_check.get("W_before_low", 0) <= w <= discontinuity_check.get("W_before_high", 0):
            before_vals["m_alpha"].append(ma)
            before_vals["m_beta"].append(mb)
        elif w >= discontinuity_check.get("W_after_low", 0):
            after_vals["m_alpha"].append(ma)
            after_vals["m_beta"].append(mb)
    if before_vals["m_alpha"] and after_vals["m_alpha"]:
        mean_ma_before = sum(before_vals["m_alpha"]) / len(before_vals["m_alpha"])
        mean_ma_after = sum(after_vals["m_alpha"]) / len(after_vals["m_alpha"])
        mean_mb_before = sum(before_vals["m_beta"]) / len(before_vals["m_beta"])
        mean_mb_after = sum(after_vals["m_beta"]) / len(after_vals["m_beta"])
        inc = mean_ma_after - mean_ma_before
        dec = mean_mb_before - mean_mb_after
        if inc >= discontinuity_check.get("m_alpha_increase_min", 0.003) and dec >= discontinuity_check.get("m_beta_decrease_min", 0.01):
            disc_score = 1.0
    else:
        disc_score = 0.0

    internal = shape_score * shape_w + ord_score * ord_w + ref_score * ref_w + disc_score * disc_w
    return internal / total_w


# === block: score_1 (check id='step_02_phase_boundaries') ===
def score_1(artifact, step, ctx):
    import csv

    params = step.get("params", {})
    required_columns = params.get("required_columns", [])
    min_rows = params.get("min_rows", 10)
    allowed_types = params.get("allowed_types", [])
    ref_neel = params.get("reference_neel_points", [])
    af1_af2_cep = params.get("af1_af2_cep", {})
    af2_pm_tcp = params.get("af2_pm_tcp", {})
    scoring_weights = step.get("scoring", {})

    shape_w = scoring_weights.get("shape_weight", 0.0)
    types_w = scoring_weights.get("types_present_weight", 0.0)
    neel_w = scoring_weights.get("neel_reference_weight", 0.0)
    cep_tcp_w = scoring_weights.get("cep_tcp_weight", 0.0)
    total_w = shape_w + types_w + neel_w + cep_tcp_w
    if total_w == 0:
        return 0.0

    # shape
    shape_ok = True
    if len(artifact) < min_rows:
        shape_ok = False
    for col in required_columns:
        if col not in artifact[0]:
            shape_ok = False
    for row in artifact:
        if any(v == "" or v is None for v in (row.get("W"), row.get("T"), row.get("boundary_type"))):
            shape_ok = False
            break
    shape_score = 1.0 if shape_ok else 0.0

    # types present
    present_types = set()
    for row in artifact:
        bt = row.get("boundary_type", "").strip()
        if bt in allowed_types:
            present_types.add(bt)
    types_score = 1.0 if set(allowed_types) == present_types else 0.0

    # Neel reference points
    neel_rows = [r for r in artifact if r.get("boundary_type","").strip() == "Neel"]
    neel_hits = 0
    for rp in ref_neel:
        w_ref = rp["W"]
        tol_T = rp.get("tol_T", 0.005)
        t_ref = rp["T"]
        best_diff = float('inf')
        best_row = None
        for row in neel_rows:
            try:
                w = float(row["W"])
            except:
                continue
            diff = abs(w - w_ref)
            if diff < best_diff:
                best_diff = diff
                best_row = row
        if best_row is not None and best_diff <= 0.02:
            try:
                T_val = float(best_row["T"])
                if abs(T_val - t_ref) <= tol_T:
                    neel_hits += 1
            except:
                pass
    neel_score = neel_hits / len(ref_neel) if ref_neel else 1.0

    # CEP and TCP
    cep_found = False
    tcp_found = False
    for row in artifact:
        bt = row.get("boundary_type","").strip()
        try:
            w = float(row["W"])
            T_val = float(row["T"])
        except:
            continue
        if bt == "AF1_AF2_first_order":
            if abs(w - af1_af2_cep.get("W",0.9826)) <= af1_af2_cep.get("tol_W",0.01) and abs(T_val - af1_af2_cep.get("T",0.0038)) <= af1_af2_cep.get("tol_T",0.001):
                cep_found = True
        elif bt == "AF2_PM_first_order":
            if abs(w - af2_pm_tcp.get("W",1.641)) <= af2_pm_tcp.get("tol_W",0.01) and abs(T_val - af2_pm_tcp.get("T",0.0011)) <= af2_pm_tcp.get("tol_T",0.0005):
                tcp_found = True
    cep_tcp_score = ((1.0 if cep_found else 0.0) + (1.0 if tcp_found else 0.0)) / 2.0

    internal = shape_score * shape_w + types_score * types_w + neel_score * neel_w + cep_tcp_score * cep_tcp_w
    return internal / total_w


_SCORERS = {
    'step_01_order_params': score_0,
    'step_02_phase_boundaries': score_1,
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
