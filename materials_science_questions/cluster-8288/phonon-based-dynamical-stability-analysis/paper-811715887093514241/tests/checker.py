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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold = step.get('config', {}).get('gold_structure', {})
    coord_tol = step['config'].get('coord_tolerance', 0.005)
    latt_tol = step['config'].get('lattice_tolerance_rel', 0.001)
    gold_coords = gold.get('fractional_coordinates', [])
    gold_latt_vecs = gold.get('lattice_vectors_angstrom', [])
    gold_latt_consts = gold.get('lattice_constants_angstrom', [])
    agent_coords = artifact.get('fractional_coordinates', [])
    agent_vecs = artifact.get('lattice_vectors_angstrom', [])
    agent_consts = artifact.get('lattice_constants_angstrom', [])

    # Compare fractional coordinates
    gold_map = {}
    for e in gold_coords:
        el = e['element']
        gold_map.setdefault(el, []).append(e['frac'])
    agent_map = {}
    for e in agent_coords:
        el = e['element']
        agent_map.setdefault(el, []).append(e['frac'])
    max_coord_dev = 0.0
    for el, gf_list in gold_map.items():
        af_list = agent_map.get(el, [])
        if len(af_list) != len(gf_list):
            max_coord_dev = float('inf')
            break
        for gf, af in zip(gf_list, af_list):
            for i in range(3):
                dev = abs(gf[i] - af[i])
                if dev > max_coord_dev: max_coord_dev = dev
    if max_coord_dev <= coord_tol:
        coord_score = 1.0
    else:
        coord_score = max(0.0, 1.0 - (max_coord_dev - coord_tol) / coord_tol)

    # Compare lattice vectors and constants
    def max_rel_error(gold_vecs, agent_vecs):
        err = 0.0
        for i in range(3):
            for j in range(3):
                g = gold_vecs[i][j] if i < len(gold_vecs) and j < len(gold_vecs[i]) else 0.0
                a = agent_vecs[i][j] if i < len(agent_vecs) and j < len(agent_vecs[i]) else 0.0
                if abs(g) < 1e-6:
                    diff = abs(a - g)
                else:
                    diff = abs(a - g) / abs(g)
                if diff > err: err = diff
        return err
    latt_vec_err = max_rel_error(gold_latt_vecs, agent_vecs)
    latt_const_err = 0.0
    if len(gold_latt_consts) == 3 and len(agent_consts) == 3:
        for i in range(3):
            e = abs(agent_consts[i] - gold_latt_consts[i]) / gold_latt_consts[i]
            if e > latt_const_err: latt_const_err = e
    latt_err = max(latt_vec_err, latt_const_err)
    if latt_err <= latt_tol:
        latt_score = 1.0
    else:
        latt_score = max(0.0, 1.0 - (latt_err - latt_tol) / latt_tol)
    score = 0.7 * coord_score + 0.3 * latt_score
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_modes = step['config'].get('gold_modes', [])
    freq_tol = step['config'].get('freq_tolerance', 10.0)
    agent_modes = artifact.get('modes', [])
    agent_ir_active = [m for m in agent_modes if m.get('relative_intensity', 0) > 0.1]
    matched = 0
    for gm in gold_modes:
        gf = gm['frequency_cm1']
        gir = gm['irreducible_representation']
        min_dist = None
        for am in agent_ir_active:
            af = am.get('frequency_cm1', 0)
            air = am.get('irreducible_representation', '')
            if air == gir:
                dist = abs(af - gf)
                if min_dist is None or dist < min_dist:
                    min_dist = dist
        if min_dist is not None and min_dist <= freq_tol:
            matched += 1
    score = 0.0
    if len(gold_modes) > 0:
        score = matched / len(gold_modes)
    return score


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    gold = step['config'].get('gold_dielectric', {})
    rel_tol = step['config'].get('rel_tolerance', 0.20)
    components = ['epsilon_aa', 'epsilon_bb', 'epsilon_cc']
    scores = []
    for name in components:
        agent_val = artifact.get(name, 0.0)
        gold_val = gold.get(name, 1.0)
        if gold_val <= 0:
            scores.append(1.0 if abs(agent_val - gold_val) < 1e-6 else 0.0)
            continue
        rel_err = abs(agent_val - gold_val) / gold_val
        if rel_err <= rel_tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol))
    score = sum(scores) / len(scores)
    return score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
