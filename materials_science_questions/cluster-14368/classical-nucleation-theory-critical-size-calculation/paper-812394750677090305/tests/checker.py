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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # Load thermodynamic properties from the same CSV that the agent uses.
    csv_path = "/app/assets/h2so4_properties.csv"
    if not os.path.exists(csv_path):
        csv_path = "h2so4_properties.csv"  # fallback
    X_vals = []
    rho_vals = []
    drho_dx_scaled = []
    sigma_vals = []
    dsigma_dx_scaled = []
    a_w_vals = []
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for row in reader:
            X_vals.append(float(row[0]))
            rho_vals.append(float(row[1]))
            drho_dx_scaled.append(float(row[2]))   # ×10³
            sigma_vals.append(float(row[3]))
            dsigma_dx_scaled.append(float(row[4]))  # ×10²
            a_w_vals.append(float(row[5]))

    # Constants (same as provided in instruction)
    M_w = 18.015          # g/mol
    R_gas = 8.314         # used as given
    T_K = 298.15          # K
    rho_pure = 1.84       # g/cm³, pure H₂SO₄

    dry_radii = [0.001, 0.005, 0.05, 0.1, 0.5]
    rh_list = [0, 10, 30, 50, 70, 80, 90, 100, 101, 110]

    def interp(x, xs, ys):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
        return ys[-1]

    def compute_expected(r0_um, rh_pct):
        if rh_pct == 0:
            return r0_um
        Sw = rh_pct / 100.0
        r0_cm = r0_um * 1e-4
        V0_cm3 = (4/3)*math.pi * r0_cm**3
        m_acid = V0_cm3 * rho_pure

        best_X = None
        min_abs = float('inf')
        # scan mass fraction X from 0.5 to 85 % with step 0.1
        X_candidates = [x/10.0 for x in range(5, 851)]
        for X in X_candidates:
            if X < X_vals[0] or X > X_vals[-1]:
                continue
            aw = interp(X, X_vals, a_w_vals)
            if aw <= 0 or Sw <= 0:
                continue
            lhs = math.log(Sw/aw)
            rho = interp(X, X_vals, rho_vals)
            sigma = interp(X, X_vals, sigma_vals)
            drho_dx = interp(X, X_vals, drho_dx_scaled) / 1000.0
            dsigma_dx = interp(X, X_vals, dsigma_dx_scaled) / 100.0

            total_mass = m_acid * (100.0 / X)
            V_cm3 = total_mass / rho
            r_cm = (3*V_cm3/(4*math.pi))**(1/3)

            corr = 1.0 + (X/rho)*drho_dx - 1.5*(X/sigma)*dsigma_dx
            rhs = (2*M_w*sigma)/(R_gas*T_K*rho) * (1.0/r_cm) * corr
            val = lhs - rhs
            if abs(val) < min_abs:
                min_abs = abs(val)
                best_X = X
            if abs(val) < 1e-12:
                break

        if best_X is None:
            return r0_um
        X_eq = best_X
        rho_eq = interp(X_eq, X_vals, rho_vals)
        total_mass = m_acid * (100.0 / X_eq)
        V_eq = total_mass / rho_eq
        r_eq_cm = (3*V_eq/(4*math.pi))**(1/3)
        return r_eq_cm * 1e4   # cm -> µm

    if not artifact:
        return 0.0
    agent_data = {}
    for row in artifact:
        try:
            dry = float(row['dry_radius_um'])
            rh = float(row['rh_pct'])
            eq = float(row['eq_radius_um'])
            agent_data[(dry, rh)] = eq
        except (KeyError, ValueError, TypeError):
            continue

    ok = 0
    for r in dry_radii:
        for rh in rh_list:
            expected = compute_expected(r, rh)
            agent_r = agent_data.get((r, float(rh)))
            if agent_r is not None:
                denom = max(expected, 1e-12)
                if abs(agent_r - expected) / denom <= 0.05:
                    ok += 1
    score = ok / 50
    return score


_SCORERS = {
    'step_01': score_0,
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