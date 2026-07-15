import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    step = spec['steps'][0]  # single step
    gold_rows = step['gold_rows']
    key = lambda r: (r['reaction_label'], int(r['T_K']))
    gold_by_key = {key(r): r for r in gold_rows}
    tol_rel = step.get('tolerance_rel', 0.10)
    abs_zero = step.get('abs_zero_tolerance', 1e-4)
    return {'gold_by_key': gold_by_key, 'tol_rel': tol_rel, 'abs_zero': abs_zero}


# === block: score_0 (check id='eqcomp_check') ===
def score_0(artifact, step, ctx):
    gold_by_key = ctx['gold_by_key']
    tol_rel = ctx['tol_rel']
    abs_zero = ctx['abs_zero']
    # artifact is list of dicts with required columns
    rows = artifact
    def row_score(gold, agent):
        score_wo3 = 0.0
        score_prod = 0.0
        for field in ['WO3_wt', 'product_wt']:
            gold_val = float(gold[field])
            try:
                agent_val = float(agent[field])
            except (KeyError, ValueError):
                return 0.0
            diff = abs(agent_val - gold_val)
            if gold_val == 0.0:
                sc = 1.0 if diff <= abs_zero else 0.0
            else:
                rel = diff / gold_val
                if rel <= tol_rel:
                    sc = 1.0
                else:
                    sc = max(0.0, 1.0 - (rel - tol_rel) / (0.2 * gold_val) if gold_val > 0 else 0.0)
            if field == 'WO3_wt':
                score_wo3 = sc
            else:
                score_prod = sc
        return (score_wo3 + score_prod) / 2.0

    total_score = 0.0
    n_gold = len(gold_by_key)
    if n_gold == 0:
        return 1.0
    agent_by_key = {}
    for r in rows:
        lbl = r.get('reaction_label', '').strip()
        try:
            t = int(r.get('T_K', 0))
        except:
            continue
        agent_by_key[(lbl, t)] = r

    for key, gold in gold_by_key.items():
        agent = agent_by_key.get(key)
        if agent is None:
            total_score += 0.0
        else:
            total_score += row_score(gold, agent)
    return total_score / n_gold


_SCORERS = {
    'eqcomp_check': score_0,
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
