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


# === block: score_0 (check id='lattice') ===
def score_0(artifact, step, ctx):
    rows = artifact
    target = step['target']
    tol = step['tolerance_percent'] / 100.0
    polymorphs = ['alpha', 'beta', 'gamma', 'alpha_prime']
    rowmap = {r['polymorph'].strip().lower(): r for r in rows}
    count = 0
    for poly in polymorphs:
        if poly not in rowmap:
            continue
        t = target[poly]
        r = rowmap[poly]
        ok = True
        for key in ['a', 'b', 'c', 'volume_per_fu']:
            try:
                val = float(r.get(key))
            except (TypeError, ValueError):
                ok = False
                break
            ref = t[key]
            if ref == 0:
                if abs(val - ref) > 1e-9:
                    ok = False
                    break
            elif abs(val - ref) > tol * abs(ref):
                ok = False
                break
        if ok:
            count += 1
    return count / len(polymorphs) if polymorphs else 0.0


# === block: score_1 (check id='formation_enthalpy_values') ===
def score_1(artifact, step, ctx):
    data = artifact
    target = step['target']
    tol = step['tolerance_abs_kJ']
    keys = ['alpha', 'beta', 'gamma', 'alpha_prime']
    count = 0
    for k in keys:
        if k not in data:
            continue
        try:
            val = float(data[k]['formation_enthalpy_kJ_per_mol_H2'])
        except (KeyError, TypeError, ValueError):
            continue
        ref = target[k]
        if abs(val - ref) <= tol:
            count += 1
    return count / len(keys) if keys else 0.0


# === block: score_2 (check id='formation_enthalpy_order') ===
def score_2(artifact, step, ctx):
    data = artifact
    keys = ['alpha', 'beta', 'gamma', 'alpha_prime']
    vals = {}
    tol = step.get('tolerance_for_comparison', 0.5)
    for k in keys:
        if k not in data:
            return 0.0
        try:
            vals[k] = float(data[k]['formation_enthalpy_kJ_per_mol_H2'])
        except (KeyError, TypeError, ValueError):
            return 0.0
    # Order must satisfy: vals['beta'] <= vals['alpha_prime'] <= vals['alpha'] <= vals['gamma']
    # Using a small slack to avoid floating-point noise flipping the order
    if vals['beta'] <= vals['alpha_prime'] + tol and vals['alpha_prime'] <= vals['alpha'] + tol and vals['alpha'] <= vals['gamma'] + tol:
        return 1.0
    return 0.0


# === block: score_3 (check id='band_gaps_values') ===
def score_3(artifact, step, ctx):
    data = artifact
    target = step['target']
    tolerances = step['tolerances']
    polymorphs = ['alpha', 'beta', 'gamma', 'alpha_prime']
    count = 0
    total = 0
    for poly in polymorphs:
        if poly not in data:
            continue
        for func in ['GGA', 'TBmBJ']:
            total += 1
            try:
                val = float(data[poly]['GGA_PBE']) if func == 'GGA' else float(data[poly]['TBmBJ'])
            except (KeyError, TypeError, ValueError):
                continue
            ref = target[poly][func]
            if abs(val - ref) <= tolerances[func]:
                count += 1
    return count / total if total else 0.0


# === block: score_4 (check id='band_gaps_order') ===
def score_4(artifact, step, ctx):
    data = artifact
    polymorphs = ['alpha', 'beta', 'gamma', 'alpha_prime']
    if 'beta' not in data:
        return 0.0
    try:
        beta_tb = float(data['beta']['TBmBJ'])
    except (KeyError, TypeError, ValueError):
        return 0.0

    for poly in polymorphs:
        if poly == 'beta' or poly not in data:
            continue
        try:
            other_tb = float(data[poly]['TBmBJ'])
        except (KeyError, TypeError, ValueError):
            return 0.0
        if other_tb >= beta_tb:
            return 0.0
    return 1.0


# === block: score_5 (check id='bader_charges') ===
def score_5(artifact, step, ctx):
    data = artifact
    target = step['target']
    tol = step['tolerance_abs']
    keys = ['alpha', 'beta', 'gamma']
    total_checks = 0
    passed = 0
    for k in keys:
        if k not in data or k not in target:
            continue
        t = target[k]
        d = data[k]
        # Check Al
        total_checks += 1
        try:
            al_val = float(d['Al'])
            if abs(al_val - t['Al']) <= tol:
                passed += 1
        except (KeyError, TypeError, ValueError):
            pass
        # Check H
        t_h = t['H']
        d_h = d.get('H')
        if d_h is None:
            continue
        if isinstance(t_h, list):
            # Expect array of length 4 (gamma)
            if not isinstance(d_h, list):
                continue
            if len(d_h) != len(t_h):
                continue
            for i, (t_val, d_val) in enumerate(zip(t_h, d_h)):
                total_checks += 1
                try:
                    if abs(float(d_val) - t_val) <= tol:
                        passed += 1
                except (TypeError, ValueError):
                    pass
        else:
            total_checks += 1
            try:
                if abs(float(d_h) - t_h) <= tol:
                    passed += 1
            except (TypeError, ValueError):
                pass
    return passed / total_checks if total_checks else 0.0


_SCORERS = {
    'lattice': score_0,
    'formation_enthalpy_values': score_1,
    'formation_enthalpy_order': score_2,
    'band_gaps_values': score_3,
    'band_gaps_order': score_4,
    'bader_charges': score_5,
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
