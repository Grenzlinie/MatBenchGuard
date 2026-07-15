import os
import json
import csv

# === author imports / helpers ===
import os
import csv
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
    steps = [s for s in spec.get('steps', []) if s.get('output_file') == 'total_energies.csv']
    if not steps:
        raise ValueError('missing recompute step')
    step = steps[0]
    gold = step['gold_values']
    tol = step['tolerance_abs_eV']
    scale = step.get('partial_credit_scale_eV', 1.0)
    return {'gold': gold, 'tol_abs': tol, 'partial_scale': scale}


# === block: score_0 (check id='recompute_doping_energies') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts from total_energies.csv
    ctx = ctx
    tol = ctx.get('tol_abs', 0.5)
    scale = ctx.get('partial_scale', 1.0)
    # Use the paper-reported gold values from the grading spec
    gold = ctx.get('gold', {})
    if not gold:
        return 0.0
    energies = {}
    for row in artifact:
        name = row['cluster_name'].strip()
        try:
            e = float(row['total_energy_eV'])
        except (ValueError, KeyError):
            return 0.0
        energies[name] = e
    required = ['Si17', 'Si17H36', 'Si15P2', 'Si15B2', 'Si15P2H36', 'Si15B2H36']
    if not all(k in energies for k in required):
        return 0.0
    E = energies
    def compute_doping(imp):
        if imp == 'P':
            E_X = E['Si15P2']
            E_XH = E['Si15P2H36']
        else:
            E_X = E['Si15B2']
            E_XH = E['Si15B2H36']
        dE1 = E_X - E['Si17']
        dE2 = E_XH - E['Si17H36']
        dEE = dE2 - dE1
        return dE1, dE2, dEE
    scores = []
    for imp in ['P', 'B']:
        dE1, dE2, dEE = compute_doping(imp)
        g = gold.get(imp, {})
        if not g:
            return 0.0
        for key, comp in [('ΔE1', dE1), ('ΔE2', dE2), ('ΔEE', dEE)]:
            target = g.get(key)
            if target is None:
                return 0.0
            err = abs(comp - target)
            if err <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (err - tol) / scale)
            scores.append(s)
    return round(sum(scores) / len(scores), 4)


# === block: score_1 (check id='consistency_doping_energies') ===
def score_1(artifact, step, ctx):
    import csv, os
    total_path = '/app/outputs/total_energies.csv'
    if not os.path.exists(total_path):
        return 0.0
    with open(total_path, newline='') as f:
        total_rows = list(csv.DictReader(f))
    energies = {}
    for row in total_rows:
        name = row['cluster_name'].strip()
        try:
            e = float(row['total_energy_eV'])
        except (ValueError, KeyError):
            return 0.0
        energies[name] = e
    required = ['Si17', 'Si17H36', 'Si15P2', 'Si15B2', 'Si15P2H36', 'Si15B2H36']
    if not all(k in energies for k in required):
        return 0.0
    E = energies
    def compute_doping(imp):
        if imp == 'P':
            E_X = E['Si15P2']
            E_XH = E['Si15P2H36']
        else:
            E_X = E['Si15B2']
            E_XH = E['Si15B2H36']
        dE1 = E_X - E['Si17']
        dE2 = E_XH - E['Si17H36']
        dEE = dE2 - dE1
        return dE1, dE2, dEE
    tol_rel = step.get('tolerance_rel', 1e-3)
    doping_rows = {r['impurity']: r for r in artifact}
    for imp in ['P', 'B']:
        if imp not in doping_rows:
            return 0.0
        row = doping_rows[imp]
        try:
            rep_dE1 = float(row['ΔE1_eV'])
            rep_dE2 = float(row['ΔE2_eV'])
            rep_dEE = float(row['ΔEE_eV'])
        except (ValueError, KeyError):
            return 0.0
        calc_dE1, calc_dE2, calc_dEE = compute_doping(imp)
        for rep, calc in [(rep_dE1, calc_dE1), (rep_dE2, calc_dE2), (rep_dEE, calc_dEE)]:
            if abs(calc) < 1e-12:
                if abs(rep - calc) > 1e-12:
                    return 0.0
            else:
                if abs(rep - calc) / max(abs(calc), 1e-12) > tol_rel:
                    return 0.0
    return 1.0


_SCORERS = {
    'recompute_doping_energies': score_0,
    'consistency_doping_energies': score_1,
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
