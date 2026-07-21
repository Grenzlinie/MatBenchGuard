import os
import json
import csv

# === author imports / helpers ===
import csv
import os

def tolerance_ok(val, ref_val, tol):
    return abs(val - ref_val) <= tol


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dicts
    ref = step.get("reference", {})
    tol_T = step.get("tolerances", {}).get("T_abs", 0.1)
    tol_I = step.get("tolerances", {}).get("I_abs", 0.03)

    rows_by_key = {}
    for r in artifact_rows:
        ph = r.get("phase", "").strip()
        try:
            dx = float(r["doping_x"])
        except:
            continue
        rows_by_key[(ph, dx)] = r

    # numeric match per required point (binary)
    total_pts = 0
    match_pts = 0
    for phase_name in ["CF", "SF"]:
        ref_pts = ref.get(phase_name, [])
        for p in ref_pts:
            dx = p["doping_x"]
            key = (phase_name, dx)
            total_pts += 1
            row = rows_by_key.get(key)
            if row is None:
                continue
            try:
                T_val = float(row["T"])
                I_val = float(row["I"])
            except:
                continue
            if abs(T_val - p["T"]) <= tol_T and abs(I_val - p["I"]) <= tol_I:
                match_pts += 1

    numeric_score = match_pts / max(total_pts, 1)

    # trend checks (stricter)
    trend_scores = []
    for ph in ["CF", "SF"]:
        phase_rows = [r for r in artifact_rows if r.get("phase", "").strip() == ph]
        phase_rows.sort(key=lambda r: float(r.get("doping_x", 0)))
        if len(phase_rows) < 4:
            trend_scores.extend([0.0, 0.0])
            continue
        I_vals = [float(r.get("I", 0)) for r in phase_rows]
        T_vals = [float(r.get("T", 0)) for r in phase_rows]

        # I monotonic non-increasing with non-trivial variation
        decr = all(I_vals[i] >= I_vals[i+1] - 1e-9 for i in range(len(I_vals)-1))
        span = max(I_vals) - min(I_vals)
        if decr and span > 0.005 and sum(I_vals) > 0.001 * len(I_vals):
            trend_scores.append(1.0)
        elif decr and span > 0.005:
            trend_scores.append(0.5)
        else:
            trend_scores.append(0.0)

        # T roughly constant and physically meaningful (non-zero magnitude)
        avgT = sum(T_vals) / len(T_vals)
        if abs(avgT) > 0.1:
            var = sum((v - avgT) ** 2 for v in T_vals) / len(T_vals)
            std = var ** 0.5
            if std < 0.05:
                trend_scores.append(1.0)
            elif std < 0.1:
                trend_scores.append(0.5)
            else:
                trend_scores.append(0.0)
        else:
            trend_scores.append(0.0)

    # CF continuous vanishing
    cf_rows = [r for r in artifact_rows if r.get("phase", "").strip() == "CF"]
    cf_dict = {}
    for r in cf_rows:
        try:
            x = float(r["doping_x"])
        except:
            continue
        cf_dict[x] = float(r.get("I", 0))
    if 0.194 in cf_dict and 0.139 in cf_dict:
        if cf_dict[0.194] <= 0.005 and cf_dict[0.139] > 0.005:
            trend_scores.append(1.0)
        else:
            trend_scores.append(0.0)
    else:
        trend_scores.append(0.0)

    # SF discontinuous vanishing
    sf_rows = [r for r in artifact_rows if r.get("phase", "").strip() == "SF"]
    sf_dict = {}
    for r in sf_rows:
        try:
            x = float(r["doping_x"])
        except:
            continue
        sf_dict[x] = float(r.get("I", 0))
    if 0.167 in sf_dict and 0.139 in sf_dict:
        if sf_dict[0.167] <= 0.005 and sf_dict[0.139] > 0.001:
            trend_scores.append(1.0)
        else:
            trend_scores.append(0.0)
    else:
        trend_scores.append(0.0)

    trend_score = sum(trend_scores) / max(len(trend_scores), 1)
    return 0.6 * numeric_score + 0.4 * trend_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    artifact_rows = artifact
    ref = step.get("reference", {})
    tol_T = step.get("tolerances", {}).get("T_abs", 0.1)
    tol_I = step.get("tolerances", {}).get("I_abs", 0.04)
    trend = step.get("trend_checks", {})

    # Numeric match by (phase, U_over_t)
    rows_by_key = {}
    for row in artifact_rows:
        phase = row["phase"].strip()
        try:
            U = float(row["U_over_t"])
        except:
            continue
        rows_by_key[(phase, U)] = row

    numeric_total = 0
    numeric_matches = 0
    for phase in ["CF", "SF"]:
        ref_points = ref.get(phase, [])
        for p in ref_points:
            U = p["U_over_t"]
            key = (phase, U)
            numeric_total += 1
            if key in rows_by_key:
                r = rows_by_key[key]
                if tolerance_ok(float(r["T"]), p["T"], tol_T) and tolerance_ok(float(r["I"]), p["I"], tol_I):
                    numeric_matches += 1
    numeric_score = numeric_matches / max(numeric_total, 1)

    trend_scores = []

    # Phase rows sorted by U
    cf_rows = [r for r in artifact_rows if r["phase"].strip() == "CF"]
    cf_rows.sort(key=lambda r: float(r["U_over_t"]))
    sf_rows = [r for r in artifact_rows if r["phase"].strip() == "SF"]
    sf_rows.sort(key=lambda r: float(r["U_over_t"]))

    # CF T constant within band
    import statistics
    cf_T_vals = [float(r["T"]) for r in cf_rows]
    if cf_T_vals:
        avg = statistics.mean(cf_T_vals)
        within = all(abs(v - avg) <= trend.get("CF_T_constant", 0.05) for v in cf_T_vals)
        trend_scores.append(1.0 if within else 0.0)
    else:
        trend_scores.append(0.0)

    # CF I increasing (non-decreasing)
    cf_I_vals = [float(r["I"]) for r in cf_rows]
    inc_cf = True
    for i in range(len(cf_I_vals)-1):
        if cf_I_vals[i+1] + 1e-5 < cf_I_vals[i]:
            inc_cf = False
            break
    trend_scores.append(1.0 if inc_cf else 0.0)

    # SF T decreasing (non-increasing, i.e., more negative)
    sf_T_vals = [float(r["T"]) for r in sf_rows]
    if sf_T_vals:
        decr_sf_T = True
        for i in range(len(sf_T_vals)-1):
            if sf_T_vals[i+1] - sf_T_vals[i] > 1e-5:  # T becomes less negative
                decr_sf_T = False
                break
        trend_scores.append(1.0 if decr_sf_T else 0.0)
    else:
        trend_scores.append(0.0)

    # SF I increasing
    sf_I_vals = [float(r["I"]) for r in sf_rows]
    inc_sf = True
    for i in range(len(sf_I_vals)-1):
        if sf_I_vals[i+1] + 1e-5 < sf_I_vals[i]:
            inc_sf = False
            break
    trend_scores.append(1.0 if inc_sf else 0.0)

    trend_score = sum(trend_scores) / max(len(trend_scores), 1)
    return 0.7 * numeric_score + 0.3 * trend_score


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    artifact_rows = artifact
    ref = step.get("reference", {})
    tol_I = step.get("tolerances", {}).get("I_abs", 0.03)
    trend = step.get("trend_checks", {})

    rows_by_key = {}
    for row in artifact_rows:
        phase = row["phase"].strip()
        try:
            K = float(row["K_over_t"])
        except:
            continue
        rows_by_key[(phase, K)] = row

    numeric_total = 0
    numeric_matches = 0
    for phase in ["CF", "SF"]:
        ref_points = ref.get(phase, [])
        for p in ref_points:
            K = p["K_over_t"]
            key = (phase, K)
            numeric_total += 1
            if key in rows_by_key:
                I_val = float(rows_by_key[key]["I"])
                if tolerance_ok(I_val, p["I"], tol_I):
                    numeric_matches += 1
    numeric_score = numeric_matches / max(numeric_total, 1)

    trend_scores = []
    # CF I decreasing with K
    cf_rows = [r for r in artifact_rows if r["phase"].strip() == "CF"]
    cf_rows.sort(key=lambda r: float(r["K_over_t"]))
    cf_I = [float(r["I"]) for r in cf_rows]
    decr_cf = True
    for i in range(len(cf_I)-1):
        if cf_I[i+1] + 1e-5 < cf_I[i]:
            decr_cf = False
            break
    trend_scores.append(1.0 if decr_cf else 0.0)

    # SF I increasing with K
    sf_rows = [r for r in artifact_rows if r["phase"].strip() == "SF"]
    sf_rows.sort(key=lambda r: float(r["K_over_t"]))
    sf_I = [float(r["I"]) for r in sf_rows]
    inc_sf = True
    for i in range(len(sf_I)-1):
        if sf_I[i+1] + 1e-5 < sf_I[i]:
            inc_sf = False
            break
    trend_scores.append(1.0 if inc_sf else 0.0)

    trend_score = sum(trend_scores) / max(len(trend_scores), 1)
    return 0.7 * numeric_score + 0.3 * trend_score


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    artifact_rows = artifact
    ref = step.get("reference", [])
    tol_T = step.get("tolerances", {}).get("T_abs", 0.1)
    tol_I = step.get("tolerances", {}).get("I_abs", 0.04)
    trend = step.get("trend_checks", {})

    rows_by_doping = {}
    for row in artifact_rows:
        try:
            x = float(row["doping_x"])
        except:
            continue
        rows_by_doping[x] = row

    numeric_total = len(ref)
    numeric_matches = 0
    for p in ref:
        x = p["doping_x"]
        if x in rows_by_doping:
            r = rows_by_doping[x]
            if tolerance_ok(float(r["T"]), p["T"], tol_T) and tolerance_ok(float(r["I"]), p["I"], tol_I):
                numeric_matches += 1
    numeric_score = numeric_matches / max(numeric_total, 1)

    trend_scores = []
    # I peak near 0.083
    center = trend.get("I_peak_near_0083", {}).get("doping_center", 0.083)
    left = trend.get("I_peak_near_0083", {}).get("doping_left", 0.0)
    right = trend.get("I_peak_near_0083", {}).get("doping_right", 0.167)
    def get_I(x):
        if x in rows_by_doping:
            return float(rows_by_doping[x]["I"])
        return None
    I_c = get_I(center)
    I_l = get_I(left)
    I_r = get_I(right)
    peak_ok = False
    if I_c is not None and I_l is not None and I_r is not None:
        if I_c >= I_l - 1e-5 and I_c >= I_r - 1e-5:
            peak_ok = True
    trend_scores.append(1.0 if peak_ok else 0.0)

    # T decreasing (more negative) with doping
    sorted_rows = sorted(artifact_rows, key=lambda r: float(r["doping_x"]))
    T_vals = [float(r["T"]) for r in sorted_rows]
    decr_T = True
    for i in range(len(T_vals)-1):
        if T_vals[i+1] - T_vals[i] > 1e-5:  # less negative
            decr_T = False
            break
    trend_scores.append(1.0 if decr_T else 0.0)

    trend_score = sum(trend_scores) / max(len(trend_scores), 1)
    return 0.7 * numeric_score + 0.3 * trend_score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
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
