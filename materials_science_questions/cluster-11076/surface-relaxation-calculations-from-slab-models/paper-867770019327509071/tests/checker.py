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
    gold = spec.get('gold', {})
    tolerances = spec.get('tolerances', {})
    return {'gold': gold, 'tolerances': tolerances}


# === block: score_0 (check id='reproduction_results') ===
def score_0(artifact, step, ctx):
    gold = ctx.get('gold', {})
    tolerances = ctx.get('tolerances', {})
    systems = ['bulk', 'sn_end_monolayer', 'sn_end_bilayer', 'sn_end_trilayer', 's_end_monolayer', 's_end_bilayer', 's_end_trilayer']
    if not isinstance(artifact, dict):
        return 0.0
    correct = 0
    for sys_key in systems:
        if sys_key not in artifact:
            continue
        entry = artifact[sys_key]
        expected = gold.get(sys_key)
        if not expected:
            continue
        if not isinstance(entry, dict):
            continue
        # magnetic state case-insensitive exact match
        if entry.get('magnetic_state', '').strip().lower() != expected['magnetic_state'].strip().lower():
            continue
        # in-plane lattice constant
        if abs(entry.get('in_plane_lattice_const_A', 0) - expected['in_plane_lattice_const_A']) > tolerances.get('in_plane_lattice_const_A', 0.01):
            continue
        # Co layer distance
        exp_dist = expected['co_layer_distance_A']
        agent_dist = entry.get('co_layer_distance_A')
        if exp_dist is None:
            if agent_dist is not None:
                continue
        else:
            if agent_dist is None:
                continue
            if abs(agent_dist - exp_dist) > tolerances.get('co_layer_distance_A', 0.01):
                continue
        # Co magnetic moments
        exp_mom = expected['co_moment_muB']
        agent_mom = entry.get('co_moment_muB')
        if isinstance(agent_mom, (int, float)):
            agent_mom = [agent_mom]
        if not isinstance(agent_mom, list) or len(agent_mom) != len(exp_mom):
            continue
        ok = True
        for a, e in zip(agent_mom, exp_mom):
            if abs(a - e) > tolerances.get('co_moment_muB', 0.005):
                ok = False
                break
        if not ok:
            continue
        # anomalous Hall conductivity
        if abs(entry.get('anomalous_hall_conductivity_e2_per_h', 0) - expected['anomalous_hall_conductivity_e2_per_h']) > tolerances.get('anomalous_hall_conductivity_e2_per_h', 0.1):
            continue
        # anomalous Nernst conductivity
        if abs(entry.get('anomalous_nernst_conductivity_kB_T_5meV', 0) - expected['anomalous_nernst_conductivity_kB_T_5meV']) > tolerances.get('anomalous_nernst_conductivity_kB_T_5meV', 0.1):
            continue
        correct += 1
    return correct / len(systems)


_SCORERS = {
    'reproduction_results': score_0,
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
