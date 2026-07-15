import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    ctx = {}
    for step in spec['steps']:
        output_file = step.get('output_file')
        if output_file and 'gold_rows' in step:
            ctx[output_file + '_gold'] = {row['base']: row for row in step['gold_rows']}
        if output_file and 'expected_entries' in step:
            ctx[output_file + '_expected_entries'] = step['expected_entries']
    return ctx


# === block: score_0 (check id='energies_check') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx.get('energies.csv_gold', {})
    if not gold_rows:
        return 0.0
    tolerances = {
        'complexation_energy_with_zpe_kcal_per_mol': step.get('tolerance_complex_with_zpe', 0.5),
        'complexation_energy_without_zpe_kcal_per_mol': step.get('tolerance_complex_without_zpe', 0.5),
    }
    # optional: zero-point energy check if tolerance_zpe is defined
    zpe_tol = step.get('tolerance_zpe')
    if zpe_tol is not None:
        tolerances['zero_point_energy_kcal_per_mol'] = zpe_tol
    # total energy tolerances are intentionally excluded to avoid penalizing
    # legitimate code-dependent differences (Gaussian/82 vs Psi4).
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    num_total = 0
    num_pass = 0
    ordering_bases = {'(CH3)2O', 'CH3CH2OH', 'CH3CN', 'CH3CHO'}
    ordering_values = {}
    for row in artifact:
        base = row.get('base', '').strip()
        if base not in gold_rows:
            continue
        gold = gold_rows[base]
        for field, tol in tolerances.items():
            if field not in row or field not in gold:
                continue
            try:
                agent_val = float(row[field])
                gold_val = float(gold[field])
            except (ValueError, TypeError):
                continue
            num_total += 1
            if abs(agent_val - gold_val) <= tol:
                num_pass += 1
        if base in ordering_bases:
            try:
                ordering_values[base] = float(row.get('complexation_energy_without_zpe_kcal_per_mol', None))
            except (ValueError, TypeError):
                pass
    # additional check: the four bases must be within 2.2 kcal/mol
    if len(ordering_values) == 4:
        vals = list(ordering_values.values())
        spread = max(vals) - min(vals)
        num_total += 1
        if spread <= 2.2:
            num_pass += 1
    if num_total == 0:
        return 0.0
    return min(1.0, num_pass / num_total)


# === block: score_1 (check id='populations_check') ===
def score_1(artifact, step, ctx):
    gold_rows = ctx.get('populations.csv_gold', {})
    if not gold_rows:
        return 0.0
    tol_sigma = step.get('tolerance_sigma', 0.01)
    tol_pi = step.get('tolerance_pi', 0.01)
    tol_inplane = step.get('tolerance_in_plane', 0.01)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    num_total = 0
    num_pass = 0
    for row in artifact:
        base = row.get('base', '').strip()
        if base not in gold_rows:
            continue
        gold = gold_rows[base]
        # sigma
        sigma_gold = gold.get('sigma_electron_transfer_to_Al')
        sigma_agent = row.get('sigma_electron_transfer_to_Al')
        if sigma_gold is not None and sigma_agent is not None:
            try:
                if abs(float(sigma_agent) - float(sigma_gold)) <= tol_sigma:
                    num_pass += 1
                num_total += 1
            except (ValueError, TypeError):
                pass
        # pi
        pi_gold = gold.get('pi_electron_transfer_to_Al')
        pi_agent = row.get('pi_electron_transfer_to_Al')
        if pi_gold is not None and pi_agent is not None and pi_agent != '' and pi_gold != '':
            try:
                if abs(float(pi_agent) - float(pi_gold)) <= tol_pi:
                    num_pass += 1
                num_total += 1
            except (ValueError, TypeError):
                pass
        # in-plane pi'
        inp_gold = gold.get('in_plane_pi_electron_transfer')
        inp_agent = row.get('in_plane_pi_electron_transfer')
        if inp_gold is not None and inp_agent is not None and inp_agent != '' and inp_gold != '':
            try:
                if abs(float(inp_agent) - float(inp_gold)) <= tol_inplane:
                    num_pass += 1
                num_total += 1
            except (ValueError, TypeError):
                pass
    if num_total == 0:
        return 0.0
    return min(1.0, num_pass / num_total)


# === block: score_2 (check id='geometries_check') ===
def score_2(artifact, step, ctx):
    expected = ctx.get('geometries.xyz_expected_entries', 12)
    if not isinstance(artifact, str) or not artifact.strip():
        return 0.0
    # count XYZ entries: each entry starts with a line giving atom count, then comment, then coordinates
    lines = artifact.splitlines()
    entries = 0
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == '':
            i += 1
            continue
        try:
            atom_count = int(line)
        except ValueError:
            i += 1
            continue
        # skip comment line
        i += 1
        # skip atom_count lines
        i += atom_count
        entries += 1
    if entries == expected:
        return 1.0
    elif entries > 0:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'energies_check': score_0,
    'populations_check': score_1,
    'geometries_check': score_2,
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
