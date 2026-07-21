import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math

def compute_DAH_gold(lam_values):
    # Material constants (Table 1)
    C_m = {'C11': 8.0, 'C12': 4.4, 'C13': 4.4, 'C33': 8.0, 'C44': 1.8, 'C66': 1.8,
           'e31': 0.0, 'e33': 0.0, 'e15': 0.0, 'eps11': 3.72e-2, 'eps33': 3.72e-2}
    C_f = {'C11': 154.837, 'C12': 83.237, 'C13': 82.712, 'C33': 131.39, 'C44': 25.696, 'C66': 35.8,
           'e31': -2.120582, 'e33': 9.52183, 'e15': 9.34959, 'eps11': 4.065, 'eps33': 2.079}
    lam_f = 0.5
    # plane-strain bulk moduli
    k_m = (C_m['C11'] + C_m['C12']) / 2.0
    k_f = (C_f['C11'] + C_f['C12']) / 2.0
    C1212_m = C_m['C66']
    C1212_f = C_f['C66']
    kappa_m = 1 + 2*C1212_m / k_m
    kappa_f = 1 + 2*C1212_f / k_f
    chi = C1212_f / C1212_m
    # Parameter K
    R = math.sqrt(lam_f / math.pi)
    S4 = 3.151212
    S8 = 4.255731
    T7 = 4.5155155
    C = 1.0 / (1 + (lam_f * k_m + (1 - lam_f) * k_f) / C1212_m)
    B = (1 - chi) / (1 + kappa_m * chi)
    A = (kappa_m * chi - kappa_f) * B / (kappa_f + chi)
    D = 2 * C * (k_f / k_m - 1)
    c73 = math.comb(7, 3)
    c75 = math.comb(7, 5)
    phi = c73 * c75 * (R**10) * (S8**2)
    c84 = math.comb(8, 4)
    c63 = math.comb(6, 3)
    psi = -3 * (R**2 * c84 * S8 - c63 * T7)
    denom = 1.0/B + R**6 * (A * (1.0/B) * phi + psi + 3 * D * R**2 * (S4**2))
    K_val = C * (1 - lam_f + (3 * (1 + kappa_m) * C * (R**8) * (S4**2)) / denom)
    # Effective properties of fibrous layer L0
    C3333_avg = (1 - lam_f) * C_m['C33'] + lam_f * C_f['C33']
    C1133_avg = (1 - lam_f) * C_m['C13'] + lam_f * C_f['C13']
    e311_avg = (1 - lam_f) * C_m['e31'] + lam_f * C_f['e31']
    e333_avg = (1 - lam_f) * C_m['e33'] + lam_f * C_f['e33']
    eps33_avg = (1 - lam_f) * C_m['eps33'] + lam_f * C_f['eps33']
    delta_C1133 = C_m['C13'] - C_f['C13']
    C3333_L0 = C3333_avg - lam_f * (delta_C1133**2) * K_val / C1212_m
    C1133_L0 = C1133_avg + (k_m - k_f) * (C3333_L0 - C3333_avg) / delta_C1133
    e311_L0 = (e311_avg + (k_m - k_f) * (C_m['e31'] - C_f['e31']) * (C3333_L0 - C3333_avg) / (delta_C1133**2))
    e333_L0 = (e333_avg + (C_m['e31'] - C_f['e31']) * (C3333_L0 - C1133_avg) / delta_C1133)
    eps33_L0 = (eps33_avg - ((C_m['e31'] - C_f['e31'])**2) * (C3333_L0 - C3333_avg) / (delta_C1133**2))
    # Pure PZT layer L1 (same as fibers)
    C3333_L1 = C_f['C33']
    e333_L1 = C_f['e33']
    eps33_L1 = C_f['eps33']
    C1133_L1 = C_f['C13']
    e311_L1 = C_f['e31']
    # Overall laminate
    gold = {}
    for lam in lam_values:
        # M matrices
        M_L0 = np.array([[C3333_L0, e333_L0], [e333_L0, -eps33_L0]])
        M_L1 = np.array([[C3333_L1, e333_L1], [e333_L1, -eps33_L1]])
        inv_M_L0 = np.linalg.inv(M_L0)
        inv_M_L1 = np.linalg.inv(M_L1)
        avg_inv_M = (1 - lam) * inv_M_L0 + lam * inv_M_L1
        inv_avg_inv_M = np.linalg.inv(avg_inv_M)
        # e31
        vec_L0 = inv_M_L0 @ np.array([C1133_L0, e311_L0])
        vec_L1 = inv_M_L1 @ np.array([C1133_L1, e311_L1])
        avg_vec = (1 - lam) * vec_L0 + lam * vec_L1
        e31_lam = (inv_avg_inv_M @ avg_vec)[1]
        # e33
        e33_lam = inv_avg_inv_M[1, 0]
        gold[lam] = (e31_lam, e33_lam)
    return gold


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
    lam_values = [0.0, 0.25, 0.5, 0.75]
    gold_dah = compute_DAH_gold(lam_values)
    return {"gold_dah": gold_dah, "lam_values": lam_values}


