import os
import json
import csv

# === author imports / helpers ===
import math, json, os


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
    spec = json.load(open('/tests/grading_spec.json'))
    steps = spec['steps']
    ctx = {'spec': spec, 'steps': steps}
    for s in steps:
        ctx[s['id']] = s
    return ctx


# === block: score_0 (check id='delta_T_and_ZT') ===
def score_0(artifact, step, ctx):
    step = ctx['delta_T_and_ZT']
    pts = step['gold_points']
    gold_dT_B = step['gold_Delta_T_B']
    gold_dT_V = step['gold_Delta_T_V']
    gold_ZT_B = step['gold_ZT_B']
    gold_ZT_V = step['gold_ZT_V']
    tol_dT = step['tolerance_Delta_T']
    tol_ZT = step['tolerance_ZT']
    col_C = step['columns']['C']
    col_TH_B = step['columns']['T_H_B']
    col_TC_B = step['columns']['T_C_B']
    col_DT_B = step['columns']['Delta_T_B']
    col_ZT_B = step['columns']['ZT_B']
    col_TH_V = step['columns']['T_H_V']
    col_TC_V = step['columns']['T_C_V']
    col_DT_V = step['columns']['Delta_T_V']
    col_ZT_V = step['columns']['ZT_V']
    rows_by_C = {}
    for row in artifact:
        try:
            c = float(row[col_C])
            rows_by_C[c] = row
        except:
            continue
    score = 0.0
    count = 0
    for i, c in enumerate(pts):
        row = rows_by_C.get(c)
        if row is None:
            continue
        try:
            dT_B = float(row[col_TH_B]) - float(row[col_TC_B])
            dT_V = float(row[col_TH_V]) - float(row[col_TC_V])
            zt_B = float(row[col_ZT_B])
            zt_V = float(row[col_ZT_V])
        except:
            continue
        # score Delta_T
        if abs(dT_B - gold_dT_B[i]) <= tol_dT * gold_dT_B[i]:
            score += 0.25
        else:
            score += max(0.0, 1.0 - abs(dT_B - gold_dT_B[i]) / (tol_dT * 2 * gold_dT_B[i])) * 0.25
        if abs(dT_V - gold_dT_V[i]) <= tol_dT * gold_dT_V[i]:
            score += 0.25
        else:
            score += max(0.0, 1.0 - abs(dT_V - gold_dT_V[i]) / (tol_dT * 2 * gold_dT_V[i])) * 0.25
        # score ZT
        if abs(zt_B - gold_ZT_B[i]) <= tol_ZT:
            score += 0.25
        else:
            score += max(0.0, 1.0 - abs(zt_B - gold_ZT_B[i]) / (tol_ZT * 2)) * 0.25
        if abs(zt_V - gold_ZT_V[i]) <= tol_ZT:
            score += 0.25
        else:
            score += max(0.0, 1.0 - abs(zt_V - gold_ZT_V[i]) / (tol_ZT * 2)) * 0.25
        count += 1
    return score / max(1, count * 4) * 4  # normalize to 0..1


# === block: score_1 (check id='heat_loss_and_power') ===
def score_1(artifact, step, ctx):
    step = ctx['heat_loss_and_power']
    pts = step['gold_points']
    gold_QL_B = step['gold_Q_loss_B']
    gold_QL_V = step['gold_Q_loss_V']
    gold_P_B = step['gold_P_TEG_B']
    gold_P_V = step['gold_P_TEG_V']
    tol_Q = step['tolerance_Q']
    tol_P = step['tolerance_P']
    col_C = step['columns']['C']
    col_QL_B = step['columns']['Q_loss_B']
    col_P_B = step['columns']['P_TEG_B']
    col_QL_V = step['columns']['Q_loss_V']
    col_P_V = step['columns']['P_TEG_V']
    rows_by_C = {}
    for row in artifact:
        try:
            c = float(row[col_C])
            rows_by_C[c] = row
        except:
            continue
    score = 0.0
    count = 0
    for i, c in enumerate(pts):
        row = rows_by_C.get(c)
        if row is None:
            continue
        try:
            ql_b = float(row[col_QL_B])
            ql_v = float(row[col_QL_V])
            p_b = float(row[col_P_B])
            p_v = float(row[col_P_V])
        except:
            continue
        pts_score = 0.0
        ref = gold_QL_B[i]
        if ref > 1:
            pts_score += 0.25 if abs(ql_b - ref) <= tol_Q * ref else max(0.0, 1.0 - abs(ql_b - ref) / (tol_Q * 2 * ref)) * 0.25
        else:
            pts_score += 0.25 if abs(ql_b - ref) <= 1.0 else max(0.0, 1.0 - abs(ql_b - ref) / 2.0) * 0.25
        ref = gold_QL_V[i]
        if ref > 1:
            pts_score += 0.25 if abs(ql_v - ref) <= tol_Q * ref else max(0.0, 1.0 - abs(ql_v - ref) / (tol_Q * 2 * ref)) * 0.25
        else:
            pts_score += 0.25 if abs(ql_v - ref) <= 1.0 else max(0.0, 1.0 - abs(ql_v - ref) / 2.0) * 0.25
        ref = gold_P_B[i]
        if ref > 1:
            pts_score += 0.25 if abs(p_b - ref) <= tol_P * ref else max(0.0, 1.0 - abs(p_b - ref) / (tol_P * 2 * ref)) * 0.25
        else:
            pts_score += 0.25 if abs(p_b - ref) <= 1.0 else max(0.0, 1.0 - abs(p_b - ref) / 2.0) * 0.25
        ref = gold_P_V[i]
        if ref > 1:
            pts_score += 0.25 if abs(p_v - ref) <= tol_P * ref else max(0.0, 1.0 - abs(p_v - ref) / (tol_P * 2 * ref)) * 0.25
        else:
            pts_score += 0.25 if abs(p_v - ref) <= 1.0 else max(0.0, 1.0 - abs(p_v - ref) / 2.0) * 0.25
        score += pts_score
        count += 1
    return score / max(1, count * 4) * 4


