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
    geo2_raw = [
        (8.64, 0.299), (9.52, 0.423), (10.45, 0.557), (11.56, 0.729), (12.84, 0.945),
        (14.14, 1.185), (15.48, 1.451), (16.84, 1.735), (18.39, 2.072), (20.10, 2.478),
        (21.83, 2.889), (23.59, 3.327), (25.37, 3.785), (27.30, 4.286), (29.36, 4.824),
        (31.44, 5.364), (33.55, 5.955), (35.67, 6.498), (37.95, 7.138), (40.37, 7.753),
        (42.81, 8.426), (45.26, 9.144), (47.73, 9.858), (50.40, 10.62), (53.27, 11.45),
        (56.15, 12.24), (59.04, 13.16), (65.09, 14.88), (68.53, 15.83), (75.19, 17.39),
        (78.76, 18.31), (82.65, 19.4), (86.72, 20.61), (91.01, 21.66), (95.52, 22.74),
        (100.3, 23.78), (105.2, 24.95), (110.2, 26.03), (115.2, 27.24), (120.2, 28.26),
        (125.5, 29.41), (131.1, 30.54), (136.6, 31.57), (142.2, 32.65), (147.7, 33.68),
        (153.3, 34.67), (158.9, 35.63), (164.5, 36.55), (170.1, 37.45), (175.8, 38.28),
        (181.5, 39.16), (187.3, 39.92), (193.2, 40.81), (199.0, 41.65), (204.8, 42.47),
        (210.7, 43.21), (216.5, 43.99), (222.4, 44.78), (228.3, 45.64), (234.1, 46.26),
        (240.1, 47.10), (246.1, 47.64), (252.2, 48.37), (258.4, 49.03), (264.5, 49.68),
        (270.7, 50.41), (276.9, 50.89), (283.1, 51.54), (289.2, 51.91), (295.4, 52.66),
        (301.6, 53.27), (307.7, 53.78), (313.9, 54.34), (320.1, 54.68), (326.3, 55.13),
        (332.6, 55.56), (338.8, 55.85), (345.0, 56.39)
    ]

    b2o3_raw = [
        (4.93, 0.110), (5.32, 0.149), (6.09, 0.202), (7.08, 0.310), (8.21, 0.489),
        (11.54, 1.180), (12.76, 1.452), (14.00, 1.757), (15.29, 2.087), (16.70, 2.468),
        (18.23, 2.899), (20.03, 3.430), (22.18, 4.087), (24.55, 4.823), (27.10, 5.635),
        (29.70, 6.484), (32.29, 7.350), (35.03, 8.266), (38.29, 9.350), (41.76, 10.48),
        (42.17, 10.61), (45.98, 11.85), (50.57, 13.29), (55.84, 14.88), (61.80, 16.62),
        (57.43, 15.35), (62.28, 16.77), (67.97, 18.30), (74.41, 19.88), (81.31, 21.66),
        (88.25, 23.31), (95.29, 24.82), (111.21, 28.17), (119.40, 29.86), (127.64, 31.55),
        (135.90, 33.21), (144.33, 34.88), (153.35, 36.55), (167.96, 39.50), (177.36, 41.30),
        (186.65, 43.09), (195.95, 44.84), (205.09, 46.52), (214.23, 48.19), (223.50, 49.91),
        (232.85, 51.58), (242.47, 53.30), (252.37, 55.01), (262.33, 56.73), (272.44, 58.40),
        (262.75, 56.22), (272.36, 58.15), (282.20, 60.03), (292.43, 61.66), (303.00, 63.34),
        (313.53, 65.05), (323.83, 66.68), (334.03, 68.23)
    ]

    def integrate(raw):
        sorted_data = sorted(raw, key=lambda x: x[0])
        T = [0.0]
        Cp = [0.0]
        for t, c in sorted_data:
            T.append(t)
            Cp.append(c)
        n = len(T)
        S = [0.0]*n
        H = [0.0]*n
        for i in range(1, n):
            dT = T[i] - T[i-1]
            if dT > 0:
                H[i] = H[i-1] + 0.5*(Cp[i-1] + Cp[i])*dT
                if T[i-1] == 0.0:
                    S[i] = S[i-1] + Cp[i]
                else:
                    avg = 0.5*(Cp[i-1]/T[i-1] + Cp[i]/T[i])
                    S[i] = S[i-1] + avg*dT
        return T[1:], S[1:], H[1:]

    def interpolate(T_raw, V_raw, T_target):
        result = []
        pos = 0
        for t in T_target:
            while pos < len(T_raw)-1 and T_raw[pos+1] <= t:
                pos += 1
            if t <= T_raw[0]:
                result.append(V_raw[0])
            elif t >= T_raw[-1]:
                result.append(V_raw[-1])
            else:
                t1, v1 = T_raw[pos], V_raw[pos]
                t2, v2 = T_raw[pos+1], V_raw[pos+1]
                frac = (t - t1)/(t2 - t1)
                result.append(v1 + frac*(v2 - v1))
        return result

    Tgrid = [5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,
             110,120,130,140,150,160,170,180,190,200,210,220,
             230,240,250,260,270,280,290,300,310,320,330,340,350]

    T_raw_g, S_raw_g, H_raw_g = integrate(geo2_raw)
    exp_S_geo2 = interpolate(T_raw_g, S_raw_g, Tgrid)
    exp_H_geo2 = interpolate(T_raw_g, H_raw_g, Tgrid)
    exp_G_geo2 = [exp_S_geo2[i] - exp_H_geo2[i]/t for i, t in enumerate(Tgrid)]

    T_raw_b, S_raw_b, H_raw_b = integrate(b2o3_raw)
    exp_S_b2o3 = interpolate(T_raw_b, S_raw_b, Tgrid)
    exp_H_b2o3 = interpolate(T_raw_b, H_raw_b, Tgrid)
    exp_G_b2o3 = [exp_S_b2o3[i] - exp_H_b2o3[i]/t for i, t in enumerate(Tgrid)]

    return {
        "geo2": (exp_S_geo2, exp_H_geo2, exp_G_geo2),
        "b2o3": (exp_S_b2o3, exp_H_b2o3, exp_G_b2o3),
        "Tgrid": Tgrid
    }


