import os
import json
import csv

# === author imports / helpers ===
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
    return spec


# === block: score_0 (check id='step_02_u_distribution') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts with keys T_K, species, mole_fraction
    checks = step.get('checks', [])
    if not rows or not checks:
        return 0.0
    passed = 0
    total = len(checks)
    for c in checks:
        if c['type'] == 'species_range':
            sp = c['species']
            t_min = float(c['T_min']); t_max = float(c['T_max'])
            lo = float(c['min_mole']); hi = float(c['max_mole'])
            vals = []
            for r in rows:
                if r['species'] == sp:
                    tk = float(r['T_K'])
                    if tk >= t_min and tk <= t_max:
                        vals.append(float(r['mole_fraction']))
            if not vals:
                if lo == 0.0:
                    passed += 1
            else:
                if lo > 0.0:
                    if any(v >= lo and v <= hi for v in vals):
                        passed += 1
                else:
                    if all(v <= hi for v in vals):
                        passed += 1
        elif c['type'] == 'sum_near_one':
            tol = float(c['tolerance'])
            groups = {}
            for r in rows:
                tk = float(r['T_K'])
                groups.setdefault(tk, 0.0)
                groups[tk] += float(r['mole_fraction'])
            if not groups:
                continue
            ok = sum(1 for s in groups.values() if abs(s-1.0) <= tol)
            if ok/len(groups) >= 0.8:
                passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_1 (check id='step_03_am_distribution') ===
def score_1(artifact, step, ctx):
    rows = artifact
    checks = step.get('checks', [])
    if not rows or not checks:
        return 0.0
    passed = 0
    total = len(checks)
    for c in checks:
        if c['type'] == 'species_range':
            sp = c['species']
            t_min = float(c['T_min']); t_max = float(c['T_max'])
            lo = float(c['min_mole']); hi = float(c['max_mole'])
            vals = []
            for r in rows:
                if r['species'] == sp:
                    tk = float(r['T_K'])
                    if tk >= t_min and tk <= t_max:
                        vals.append(float(r['mole_fraction']))
            if not vals:
                if lo == 0.0:
                    passed += 1
            else:
                if lo > 0.0:
                    if any(v >= lo and v <= hi for v in vals):
                        passed += 1
                else:
                    if all(v <= hi for v in vals):
                        passed += 1
        elif c['type'] == 'sum_near_one':
            tol = float(c['tolerance'])
            groups = {}
            for r in rows:
                tk = float(r['T_K'])
                groups.setdefault(tk, 0.0)
                groups[tk] += float(r['mole_fraction'])
            if not groups:
                continue
            ok = sum(1 for s in groups.values() if abs(s-1.0) <= tol)
            if ok/len(groups) >= 0.8:
                passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_2 (check id='step_04_pu_distribution') ===
def score_2(artifact, step, ctx):
    rows = artifact
    checks = step.get('checks', [])
    if not rows or not checks:
        return 0.0
    passed = 0
    total = len(checks)
    for c in checks:
        if c['type'] == 'species_range':
            sp = c['species']
            t_min = float(c['T_min']); t_max = float(c['T_max'])
            lo = float(c['min_mole']); hi = float(c['max_mole'])
            vals = []
            for r in rows:
                if r['species'] == sp:
                    tk = float(r['T_K'])
                    if tk >= t_min and tk <= t_max:
                        vals.append(float(r['mole_fraction']))
            if not vals:
                if lo == 0.0:
                    passed += 1
            else:
                if lo > 0.0:
                    if any(v >= lo and v <= hi for v in vals):
                        passed += 1
                else:
                    if all(v <= hi for v in vals):
                        passed += 1
        elif c['type'] == 'sum_near_one':
            tol = float(c['tolerance'])
            groups = {}
            for r in rows:
                tk = float(r['T_K'])
                groups.setdefault(tk, 0.0)
                groups[tk] += float(r['mole_fraction'])
            if not groups:
                continue
            ok = sum(1 for s in groups.values() if abs(s-1.0) <= tol)
            if ok/len(groups) >= 0.8:
                passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_3 (check id='step_05_equilibrium_constants') ===
def score_3(artifact, step, ctx):
    rows = artifact  # list of dicts with keys reaction_number, coefficient_a, coefficient_b
    gold = step.get('gold_constants', [])
    if not rows or not gold:
        return 0.0
    total = len(gold)
    if total == 0:
        return 0.0
    t_a = 5.0
    t_b = 5000.0
    passed = 0
    for g in gold:
        rn = int(g['reaction_number'])
        match = None
        for r in rows:
            if int(r['reaction_number']) == rn:
                match = r
                break
        if match is None:
            continue
        try:
            a = float(match['coefficient_a'])
            b = float(match['coefficient_b'])
        except (ValueError, KeyError):
            continue
        if abs(a - float(g['a'])) <= t_a and abs(b - float(g['b'])) <= t_b:
            passed += 1
    return passed / total


_SCORERS = {
    'step_02_u_distribution': score_0,
    'step_03_am_distribution': score_1,
    'step_04_pu_distribution': score_2,
    'step_05_equilibrium_constants': score_3,
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
