import os
import json
import csv

# === author imports / helpers ===
import csv, math, os
from collections import defaultdict


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


# === block: score_0 (check id='yap_optimized_lattice') ===
def score_0(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    values = {}
    for row in artifact:
        p = row.get('parameter','').strip()
        if p in gold:
            try:
                v = float(row['value_angstrom'])
                values[p] = v
            except:
                pass
    if len(values) != len(gold):
        return 0.0
    scores = []
    for k, g in gold.items():
        diff = abs(values.get(k, 1e9) - g)
        if diff <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (diff - tol) / (2 * tol))
        scores.append(s)
    return sum(scores) / len(scores)


# === block: score_1 (check id='total_energies') ===
def score_1(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    energies = {}
    for row in artifact:
        sys = row.get('system','').strip()
        if sys in gold:
            try:
                energies[sys] = float(row['total_energy_eV'])
            except:
                pass
    if len(energies) != len(gold):
        return 0.0
    scores = []
    for sys, g in gold.items():
        diff = abs(energies.get(sys, 1e9) - g)
        if diff <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (diff - tol) / (2 * tol))
        scores.append(s)
    return sum(scores) / len(scores)


# === block: score_2 (check id='formation_energy') ===
def score_2(artifact, step, ctx):
    tol = step['tolerance']
    gold = step['target']
    try:
        with open('/app/outputs/total_energies.csv', newline='') as f:
            reader = csv.DictReader(f)
            energies = {}
            for row in reader:
                sys = row.get('system','').strip()
                if sys in ('YAP','Y2O3','Al2O3'):
                    try:
                        energies[sys] = float(row['total_energy_eV'])
                    except:
                        pass
        if len(energies) < 3:
            return 0.0
        delta = energies['YAP'] - 0.5 * energies['Y2O3'] - 0.5 * energies['Al2O3']
    except:
        return 0.0
    diff = abs(delta - gold)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))


# === block: score_3 (check id='mulliken_charges') ===
def score_3(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    data = {}
    for row in artifact:
        atom = row.get('atom','').strip()
        if atom in gold:
            try:
                total = float(row['total'])
                charge = float(row['mulliken_charge'])
                data[atom] = (total, charge)
            except:
                pass
    if len(data) != len(gold):
        return 0.0
    items = []
    for atom, g in gold.items():
        if atom not in data:
            return 0.0
        t, c = data[atom]
        d_t = abs(t - g['total'])
        d_c = abs(c - g['charge'])
        s_t = 1.0 if d_t <= tol else max(0.0, 1.0 - (d_t - tol) / (2 * tol))
        s_c = 1.0 if d_c <= tol else max(0.0, 1.0 - (d_c - tol) / (2 * tol))
        items.append((s_t + s_c) / 2.0)
    return sum(items) / len(items)


# === block: score_4 (check id='mulliken_overlap') ===
def score_4(artifact, step, ctx):
    gold = step['target']
    tol = step['tolerance']
    agent_groups = defaultdict(list)
    for row in artifact:
        bond = row.get('bond','').strip()
        if bond in gold:
            try:
                pop = float(row['population'])
            except:
                continue
            agent_groups[bond].append(pop)
    if len(agent_groups) != len(gold):
        return 0.0
    scores = []
    for bond, gold_pops in gold.items():
        agent_pops = sorted(agent_groups.get(bond, []))
        gold_sorted = sorted(gold_pops)
        if len(agent_pops) != len(gold_sorted):
            scores.append(0.0)
            continue
        diffs = [abs(a - g) for a, g in zip(agent_pops, gold_sorted)]
        elem_scores = []
        for d in diffs:
            if d <= tol:
                elem_scores.append(1.0)
            else:
                elem_scores.append(max(0.0, 1.0 - (d - tol) / (2 * tol)))
        scores.append(sum(elem_scores) / len(elem_scores))
    return sum(scores) / len(scores)


_SCORERS = {
    'yap_optimized_lattice': score_0,
    'total_energies': score_1,
    'formation_energy': score_2,
    'mulliken_charges': score_3,
    'mulliken_overlap': score_4,
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
