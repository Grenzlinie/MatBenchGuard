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


# === block: score_0 (check id='energy_vs_B') ===
def score_0(artifact, step, ctx):
    rows = artifact
    B_T = [float(r['B_T']) for r in rows]
    L1 = [float(r['E_L1_meV']) for r in rows]
    L2 = [float(r['E_L2_meV']) for r in rows]

    # Zero‑field splitting: L1 at B ≈ 0
    idx0 = next((i for i,b in enumerate(B_T) if abs(b) < 1e-6), None)
    e1_0 = L1[idx0] if idx0 is not None else None

    if e1_0 is not None:
        gold_e1 = 0.19
        tol_e1 = 0.02
        err = abs(e1_0 - gold_e1)
        if err <= tol_e1:
            score_e1 = 1.0
        else:
            excess = err - tol_e1
            score_e1 = max(0.0, 1.0 - excess / tol_e1)
    else:
        score_e1 = 0.0

    # Anticrossings: minima of |L1 - L2|
    diff = [abs(l1 - l2) for l1,l2 in zip(L1, L2)]
    minima_B = []
    for i in range(1, len(diff)-1):
        if diff[i] < diff[i-1] and diff[i] < diff[i+1]:
            minima_B.append(B_T[i])
    # Include endpoints if they are minimadef=[]
    if len(diff) > 1:
        if diff[0] < diff[1]:
            minima_B.append(B_T[0])
        if diff[-1] < diff[-2]:
            minima_B.append(B_T[-1])

    gold_pos = [1.5, 8.0]
    tol_T = 0.3
    found = [False for _ in gold_pos]
    for mb in minima_B:
        for j, gp in enumerate(gold_pos):
            if abs(mb - gp) <= tol_T:
                found[j] = True
    score_anti = sum(found) / len(gold_pos)

    w1 = step['metrics'][0]['sub_weight']
    w2 = step['metrics'][1]['sub_weight']
    return w1 * score_e1 + w2 * score_anti


# === block: score_1 (check id='fitted_N0alpha') ===
def score_1(artifact, step, ctx):
    text = artifact.strip()
    try:
        val = float(text)
    except Exception:
        return 0.0
    gold = step['gold']
    tol = step['tolerance']
    err = abs(val - gold)
    if err <= tol:
        return 1.0
    else:
        excess = err - tol
        return max(0.0, 1.0 - excess / tol)


_SCORERS = {
    'energy_vs_B': score_0,
    'fitted_N0alpha': score_1,
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
