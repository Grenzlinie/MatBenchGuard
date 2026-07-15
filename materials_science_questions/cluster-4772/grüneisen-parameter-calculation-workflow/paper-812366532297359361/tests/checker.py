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


# === block: score_0 (check id='step_04_moments') ===
def score_0(artifact, step, ctx):
    data = artifact
    targets = step['targets']
    tols = step.get('tolerances', {})

    def score_rel(value, target, rel_tol):
        if target == 0:
            return 1.0 if abs(value) < 1e-12 else 0.0
        re = abs((value - target) / target)
        if re <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (re - rel_tol) / (3 * rel_tol))

    def score_abs(value, target, abs_tol):
        d = abs(value - target)
        if d <= abs_tol:
            return 1.0
        return max(0.0, 1.0 - (d - abs_tol) / (2 * abs_tol))

    h = 6.62607015e-34
    k = 1.380649e-23
    theta = data.get('theta_inf')
    mu2 = data.get('mu2')

    s_theta = score_abs(theta, targets['theta_inf'], tols['theta_abs'])
    s_mu2 = score_rel(data.get('mu2', 0), targets['mu2'], tols['mu_rel'])
    s_mu4 = score_rel(data.get('mu4', 0), targets['mu4'], tols['mu_rel'])
    s_mu6 = score_rel(data.get('mu6', 0), targets['mu6'], tols['mu_rel'])

    # consistency: recompute mu2 from theta_inf
    if theta is not None:
        mu2_calc = (3.0/5.0) * (k * theta / h) ** 2
        # check against reported mu2 with tighter tolerance 0.01
        s_consist = score_rel(mu2, mu2_calc, 0.01) if mu2 is not None else 0.0
    else:
        s_consist = 0.0

    w = step.get('consistency_weight', 0.2)
    total = w * s_consist + (1.0 - w) * (s_mu2 + s_mu4 + s_mu6 + s_theta) / 4.0
    return total


# === block: score_1 (check id='step_06_anharmonic') ===
def score_1(artifact, step, ctx):
    data = artifact
    targets = step['targets']
    tols = step.get('tolerances', {})
    def score_abs(value, target, abs_tol):
        d = abs(value - target)
        if d <= abs_tol:
            return 1.0
        return max(0.0, 1.0 - (d - abs_tol) / (2 * abs_tol))

    s_b1 = score_abs(data.get('b1', 0), targets['b1'], tols['b1_abs'])
    s_b2 = score_abs(data.get('b2', 0), targets['b2'], tols['b2_abs'])
    return (s_b1 + s_b2) / 2.0


# === block: score_2 (check id='step_07_gruneisen') ===
def score_2(artifact, step, ctx):
    rows = artifact  # list of dicts from CSV
    ref_rows = step['targets']['rows']
    tol_rel = step['tolerances']['rel_tol']
    tol_abs = step['tolerances']['abs_tol']

    # build lookup
    ref_dict = {row['T']: row for row in ref_rows}

    def score_gamma(val, gold):
        if gold == 0:
            return 1.0 if abs(val) < 1e-12 else 0.0
        re = abs((val - gold) / gold)
        if re <= tol_rel:
            return 1.0
        # fallback absolute check
        if abs(val - gold) <= tol_abs:
            return 1.0
        # partial
        return max(0.0, 1.0 - (re - tol_rel) / (2 * tol_rel))

    total = 0.0
    count = 0
    gamma_keys = ['gamma_a', 'gamma_b', 'gamma_c', 'gamma_volume']
    for agent_row in rows:
        try:
            T = float(agent_row['T'])
        except (KeyError, ValueError):
            continue
        ref = ref_dict.get(T)
        if ref is None:
            continue
        for key in gamma_keys:
            if key in agent_row and key in ref:
                total += score_gamma(float(agent_row[key]), float(ref[key]))
                count += 1

    if count == 0:
        return 0.0
    return total / count


_SCORERS = {
    'step_04_moments': score_0,
    'step_06_anharmonic': score_1,
    'step_07_gruneisen': score_2,
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
