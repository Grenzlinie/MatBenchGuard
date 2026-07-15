import os
import json
import csv


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


# === block: score_0 (check id='zincblende') ===
def score_0(artifact, step, ctx):
    ref = step.get('reference', {})
    tol = step.get('tolerance', {})
    keys = ['lattice_constant_angstrom', 'bulk_modulus_Mbar', 'bulk_modulus_derivative',
            'cohesive_energy_eV_per_atom', 'elastic_C11_minus_C12_over_2_Mbar', 'elastic_C44_Mbar']
    cnt = 0
    for k in keys:
        if k in artifact and abs(artifact[k] - ref.get(k, 0)) <= tol.get(k, 0):
            cnt += 1
    return cnt / float(len(keys))


# === block: score_1 (check id='rocksalt') ===
def score_1(artifact, step, ctx):
    data = artifact.get('diffusion_coefficients', [])
    if not data:
        return 0.0
    # gold point
    gold_cfg = step.get('gold_point', {})
    gold_D = None
    for d in data:
        if abs(d.get('pressure_kbar', 0) - gold_cfg.get('pressure', -1)) < 0.01 and \
           abs(d.get('temperature_K', 0) - gold_cfg.get('temperature', -1)) < 0.1:
            gold_D = d.get('diffusion_coefficient_cm2_per_s', 0)
            break
    gold_score = 0.0
    if gold_D is not None and gold_cfg:
        ref_D = gold_cfg.get('D', 1e-5)
        factor = gold_cfg.get('factor', 2.0)
        if gold_D > 0 and gold_D <= ref_D * factor and gold_D >= ref_D / factor:
            gold_score = 1.0
    # monotonicity
    pressures = {}
    for d in data:
        p = d.get('pressure_kbar')
        if p is not None:
            pressures.setdefault(p, []).append(d)
    mono_ok = 0
    if pressures:
        for p, pts in pressures.items():
            pts_sorted = sorted(pts, key=lambda x: x.get('temperature_K', 0))
            ok = True
            for i in range(len(pts_sorted)-1):
                if pts_sorted[i].get('diffusion_coefficient_cm2_per_s', 0) > pts_sorted[i+1].get('diffusion_coefficient_cm2_per_s', 0):
                    ok = False
                    break
            if ok and len(pts_sorted) >= 2:
                mono_ok += 1
    mono_score = mono_ok / float(len(pressures)) if pressures else 0.0
    # magnitude
    mag_ok = 0
    for d in data:
        D = d.get('diffusion_coefficient_cm2_per_s', 0)
        if D > 0 and 0.1e-5 <= D <= 10e-5:
            mag_ok += 1
    mag_score = mag_ok / float(len(data)) if data else 0.0
    # combine
    w_g = step.get('weight_gold', 0.3)
    w_m = step.get('weight_mono', 0.5)
    w_a = step.get('weight_mag', 0.2)
    total = w_g * gold_score + w_m * mono_score + w_a * mag_score
    return max(0.0, min(1.0, total))


_SCORERS = {
    'zincblende': score_0,
    'rocksalt': score_1,
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
