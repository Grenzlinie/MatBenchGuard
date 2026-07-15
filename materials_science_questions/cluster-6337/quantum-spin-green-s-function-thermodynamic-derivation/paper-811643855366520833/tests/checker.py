import os
import json
import csv

# === author imports / helpers ===
import math
import json

def _li2(z, tol=1e-15):
    """Dilogarithm Li_2(z) for real z with |z| <= 1 via power series."""
    if z == 0.0:
        return 0.0
    if z == 1.0:
        return math.pi**2 / 6.0
    s = z
    term = z
    k = 1
    while True:
        k += 1
        term = term * z * ((k - 1) ** 2) / (k ** 2)
        s += term
        if abs(term) <= tol * abs(s):
            break
    return s

def spence(z):
    """spence(z) = Li_2(z) for real z."""
    return _li2(z)


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
    def li2(z):
        return spence(1 - z)

    alpha = (9 * math.pi / 4) ** (-1/3)
    pi = math.pi
    ln2 = math.log(2)

    def lambda1a_spin_scaling(zeta):
        kd = (1 - zeta) ** (1/3)
        ku = (1 + zeta) ** (1/3)
        if abs(kd - ku) < 1e-15:
            return 1.0
        term1 = (pi**2/6 + 0.25) * (kd**2 + ku**2) - 1.5 * kd * ku
        term2 = - (kd**2 + ku**2) / (kd**2 - ku**2) * kd * ku * math.log(kd / ku)
        term3 = - (kd**2 - ku**2) / 2 * (li2((kd - ku)/(kd + ku)) - li2((ku - kd)/(kd + ku)))
        factor = 3 / (pi**2 - 6)
        return factor * (term1 + term2 + term3)

    def lambda1b_spin_scaling(zeta):
        kd = (1 - zeta) ** (1/3)
        ku = (1 + zeta) ** (1/3)
        if abs(kd - ku) < 1e-15:
            return 1.0
        term1 = pi**2/6 * (kd**2 + ku**2) + (1 - ln2) * (kd - ku)**2
        term2 = - kd**2/2 * li2((kd - ku)/(kd + ku)) - ku**2/2 * li2((ku - kd)/(kd + ku))
        term3 = 1/(kd*ku) * (kd**4 * math.log(kd/(kd+ku)) + kd**2*ku**2 * math.log(kd*ku/((kd+ku)**2)) + ku**4 * math.log(ku/(kd+ku)))
        factor = 3 / (pi**2 - 12*ln2)
        return factor * (term1 + term2 + term3)

    lam_a0 = alpha / (24 * pi**3) * (pi**2 - 6)
    lam_b0 = alpha / (4 * pi**3) * (pi**2 - 12 * ln2)
    lam_0 = lam_a0 + lam_b0
    lam_a1 = (2**(-7/3)) * alpha / (24 * pi**3) * (pi**2 + 6)
    lam_b1 = (2**(-4/3)) * lam_b0
    lam_1 = lam_a1 + lam_b1

    gold_step01 = {
        "lambda1_0": lam_0,
        "lambda1_1": lam_1,
        "lambda1_a_0": lam_a0,
        "lambda1_a_1": lam_a1,
        "lambda1_b_0": lam_b0,
        "lambda1_b_1": lam_b1
    }

    zeta = 0.5
    Lam_a = lambda1a_spin_scaling(zeta)
    Lam_b = lambda1b_spin_scaling(zeta)
    kup = (1+zeta)**(1/3)
    Lam_a_upup = (1/8) * (pi**2+6)/(pi**2-6) * kup**2 / Lam_a
    Lam_b_upup = (1/4) * kup**2 / Lam_b
    gold_step02 = {
        "Lambda1_a_upup_05": Lam_a_upup,
        "Lambda1_b_upup_05": Lam_b_upup
    }

    delta = 2**(-1/3) * alpha / (8 * pi**3)
    gold_step03 = {
        "delta_lambda1a_1": delta
    }

    return {
        'gold_step01': gold_step01,
        'gold_step02': gold_step02,
        'gold_step03': gold_step03
    }


# === block: score_0 (check id='compute_lambda1_limits') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_step01']
    tol = step.get('tolerance', 1e-8)
    score_sum = 0.0
    count = 0
    for field in step.get('fields', []):
        agent_val = artifact.get(field)
        gold_val = gold.get(field)
        if gold_val is None or agent_val is None:
            continue
        rel_err = abs(agent_val - gold_val) / max(abs(gold_val), 1e-12)
        if rel_err <= tol:
            score_sum += 1.0
        count += 1
    return score_sum / count if count > 0 else 0.0


# === block: score_1 (check id='compute_spin_resolution') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold_step02']
    tol = step.get('tolerance', 1e-8)
    score_sum = 0.0
    count = 0
    for field in step.get('fields', []):
        agent_val = artifact.get(field)
        gold_val = gold.get(field)
        if gold_val is None or agent_val is None:
            continue
        rel_err = abs(agent_val - gold_val) / max(abs(gold_val), 1e-12)
        if rel_err <= tol:
            score_sum += 1.0
        count += 1
    return score_sum / count if count > 0 else 0.0


# === block: score_2 (check id='compute_delta_lambda1a') ===
def score_2(artifact, step, ctx):
    gold = ctx['gold_step03']
    tol = step.get('tolerance', 1e-8)
    score_sum = 0.0
    count = 0
    for field in step.get('fields', []):
        agent_val = artifact.get(field)
        gold_val = gold.get(field)
        if gold_val is None or agent_val is None:
            continue
        rel_err = abs(agent_val - gold_val) / max(abs(gold_val), 1e-12)
        if rel_err <= tol:
            score_sum += 1.0
        count += 1
    return score_sum / count if count > 0 else 0.0


_SCORERS = {
    'compute_lambda1_limits': score_0,
    'compute_spin_resolution': score_1,
    'compute_delta_lambda1a': score_2,
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
