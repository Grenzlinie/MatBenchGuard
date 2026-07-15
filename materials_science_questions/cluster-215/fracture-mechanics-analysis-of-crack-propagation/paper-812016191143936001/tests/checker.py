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


# === block: score_0 (check id='linear_energy_release_rates') ===
def score_0(artifact, step, ctx):
    import math
    E1 = 181e9; E2 = 10.3e9; G12 = 7.17e9; nu12 = 0.28
    Lx = 0.3; Ly = 0.3; B = 0.0025; a = 0.05
    Fy = 0.331e6
    a11 = 1/E1; a22 = 1/E2; a12 = -nu12/E1; a66 = 1/G12
    sqrt_a11_over_a22 = math.sqrt(a11/a22)
    psi = math.sqrt(math.sqrt(a22/a11) + (2*a12 + a66)/(2*a11)) * math.sqrt(a11*a22/2)

    def _compute_expected(beta_deg, k):
        beta = math.radians(beta_deg)
        c = math.cos(beta); s = math.sin(beta)
        c2 = c*c; s2 = s*s
        Fx = k * Fy
        prefactor_Gx = (math.pi * a * psi) / (4 * B*B * Ly*Ly)
        prefactor_Gy = (math.pi * a * psi) / (4 * B*B * Lx*Lx)
        prefactor_Gxy = (math.pi * a * psi) / (2 * B*B * Lx * Ly)
        G_x = prefactor_Gx * (Fx**2) * c2 * (c2 + sqrt_a11_over_a22 * s2) / 1e6
        G_y = prefactor_Gy * (Fy**2) * s2 * (s2 + sqrt_a11_over_a22 * c2) / 1e6
        G_xy = prefactor_Gxy * (Fx * Fy) * s2 * c2 * (1 - sqrt_a11_over_a22) / 1e6
        G_total = G_x + G_y + G_xy
        return G_x, G_y, G_xy, G_total

    lookup = {}
    for row in artifact:
        try:
            b = float(row["beta"])
            kk = float(row["k"])
            lookup[(b, kk)] = row
        except:
            pass

    tol_rel = step.get("tolerance_relative", 1e-6)
    tol_abs = step.get("tolerance_absolute", 1e-10)
    expected_conds = step["expected_conditions"]
    correct = 0
    total = 0
    columns = ["G_x", "G_y", "G_xy", "G_total"]
    for cond in expected_conds:
        exp_beta = cond["beta"]
        exp_k = cond["k"]
        exp_vals = _compute_expected(exp_beta, exp_k)
        row = lookup.get((exp_beta, exp_k))
        if row is None:
            total += 4
            continue
        for col, exp_val in zip(columns, exp_vals):
            got_str = row.get(col)
            if got_str is None:
                total += 1
                continue
            try:
                got_val = float(got_str)
            except ValueError:
                total += 1
                continue
            diff = abs(got_val - exp_val)
            if diff <= tol_abs or (exp_val != 0.0 and diff <= tol_rel * abs(exp_val)):
                correct += 1
            total += 1
    if total == 0:
        score = 0.0
    else:
        score = correct / total
    return score


_SCORERS = {
    'linear_energy_release_rates': score_0,
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
