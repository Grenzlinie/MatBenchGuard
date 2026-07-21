import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

def linear_slope(points):
    """Compute ordinary least squares slope from (x,y) points."""
    if len(points) < 2:
        return None
    n = len(points)
    sx = sy = sxy = sxx = 0.0
    for x, y in points:
        sx += x
        sy += y
        sxy += x * y
        sxx += x * x
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-12:
        return None
    return (n * sxy - sx * sy) / denom


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
        try:
            step = next(s for s in spec['steps'] if s['id'] == 'step_01_results')
        except StopIteration:
            raise ValueError('Missing required grading step')
        return {
            'references': step['reference_points'],
            'tolerances': step['tolerances'],
            'trend': step['trend']
        }


# === block: score_0 (check id='step_01_results') ===
def score_0(artifact, step, ctx):
    def safe_float(v, default=None):
        try:
            return float(v)
        except (ValueError, TypeError):
            return default

    parsed = []
    if isinstance(artifact, list):
        for r in artifact:
            try:
                T_val = r.get('T')
                c_val = r.get('c')
                E_val = r.get('E_N')
                DE_val = r.get('ΔE_N')
                shift_val = r.get('shift')
                broad_val = r.get('broadening')
                if any(v is None for v in (T_val, c_val, E_val, DE_val, shift_val, broad_val)):
                    continue
                T = safe_float(T_val)
                c = safe_float(c_val)
                E_N = safe_float(E_val)
                DE_N = safe_float(DE_val)
                shift = safe_float(shift_val)
                broad = safe_float(broad_val)
                if None in (T, c, E_N, DE_N, shift, broad):
                    continue
                parsed.append({'T': T, 'c': c, 'E_N': E_N, 'ΔE_N': DE_N, 'shift': shift, 'broadening': broad})
            except Exception:
                continue

    if not parsed:
        return 0.0

    refs = ctx['references']
    tol = ctx['tolerances']
    trend_cfg = ctx['trend']

    # Match references to agent rows
    def find_closest(target_T, target_c):
        best = None
        best_dist = float('inf')
        for row in parsed:
            if row['T'] == target_T:
                dist = abs(row['c'] - target_c)
                if dist < 0.05 and dist < best_dist:
                    best = row
                    best_dist = dist
        return best

    scores_E = []
    scores_shift = []
    scores_DE = []
    scores_broad = []

    for ref in refs:
        row = find_closest(ref['T'], ref['c'])
        if row is None:
            scores_E.append(0.0)
            scores_shift.append(0.0)
            scores_DE.append(0.0)
            scores_broad.append(0.0)
            continue
        # E_N relative tolerance
        ref_en = ref['E_N']
        if abs(ref_en) < 1e-12:
            rel_err = abs(row['E_N'] - ref_en)
            score_e = 1.0 if rel_err < 1e-12 else 0.0
        else:
            rel_err = abs(row['E_N'] - ref_en) / abs(ref_en)
            score_e = max(0.0, 1.0 - rel_err / tol['E_N_rel_tol'])
        scores_E.append(score_e)

        # Shift absolute tolerance
        abs_err_s = abs(row['shift'] - ref['shift'])
        score_shift = max(0.0, 1.0 - abs_err_s / tol['shift_abs_tol'])
        scores_shift.append(score_shift)

        # ΔE_N relative tolerance
        ref_den = ref['ΔE_N']
        if abs(ref_den) < 1e-12:
            rel_err = abs(row['ΔE_N'] - ref_den)
            score_de = 1.0 if rel_err < 1e-12 else 0.0
        else:
            rel_err = abs(row['ΔE_N'] - ref_den) / abs(ref_den)
            score_de = max(0.0, 1.0 - rel_err / tol['ΔE_N_rel_tol'])
        scores_DE.append(score_de)

        # Broadening self-consistency: broadening = |ΔE_N(K)| / 11604.5
        expected_broadening = abs(row['ΔE_N']) / 11604.5
        abs_err_b = abs(row['broadening'] - expected_broadening)
        score_broad = max(0.0, 1.0 - abs_err_b / 0.005)
        scores_broad.append(score_broad)

    avg_E = sum(scores_E) / len(scores_E) if scores_E else 0.0
    avg_shift = sum(scores_shift) / len(scores_shift) if scores_shift else 0.0
    avg_DE = sum(scores_DE) / len(scores_DE) if scores_DE else 0.0
    avg_broad = sum(scores_broad) / len(scores_broad) if scores_broad else 0.0

    composite_ES = (avg_E + avg_shift) / 2.0
    composite_DB = (avg_DE + avg_broad) / 2.0

    # Trend linearity on shift vs c
    points = [(r['c'], r['shift']) for r in parsed]
    slope = linear_slope(points)
    trend_score = 0.0
    if slope is not None:
        trend_score = max(0.0, 1.0 - abs(slope - trend_cfg['target_slope']) / trend_cfg['slope_tol'])

    final = 0.4 * composite_ES + 0.4 * composite_DB + 0.2 * trend_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'step_01_results': score_0,
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
