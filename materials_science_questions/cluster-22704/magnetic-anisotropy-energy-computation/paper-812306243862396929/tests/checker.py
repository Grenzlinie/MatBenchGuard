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


# === block: score_0 (check id='ma_energies_step') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    refs = step.get('ref_values', {})
    tol = step.get('tolerances', {}).get('MA_energy_meV_per_unit_area', 0.5)
    config_order = ['FFFFFF/', 'CCCCCC/', 'CCCCFF/']
    values = {}
    for r in rows:
        cfg = r.get('configuration', '').strip()
        try:
            val = float(r['MA_energy_meV_per_unit_area'])
        except (KeyError, ValueError):
            return 0.0
        values[cfg] = val
    # closeness sub-score
    closeness_scores = []
    for cfg in config_order:
        if cfg not in values:
            closeness_scores.append(0.0)
            continue
        v = values[cfg]
        ref = refs.get(cfg)
        if ref is None:
            closeness_scores.append(0.0)
            continue
        diff = abs(v - ref)
        if diff <= tol:
            cs = 1.0
        else:
            cs = max(0.0, 1.0 - (diff - tol) / tol)
        closeness_scores.append(cs)
    closeness = sum(closeness_scores) / len(closeness_scores) if closeness_scores else 0.0
    # structural sub-score: signs and ordering
    struct_ok = True
    for cfg in config_order:
        if cfg not in values:
            struct_ok = False
            break
    fff = values.get('FFFFFF/', None)
    ccc = values.get('CCCCCC/', None)
    ccff = values.get('CCCCFF/', None)
    if fff is not None and fff <= 0:
        struct_ok = False
    if ccc is not None and ccc >= 0:
        struct_ok = False
    if ccff is not None and (ccff <= 0 or (ccc is not None and ccff <= ccc)):
        struct_ok = False
    # combine weights: 0.7 closeness, 0.3 structural
    score = 0.7 * closeness + 0.3 * (1.0 if struct_ok else 0.0)
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='efield_mod_step') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # expect single row for CCCCFF/
    if len(rows) != 1:
        return 0.0
    row = rows[0]
    cfg = row.get('configuration', '').strip()
    if cfg != 'CCCCFF/':
        return 0.0
    try:
        eta = float(row['eta_MA_meV_per_V_per_Angstrom'])
    except (KeyError, ValueError):
        return 0.0
    ref_eta = step.get('ref_eta', 0.5)
    tol = step.get('tolerances', {}).get('eta_MA_meV_per_V_per_Angstrom', 0.2)
    diff = abs(eta - ref_eta)
    if diff <= tol:
        closeness = 1.0
    else:
        closeness = max(0.0, 1.0 - (diff - tol) / tol)
    # structural: must be positive
    struct_ok = eta > 0
    score = 0.7 * closeness + 0.3 * (1.0 if struct_ok else 0.0)
    return max(0.0, min(1.0, score))


_SCORERS = {
    'ma_energies_step': score_0,
    'efield_mod_step': score_1,
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
