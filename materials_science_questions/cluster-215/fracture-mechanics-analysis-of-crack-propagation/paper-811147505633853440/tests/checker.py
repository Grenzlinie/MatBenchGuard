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


# === block: score_0 (check id='numeric') ===
def score_0(artifact, step, ctx):
        rows = artifact
        tolerance_rel = step.get("tolerance_rel", 1e-3)
        tolerance_abs = step.get("tolerance_abs", 1e-9)
        columns = step["columns_to_check"]

        def recompute(row):
            V_f = float(row["V_f"])
            rho = float(row["rho"])
            Phi = float(row["Phi"])
            lam = float(row["lambda"])
            h2_over_H = float(row["h2_over_H"])
            delta = float(row["delta"])
            L = float(row["L"])
            B = float(row["B"])
            H = float(row["H"])
            sigma_b = float(row["sigma_b"])
            tau_s = float(row["tau_s"])
            gamma = float(row["gamma"])

            h2 = h2_over_H * H

            # E_ratio (Eq. 3)
            numer = (1.0 - Phi) * Phi * rho**2 * V_f**2
            denom = (1.0 - V_f) * lam + (1.0 - Phi) * Phi * rho**2 * V_f
            E_ratio = numer / denom if denom != 0 else 0.0

            # I_z (Eq. 6a)
            Iz = B * H / 12.0 * ((H - h2) * (H - 2.0*h2) * V_f + (3.0*H - 2.0*h2) * h2)

            # S_zmax (Eq. 6b)
            if V_f > 0:
                Sz_max = B / 8.0 * (4.0*H*h2 - 4.0*h2**2 + (H - h2)**2 * V_f - (2.0/V_f)*(H - h2)*h2)
            else:
                Sz_max = 0.0

            # I_z0
            I_z0 = B * H**3 / 12.0

            # kappa (Eq. 7)
            kappa = (E_ratio * Iz) / I_z0 if I_z0 != 0 else 0.0

            # P1 (Eq. 12)
            P1 = (8.0 * Iz * sigma_b) / (H * L) if H*L != 0 else 0.0

            # P2 (Eq. 14)
            P2 = (2.0 * Iz * tau_s * B) / Sz_max if Sz_max != 0 else 0.0

            # P0 and chi (Eq. 15)
            P0 = (8.0 * I_z0 * sigma_b) / (H * L) if H*L != 0 else 0.0
            P_min = min(P1, P2)
            chi = P_min / P0 if P0 != 0 else 0.0

            # L_c (Eq. 19)
            L_c = 0.0
            if delta != 0.0 and tau_s != 0.0 and B != 0.0 and H != 0.0 and L != 0.0:
                disc = (16.0 * Sz_max**2 * sigma_b**2) / (H**2 * L**2 * B**2 * tau_s**2) - 1.0
                if disc >= 0.0:
                    L_c = L - (L**2 / (4.0 * delta)) * math.sqrt(disc)
                # else L_c remains 0.0

            # W_PASB (Eq. 20)
            W_PASB = gamma * H * B

            # W_MSCB (Eq. 23)  requires h1, l = rho * h1, m = L_c / l
            if V_f > 0.0 and V_f < 1.0:
                h1 = V_f * h2 / (1.0 - V_f)
            else:
                h1 = 0.0
            l = rho * h1
            if l > 0.0:
                m = L_c / l
            else:
                m = 0.0
            W_MSCB = (m / 6.0) * Phi * rho * V_f * gamma * H * B

            return {
                "E_ratio": E_ratio,
                "I_z": Iz,
                "S_zmax": Sz_max,
                "kappa": kappa,
                "P1": P1,
                "P2": P2,
                "chi": chi,
                "L_c": L_c,
                "W_PASB": W_PASB,
                "W_MSCB": W_MSCB
            }

        match = 0
        total = 0
        for row in rows:
            try:
                ref = recompute(row)
                ok = True
                for col in columns:
                    agent_val = float(row.get(col, 0.0))
                    ref_val = ref[col]
                    if ref_val == 0.0:
                        if abs(agent_val - ref_val) > tolerance_abs:
                            ok = False
                            break
                    else:
                        if abs(agent_val - ref_val) > tolerance_rel * abs(ref_val) + tolerance_abs:
                            ok = False
                            break
                if ok:
                    match += 1
                total += 1
            except Exception:
                total += 1
        if total == 0:
            return 0.0
        return match / total


# === block: score_1 (check id='trends') ===
def score_1(artifact, step, ctx):
        rows = artifact
        all_input_params = ["V_f", "rho", "Phi", "lambda", "h2_over_H",
                            "delta", "L", "B", "H", "sigma_b", "tau_s", "gamma"]
        columns_to_check = step["columns_to_check"]

        def is_increasing(vals):
            for i in range(1, len(vals)):
                if vals[i] < vals[i-1] - 1e-12:
                    return False
            return True

        allowed_params = {"V_f", "rho"}

        total_checks = 0
        passed_checks = 0

        for col_name, params in columns_to_check.items():
            for param in params:
                if param not in allowed_params:
                    continue
                other_params = [p for p in all_input_params if p != param]
                groups = {}
                for row in rows:
                    key = tuple(row.get(p) for p in other_params)
                    try:
                        val_param = float(row[param])
                        val_col = float(row[col_name])
                    except Exception:
                        continue
                    groups.setdefault(key, []).append((val_param, val_col))
                for key, group in groups.items():
                    group.sort(key=lambda x: x[0])
                    vals = [v for _, v in group]
                    if len(vals) >= 2:
                        total_checks += 1
                        if is_increasing(vals):
                            passed_checks += 1

        if total_checks == 0:
            return 1.0
        return passed_checks / total_checks


_SCORERS = {
    'numeric': score_0,
    'trends': score_1,
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