# === block: score_0 (check id='step_geo2_funcs') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        exp_S, exp_H, exp_G = ctx["geo2"]
        Tgrid = ctx["Tgrid"]
        if len(rows) != len(Tgrid):
            return 0.0
        # Read tolerances from grading_spec step definition
        tol = step.get("tolerance", {})
        tol_S = tol.get("S", 0.5)
        tol_H = tol.get("H", 10.0)
        tol_G = tol.get("G", 0.5)
        passed = 0
        for i, row in enumerate(rows):
            try:
                s = float(row.get("S_T_minus_S0(J/mol_K)", math.nan))
                h = float(row.get("H_T_minus_H0(J/mol)", math.nan))
                g = float(row.get("minus_G_T_minus_H0_over_T(J/mol_K)", math.nan))
                if (not math.isnan(s) and not math.isnan(h) and not math.isnan(g) and
                    abs(s - exp_S[i]) <= tol_S and abs(h - exp_H[i]) <= tol_H and abs(g - exp_G[i]) <= tol_G):
                    passed += 1
            except (ValueError, TypeError):
                pass
        return passed / len(Tgrid)
    except Exception:
        return 0.0


# === block: score_1 (check id='step_b2o3_funcs') ===
def score_1(artifact, step, ctx):
    try:
        rows = artifact
        exp_S, exp_H, exp_G = ctx["b2o3"]
        Tgrid = ctx["Tgrid"]
        if len(rows) != len(Tgrid):
            return 0.0
        tol_S, tol_H, tol_G = 0.5, 10.0, 0.5
        passed = 0
        for i, row in enumerate(rows):
            try:
                s = float(row.get("S_T_minus_S0(J/mol_K)", math.nan))
                h = float(row.get("H_T_minus_H0(J/mol)", math.nan))
                g = float(row.get("minus_G_T_minus_H0_over_T(J/mol_K)", math.nan))
                if (not math.isnan(s) and not math.isnan(h) and not math.isnan(g) and
                    abs(s - exp_S[i]) <= tol_S and abs(h - exp_H[i]) <= tol_H and abs(g - exp_G[i]) <= tol_G):
                    passed += 1
            except (ValueError, TypeError):
                pass
        return passed / len(Tgrid)
    except Exception:
        return 0.0


# === block: score_2 (check id='step_residual_entropy') ===
def score_2(artifact, step, ctx):
    try:
        val_g = float(artifact.get("GeO2", math.nan))
        val_b = float(artifact.get("B2O3", math.nan))
        if math.isnan(val_g) or math.isnan(val_b):
            return 0.0
        score_g = max(0.0, 1.0 - abs(val_g - 6.6) / 1.5)
        score_b = max(0.0, 1.0 - abs(val_b - 11.2) / 1.5)
        return (score_g + score_b) / 2.0
    except Exception:
        return 0.0


_SCORERS = {
    'step_geo2_funcs': score_0,
    'step_b2o3_funcs': score_1,
    'step_residual_entropy': score_2,
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
