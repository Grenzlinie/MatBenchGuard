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
    import json
    spec = json.loads(open('/tests/grading_spec.json').read())
    gold = spec.get('gold_data', {})
    eg_gold = gold.get('eg_gold', {})
    eb_gold = gold.get('eb_gold', {})
    return {'eg_gold': eg_gold, 'eb_gold': eb_gold}


# === block: score_0 (check id='ordering') ===
def score_0(artifact, step, ctx):
    artifact_list = artifact  # list of dicts
    order_sequence = ['3,6-MMCB-OCP','3,6-MMCB-BCO','3,6-MMCB-SDP','3,6-MMCB-SCP','3,6-MMCB-TCP','3,6-MMCB-TDP','3,6-MMCB-BCS','3,6-MMCB-BCT']
    phases = ['gas', 'sol']
    score_total = 0.0
    for phase in phases:
        rows = [r for r in artifact_list if r.get('phase','') == phase]
        if len(rows) != 9:
            continue
        eg_map = {r['monomer']: float(r['Eg_eV']) for r in rows}
        # constraints: OCP < SDP, BCO < SDP, SDP < SCP, SCP < TCP, TCP < TDP, TDP < BCS, BCS < BCT
        constraints = [
            ('3,6-MMCB-OCP', '3,6-MMCB-SDP'),
            ('3,6-MMCB-BCO', '3,6-MMCB-SDP'),
            ('3,6-MMCB-SDP', '3,6-MMCB-SCP'),
            ('3,6-MMCB-SCP', '3,6-MMCB-TCP'),
            ('3,6-MMCB-TCP', '3,6-MMCB-TDP'),
            ('3,6-MMCB-TDP', '3,6-MMCB-BCS'),
            ('3,6-MMCB-BCS', '3,6-MMCB-BCT')
        ]
        satisfied = 0
        for a, b in constraints:
            if a in eg_map and b in eg_map and eg_map[a] < eg_map[b]:
                satisfied += 1
        score_total += satisfied / len(constraints)
    return score_total / len(phases)


# === block: score_1 (check id='eg_tolerance') ===
def score_1(artifact, step, ctx):
    artifact_list = artifact
    eg_gold = ctx['eg_gold']
    tolerance = 0.15
    count = 0
    for row in artifact_list:
        monomer = row['monomer']
        phase = row['phase']
        if phase in eg_gold and monomer in eg_gold[phase]:
            diff = abs(float(row['Eg_eV']) - eg_gold[phase][monomer])
            if diff <= tolerance:
                count += 1
    return count / max(len(artifact_list), 1)


# === block: score_2 (check id='dihedral_range') ===
def score_2(artifact, step, ctx):
    artifact_list = artifact
    count = 0
    for row in artifact_list:
        phi = float(row['phi_deg'])
        if 130.0 <= phi <= 160.0:
            count += 1
    return count / max(len(artifact_list), 1)


# === block: score_3 (check id='bond_anomaly') ===
def score_3(artifact, step, ctx):
    artifact_list = artifact
    count = 0
    for row in artifact_list:
        monomer = row['monomer']
        d = float(row['d_BL_A'])
        if monomer == '3,6-MMCB-SDP':
            if 1.52 <= d <= 1.56:
                count += 1
        else:
            if 1.46 <= d <= 1.50:
                count += 1
    return count / max(len(artifact_list), 1)


# === block: score_4 (check id='eb_tolerance') ===
def score_4(artifact, step, ctx):
    artifact_list = artifact
    eb_gold = ctx['eb_gold']
    tolerance = 0.5
    count = 0
    for row in artifact_list:
        monomer = row['monomer']
        phase = row['phase']
        if phase in eb_gold and monomer in eb_gold[phase]:
            diff = abs(float(row['EB_eV']) - eb_gold[phase][monomer])
            if diff <= tolerance:
                count += 1
    return count / max(len(artifact_list), 1)


_SCORERS = {
    'ordering': score_0,
    'eg_tolerance': score_1,
    'dihedral_range': score_2,
    'bond_anomaly': score_3,
    'eb_tolerance': score_4,
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
