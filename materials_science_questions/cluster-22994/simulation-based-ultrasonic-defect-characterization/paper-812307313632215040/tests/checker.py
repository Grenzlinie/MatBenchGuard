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


# === block: score_0 (check id='value_accuracy') ===
def score_0(artifact, step, ctx):
    import math
    # Fixed parameters (same as given in task)
    A_c = 1.0
    phi_c = 0.0
    phi_1 = math.pi / 6.0
    t_u = 1.0e-5
    t_d = 1.01e-5
    m_c = 0.1
    ratios = {'fluoroplastic': 0.09, 'metal': 0.225}

    tol_abs = step.get('tol_abs', 1e-12)
    tol_rel = step.get('tol_rel', 1e-6)

    Delta_f = 1.0/t_u - 1.0/t_d

    correct = 0
    total = 0
    for row in artifact:
        total += 1
        atype = row['assembly_type'].strip().lower()
        if atype not in ratios:
            continue
        A1 = ratios[atype]
        f_MHz = float(row['frequency_MHz'])
        f = f_MHz * 1e6
        # composite amplitude and phase
        A = math.sqrt(A_c**2 + A1**2 + 2*A_c*A1*math.cos(phi_c - phi_1))
        numer = A_c*math.sin(phi_c) + A1*math.sin(phi_1)
        denom = A_c*math.cos(phi_c) + A1*math.cos(phi_1)
        phi = math.atan2(numer, denom)
        m = m_c * A_c / A   # since A_c=1
        # phase-induced
        td_prime = (phi - phi_c) / (2*math.pi*f)
        Delta_f_prime = 1.0/t_u - 1.0/(t_d + td_prime)
        delta_prime_exp = (Delta_f - Delta_f_prime) / Delta_f
        # amplitude-induced
        td_double_prime = (math.asin(m_c) - math.asin(m)) / (2*math.pi*f)
        Delta_f_double_prime = 1.0/t_u - 1.0/(t_d + td_double_prime)
        delta_double_prime_exp = (Delta_f - Delta_f_double_prime) / Delta_f
        delta_prime_agent = float(row['delta_prime'])
        delta_double_prime_agent = float(row['delta_double_prime'])
        # tolerance check
        ok_p = abs(delta_prime_agent - delta_prime_exp) <= tol_abs + tol_rel * abs(delta_prime_exp)
        ok_dp = abs(delta_double_prime_agent - delta_double_prime_exp) <= tol_abs + tol_rel * abs(delta_double_prime_exp)
        if ok_p and ok_dp:
            correct += 1

    score = correct / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='trend_monotonic') ===
def score_1(artifact, step, ctx):
    import math
    from collections import defaultdict

    # Fixed parameters (same as given in task)
    A_c = 1.0
    phi_c = 0.0
    phi_1 = math.pi / 6.0
    t_u = 1.0e-5
    t_d = 1.01e-5
    m_c = 0.1
    ratios = {'fluoroplastic': 0.09, 'metal': 0.225}

    tol_abs = 1e-12
    tol_rel = 1e-6

    Delta_f = 1.0/t_u - 1.0/t_d

    # First, verify value accuracy: if any row is not accurate, return 0.0 immediately.
    for row in artifact:
        atype = row['assembly_type'].strip().lower()
        if atype not in ratios:
            continue
        A1 = ratios[atype]
        f_MHz = float(row['frequency_MHz'])
        f = f_MHz * 1e6
        # composite amplitude and phase
        A = math.sqrt(A_c**2 + A1**2 + 2*A_c*A1*math.cos(phi_c - phi_1))
        numer = A_c*math.sin(phi_c) + A1*math.sin(phi_1)
        denom = A_c*math.cos(phi_c) + A1*math.cos(phi_1)
        phi = math.atan2(numer, denom)
        m = m_c * A_c / A
        # phase-induced
        td_prime = (phi - phi_c) / (2*math.pi*f)
        Delta_f_prime = 1.0/t_u - 1.0/(t_d + td_prime)
        delta_prime_exp = (Delta_f - Delta_f_prime) / Delta_f
        # amplitude-induced
        td_double_prime = (math.asin(m_c) - math.asin(m)) / (2*math.pi*f)
        Delta_f_double_prime = 1.0/t_u - 1.0/(t_d + td_double_prime)
        delta_double_prime_exp = (Delta_f - Delta_f_double_prime) / Delta_f
        delta_prime_agent = float(row['delta_prime'])
        delta_double_prime_agent = float(row['delta_double_prime'])
        ok_p = abs(delta_prime_agent - delta_prime_exp) <= tol_abs + tol_rel * abs(delta_prime_exp)
        ok_dp = abs(delta_double_prime_agent - delta_double_prime_exp) <= tol_abs + tol_rel * abs(delta_double_prime_exp)
        if not (ok_p and ok_dp):
            return 0.0

    # If all values are accurate, now check monotonic trend.
    groups = defaultdict(list)
    for row in artifact:
        atype = row['assembly_type'].strip().lower()
        f_MHz = float(row['frequency_MHz'])
        dp = float(row['delta_prime'])
        ddp = float(row['delta_double_prime'])
        groups[atype].append((f_MHz, abs(dp), abs(ddp)))

    for atype, rows in groups.items():
        rows.sort(key=lambda x: x[0])
        dp_abs = [r[1] for r in rows]
        if len(dp_abs) > 1:
            # non-increasing and not constant
            if not all(x >= y - 1e-12 for x, y in zip(dp_abs, dp_abs[1:])):
                return 0.0
            if max(dp_abs) - min(dp_abs) < 1e-12:
                return 0.0
        ddp_abs = [r[2] for r in rows]
        if len(ddp_abs) > 1:
            if not all(x >= y - 1e-12 for x, y in zip(ddp_abs, ddp_abs[1:])):
                return 0.0
            if max(ddp_abs) - min(ddp_abs) < 1e-12:
                return 0.0

    return 1.0


_SCORERS = {
    'value_accuracy': score_0,
    'trend_monotonic': score_1,
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
