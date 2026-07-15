import os
import json
import csv

# === author imports / helpers ===
import re
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
    import os
    os.makedirs('/logs/verifier', exist_ok=True)
    return {}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerances', {})
    dh = artifact.get('delta_H_formation', None)
    se = artifact.get('S_entropy', None)
    peri = artifact.get('peritectic_temperature_C', None)
    cp = artifact.get('Cp_coefficients', None)
    if None in (dh, se, peri, cp):
        return 0.0
    # enthalpy and entropy and peritectic ternary check
    ok_dh = abs(dh - gold['delta_H_formation']) <= tol.get('delta_H_formation', 2.0)
    ok_se = abs(se - gold['S_entropy']) <= tol.get('S_entropy', 5.0)
    ok_peri = abs(peri - gold['peritectic_temperature_C']) <= tol.get('peritectic_temperature_C', 30)
    # Cp coefficients: compute max relative error across all 12 numbers
    gold_cp = gold.get('Cp_coefficients', [])
    tol_rel = tol.get('Cp_coefficient_relative', 0.02)
    max_err = 0.0
    for row_a, row_g in zip(cp, gold_cp):
        for a, g in zip(row_a, row_g):
            denom = abs(g) + 1e-12
            err = abs(a - g) / denom
            if err > max_err:
                max_err = err
    ok_cp = 1.0 if max_err <= tol_rel else 0.0
    return (ok_dh + ok_se + ok_peri + ok_cp) / 4.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    checks = step.get('checks', {})
    exp_dominant = set(checks.get('expected_dominant_species', []))
    if not exp_dominant:
        return 0.0
    agent_dominant = set(artifact.get('dominant_species', []))
    dominant_ok = agent_dominant.issuperset(exp_dominant)
    temp_C = artifact.get('temperature_C', None)
    br_at = artifact.get('bromine_content_at_percent', None)
    temp_range = checks.get('temperature_range_C', [680, 720])
    br_range = checks.get('bromine_range_at_percent', [3, 7])
    temp_ok = isinstance(temp_C, (int, float)) and temp_range[0] <= temp_C <= temp_range[1]
    br_ok = isinstance(br_at, (int, float)) and br_range[0] <= br_at <= br_range[1]
    score = 0.0
    if dominant_ok:
        score += 0.8
    if temp_ok:
        score += 0.1
    if br_ok:
        score += 0.1
    return min(1.0, score)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    checks = step.get('checks', {})
    required_agent = checks.get('transport_agent', 'TeBr2')
    required_migrating = set(checks.get('migrating_species_required', []))
    net_reaction_expected = checks.get('net_reaction_normalized', '')

    def parse_side(side):
        result = {}
        terms = side.split('+')
        for term in terms:
            term = term.strip()
            if not term:
                continue
            coeff = 1
            # extract leading coefficient if present
            m = re.match(r'^(\d+)\s*(.*)', term)
            if m:
                coeff = int(m.group(1))
                species_part = m.group(2)
            else:
                species_part = term
            # remove trailing state (s)/(g)/(l)/(aq) etc.
            species = re.sub(r'\s*\([^)]*\)\s*$', '', species_part).strip()
            if not species:
                continue
            result[species] = result.get(species, 0) + coeff
        return result

    def parse_reaction(s):
        s = s.strip().lower()
        s = re.sub(r'\s+', ' ', s)
        # normalize arrows
        s = s.replace('=>', '<=>').replace('\u21cc', '<=>').replace('<->', '<=>')
        parts = re.split(r'<=>', s)
        if len(parts) != 2:
            return None, None
        left = parse_side(parts[0])
        right = parse_side(parts[1])
        return left, right

    agent_ok = artifact.get('transport_agent') == required_agent
    agent_migrating = set(artifact.get('migrating_species', []))
    migrating_ok = agent_migrating.issuperset(required_migrating)

    gold_left, gold_right = parse_reaction(net_reaction_expected)
    agent_left, agent_right = parse_reaction(artifact.get('net_reaction', ''))
    reaction_ok = (agent_left is not None and gold_left is not None and agent_left == gold_left and agent_right == gold_right)

    score = 0.0
    if agent_ok:
        score += 0.3
    if migrating_ok:
        score += 0.3
    if reaction_ok:
        score += 0.4
    return score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
