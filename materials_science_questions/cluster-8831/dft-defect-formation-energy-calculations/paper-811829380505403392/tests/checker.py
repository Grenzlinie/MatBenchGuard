import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='step_01_lowdin') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    csv_path = os.path.join('/app/outputs', step['output_file'])
    with open(csv_path, newline='') as f:
        rows = list(csv.DictReader(f))
    data = {}
    for r in rows:
        config = r.get('configuration','').strip()
        atom = r.get('atom_type','').strip()
        try:
            pop = float(r.get('population',''))
        except:
            pop = None
        data.setdefault(config, {})[atom] = pop

    if 'SrFeO3' not in data or 'SrFeO2.875' not in data:
        return 0.0
    baseline_atoms = {'Fe','Sr','O'}
    defect_atoms = {'Fe1','Fe2','Fe3','Sr1','Sr2','O1','O2','O3','O4','O5','O6','O7'}
    if not baseline_atoms.issubset(data['SrFeO3']) or not defect_atoms.issubset(data['SrFeO2.875']):
        return 0.0

    gold = step.get('gold_populations')
    tolerance = step.get('pop_tolerance', 0.05)
    matches = 0
    total = 0
    for config_name, atoms_dict in gold.items():
        if config_name not in data:
            continue
        for atom, gval in atoms_dict.items():
            total += 1
            agent_val = data[config_name].get(atom)
            if agent_val is not None and abs(agent_val - gval) <= tolerance:
                matches += 1
    pop_score = matches / total if total > 0 else 0.0

    baseline_fe = data['SrFeO3'].get('Fe')
    baseline_sr = data['SrFeO3'].get('Sr')
    baseline_o  = data['SrFeO3'].get('O')
    if None in (baseline_fe, baseline_sr, baseline_o):
        ordering_score = 0.0
    else:
        fe3_inc = data['SrFeO2.875'].get('Fe3') - baseline_fe
        sr2_inc = data['SrFeO2.875'].get('Sr2') - baseline_sr
        o7_inc  = data['SrFeO2.875'].get('O7') - baseline_o
        ord_tol = step.get('ordering_tolerance', 0.03)
        cond1 = fe3_inc > sr2_inc
        cond2 = abs(sr2_inc - o7_inc) <= ord_tol
        ordering_score = (0.5 if cond1 else 0.0) + (0.5 if cond2 else 0.0)

    return 0.2 * ordering_score + 0.8 * pop_score


# === block: score_1 (check id='step_02_energies') ===
def score_1(artifact, step, ctx):
    import re
    import os

    txt_path = os.path.join('/app/outputs', step['output_file'])
    with open(txt_path) as f:
        content = f.read()

    vf1 = None
    vf2 = None
    m1 = re.search(r'E_vf1\s*=\s*([\d\.]+)\s*eV', content)
    m2 = re.search(r'E_vf2\s*=\s*([\d\.]+)\s*eV', content)
    if m1:
        try: vf1 = float(m1.group(1))
        except: pass
    if m2:
        try: vf2 = float(m2.group(1))
        except: pass

    tol = step.get('energy_tolerance', 0.15)
    gold1 = step.get('gold_E_vf1')
    gold2 = step.get('gold_E_vf2')
    score1 = 1.0 if vf1 is not None and abs(vf1 - gold1) <= tol else 0.0
    score2 = 1.0 if vf2 is not None and abs(vf2 - gold2) <= tol else 0.0
    return (score1 + score2) / 2.0


_SCORERS = {
    'step_01_lowdin': score_0,
    'step_02_energies': score_1,
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
