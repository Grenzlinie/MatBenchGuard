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


# === block: score_0 (check id='scaled_stress_step') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_cols = ['psi_deg', 'scaled_stress_v0', 'scaled_stress_v99', 'scaled_stress_stationary']
    for col in required_cols:
        if col not in artifact[0]:
            return 0.0
    c44 = 5.0e10
    R = 1.2e9
    K = 3.0e8
    e15 = -0.138
    e15p = -0.160
    eps11 = 82.6e-12
    rho = 5.1e3
    cbar44 = c44 + e15**2 / eps11
    Kbar = K + e15p**2 / eps11
    Rbar = R + e15 * e15p / eps11
    alpha = (cbar44 - Kbar + math.sqrt((cbar44 - Kbar)**2 + 4 * Rbar**2)) / 2
    eps1 = (cbar44 + Kbar + math.sqrt((cbar44 - Kbar)**2 + 4 * Rbar**2)) / 2
    eps2 = (cbar44 + Kbar - math.sqrt((cbar44 - Kbar)**2 + 4 * Rbar**2)) / 2
    s1 = math.sqrt(eps1 / rho)
    s2 = math.sqrt(eps2 / rho)

    def compute_gold_for_speed(v_ratio):
        v = v_ratio * s2
        beta1 = math.sqrt(1 - v**2 / s1**2)
        beta2 = math.sqrt(1 - v**2 / s2**2)
        denom1 = (alpha**2 + Rbar**2) * (cbar44 * Kbar - Rbar**2)
        Lambda1 = (cbar44 * alpha + Rbar**2) * (alpha * Kbar - Rbar**2) / denom1
        Lambda2 = Rbar**2 * (cbar44 - alpha) * (alpha + Kbar) / denom1
        results = []
        for row in artifact:
            try:
                psi_deg = float(row['psi_deg'])
            except:
                results.append(None)
                continue
            psi = math.radians(psi_deg)
            tan_psi = math.tan(psi)
            def phi_k(k):
                phi = math.atan(k * tan_psi)
                if psi > math.pi / 2:
                    phi += math.pi
                return phi
            phi_b1 = phi_k(beta1)
            phi_b2 = phi_k(beta2)
            Delta_b1 = (math.cos(psi)**2 + beta1**2 * math.sin(psi)**2) ** 0.25
            Delta_b2 = (math.cos(psi)**2 + beta2**2 * math.sin(psi)**2) ** 0.25
            C1 = (1 / beta1) * math.sin(phi_b1 / 2) * math.sin(psi) + math.cos(phi_b1 / 2) * math.cos(psi)
            C2 = (1 / beta2) * math.sin(phi_b2 / 2) * math.sin(psi) + math.cos(phi_b2 / 2) * math.cos(psi)
            scaled = 1e5 * (Lambda1 / Delta_b1 * C1 + Lambda2 / Delta_b2 * C2)
            results.append(scaled)
        return results

    gold_v0 = compute_gold_for_speed(0.0)
    gold_v99 = compute_gold_for_speed(0.99)
    gold_stat = []
    for row in artifact:
        try:
            psi_deg = float(row['psi_deg'])
        except:
            gold_stat.append(None)
            continue
        psi = math.radians(psi_deg)
        gold_stat.append(math.cos(psi / 2))

    rel_tol = 0.05
    abs_tol = 0.01

    def count_correct(agent_vals, gold_col):
        total = 0
        correct = 0
        for a, g in zip(agent_vals, gold_col):
            if g is None:
                continue
            try:
                af = float(a)
            except:
                continue
            tol = max(rel_tol * abs(g), abs_tol)
            if abs(af - g) <= tol:
                correct += 1
            total += 1
        if total == 0:
            return 0.0
        return correct / total

    vals_v0 = [row.get('scaled_stress_v0', 0) for row in artifact]
    vals_v99 = [row.get('scaled_stress_v99', 0) for row in artifact]
    vals_stat = [row.get('scaled_stress_stationary', 0) for row in artifact]
    frac0 = count_correct(vals_v0, gold_v0)
    frac99 = count_correct(vals_v99, gold_v99)
    frac_st = count_correct(vals_stat, gold_stat)
    score = (frac0 + frac99 + frac_st) / 3.0
    return score


_SCORERS = {
    'scaled_stress_step': score_0,
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
