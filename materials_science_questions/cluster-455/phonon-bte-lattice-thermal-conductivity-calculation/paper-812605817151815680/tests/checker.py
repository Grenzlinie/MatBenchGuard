import os
import json
import csv

# === author imports / helpers ===
import math
from collections import OrderedDict


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
    def cumulative(kappa_max, mfp, median=0.2, sigma=1.163):
        if mfp <= 0:
            return 0.0
        x = (math.log(mfp) - math.log(median)) / (sigma * math.sqrt(2))
        cdf = 0.5 * (1.0 + math.erf(x))
        return kappa_max * cdf

    ref_mfp_points = [0.1, 0.5, 1.0, 5.0, 10.0]
    ref_accumulation = []
    for mfp in ref_mfp_points:
        k_in = cumulative(380.0, mfp)
        k_cross = cumulative(320.0, mfp)
        ref_accumulation.append({"mfp": mfp, "k_in": k_in, "k_cross": k_cross})

    ctx = {
        "ref_accumulation": ref_accumulation,
        "bulk_gold_in": 380.0,
        "bulk_gold_cross": 320.0
    }
    return ctx


# === block: score_0 (check id='accumulation_csv') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 50:
        return 0.0

    cols_set = set(rows[0].keys())
    if not cols_set.issuperset({"mfp_um", "kappa_in_plane", "kappa_cross_plane"}):
        return 0.0

    rows = sorted(rows, key=lambda r: float(r["mfp_um"]))
    mfp = [float(r["mfp_um"]) for r in rows]
    kin = [float(r["kappa_in_plane"]) for r in rows]
    kcross = [float(r["kappa_cross_plane"]) for r in rows]

    mono_in = all(kin[i] <= kin[i+1] for i in range(len(kin)-1))
    mono_cross = all(kcross[i] <= kcross[i+1] for i in range(len(kcross)-1))
    mono_score = 1.0 if (mono_in and mono_cross) else 0.0

    def interp_mfp(xs, ys, y_target):
        if y_target <= ys[0]:
            return xs[0]
        if y_target >= ys[-1]:
            return xs[-1]
        for i in range(1, len(ys)):
            if ys[i] >= y_target:
                x0, x1 = xs[i-1], xs[i]
                y0, y1 = ys[i-1], ys[i]
                if y1 - y0 == 0:
                    return (x0 + x1) / 2.0
                t = (y_target - y0) / (y1 - y0)
                return x0 + t * (x1 - x0)
        return xs[-1]

    max_in = kin[-1] if kin else 0.0
    max_cross = kcross[-1] if kcross else 0.0
    if max_in <= 0 or max_cross <= 0:
        return 0.0

    mfp50_in = interp_mfp(mfp, kin, 0.5 * max_in)
    mfp50_cross = interp_mfp(mfp, kcross, 0.5 * max_cross)

    mfp95_in = interp_mfp(mfp, kin, 0.95 * max_in)
    mfp95_cross = interp_mfp(mfp, kcross, 0.95 * max_cross)

    def quantile_score(mfp_val, target, tol):
        return max(0.0, 1.0 - abs(mfp_val - target) / tol)

    target50 = 0.2
    tol50 = 0.2
    target95 = 3.0
    tol95 = 1.5

    score50_in = quantile_score(mfp50_in, target50, tol50)
    score50_cross = quantile_score(mfp50_cross, target50, tol50)
    score50 = (score50_in + score50_cross) / 2.0

    score95_in = quantile_score(mfp95_in, target95, tol95)
    score95_cross = quantile_score(mfp95_cross, target95, tol95)
    score95 = (score95_in + score95_cross) / 2.0

    overall = 0.1 * mono_score + 0.45 * score50 + 0.45 * score95
    return overall


# === block: score_1 (check id='bulk_kappa_json') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0

    in_val = float(data.get("kappa_in_plane_300K", 0))
    cross_val = float(data.get("kappa_cross_plane_300K", 0))

    gold_in = ctx["bulk_gold_in"]
    gold_cross = ctx["bulk_gold_cross"]

    def directional_score(val, ref):
        if val >= ref:
            return 1.0
        # gradient decay: lose 1/4 fraction of score per 50% deficit
        deficit_ratio = (ref - val) / ref if ref > 0 else 0
        return max(0.0, 1.0 - 4.0 * deficit_ratio)

    score_in = directional_score(in_val, gold_in)
    score_cross = directional_score(cross_val, gold_cross)
    return (score_in + score_cross) / 2.0


_SCORERS = {
    'accumulation_csv': score_0,
    'bulk_kappa_json': score_1,
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
