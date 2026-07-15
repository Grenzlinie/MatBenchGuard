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


# === block: score_0 (check id='thermal_conductivity_300K') ===
def score_0(artifact, step, ctx):
    target = step.get('target', 645)
    tol = step.get('tolerance', 50)
    rows = artifact
    k_lat = None
    for r in rows:
        try:
            T = float(r['Temperature_K'])
            if abs(T - 300.0) < 0.5:
                k_lat = float(r['K_lat_W_mK'])
                break
        except (ValueError, KeyError):
            continue
    if k_lat is None:
        return 0.0
    diff = abs(k_lat - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_1 (check id='power_law_exponent') ===
def score_1(artifact, step, ctx):
    target = step.get('target', 0.735)
    tol = step.get('tolerance', 0.05)
    rows = artifact
    xs, ys = [], []
    for r in rows:
        try:
            t = float(r['Temperature_K'])
            k = float(r['K_lat_W_mK'])
            if t > 0 and k > 0:
                xs.append(math.log(t))
                ys.append(math.log(k))
        except (ValueError, KeyError):
            continue
    if len(xs) < 3:
        return 0.0
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x*y for x,y in zip(xs,ys))
    sum_x2 = sum(x*x for x in xs)
    deno = n*sum_x2 - sum_x*sum_x
    if abs(deno) < 1e-12:
        return 0.0
    slope = (n*sum_xy - sum_x*sum_y) / deno
    alpha = -slope
    diff = abs(alpha - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='rta_ratio_at_300K') ===
def score_2(artifact, step, ctx):
    rows = artifact
    k_lat = k_rta = None
    for r in rows:
        try:
            if abs(float(r['Temperature_K']) - 300.0) < 0.5:
                k_lat = float(r['K_lat_W_mK'])
                k_rta = float(r['K_RTA_W_mK'])
                break
        except (ValueError, KeyError):
            continue
    if k_lat is None or k_lat == 0:
        return 0.0
    ratio = k_rta / k_lat
    if 0.4 <= ratio <= 0.6:
        return 1.0
    return 0.0


# === block: score_3 (check id='za_contribution') ===
def score_3(artifact, step, ctx):
    target = step.get('target', 60.0)
    tol = step.get('tolerance', 5.0)
    rows = artifact
    za_pct = None
    for r in rows:
        try:
            if r['phonon_branch'].strip().upper() == 'ZA':
                za_pct = float(r['contribution_percentage'])
                break
        except (ValueError, KeyError):
            continue
    if za_pct is None:
        return 0.0
    diff = abs(za_pct - target)
    if diff <= tol:
        return 1.0
    return max(0.0, 1.0 - (diff - tol) / tol)


_SCORERS = {
    'thermal_conductivity_300K': score_0,
    'power_law_exponent': score_1,
    'rta_ratio_at_300K': score_2,
    'za_contribution': score_3,
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
