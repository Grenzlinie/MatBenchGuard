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


# === block: score_0 (check id='enthalpy_diff') ===
def score_0(artifact, step, ctx):
    H_rel_bcc = artifact.get('H_rel_bcc', None)
    if H_rel_bcc is None:
        return 0.0
    target = step['target']
    tol = step['tolerance']
    if abs(H_rel_bcc - target) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='phonon_stability') ===
def score_1(artifact, step, ctx):
    freqs = artifact.get('frequencies', [])
    if not freqs:
        return 0.0
    try:
        flatten = [f for branch in freqs for f in branch]
    except TypeError:
        return 0.0
    if not flatten:
        return 0.0
    if all(f >= step.get('threshold_cm1', -1.0) for f in flatten):
        return 1.0
    return 0.0


# === block: score_2 (check id='pnma_elastic') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance']
    constants = ['C11','C22','C33','C44','C55','C66','C12','C13','C23']
    scores = []
    for c in constants:
        v = artifact.get(c)
        g = gold.get(c)
        if v is None or g is None:
            scores.append(0.0)
        else:
            if abs(v - g) / g <= tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
    elastic_score = sum(scores)/len(scores) if scores else 0.0
    C11 = artifact.get('C11')
    C22 = artifact.get('C22')
    C33 = artifact.get('C33')
    C44 = artifact.get('C44')
    C55 = artifact.get('C55')
    C66 = artifact.get('C66')
    C12 = artifact.get('C12')
    C13 = artifact.get('C13')
    C23 = artifact.get('C23')
    if None in (C11,C22,C33,C44,C55,C66,C12,C13,C23):
        return 0.0
    criterions = [
        C11>0, C22>0, C33>0, C44>0, C55>0, C66>0,
        C11+C22+C33+2*(C12+C13+C23)>0,
        C11+C22-2*C12>0,
        C11+C33-2*C13>0,
        C22+C33-2*C23>0
    ]
    if not all(criterions):
        return 0.0
    return elastic_score


# === block: score_3 (check id='pnma_sound') ===
def score_3(artifact, step, ctx):
    targets = step['gold']
    tol = step['tolerance']
    Cl = artifact.get('C_l')
    Cb = artifact.get('C_b')
    if Cl is None or Cb is None:
        return 0.0
    score = 0.0
    if abs(Cl - targets['C_l']) / targets['C_l'] <= tol:
        score += 0.5
    if abs(Cb - targets['C_b']) / targets['C_b'] <= tol:
        score += 0.5
    return score


# === block: score_4 (check id='omega_elastic') ===
def score_4(artifact, step, ctx):
    entries = artifact
    if not isinstance(entries, list) or not entries:
        return 0.0
    all_neg = all(e.get('C44', 0) < 0 for e in entries)
    return 1.0 if all_neg else 0.0


_SCORERS = {
    'enthalpy_diff': score_0,
    'phonon_stability': score_1,
    'pnma_elastic': score_2,
    'pnma_sound': score_3,
    'omega_elastic': score_4,
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
