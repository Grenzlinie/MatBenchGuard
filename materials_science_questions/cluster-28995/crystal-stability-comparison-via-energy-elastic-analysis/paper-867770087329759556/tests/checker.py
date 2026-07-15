import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np


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
    params = {
        "A": 2.10e-15,
        "a1": -0.5819,
        "a2": 0.09309,
        "mu1": 3.000,
        "mu2": -0.03996,
        "g": 80.0,
        "nu": 3.60
    }
    neighbor_indices = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for k in range(-2, 3):
                if i == 0 and j == 0 and k == 0:
                    continue
                if (i + j + k) % 2 != 0:
                    continue
                rsq = i*i + j*j + k*k
                if rsq <= 3:
                    neighbor_indices.append((i, j, k))
    return {"params": params, "neighbor_indices": neighbor_indices}


# === block: score_0 (check id='step_01_csv') ===
def score_0(artifact, step, ctx):
    def VR(R, A, a1, a2, mu1, mu2):
        return A * (1 + a1*R + a2*R**2) * math.exp(-mu1*R - mu2*R**2)

    def dVR_dR(R, A, a1, a2, mu1, mu2):
        term = 1 + a1*R + a2*R**2
        dterm = a1 + 2*a2*R
        exp_f = math.exp(-mu1*R - mu2*R**2)
        dexp = -(mu1 + 2*mu2*R) * exp_f
        return A * (dterm*exp_f + term*dexp)

    def d2VR_dR2(R, A, a1, a2, mu1, mu2):
        term = 1 + a1*R + a2*R**2
        dterm = a1 + 2*a2*R
        d2term = 2*a2
        exp_f = math.exp(-mu1*R - mu2*R**2)
        dexp = -(mu1 + 2*mu2*R) * exp_f
        d2exp = (-2*mu2 + (mu1 + 2*mu2*R)**2) * exp_f
        return A * (d2term*exp_f + 2*dterm*dexp + term*d2exp)

    def rho(R, g, nu):
        return g * math.exp(-nu * R)

    def drho_dR(R, g, nu):
        return -nu * rho(R, g, nu)

    def d2rho_dR2(R, g, nu):
        return nu**2 * rho(R, g, nu)

    params = ctx["params"]
    A = params["A"]
    a1 = params["a1"]
    a2 = params["a2"]
    mu1 = params["mu1"]
    mu2 = params["mu2"]
    g = params["g"]
    nu = params["nu"]

    # Build correct fcc neighbor positions within 6 shells (r^2 <= 3 a^2).
    # fcc basis offsets in units of a.
    basis = [(0,0,0), (0,1,1), (1,0,1), (1,1,0)]
    neighbor_positions = []  # (dx, dy, dz) in units of a
    max_n = 3  # sufficient to cover radius sqrt(3)
    for i in range(-max_n, max_n+1):
        for j in range(-max_n, max_n+1):
            for k in range(-max_n, max_n+1):
                for (ox, oy, oz) in basis:
                    dx = i + ox/2.0
                    dy = j + oy/2.0
                    dz = k + oz/2.0
                    rsq = dx*dx + dy*dy + dz*dz
                    if 0 < rsq <= 3.0:
                        neighbor_positions.append((dx, dy, dz))

    if not artifact:
        return 0.0

    total_passes = 0
    total_count = len(artifact) * 6

    for row in artifact:
        try:
            a_val = float(row["lattice_constant_A"])
        except (KeyError, ValueError):
            continue

        # compute lambda using correct neighbor distances
        lam = 0.0
        for (dx, dy, dz) in neighbor_positions:
            R = a_val * math.sqrt(dx*dx + dy*dy + dz*dz)
            lam += rho(R, g, nu)

        factor = math.exp(-2 * lam)
        omega = a_val**3 / 4.0

        u = 0.0
        v = 0.0
        w = 0.0
        us = 0.0
        vs = 0.0
        ws = 0.0
        alpha0 = 0.0
        alpha0_s = 0.0
        beta0 = 0.0
        beta0_s = 0.0

        for (dx, dy, dz) in neighbor_positions:
            R = a_val * math.sqrt(dx*dx + dy*dy + dz*dz)
            x = a_val * dx
            y = a_val * dy
            z = a_val * dz
            s_weight = (x**4 + y**4 + z**4) / (R**4)

            vr = VR(R, A, a1, a2, mu1, mu2)
            dVR = dVR_dR(R, A, a1, a2, mu1, mu2)
            d2VR = d2VR_dR2(R, A, a1, a2, mu1, mu2)

            u += vr
            v += R * dVR
            w += R**2 * d2VR
            us += vr * s_weight
            vs += R * dVR * s_weight
            ws += R**2 * d2VR * s_weight

            alpha0 += R * drho_dR(R, g, nu)
            alpha0_s += R * drho_dR(R, g, nu) * s_weight
            beta0 += R**2 * d2rho_dR2(R, g, nu)
            beta0_s += R**2 * d2rho_dR2(R, g, nu) * s_weight

        inv_2omega = 1.0 / (2 * omega)
        u *= factor * inv_2omega
        v *= factor * inv_2omega
        w *= factor * inv_2omega
        us *= factor * inv_2omega
        vs *= factor * inv_2omega
        ws *= factor * inv_2omega

        # convert to GPa: 1 J/Å^3 = 1e21 GPa
        conv = 1e21

        P = (1.0/3.0) * (-v + 2*u*alpha0) * conv
        delta = (4.0/9.0) * (-alpha0*v + u*alpha0**2) * conv
        Ps = (1.0/3.0) * (-vs + 2*u*alpha0_s) * conv
        K = (1.0/3.0) * (w - 2*u*beta0) * conv
        Ks = (1.0/3.0) * (ws - 2*u*beta0_s) * conv

        B = (2.0/3.0)*P + (1.0/3.0)*K + delta
        C11 = -P + Ps + Ks + delta
        C12 = 0.5*(3*P + K - Ps - Ks) + delta
        C44 = 0.5*(-P + K - Ps - Ks)

        # evaluate each property
        props = {
            "pressure_GPa": P,
            "delta_GPa": delta,
            "B_GPa": B,
            "C11_GPa": C11,
            "C12_GPa": C12,
            "C44_GPa": C44
        }

        for col, expected in props.items():
            try:
                agent_val = float(row.get(col, 0.0))
            except (ValueError, TypeError):
                continue
            if col == "delta_GPa":
                tol = 0.1
            else:
                if abs(expected) > 1.0:
                    tol = 0.02 * abs(expected)
                else:
                    tol = 0.5
            if abs(agent_val - expected) <= tol:
                total_passes += 1

    score = total_passes / total_count if total_count > 0 else 0.0
    return score


_SCORERS = {
    'step_01_csv': score_0,
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
