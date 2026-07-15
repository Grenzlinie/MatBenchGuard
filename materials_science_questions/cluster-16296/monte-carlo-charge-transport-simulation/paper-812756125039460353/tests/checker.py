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


# === block: score_0 (check id='mu_eff_mu1_structural') ===
def score_0(artifact, step, ctx):
    data = artifact.get('mu_eff_mu1_vs_r', [])
    if not data:
        return 0.0
    from collections import defaultdict
    curves = defaultdict(list)
    for pt in data:
        curves[pt['gamma']].append((pt['r'], pt['value']))
    req_gammas = {2,3,4,5}
    if not req_gammas.issubset(set(curves.keys())):
        return 0.0
    checks = []
    peak_vals = {}
    for g in [2,3,4,5]:
        points = sorted(curves[g], key=lambda x: x[0])
        if not points:
            return 0.0
        start_val = min(points, key=lambda x: x[0])[1]
        checks.append(0.9 < start_val < 1.05)
        max_val = max(p[1] for p in points)
        peak_vals[g] = max_val
        if g == 5:
            checks.append(1.14 < max_val < 1.38)
        for _,v in points:
            if v < 0.8 or v > 1.5:
                return 0.0
            break
        end_val = max(points, key=lambda x: x[0])[1]
        checks.append(abs(end_val - 1.0) < 0.05)
    checks.append(peak_vals[2] < peak_vals[3] and peak_vals[3] < peak_vals[4] and peak_vals[4] < peak_vals[5])
    for g in req_gammas:
        if len(curves[g]) < 5:
            return 0.0
    score = sum(checks) / len(checks) if checks else 0.0
    return score


# === block: score_1 (check id='mu2_mu1_structural') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('mu2_mu1_vs_r', [])
        if not data:
            return 0.0
        # sort by r
        data_sorted = sorted(data, key=lambda x: x['r'])
        if len(data_sorted) < 5:
            return 0.0
        checks = []
        # start near 1
        start_val = data_sorted[0]['value']
        checks.append(abs(start_val - 1.0) < 0.05)
        # monotonic decrease
        monotonic = all(data_sorted[i]['value'] >= data_sorted[i+1]['value'] for i in range(len(data_sorted)-1))
        checks.append(monotonic)
        # value at r~10 should be < 2.0
        r10_vals = [p['value'] for p in data_sorted if abs(p['r'] - 10.0) < 0.1]
        if r10_vals:
            checks.append(r10_vals[0] < 2.2)
        else:
            # approximate with nearest
            pass
        # value at large r (~>=40) near 1
        large_r = [p for p in data_sorted if p['r'] >= 40]
        if large_r:
            checks.append(all(abs(p['value'] - 1.0) < 0.1 for p in large_r))
        else:
            # check end
            checks.append(abs(data_sorted[-1]['value'] - 1.0) < 0.1)
        # also check that all values are positive (<2.0)
        for p in data_sorted:
            if p['value'] < 0.5 or p['value'] > 2.5:
                return 0.0
        score = sum(checks) / len(checks) if checks else 0.0
        return score


# === block: score_2 (check id='rH_vs_gamma_structural') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('rH_vs_gamma', [])
        if not data:
            return 0.0
        # sort by gamma
        data_sorted = sorted(data, key=lambda x: x['gamma'])
        if len(data_sorted) < 5:
            return 0.0
        checks = []
        # find value at gamma ~0.5
        gamma05 = [p['value'] for p in data_sorted if abs(p['gamma'] - 0.5) < 0.05]
        if gamma05:
            checks.append(1.8 < gamma05[0] < 2.2)
        else:
            # use smallest gamma
            first = data_sorted[0]
            if first['gamma'] < 0.75:
                checks.append(1.6 < first['value'] < 2.4)
        # monotonic decrease
        monotonic = all(data_sorted[i]['value'] >= data_sorted[i+1]['value'] for i in range(len(data_sorted)-1))
        checks.append(monotonic)
        # value at gamma=5 near 1
        gamma5 = [p['value'] for p in data_sorted if abs(p['gamma'] - 5.0) < 0.05]
        if gamma5:
            checks.append(abs(gamma5[0] - 1.0) < 0.15)
        else:
            last_val = data_sorted[-1]['value']
            checks.append(abs(last_val - 1.0) < 0.15)
        # all values positive, < 2.5
        for p in data_sorted:
            if p['value'] < 1.0 or p['value'] > 2.5:
                return 0.0
                break
        score = sum(checks) / len(checks) if checks else 0.0
        return score


_SCORERS = {
    'mu_eff_mu1_structural': score_0,
    'mu2_mu1_structural': score_1,
    'rH_vs_gamma_structural': score_2,
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
