import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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
    exp = {"a": 6.09, "b": 9.57, "c": 4.67}
    lattice_tol_percent = 5.0
    degeneracy_tol_Hartree = 0.01
    degeneracy_tol_eV = 0.01 * 27.2114   # 1 Hartree = 27.2114 eV
    return {
        "exp": exp,
        "lattice_tol_percent": lattice_tol_percent,
        "degeneracy_tol_Hartree": degeneracy_tol_Hartree,
        "degeneracy_tol_eV": degeneracy_tol_eV
    }


# === block: score_0 (check id='step_lattice_accuracy') ===
def score_0(artifact, step, ctx):
    try:
        entries = artifact
        if not isinstance(entries, list):
            return 0.0
        exp = ctx['exp']
        tol = ctx['lattice_tol_percent']
        o_entries = [e for e in entries if e.get('structure_id') == 'O']
        if len(o_entries) == 0:
            return 0.0
        passed = 0
        for e in o_entries:
            lat = e.get('lattice_parameters_angstrom', {})
            a = float(lat.get('a'))
            b = float(lat.get('b'))
            c = float(lat.get('c'))
            da = abs(a - exp['a']) / exp['a'] * 100
            db = abs(b - exp['b']) / exp['b'] * 100
            dc = abs(c - exp['c']) / exp['c'] * 100
            if da <= tol and db <= tol and dc <= tol:
                passed += 1
        return passed / len(o_entries) if o_entries else 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='step_energy_ordering') ===
def score_1(artifact, step, ctx):
    try:
        entries = artifact
        if not isinstance(entries, list):
            return 0.0
        from collections import defaultdict
        by_func = defaultdict(list)
        for e in entries:
            func = e.get('functional')
            if func:
                by_func[func].append(e)
        required_funcs = {'LDA','PBE','B3LYP'}
        if set(by_func.keys()) != required_funcs:
            return 0.0
        for func in required_funcs:
            group = {e['structure_id']: e['total_energy_per_fu'] for e in by_func[func] if 'structure_id' in e}
            if 'O' not in group or 'H1' not in group or 'H2' not in group:
                return 0.0
            o_e = group['O']
            h1_e = group['H1']
            h2_e = group['H2']
            if not (o_e < h1_e and o_e < h2_e):
                return 0.0
        return 1.0
    except Exception:
        return 0.0


# === block: score_2 (check id='step_degeneracy') ===
def score_2(artifact, step, ctx):
    try:
        entries = artifact
        if not isinstance(entries, list):
            return 0.0
        from collections import defaultdict
        by_func = defaultdict(list)
        for e in entries:
            func = e.get('functional')
            if func:
                by_func[func].append(e)
        required_funcs = {'LDA','PBE','B3LYP'}
        if set(by_func.keys()) != required_funcs:
            return 0.0
        for func in required_funcs:
            group = {}
            for e in by_func[func]:
                sid = e.get('structure_id')
                if sid in ('H1','H2'):
                    unit = e.get('energy_unit','Hartree')
                    energy = e['total_energy_per_fu']
                    group[sid] = (energy, unit)
            if 'H1' not in group or 'H2' not in group:
                return 0.0
            e1, u1 = group['H1']
            e2, u2 = group['H2']
            if u1 != u2:
                return 0.0
            diff = abs(e1 - e2)
            if u1 == 'eV':
                tol = ctx['degeneracy_tol_eV']
            else:
                tol = ctx['degeneracy_tol_Hartree']
            if diff >= tol:
                return 0.0
        return 1.0
    except Exception:
        return 0.0


# === block: score_3 (check id='step_schema_completeness') ===
def score_3(artifact, step, ctx):
    try:
        entries = artifact
        if not isinstance(entries, list) or len(entries) != 9:
            return 0.0
        expected_ids = {'O','H1','H2'}
        expected_funcs = {'LDA','PBE','B3LYP'}
        seen = set()
        for e in entries:
            sid = e.get('structure_id')
            func = e.get('functional')
            if sid not in expected_ids or func not in expected_funcs:
                return 0.0
            pair = (sid, func)
            if pair in seen:
                return 0.0
            seen.add(pair)
            if 'lattice_parameters_angstrom' not in e or 'atomic_positions' not in e or 'total_energy_per_fu' not in e or 'energy_unit' not in e:
                return 0.0
            lat = e['lattice_parameters_angstrom']
            if not all(k in lat for k in ('a','b','c')):
                return 0.0
            if sid in ('H1','H2'):
                if not (abs(lat['b'] - lat['a']) < 1e-6 and abs(lat['c'] - lat['a']) < 1e-6):
                    return 0.0
            if e['energy_unit'] not in ('eV','Hartree'):
                return 0.0
        if seen != {(sid, func) for sid in expected_ids for func in expected_funcs}:
            return 0.0
        return 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'step_lattice_accuracy': score_0,
    'step_energy_ordering': score_1,
    'step_degeneracy': score_2,
    'step_schema_completeness': score_3,
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
