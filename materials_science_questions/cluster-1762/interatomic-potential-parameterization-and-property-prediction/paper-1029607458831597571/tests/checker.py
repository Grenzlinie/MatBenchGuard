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


# === block: score_0 (check id='defect_energies') ===
def score_0(artifact, step, ctx):
    fields = step.get('fields', [])
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.10)
    scores = []
    for f in fields:
        if f not in artifact:
            scores.append(0.0)
            continue
        val = artifact[f]
        ref = gold[f]
        if val <= ref:
            scores.append(1.0)
        elif val <= ref + tol:
            scores.append(1.0 - (val - ref) / tol)
        else:
            scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='migration_energies') ===
def score_1(artifact, step, ctx):
    local_gold = step['local_hops_gold']
    long_gold = step['long_range_gold']
    dist_tol = step['distance_tolerance']
    eng_tol = step['energy_tolerance']
    local_scores = []
    for hop, ref in local_gold.items():
        if 'local_hops' not in artifact or hop not in artifact['local_hops']:
            local_scores.append(0.0)
            continue
        hop_data = artifact['local_hops'][hop]
        if 'distance_angstrom' in hop_data:
            d = hop_data['distance_angstrom']
            rd = ref['distance_angstrom']
            if abs(d - rd) <= dist_tol:
                local_scores.append(1.0)
            else:
                local_scores.append(0.0)
        else:
            local_scores.append(0.0)
        if 'activation_energy_eV' in hop_data:
            e = hop_data['activation_energy_eV']
            re = ref['activation_energy_eV']
            if e <= re:
                local_scores.append(1.0)
            elif e <= re + eng_tol:
                local_scores.append(1.0 - (e - re) / eng_tol)
            else:
                local_scores.append(0.0)
        else:
            local_scores.append(0.0)
    long_scores = []
    for path, ref in long_gold.items():
        if 'long_range_pathways' not in artifact or path not in artifact['long_range_pathways']:
            long_scores.append(0.0)
            continue
        path_data = artifact['long_range_pathways'][path]
        if 'overall_activation_energy_eV' in path_data:
            oe = path_data['overall_activation_energy_eV']
            roe = ref['overall_activation_energy_eV']
            if oe <= roe:
                long_scores.append(1.0)
            elif oe <= roe + eng_tol:
                long_scores.append(1.0 - (oe - roe) / eng_tol)
            else:
                long_scores.append(0.0)
        else:
            long_scores.append(0.0)
        seq_key = 'hop_sequence_eV'
        if seq_key in path_data and seq_key in ref:
            agent_seq = path_data[seq_key]
            ref_seq = ref[seq_key]
            if isinstance(agent_seq, list) and len(agent_seq) == len(ref_seq):
                for i in range(len(agent_seq)):
                    ae = agent_seq[i]
                    re = ref_seq[i]
                    if ae <= re:
                        long_scores.append(1.0)
                    elif ae <= re + eng_tol:
                        long_scores.append(1.0 - (ae - re) / eng_tol)
                    else:
                        long_scores.append(0.0)
            else:
                long_scores.append(0.0)
        else:
            long_scores.append(0.0)
    all_scores = local_scores + long_scores
    return sum(all_scores) / len(all_scores) if all_scores else 0.0


# === block: score_2 (check id='dopant_solutions') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance']
    scores = []
    for category in ['monovalent', 'trivalent', 'tetravalent']:
        for elem, ref in gold[category].items():
            if category not in artifact or elem not in artifact[category]:
                scores.append(0.0)
                continue
            val = artifact[category][elem]
            if val <= ref:
                scores.append(1.0)
            elif val <= ref + tol:
                scores.append(1.0 - (val - ref) / tol)
            else:
                scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'defect_energies': score_0,
    'migration_energies': score_1,
    'dopant_solutions': score_2,
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
