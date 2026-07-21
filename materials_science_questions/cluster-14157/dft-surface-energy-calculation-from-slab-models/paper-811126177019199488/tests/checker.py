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


# === block: score_0 (check id='check_surface_energies') ===
def score_0(artifact, step, ctx):
    ref = step['reference_data']
    tol_rel = step['tolerances']['relative']
    tol_abs_min = step['tolerances']['absolute_min']
    ref_map = {(r['metal'], r['face']): (r['LDA_surface_energy'], r['corrected_surface_energy']) for r in ref}
    if not isinstance(artifact, list):
        return 0.0
    matches = 0
    total = len(ref)
    for entry in artifact:
        key = (entry.get('metal'), entry.get('face'))
        if key in ref_map:
            lda_gold, corr_gold = ref_map[key]
            lda_sub = entry.get('LDA_surface_energy')
            corr_sub = entry.get('corrected_surface_energy')
            if lda_sub is not None and corr_sub is not None:
                lda_ok = abs(lda_sub - lda_gold) <= max(tol_rel * abs(lda_gold), tol_abs_min)
                corr_ok = abs(corr_sub - corr_gold) <= max(tol_rel * abs(corr_gold), tol_abs_min)
                if lda_ok and corr_ok:
                    matches += 1
    match_rate = matches / total if total else 0.0

    # trend check
    trend_check = step.get('trend_check', {})
    trend_rate = 0.0
    if trend_check.get('enable'):
        metals_expected = trend_check['metals_expected']
        metal_face_energy = {}
        for entry in artifact:
            m = entry.get('metal')
            f = entry.get('face')
            v = entry.get('corrected_surface_energy')
            if m and f and v is not None:
                metal_face_energy.setdefault(m, {})[f] = v
        trend_correct = 0
        trend_total = 0
        for metal, spec in metals_expected.items():
            faces = spec['faces']
            ascending = spec['ascending']
            if metal in metal_face_energy:
                vals = []
                for f in faces:
                    if f in metal_face_energy[metal]:
                        vals.append(metal_face_energy[metal][f])
                if len(vals) == len(faces):
                    trend_total += 1
                    if ascending:
                        if all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
                            trend_correct += 1
                    else:
                        if all(vals[i] > vals[i+1] for i in range(len(vals)-1)):
                            trend_correct += 1
        trend_rate = trend_correct / trend_total if trend_total else 0.0

    return 0.7 * match_rate + 0.3 * trend_rate


# === block: score_1 (check id='check_work_functions') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step['reference_data']
        tol_abs = step['tolerance_abs']
        ref_map = {(r['metal'], r['face']): r['Phi_DPDeltaSCF'] for r in ref}
        if not isinstance(artifact, list):
            return 0.0
        matches = 0
        total = len(ref)
        for entry in artifact:
            key = (entry.get('metal'), entry.get('face'))
            if key in ref_map:
                gold = ref_map[key]
                sub = entry.get('Phi_DPDeltaSCF')
                if sub is not None and abs(sub - gold) <= tol_abs:
                    matches += 1
        return matches / total if total else 0.0


_SCORERS = {
    'check_surface_energies': score_0,
    'check_work_functions': score_1,
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
