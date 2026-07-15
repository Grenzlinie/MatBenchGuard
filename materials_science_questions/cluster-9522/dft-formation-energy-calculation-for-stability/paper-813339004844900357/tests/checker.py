import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    gold = spec.get('gold_reference', {})
    tol = gold.get('tolerances', {})
    return {'gold': gold, 'tol': tol}


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    # Extract artifact
    artifact_data = artifact
    if not isinstance(artifact_data, dict):
        return 0.0
    ctx_gold = ctx.get('gold', {})
    compositions = ctx_gold.get('compositions_order', [])
    gold_vals = ctx_gold.get('values', {})
    tol = ctx.get('tol', {})

    # Fields to check (exclude ratio, Delta_W, gamma_b3, gamma_b6; gold for b3/b6 is fabricated)
    num_fields = ['bcc_hcp_energy_difference', 'C_prime', 'gamma_us_112', 'gamma_us_110', 'G', 'lattice_constant_a']
    field_weight = 1.0 / len(num_fields)
    comp_weight = 1.0 / len(compositions)

    numeric_score = 0.0
    for comp in compositions:
        if comp not in artifact_data:
            continue
        agent_comp = artifact_data[comp]
        gold_comp = gold_vals.get(comp, {})
        comp_score = 0.0
        for field in num_fields:
            if field not in agent_comp or field not in gold_comp:
                continue
            val = agent_comp[field]
            gval = gold_comp[field]
            t = tol.get(field, {})
            abs_tol = t.get('abs', 1e6)
            rel_tol = t.get('rel', 1.0)
            # compute allowed deviation
            max_dev = max(abs_tol, rel_tol * abs(gval) if abs(gval) > 1e-12 else abs_tol)
            diff = abs(val - gval)
            if diff <= max_dev:
                comp_score += field_weight
            else:
                # partial: decay beyond tolerance
                excess = diff - max_dev
                decay = max(0.0, 1.0 - excess / (max_dev * 3))
                comp_score += field_weight * decay
        numeric_score += comp_score * comp_weight

    # Structural trends
    structural_score = 0.0
    # collect for trends
    bcc_hcp = []
    c_prime_vals = []
    ratio_vals = []
    delta_w_vals = []
    for comp in compositions:
        if comp in artifact_data:
            bcc_hcp.append(artifact_data[comp].get('bcc_hcp_energy_difference', None))
            c_prime_vals.append(artifact_data[comp].get('C_prime', None))
            ratio_vals.append(artifact_data[comp].get('ratio_gamma_b3_to_2gamma_b6', None))
            delta_w_vals.append(artifact_data[comp].get('Delta_W_min', None))
        else:
            bcc_hcp.append(None)
            c_prime_vals.append(None)
            ratio_vals.append(None)
            delta_w_vals.append(None)

    # Trend 1: bcc_hcp_energy_difference decreases monotonically (less negative -> less stable) and final near zero
    trend1_ok = True
    if len(bcc_hcp) == 4:
        # expect increasing values (from negative towards zero)
        for i in range(1, 4):
            if bcc_hcp[i] is None or bcc_hcp[i-1] is None:
                trend1_ok = False; break
            if bcc_hcp[i] < bcc_hcp[i-1] - 0.01:  # allow small noise
                trend1_ok = False; break
        if trend1_ok and abs(bcc_hcp[3]) > 0.02:
            trend1_ok = False  # Ti25Nb should be near zero
    else:
        trend1_ok = False
    if trend1_ok:
        structural_score += 0.1

    # Trend 2: C_prime decreases monotonically and final near zero
    trend2_ok = True
    if len(c_prime_vals) == 4:
        for i in range(1, 4):
            if c_prime_vals[i] is None or c_prime_vals[i-1] is None:
                trend2_ok = False; break
            if c_prime_vals[i] > c_prime_vals[i-1] + 2.0:  # some tolerance
                trend2_ok = False; break
        if trend2_ok and c_prime_vals[3] > 5.0:
            trend2_ok = False
    else:
        trend2_ok = False
    if trend2_ok:
        structural_score += 0.1

    # Trend 3: ratio_gamma_b3_to_2gamma_b6 increases monotonically
    trend3_ok = True
    if len(ratio_vals) == 4:
        for i in range(1, 4):
            if ratio_vals[i] is None or ratio_vals[i-1] is None:
                trend3_ok = False; break
            if ratio_vals[i] < ratio_vals[i-1] - 0.02:
                trend3_ok = False; break
    else:
        trend3_ok = False
    if trend3_ok:
        structural_score += 0.1

    # Trend 4: Delta_W_min negative only for Ti25Nb
    trend4_ok = True
    if len(delta_w_vals) == 4:
        for idx, comp in enumerate(compositions):
            val = delta_w_vals[idx]
            if val is None:
                trend4_ok = False; break
            if comp == 'Ti25Nb':
                if val >= -0.02:
                    trend4_ok = False; break
            else:
                if val < -0.02:
                    trend4_ok = False; break
    else:
        trend4_ok = False
    if trend4_ok:
        structural_score += 0.1

    # Combine scores
    final_score = numeric_score * 0.6 + structural_score
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'results_check': score_0,
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
