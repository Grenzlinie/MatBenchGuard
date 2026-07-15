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
    def prepare(outputs_dir, spec):
        fit_step = next(s for s in spec['steps'] if s['id'] == 'step_01_fit')
        mass_step = next(s for s in spec['steps'] if s['id'] == 'step_02_masses')
        ctx = {
            'fit_groups': fit_step['target']['groups'],
            'fit_tol_a': fit_step['tolerances']['a_dyne_cm'],
            'fit_tol_b': fit_step['tolerances']['b_dyne_cm2'],
            'mass_elements': mass_step['target']['elements'],
            'mass_tol': mass_step['tolerances']['m_star_over_m']
        }
        return ctx


# === block: score_0 (check id='step_01_fit') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_groups = ctx['fit_groups']
        tol_a = ctx['fit_tol_a']
        tol_b = ctx['fit_tol_b']
        # artifact is list of dicts from csv.DictReader
        rows_by_group = {r['Group']: r for r in artifact}
        n = len(gold_groups)
        if n == 0:
            return 0.0
        passed = 0
        for group_name, gold in gold_groups.items():
            row = rows_by_group.get(group_name)
            if row is None:
                continue
            try:
                a = float(row['a_dyne_cm'])
                b = float(row['b_dyne_cm2'])
            except (ValueError, KeyError, TypeError):
                continue
            a_ok = abs(a - gold['a_dyne_cm']) <= tol_a
            b_ok = abs(b - gold['b_dyne_cm2']) <= tol_b
            if a_ok and b_ok:
                passed += 1
        return passed / n


# === block: score_1 (check id='step_02_masses') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_elements = ctx['mass_elements']
        tol = ctx['mass_tol']
        rows_by_elem = {r['Element']: r for r in artifact}
        n = len(gold_elements)
        if n == 0:
            return 0.0
        passed = 0
        for elem, gold_val in gold_elements.items():
            row = rows_by_elem.get(elem)
            if row is None:
                continue
            try:
                val = float(row['m_star_over_m'])
            except (ValueError, KeyError, TypeError):
                continue
            if abs(val - gold_val) <= tol:
                passed += 1
        return passed / n


_SCORERS = {
    'step_01_fit': score_0,
    'step_02_masses': score_1,
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
