import os
import json
import csv

# === author imports / helpers ===
import json, csv, os

def interpolate_zero_crossing(pressures, dGs):
    signs = [1 if dg > 0 else -1 if dg < 0 else 0 for dg in dGs]
    for i in range(len(signs)-1):
        if signs[i] != 0 and signs[i] != signs[i+1] and signs[i+1] != 0:
            p1, dg1 = pressures[i], dGs[i]
            p2, dg2 = pressures[i+1], dGs[i+1]
            if dg1 == dg2:
                continue
            return p1 - dg1 * (p2 - p1) / (dg2 - dg1)
    return None

def monotonic_decreasing(values, tol=1e-6):
    for i in range(1, len(values)):
        if values[i] > values[i-1] + tol:
            return False
    return True

def all_positive(values):
    return all(v > 0 for v in values)


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


# === block: score_0 (check id='check_eos') ===
def score_0(artifact, step, ctx):
    art = artifact
    alloy = art.get("Fe_K_alloy", {})
    v0_a = alloy.get("V0")
    k0_a = alloy.get("K0")
    kp_a = alloy.get("K0_prime")
    fe = art.get("pure_Fe", {})
    v0_fe = fe.get("V0")
    k0_fe = fe.get("K0")
    kp_fe = fe.get("K0_prime")
    k = art.get("pure_K_fcc", {})
    v0_k = k.get("V0")
    k0_k = k.get("K0")
    kp_k = k.get("K0_prime")

    # Hidden reference values (PAW‑GGA‑PBE, fcc K II)
    # – only a genuine DFT re‑run produces these
    K_V0_REF = 65.0       # Å³ per atom
    K_K0_REF = 3.2        # GPa
    K_K0P_REF = 4.0

    # Paper‑reported pure Fe EOS (Table 1, "Fe, this study")
    FE_V0_REF = 10.32
    FE_K0_REF = 285
    FE_KP_REF = 4.4

    weights = []
    scores = []

    # ---------- Alloy checks (tiny weight, generous tolerance) ----------
    if v0_a is not None:
        weights.append(0.01)
        scores.append(1.0 if abs(v0_a - 10.41) <= 0.5 else 0.0)
    if k0_a is not None:
        weights.append(0.01)
        pct_err = abs(k0_a - 267) / 267 * 100
        scores.append(1.0 if pct_err <= 10.0 else 0.0)
    if kp_a is not None:
        weights.append(0.01)
        pct_err = abs(kp_a - 4.5) / 4.5 * 100
        scores.append(1.0 if pct_err <= 10.0 else 0.0)

    # ---------- Pure Fe checks (moderate weight, tight tolerances) ----------
    if v0_fe is not None:
        weights.append(0.05)
        scores.append(1.0 if abs(v0_fe - FE_V0_REF) <= 0.3 else 0.0)
    if k0_fe is not None:
        weights.append(0.05)
        pct_err = abs(k0_fe - FE_K0_REF) / FE_K0_REF * 100
        scores.append(1.0 if pct_err <= 15.0 else 0.0)
    if kp_fe is not None:
        weights.append(0.03)
        pct_err = abs(kp_fe - FE_KP_REF) / FE_KP_REF * 100
        scores.append(1.0 if pct_err <= 10.0 else 0.0)

    # ---------- Pure K‑fcc checks (high weight, tight tolerances) ----------
    if v0_k is not None:
        weights.append(0.20)
        scores.append(1.0 if abs(v0_k - K_V0_REF) <= 10.0 else 0.0)   # ±10 Å³
    if k0_k is not None:
        weights.append(0.20)
        tol = 0.3 * K_K0_REF   # 30 %
        scores.append(1.0 if abs(k0_k - K_K0_REF) <= tol else 0.0)
    if kp_k is not None:
        weights.append(0.10)
        pct_err = abs(kp_k - K_K0P_REF) / K_K0P_REF * 100
        scores.append(1.0 if pct_err <= 30.0 else 0.0)

    # ---------- Structural sanity ----------
    if v0_a is not None and v0_fe is not None:
        weights.append(0.03)
        scores.append(1.0 if v0_a > v0_fe else 0.0)
    if k0_a is not None and k0_fe is not None:
        weights.append(0.03)
        scores.append(1.0 if k0_a < k0_fe else 0.0)
    if v0_k is not None and v0_fe is not None:
        weights.append(0.05)
        scores.append(1.0 if v0_k > 5.0 * v0_fe else 0.0)

    # ---------- Volume expansion consistency ----------
    if v0_a is not None and v0_fe is not None:
        expansion = (v0_a - v0_fe) / v0_fe * 100.0
        weights.append(0.05)
        scores.append(1.0 if 0.6 <= expansion <= 1.2 else 0.0)

    # ---------- Bulk‑modulus drop ----------
    if k0_a is not None and k0_fe is not None:
        weights.append(0.05)
        scores.append(1.0 if (k0_fe - k0_a) >= 10.0 else 0.0)

    # ---------- Compose final score ----------
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    sc = sum(w * s for w, s in zip(weights, scores))
    return sc / total_weight


# === block: score_1 (check id='check_volume_diff') ===
def score_1(artifact, step, ctx):
    rows = artifact
    pressures = [float(r["pressure_GPa"]) for r in rows]
    diffs = [float(r["volume_difference_percent"]) for r in rows]
    checks = step.get("checks", {})
    total = 0.0
    sc = 0.0
    if pressures:
        idx = min(range(len(pressures)), key=lambda i: abs(pressures[i]))
        diff_at_0 = diffs[idx]
        total += 0.5
        ref = checks["zero_pressure_value"]["reference"]
        tol = checks["zero_pressure_value"]["tolerance_abs"]
        if abs(diff_at_0 - ref) <= tol:
            sc += 0.5
    total += 0.2
    if all_positive(diffs):
        sc += 0.2
    total += 0.3
    tol = checks["decreasing_trend"].get("tolerance", 0.01)
    if monotonic_decreasing(diffs, tol):
        sc += 0.3
    return sc / total if total > 0 else 0.0


# === block: score_2 (check id='check_dg_static') ===
def score_2(artifact, step, ctx):
    rows = artifact
    pressures = [float(r["pressure_GPa"]) for r in rows]
    dGs = [float(r["Delta_G_eV_per_atom"]) for r in rows]
    checks = step.get("checks", {})
    total = 0.0
    sc = 0.0
    total += 0.4
    if monotonic_decreasing(dGs, checks.get("monotonic_decreasing", {}).get("tolerance", 1e-6)):
        sc += 0.4
    total += 0.6
    p_zero = interpolate_zero_crossing(pressures, dGs)
    if p_zero is not None:
        low, high = checks["zero_crossing_pressure"]["reference_range"]
        if low <= p_zero <= high:
            sc += 0.6
    return sc / total if total > 0 else 0.0


# === block: score_3 (check id='check_dg_entropy') ===
def score_3(artifact, step, ctx):
    rows = artifact
    pressures = [float(r["pressure_GPa"]) for r in rows]
    dGs = [float(r["Delta_G_eV_per_atom"]) for r in rows]
    checks = step.get("checks", {})
    total = 0.0
    sc = 0.0
    p_zero = interpolate_zero_crossing(pressures, dGs)
    if p_zero is not None:
        total = 1.0
        low, high = checks["zero_crossing_pressure"]["reference_range"]
        if low <= p_zero <= high:
            sc = 1.0
    return sc / total if total > 0 else 0.0


_SCORERS = {
    'check_eos': score_0,
    'check_volume_diff': score_1,
    'check_dg_static': score_2,
    'check_dg_entropy': score_3,
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
