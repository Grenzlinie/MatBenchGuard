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
    import math

    # ===== analytic helpers =====
    def thue_morse_sigma(x, max_k=50):
        """Eq. 3.10: Sigma(x) = sum over k of ..."""
        s = 0.0
        for k in range(0, max_k):
            x2k = x ** (2**k)
            if x2k < 1e-16:
                break
            prod_p = 1.0
            for p in range(0, k+1):
                prod_p *= (1.0 - x**(2**p))
            denom = (1.0 - x2k) * (1.0 - x2k*x2k)   # (1-x^{2^k})(1-x^{2^{k+1}})
            if denom == 0:
                continue
            term = x * x2k * prod_p / denom
            s += term
            if abs(term) < 1e-16:
                break
        return s

    def thue_morse_S(lam_ratio, r=2.0):
        """S(lambda,r) for lambda/lambda_c > 1. For <= 1 returns inf (we handle later)."""
        if lam_ratio <= 1.0:
            return float('inf')
        lam_c = r ** -0.5  # rho=0.5
        x = (lam_c / (lam_ratio * lam_c)) ** 4   # = 1/ratio^4
        term1 = (1.0 + r * x**0.5) / (1.0 - x)
        term2 = (1.0/r - r) * (lam_ratio)**2 * thue_morse_sigma(x)
        return term1 + term2

    def period_doubling_S(lam_ratio, r=2.0, max_k=20):
        """S(lambda,r) via infinite product Eq. 4.7, for lambda/lambda_c > 1."""
        if lam_ratio <= 1.0:
            return float('inf')
        lam_c = r ** -(2.0/3.0)
        x = lam_c / (lam_ratio * lam_c)   # = 1/ratio
        prod = 1.0
        for k in range(1, max_k+1):
            pow1 = 2**(2*k-1)
            pow2 = 2**(2*k)
            term1 = x ** pow1
            term2 = x ** pow2
            factor = (1.0 + lam_c * term1) * (1.0 + (1.0/lam_c) * term2)
            prod *= factor
            if abs(factor - 1.0) < 1e-16:
                break
        return prod

    def ms_from_S(S):
        if S == float('inf'):
            return 0.0
        return 1.0 / math.sqrt(S)

    # ===== build gold table =====
    r_val = 2.0
    ratios = [0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1]
    gold_ms = {}
    for seq in ['thue_morse', 'period_doubling']:
        gold_ms[seq] = {}
        for ratio in ratios:
            if ratio <= 1.0:
                ms_val = 0.0
            else:
                if seq == 'thue_morse':
                    S = thue_morse_S(ratio, r_val)
                else:
                    S = period_doubling_S(ratio, r_val)
                ms_val = ms_from_S(S)
            gold_ms[seq][ratio] = ms_val

    # theoretical exponents
    lam_c_pd = r_val ** -(2.0/3.0)
    period_beta = math.log((1.0+lam_c_pd)*(1.0+1.0/lam_c_pd)) / (4.0 * math.log(2.0))
    target_betas = {
        'thue_morse_beta_s': 0.5,
        'period_doubling_beta_s': period_beta
    }

    ctx = {
        'gold_ms': gold_ms,
        'target_betas': target_betas,
        'r_val': r_val,
        'ratios': ratios
    }
    return ctx


# === block: score_0 (check id='step_01_surface_magnetization_data') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 18:
        return 0.0

    gold_ms = ctx['gold_ms']
    tol = step.get('tolerance_relative', 0.0001)
    correct = 0
    total = 0
    for row in artifact:
        seq = row.get('sequence', '').strip()
        r_read = row.get('r', '').strip()
        lr_str = row.get('lambda_over_lambda_c', '').strip()
        ms_str = row.get('ms', '').strip()
        if not seq or not r_read or not lr_str or not ms_str:
            continue
        try:
            r_val = float(r_read)
            lr = float(lr_str)
            ms = float(ms_str)
        except:
            continue
        # Only score rows where sequence and ratio are expected
        if seq not in gold_ms or lr not in gold_ms[seq]:
            continue
        gold = gold_ms[seq][lr]
        denom = max(abs(gold), 1e-15)
        err = abs(ms - gold) / denom
        total += 1
        if err <= tol:
            correct += 1

    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='step_02_critical_exponents') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    
    target_betas = ctx['target_betas']
    tol = step.get('tolerance_abs', 0.01)
    keys = ['thue_morse_beta_s', 'period_doubling_beta_s']
    ok = 0
    for k in keys:
        if k not in artifact:
            continue
        try:
            val = float(artifact[k])
        except:
            continue
        if abs(val - target_betas[k]) <= tol:
            ok += 1
    return ok / len(keys)


_SCORERS = {
    'step_01_surface_magnetization_data': score_0,
    'step_02_critical_exponents': score_1,
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
