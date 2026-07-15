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
    gold_rows = [
        dict(system='Be-C2H2+', state='2A1', R_min=2.032, D_e=30.0),
        dict(system='Be-C2H2', state='3B2', R_min=1.771, D_e=19.1),
        dict(system='Be-C2H4+', state='2A1', R_min=2.088, D_e=33.2),
        dict(system='Be-C2H4', state='3B2', R_min=1.782, D_e=24.5),
    ]
    gold_energy = -91.298
    tol_R = 0.01
    tol_eng = 0.001
    tol_de = 0.5
    return {
        'gold_rows': gold_rows,
        'gold_energy': gold_energy,
        'tol_R': tol_R,
        'tol_De': tol_de,
        'tol_eng': tol_eng,
    }


# === block: score_0 (check id='step_binding') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    rows = artifact  # list of dicts from csv.DictReader
    gold_rows = step.get('gold', [])
    tol_R = step.get('tolerance_R', 0.01)
    tol_De = step.get('tolerance_energy', 0.5)
    agents = {}
    for r in rows:
        sys = str(r.get('system','')).strip().lower()
        st = str(r.get('state','')).strip().lower()
        agents[(sys, st)] = r
    correct = 0
    for gold in gold_rows:
        key = (gold['system'].lower(), gold['state'].lower())
        if key not in agents:
            continue
        ar = agents[key]
        try:
            R = float(ar.get('R_min', ''))
            D = float(ar.get('D_e', ''))
        except (ValueError, TypeError):
            continue
        if abs(R - gold['R_min']) <= tol_R and abs(D - gold['D_e']) <= tol_De:
            correct += 1
    return correct / len(gold_rows) if gold_rows else 0.0


# === block: score_1 (check id='step_verification') ===
def score_1(artifact, step, ctx):
    text = artifact  # artifact is a string (file content)
    lines = [line.strip() for line in text.splitlines() if line.strip() != '']
    if not lines:
        return 0.0
    try:
        val = float(lines[0])
    except (ValueError, TypeError):
        return 0.0
    gold_eng = ctx['gold_energy']
    tol_eng = ctx['tol_eng']
    if abs(val - gold_eng) <= tol_eng:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_binding': score_0,
    'step_verification': score_1,
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
