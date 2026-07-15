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
    def prepare_gold(spec):
        bg_acc = None
        ep_acc = None
        trend_elems = None
        for s in spec.get('steps', []):
            if s['id'] == 'band_gaps_accuracy':
                bg_acc = s['gold_table']
            if s['id'] == 'extraction_potentials_accuracy':
                ep_acc = s['gold_table']
            if s['id'] in ('band_gaps_trend','extraction_potentials_trend'):
                trend_elems = s['trend_elements']
        # build expected ordering from gold for trend checks
        # ordering: Mn, Co, Ni, Zn within each phase
        bg_ordering = {}
        ep_ordering = {}
        if bg_acc is not None and trend_elems is not None:
            for phase in ['α','β']:
                vals = [bg_acc.get(f"{phase}-Na{el}Fe(MoO₄)₃", None) for el in trend_elems]
                if all(v is not None for v in vals):
                    bg_ordering[phase] = vals
        if ep_acc is not None and trend_elems is not None:
            for phase in ['α','β']:
                for metric in ['V1_ev','V2_ev']:
                    vals = [ep_acc.get(f"{phase}-Na{el}Fe(MoO₄)₃", {}).get(metric, None) for el in trend_elems]
                    if all(v is not None for v in vals):
                        ep_ordering.setdefault(phase, {})[metric] = vals
        return {
            'bg_gold': bg_acc,
            'ep_gold': ep_acc,
            'trend_elements': trend_elems,
            'bg_ordering': bg_ordering,
            'ep_ordering': ep_ordering
        }
    ctx = prepare_gold(spec)


# === block: score_0 (check id='band_gaps_accuracy') ===
def score_0(artifact, step, ctx):
    tol = float(step['tolerance_abs'])
    gold = ctx.get('bg_gold', {})
    if not gold:
        return 0.0
    reader = csv.DictReader(artifact)  # artifact is a list of dicts from csv.DictReader
    rows = list(reader)
    total = len(gold)
    if total == 0:
        return 0.0
    correct = 0
    for row in rows:
        comp = row.get('compound','').strip()
        if comp in gold:
            try:
                pred = float(row['band_gap_ev'])
            except (ValueError, KeyError):
                continue
            if abs(pred - gold[comp]) <= tol:
                correct += 1
    return correct / total


# === block: score_1 (check id='band_gaps_trend') ===
def score_1(artifact, step, ctx):
    elems = ctx.get('trend_elements', [])
    ordering = ctx.get('bg_ordering', {})
    if not elems or not ordering:
        return 0.0
    reader = csv.DictReader(artifact)
    rows = list(reader)
    # build dict of phase->elem->value
    vals = {}
    for row in rows:
        comp = row.get('compound','').strip()
        try:
            gap = float(row['band_gap_ev'])
        except (ValueError, KeyError):
            continue
        # identify phase and element
        for phase in ['α','β']:
            for el in elems:
                if f"{phase}-Na{el}Fe(MoO₄)₃" in comp:
                    vals.setdefault(phase, {})[el] = gap
                    break
    # count violations
    violations = 0
    comparisons = 0
    for phase, gold_seq in ordering.items():
        if phase not in vals:
            continue
        seq = [vals[phase].get(el, None) for el in elems]
        if None in seq:
            continue
        for i in range(len(seq)-1):
            comparisons += 1
            if seq[i] > seq[i+1]:
                violations += 1
    if comparisons == 0:
        return 1.0
    return 1.0 - violations / comparisons


# === block: score_2 (check id='extraction_potentials_accuracy') ===
def score_2(artifact, step, ctx):
    tol = float(step['tolerance_abs'])
    gold = ctx.get('ep_gold', {})
    if not gold:
        return 0.0
    reader = csv.DictReader(artifact)
    rows = list(reader)
    total = len(gold) * 2  # each compound has two values
    if total == 0:
        return 0.0
    correct = 0
    for row in rows:
        comp = row.get('compound','').strip()
        if comp not in gold:
            continue
        g = gold[comp]
        for col in ['V1_ev','V2_ev']:
            try:
                pred = float(row[col])
            except (ValueError, KeyError):
                continue
            if abs(pred - g[col]) <= tol:
                correct += 1
    return correct / total


# === block: score_3 (check id='extraction_potentials_trend') ===
def score_3(artifact, step, ctx):
    elems = ctx.get('trend_elements', [])
    ordering = ctx.get('ep_ordering', {})
    if not elems or not ordering:
        return 0.0
    reader = csv.DictReader(artifact)
    rows = list(reader)
    # build dict phase->metric->elem->value
    vals = {}
    for row in rows:
        comp = row.get('compound','').strip()
        for phase in ['α','β']:
            for el in elems:
                if f"{phase}-Na{el}Fe(MoO₄)₃" in comp:
                    for metric in ['V1_ev','V2_ev']:
                        try:
                            v = float(row[metric])
                        except (ValueError, KeyError):
                            continue
                        vals.setdefault(phase, {}).setdefault(metric, {})[el] = v
                    break
    violations = 0
    comparisons = 0
    for phase, metrics in ordering.items():
        if phase not in vals:
            continue
        for metric, gold_seq in metrics.items():
            if metric not in vals[phase]:
                continue
            seq = [vals[phase][metric].get(el, None) for el in elems]
            if None in seq:
                continue
            for i in range(len(seq)-1):
                comparisons += 1
                if seq[i] > seq[i+1]:
                    violations += 1
    if comparisons == 0:
        return 1.0
    return 1.0 - violations / comparisons


_SCORERS = {
    'band_gaps_accuracy': score_0,
    'band_gaps_trend': score_1,
    'extraction_potentials_accuracy': score_2,
    'extraction_potentials_trend': score_3,
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
