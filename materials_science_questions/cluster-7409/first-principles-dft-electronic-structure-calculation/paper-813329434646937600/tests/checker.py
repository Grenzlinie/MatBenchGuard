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


# === block: score_0 (check id='field_check') ===
def score_0(artifact, step, ctx):
    return 1.0 if artifact and all(k in artifact for k in ['bulk_bandgap_eV','slab3_t2_bandgap_eV','slab6_t2_bandgap_eV','slab9_t2_bandgap_eV','surface_energies']) else 0.0


# === block: score_1 (check id='bandgaps') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_bandgaps', {})
    tol_bulk = step['tolerances']['bulk']
    tol_slab = step['tolerances']['slab']
    key_to_gold = {
        'bulk_bandgap_eV': 'bulk',
        'slab3_t2_bandgap_eV': 'slab3_t2',
        'slab6_t2_bandgap_eV': 'slab6_t2',
        'slab9_t2_bandgap_eV': 'slab9_t2'
    }
    def score_gap(name, tol):
        val = artifact.get(name, None)
        gold_key = key_to_gold.get(name)
        if val is None or gold_key is None or gold_key not in gold:
            return 0.0
        dev = abs(val - gold[gold_key])
        if dev <= tol:
            return 1.0
        decay = (dev - tol) / (2*tol)
        return max(0.0, 1.0 - decay)
    scores = [
        score_gap('bulk_bandgap_eV', tol_bulk),
        score_gap('slab3_t2_bandgap_eV', tol_slab),
        score_gap('slab6_t2_bandgap_eV', tol_slab),
        score_gap('slab9_t2_bandgap_eV', tol_slab)
    ]
    return sum(scores) / len(scores)


# === block: score_2 (check id='surface_order') ===
def score_2(artifact, step, ctx):
    entries = artifact.get('surface_energies', [])
    if not isinstance(entries, list):
        return 0.0
    term_map = {}
    for e in entries:
        if e.get('n_layers') == 3 and 'E_surface_Jpm2' in e:
            t = e.get('termination_layer')
            if t in (1,2,3):
                term_map[t] = e['E_surface_Jpm2']
    if not (1 in term_map and 2 in term_map and 3 in term_map):
        return 0.0
    ok = term_map[2] < term_map[1] and term_map[2] < term_map[3]
    return 1.0 if ok else 0.0


# === block: score_3 (check id='surface_formula') ===
def score_3(artifact, step, ctx):
    entries = artifact.get('surface_energies', [])
    if not isinstance(entries, list) or len(entries)==0:
        return 0.0
    A = step['area_A_angstrom2']
    factor = step['hartree_to_Jpm2_factor']
    tol = step['surface_energy_tolerance_Jpm2']
    lo, hi = step['magnitude_range']
    tot = 0.0
    n = 0
    for e in entries:
        n_layers = e.get('n_layers')
        k = e.get('k')
        E_slab = e.get('E_slab_Ha')
        E_bulk = e.get('E_bulk_per_repeat_unit_Ha')
        reported = e.get('E_surface_Jpm2')
        if None in (n_layers, k, E_slab, E_bulk, reported):
            continue
        # k check
        if n_layers == 3:
            k_ok = 1.0 if k == 1 else 0.0
        elif n_layers == 6:
            k_ok = 1.0 if k == 2 else 0.0
        else:
            k_ok = 1.0  # not required
        # recalculate surface energy
        try:
            calc = (E_slab - k * E_bulk) / (2*A) * factor
        except Exception:
            continue
        # formula match
        formula_ok = 1.0 if abs(reported - calc) <= tol else 0.0
        # magnitude check
        mag_ok = 1.0 if lo <= calc <= hi else 0.0
        entry_score = (k_ok + formula_ok + mag_ok) / 3.0
        tot += entry_score
        n += 1
    if n == 0:
        return 0.0
    return tot / n


_SCORERS = {
    'field_check': score_0,
    'bandgaps': score_1,
    'surface_order': score_2,
    'surface_formula': score_3,
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
