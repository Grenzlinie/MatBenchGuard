import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    gold_values = {}
    for step in spec.get('steps', []):
        oid = step['id']
        gold_values[oid] = {
            'gold_map': step.get('gold', {}),
            'tol': step.get('tolerance_abs', 0.0)
        }
    return {'gold': gold_values}


# === block: score_0 (check id='band_gap_accuracy') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # dict with 'parameter_sets'
    step_id = 'band_gap_accuracy'
    gold_map = ctx['gold'][step_id]['gold_map']
    tol = ctx['gold'][step_id]['tol']

    sets = artifact.get('parameter_sets', [])
    if not sets:
        return 0.0

    scores = []
    for s in sets:
        label = s.get('label', '')
        if label not in gold_map:
            scores.append(0.0)
            continue
        energy = np.array(s['energy'])
        total_dos = np.array(s['total_dos'])
        # band gap around E=0
        max_dos = np.max(total_dos)
        threshold = 1e-4 * max_dos if max_dos > 0 else 0.0
        if threshold == 0.0:
            scores.append(0.0)
            continue
        below = total_dos < threshold
        # find zero crossing near 0
        idx0 = np.argmin(np.abs(energy))
        if not below[idx0]:
            scores.append(0.0)
            continue
        # expand left and right until above threshold
        left = idx0
        while left > 0 and below[left]:
            left -= 1
        if not below[left]:
            left += 1
        right = idx0
        while right < len(below) - 1 and below[right]:
            right += 1
        if not below[right]:
            right -= 1
        if left >= right:
            scores.append(0.0)
            continue
        gap = energy[right] - energy[left]
        gold = gold_map[label]
        err = abs(gap - gold)
        if err <= tol:
            score = 1.0
        else:
            # linear decay over next tol of extra error
            extra = err - tol
            score = max(0.0, 1.0 - extra / tol) if tol > 0 else (1.0 if err == 0 else 0.0)
        scores.append(score)
    return float(np.mean(scores)) if scores else 0.0


# === block: score_1 (check id='schottky_temp_accuracy') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    step_id = 'schottky_temp_accuracy'
    gold_map = ctx['gold'][step_id]['gold_map']
    tol = ctx['gold'][step_id]['tol']

    sets = artifact.get('parameter_sets', [])
    if not sets:
        return 0.0
    scores = []
    for s in sets:
        label = s.get('label', '')
        if label not in gold_map:
            scores.append(0.0)
            continue
        temp = np.array(s['temperature'])
        total_ehc = np.array(s['total_ehc'])
        idx_peak = np.argmax(total_ehc)
        schottky = temp[idx_peak]
        gold = gold_map[label]
        err = abs(schottky - gold)
        if err <= tol:
            score = 1.0
        else:
            extra = err - tol
            score = max(0.0, 1.0 - extra / tol) if tol > 0 else (1.0 if err == 0 else 0.0)
        scores.append(score)
    return float(np.mean(scores)) if scores else 0.0


_SCORERS = {
    'band_gap_accuracy': score_0,
    'schottky_temp_accuracy': score_1,
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
