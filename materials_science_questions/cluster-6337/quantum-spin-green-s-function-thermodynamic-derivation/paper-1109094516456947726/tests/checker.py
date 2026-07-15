import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
        N = 100
        Jx = 1.0
        Jy_ratios = [-2.0, -1.0, 0.0, 1.0, 2.0]
        h_ratios = np.linspace(-3.0, 3.0, 61)

        def compute_expected(Jy_ratio, h_ratio):
            Jy = Jy_ratio * Jx
            h = h_ratio * Jx
            k = np.pi * np.arange(1, N) / N
            A = -h + (Jx + Jy) * np.cos(2*k)
            B = (Jx - Jy) * np.sin(2*k)
            omega = np.sqrt(A**2 + B**2)
            small = omega < 1e-12
            if np.any(small):
                A_safe = np.where(small, 0.0, A)
                B_safe = np.where(small, 0.0, B)
                omega_safe = np.where(small, 1e-12, omega)
                sin2_half = 0.5 * (1 - A_safe / omega_safe)
                sin_theta = -B_safe / omega_safe
            else:
                sin2_half = 0.5 * (1 - A / omega)
                sin_theta = -B / omega
            n_l = (2.0 / N) * np.sum(sin2_half)
            gamma1 = (2.0 / N) * np.sum(np.cos(k) * sin2_half)
            gamma2 = (2.0 / N) * np.sum(np.cos(2*k) * sin2_half)
            xi1 = -(1.0 / N) * np.sum(np.sin(k) * sin_theta)
            xi2 = -(1.0 / N) * np.sum(np.sin(2*k) * sin_theta)
            M = 2*n_l - 1
            E_global = 4 * n_l * (1 - n_l)
            # nearest neighbour
            z12 = gamma1
            x12 = xi1
            sigma_z12 = M**2 - 4*(gamma1**2 + xi1**2)
            sigma_z12 = max(min(sigma_z12, 1.0), -1.0)
            u12 = (1 + 2*M + sigma_z12)/4
            v12 = (1 - 2*M + sigma_z12)/4
            w12 = (1 - sigma_z12)/4
            C12 = 2 * max(0.0, abs(x12) - w12, abs(z12) - math.sqrt(max(0.0, u12*v12)))
            # next-neighbour
            z13 = gamma2 * (1 - 2*n_l) + 2 * gamma1**2
            x13 = xi2 * (1 - 2*n_l)
            sigma_z13 = M**2 - 4*(gamma2**2 + xi2**2)
            sigma_z13 = max(min(sigma_z13, 1.0), -1.0)
            u13 = (1 + 2*M + sigma_z13)/4
            v13 = (1 - 2*M + sigma_z13)/4
            w13 = (1 - sigma_z13)/4
            C13 = 2 * max(0.0, abs(x13) - w13, abs(z13) - math.sqrt(max(0.0, u13*v13)))
            # I(1,3)
            S1 = - (n_l * math.log2(n_l) + (1-n_l)*math.log2(1-n_l)) if 0 < n_l < 1 else 0.0
            sqrt_term1 = math.sqrt(max(0.0, ((u13 - v13)/2)**2 + x13**2))
            eigs = [
                (u13+v13)/2 + sqrt_term1,
                (u13+v13)/2 - sqrt_term1,
                w13 + abs(z13),
                w13 - abs(z13)
            ]
            S13 = 0.0
            for e in eigs:
                if 0 < e < 1:
                    S13 -= e * math.log2(e)
            I13 = 2*S1 - S13
            # D(1,3)
            zeta = 0.5 + math.sqrt( ((u13 - v13)/2)**2 + (abs(x13) + abs(z13))**2 )
            if zeta <= 0.0 or zeta >= 1.0:
                Q = 0.0
            else:
                Q = - (zeta * math.log2(zeta) + (1-zeta)*math.log2(1-zeta))
            D13 = Q + S1 - S13
            return {
                "magnetization": M,
                "C_12": C12,
                "C_13": C13,
                "I_13": I13,
                "D_13": D13,
                "E_global": E_global,
                "dC_dJ_y": 0.0,
                "dC_dh": 0.0
            }

        grid = {}
        for Jy_r in Jy_ratios:
            for h_r in h_ratios:
                grid[(Jy_r, h_r)] = compute_expected(Jy_r, h_r)

        dJ = 1e-4
        dh = 1e-4
        for Jy_r in Jy_ratios:
            for h_r in h_ratios:
                Jy_plus = Jy_r + dJ
                Jy_minus = Jy_r - dJ
                C_plus = compute_expected(Jy_plus, h_r)["C_13"]
                C_minus = compute_expected(Jy_minus, h_r)["C_13"]
                dC_dJy = (C_plus - C_minus) / (2 * dJ)
                h_plus = h_r + dh
                h_minus = h_r - dh
                C_plus_h = compute_expected(Jy_r, h_plus)["C_13"]
                C_minus_h = compute_expected(Jy_r, h_minus)["C_13"]
                dC_dh = (C_plus_h - C_minus_h) / (2 * dh)
                grid[(Jy_r, h_r)]["dC_dJ_y"] = dC_dJy
                grid[(Jy_r, h_r)]["dC_dh"] = dC_dh

        return {"expected": grid}


