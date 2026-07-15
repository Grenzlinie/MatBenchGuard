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
    ctx = {'step01': [s for s in spec['steps'] if s['id']=='step_01'][0]['params'], 'step02': [s for s in spec['steps'] if s['id']=='step_02'][0]['params']}
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    params = step['params']
    hot_kx = params['hot_spot_kx']
    hot_ky = params['hot_spot_ky']
    cold_kx = params['cold_spot_kx']
    gold_hot_peak = params['hot_peak_gold_frequency']
    rel_tol = params['tolerance_relative']
    cold_tol = params['cold_peak_proximity_tol']
    # filter hot spot rows
    hot_rows = [r for r in artifact if abs(float(r['kx']) - hot_kx) < 1e-4 and abs(float(r['ky']) - hot_ky) < 1e-4]
    if not hot_rows:
        return 0.0
    # max spectral_density for omega < 0
    best = max([r for r in hot_rows if float(r['omega']) < 0], key=lambda r: float(r['spectral_density']), default=None)
    if best is None:
        return 0.0
    hot_omega_peak = float(best['omega'])
    hot_score = 1.0 if abs(hot_omega_peak - gold_hot_peak) <= abs(gold_hot_peak) * rel_tol else 0.0
    # cold spot check
    cold_rows = [r for r in artifact if abs(float(r['kx']) - cold_kx) < 1e-4]
    if not cold_rows:
        return hot_score * 0.5
    cold_best = max(cold_rows, key=lambda r: float(r['spectral_density']))
    cold_omega_peak = float(cold_best['omega'])
    cold_score = 1.0 if abs(cold_omega_peak - 0.0) <= cold_tol else 0.0
    return 0.7 * hot_score + 0.3 * cold_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    params = step['params']
    T_cr = params['T_cr']
    min_points = params['temperature_min_points']
    if len(artifact) < min_points:
        return 0.0
    # parse and sort rows
    parsed = []
    for row in artifact:
        try:
            T = float(row['temperature_K'])
            ratio = float(row['ratio_chiQ2_over_gammaQ'])
            parsed.append((T, ratio))
        except:
            return 0.0
    if len(parsed) < 2:
        return 0.0
    parsed.sort(key=lambda x: x[0])
    # compute slope signs
    signs = []
    for i in range(1, len(parsed)):
        T1, r1 = parsed[i-1]
        T2, r2 = parsed[i]
        if T2 == T1:
            continue
        signs.append((r2 - r1) / (T2 - T1) > 0)
    if not signs:
        return 0.0
    compliant = 0
    total = 0
    for i in range(1, len(parsed)):
        T_mid = (parsed[i-1][0] + parsed[i][0]) / 2.0
        slope_pos = signs[i-1]
        if T_mid < T_cr and slope_pos:
            compliant += 1
        elif T_mid > T_cr and not slope_pos:
            compliant += 1
        total += 1
    return 1.0 if total == 0 else min(1.0, compliant / float(total))


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
