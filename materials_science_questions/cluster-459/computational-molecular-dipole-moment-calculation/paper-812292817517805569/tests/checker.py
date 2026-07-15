import os
import json
import csv

# === author imports / helpers ===
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
    def prepare(outputs_dir, spec):
        step = spec['steps'][0]
        ref_rows = step['reference_rows']
        expected_charges = {}
        expected_dipoles = {}
        diatomic_mols = set()
        for r in ref_rows:
            key = (r['molecule'].strip(), r['atom'].strip())
            expected_charges[key] = float(r['charge'])
            if r['dipole'] is not None:
                mol = r['molecule'].strip()
                diatomic_mols.add(mol)
                if mol not in expected_dipoles:
                    expected_dipoles[mol] = float(r['dipole'])
        return {
            'expected_charges': expected_charges,
            'expected_dipoles': expected_dipoles,
            'diatomic_mols': diatomic_mols,
            'charge_mae_threshold': step['charge_mae_threshold'],
            'dipole_mae_threshold': step['dipole_mae_threshold']
        }


# === block: score_0 (check id='qeq_accuracy') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected_charges = ctx['expected_charges']
        expected_dipoles = ctx['expected_dipoles']
        diatomic_mols = ctx['diatomic_mols']
        charge_thresh = ctx['charge_mae_threshold']
        dipole_thresh = ctx['dipole_mae_threshold']
        rows = artifact
        agent_charges = {}
        agent_dipoles = {}
        for row in rows:
            mol = row['molecule'].strip()
            atom = row['atom'].strip()
            key = (mol, atom)
            try:
                charge = float(row['predicted_charge'])
            except (ValueError, TypeError):
                charge = 0.0
            if key not in agent_charges:
                agent_charges[key] = charge
            else:
                agent_charges[key] = (agent_charges[key] + charge) / 2.0
            if mol in diatomic_mols:
                try:
                    dipole = float(row['predicted_dipole_moment'])
                    if math.isnan(dipole):
                        continue
                except (ValueError, TypeError):
                    continue
                if mol not in agent_dipoles:
                    agent_dipoles[mol] = dipole
        charge_errors = []
        for key, exp in expected_charges.items():
            if key in agent_charges:
                charge_errors.append(abs(agent_charges[key] - exp))
            else:
                charge_errors.append(10.0)
        mae_charge = sum(charge_errors) / len(charge_errors) if charge_errors else 0.0
        dipole_errors = []
        for mol, exp in expected_dipoles.items():
            if mol in agent_dipoles:
                dipole_errors.append(abs(agent_dipoles[mol] - exp))
            else:
                dipole_errors.append(10.0)
        mae_dipole = sum(dipole_errors) / len(dipole_errors) if dipole_errors else 0.0
        def mm_score(mae, thresh):
            if mae <= thresh:
                return 1.0
            return max(0.0, 1.0 - (mae - thresh) / thresh)
        charge_score = mm_score(mae_charge, charge_thresh)
        dipole_score = mm_score(mae_dipole, dipole_thresh)
        return 0.5 * charge_score + 0.5 * dipole_score


_SCORERS = {
    'qeq_accuracy': score_0,
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
