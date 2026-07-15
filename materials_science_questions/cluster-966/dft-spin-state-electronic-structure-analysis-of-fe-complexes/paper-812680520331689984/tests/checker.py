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
    return {}


# === block: score_0 (check id='step_geometry') ===
def score_0(artifact, step, ctx):
    import math

    lines = artifact.strip().split('\n')
    if len(lines) < 3:
        return 0.0
    try:
        natoms = int(lines[0])
    except:
        return 0.0
    atoms = []
    for line in lines[2:]:
        if line.strip() == '':
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        el = parts[0]
        x = float(parts[1])
        y = float(parts[2])
        z = float(parts[3])
        atoms.append((el, x, y, z))
    mn = None
    cl = None
    ns = []
    for el, x, y, z in atoms:
        if el == 'Mn':
            mn = (x, y, z)
        elif el == 'Cl':
            cl = (x, y, z)
        elif el == 'N':
            ns.append((x, y, z))
    if mn is None or cl is None or len(ns) < 4:
        return 0.0
    mn_cl_dist = math.sqrt(sum((a - b)**2 for a, b in zip(mn, cl)))
    mn_n_dists = [math.sqrt(sum((a - b)**2 for a, b in zip(mn, n))) for n in ns]
    avg_mn_n = sum(mn_n_dists) / len(mn_n_dists)
    ref_cl = step['params']['experimental_mn_cl']
    ref_n = step['params']['experimental_avg_mn_n']
    tol = step['params']['tolerance_abs']
    score_cl = max(0, 1 - abs(mn_cl_dist - ref_cl) / tol)
    score_n = max(0, 1 - abs(avg_mn_n - ref_n) / tol)
    return (score_cl + score_n) / 2.0


# === block: score_1 (check id='step_mo') ===
def score_1(artifact, step, ctx):
    import json

    if not isinstance(artifact, list):
        return 0.0
    required_labels = [
        'alpha LUMO', 'alpha HOMO', 'alpha HOMO-1', 'alpha HOMO-2', 'alpha HOMO-3', 'alpha HOMO-4'
    ]
    mo_by_label = {}
    for item in artifact:
        label = item.get('mo_label')
        if label in required_labels:
            mo_by_label[label] = item
    gold_list = step['params']['mo_gold']
    gold_by_label = {g['mo_label']: g for g in gold_list}
    energy_tol = step['params']['energy_tolerance_abs']
    percent_tol = step['params']['percent_tolerance_abs']
    total_score = 0.0
    num_properties = 0
    for label in required_labels:
        if label not in mo_by_label:
            num_properties += 4
            continue
        agent_mo = mo_by_label[label]
        gold = gold_by_label[label]
        errors = []
        if 'energy_Hartree' in agent_mo:
            err = abs(agent_mo['energy_Hartree'] - gold['energy_Hartree'])
            errors.append(max(0, 1 - err / energy_tol))
        else:
            errors.append(0)
        for pct_key in ['percent_Mn_d', 'percent_Cl_p', 'percent_porphyrin']:
            if pct_key in agent_mo:
                err = abs(agent_mo[pct_key] - gold[pct_key])
                errors.append(max(0, 1 - err / percent_tol))
            else:
                errors.append(0)
        total_score += sum(errors)
        num_properties += len(errors)
    if num_properties == 0:
        return 0.0
    return total_score / num_properties


_SCORERS = {
    'step_geometry': score_0,
    'step_mo': score_1,
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
