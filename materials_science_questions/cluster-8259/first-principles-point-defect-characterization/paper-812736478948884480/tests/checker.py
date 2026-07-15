import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    gold = spec.get('gold', {})
    return {'gold': gold}


# === block: score_0 (check id='structural_distances') ===
def score_0(artifact, step, ctx):
    gold_dist = ctx['gold'].get('structural_distances', {})
    tolerance = step.get('tolerance', 0.05)
    hits = 0
    total = 0
    for sys in ['I_i', 'I_i_minus1', 'I_i_plus1']:
        for temp in ['0K', '300K']:
            for key in ['I_I_distance', 'I_Pb_distance']:
                gold_val = gold_dist.get(sys, {}).get(temp, {}).get(key)
                if gold_val is None:
                    continue
                total += 1
                try:
                    agent_val = float(artifact[sys][temp][key])
                except (KeyError, TypeError, ValueError):
                    continue
                if abs(agent_val - gold_val) <= tolerance:
                    hits += 1
    if total == 0:
        return 0.0
    return hits / total


# === block: score_1 (check id='rms_velocities') ===
def score_1(artifact, step, ctx):
    gold_rows = ctx['gold'].get('rms_velocities', [])
    tolerance = step.get('tolerance', 0.001)
    if not isinstance(artifact, list):
        return 0.0
    agent_by_system = {}
    for row in artifact:
        sys = row.get('System')
        if sys:
            agent_by_system[sys] = row
    hits = 0
    total = 0
    for g in gold_rows:
        sys = g.get('System')
        if sys not in agent_by_system:
            continue
        arow = agent_by_system[sys]
        for col in ['total', 'MA', 'Pb_I_lattice', 'Pb_I_including_interstitial', 'interstitial_I', 'O']:
            gval = g.get(col)
            if gval is None:
                continue
            total += 1
            try:
                aval = float(arow.get(col))
            except (TypeError, ValueError):
                continue
            if abs(aval - gval) <= tolerance:
                hits += 1
    if total == 0:
        return 0.0
    return hits / total


# === block: score_2 (check id='recombination_times') ===
def score_2(artifact, step, ctx):
    gold_times = ctx['gold'].get('recombination_times', {})
    gold_ordering = gold_times.get('ordering', [])
    factor = step.get('tolerance_factor', 2.0)
    ordering_weight = step.get('ordering_weight', 0.3)
    time_score = 0.0
    for key in ['pristine', 'I_i', 'I_i_minus1', 'I_i_plus1', 'IO3_minus1']:
        gold_val = gold_times.get(key)
        if gold_val is None:
            continue
        try:
            agent_val = float(artifact[key]['recombination_time_ns'])
        except (KeyError, TypeError, ValueError):
            continue
        lower = gold_val / factor
        upper = gold_val * factor
        if lower <= agent_val <= upper:
            time_score += 1.0 / 5.0
    ordering_score = 1.0 if artifact.get('recombination_ordering') == gold_ordering else 0.0
    total = (1.0 - ordering_weight) * time_score + ordering_weight * ordering_score
    return total


_SCORERS = {
    'structural_distances': score_0,
    'rms_velocities': score_1,
    'recombination_times': score_2,
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
