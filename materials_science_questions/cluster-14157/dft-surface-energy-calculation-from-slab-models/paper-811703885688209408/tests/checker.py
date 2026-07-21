import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, bisect


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
    ctx = {}
    for step in spec.get('steps', []):
        if step.get('id') == 'calibration_density_check':
            config = step.get('config', {})
            ctx['target_shifts'] = config.get('target_shifts_eV', [0.35, 0.20])
            ctx['reference_densities'] = config.get('reference_densities', [5.5e13, 3.2e13])
            ctx['relative_tolerance'] = config.get('relative_tolerance', 0.20)
            break
    return ctx


# === block: score_0 (check id='calibration_density_check') ===
def score_0(artifact, step, ctx):
    required = ["density (electrons/cm^2)", "fermi_shift (eV)"]
    if not artifact or not all(col in artifact[0] for col in required):
        return 0.0
    rows = []
    for row in artifact:
        try:
            dens = float(row["density (electrons/cm^2)"])
            shift = float(row["fermi_shift (eV)"])
            rows.append((shift, dens))
        except (ValueError, KeyError):
            return 0.0
    if len(rows) < 5:
        return 0.0
    rows_by_density = sorted(rows, key=lambda x: x[1])
    for i in range(1, len(rows_by_density)):
        if rows_by_density[i][0] < rows_by_density[i-1][0] - 1e-12:
            return 0.0
    paired = sorted(rows, key=lambda x: x[0])
    shift_vals = [p[0] for p in paired]
    dens_vals = [p[1] for p in paired]
    target_shifts = ctx['target_shifts']
    ref_densities = ctx['reference_densities']
    tol = ctx['relative_tolerance']
    scores = []
    for target_shift, ref_density in zip(target_shifts, ref_densities):
        if target_shift <= shift_vals[0]:
            est_dens = dens_vals[0]
        elif target_shift >= shift_vals[-1]:
            est_dens = dens_vals[-1]
        else:
            i = bisect.bisect_left(shift_vals, target_shift)
            s0 = shift_vals[i-1]
            s1 = shift_vals[i]
            d0 = dens_vals[i-1]
            d1 = dens_vals[i]
            if s1 - s0 < 1e-15:
                est_dens = d0
            else:
                t = (target_shift - s0) / (s1 - s0)
                est_dens = d0 + t * (d1 - d0)
        if ref_density == 0:
            score_i = 1.0 if est_dens == 0 else 0.0
        else:
            rel_error = abs(est_dens - ref_density) / ref_density
            if rel_error <= tol:
                score_i = 1.0
            elif rel_error >= 2*tol:
                score_i = 0.0
            else:
                score_i = (2*tol - rel_error) / tol
        scores.append(score_i)
    return sum(scores) / len(scores)


_SCORERS = {
    'calibration_density_check': score_0,
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
