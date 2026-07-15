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


# === block: score_0 (check id='step_meanfield') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    T = []
    spin_low = []
    spin_high = []
    for row in artifact:
        try:
            t = float(row.get('T', None))
            sl = float(row.get('rho_spin_low', None))
            sh = float(row.get('rho_spin_high', None))
            if t is not None and sl is not None and sh is not None:
                T.append(t)
                spin_low.append(sl)
                spin_high.append(sh)
        except:
            pass
    if not T:
        return 0.0
    # critical temperature as T where |spin_low - spin_high| is minimal
    min_diff = float('inf')
    T_c = None
    for t, sl, sh in zip(T, spin_low, spin_high):
        diff = abs(sl - sh)
        if diff < min_diff:
            min_diff = diff
            T_c = t
    score_crit = 0.0
    if T_c is not None:
        if 1.425 <= T_c <= 1.575:
            score_crit = 0.5
        else:
            dist = abs(T_c - 1.5)
            if dist <= 0.2:
                score_crit = 0.5 * max(0.0, 1.0 - (dist - 0.075) / 0.125)
            else:
                score_crit = 0.0
    # reentrance: spin_low at T_lo=0.2 > spin_low at T_hi=0.8
    def find_closest(target, Tvals, vals):
        best = None
        best_dist = float('inf')
        for t, v in zip(Tvals, vals):
            d = abs(t - target)
            if d < best_dist:
                best_dist = d
                best = v
        return best
    rho_lo = find_closest(0.2, T, spin_low)
    rho_hi = find_closest(0.8, T, spin_low)
    score_reent = 0.0
    if rho_lo is not None and rho_hi is not None:
        if rho_lo > rho_hi:
            score_reent = 0.5
    return score_crit + score_reent


# === block: score_1 (check id='step_exponent') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    text = artifact.strip() if isinstance(artifact, str) else ''
    if not text:
        return 0.0
    try:
        val = float(text)
    except:
        return 0.0
    target = float(step.get('target', 3.5))
    tolerance = float(step.get('tolerance', 0.1))
    abs_val = abs(val)
    err = abs(abs_val - target)
    if err <= tolerance:
        return 1.0
    max_err = 0.5
    if err >= max_err:
        return 0.0
    return (max_err - err) / (max_err - tolerance)


_SCORERS = {
    'step_meanfield': score_0,
    'step_exponent': score_1,
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
