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
    z = 1
    n_i = 6.2e14
    ctx = {}
    ctx['E0_expected'] = 2e-7 * z * math.sqrt(n_i)
    t = 3
    G_half = math.gamma(0.5)
    G_onehalf = math.gamma(1.5)
    G_4 = 6.0
    D_gam = G_half * G_4 / (G_onehalf * G_onehalf) * (1.0 / t)
    gamma_num = math.gamma((3 + t) / (2 * t))
    gamma_den = math.gamma((3 + 2 * t) / (2 * t))
    J_factor = (1.0 / D_gam) * gamma_num / gamma_den * t**(-0.5)
    H_over_H0 = 1.0
    rows = []
    for i in range(1, 100):
        Ex_ratio = i / 100.0
        factor = 1.0 / math.sqrt(1.0 - Ex_ratio**2)
        tan_theta = Ex_ratio * factor
        rho_ratio = D_gam * H_over_H0 * Ex_ratio * factor
        j_ratio = J_factor * factor
        rows.append((Ex_ratio, tan_theta, rho_ratio, j_ratio))
    ctx['csv_rows'] = rows
    c0 = 0.5
    r = 1
    sigma_ratio = 1.0
    G_1_3 = math.gamma(1.0/3.0)
    G_half = math.gamma(0.5)
    G_1half = math.gamma(1.5)
    bracket = sigma_ratio * G_1_3 / G_half * (c0 / (1 - c0))
    Phi2 = bracket**(1.0/(2*r)) * (G_1half / math.gamma(1.0))
    Ex_cr = Phi2 * H_over_H0 / math.sqrt(1 + (Phi2 * H_over_H0)**2)
    ctx['Ex_cr_expected'] = Ex_cr
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    val_str = artifact.strip()
    if not val_str:
        return 0.0
    try:
        val = float(val_str)
    except:
        return 0.0
    expected = ctx['E0_expected']
    if abs(val - expected) <= 1e-8:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    expected_rows = ctx['csv_rows']
    if len(artifact) != len(expected_rows):
        return 0.0
    cols = ['Ex_ratio', 'tan_theta', 'rho_ratio', 'j_ratio']
    for row, exp_tup in zip(artifact, expected_rows):
        try:
            for i, col in enumerate(cols):
                val = float(row[col])
                exp = exp_tup[i]
                if abs(val - exp) > 1e-5:
                    return 0.0
        except:
            return 0.0
    return 1.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    val_str = artifact.strip()
    if not val_str:
        return 0.0
    try:
        val = float(val_str)
    except:
        return 0.0
    expected = ctx['Ex_cr_expected']
    if abs(val - expected) <= 1e-8:
        return 1.0
    return 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
