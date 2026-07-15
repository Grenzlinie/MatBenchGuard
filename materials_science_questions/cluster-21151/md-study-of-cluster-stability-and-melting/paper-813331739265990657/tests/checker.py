import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import json
import os


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
    autocorr_step = next((s for s in spec.get('steps', []) if s.get('id') == 'step_autocorr'), None)
    viscosity_step = next((s for s in spec.get('steps', []) if s.get('id') == 'step_viscosity'), None)
    reference_params = autocorr_step.get('reference_params', {}) if autocorr_step else {}
    reference_decay = reference_params.get('decay_constant', 0.5)
    viscosity_target = viscosity_step.get('target', 2.5) if viscosity_step else 2.5
    viscosity_tol = viscosity_step.get('tolerance_abs', 0.5) if viscosity_step else 0.5
    viscosity_max_diff = viscosity_step.get('max_diff', 1.5) if viscosity_step else 1.5
    return {'decay_constant': reference_decay, 'viscosity_target': viscosity_target, 'viscosity_tol': viscosity_tol, 'viscosity_max_diff': viscosity_max_diff}


# === block: score_0 (check id='step_autocorr') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    if len(artifact) == 0:
        return 0.0
    rows = []
    for row in artifact:
        try:
            t = float(row['time'])
            c = float(row['autocorrelation'])
        except (ValueError, KeyError):
            return 0.0
        rows.append((t, c))
    rows.sort(key=lambda x: x[0])
    times = [r[0] for r in rows]
    vals = [r[1] for r in rows]
    if max(times) < 2.5:
        return 0.0
    # check that autocorrelation at t=0 is close to 1.0
    idx_0 = min(range(len(times)), key=lambda i: abs(times[i] - 0.0))
    if abs(vals[idx_0] - 1.0) > 0.15:
        return 0.0
    # tail values (time >= 2.5) should be near zero
    tail_vals = [v for t, v in zip(times, vals) if t >= 2.5]
    if not tail_vals:
        return 0.0
    mean_tail = sum(tail_vals) / len(tail_vals)
    target_tail = 0.1
    worst_tail = 0.3
    if mean_tail >= worst_tail:
        return 0.0
    score = max(0.0, min(1.0, (worst_tail - mean_tail) / (worst_tail - target_tail)))
    return score


# === block: score_1 (check id='step_viscosity') ===
def score_1(artifact, step, ctx):
    target = ctx.get('viscosity_target', 2.5)
    tol_abs = ctx.get('viscosity_tol', 0.5)
    max_diff = ctx.get('viscosity_max_diff', 1.5)
    if not artifact or 'shear_viscosity' not in artifact:
        return 0.0
    try:
        v = float(artifact['shear_viscosity'])
    except (ValueError, TypeError):
        return 0.0
    diff = abs(v - target)
    if diff <= tol_abs:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol_abs) / (max_diff - tol_abs))


_SCORERS = {
    'step_autocorr': score_0,
    'step_viscosity': score_1,
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
