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
    gold_rows = spec.get('gold_rows', [])
    expected_counts = spec.get('expected_counts', [])
    # build lookup by (model,adsorbate,config_id) for fast matching
    gold_lookup = {}
    for r in gold_rows:
        key = (r['model'], r['adsorbate'], r['configuration_id'])
        gold_lookup[key] = r
    # also build expected counts dict
    count_lookup = {}
    for c in expected_counts:
        count_lookup[(c['model'], c['adsorbate'])] = c['count']
    return {'gold_lookup': gold_lookup, 'count_lookup': count_lookup, 'gold_rows': gold_rows}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    count_lookup = ctx['count_lookup']
    agent_counts = {}
    for row in artifact:
        key = (row.get('model',''), row.get('adsorbate',''))
        agent_counts[key] = agent_counts.get(key, 0) + 1
    # check all expected counts
    matched = 0
    for key, expected in count_lookup.items():
        if agent_counts.get(key, 0) == expected:
            matched += 1
    return matched / len(count_lookup) if count_lookup else 1.0


# === block: score_1 (check id='bounds_check') ===
def score_1(artifact, step, ctx):
    all_good = True
    for row in artifact:
        ads = row.get('delta_E_ads_kcalmol', None)
        gap = row.get('delta_E_GAP_eV', None)
        if ads is not None and ads != '' and ads != 'NaN':
            try:
                ads_val = float(ads)
                if ads_val > 0.0:
                    all_good = False
                    break
            except (ValueError, TypeError):
                all_good = False
                break
        if gap is not None and gap != '' and gap != 'NaN':
            try:
                gap_val = float(gap)
                if gap_val < 0.0:
                    all_good = False
                    break
            except (ValueError, TypeError):
                all_good = False
                break
    return 1.0 if all_good else 0.0


# === block: score_2 (check id='ads_energy_accuracy') ===
def score_2(artifact, step, ctx):
    gold_lookup = ctx['gold_lookup']
    tol = step.get('tolerance', 2.0)

    # collect gold energies per (model, adsorbate)
    gold_groups = {}
    for key, gold in gold_lookup.items():
        if gold['adsorbate'] == 'bare':
            continue
        gkey = (gold['model'], gold['adsorbate'])
        gold_groups.setdefault(gkey, []).append(gold['delta_E_ads_kcalmol'])

    for energies in gold_groups.values():
        energies.sort()

    # collect agent energies per (model, adsorbate)
    agent_groups = {}
    for row in artifact:
        if row.get('adsorbate', '') == 'bare':
            continue
        try:
            energy = float(row.get('delta_E_ads_kcalmol'))
        except (ValueError, TypeError):
            continue
        akey = (row.get('model', ''), row.get('adsorbate', ''))
        agent_groups.setdefault(akey, []).append(energy)

    for energies in agent_groups.values():
        energies.sort()

    total = sum(len(gold_ens) for gold_ens in gold_groups.values())
    passed = 0
    for gkey, gold_ens in gold_groups.items():
        agent_ens = agent_groups.get(gkey, [])
        n = min(len(gold_ens), len(agent_ens))
        for i in range(n):
            if abs(gold_ens[i] - agent_ens[i]) <= tol:
                passed += 1

    return passed / total if total > 0 else 0.0


# === block: score_3 (check id='gap_accuracy') ===
def score_3(artifact, step, ctx):
    gold_groups = {}
    for r in ctx['gold_rows']:
        key = (r['model'], r['adsorbate'])
        gold_groups.setdefault(key, []).append(r['delta_E_GAP_eV'])

    for gaps in gold_groups.values():
        gaps.sort()

    agent_groups = {}
    for row in artifact:
        try:
            gap = float(row.get('delta_E_GAP_eV'))
        except (ValueError, TypeError):
            continue
        akey = (row.get('model',''), row.get('adsorbate',''))
        agent_groups.setdefault(akey, []).append(gap)

    for gaps in agent_groups.values():
        gaps.sort()

    tol = step.get('tolerance', 0.5)
    total = sum(len(gaps) for gaps in gold_groups.values())
    passed = 0
    for key, gold_gaps in gold_groups.items():
        agent_gaps = agent_groups.get(key, [])
        n = min(len(gold_gaps), len(agent_gaps))
        for i in range(n):
            if abs(gold_gaps[i] - agent_gaps[i]) <= tol:
                passed += 1

    return passed / total if total > 0 else 0.0


# === block: score_4 (check id='strongest_match') ===
def score_4(artifact, step, ctx):
    gold_rows = ctx['gold_rows']
    tol = step.get('tolerance', 1.0)

    # Find minimum gold adsorption energy for each model/adsorbate (excluding bare)
    gold_min = {}
    for row in gold_rows:
        if row['adsorbate'] == 'bare':
            continue
        key = (row['model'], row['adsorbate'])
        energy = row['delta_E_ads_kcalmol']
        if key not in gold_min or energy < gold_min[key]:
            gold_min[key] = energy

    # Collect agent's adsorption energies per model/adsorbate
    agent_energies = {}
    for row in artifact:
        adsorbate = row.get('adsorbate', '')
        if adsorbate == 'bare':
            continue
        try:
            energy = float(row.get('delta_E_ads_kcalmol'))
        except (ValueError, TypeError):
            continue
        key = (row.get('model', ''), adsorbate)
        if key not in agent_energies:
            agent_energies[key] = []
        agent_energies[key].append(energy)

    total = len(gold_min)
    matched = 0
    for key, gold_energy in gold_min.items():
        agent_vals = agent_energies.get(key, [])
        if not agent_vals:
            continue
        agent_min = min(agent_vals)
        if abs(agent_min - gold_energy) <= tol:
            matched += 1

    return matched / total if total > 0 else 0.0


_SCORERS = {
    'shape_check': score_0,
    'bounds_check': score_1,
    'ads_energy_accuracy': score_2,
    'gap_accuracy': score_3,
    'strongest_match': score_4,
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
