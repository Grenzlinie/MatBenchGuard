import os
import json
import csv

# === author imports / helpers ===
import math

def _within_rel(value, gold, rel_tol, abs_min=0.0):
    if gold == 0:
        return abs(value) <= abs_min + 1e-12
    return abs(value - gold) / abs(gold) <= rel_tol + 1e-12

def _match_null_or_rel(name, value, gold, rel_tol, abs_min=0.0):
    if gold is None:
        return value is None
    if value is None:
        return False
    return _within_rel(value, gold, rel_tol, abs_min)


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
    spec = load_artifact('/tests/grading_spec.json')
    ctx = {
        'expected_structural': spec['expected_structural'],
        'expected_electronic': spec['expected_electronic'],
        'expected_mechanical': spec['expected_mechanical'],
        'expected_dielectric': spec['expected_dielectric']
    }
    return ctx


# === block: score_0 (check id='structural') ===
def score_0(artifact, step, ctx):
    # helper functions defined locally to avoid NameError
    def _within_rel(value, gold, rel_tol, abs_min=0.0):
        if gold == 0:
            return abs(value) <= abs_min + 1e-12
        return abs(value - gold) / abs(gold) <= rel_tol + 1e-12

    def _match_null_or_rel(name, value, gold, rel_tol, abs_min=0.0):
        if gold is None:
            return value is None
        if value is None:
            return False
        return _within_rel(value, gold, rel_tol, abs_min)

    if not isinstance(artifact, list):
        return 0.0
    exp = ctx['expected_structural']
    tols = exp['tolerances']
    gold_systems = exp['systems']
    agent_map = {item['system']: item for item in artifact if 'system' in item}
    total_checks = 0
    passed = 0
    for name, gold in gold_systems.items():
        if name not in agent_map:
            continue
        a_val = agent_map[name].get('a')
        b_val = agent_map[name].get('b')
        total_checks += 2
        if a_val is not None and _within_rel(a_val, gold['a'], tols['rel_tol'], 0.001):
            passed += 1
        if b_val is not None and _within_rel(b_val, gold['b'], tols['rel_tol'], 0.001):
            passed += 1
        mismatch_agent = agent_map[name].get('lattice_mismatch')
        mismatch_gold = gold['lattice_mismatch']
        total_checks += 1
        if _match_null_or_rel(name, mismatch_agent, mismatch_gold, tols['rel_tol'], 0.01):
            passed += 1
        inter_agent = agent_map[name].get('interlayer_distance')
        inter_gold = gold['interlayer_distance']
        total_checks += 1
        if _match_null_or_rel(name, inter_agent, inter_gold, tols['rel_tol'], 0.01):
            passed += 1
        bind_agent = agent_map[name].get('binding_energy_per_atom')
        bind_gold = gold['binding_energy_per_atom']
        total_checks += 1
        if bind_gold is None:
            if bind_agent is None:
                passed += 1
        else:
            if bind_agent is not None and abs(bind_agent - bind_gold) <= tols.get('binding_abs_tol', 0.01):
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='electronic') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    exp = ctx['expected_electronic']
    band_tol = exp['band_gap_abs_tol']
    schottky_tol = exp['schottky_abs_tol']
    gold_systems = exp['systems']
    agent_map = {item['system']: item for item in artifact if 'system' in item}
    total = 0
    passed = 0
    # Score per system
    for name, gold in gold_systems.items():
        if name not in agent_map:
            continue
        a = agent_map[name]
        # band_gap
        total += 1
        ag = a.get('band_gap')
        gg = gold['band_gap']
        if gg is not None and ag is not None and abs(ag - gg) <= band_tol:
            passed += 1
        elif gg is None and ag is None:
            passed += 1
        # band_gap_type
        total += 1
        aty = a.get('band_gap_type')
        gty = gold['band_gap_type']
        if (aty == gty) or (aty is None and gty is None):
            passed += 1
        # schottky
        sh_agent = a.get('schottky_barrier_height')
        sh_gold = gold['schottky_barrier_height']
        st_agent = a.get('schottky_barrier_type')
        st_gold = gold['schottky_barrier_type']
        if sh_gold is not None:
            total += 1
            if sh_agent is not None and abs(sh_agent - sh_gold) <= schottky_tol:
                passed += 1
            total += 1
            if st_agent == st_gold:
                passed += 1
    # band_gap_vs_field for the two semiconducting heterostructures
    field_exp = exp.get('band_gap_vs_field', {})
    for sys_name, cfg in field_exp.items():
        if sys_name not in agent_map:
            continue
        field_arr = agent_map[sys_name].get('band_gap_vs_field')
        if not isinstance(field_arr, list):
            continue
        fields_expected = cfg['fields']
        # Check presence of correct fields and values
        if len(field_arr) != len(fields_expected):
            continue
        for entry in field_arr:
            f = entry.get('field')
            g = entry.get('band_gap')
            if f not in fields_expected or g is None:
                continue
            total += 1
            cond = cfg.get('conditions', {})
            metal_at = cond.get('metal_at', [])
            nonzero_at = cond.get('nonzero_at', [])
            nonzero_all = cond.get('nonzero_all', False)
            if f in metal_at:
                if g <= 0.1:
                    passed += 1
            elif f in nonzero_at:
                if g > 0.1:
                    passed += 1
            elif f == 0.0:
                eg = cfg['expected_at_zero']
                if abs(g - eg) <= band_tol:
                    passed += 1
                else:
                    pass
            elif nonzero_all:
                if g > 0.1:
                    passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='mechanical') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    exp = ctx['expected_mechanical']
    rel_tol = exp['rel_tol']
    gold_systems = exp['systems']
    agent_map = {item['system']: item for item in artifact if 'system' in item}
    total = 0
    passed = 0
    fields = ['Cx','Cy','vx','vy']
    for name, gold in gold_systems.items():
        if name not in agent_map:
            continue
        a = agent_map[name]
        for f in fields:
            total += 1
            av = a.get(f)
            gv = gold[f]
            if av is not None and _within_rel(av, gv, rel_tol, 0.001):
                passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_3 (check id='dielectric') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    exp = ctx['expected_dielectric']
    rel_tol = exp['rel_tol']
    gold_systems = exp['systems']
    agent_map = {item['system']: item for item in artifact if 'system' in item}
    total = 0
    passed = 0
    for name, gold in gold_systems.items():
        if name not in agent_map:
            continue
        a = agent_map[name]
        for key in ['lateral_eps','vertical_eps']:
            total += 1
            av = a.get(key)
            gv = gold[key]
            if av is not None and _within_rel(av, gv, rel_tol, 0.001):
                passed += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'structural': score_0,
    'electronic': score_1,
    'mechanical': score_2,
    'dielectric': score_3,
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
