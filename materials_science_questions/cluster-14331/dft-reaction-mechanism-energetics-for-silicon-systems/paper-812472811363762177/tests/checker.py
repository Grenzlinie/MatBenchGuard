import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math

def is_float(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


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
    reference = None
    # no global ctx needed beyond step-ref; scorers have access to step dict
    return {}


# === block: score_0 (check id='table5_barriers') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    ref = step.get('reference_data', {})
    tolerances = step.get('tolerances', {})
    field_tol = step.get('field_tolerance_label', {})
    total_score = 0.0
    n_fields_total = 0
    for row in rows:
        name = row.get('silicate', '').strip()
        if name not in ref:
            # unknown row; skip or penalize?
            continue
        gold = ref[name]
        row_score = 0.0
        n_fields = 0
        for field, gval in gold.items():
            rval_str = row.get(field, '').strip()
            if rval_str == '' or not is_float(rval_str):
                # field missing, skip (only fields with agent value are scored)
                continue
            rval = float(rval_str)
            tol_label = field_tol.get(field, field)
            tol = tolerances.get(tol_label, 5.0)
            diff = abs(rval - gval)
            if diff <= tol:
                score_field = 1.0
            else:
                score_field = max(0.0, 1.0 - (diff - tol) / (tol))  # gentle decay
            row_score += score_field
            n_fields += 1
        if n_fields > 0:
            total_score += row_score / n_fields
            n_fields_total += 1
    if n_fields_total == 0:
        return 0.0
    return total_score / n_fields_total


# === block: score_1 (check id='cis_trans_gaps') ===
def score_1(artifact, step, ctx):
    data = artifact
    ref = step.get('reference_data', {})
    tolerances = step.get('tolerances', {})
    compounds = ['1b', '1h']
    score_sum = 0.0
    n = 0
    for comp in compounds:
        if comp not in data or comp not in ref:
            continue
        agent = data[comp]
        gold = ref[comp]
        comp_score = 0.0
        count = 0
        # gap
        if 'gap' in agent and is_float(agent['gap']):
            diff = abs(float(agent['gap']) - gold['gap'])
            tol = tolerances.get('gap', 1.0)
            if diff <= tol:
                comp_score += 1.0
            else:
                comp_score += max(0.0, 1.0 - (diff - tol) / tol)
            count += 1
        # check internal consistency: gap should equal cis_energy - trans_energy
        if all(k in agent for k in ('cis_energy', 'trans_energy', 'gap')):
            try:
                cis = float(agent['cis_energy'])
                trans = float(agent['trans_energy'])
                gap_agent = float(agent['gap'])
                if abs(cis - trans - gap_agent) < 0.01:
                    comp_score += 0.2  # small bonus for consistency
            except Exception:
                pass
        # cis_energy and trans_energy closeness
        for ekey in ('cis_energy', 'trans_energy'):
            if ekey in agent and is_float(agent[ekey]):
                diff = abs(float(agent[ekey]) - gold[ekey])
                tol = tolerances.get('energy', 2.0)
                if diff <= tol:
                    comp_score += 0.5
                else:
                    comp_score += 0.5 * max(0.0, 1.0 - (diff - tol) / tol)
                count += 1
        if count > 0:
            score_sum += comp_score / (count + 0.2)  # normalize
            n += 1
    if n == 0:
        return 0.0
    return score_sum / n


# === block: score_2 (check id='somo_homo') ===
def score_2(artifact, step, ctx):
    data = artifact
    ref = step.get('reference_data', {})
    tol_energy = step.get('tolerances', {}).get('orbital_energy', 0.5)
    radicals = [('II_Ph', 'II_Ph'), ('II_Ph_CN', 'II_Ph_CN')]
    score_sum = 0.0
    n = 0
    for key, ref_key in radicals:
        if key not in data or ref_key not in ref:
            continue
        agent_r = data[key]
        gold_r = ref[ref_key]
        # inversion check
        inv_score = 0.0
        if all(k in agent_r for k in ('HOMO_energy', 'SOMO_energy')):
            try:
                homo = float(agent_r['HOMO_energy'])
                somo = float(agent_r['SOMO_energy'])
                if somo < homo:
                    inv_score = 0.5
            except Exception:
                pass
        # energy match
        energy_score = 0.0
        for orb in ('HOMO_energy', 'SOMO_energy'):
            if orb in agent_r and is_float(agent_r[orb]):
                diff = abs(float(agent_r[orb]) - gold_r[orb])
                if diff <= tol_energy:
                    energy_score += 0.25
                else:
                    energy_score += 0.25 * max(0.0, 1.0 - (diff - tol_energy) / tol_energy)
        score_sum += inv_score + energy_score
        n += 1
    if n == 0:
        return 0.0
    return score_sum / n


_SCORERS = {
    'table5_barriers': score_0,
    'cis_trans_gaps': score_1,
    'somo_homo': score_2,
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