# === block: score_2 (check id='efficiency_vs_C_water') ===
def score_2(artifact, step, ctx):
    step = ctx['efficiency_vs_C_water']
    pts = step['gold_points']
    gold_ee_B = step['gold_eta_elec_B']
    gold_et_B = step['gold_eta_th_B']
    gold_ee_V = step['gold_eta_elec_V']
    gold_et_V = step['gold_eta_th_V']
    tol_ee = step['tolerance_eta_elec']
    tol_et = step['tolerance_eta_th']
    col_C = step['columns']['C']
    col_ee_B = step['columns']['eta_elec_B']
    col_et_B = step['columns']['eta_th_B']
    col_ee_V = step['columns']['eta_elec_V']
    col_et_V = step['columns']['eta_th_V']
    rows_by_C = {}
    for row in artifact:
        try:
            c = int(float(row[col_C]))
            rows_by_C[c] = row
        except:
            continue
    score = 0.0
    count = 0
    for i, c in enumerate(pts):
        row = rows_by_C.get(c)
        if row is None:
            continue
        try:
            ee_b = float(row[col_ee_B])
            et_b = float(row[col_et_B])
            ee_v = float(row[col_ee_V])
            et_v = float(row[col_et_V])
        except:
            continue
        pts_score = 0.0
        pts_score += 0.25 if abs(ee_b - gold_ee_B[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_b - gold_ee_B[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_b - gold_et_B[i]) <= tol_et else max(0.0, 1.0 - abs(et_b - gold_et_B[i]) / (tol_et * 2)) * 0.25
        pts_score += 0.25 if abs(ee_v - gold_ee_V[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_v - gold_ee_V[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_v - gold_et_V[i]) <= tol_et else max(0.0, 1.0 - abs(et_v - gold_et_V[i]) / (tol_et * 2)) * 0.25
        score += pts_score
        count += 1
    return score / max(1, count * 4) * 4


# === block: score_3 (check id='efficiency_vs_C_oil') ===
def score_3(artifact, step, ctx):
    import statistics
    step = ctx['efficiency_vs_C_oil']
    col_ee_B = step['columns']['eta_elec_B']
    col_et_B = step['columns']['eta_th_B']
    col_ee_V = step['columns']['eta_elec_V']
    col_et_V = step['columns']['eta_th_V']
    rows = artifact
    score = 0.0
    if not rows:
        return 0.0
    # check all values in [0,1]
    valid = all([0 <= float(r.get(col_ee_B, 0)) <= 1 and 0 <= float(r.get(col_et_B, 0)) <= 1 and 0 <= float(r.get(col_ee_V, 0)) <= 1 and 0 <= float(r.get(col_et_V, 0)) <= 1 for r in rows])
    if not valid:
        score += 0.1
    else:
        score += 0.3
    # check monotonic trends: electrical efficiency should peak roughly around C 25-55, thermal should generally increase
    try:
        c_vals = [int(float(r['C'])) for r in rows]
        ee_B = [float(r[col_ee_B]) for r in rows]
        et_B = [float(r[col_et_B]) for r in rows]
        ee_V = [float(r[col_ee_V]) for r in rows]
        et_V = [float(r[col_et_V]) for r in rows]
        # Sort by C
        sorted_idx = sorted(range(len(c_vals)), key=lambda i: c_vals[i])
        c_sorted = [c_vals[i] for i in sorted_idx]
        ee_B_sorted = [ee_B[i] for i in sorted_idx]
        et_B_sorted = [et_B[i] for i in sorted_idx]
        ee_V_sorted = [ee_V[i] for i in sorted_idx]
        et_V_sorted = [et_V[i] for i in sorted_idx]
        trend_ok = 0.0
        # Check that thermal efficiency increases overall (end > start)
        if et_B_sorted[-1] > et_B_sorted[0]: trend_ok += 0.2
        if et_V_sorted[-1] > et_V_sorted[0]: trend_ok += 0.2
        # Electrical efficiency should have a local maximum between C 20 and 60
        peak_region_B = [x for x, c in zip(ee_B_sorted, c_sorted) if 20 <= c <= 80]
        if peak_region_B and max(peak_region_B) > ee_B_sorted[0] and max(peak_region_B) > ee_B_sorted[-1]:
            trend_ok += 0.1
        peak_region_V = [x for x, c in zip(ee_V_sorted, c_sorted) if 20 <= c <= 80]
        if peak_region_V and max(peak_region_V) > ee_V_sorted[0] and max(peak_region_V) > ee_V_sorted[-1]:
            trend_ok += 0.1
        score += trend_ok
    except:
        pass
    # Final score capped at 1.0
    return min(score, 1.0)


# === block: score_4 (check id='efficiency_vs_ZT') ===
def score_4(artifact, step, ctx):
    step = ctx['efficiency_vs_ZT']
    gold_ZT = step['gold_ZT']
    gold_ee_B = step['gold_eta_elec_B']
    gold_et_B = step['gold_eta_th_B']
    gold_ee_V = step['gold_eta_elec_V']
    gold_et_V = step['gold_eta_th_V']
    tol_ee = step['tolerance_eta_elec']
    tol_et = step['tolerance_eta_th']
    col_ZT = step['columns']['ZT']
    col_ee_B = step['columns']['eta_elec_B']
    col_et_B = step['columns']['eta_th_B']
    col_ee_V = step['columns']['eta_elec_V']
    col_et_V = step['columns']['eta_th_V']
    rows_by_ZT = {}
    for row in artifact:
        try:
            zt = float(row[col_ZT])
            rows_by_ZT[zt] = row
        except:
            continue
    score = 0.0
    count = 0
    for i, zt in enumerate(gold_ZT):
        row = rows_by_ZT.get(zt)
        if row is None:
            continue
        try:
            ee_b = float(row[col_ee_B])
            et_b = float(row[col_et_B])
            ee_v = float(row[col_ee_V])
            et_v = float(row[col_et_V])
        except:
            continue
        pts_score = 0.0
        pts_score += 0.25 if abs(ee_b - gold_ee_B[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_b - gold_ee_B[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_b - gold_et_B[i]) <= tol_et else max(0.0, 1.0 - abs(et_b - gold_et_B[i]) / (tol_et * 2)) * 0.25
        pts_score += 0.25 if abs(ee_v - gold_ee_V[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_v - gold_ee_V[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_v - gold_et_V[i]) <= tol_et else max(0.0, 1.0 - abs(et_v - gold_et_V[i]) / (tol_et * 2)) * 0.25
        score += pts_score
        count += 1
    return score / max(1, count * 4) * 4


# === block: score_5 (check id='efficiency_vs_Tcfi') ===
def score_5(artifact, step, ctx):
    step = ctx['efficiency_vs_Tcfi']
    gold_Tcfi = step['gold_Tcfi']
    gold_ee_B = step['gold_eta_elec_B']
    gold_et_B = step['gold_eta_th_B']
    gold_ee_V = step['gold_eta_elec_V']
    gold_et_V = step['gold_eta_th_V']
    tol_ee = step['tolerance_eta_elec']
    tol_et = step['tolerance_eta_th']
    col_Tcfi = step['columns']['Tcfi']
    col_ee_B = step['columns']['eta_elec_B']
    col_et_B = step['columns']['eta_th_B']
    col_ee_V = step['columns']['eta_elec_V']
    col_et_V = step['columns']['eta_th_V']
    rows_by_Tcfi = {}
    for row in artifact:
        try:
            t = int(float(row[col_Tcfi]))
            rows_by_Tcfi[t] = row
        except:
            continue
    score = 0.0
    count = 0
    for i, t in enumerate(gold_Tcfi):
        row = rows_by_Tcfi.get(t)
        if row is None:
            continue
        try:
            ee_b = float(row[col_ee_B])
            et_b = float(row[col_et_B])
            ee_v = float(row[col_ee_V])
            et_v = float(row[col_et_V])
        except:
            continue
        pts_score = 0.0
        pts_score += 0.25 if abs(ee_b - gold_ee_B[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_b - gold_ee_B[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_b - gold_et_B[i]) <= tol_et else max(0.0, 1.0 - abs(et_b - gold_et_B[i]) / (tol_et * 2)) * 0.25
        pts_score += 0.25 if abs(ee_v - gold_ee_V[i]) <= tol_ee else max(0.0, 1.0 - abs(ee_v - gold_ee_V[i]) / (tol_ee * 2)) * 0.25
        pts_score += 0.25 if abs(et_v - gold_et_V[i]) <= tol_et else max(0.0, 1.0 - abs(et_v - gold_et_V[i]) / (tol_et * 2)) * 0.25
        score += pts_score
        count += 1
    return score / max(1, count * 4) * 4


_SCORERS = {
    'delta_T_and_ZT': score_0,
    'heat_loss_and_power': score_1,
    'efficiency_vs_C_water': score_2,
    'efficiency_vs_C_oil': score_3,
    'efficiency_vs_ZT': score_4,
    'efficiency_vs_Tcfi': score_5,
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
