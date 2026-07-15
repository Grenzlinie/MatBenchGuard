import os
import json
import csv


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


# === block: score_0 (check id='structural_at_1100C') ===
def score_0(artifact, step, ctx):
    config = step['config']
    temp = config['temperature']
    min_mol = config['min_mole_fraction']
    max_mol = config['max_mole_fraction']
    required = config['required_categories']
    forbidden = config['forbidden_categories']

    # filter rows for the target temperature
    rows_temp = [row for row in artifact if int(float(row.get('Temperature', -999))) == temp]

    # check required categories
    req_found = 0
    for cat in required:
        aliases = cat['aliases']
        found = any(
            row['Phase'] in aliases and float(row['MoleFraction']) > min_mol
            for row in rows_temp
        )
        if found:
            req_found += 1

    # check forbidden categories
    forbidden_violation = False
    for cat in forbidden:
        aliases = cat['aliases']
        for row in rows_temp:
            if row['Phase'] in aliases and float(row['MoleFraction']) > max_mol:
                forbidden_violation = True
                break
        if forbidden_violation:
            break

    num_required = len(required)
    if num_required == 0:
        base_score = 1.0
    else:
        base_score = req_found / num_required

    if forbidden_violation:
        base_score = max(0.0, base_score - 0.5)

    return round(base_score, 6)


# === block: score_1 (check id='monotonic_trend') ===
def score_1(artifact, step, ctx):
    config = step['config']
    temps = config['temperatures']
    beta_aliases = config['beta_aliases']
    gp_aliases = config['gamma_prime_aliases']
    eps = config['epsilon']

    # accumulate fractions per temperature
    temp_to_beta = {t: 0.0 for t in temps}
    temp_to_gp = {t: 0.0 for t in temps}

    for row in artifact:
        temp = int(float(row.get('Temperature', -999)))
        if temp not in temp_to_beta:
            continue
        phase = row['Phase']
        frac = float(row['MoleFraction'])
        if phase in beta_aliases:
            temp_to_beta[temp] += frac
        elif phase in gp_aliases:
            temp_to_gp[temp] += frac

    # check that all required temperatures have at least one row
    if any(temp_to_beta[t] == 0.0 and temp_to_gp[t] == 0.0 for t in temps):
        # missing temperature entirely
        return 0.0

    sorted_temps = sorted(temps)

    # beta: non-increasing (frac at lower temp >= frac at higher temp)
    beta_violations = 0
    beta_pairs = 0
    for i in range(len(sorted_temps)-1):
        t1, t2 = sorted_temps[i], sorted_temps[i+1]
        beta_pairs += 1
        if temp_to_beta[t1] + eps < temp_to_beta[t2]:
            beta_violations += 1

    # gamma prime: non-decreasing (frac at lower temp <= frac at higher temp)
    gp_violations = 0
    gp_pairs = 0
    for i in range(len(sorted_temps)-1):
        t1, t2 = sorted_temps[i], sorted_temps[i+1]
        gp_pairs += 1
        if temp_to_gp[t1] - eps > temp_to_gp[t2]:
            gp_violations += 1

    beta_score = 1.0 - (beta_violations / beta_pairs) if beta_pairs > 0 else 1.0
    gp_score = 1.0 - (gp_violations / gp_pairs) if gp_pairs > 0 else 1.0
    overall = 0.5 * beta_score + 0.5 * gp_score
    return round(max(0.0, overall), 6)


_SCORERS = {
    'structural_at_1100C': score_0,
    'monotonic_trend': score_1,
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
