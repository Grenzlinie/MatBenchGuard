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


# === block: score_0 (check id='elastic_check') ===
def score_0(artifact, step, ctx):
    import json
    gold = step['gold']
    tolerance = step['tolerance']
    scores = []
    for k in ['C11', 'C12', 'C44']:
        val = artifact.get(k)
        if val is None:
            scores.append(0.0)
            continue
        err = abs(val - gold[k])
        tol = tolerance.get(k, 15.0)
        scores.append(1.0 if err <= tol else 0.0)
    return sum(scores) / 3.0


# === block: score_1 (check id='derived_check') ===
def score_1(artifact, step, ctx):
    import os, json
    path = os.path.join('/app/outputs', 'elastic_constants.json')
    if not os.path.exists(path):
        return 0.0
    with open(path) as f:
        elas = json.load(f)
    C11 = elas.get('C11', None)
    C12 = elas.get('C12', None)
    C44 = elas.get('C44', None)
    if None in (C11, C12, C44):
        return 0.0
    B = (C11 + 2*C12) / 3.0
    GV = (C11 - C12 + 3*C44) / 5.0
    denom = 4*C44 + 3*(C11 - C12)
    GR = (5*(C11 - C12)*C44) / denom if denom != 0 else 0.0
    G = (GV + GR) / 2.0
    CP = C12 - C44
    BG = B / G if G != 0 else 0.0
    gold = step['gold']
    tol = step['tolerance']
    b_score = 1.0 if abs(B - gold['B']) <= tol.get('B', 10.0) else 0.0
    g_score = 1.0 if abs(G - gold['G']) <= tol.get('G', 10.0) else 0.0
    bg_score = 1.0 if abs(BG - gold['B/G']) <= tol.get('B/G', 0.1) else 0.0
    cp_score = 1.0 if abs(CP - gold['C_P']) <= tol.get('C_P', 5.0) else 0.0
    return (b_score + g_score + bg_score + cp_score) / 4.0


# === block: score_2 (check id='phonon_check') ===
def score_2(artifact, step, ctx):
    freqs = artifact.get('frequencies_THz')
    if not isinstance(freqs, list) or len(freqs) != 8:
        return 0.0
    all_real = artifact.get('all_real', False)
    if not all_real or any(f < -0.1 for f in freqs):
        return 0.0
    gold = step['gold']
    tol = step['tolerance'].get('freq', 0.5)
    match = sum(1 for i in range(8) if abs(freqs[i] - gold[i]) <= tol)
    return match / 8.0


_SCORERS = {
    'elastic_check': score_0,
    'derived_check': score_1,
    'phonon_check': score_2,
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
