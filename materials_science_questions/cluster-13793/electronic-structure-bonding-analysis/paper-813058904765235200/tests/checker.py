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


# === block: score_0 (check id='step_interaction_energies_csv') ===
def score_0(artifact, step, ctx):
    _canonical = {
        'yes': 'spontaneous',
        'no': 'no_reconstruction',
        'spontaneous': 'spontaneous',
        'no_reconstruction': 'no_reconstruction',
        'energetically_favorable_but_not_spontaneous': 'energetically_favorable_but_not_spontaneous',
    }
    expected_list = step.get('expected', [])
    tolerance = step.get('tolerance_eV', 0.25)
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    total = len(expected_list)
    correct = 0
    for exp in expected_list:
        exp_solute = exp['solute'].strip()
        exp_sep = exp['separation'].strip()
        exp_e = exp['E_int']
        exp_rc = exp['reconstruction_spontaneous'].strip().lower()
        exp_rc_canon = _canonical.get(exp_rc, exp_rc)
        found = False
        for row in artifact:
            row_solute = row.get('solute', '').strip()
            row_sep = row.get('separation', '').strip()
            if row_solute == exp_solute and row_sep == exp_sep:
                found = True
                try:
                    row_e = float(row.get('E_int', 'nan'))
                except (ValueError, TypeError):
                    row_e = None
                row_rc = row.get('reconstruction_spontaneous', '').strip().lower()
                row_rc_canon = _canonical.get(row_rc, row_rc)
                if row_e is not None and abs(row_e - exp_e) <= tolerance:
                    if row_rc_canon == exp_rc_canon:
                        correct += 1
                break
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_reconstruction_summary_json') ===
def score_1(artifact, step, ctx):
    expected_list = step.get('expected', [])
    tolerance = step.get('tolerance_eV', 0.25)
    if not isinstance(artifact, dict) or 'results' not in artifact:
        return 0.0
    results = artifact['results']
    total = len(expected_list)
    correct = 0
    for exp in expected_list:
        exp_solute = exp['solute'].strip()
        exp_sep = exp['separation'].strip()
        exp_e = exp['E_int_eV']
        exp_rc = exp['reconstruction'].strip().lower()
        found = False
        for res in results:
            if res.get('solute', '').strip() == exp_solute and res.get('separation', '').strip() == exp_sep:
                found = True
                try:
                    val = float(res.get('E_int_eV', 'nan'))
                except (ValueError, TypeError):
                    val = None
                rc = res.get('reconstruction', '').strip().lower()
                if val is not None and abs(val - exp_e) <= tolerance:
                    if rc == exp_rc:
                        correct += 1
                break
    return correct / total if total > 0 else 0.0


_SCORERS = {
    'step_interaction_energies_csv': score_0,
    'step_reconstruction_summary_json': score_1,
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
