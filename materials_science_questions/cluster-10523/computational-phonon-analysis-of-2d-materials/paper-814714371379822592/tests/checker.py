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


# === block: score_0 (check id='dielectric_check') ===
def score_0(artifact, step, ctx):
    def scorer(artifact, step):
        gold = step.get('gold', {})
        tol_abs = step.get('tolerance_abs', 3.0)
        tol_rel = step.get('tolerance_rel', 0.10)
        data = artifact.get('dielectric_constants', {})
        score = 0.0
        n_compounds = len(gold)
        n_fields = 3
        for comp, gc in gold.items():
            if comp not in data:
                continue
            comp_data = data[comp]
            for field in ('average', 'epsilon_11', 'epsilon_33'):
                if field not in comp_data:
                    continue
                val = comp_data[field]
                if val is None or not isinstance(val, (int, float)):
                    continue
                exp = gc[field]
                diff = abs(val - exp)
                if diff <= tol_abs or (exp != 0 and diff / abs(exp) <= tol_rel):
                    score += 1.0 / (n_compounds * n_fields)
        return min(score, 1.0)


# === block: score_1 (check id='phonon_check') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step):
        gold = step.get('gold', {})
        tol_abs = step.get('tolerance_abs', 5.0)
        data = artifact.get('phonon_frequencies', {})
        total = 0
        count = 0
        for comp, spec in gold.items():
            if comp not in data:
                continue
            ir = data[comp].get('IR_active', {})
            eu = ir.get('E_u', [])
            if not isinstance(eu, list):
                continue
            idx = spec['index']
            if idx >= len(eu):
                continue
            val = eu[idx]
            diff = abs(val - spec['value'])
            if diff <= tol_abs:
                total += 1
            count += 1
        if count == 0:
            return 0.0
        return total / count


# === block: score_2 (check id='consistency_check') ===
def score_2(artifact, step, ctx):
    def scorer(artifact, step):
        gold = step.get('gold', {})
        tol = step.get('tolerance_abs', 0.5)
        per_atom = artifact.get('per_atom_dielectric_contributions', {})
        total = 0
        count = 0
        for comp, gs in gold.items():
            if comp not in per_atom:
                continue
            atoms = per_atom[comp]
            if not isinstance(atoms, dict):
                continue
            sum_11 = sum(v.get('epsilon_i_11', 0.0) for v in atoms.values() if isinstance(v, dict))
            sum_33 = sum(v.get('epsilon_i_33', 0.0) for v in atoms.values() if isinstance(v, dict))
            diff_11 = abs(sum_11 - gs['sum_11'])
            diff_33 = abs(sum_33 - gs['sum_33'])
            if diff_11 <= tol:
                total += 1
            if diff_33 <= tol:
                total += 1
            count += 2
        if count == 0:
            return 0.0
        return total / count


_SCORERS = {
    'dielectric_check': score_0,
    'phonon_check': score_1,
    'consistency_check': score_2,
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
