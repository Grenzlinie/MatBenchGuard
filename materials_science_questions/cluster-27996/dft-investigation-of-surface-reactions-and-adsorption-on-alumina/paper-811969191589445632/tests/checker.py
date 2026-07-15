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
    return {}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    import math

    # artifact is the loaded JSON for this step
    if artifact is None or 'systems' not in artifact:
        return 0.0

    systems_list = artifact['systems']
    # index by system name (case-insensitive, strip)
    by_name = {}
    for s in systems_list:
        name = s.get('system', '').strip()
        if name:
            by_name[name.lower()] = s

    gold = step.get('gold', {})
    expected_systems = gold.get('expected_systems', [])
    interaction_gold = gold.get('interaction_energies', {})
    distance_gold = gold.get('distances', {})
    fragment_map = gold.get('complex_fragment_map', {})
    tols = step.get('tolerances', {})
    e_tol = tols.get('interaction_energy_kjmol', 10.0)
    d_tol = tols.get('distance_angstrom', 0.1)

    # 1) Presence check (small weight)
    missing_systems = [s for s in expected_systems if s.lower() not in by_name]
    presence_score = 1.0 - len(missing_systems) / len(expected_systems) if expected_systems else 1.0

    # 2) Interaction energies (weight 0.5)
    energy_scores = []
    for comp_name, frags in fragment_map.items():
        comp_key = comp_name.lower()
        comp = by_name.get(comp_key)
        if comp is None:
            energy_scores.append(0.0)
            continue
        frag_energies = []
        for fname in frags:
            f = by_name.get(fname.lower())
            if f is None:
                frag_energies = None
                break
            frag_energies.append(f['total_energy_kjmol'])
        if frag_energies is None:
            energy_scores.append(0.0)
            continue
        inter_energy = comp['total_energy_kjmol'] - sum(frag_energies)
        target = interaction_gold.get(comp_name, 0.0)
        # check within tolerance
        if abs(inter_energy - target) <= e_tol:
            energy_scores.append(1.0)
        else:
            # partial credit based on deviation beyond tolerance
            deviation = abs(inter_energy - target)
            energy_scores.append(max(0.0, 1.0 - (deviation - e_tol) / (2 * e_tol)))

    energy_score_total = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0

    # 3) Distances (weight 0.3)
    distance_scores = []
    for sys_name, dists in distance_gold.items():
        sys = by_name.get(sys_name.lower())
        if sys is None:
            distance_scores.append(0.0)
            continue
        key_distances = sys.get('key_distances', {})
        if not key_distances:
            distance_scores.append(0.0)
            continue
        sys_dist_scores = []
        for dname, gold_val in dists.items():
            agent_val = key_distances.get(dname)
            if agent_val is None:
                sys_dist_scores.append(0.0)
            elif abs(agent_val - gold_val) <= d_tol:
                sys_dist_scores.append(1.0)
            else:
                sys_dist_scores.append(0.0)
        distance_scores.append(sum(sys_dist_scores) / len(sys_dist_scores) if sys_dist_scores else 0.0)

    distance_score_total = sum(distance_scores) / len(distance_scores) if distance_scores else 0.0

    # 4) Relative trends (weight 0.2)
    trend_score = 0.0
    # Collect interaction energies again for trend evaluation
    comp_energies = {}
    for comp_name, frags in fragment_map.items():
        comp = by_name.get(comp_name.lower())
        if comp is None:
            continue
        frag_energies = [by_name[f.lower()]['total_energy_kjmol'] for f in frags if f.lower() in by_name]
        if len(frag_energies) != len(frags):
            continue
        comp_energies[comp_name] = comp['total_energy_kjmol'] - sum(frag_energies)

    correct_trends = 0
    total_trends = 0

    # a) BF3_DEE interaction energy < BF3_PDEE (more negative)
    if 'BF3_DEE' in comp_energies and 'BF3_PDEE' in comp_energies:
        if comp_energies['BF3_DEE'] < comp_energies['BF3_PDEE']:
            correct_trends += 1
        total_trends += 1
    # b) OH+_PDME interaction energy < OH_PDME
    if 'OH+_PDME' in comp_energies and 'OH_PDME' in comp_energies:
        if comp_energies['OH+_PDME'] < comp_energies['OH_PDME']:
            correct_trends += 1
        total_trends += 1
    # c) OH-_PDME interaction energy < OH+_PDME and OH-_PDME < OH_PDME
    if 'OH-_PDME' in comp_energies:
        oh_minus = comp_energies['OH-_PDME']
        if 'OH+_PDME' in comp_energies and oh_minus < comp_energies['OH+_PDME']:
            correct_trends += 1
        if 'OH_PDME' in comp_energies and oh_minus < comp_energies['OH_PDME']:
            correct_trends += 1
        total_trends += 2

    trend_score = correct_trends / total_trends if total_trends > 0 else 0.0

    # combine with weights: presence 0.05, energy 0.5, distance 0.25, trend 0.2
    final_score = presence_score * 0.05 + energy_score_total * 0.5 + distance_score_total * 0.25 + trend_score * 0.2
    # ensure within [0,1]
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'step_02': score_0,
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
