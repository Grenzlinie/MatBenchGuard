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
    def compute_tau(ct, c2_over_ct):
        return (-(49.7457 * math.log(ct) + 165.004) * c2_over_ct + 174.65 * (ct ** -0.3405)) / 1000.0

    def compute_G(ct, c2_over_ct):
        # Eq. (2) is the effective shear modulus G (paper labels it 'E' but it is G)
        return -(7.233 * ct - 0.384) * c2_over_ct + 32.729 * math.exp(-3.673 * ct)

    cts = [0.075, 0.15, 0.223]
    c2_over_cts = [0.0, 0.25, 0.5, 0.75, 1.0]
    gold = {}
    for ct in cts:
        for c2 in c2_over_cts:
            key = (round(ct, 6), round(c2, 6))
            gold[key] = (compute_tau(ct, c2), compute_G(ct, c2))

    return {
        'gold': gold,
        'cts': cts,
        'c2_over_cts': c2_over_cts,
    }


# === block: score_0 (check id='effective_properties') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    cts = ctx['cts']
    c2_over_cts = ctx['c2_over_cts']
    tol_rel = step.get('tolerance_relative', 0.15)

    # build agent data
    agent_data = {}
    for row in artifact:
        try:
            ct = round(float(row['Ct']), 6)
            c2 = round(float(row['C2_over_Ct']), 6)
            tau = float(row['tau_mean'])
            g = float(row['G_mean'])
            agent_data[(ct, c2)] = (tau, g)
        except Exception:
            continue

    # tolerance score
    count_total = 0
    count_pass = 0
    for ct in cts:
        for c2 in c2_over_cts:
            key = (round(ct, 6), round(c2, 6))
            if key not in gold:
                continue
            tau_ref, g_ref = gold[key]
            if key in agent_data:
                tau_agent, g_agent = agent_data[key]
                err_tau = abs(tau_agent - tau_ref) / max(abs(tau_ref), 1e-12)
                err_g = abs(g_agent - g_ref) / max(abs(g_ref), 1e-12)
                if err_tau <= tol_rel and err_g <= tol_rel:
                    count_pass += 1
            count_total += 1

    tolerance_score = (count_pass / count_total) if count_total > 0 else 0.0

    # monotonicity score
    trend_total = 0
    trend_pass = 0
    for ct in cts:
        sorted_c2 = sorted(c2_over_cts)
        for i in range(len(sorted_c2)-1):
            key_curr = (round(ct, 6), round(sorted_c2[i], 6))
            key_next = (round(ct, 6), round(sorted_c2[i+1], 6))
            if key_curr in agent_data and key_next in agent_data:
                tau_curr, g_curr = agent_data[key_curr]
                tau_next, g_next = agent_data[key_next]
                if tau_curr >= tau_next:
                    trend_pass += 1
                trend_total += 1
                if g_curr >= g_next:
                    trend_pass += 1
                trend_total += 1

    trend_score = (trend_pass / trend_total) if trend_total > 0 else 1.0

    score = 0.7 * tolerance_score + 0.3 * trend_score
    return score


_SCORERS = {
    'effective_properties': score_0,
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