# === block: score_0 (check id='check_results') ===
def score_0(artifact, step, ctx):
        expected = ctx["expected"]
        tol_default_rtol = step.get("tolerances", {}).get("default", 1e-6)
        tol_deriv_rtol = step.get("tolerances", {}).get("derivatives", 1e-5)
        tol_c12_zero = step.get("tolerances", {}).get("C12_abs_zero", 1e-10)
        tol_deriv_zero = step.get("tolerances", {}).get("derivatives_zero_abs", 1e-10)
        atol_default = step.get("tolerances", {}).get("default_atol", 1e-9)
        atol_deriv = step.get("tolerances", {}).get("derivatives_atol", 1e-8)

        def within_tol(a, b, rtol, atol):
            return abs(a - b) <= atol + rtol * max(abs(b), 1e-12)

        total = 0
        passed = 0
        for row in artifact:
            Jy_ratio = float(row["J_y_over_J_x"])
            h_ratio = float(row["h_over_J_x"])
            key = (Jy_ratio, h_ratio)
            if key not in expected:
                continue
            exp = expected[key]
            ok = True
            # magnetization
            if not within_tol(float(row["magnetization"]), exp["magnetization"], tol_default_rtol, atol_default):
                ok = False
            # C_12 must be zero
            if abs(float(row["C_12"])) > tol_c12_zero:
                ok = False
            # C_13
            if not within_tol(float(row["C_13"]), exp["C_13"], tol_default_rtol, atol_default):
                ok = False
            # I_13
            if not within_tol(float(row["I_13"]), exp["I_13"], tol_default_rtol, atol_default):
                ok = False
            # D_13
            if not within_tol(float(row["D_13"]), exp["D_13"], tol_default_rtol, atol_default):
                ok = False
            # E_global
            if not within_tol(float(row["E_global"]), exp["E_global"], tol_default_rtol, atol_default):
                ok = False
            # derivatives
            dC_dJy = float(row["dC_dJ_y"])
            dC_dh = float(row["dC_dh"])
            if Jy_ratio == 1.0:
                if abs(dC_dJy) > tol_deriv_zero or abs(dC_dh) > tol_deriv_zero:
                    ok = False
            else:
                if not within_tol(dC_dJy, exp["dC_dJ_y"], tol_deriv_rtol, atol_deriv):
                    ok = False
                if not within_tol(dC_dh, exp["dC_dh"], tol_deriv_rtol, atol_deriv):
                    ok = False
            total += 1
            if ok:
                passed += 1
        if total == 0:
            return 0.0
        return passed / total


_SCORERS = {
    'check_results': score_0,
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
