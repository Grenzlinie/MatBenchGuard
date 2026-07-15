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


# === block: score_0 (check id='relax_csv') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    csv_path = '/app/outputs/relaxed_parameters.csv'
    if not os.path.exists(csv_path):
        return 0.0

    rows = []
    with open(csv_path, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader, None)
        for line in reader:
            if len(line) < 5:
                continue
            system = line[0].strip()
            comp_x = line[1].strip()
            # distribution = everything between composition_x and the last two numeric fields
            if len(line) > 5:
                dist = ','.join(line[2:-2])
            else:
                dist = line[2].strip()
            a_str = line[-2].strip()
            bond_str = line[-1].strip()
            try:
                a_val = float(a_str)
                bond_val = float(bond_str)
            except ValueError:
                continue
            rows.append({
                'system': system,
                'composition_x': comp_x,
                'distribution': dist,
                'relaxed_a_Angstrom': a_val,
                'MPn_bond_Angstrom': bond_val,
            })

    if len(rows) != 15:
        return 0.0

    tol_a = step.get('tol_a', 0.03)
    tol_bond = step.get('tol_bond', 0.05)
    trend_tol = step.get('trend_tol', 0.03)

    ref_table = step.get('reference_table', [])
    if not ref_table:
        return 0.0
    ref_lookup = {}
    for r in ref_table:
        key = (r['system'], r['composition_x'], r['distribution'])
        ref_lookup[key] = r

    pass_abs = 0
    system_bonds = {'TiP': [], 'VP': [], 'VAs': []}
    bond_ideal_ok = 0

    for row in rows:
        sys = row['system']
        try:
            x = int(row['composition_x'])
        except:
            continue
        dist = row['distribution']
        a_val = row['relaxed_a_Angstrom']
        bond = row['MPn_bond_Angstrom']

        key = (sys, x, dist)
        if key in ref_lookup:
            ref = ref_lookup[key]
            a_err = abs(a_val - ref['a'])
            bond_err = abs(bond - ref['bond'])
            if a_err <= tol_a and bond_err <= tol_bond:
                pass_abs += 1

        if sys in system_bonds:
            system_bonds[sys].append((x, bond, a_val))

        ideal_bond = a_val * math.sqrt(3) / 4.0
        diff = bond - ideal_bond
        if x in (3, 7):
            if diff <= -trend_tol:
                bond_ideal_ok += 1
        elif x in (9, 11):
            if abs(diff) <= trend_tol:
                bond_ideal_ok += 1

    abs_score = pass_abs / 15.0

    mono_ok = True
    for sys, entries in system_bonds.items():
        entries_sorted = sorted(entries, key=lambda e: e[0])
        bonds = [e[1] for e in entries_sorted]
        if len(bonds) < 2:
            continue
        for i in range(len(bonds) - 1):
            if bonds[i] > bonds[i + 1]:
                mono_ok = False
                break
        if not mono_ok:
            break
    mono_score = 1.0 if mono_ok else 0.0
    bond_rel_score = bond_ideal_ok / 15.0
    trend_score = (mono_score + bond_rel_score) / 2.0

    return 0.7 * abs_score + 0.3 * trend_score


_SCORERS = {
    'relax_csv': score_0,
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
