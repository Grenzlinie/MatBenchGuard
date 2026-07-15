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
    import csv, os

    output_dir = '/app/outputs'
    csv_path = os.path.join(output_dir, 'free_energies_table.csv')
    species_required = ['*NO','*HNO','*NOH','*HNOH','*H2NO','*N','*H2NOH','*NH','*NH2','*NH3','*H','NO(g)','H2(g)','N2(g)','H2O(g)','NH3(g)']

    if not os.path.exists(csv_path):
        return {'valid': False}

    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        return {'valid': False}

    cols = set(rows[0].keys())
    required_cols = {'species','total_energy_eV','ZPE_eV','TS_eV','free_energy_eV'}
    if not required_cols.issubset(cols):
        return {'valid': False}

    species_present = {r['species'].strip() for r in rows}
    if not set(species_required).issubset(species_present):
        return {'valid': False}

    free_energy = {}
    for r in rows:
        sp = r['species'].strip()
        try:
            free_energy[sp] = float(r['free_energy_eV'])
        except ValueError:
            return {'valid': False}

    G_HNO = free_energy.get('*HNO')
    G_HNOH = free_energy.get('*HNOH')
    G_H = free_energy.get('*H')
    if G_HNO is None or G_HNOH is None or G_H is None:
        return {'valid': False}

    delta_G_RDS = G_HNOH - G_HNO
    u_NO = -delta_G_RDS
    u_HER = -G_H
    return {'valid': True, 'u_NO': u_NO, 'u_HER': u_HER}


# === block: score_0 (check id='csv_structure') ===
def score_0(artifact, step, ctx):
    species_required = ['*NO','*HNO','*NOH','*HNOH','*H2NO','*N','*H2NOH','*NH','*NH2','*NH3','*H','NO(g)','H2(g)','N2(g)','H2O(g)','NH3(g)']

    if artifact is None:
        return 0.0

    species_present = set()
    for row in artifact:
        sp = row.get('species', '').strip()
        if sp:
            species_present.add(sp)

    found = len(species_present.intersection(species_required))
    total = len(species_required)
    fraction = found / total if total > 0 else 0.0

    tol = step.get('tolerance', 0.0)
    threshold = 1.0 - tol
    if fraction >= threshold:
        return 1.0
    else:
        return max(0.0, fraction / threshold) if threshold > 0 else 0.0


# === block: score_1 (check id='recompute_NORR') ===
def score_1(artifact, step, ctx):
    import step as step_def

    target = -0.33
    tol = 0.15
    if not ctx.get('valid'):
        return 0.0
    u = ctx['u_NO']
    if u >= target - tol:
        return 1.0
    # worse: u < target - tol
    error = (target - u) - tol
    score = max(0.0, 1.0 - error / 0.5)
    return score


# === block: score_2 (check id='recompute_HER') ===
def score_2(artifact, step, ctx):
    import step as step_def

    target = -0.60
    tol = 0.15
    if not ctx.get('valid'):
        return 0.0
    u = ctx['u_HER']
    if u <= target + tol:
        return 1.0
    # worse: u > target + tol
    error = u - (target + tol)
    score = max(0.0, 1.0 - error / 0.5)
    return score


# === block: score_3 (check id='check_rds') ===
def score_3(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0
    return 1.0 if artifact.get('rate_determining_step') == '*HNO -> *HNOH' else 0.0


# === block: score_4 (check id='json_consistency') ===
def score_4(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0
    if not ctx.get('valid'):
        return 0.0
    no_match = abs(artifact.get('NO_reduction_limiting_potential_V', None) - ctx['u_NO']) <= 1e-2
    her_match = abs(artifact.get('HER_limiting_potential_V', None) - ctx['u_HER']) <= 1e-2
    return 1.0 if no_match and her_match else 0.0


_SCORERS = {
    'csv_structure': score_0,
    'recompute_NORR': score_1,
    'recompute_HER': score_2,
    'check_rds': score_3,
    'json_consistency': score_4,
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
