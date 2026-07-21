import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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
    spec = json.load(open('/tests/grading_spec.json'))
    steps = spec['steps']
    ctx = {}
    for step in steps:
        if step['id'] == 'step_5':
            ctx['overpotentials_gold'] = step['gold']
            ctx['overpotentials_tol'] = step['tolerance_abs']
            ctx['overpotentials_max_dev'] = step['max_deviation']
        elif step['id'] == 'step_6':
            ctx['activation_gold_rows'] = step['gold_rows']
    return ctx


# === block: score_0 (check id='step_5') ===
def score_0(artifact, step, ctx):
    def score_value(val, gold, tol, max_dev):
        # Overpotential is lower-is-better; full credit if val <= gold + tol.
        # Penalize only higher values.
        if val <= gold + tol:
            return 1.0
        excess = val - (gold + tol)
        max_excess = max_dev - tol
        if max_excess <= 0.0:
            return 0.0
        if excess >= max_excess:
            return 0.0
        return 1.0 - excess / max_excess

    if not artifact:
        return 0.0
    rows = artifact
    if not rows:
        return 0.0
    # build lookup
    lookup = {r['catalyst'].strip(): r for r in rows}
    score_total = 0.0
    for cat, gold_info in ctx['overpotentials_gold'].items():
        if cat not in lookup:
            continue
        row = lookup[cat]
        try:
            op_v = float(row['overpotential_V'])
        except (ValueError, KeyError):
            continue
        op_score = score_value(op_v, gold_info['overpotential_V'], ctx['overpotentials_tol'], ctx['overpotentials_max_dev'])
        rds_score = 1.0 if row.get('rds', '').strip() == gold_info['rds'] else 0.0
        cat_score = 0.5 * op_score + 0.5 * rds_score
        score_total += cat_score
    score_total /= len(ctx['overpotentials_gold'])  # average over catalysts
    # trend: V3C2 < Nb3C2
    if 'V3C2' in lookup and 'Nb3C2' in lookup:
        try:
            v3 = float(lookup['V3C2']['overpotential_V'])
            nb = float(lookup['Nb3C2']['overpotential_V'])
            if v3 < nb:
                pass # no deduction, extra reward could be given but we keep score as is
        except:
            pass
    return score_total


# === block: score_1 (check id='step_6') ===
def score_1(artifact, step, ctx):
    def score_barrier(value, gold, tol, max_dev):
        diff = abs(value - gold)
        if diff <= tol:
            return 1.0
        elif diff <= max_dev:
            return max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
        else:
            return 0.0

    rows = artifact
    if not rows:
        return 0.0
    lookup = {}
    for r in rows:
        key = (r['catalyst'].strip(), r['ts_id'].strip())
        try:
            lookup[key] = float(r['barrier_eV'])
        except (ValueError, KeyError):
            continue

    scores = []
    for gr in ctx['activation_gold_rows']:
        key = (gr['catalyst'], gr['ts_id'])
        if key not in lookup:
            scores.append(0.0)
            continue
        val = lookup[key]
        s = score_barrier(val, gr['barrier_eV'], gr['tolerance'], gr['max_deviation'])
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'step_5': score_0,
    'step_6': score_1,
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
