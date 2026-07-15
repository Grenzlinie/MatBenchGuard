import os
import json
import csv

# === author imports / helpers ===
import math
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


# === block: score_0 (check id='caseII_ratio') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = defaultdict(list)
    for row in artifact:
        try:
            m = int(row["m"])
            L = float(row["L_over_b"])
            sigma = float(row["sigma_over_G"])
            if L <= 0 or sigma <= 0:
                continue
            groups[m].append((L, sigma))
        except (ValueError, KeyError):
            continue
    if len(groups) < 2:
        return 0.0
    slopes = {}
    for m_val, pts in groups.items():
        if len(pts) < 3:
            continue
        sum_xy = sum((1.0 / math.sqrt(L)) * s for L, s in pts)
        sum_xx = sum(1.0 / L for L, _ in pts)
        if sum_xx == 0:
            continue
        slopes[m_val] = sum_xy / sum_xx
    if 1 not in slopes or 2 not in slopes:
        return 0.0
    ratio = slopes[2] / slopes[1]
    target = step["target"]
    tol = step["tolerance_relative"]
    rel_err = abs(ratio - target) / target
    return 1.0 if rel_err <= tol else 0.0


# === block: score_1 (check id='caseII_fit') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = defaultdict(list)
    for row in artifact:
        try:
            m = int(row["m"])
            L = float(row["L_over_b"])
            sigma = float(row["sigma_over_G"])
            if L <= 0 or sigma <= 0:
                continue
            groups[m].append((L, sigma))
        except (ValueError, KeyError):
            continue
    r2_vals = []
    for m_val, pts in groups.items():
        if len(pts) < 3:
            continue
        X = [1.0 / math.sqrt(L) for L, _ in pts]
        Y = [s for _, s in pts]
        sum_xy = sum(x * y for x, y in zip(X, Y))
        sum_xx = sum(x * x for x in X)
        if sum_xx == 0:
            continue
        slope = sum_xy / sum_xx
        ss_res = sum((y - slope * x) ** 2 for x, y in zip(X, Y))
        ss_tot = sum(y * y for y in Y)
        if ss_tot == 0:
            r2 = 1.0
        else:
            r2 = 1 - ss_res / ss_tot
        r2_vals.append(r2)
    if not r2_vals:
        return 0.0
    min_r2 = min(r2_vals)
    target = step["target"]
    return 1.0 if min_r2 >= target - 1e-9 else 0.0


# === block: score_2 (check id='caseI_ratio') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = defaultdict(list)
    for row in artifact:
        try:
            K = float(row["K"])
            L = float(row["L_over_b"])
            sigma = float(row["sigma_over_G"])
            if L <= 0 or sigma <= 0:
                continue
            groups[K].append((L, sigma))
        except (ValueError, KeyError):
            continue
    if len(groups) < 2:
        return 0.0
    slopes = {}
    for K_val, pts in groups.items():
        if len(pts) < 3:
            continue
        sum_xy = sum((1.0 / math.sqrt(L)) * s for L, s in pts)
        sum_xx = sum(1.0 / L for L, _ in pts)
        if sum_xx == 0:
            continue
        slopes[K_val] = sum_xy / sum_xx
    if 0.0 not in slopes or 0.5 not in slopes:
        return 0.0
    ratio = slopes[0.5] / slopes[0.0]
    target = step["target"]
    tol = step["tolerance_relative"]
    rel_err = abs(ratio - target) / target
    return 1.0 if rel_err <= tol else 0.0


# === block: score_3 (check id='caseI_fit') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = defaultdict(list)
    for row in artifact:
        try:
            K = float(row["K"])
            L = float(row["L_over_b"])
            sigma = float(row["sigma_over_G"])
            if L <= 0 or sigma <= 0:
                continue
            groups[K].append((L, sigma))
        except (ValueError, KeyError):
            continue
    r2_vals = []
    for K_val, pts in groups.items():
        if len(pts) < 3:
            continue
        X = [1.0 / math.sqrt(L) for L, _ in pts]
        Y = [s for _, s in pts]
        sum_xy = sum(x * y for x, y in zip(X, Y))
        sum_xx = sum(x * x for x in X)
        if sum_xx == 0:
            continue
        slope = sum_xy / sum_xx
        ss_res = sum((y - slope * x) ** 2 for x, y in zip(X, Y))
        ss_tot = sum(y * y for y in Y)
        if ss_tot == 0:
            r2 = 1.0
        else:
            r2 = 1 - ss_res / ss_tot
        r2_vals.append(r2)
    if not r2_vals:
        return 0.0
    min_r2 = min(r2_vals)
    target = step["target"]
    return 1.0 if min_r2 >= target - 1e-9 else 0.0


_SCORERS = {
    'caseII_ratio': score_0,
    'caseII_fit': score_1,
    'caseI_ratio': score_2,
    'caseI_fit': score_3,
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
