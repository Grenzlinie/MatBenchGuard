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


# === block: score_0 (check id='step_film_conductance') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    data = {}
    for row in artifact:
        try:
            tn = float(row.get("thickness_nm", 0))
            cond = float(row.get("conductance_W_per_K", 0))
            if tn > 0 and cond > 0:
                data[tn] = cond
        except (ValueError, TypeError):
            continue

    if len(data) < 5:
        return 0.0

    ref_pts = step.get("reference_points", [])
    tol_rel = float(step.get("tolerance_rel", 0.30))

    pt_scores = []
    for rp in ref_pts:
        rt = float(rp.get("thickness_nm", 0))
        rc = float(rp.get("conductance_W_per_K", 0))
        if rc <= 0:
            continue
        if not data:
            pt_scores.append(0.0)
            continue
        closest = min(data.keys(), key=lambda x: abs(x - rt))
        ac = data[closest]
        re = abs(ac - rc) / rc
        if re <= tol_rel:
            s = 1.0
        elif re >= 3.0 * tol_rel:
            s = 0.0
        else:
            s = 1.0 - (re - tol_rel) / (2.0 * tol_rel)
        pt_scores.append(max(0.0, min(1.0, s)))

    val_score = sum(pt_scores) / len(pt_scores) if pt_scores else 0.0

    t_sorted = sorted(data.keys())
    cond_vals = [data[t] for t in t_sorted]
    if len(cond_vals) >= 2:
        decreasing = sum(1 for i in range(len(cond_vals)-1) if cond_vals[i] >= cond_vals[i+1] * 0.95)
        mono_score = decreasing / (len(cond_vals) - 1)
    else:
        mono_score = 0.0

    return 0.70 * val_score + 0.30 * mono_score


# === block: score_1 (check id='step_wire_conductivity') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    data = {}
    for row in artifact:
        try:
            d = float(row.get("diameter_nm", 0))
            t = float(row.get("temperature_K", 0))
            k = float(row.get("thermal_conductivity_W_per_mK", 0))
            if d > 0 and t > 0 and k > 0:
                data[(d, t)] = k
        except (ValueError, TypeError):
            continue

    if len(data) < 12:
        return 0.0

    ref_pts = step.get("reference_points", [])
    tol_rel = float(step.get("tolerance_rel", 0.35))

    pt_scores = []
    for rp in ref_pts:
        rd = float(rp.get("diameter_nm", 0))
        rt = float(rp.get("temperature_K", 0))
        rk = float(rp.get("thermal_conductivity_W_per_mK", 0))
        if rk <= 0:
            continue
        if not data:
            pt_scores.append(0.0)
            continue
        best_key = min(data.keys(), key=lambda k: abs(k[0] - rd) + abs(k[1] - rt))
        ak = data[best_key]
        re = abs(ak - rk) / rk
        if re <= tol_rel:
            s = 1.0
        elif re >= 3.0 * tol_rel:
            s = 0.0
        else:
            s = 1.0 - (re - tol_rel) / (2.0 * tol_rel)
        pt_scores.append(max(0.0, min(1.0, s)))

    val_score = sum(pt_scores) / len(pt_scores) if pt_scores else 0.0

    diameters_of_interest = [37.0, 56.0, 115.0]
    temperatures = sorted(set(k[1] for k in data.keys()))
    order_scores = []
    for temp in temperatures:
        k_vals = {}
        for dd in diameters_of_interest:
            key = (dd, temp)
            if key in data:
                k_vals[dd] = data[key]
            else:
                candidates = [(abs(k[0] - dd), k) for k in data.keys() if abs(k[1] - temp) < 20.0]
                if candidates:
                    k_vals[dd] = data[min(candidates)[1]]
        if len(k_vals) >= 2:
            sorted_d = sorted(k_vals.keys())
            vals = [k_vals[d] for d in sorted_d]
            correct = sum(1 for i in range(len(vals)-1) if vals[i] <= vals[i+1])
            order_scores.append(correct / (len(vals) - 1))

    order_score = sum(order_scores) / len(order_scores) if order_scores else 0.5

    return 0.70 * val_score + 0.30 * order_score


