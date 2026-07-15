import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    def compute_reference():
        # Temperatures
        tC = np.arange(0, 101, 5)
        TK = tC + 273.15
        theta = 298.15
        K1 = 1.0 / TK
        ln_T_theta = np.log(TK / theta)
        K2 = theta / TK + ln_T_theta - 1.0
        K3 = TK/2 - theta**2/(2*TK) - theta * ln_T_theta
        K4 = TK**2/6 + theta**2*(0.5 - ln_T_theta) - 2*theta**3/(3*TK)
        params = {
            'A': (-20.0, -1000.0, -15.0, 4.0, -0.0055),
            'B': (-20.0, 0.0, -15.0, 0.6, -0.0008)
        }
        # exact RlnK
        RlnK_exact = {}
        for set_label, (DS, DH, DCp, Db, Dc) in params.items():
            RlnK_exact[set_label] = DS - DH*K1 + DCp*K2 + Db*K3 + Dc*K4
        # add noise seed 42
        rng = np.random.default_rng(42)
        RlnK_noisy = {}
        for set_label in ('A','B'):
            exact = RlnK_exact[set_label]
            sigma = np.abs(exact) / 1500.0
            noise = rng.normal(0, sigma, size=exact.shape)
            RlnK_noisy[set_label] = exact + noise
        # method of intervals (20°C intervals: 0-20, 20-40, ..., 80-100)
        idx = [0, 4, 8, 12, 16, 20]   # indices for 0,20,40,60,80,100 °C
        result = {}
        for set_label in ('A','B'):
            R = RlnK_noisy[set_label]
            Z, x_vals, y_vals = [], [], []
            for i in range(len(idx)-2):
                i0, i1, i2 = idx[i], idx[i+1], idx[i+2]
                # interval (T0,T1)
                dR1 = R[i1] - R[i0]
                dK1_1 = K1[i1] - K1[i0]
                dK2_1 = K2[i1] - K2[i0]
                dK3_1 = K3[i1] - K3[i0]
                dK4_1 = K4[i1] - K4[i0]
                # interval (T1,T2)
                dR2 = R[i2] - R[i1]
                dK1_2 = K1[i2] - K1[i1]
                dK2_2 = K2[i2] - K2[i1]
                dK3_2 = K3[i2] - K3[i1]
                dK4_2 = K4[i2] - K4[i1]
                quot1 = dR1 / dK1_1
                quot2 = dR2 / dK1_2
                dquot = quot2 - quot1
                delta_r2 = (dK2_2/dK1_2) - (dK2_1/dK1_1)
                delta_r3 = (dK3_2/dK1_2) - (dK3_1/dK1_1)
                delta_r4 = (dK4_2/dK1_2) - (dK4_1/dK1_1)
                Z.append(dquot / delta_r2)
                x_vals.append(delta_r3 / delta_r2)
                y_vals.append(delta_r4 / delta_r2)
            Z = np.array(Z)
            X = np.column_stack([np.ones_like(Z), x_vals, y_vals])
            coeffs, _, _, _ = np.linalg.lstsq(X, Z, rcond=None)
            DCp = coeffs[0]
            Db  = coeffs[1]
            Dc  = coeffs[2]
            R_prime = R - (DCp*K2 + Db*K3 + Dc*K4)
            A_mat = np.column_stack([np.ones_like(K1), K1])
            sol, _, _, _ = np.linalg.lstsq(A_mat, R_prime, rcond=None)
            DS = sol[0]
            DH = -sol[1]
            result[set_label] = (DS, DH, DCp, Db, Dc)
        return result

    ref = compute_reference()
    ctx = {}
    for set_label in ('A','B'):
        DS, DH, DCp, Db, Dc = ref[set_label]
        ctx[f"ref_{set_label}_DeltaS"] = DS
        ctx[f"ref_{set_label}_DeltaH"] = DH
        ctx[f"ref_{set_label}_DeltaCp"] = DCp
        ctx[f"ref_{set_label}_Delta_b"] = Db
        ctx[f"ref_{set_label}_Delta_c"] = Dc
    return ctx


# === block: score_0 (check id='recover_params') ===
def score_0(artifact, step, ctx):
    tolerances = step.get("tolerances", {})
    tol_map = {
        "DeltaS": tolerances.get("DeltaS", 0.001),
        "DeltaH": tolerances.get("DeltaH", 0.001),
        "DeltaCp": tolerances.get("DeltaCp", 0.001),
        "Delta_b": tolerances.get("Delta_b", 0.005),
        "Delta_c": tolerances.get("Delta_c", 0.005)
    }
    fields = ["DeltaS", "DeltaH", "DeltaCp", "Delta_b", "Delta_c"]
    correct = 0
    for row in artifact:
        set_label = row.get("set", "")
        if set_label not in ("A","B"):
            continue
        for f in fields:
            try:
                submitted = float(row.get(f, 0))
            except (ValueError, TypeError):
                submitted = 0.0
            ref_val = ctx.get(f"ref_{set_label}_{f}", 0.0)
            rtol = tol_map[f]
            atol = rtol * abs(ref_val) if abs(ref_val) > 1e-12 else rtol
            if abs(submitted - ref_val) <= atol:
                correct += 1
    total = 2 * 5
    score = correct / total if total > 0 else 0.0
    return score


_SCORERS = {
    'recover_params': score_0,
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
