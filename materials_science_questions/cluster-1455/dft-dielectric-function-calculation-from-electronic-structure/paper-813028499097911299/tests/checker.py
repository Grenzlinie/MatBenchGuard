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


# === block: score_0 (check id='band_gap_trend') ===
def score_0(artifact, step, ctx):
    rows = {}
    for r in artifact:
        try:
            s = int(r.get('strain_percent'))
            g = float(r.get('band_gap_eV'))
            rows[s] = g
        except (ValueError, TypeError):
            continue
    for s in [-8, 0, 8]:
        if s not in rows:
            return 0.0
    gap_neg8 = rows[-8]
    gap_0 = rows[0]
    gap_8 = rows[8]
    cond1 = gap_neg8 < gap_0 - 0.2
    cond2 = abs(gap_8 - gap_0) <= 0.1
    score = 0.0
    if cond1:
        score += 0.5
    if cond2:
        score += 0.5
    return score


# === block: score_1 (check id='dielectric_peak') ===
def score_1(artifact, step, ctx):
    window = step.get('peak_window', [4.2, 4.8])
    strain_neg = step.get('strain_neg', -8)
    strain_ref = step.get('strain_ref', 0)
    min_ratio = step.get('min_ratio', 1.3)
    eps2_neg = []
    eps2_ref = []
    for r in artifact:
        try:
            s = int(r.get('strain_percent'))
            e = float(r.get('energy_eV'))
            e2 = float(r.get('epsilon2'))
            if e < window[0] or e > window[1]:
                continue
            if s == strain_neg:
                eps2_neg.append((e, e2))
            elif s == strain_ref:
                eps2_ref.append((e, e2))
        except (ValueError, TypeError):
            continue
    if not eps2_neg or not eps2_ref:
        return 0.0
    max_e, max_val = max(eps2_neg, key=lambda x: x[1])
    eps2_ref_sorted = sorted(eps2_ref, key=lambda x: abs(x[0] - max_e))
    ref_val = eps2_ref_sorted[0][1]
    if ref_val < 1e-6:
        ratio = 1e9
    else:
        ratio = max_val / ref_val
    if ratio >= min_ratio:
        return 1.0
    if ratio >= 1.0:
        return (ratio - 1.0) / (min_ratio - 1.0)
    return 0.0


_SCORERS = {
    'band_gap_trend': score_0,
    'dielectric_peak': score_1,
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