# === block: score_2 (check id='step_transient') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    film_rows = []
    wire_rows = []
    for r in artifact:
        sys_name = str(r.get("system", "")).strip().lower()
        if "film" in sys_name:
            film_rows.append(r)
        elif "wire" in sys_name or "nanowire" in sys_name:
            wire_rows.append(r)

    def parse_pts(rows):
        pts = []
        for r in rows:
            try:
                t = float(r.get("time_ns", 0))
                T = float(r.get("temperature_K", 0))
                if T > 0:
                    pts.append((t, T))
            except (ValueError, TypeError):
                continue
        pts.sort()
        return pts

    film_pts = parse_pts(film_rows)
    wire_pts = parse_pts(wire_rows)

    if len(film_pts) < 4 or len(wire_pts) < 4:
        return 0.0

    # ---- Film scoring (max 0.50) ----
    film_score = 0.0
    times_f = [p[0] for p in film_pts]
    temps_f = [p[1] for p in film_pts]

    # Initial temperature near 10K
    if abs(temps_f[0] - 10.0) <= 3.0:
        film_score += 0.05

    # Ballistic step detection: look for plateaus (|dT| < 0.5K between consecutive)
    # AND steps (dT > 2.0K) indicating ballistic propagation
    dTs = [temps_f[i+1] - temps_f[i] for i in range(len(temps_f)-1)]
    has_plateau = any(abs(dT) < 0.5 for dT in dTs)
    has_step = any(dT > 2.0 for dT in dTs)
    if has_plateau and has_step:
        film_score += 0.20

    # Final temperature increase
    if temps_f[-1] > temps_f[0] + 3.0:
        film_score += 0.05

    # Compare to hidden gold at key times
    film_refs = step.get("film_reference", [])
    tol_abs = float(step.get("tolerance_abs_K", 5.0))
    f_scores = []
    for ref in film_refs:
        rt = float(ref.get("time_ns", 0))
        rT = float(ref.get("temperature_K", 0))
        if not times_f:
            f_scores.append(0.0)
            continue
        idx = min(range(len(times_f)), key=lambda i: abs(times_f[i] - rt))
        aT = temps_f[idx]
        err = abs(aT - rT)
        if err <= tol_abs:
            f_scores.append(1.0)
        elif err <= 2.0 * tol_abs:
            f_scores.append(0.5)
        else:
            f_scores.append(0.0)
    f_val = sum(f_scores) / len(f_scores) if f_scores else 0.0
    film_score += f_val * 0.20

    film_score = min(film_score, 0.50)

    # ---- Nanowire scoring (max 0.50) ----
    wire_score = 0.0
    times_w = [p[0] for p in wire_pts]
    temps_w = [p[1] for p in wire_pts]

    # Monotonic increasing
    if len(temps_w) >= 2:
        mono = all(temps_w[i+1] >= temps_w[i] - 0.1 for i in range(len(temps_w)-1))
        if mono:
            wire_score += 0.15

    # Final temperature increase
    if temps_w[-1] > temps_w[0] + 5.0:
        wire_score += 0.05

    # Compare to hidden gold at key times
    wire_refs = step.get("nanowire_reference", [])
    w_scores = []
    for ref in wire_refs:
        rt = float(ref.get("time_ns", 0))
        rT = float(ref.get("temperature_K", 0))
        if not times_w:
            w_scores.append(0.0)
            continue
        idx = min(range(len(times_w)), key=lambda i: abs(times_w[i] - rt))
        aT = temps_w[idx]
        err = abs(aT - rT)
        if err <= tol_abs:
            w_scores.append(1.0)
        elif err <= 2.0 * tol_abs:
            w_scores.append(0.5)
        else:
            w_scores.append(0.0)
    w_val = sum(w_scores) / len(w_scores) if w_scores else 0.0
    wire_score += w_val * 0.30

    wire_score = min(wire_score, 0.50)

    return film_score + wire_score


_SCORERS = {
    'step_film_conductance': score_0,
    'step_wire_conductivity': score_1,
    'step_transient': score_2,
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
