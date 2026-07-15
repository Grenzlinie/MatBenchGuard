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
        steps = spec.get('steps', spec.get('checks', []))
        targets = {}
        for step in steps:
            sid = step.get('id')
            if 'targets' in step:
                targets[sid] = step['targets']
            else:
                targets[sid] = {}
        return {'targets': targets}


# === block: score_0 (check id='band_gaps_GGA') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv
        gold = ctx['targets']['band_gaps_GGA']
        tol = 0.2
        expected = ['MgSiN2', 'MgGeN2', 'MgSiP2', 'MgGeP2']
        actual = [row['Compound'] for row in artifact]
        if actual != expected:
            return 0.0
        scores = []
        for i, row in enumerate(artifact):
            compound = row['Compound']
            try:
                val = float(row['Eg_GGA (eV)'])
            except:
                return 0.0
            target = gold[compound]['Eg_GGA']
            if val >= target - tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (target - tol - val) / tol)
            scores.append(s)
        return sum(scores) / len(scores)


# === block: score_1 (check id='band_gaps_EV') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import csv
        gold = ctx['targets']['band_gaps_EV']
        tol = 0.2
        expected = ['MgSiN2', 'MgGeN2', 'MgSiP2', 'MgGeP2']
        actual = [row['Compound'] for row in artifact]
        if actual != expected:
            return 0.0
        scores = []
        for i, row in enumerate(artifact):
            compound = row['Compound']
            try:
                val = float(row['Eg_EV (eV)'])
            except:
                return 0.0
            target = gold[compound]['Eg_EV']
            if val >= target - tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (target - tol - val) / tol)
            scores.append(s)
        return sum(scores) / len(scores)


# === block: score_2 (check id='optical_static') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        targets = ctx['targets']['optical_static']
        tols = step.get('tols', {})
        n_abs = tols.get('n_abs', 0.1)
        R_rel = tols.get('R_rel', 0.05)
        crit_abs = tols.get('crit_abs', 0.5)
        expected = ['MgSiN2', 'MgGeN2', 'MgSiP2', 'MgGeP2']
        actual = [row['Compound'] for row in artifact]
        if actual != expected:
            return 0.0
        comp_scores = []
        for row in artifact:
            compound = row['Compound']
            target = targets[compound]
            fields = [
                ('n_par_0', n_abs, 'abs'),
                ('n_perp_0', n_abs, 'abs'),
                ('R_par_0 (%)', R_rel, 'rel'),
                ('R_perp_0 (%)', R_rel, 'rel'),
                ('critical_point (eV)', crit_abs, 'abs')
            ]
            field_scores = []
            for field, tol, mode in fields:
                try:
                    val = float(row[field])
                except:
                    return 0.0
                if mode == 'abs':
                    if abs(val - target[field]) <= tol:
                        field_scores.append(1.0)
                    else:
                        field_scores.append(0.0)
                else:
                    if target[field] != 0:
                        if abs(val - target[field]) <= tol * abs(target[field]):
                            field_scores.append(1.0)
                        else:
                            field_scores.append(0.0)
                    else:
                        if abs(val) <= 1e-9:
                            field_scores.append(1.0)
                        else:
                            field_scores.append(0.0)
            comp_scores.append(sum(field_scores)/len(fields))
        return sum(comp_scores)/len(comp_scores)


_SCORERS = {
    'band_gaps_GGA': score_0,
    'band_gaps_EV': score_1,
    'optical_static': score_2,
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
