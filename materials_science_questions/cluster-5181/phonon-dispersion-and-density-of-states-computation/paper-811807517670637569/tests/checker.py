import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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


# === block: score_0 (check id='step_phonon_properties') ===
def score_0(artifact, step, ctx):
    reference_sets = [
        {
            "C11_GPa": 411.5,
            "C12_GPa": 219.5,
            "C44_GPa": 163.0,
            "Bulk_modulus_GPa": 283.5,
            "X_longitudinal_THz": 7.15,
            "X_transverse_THz": 5.56
        },
        {
            "C11_GPa": 481.8,
            "C12_GPa": 221.9,
            "C44_GPa": 205.6,
            "Bulk_modulus_GPa": 308.5,
            "X_longitudinal_THz": 7.25,
            "X_transverse_THz": 5.80
        }
    ]
    tolerances = {
        "C11_GPa": 0.10,
        "C12_GPa": 0.10,
        "C44_GPa": 0.10,
        "Bulk_modulus_GPa": 0.10,
        "X_longitudinal_THz": 0.05,
        "X_transverse_THz": 0.05
    }
    if not isinstance(artifact, dict):
        return 0.0
    scores = []
    for fname in tolerances:
        val = artifact.get(fname)
        if val is None:
            scores.append(0.0)
            continue
        try:
            val = float(val)
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        min_err = float('inf')
        for ref in reference_sets:
            gold = ref.get(fname)
            if gold is None:
                continue
            if gold == 0.0:
                if val == 0.0:
                    min_err = 0.0
                else:
                    min_err = min(min_err, 1.0)
            else:
                rel = abs(val - gold) / abs(gold)
                if rel < min_err:
                    min_err = rel
        if min_err == float('inf'):
            scores.append(0.0)
        else:
            tol = tolerances[fname]
            scores.append(1.0 if min_err <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_anomaly_data') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    params = step.get('params', {})
    q_lo = float(params.get('q_min_range', 0.1))
    q_hi = float(params.get('q_max_range', 0.5))
    q_tol = float(params.get('coincidence_tolerance_q', 0.02))
    depth_th = float(params.get('depth_threshold', 0.1))
    rows = []
    for row in artifact:
        try:
            q = float(row.get('q', None))
            m2 = float(row.get('momega2', None))
            d2 = float(row.get('D2approx', None))
            if q is None or m2 is None or d2 is None:
                continue
            if q_lo <= q <= q_hi:
                rows.append({'q': q, 'momega2': m2, 'D2approx': d2})
        except (ValueError, TypeError):
            continue
    if not rows:
        return 0.0
    # find minimum momega2
    min_m2_row = min(rows, key=lambda r: r['momega2'])
    q_min = min_m2_row['q']
    # find maximum D2approx
    max_d2_row = max(rows, key=lambda r: r['D2approx'])
    q_max = max_d2_row['q']
    # global max momega2 in range
    max_m2 = max(r['momega2'] for r in rows)
    min_m2 = min_m2_row['momega2']
    coincidence_ok = abs(q_min - q_max) <= q_tol
    depth = (max_m2 - min_m2) / max_m2 if max_m2 > 0 else 0.0
    depth_ok = depth >= depth_th
    return 0.5 * float(coincidence_ok) + 0.5 * float(depth_ok)


_SCORERS = {
    'step_phonon_properties': score_0,
    'step_anomaly_data': score_1,
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
