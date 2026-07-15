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


# === block: score_0 (check id='electronic_properties') ===
def score_0(artifact, step, ctx):
    hidden = step.get('hidden', {})
    materials = ['FeS', 'MnS', 'VS']
    passed = 0
    for key in materials:
        gold = hidden.get(key, {})
        if not gold:
            continue
        entry = artifact.get(key)
        if entry is None:
            continue
        if entry.get('ground_state') != gold['ground_state']:
            continue
        if entry.get('is_metallic') != gold['is_metallic']:
            continue
        val = entry.get('magnetic_moment')
        if val is None:
            continue
        if abs(val - gold['magnetic_moment']) <= gold.get('tolerance', 0.5):
            passed += 1
    return passed / len(materials) if materials else 0.0


# === block: score_1 (check id='phonon') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        threshold = step.get('hidden', {}).get('threshold', 0.1)
        materials = ['FeS', 'MnS', 'VS']
        passed = 0
        for key in materials:
            entry = artifact.get(key)
            if entry is None:
                continue
            freq = entry.get('max_imaginary_frequency')
            if freq is not None and freq <= threshold:
                passed += 1
        return passed / len(materials) if materials else 0.0


# === block: score_2 (check id='aimd') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        hidden = step.get('hidden', {})
        drift_thr = hidden.get('drift_threshold', 0.01)
        runs = ['FeS_673K', 'VS_673K', 'MnS_300K']
        passed = 0
        for run in runs:
            entry = artifact.get(run)
            if entry is None:
                continue
            drift = entry.get('potential_energy_drift')
            stable = entry.get('structural_stable')
            if drift is not None and stable is not None and drift <= drift_thr and stable is True:
                passed += 1
        return passed / len(runs) if runs else 0.0


# === block: score_3 (check id='elastic') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        hidden = step.get('hidden', {})
        materials = ['FeS', 'MnS', 'VS']
        passed_materials = 0
        for mat in materials:
            gold_const = hidden.get(mat, {})
            consts = artifact.get(mat)
            if consts is None or not gold_const:
                continue
            all_ok = True
            for c in ['c11_2D', 'c12_2D', 'c66_2D']:
                val = consts.get(c)
                ref = gold_const.get(c)
                if val is None or ref is None:
                    all_ok = False
                    break
                tol = max(gold_const.get('tolerance_rel', 0.1) * abs(ref), gold_const.get('tolerance_abs', 2.0))
                if abs(val - ref) > tol:
                    all_ok = False
                    break
            if all_ok:
                passed_materials += 1
        return passed_materials / len(materials) if materials else 0.0


# === block: score_4 (check id='her') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        hidden = step.get('hidden', {})
        tol = hidden.get('tolerance', 0.1)
        materials = ['FeS', 'VS']
        total_checks = 0
        passed_checks = 0
        for mat in materials:
            gold_data = hidden.get(mat, {})
            mat_data = artifact.get(mat)
            if not gold_data or not mat_data:
                continue
            for energy_type in ['differential', 'average']:
                gold_vals = gold_data.get(energy_type, {})
                vals = mat_data.get(energy_type, {})
                for n_str, ref in gold_vals.items():
                    val = vals.get(n_str)
                    if val is None:
                        continue
                    total_checks += 1
                    if abs(val - ref) <= tol:
                        passed_checks += 1
        return passed_checks / total_checks if total_checks > 0 else 0.0


_SCORERS = {
    'electronic_properties': score_0,
    'phonon': score_1,
    'aimd': score_2,
    'elastic': score_3,
    'her': score_4,
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
