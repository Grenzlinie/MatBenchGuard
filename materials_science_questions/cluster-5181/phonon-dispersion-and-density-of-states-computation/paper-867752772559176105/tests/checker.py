import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    # parse grading spec for constants and conditions
    spec = json.load(open('/tests/grading_spec.json'))
    step = spec['steps'][0]
    T = step['parameters']['T_K']
    L = step['parameters']['L_um']
    omega_D1 = step['parameters']['omega_D1_rad_s']
    hbar = step['parameters']['hbar']
    kB = step['parameters']['kB']
    theta = hbar * omega_D1 / kB
    Theta = T / theta
    # Ideal graphene coefficients
    A1 = 1310.0 / (0.573 + L**(-0.45))
    A2 = 3.0 / (26.0 * L**0.07) - 0.0594
    A3 = 5.0 / (121.0 * L**0.35) - 0.005
    kappa_I = A1 * Theta**2 / ((Theta + A2)**3 + A3**2)
    # Defect-term coefficients
    B1 = -14.9 * L**(7.0/13.0) + 1711.0 / (11.0 - math.log(L)) - 107.0
    B2 = 46.5 * (L - 153.0) / (L**0.5 + 8.0) + 913.0
    B3 = 13.6 * L**0.42 - 3.7 * math.log(L) - 16.8
    def expected_kappa(mu, n):
        if mu == 0.0 or n == 0.0:
            return kappa_I
        kappa_D = B1 * math.sqrt(Theta) + B2 * mu * n**0.53 + B3
        return 1.0 / (1.0 / kappa_I + mu**2 * n / kappa_D)
    expected = {}
    for c in step['parameters']['conditions']:
        expected[c['name']] = expected_kappa(c['mu'], c['n'])
    return {'expected': expected, 'relative_tolerance': step['relative_tolerance'], 'check_ordering': step['check_ordering']}


# === block: score_0 (check id='step_total_kappa') ===
def score_0(artifact, step, ctx):
    # Build lookup from agent's rows
    agent = {}
    for row in artifact:
        cond = str(row.get('condition', '')).strip()
        try:
            k = float(row.get('kappa_W_mK', 0))
        except (ValueError, TypeError):
            k = None
        agent[cond] = k

    expected = ctx['expected']
    tol = ctx['relative_tolerance']
    check_ordering = ctx['check_ordering']

    # Score each expected condition
    scores = {}
    for cond in ['ideal', 'doped_Al', 'doped_N']:
        exp = expected.get(cond)
        if exp is None or exp == 0.0:
            scores[cond] = 0.0
            continue
        got = agent.get(cond)
        if got is None:
            scores[cond] = 0.0
            continue
        rel_err = abs(got - exp) / abs(exp) if abs(exp) > 1e-12 else (0.0 if abs(got) < 1e-12 else 1.0)
        # Score: 1.0 if rel_err <= tol, linear decay to 0 at 2*tol
        if rel_err <= tol:
            scores[cond] = 1.0
        elif rel_err <= 2*tol:
            scores[cond] = (2*tol - rel_err) / tol
        else:
            scores[cond] = 0.0

    num_score = sum(scores.values()) / 3.0 if scores else 0.0

    # Ordering score: ideal > doped_N > doped_Al
    order_score = 0.0
    if check_ordering:
        k_ideal = agent.get('ideal')
        k_N = agent.get('doped_N')
        k_Al = agent.get('doped_Al')
        if k_ideal is not None and k_N is not None and k_Al is not None:
            if k_ideal > k_N > k_Al:
                order_score = 1.0
            elif k_ideal > k_N or k_ideal > k_Al or k_N > k_Al:
                order_score = 0.5  # partial
            else:
                order_score = 0.0
        else:
            order_score = 0.0

    # Weighted combination: 0.9 numerical, 0.1 ordering
    final = num_score * 0.9 + order_score * 0.1
    return final


_SCORERS = {
    'step_total_kappa': score_0,
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