# === block: score_0 (check id='final_csv') ===
def score_0(artifact, step, ctx):
    import csv, os, math

    gold_dah = ctx["gold_dah"]
    lam_values = ctx["lam_values"]

    #  Paper-reported FFT coefficients (extracted from Fig. 2, units C/m^2)
    fft_ref = {
        0.0:  {"e31": -0.12,  "e33": 4.2},
        0.25: {"e31": -0.55,  "e33": 5.3},
        0.5:  {"e31": -1.0,   "e33": 6.4},
        0.75: {"e31": -1.5,   "e33": 7.5},
    }

    rows = {}
    with open("/app/outputs/piezoelectric_coefficients.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lam = float(row["λ"])
            except (ValueError, TypeError):
                continue
            rows[lam] = {
                "e31_DAH": float(row["e31_DAH"]),
                "e33_DAH": float(row["e33_DAH"]),
                "e31_FFT": float(row["e31_FFT"]),
                "e33_FFT": float(row["e33_FFT"]),
            }

    # ----- DAH accuracy score (recompute from formulas) -----
    dah_score = 0.0
    n_dah = 0
    for lam in lam_values:
        if lam not in rows:
            continue
        gold_e31, gold_e33 = gold_dah[lam]
        for rep, gold, name in [(rows[lam]["e31_DAH"], gold_e31, "e31"),
                                (rows[lam]["e33_DAH"], gold_e33, "e33")]:
            if abs(gold) < 1e-12:
                err = abs(rep - gold)
                step_score = 1.0 if err < 1e-10 else max(0.0, 1.0 - err / 1e-8)
            else:
                rel_err = abs((rep - gold) / gold)
                step_score = 1.0 if rel_err <= 0.001 else max(0.0, 1.0 - (rel_err - 0.001) / 0.099)
            dah_score += step_score
            n_dah += 1
    if n_dah > 0:
        dah_score /= n_dah

    # ----- FFT accuracy score (compare to paper reference, 10% tolerance) -----
    fft_score = 0.0
    n_fft = 0
    for lam in lam_values:
        if lam not in rows or lam not in fft_ref:
            continue
        for key, gold in [("e31_FFT", fft_ref[lam]["e31"]),
                          ("e33_FFT", fft_ref[lam]["e33"])]:
            rep = rows[lam][key]
            if abs(gold) < 1e-12:
                err = abs(rep - gold)
                step_score = 1.0 if err < 1e-10 else max(0.0, 1.0 - err / 1e-8)
            else:
                rel_err = abs((rep - gold) / gold)
                # full credit if rel_err <= 0.10 (10%), linear decay to zero at 0.30
                step_score = 1.0 if rel_err <= 0.10 else max(0.0, 1.0 - (rel_err - 0.10) / 0.20)
            fft_score += step_score
            n_fft += 1
    if n_fft > 0:
        fft_score /= n_fft

    # ----- Trend score: DAH overestimates FFT -----
    # e31 is negative → DAH more negative → e31_DAH < e31_FFT
    # e33 is positive → DAH larger positive → e33_DAH > e33_FFT
    trend_ok = True
    for lam in lam_values:
        if lam not in rows:
            trend_ok = False
            break
        if not (rows[lam]["e31_DAH"] < rows[lam]["e31_FFT"]):   # more negative means smaller
            trend_ok = False
            break
        if not (rows[lam]["e33_DAH"] > rows[lam]["e33_FFT"]):
            trend_ok = False
            break
    trend_score = 1.0 if trend_ok else 0.0

    # Combined score
    return 0.4 * dah_score + 0.4 * fft_score + 0.2 * trend_score


_SCORERS = {
    'final_csv': score_0,
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
