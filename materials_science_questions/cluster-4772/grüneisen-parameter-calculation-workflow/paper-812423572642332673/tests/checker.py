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
    steps = spec.get('steps', [])
    ctx = {}
    if len(steps) > 0:
        ctx['phonon_gold'] = steps[0].get('gold_rows', [])
    if len(steps) > 1:
        ctx['thermo_gold'] = steps[1].get('gold_rows', [])
    return ctx


# === block: score_0 (check id='check_phonon_results') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx.get('phonon_gold', [])
    artifact_rows = artifact  # list of dicts from CSV
    tol_freq = 50.0
    tol_gamma = 0.2

    scores = []
    for gold in gold_rows:
        comp = gold['compound'].strip().lower()
        press = gold['pressure'].strip().lower()
        mode = gold['mode'].strip().lower()
        match = None
        for row in artifact_rows:
            if row.get('compound', '').strip().lower() == comp and \
               row.get('pressure', '').strip().lower() == press and \
               row.get('mode', '').strip().lower() == mode:
                match = row
                break
        if match is None:
            scores.append(0.0)
            continue
        freq = float(match.get('frequency_cm1', 0.0))
        freq_err = abs(freq - gold['frequency_cm1'])
        freq_score = max(0.0, 1.0 - freq_err / (2 * tol_freq))
        gamma = float(match.get('mode_gamma', 0.0))
        gamma_err = abs(gamma - gold['mode_gamma'])
        gamma_score = max(0.0, 1.0 - gamma_err / (2 * tol_gamma))
        per_row = 0.7 * freq_score + 0.3 * gamma_score
        scores.append(per_row)

    if len(scores) == 0:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='check_thermo_results') ===
def score_1(artifact, step, ctx):
    gold_rows = ctx.get('thermo_gold', [])
    artifact_rows = artifact
    tol_cv = 2.0
    tol_alpha = 0.5  # 10⁻⁶ K⁻¹

    scores = []
    for gold in gold_rows:
        comp = gold['compound'].strip().lower()
        temp = float(gold['temperature_K'])
        match = None
        for row in artifact_rows:
            if row.get('compound', '').strip().lower() == comp and abs(float(row.get('temperature_K', 0.0)) - temp) < 1e-4:
                match = row
                break
        if match is None:
            scores.append(0.0)
            continue
        cv = float(match.get('Cv_J_mol_K', 0.0))
        cv_err = abs(cv - gold['Cv_J_mol_K'])
        cv_score = max(0.0, 1.0 - cv_err / (2 * tol_cv))
        alpha = float(match.get('alpha_1e6_K', 0.0))
        alpha_err = abs(alpha - gold['alpha_1e6_K'])
        alpha_score = max(0.0, 1.0 - alpha_err / (2 * tol_alpha))
        per_row = 0.5 * cv_score + 0.5 * alpha_score
        scores.append(per_row)

    # structural: Cv and alpha increase with T for each compound
    struct_score = 1.0
    for comp in set(r.get('compound', '').strip().lower() for r in artifact_rows):
        rows = [r for r in artifact_rows if r.get('compound', '').strip().lower() == comp]
        rows.sort(key=lambda x: float(x['temperature_K']))
        cv_vals = [float(r['Cv_J_mol_K']) for r in rows]
        alpha_vals = [float(r['alpha_1e6_K']) for r in rows]
        for i in range(1, len(cv_vals)):
            if cv_vals[i] < cv_vals[i-1] - 1e-6:
                struct_score = 0.0
            if alpha_vals[i] < alpha_vals[i-1] - 1e-6:
                struct_score = 0.0

    if len(scores) == 0:
        return 0.0
    avg_row = sum(scores) / len(scores)
    return 0.8 * avg_row + 0.2 * struct_score


_SCORERS = {
    'check_phonon_results': score_0,
    'check_thermo_results': score_1,
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
