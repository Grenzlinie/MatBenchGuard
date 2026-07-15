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


# === block: score_0 (check id='step_02_dos') ===
def score_0(artifact, step, ctx):
        data = {}
        for row in artifact:
            compound = row.get('compound')
            n_ef = row.get('N_EF')
            if compound and n_ef is not None:
                try:
                    data[compound] = float(n_ef)
                except Exception:
                    pass
        compounds = ['Ba8Si46', 'Ba8Ag6Si40', 'Ba8Au6Si40']
        if not all(c in data for c in compounds):
            return 0.0
        ordering_ok = data['Ba8Si46'] > data['Ba8Ag6Si40'] and data['Ba8Si46'] > data['Ba8Au6Si40']
        if not ordering_ok:
            return 0.0
        cfg = step.get('scoring', {})
        sim_tol = cfg.get('similarity_tolerance', 0.5)
        diff = abs(data['Ba8Ag6Si40'] - data['Ba8Au6Si40'])
        if diff <= sim_tol:
            return 1.0
        return 0.7


# === block: score_1 (check id='step_04_highest_phonon') ===
def score_1(artifact, step, ctx):
    def _score(artifact, step, ctx):
        data = {}
        for row in artifact:
            if row.get('compound'):
                try:
                    data[row['compound']] = float(row['frequency'])
                except:
                    pass
        cfg = step['scoring']
        expected = cfg['expected']
        tolerance = cfg['tolerance']
        scores = []
        for comp in ['Ba8Si46', 'Ba8Ag6Si40', 'Ba8Au6Si40']:
            if comp not in data:
                return 0.0
            tol = tolerance.get(comp, 10.0)
            diff = abs(data[comp] - expected[comp])
            if diff <= tol:
                scores.append(1.0)
            elif diff <= 2 * tol:
                scores.append(0.5)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='step_05_ba_vibrations') ===
def score_2(artifact, step, ctx):
    def _score(artifact, step, ctx):
        data = {}
        for row in artifact:
            key = row.get('compound','') + '_' + row.get('cage_type','')
            try:
                data[key] = float(row['frequency'])
            except:
                pass
        expected = step['scoring']['expected']
        scores = []
        for key, spec in expected.items():
            if key not in data:
                scores.append(0.0)
                continue
            freq = data[key]
            target = spec['target']
            tol = spec['tolerance']
            diff = abs(freq - target)
            if diff <= tol:
                scores.append(1.0)
            elif diff <= 2 * tol:
                scores.append(0.5)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_3 (check id='step_06_el_ph_lambda') ===
def score_3(artifact, step, ctx):
    def _score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        lam = artifact.get('lambda')
        if lam is None:
            return 0.0
        low, high = step['scoring']['range']
        if low <= lam <= high:
            return 1.0
        if 0.7 <= lam <= 1.5:
            return 0.5
        return 0.0


_SCORERS = {
    'step_02_dos': score_0,
    'step_04_highest_phonon': score_1,
    'step_05_ba_vibrations': score_2,
    'step_06_el_ph_lambda': score_3,
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
