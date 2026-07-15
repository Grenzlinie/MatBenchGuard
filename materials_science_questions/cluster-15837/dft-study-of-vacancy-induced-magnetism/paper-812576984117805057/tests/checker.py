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


# === block: score_0 (check id='dbar_ratio') ===
def score_0(artifact, step, ctx):
    data = artifact
    mom = []
    rat = []
    for row in data:
        mom.append(float(row['momentum']))
        rat.append(float(row['ratio']))

    def get_at_p(target):
        best = None
        best_dist = float('inf')
        for i, m in enumerate(mom):
            d = abs(m - target)
            if d < best_dist:
                best_dist = d
                best = rat[i]
        return best

    # Hidden gold points derived from theoretical V12 ratio curve (Fig. 3)
    gold = {
        0.0: 1.12,
        0.005: 1.07,
        0.010: 1.03,
        0.015: 1.01,
    }
    tol = 0.03  # per‑point tolerance
    num_points = len(gold)
    errors = []
    for p, expected in gold.items():
        agent_val = get_at_p(p)
        if agent_val is None:
            errors.append(1.0)
        else:
            errors.append(abs(agent_val - expected))
    mae = sum(errors) / num_points
    two_tol = 2.0 * tol
    if mae <= tol:
        score = 1.0
    elif mae >= two_tol:
        score = 0.0
    else:
        score = (two_tol - mae) / tol
    return score


# === block: score_1 (check id='mdb_diff') ===
def score_1(artifact, step, ctx):
    data = artifact
    mom = []
    intens = []
    for row in data:
        mom.append(float(row['momentum']))
        intens.append(float(row['differential_intensity']))
    config = step.get('config', {})
    peak_thresh = config.get('peak_intensity_threshold', 0.005)
    peak_window = config.get('peak_momentum_window', 0.002)
    tail_thresh = config.get('tail_intensity_threshold', 0.002)
    tail_start = config.get('tail_momentum_start', 0.010)
    # find peak
    max_int = None
    max_mom = None
    for m, i in zip(mom, intens):
        if max_int is None or i > max_int:
            max_int = i
            max_mom = m
    peak_ok = 1.0 if max_int is not None and max_int >= peak_thresh else 0.0
    center_ok = 1.0 if max_mom is not None and abs(max_mom) < peak_window else 0.0
    # tail check: max |intensity| for p >= tail_start
    max_tail = 0.0
    for m, i in zip(mom, intens):
        if m >= tail_start and abs(i) > max_tail:
            max_tail = abs(i)
    tail_ok = 1.0 if max_tail < tail_thresh else 0.0
    score = (peak_ok + center_ok + tail_ok) / 3.0
    return score


# === block: score_2 (check id='magnetization') ===
def score_2(artifact, step, ctx):
    raw = artifact.strip()
    try:
        val = float(raw)
    except:
        return 0.0
    cfg = step.get('config', {})
    target = cfg.get('target', 4.0)
    tol = cfg.get('tolerance_abs', 0.2)
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'dbar_ratio': score_0,
    'mdb_diff': score_1,
    'magnetization': score_2,
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
