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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance', 0.5)
    # artifact is list of dicts with keys 'system','formation_energy_eV'
    rows = {row['system']: float(row['formation_energy_eV']) for row in artifact if row.get('system')}
    if not rows: return 0.0
    score = 0.0
    n = 0
    for sys, target in targets.items():
        val = rows.get(sys)
        if val is None or math.isnan(val) or math.isinf(val):
            continue
        diff = abs(val - target)
        if diff <= tol:
            score += 1.0
        else:
            # partial credit: linear decay with distance, capped at 0
            credit = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
            score += credit
        n += 1
    if n == 0: return 0.0
    return score / n


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance', 0.2)
    rows = {row['system']: float(row['band_gap_eV']) for row in artifact if row.get('system')}
    if not rows: return 0.0
    score = 0.0
    n = 0
    for sys, target in targets.items():
        val = rows.get(sys)
        if val is None or math.isnan(val) or math.isinf(val):
            continue
        diff = abs(val - target)
        if diff <= tol:
            score += 1.0
        else:
            credit = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
            score += credit
        n += 1
    if n == 0: return 0.0
    return score / n


# === block: score_2 (check id='absorption_coefficient') ===
def score_2(artifact, step, ctx):
    config = step.get('config', {})
    ref_sys = config.get('reference_system', 'pristine')
    energies = config.get('energies', [])
    doped = config.get('doped_systems', [])
    if not energies or not doped:
        return 0.0
    # build lookup: dict (energy, system) -> absorption
    data = {}
    for row in artifact:
        try:
            e = float(row['energy_eV'])
            sys = row['system']
            a = float(row['absorption_cm1'])
            data[(e, sys)] = a
        except (KeyError, ValueError):
            continue
    passes = 0
    total = 0
    for e in energies:
        pristine_abs = data.get((e, ref_sys))
        if pristine_abs is None:
            continue
        for d in doped:
            d_abs = data.get((e, d))
            if d_abs is None:
                continue
            if d_abs > pristine_abs:
                passes += 1
            total += 1
    if total == 0: return 0.0
    return passes / total


# === block: score_3 (check id='band_edges') ===
def score_3(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance', 0.2)
    fields = ['VBM_vacuum','CBM_vacuum','VBM_NHE','CBM_NHE']
    rows = {}
    for row in artifact:
        sys = row.get('system')
        if not sys: continue
        try:
            rows[sys] = {f: float(row[f]) for f in fields}
        except (KeyError, ValueError):
            continue
    if not rows: return 0.0
    total_points = sum(len(fields) for _ in targets)
    score = 0.0
    n = 0
    for sys, ref in targets.items():
        if sys not in rows: continue
        vals = rows[sys]
        for f in fields:
            target = ref.get(f)
            val = vals.get(f)
            if target is None or val is None or math.isnan(val) or math.isinf(val):
                continue
            diff = abs(val - target)
            if diff <= tol:
                score += 1.0
            else:
                credit = max(0.0, 1.0 - (diff - tol) / (2.0 * tol))
                score += credit
            n += 1
    if n == 0: return 0.0
    return score / n


_SCORERS = {
    'formation_energies': score_0,
    'band_gaps': score_1,
    'absorption_coefficient': score_2,
    'band_edges': score_3,
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
