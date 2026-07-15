import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
        gold_rows = []
        for step in steps:
            if step.get('id') == 'score_reproduction_results':
                gold_rows = step.get('gold_rows', [])
                break
        return {'gold_rows': gold_rows}


# === block: score_0 (check id='score_reproduction_results') ===
def score_0(artifact, step, ctx):
        gold_rows = ctx.get('gold_rows', [])
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        # Build lookup by phi from gold rows
        gold_by_phi = {}
        for g in gold_rows:
            phi = g.get('phi')
            if phi is not None:
                gold_by_phi[phi] = g
        # Per‑field tolerances: (relative, absolute_min)
        tolerances = {
            'inert_max': (0.02, 0.001),
            'chem_acoustic_tstar': (0.02, 0.01),
            'full_tstar': (0.02, 0.01),
            'pressure_tstar_phi125': (0.05, 0.01),
            'pressure_tstar_phi5': (0.05, 0.01),
        }
        numeric_fields = list(tolerances.keys())
        total_checks = 0
        correct = 0
        for row in artifact:
            phi_str = row.get('phi')
            if phi_str is None:
                continue
            try:
                phi_val = float(phi_str)
            except:
                continue
            if phi_val not in gold_by_phi:
                continue
            gold = gold_by_phi[phi_val]
            # blowup_mode exact match (case‑insensitive, strip whitespace)
            gold_mode = (gold.get('blowup_mode') or '').strip().lower()
            agent_mode = (row.get('blowup_mode') or '').strip().lower()
            if gold_mode:
                total_checks += 1
                if agent_mode == gold_mode:
                    correct += 1
            # Numeric fields
            for field in numeric_fields:
                gold_val = gold.get(field)
                if gold_val is None:
                    continue
                agent_val_str = row.get(field, '').strip()
                if agent_val_str == '':
                    # Missing value counts as incorrect
                    total_checks += 1
                    continue
                try:
                    agent_val = float(agent_val_str)
                except:
                    total_checks += 1
                    continue
                rel_tol, abs_max = tolerances[field]
                # Allowable absolute difference is the larger of relative tolerance and the floor
                allowed_diff = max(rel_tol * abs(gold_val), abs_max)
                if abs(agent_val - gold_val) <= allowed_diff:
                    correct += 1
                total_checks += 1
        if total_checks == 0:
            return 0.0
        return float(correct) / float(total_checks)


_SCORERS = {
    'score_reproduction_results': score_0,
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
