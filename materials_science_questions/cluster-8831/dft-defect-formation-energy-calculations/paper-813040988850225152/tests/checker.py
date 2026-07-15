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
    gold = spec.get('gold', {})
    tols_fe = spec['steps'][0]['tolerances']
    tols_props = spec['steps'][1]['tolerances']
    return {'gold_fe': gold.get('formation_energies_reference', []), 'gold_props': gold.get('properties_reference', []), 'tols_fe': tols_fe, 'tols_props': tols_props}


# === block: score_0 (check id='step_formation_energies') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list): return 0.0

    gold_fe = ctx['gold_fe']
    tols_fe = ctx['tols_fe']

    # build gold lookup
    gold_lookup = {}
    for g in gold_fe:
        gold_lookup[(g['system'], g['phase'])] = g

    # numeric closeness (total_energy is excluded because absolute DFT energies
    # shift by several eV across plane‑wave codes; only the physical differences
    # – formation_helmholtz, formation_O_rich, formation_V_rich – are compared)
    numeric_matches = 0
    total_entries = len(gold_fe)
    for entry in artifact:
        key = (entry.get('system'), entry.get('phase'))
        gref = gold_lookup.get(key)
        if gref is None:
            continue
        ok = True
        for field in ['formation_helmholtz','formation_O_rich','formation_V_rich']:
            a_val = entry.get(field)
            g_val = gref.get(field)
            if g_val is None and a_val is None:
                continue
            if g_val is None or a_val is None:
                ok = False
                break
            if abs(a_val - g_val) > tols_fe[field]:
                ok = False
                break
        if ok:
            numeric_matches += 1
    numeric_score = numeric_matches / total_entries if total_entries > 0 else 0.0

    # structural checks
    struct_score = 0.0
    checks = 3

    # 1. all formation_helmholtz negative
    helmholtz_neg = all(e.get('formation_helmholtz', 0) < 0 for e in artifact if e.get('formation_helmholtz') is not None)
    if helmholtz_neg:
        struct_score += 1

    # 2. P@V is the lowest formation_O_rich among all doped entries
    doped = [e for e in artifact if e.get('formation_O_rich') is not None]
    if doped:
        min_fe = min(doped, key=lambda x: x['formation_O_rich'])
        if min_fe.get('system') == 'P@V':
            struct_score += 1

    # 3. ordering M@V < M@i < M@O under O-rich for each dopant/phase
    ordering_ok = True
    for dopant in ['P','As','Bi']:
        for ph in ['R','M1']:
            vals = {}
            for e in artifact:
                if e.get('system') == f'{dopant}@V' and e.get('phase') == ph:
                    vals['@V'] = e.get('formation_O_rich')
                if e.get('system') == f'{dopant}@i' and e.get('phase') == ph:
                    vals['@i'] = e.get('formation_O_rich')
                if e.get('system') == f'{dopant}@O' and e.get('phase') == ph:
                    vals['@O'] = e.get('formation_O_rich')
            if None not in (vals.get('@V'), vals.get('@i'), vals.get('@O')):
                if not (vals['@V'] < vals['@i'] < vals['@O']):
                    ordering_ok = False
                    break
        if not ordering_ok:
            break
    if ordering_ok:
        struct_score += 1

    struct_score = struct_score / checks
    return 0.5 * numeric_score + 0.5 * struct_score


# === block: score_1 (check id='step_properties') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list): return 0.0

    gold_props = ctx['gold_props']
    tols_props = ctx['tols_props']

    # build gold lookup
    gold_lookup = {g['system']: g for g in gold_props}

    # numeric closeness
    numeric_matches = 0
    total_entries = len(gold_props)
    for entry in artifact:
        sys = entry.get('system')
        gref = gold_lookup.get(sys)
        if gref is None:
            continue
        ok = True
        for field in ['Eg2','Tc']:
            a_val = entry.get(field)
            g_val = gref.get(field)
            if a_val is None or g_val is None:
                ok = False
                break
            if abs(a_val - g_val) > tols_props[field]:
                ok = False
                break
        if ok:
            numeric_matches += 1
    numeric_score = numeric_matches / total_entries if total_entries > 0 else 0.0

    # structural checks
    struct_score = 0.0
    checks = 3

    # 1. Band gaps: all Eg2 < pure VO2 Eg2
    pure_entry = gold_lookup.get('pure')
    if pure_entry and all(e.get('Eg2', float('inf')) < pure_entry['Eg2'] for e in artifact if e.get('system') != 'pure' and e.get('Eg2') is not None):
        struct_score += 1

    # 2. Bi-doped systems have the smallest Eg2
    bi_systems = [e for e in artifact if e.get('system','').startswith('Bi') and e.get('Eg2') is not None]
    non_bi = [e for e in artifact if not e.get('system','').startswith('Bi') and e.get('system') != 'pure' and e.get('Eg2') is not None]
    if bi_systems and non_bi:
        max_bi = max(e['Eg2'] for e in bi_systems)
        min_other = min(e['Eg2'] for e in non_bi)
        if max_bi < min_other:
            struct_score += 1

    # 3. Tc ordering: Bi@O < Bi@i < Bi@V < 340
    bi_tc = {}
    for e in artifact:
        if e.get('system') in ('Bi@O','Bi@i','Bi@V') and e.get('Tc') is not None:
            bi_tc[e['system']] = e['Tc']
    if len(bi_tc) == 3:
        if bi_tc.get('Bi@O') < bi_tc.get('Bi@i') < bi_tc.get('Bi@V') < 340:
            struct_score += 1

    struct_score = struct_score / checks
    return 0.5 * numeric_score + 0.5 * struct_score


_SCORERS = {
    'step_formation_energies': score_0,
    'step_properties': score_1,
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
