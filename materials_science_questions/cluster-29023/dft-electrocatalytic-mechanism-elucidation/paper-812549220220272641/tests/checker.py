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


# === block: score_0 (check id='adsorption_energies_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    fragments = {}
    for row in rows:
        frag = row['Fragment'].strip()
        val = float(row['DeltaE_ads_kcal_mol'])
        if frag not in fragments or val < fragments[frag]:
            fragments[frag] = val

    gold = step['gold_best']
    tol = step['tolerance_abs']
    decay = step['decay_range']
    scores = []
    for frag, gold_best in gold.items():
        agent_min = fragments.get(frag)
        if agent_min is None:
            scores.append(0.0)
            continue
        full_thresh = gold_best + tol
        if agent_min <= full_thresh:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (agent_min - full_thresh) / decay)
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='hole_electron_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    frag_S = {}
    frag_D = {}
    for row in rows:
        frag = row['Fragment'].strip()
        state = row['State'].strip()
        if state != 'S1':
            continue
        S_val = float(row['S'])
        D_val = float(row['D'])
        frag_S[frag] = S_val
        frag_D[frag] = D_val

    gold_S = step['gold_S']
    gold_D = step['gold_D']
    tol_S = step['tolerance_S']
    tol_D = step['tolerance_D']
    decay_S = step['decay_S_range']
    decay_D = step['decay_D_range']

    fragments = ['PY_DHBD_COF', 'PY_BPY_COF', 'PY_BP_COF']
    scores = []
    for frag in fragments:
        if frag not in frag_S or frag not in frag_D:
            scores.append(0.0)
            continue
        agent_S = frag_S[frag]
        agent_D = frag_D[frag]
        # S (lower is better)
        thresh_s = gold_S[frag] + tol_S
        if agent_S <= thresh_s:
            s_score = 1.0
        else:
            s_score = max(0.0, 1.0 - (agent_S - thresh_s) / decay_S)
        # D
        if frag == 'PY_BPY_COF':
            # centrosymmetric, target is exactly 0.0
            diff = abs(agent_D - gold_D[frag])
            if diff <= tol_D:
                d_score = 1.0
            else:
                d_score = max(0.0, 1.0 - (diff - tol_D) / decay_D)
        else:
            # larger is better
            thresh_d = gold_D[frag] - tol_D
            if agent_D >= thresh_d:
                d_score = 1.0
            else:
                d_score = max(0.0, 1.0 - (thresh_d - agent_D) / decay_D)
        scores.append((s_score + d_score) / 2.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'adsorption_energies_check': score_0,
    'hole_electron_check': score_1,
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
