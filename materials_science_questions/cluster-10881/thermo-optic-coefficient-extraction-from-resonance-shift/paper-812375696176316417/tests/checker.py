import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np

def compute_expected_fth(P):
    a = 1.0
    d = 0.5
    k = 0.037
    beta = 0.012
    n0 = 3.30
    gamma = 18.7e-5
    alpha = 5.7e-6
    T0 = 298.0
    Tn = 298.1
    g = (Tn - T0) / d
    if P == 0:
        return float('inf')
    Tc = T0 + 2e-4 * P
    target_ratio = T0 / Tc
    # solve for lambda*a satisfying j0(lam*a) = target_ratio
    def fn(x):
        return np.j0(x * a) - target_ratio
    low, high = 0.0, 2.5
    for _ in range(100):
        mid = (low + high) / 2.0
        if fn(mid) < 0:
            high = mid
        else:
            low = mid
    lam = (low + high) / 2.0
    I = P / (math.pi * a**2)
    term = (alpha + gamma) * n0
    inner = T0 * d + 0.5 * g * d**2 + (beta * I) / (6.0 * k) * d**3
    j0_val = np.j0(lam * a)
    if j0_val == 0:
        Delta = float('inf')
    else:
        Delta = term * inner * (1.0 / j0_val - 1.0)
    if Delta == 0:
        return float('inf')
    return a**2 / (2.0 * Delta * (n0 - 1.0))


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


# === block: score_0 (check id='thermal_focal_length') ===
def score_0(artifact, step, ctx):
    from scipy.special import j0

    def compute_expected_fth(P):
        a = 1.0
        d = 0.5
        k = 0.037
        beta = 0.012
        n0 = 3.30
        gamma = 18.7e-5
        alpha = 5.7e-6
        T0 = 298.0
        Tn = 298.1
        g = (Tn - T0) / d
        if P == 0:
            return float('inf')
        Tc = T0 + 2e-4 * P
        target_ratio = T0 / Tc
        def fn(x):
            return j0(x * a) - target_ratio
        low, high = 0.0, 2.5
        for _ in range(100):
            mid = (low + high) / 2.0
            if fn(mid) < 0:
                high = mid
            else:
                low = mid
        lam = (low + high) / 2.0
        I = P / (math.pi * a**2)
        term = (alpha + gamma) * n0
        inner = T0 * d + 0.5 * g * d**2 + (beta * I) / (6.0 * k) * d**3
        j0_val = j0(lam * a)
        if j0_val == 0:
            Delta = float('inf')
        else:
            Delta = term * inner * (1.0 / j0_val - 1.0)
        if Delta == 0:
            return float('inf')
        return a**2 / (2.0 * Delta * (n0 - 1.0))

    rows = artifact
    required_powers = set(step.get('required_powers', []))
    if not required_powers:
        return 0.0

    agent_by_power = {}
    for row in rows:
        try:
            p = float(row.get('P', None))
            fth_str = row.get('f_th', '')
            if isinstance(fth_str, str):
                fth_str = fth_str.strip().lower()
                if fth_str in ('inf', 'infinity'):
                    val = float('inf')
                elif fth_str == 'nan':
                    val = float('nan')
                else:
                    val = float(fth_str)
            else:
                val = float(fth_str) if fth_str is not None else float('nan')
        except (ValueError, TypeError):
            return 0.0
        agent_by_power[p] = val

    agent_p_set = set(round(p) for p in agent_by_power)
    if agent_p_set != set(required_powers):
        return 0.0

    correct = 0
    for p in required_powers:
        expected = compute_expected_fth(p)
        agent = agent_by_power.get(float(p), None)
        if agent is None:
            continue
        if math.isinf(expected) and math.isinf(agent):
            correct += 1
            continue
        if math.isnan(expected) or math.isnan(agent) or math.isinf(expected) or math.isinf(agent):
            continue
        rel_err = abs(agent - expected) / max(abs(expected), 1e-6)
        if rel_err <= 0.05:
            correct += 1
    return correct / len(required_powers)


_SCORERS = {
    'thermal_focal_length': score_0,
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
