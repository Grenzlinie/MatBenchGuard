import os
import json
import csv

# === author imports / helpers ===
import math
import statistics
from collections import defaultdict


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


# === block: score_0 (check id='step_dispersion') ===
def score_0(artifact, step, ctx):
    def _scorer(artifact, step, ctx):
        gold_dict = step['gold_dispersion']
        targets = {
            'X': (0.5, 0.0, 0.0),
            'L': (0.5, 0.5, 0.5),
            'W': (0.5, 0.25, 0.0)
        }
        tol_point = 0.001
        tol_trans = step['tolerance_transverse']
        tol_long = step['tolerance_longitudinal']
        rows = artifact
        qpoint_groups = defaultdict(list)
        for r in rows:
            x = float(r['qpoint_x'])
            y = float(r['qpoint_y'])
            z = float(r['qpoint_z'])
            branch = int(r['branch_index'])
            freq = float(r['frequency'])
            for name, (tx, ty, tz) in targets.items():
                dx = x - tx
                dy = y - ty
                dz = z - tz
                dist = math.sqrt(dx*dx + dy*dy + dz*dz)
                if dist <= tol_point:
                    qpoint_groups[name].append((branch, freq))
                    break
        scores = []
        for name in ['X', 'L', 'W']:
            gold = gold_dict[name]
            items = qpoint_groups.get(name, [])
            if len(items) != 3:
                scores.append(0.0)
                continue
            branch_freqs = {}
            for b, f in items:
                if b in branch_freqs:
                    branch_freqs[b] = (branch_freqs[b] + f) / 2.0
                else:
                    branch_freqs[b] = f
            if set(branch_freqs.keys()) != {0, 1, 2}:
                scores.append(0.0)
                continue
            agent_freqs = sorted([branch_freqs[0], branch_freqs[1], branch_freqs[2]])
            point_score = 0.0
            for i in range(3):
                err = abs(agent_freqs[i] - gold[i])
                tol = tol_long if i == 2 else tol_trans
                if err <= tol:
                    score = 1.0
                else:
                    score = max(0.0, 1.0 - (err - tol) / tol)
                point_score += score
            point_score /= 3.0
            scores.append(point_score)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_dos') ===
def score_1(artifact, step, ctx):
    def _scorer(artifact, step, ctx):
        max_cutoff = step['max_frequency_cutoff']
        min_std = step['min_std']
        rows = artifact
        freqs = []
        vals = []
        for r in rows:
            v = float(r['dos_value'])
            if v > 0:
                freqs.append(float(r['frequency']))
                vals.append(v)
        if not freqs:
            return 0.0
        if max(freqs) > max_cutoff:
            return 0.0
        if len(vals) < 2:
            return 0.0
        if statistics.stdev(vals) < min_std:
            return 0.0
        return 1.0


# === block: score_2 (check id='step_debye') ===
def score_2(artifact, step, ctx):
    def _scorer(artifact, step, ctx):
        gold = step['gold_debye_temp']
        tol_abs = step['tolerance_abs']
        rows = artifact
        debye = None
        for r in rows:
            if abs(float(r['temperature_K']) - 0.0) < 1.0:
                debye = float(r['debye_temperature_K'])
                break
        if debye is None:
            best = None
            best_dist = float('inf')
            for r in rows:
                dist = abs(float(r['temperature_K']) - 0.0)
                if dist < best_dist:
                    best_dist = dist
                    best = float(r['debye_temperature_K'])
            debye = best
        if debye is None:
            return 0.0
        err = abs(debye - gold)
        if err <= tol_abs:
            return 1.0
        return max(0.0, 1.0 - (err - tol_abs) / (2 * tol_abs))


_SCORERS = {
    'step_dispersion': score_0,
    'step_dos': score_1,
    'step_debye': score_2,
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
