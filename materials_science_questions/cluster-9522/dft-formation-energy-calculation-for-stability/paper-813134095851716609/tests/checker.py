import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict


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


# === block: score_0 (check id='formation') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = defaultdict(lambda: defaultdict(list))
        for row in artifact:
            sys = row.get('system','').strip()
            dtyp = row.get('dumbbell_type','').strip()
            comp = row.get('composition','').strip()
            try:
                e = float(row.get('formation_energy', 0))
            except:
                continue
            data[sys][dtyp].append((comp, e))
        constraints = step.get('constraints', [])
        if not constraints:
            return 0.0
        passed = 0
        for c in constraints:
            t = c['type']
            if t == 'ordering':
                sys = c['system']
                dtyp = c['dumbbell_type']
                expected = c['expected_order']
                entries = data.get(sys, {}).get(dtyp, [])
                if not entries:
                    continue
                sorted_comps = [comp for comp, _ in sorted(entries, key=lambda x: x[1])]
                if sorted_comps == expected:
                    passed += 1
            elif t == 'gap':
                sys = c['system']
                dtyp = c['dumbbell_type']
                comp1 = c['comp1']
                comp2 = c['comp2']
                entries = dict(data.get(sys, {}).get(dtyp, []))
                if comp1 not in entries or comp2 not in entries:
                    continue
                diff = entries[comp2] - entries[comp1]
                if 'abs_less_than' in c:
                    if abs(diff) <= c['abs_less_than']:
                        passed += 1
                else:
                    target = c.get('target_diff')
                    tol = c.get('tolerance', 0.0)
                    if target is not None and abs(diff - target) <= tol:
                        passed += 1
            elif t == 'minimum_type_is_100':
                sys = c['system']
                all_entries = []
                for dtyp, comps in data.get(sys, {}).items():
                    for comp, e in comps:
                        all_entries.append((comp, e, dtyp))
                if not all_entries:
                    continue
                min_energy = min(all_entries, key=lambda x: x[1])[1]
                min_100 = min((e for comp, e, dtyp in all_entries if dtyp == '<100>'), default=None)
                if min_100 is not None and abs(min_energy - min_100) < 1e-9:
                    passed += 1
        return passed / len(constraints)


# === block: score_1 (check id='migration') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = {}
        for row in artifact:
            sys = row.get('system','').strip()
            desc = row.get('process_description','').strip()
            try:
                barrier = float(row.get('barrier_eV', 0))
            except:
                continue
            if sys not in data:
                data[sys] = []
            data[sys].append({'desc': desc, 'barrier': barrier})
        constraints = step.get('constraints', [])
        if not constraints:
            return 0.0
        passed = 0
        for c in constraints:
            t = c['type']
            if t == 'barrier_threshold':
                sys = c['system']
                desc_contains = c['desc_contains']
                op = c['operator']
                thresh = c['threshold']
                absent_ok = c.get('absent_allowed', False)
                matching = [d for d in data.get(sys, []) if desc_contains in d['desc']]
                if not matching:
                    if absent_ok:
                        passed += 1
                    continue
                bar = matching[0]['barrier']
                if (op == '<' and bar < thresh) or (op == '>' and bar > thresh):
                    passed += 1
            elif t == 'any_3d_exists':
                sys = c['system']
                if any('3D' in d['desc'] and d['barrier'] > 0 for d in data.get(sys, [])):
                    passed += 1
            elif t == 'all_positive':
                all_ok = all(d['barrier'] > 0 and d['barrier'] < 2.0 for sys_entries in data.values() for d in sys_entries)
                if all_ok:
                    passed += 1
        return passed / len(constraints)


_SCORERS = {
    'formation': score_0,
    'migration': score_1,
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
