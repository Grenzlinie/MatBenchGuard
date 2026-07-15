import os
import json
import csv

# === author imports / helpers ===
import csv, os


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


# === block: score_0 (check id='kappa_lat_summary') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 4: return 0.0
    rows = {}
    for row in artifact:
        comp = str(row.get('composition', '')).strip()
        try:
            r = {
                'kappa300': float(row['kappa_lat_300K']),
                'kappa1000': float(row['kappa_lat_1000K']),
                'red': float(row['reduction_percentage_300K'])
            }
        except (KeyError, ValueError, TypeError):
            return 0.0
        rows[comp] = r
    required = ['TiNiSn', 'Ti0.75Zr0.25NiSn', 'Ti0.75Hf0.25NiSn', 'Ti0.50Mn0.50NiSn']
    if not all(c in rows for c in required):
        return 0.0
    gold = step.get('gold', {})
    tol_kappa = step.get('tol_kappa_relative', 0.10)
    tol_self = step.get('tol_reduction_self_consistency', 0.5)
    total = 0.0
    count = 0
    for comp in required:
        row = rows[comp]
        for tkey in ['300K', '1000K']:
            gk = f'kappa_lat_{tkey}_{comp}'
            gval = gold.get(gk)
            if gval is None:
                continue
            aval = row['kappa300'] if tkey == '300K' else row['kappa1000']
            if abs(gval) < 1e-12:
                ok = (abs(aval) <= 0.01)
            else:
                ok = (abs(aval - gval) / abs(gval) <= tol_kappa)
            count += 1
            total += 1.0 if ok else 0.0
    ref_k300 = rows['TiNiSn']['kappa300']
    if ref_k300 > 0:
        consist_count = 0
        consist_total = 0.0
        for comp in required[1:]:
            sub_k300 = rows[comp]['kappa300']
            expected_red = (1 - sub_k300 / ref_k300) * 100.0
            reported_red = rows[comp]['red']
            consist_ok = (abs(expected_red - reported_red) <= tol_self)
            consist_count += 1
            consist_total += 1.0 if consist_ok else 0.0
        ti_red = rows['TiNiSn']['red']
        if abs(ti_red - 0.0) <= tol_self:
            consist_count += 1
            consist_total += 1.0
        total += consist_total
        count += consist_count
    score = total / count if count > 0 else 0.0
    return score


# === block: score_1 (check id='ti_nisn_properties') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    props = {}
    for row in artifact:
        prop = str(row.get('property', '')).strip()
        try:
            val = float(row['value'])
        except (KeyError, ValueError, TypeError):
            return 0.0
        props[prop] = val
    gold = step.get('gold', {})
    checks = {
        'a0_0K': (gold.get('a0', 0.0), step.get('tol_a0', 0.02)),
        'B0_0K': (gold.get('B0', 0.0), step.get('tol_B0', 5.0)),
        'Debye_temperature_300K': (gold.get('Debye_temperature', 0.0), step.get('tol_theta', 10.0))
    }
    ok = 0
    for prop, (gval, tol) in checks.items():
        if prop not in props:
            continue
        if abs(props[prop] - gval) <= tol:
            ok += 1
    score = ok / len(checks) if checks else 0.0
    return score


_SCORERS = {
    'kappa_lat_summary': score_0,
    'ti_nisn_properties': score_1,
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
