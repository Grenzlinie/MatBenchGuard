import os
import json
import csv

# === author imports / helpers ===
import csv
import math


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


# === block: score_0 (check id='check_csv_shape') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact:
            return 0.0
        required = ['electron_concentration_cm3', 'zT_bulk', 'zT_barrier']
        if not all(c in artifact[0] for c in required):
            return 0.0
        try:
            for row in artifact:
                float(row['electron_concentration_cm3'])
                float(row['zT_bulk'])
                float(row['zT_barrier'])
        except (ValueError, KeyError):
            return 0.0
        return 1.0


# === block: score_1 (check id='check_zT_values') ===
def score_1(artifact, step, ctx):
    config = step.get('config', {})
    ref_concs = config['concentrations']
    ref_bulk = config['zT_bulk_ref']
    ref_barrier = config['zT_barrier_ref']
    tol_below = config.get('max_relative_error', 0.15)
    data = {}
    for row in artifact:
        conc = float(row['electron_concentration_cm3'])
        data[conc] = (float(row['zT_bulk']), float(row['zT_barrier']))
    concentrations_list = sorted(data.keys())
    point_scores = []
    for c, rb, rbr in zip(ref_concs, ref_bulk, ref_barrier):
        best_conc = min(concentrations_list, key=lambda x: abs(x - c))
        if abs(best_conc - c) / c > 0.01:
            continue
        bulk, barrier = data[best_conc]
        # bulk score
        if rb > 0:
            ratio = bulk / rb
            if ratio >= 1 - tol_below:
                s = 1.0
            else:
                s = max(0.0, ratio / (1 - tol_below))
        else:
            s = 1.0 if bulk == 0 else 0.0
        point_scores.append(s)
        # barrier score
        if rbr > 0:
            ratio = barrier / rbr
            if ratio >= 1 - tol_below:
                s = 1.0
            else:
                s = max(0.0, ratio / (1 - tol_below))
        else:
            s = 1.0 if barrier == 0 else 0.0
        point_scores.append(s)
    if not point_scores:
        return 0.0
    return sum(point_scores) / len(point_scores)


# === block: score_2 (check id='check_peak_zT') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step['config']
        bulk_thresh = config['bulk_peak_threshold']
        barrier_thresh = config['barrier_peak_threshold']
        peak_bulk = 0.0
        peak_barrier = 0.0
        for row in artifact:
            bulk = float(row['zT_bulk'])
            barrier = float(row['zT_barrier'])
            if bulk > peak_bulk:
                peak_bulk = bulk
            if barrier > peak_barrier:
                peak_barrier = barrier
        score_bulk = min(1.0, peak_bulk / bulk_thresh)
        score_barrier = min(1.0, peak_barrier / barrier_thresh)
        return (score_bulk + score_barrier) / 2.0


# === block: score_3 (check id='check_peak_concentration') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        config = step['config']
        bulk_range = config['bulk_conc_range']
        barrier_range = config['barrier_conc_range']
        bulk_peak_conc = None
        barrier_peak_conc = None
        bulk_max = -1.0
        barrier_max = -1.0
        for row in artifact:
            bulk = float(row['zT_bulk'])
            barrier = float(row['zT_barrier'])
            conc = float(row['electron_concentration_cm3'])
            if bulk > bulk_max:
                bulk_max = bulk
                bulk_peak_conc = conc
            if barrier > barrier_max:
                barrier_max = barrier
                barrier_peak_conc = conc
        ok_bulk = (bulk_peak_conc is not None and bulk_range[0] <= bulk_peak_conc <= bulk_range[1])
        ok_barrier = (barrier_peak_conc is not None and barrier_range[0] <= barrier_peak_conc <= barrier_range[1])
        return (1.0 if ok_bulk else 0.0) * 0.5 + (1.0 if ok_barrier else 0.0) * 0.5


_SCORERS = {
    'check_csv_shape': score_0,
    'check_zT_values': score_1,
    'check_peak_zT': score_2,
    'check_peak_concentration': score_3,
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
