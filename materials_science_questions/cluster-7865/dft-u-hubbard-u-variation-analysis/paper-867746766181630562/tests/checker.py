import os
import json
import csv

# === author imports / helpers ===
import json, math


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
        ctx = {}
        for check in spec['checks']:
            cid = check['id']
            if cid == 'exchange_couplings':
                ctx['J_gold'] = {
                    'J_NiIr': float(check['gold_J_NiIr']),
                    'J_IrIr_artificial': float(check['gold_J_IrIr_artificial']),
                    'J_IrIr_real': float(check['gold_J_IrIr_real']),
                    'J_NiNi': float(check['gold_J_NiNi']),
                    'J_IrIr_3NN': float(check['gold_J_IrIr_3NN']),
                    'tolerance': float(check['tolerance'])
                }
            elif cid == 'orbital_moment':
                ctx['orbital_target'] = float(check['target'])
                ctx['orbital_tol'] = float(check['tolerance'])
        return ctx


# === block: score_0 (check id='exchange_couplings') ===
def score_0(artifact, step, ctx):
        # Build energy lookup from the CSV rows
        energy = {}
        for row in artifact:
            sys = row.get('system', '').strip()
            state = row.get('magnetic_state', '').strip()
            try:
                e = float(row.get('total_energy_ev', ''))
            except:
                return 0.0
            energy[(sys, state)] = e

        # Required systems and magnetic states
        required = [
            ('Sr2NiIrO6', 'FM'),
            ('Sr2NiIrO6', 'G_AF'),
            ('Sr2Zn(Ni)IrO6', 'FM'),
            ('Sr2Zn(Ni)IrO6', 'layered_AF'),
            ('La2NiSiO6', 'FM'),
            ('La2NiSiO6', 'layered_AF'),
            ('Sr2ZnIrO6', 'FM'),
            ('Sr2ZnIrO6', 'layered_AF'),
            ('Sr2ZnIrO6', 'bilayered_AF')
        ]
        if not all(pair in energy for pair in required):
            return 0.0

        # Compute energy differences (eV) and convert to meV for J values
        delta_Sr2NiIrO6 = energy[('Sr2NiIrO6', 'G_AF')] - energy[('Sr2NiIrO6', 'FM')]
        J_NiIr = -delta_Sr2NiIrO6 * 1000 / 12

        delta_art = energy[('Sr2Zn(Ni)IrO6', 'layered_AF')] - energy[('Sr2Zn(Ni)IrO6', 'FM')]
        J_IrIr_art = -delta_art * 1000 / 8

        delta_real_layered = energy[('Sr2ZnIrO6', 'layered_AF')] - energy[('Sr2ZnIrO6', 'FM')]
        J_IrIr_real = -delta_real_layered * 1000 / 8

        delta_NiNi = energy[('La2NiSiO6', 'layered_AF')] - energy[('La2NiSiO6', 'FM')]
        J_NiNi = -delta_NiNi * 1000 / 8

        delta_bilayered = energy[('Sr2ZnIrO6', 'bilayered_AF')] - energy[('Sr2ZnIrO6', 'FM')]
        J_IrIr_3NN = ( - (delta_bilayered * 1000) - 4 * J_IrIr_real ) / 2

        gold = ctx['J_gold']
        tol = gold['tolerance']
        comparisons = [
            (J_NiIr, gold['J_NiIr']),
            (J_IrIr_art, gold['J_IrIr_artificial']),
            (J_IrIr_real, gold['J_IrIr_real']),
            (J_NiNi, gold['J_NiNi']),
            (J_IrIr_3NN, gold['J_IrIr_3NN'])
        ]
        num_within = sum(1 for calc, ref in comparisons if abs(calc - ref) <= tol)
        return num_within / len(comparisons)


# === block: score_1 (check id='orbital_moment') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        val = artifact.get('ir_orbital_moment')
        if val is None:
            return 0.0
        try:
            val = float(val)
        except:
            return 0.0
        target = ctx['orbital_target']
        tol = ctx['orbital_tol']
        return 1.0 if abs(val - target) <= tol else 0.0


_SCORERS = {
    'exchange_couplings': score_0,
    'orbital_moment': score_1,
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
