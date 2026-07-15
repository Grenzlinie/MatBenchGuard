import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='geom_check') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # dict
    config = step['config']
    tol_len = config['tol_length']
    tol_ang = config['tol_angle']

    def check_method(prefix, lengths_gold, angles_gold):
        data = artifact.get(prefix, {})
        lengths = data.get('bond_lengths', {})
        angles = data.get('bond_angles', {})
        total = 0
        ok = 0
        for name, val in lengths_gold.items():
            total += 1
            sub = lengths.get(name, None)
            if sub is not None and abs(sub - val) <= tol_len:
                ok += 1
        for name, val in angles_gold.items():
            total += 1
            sub = angles.get(name, None)
            if sub is not None and abs(sub - val) <= tol_ang:
                ok += 1
        return ok, total

    ok_hf, tot_hf = check_method('hf', config['gold_hf_lengths'], config['gold_hf_angles'])
    ok_b3, tot_b3 = check_method('b3lyp', config['gold_b3lyp_lengths'], config['gold_b3lyp_angles'])
    score = (ok_hf + ok_b3) / max(1, tot_hf + tot_b3)
    return score


# === block: score_1 (check id='freq_check') ===
def score_1(artifact, step, ctx):
    artifact = artifact  # dict
    hf_sub = artifact.get('hf', [])
    b3_sub = artifact.get('b3lyp', [])
    if not isinstance(hf_sub, list) or not isinstance(b3_sub, list):
        return 0.0
    hf_sort = sorted(hf_sub)
    b3_sort = sorted(b3_sub)
    config = step['config']
    gold_hf = config['gold_hf_sorted']
    gold_b3 = config['gold_b3lyp_sorted']
    thresh = config['rmse_threshold']

    def rmse(vals, target):
        if len(vals) != len(target):
            return float('inf')
        n = len(vals)
        ss = sum((v - t) ** 2 for v, t in zip(vals, target))
        return math.sqrt(ss / n)

    rmse_hf = rmse(hf_sort, gold_hf)
    rmse_b3 = rmse(b3_sort, gold_b3)
    def score_rmse(r):
        return max(0.0, 1.0 - r / thresh)
    score = (score_rmse(rmse_hf) + score_rmse(rmse_b3)) / 2.0
    return score


_SCORERS = {
    'geom_check': score_0,
    'freq_check': score_1,
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
