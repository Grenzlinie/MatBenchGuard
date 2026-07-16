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
    steps = spec.get('steps', spec.get('checks', []))
    ctx = {}
    for step in steps:
        if step['id'] == 'step2':
            ctx['gold'] = step['config']['gold']
            ctx['tolerances'] = step['config']['tolerances']
            break
    return ctx


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = ctx.get('gold', {})
    if not gold:
        return 0.0
    tol = ctx.get('tolerances', {})
    energy_tol = tol.get('energy', 2.0)
    int_abs = tol.get('intensity_abs', 0.02)
    int_rel = tol.get('intensity_rel', 0.2)
    p_rel = tol.get('p_ratio_rel', 0.2)
    p_abs = tol.get('p_ratio_abs', 0.1)
    coarse = tol.get('coarse_energy_tol', 5.0)

    def within_energy(e1, e2):
        if e1 is None or e2 is None:
            return False
        return abs(e1 - e2) <= energy_tol

    def within_intensity(comp, gold_val):
        if comp is None or gold_val is None:
            return False
        if gold_val < 0.1:
            return abs(comp - gold_val) <= int_abs
        else:
            return abs(comp - gold_val) / max(abs(gold_val), 1e-9) <= int_rel

    def within_polarization(comp, gold_val):
        if comp is None or gold_val is None:
            return False
        if abs(comp - gold_val) <= p_abs:
            return True
        denom = max(abs(gold_val), 1e-9)
        return abs(comp - gold_val) / denom <= p_rel

    # build list of gold entries with type info
    entries = []
    # NTS
    try:
        nts = artifact.get('nts', [])
    except Exception:
        nts = []
    for block in gold.get('nts', []):
        l = block['l']
        for ed in block.get('ed', []):
            entries.append({'l': l, 'type': 'ed', 'energy': ed['energy'], 'intensity': ed['intensity'], 'extra': None})
        for ep in block.get('ep', []):
            entries.append({'l': l, 'type': 'ep', 'energy': ep['energy'], 'intensity': ep['intensity'], 'extra': None})

    # TS
    try:
        ts_artifact = artifact.get('ts', {})
    except Exception:
        ts_artifact = {}
    gold_ts = gold.get('ts', {})

    for edp in gold_ts.get('edp_bands', []):
        entries.append({'l': edp['l'], 'type': 'edp', 'energy': edp['E'], 'intensity': None,
                       'extra': {'I_a': edp['I_a'], 'I_b': edp['I_b'], 'p_ab': edp['p_ab'], 'M_imp': edp['M_imp']}})

    for fine in gold_ts.get('ed_ep_fine', []):
        entries.append({'l': fine['l'], 'type': fine['type'].lower(), 'energy': fine['E_j'], 'intensity': None,
                       'extra': {'I_a': fine['I_a'], 'I_b': fine['I_b'], 'p_ab': fine['p_ab']}})

    # collect agent items
    def collect_agent_items():
        agent_entries = []
        # nts
        for block in nts:
            try:
                l = int(block.get('l', -1))
            except Exception:
                continue
            ed_list = block.get('ed', [])
            ep_list = block.get('ep', [])
            if not isinstance(ed_list, list):
                ed_list = []
            if not isinstance(ep_list, list):
                ep_list = []
            for e in ed_list:
                try:
                    energy = float(e.get('energy', 0))
                    intensity = float(e.get('intensity', 0))
                except Exception:
                    continue
                agent_entries.append({'l': l, 'type': 'ed', 'energy': energy, 'intensity': intensity, 'extra': None})
            for e in ep_list:
                try:
                    energy = float(e.get('energy', 0))
                    intensity = float(e.get('intensity', 0))
                except Exception:
                    continue
                agent_entries.append({'l': l, 'type': 'ep', 'energy': energy, 'intensity': intensity, 'extra': None})
        # ts edp
        edp_list = ts_artifact.get('edp_bands', [])
        if not isinstance(edp_list, list):
            edp_list = []
        for edp in edp_list:
            try:
                l = int(edp.get('l', -1))
                E = float(edp.get('E', 0))
                I_a = float(edp.get('I_a', 0))
                I_b = float(edp.get('I_b', 0))
                p_ab = float(edp.get('p_ab', 0))
                M_imp = float(edp.get('M_imp', 0))
            except Exception:
                continue
            agent_entries.append({'l': l, 'type': 'edp', 'energy': E, 'intensity': None,
                                  'extra': {'I_a': I_a, 'I_b': I_b, 'p_ab': p_ab, 'M_imp': M_imp}})
        # ts fine
        fine_list = ts_artifact.get('ed_ep_fine', [])
        if not isinstance(fine_list, list):
            fine_list = []
        for fine in fine_list:
            try:
                l = int(fine.get('l', -1))
                typ = str(fine.get('type', '')).upper()
                if typ not in ('ED', 'EP'):
                    continue
                E_j = float(fine.get('E_j', 0))
                I_a = float(fine.get('I_a', 0))
                I_b = float(fine.get('I_b', 0))
                p_ab = float(fine.get('p_ab', 0))
            except Exception:
                continue
            agent_entries.append({'l': l, 'type': typ.lower(), 'energy': E_j, 'intensity': None,
                                  'extra': {'I_a': I_a, 'I_b': I_b, 'p_ab': p_ab}})
        return agent_entries

    agent_items = collect_agent_items()
    num_gold = len(entries)
    if num_gold == 0:
        return 1.0
    used_agent = [False] * len(agent_items)
    matched = 0
    for gold_entry in entries:
        best_idx = -1
        best_dist = float('inf')
        for i, a in enumerate(agent_items):
            if a['l'] != gold_entry['l'] or a['type'] != gold_entry['type']:
                continue
            d = abs(a['energy'] - gold_entry['energy']) if a['energy'] is not None and gold_entry['energy'] is not None else float('inf')
            if d < best_dist and d <= coarse:
                best_dist = d
                best_idx = i
        if best_idx == -1 or used_agent[best_idx]:
            continue
        # check fine tolerances
        a = agent_items[best_idx]
        if gold_entry['type'] in ('ed', 'ep'):
            if not within_energy(a['energy'], gold_entry['energy']):
                continue
            if not within_intensity(a['intensity'], gold_entry['intensity']):
                continue
        elif gold_entry['type'] == 'edp':
            if not within_energy(a['energy'], gold_entry['energy']):
                continue
            g = gold_entry['extra']
            a_extra = a.get('extra', {})
            if not within_intensity(a_extra.get('I_a', 0), g['I_a']):
                continue
            if not within_intensity(a_extra.get('I_b', 0), g['I_b']):
                continue
            if not within_polarization(a_extra.get('p_ab', 0), g['p_ab']):
                continue
            if abs(a_extra.get('M_imp', 0) - g['M_imp']) > 1e-6:  # M_imp is exact input parameter
                continue
        else:  # ts ed/ep fine
            if not within_energy(a['energy'], gold_entry['energy']):
                continue
            g = gold_entry['extra']
            a_extra = a.get('extra', {})
            if not within_intensity(a_extra.get('I_a', 0), g['I_a']):
                continue
            if not within_intensity(a_extra.get('I_b', 0), g['I_b']):
                continue
            if not within_polarization(a_extra.get('p_ab', 0), g['p_ab']):
                continue
        matched += 1
        used_agent[best_idx] = True

    return matched / num_gold


_SCORERS = {
    'step2': score_0,
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
