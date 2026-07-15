import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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
    # extract gold coefficients
    step01 = next(s for s in spec['steps'] if s['id'] == 'step_01')
    gold_a = step01['target']['a']
    gold_b = step01['target']['b']

    # compute reference log10(P/Pa) for equilibrium curves using paper eqs 27-29
    # P° = 100000 Pa, log10(P/Pa) = log10(P/P°) + 5
    import math

    def gypsum_hemihydrate_log10P_Pa(T):
        # eq 27: P_H2O/P° = exp(80.19 * [ -86.35 + 0.2316*T - 0.2970e-5*T^2 - 0.2110e-7*T^3 ] / T )
        t2 = T*T
        t3 = T*t2
        arg = -86.35 + 0.2316*T - 0.2970e-5*t2 - 0.2110e-7*t3
        return 80.19 * arg / T / math.log(10) + 5.0

    def gypsum_anhydrite_log10P_Pa(T):
        # eq 28
        t2 = T*T
        t3 = T*t2
        arg = -114.70 + 0.2898*T + 0.2154e-4*t2 - 0.5509e-7*t3
        return 60.14 * arg / T / math.log(10) + 5.0

    def hemihydrate_anhydrite_log10P_Pa(T):
        # eq 29
        t2 = T*T
        t3 = T*t2
        arg = -28.33 + 0.05823*T + 0.2451e-4*t2 - 0.3399e-7*t3
        return 240.60 * arg / T / math.log(10) + 5.0

    check_temps = [300, 350, 400, 450, 500, 550, 600]
    ref_pressures = {}
    for T in check_temps:
        ref_pressures[T] = {
            'P_gypsum_hemihydrate_Pa': gypsum_hemihydrate_log10P_Pa(T),
            'P_gypsum_anhydrite_Pa': gypsum_anhydrite_log10P_Pa(T),
            'P_hemihydrate_anhydrite_Pa': hemihydrate_anhydrite_log10P_Pa(T)
        }

    return {
        'gold_a': gold_a,
        'gold_b': gold_b,
        'ref_pressures': ref_pressures,
        'check_temps': check_temps
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    gold_a = ctx['gold_a']
    gold_b = ctx['gold_b']
    tol_a = step.get('tolerance', {}).get('a', 0.5)
    tol_b = step.get('tolerance', {}).get('b', 0.002)
    score = 0.0
    if abs(artifact.get('a', 0) - gold_a) <= tol_a:
        score += 0.5
    if abs(artifact.get('b', 0) - gold_b) <= tol_b:
        score += 0.5
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = ctx.get('prepare_result', {}).get('ref_pressures', {})
    tol = step.get('tolerance_log10', 0.1)
    total = 0
    matched = 0
    for r in rows:
        try:
            T = float(r['T_K'])
        except (ValueError, TypeError):
            continue
        if T not in ref:
            continue
        for col in ['P_gypsum_hemihydrate_Pa', 'P_gypsum_anhydrite_Pa', 'P_hemihydrate_anhydrite_Pa']:
            try:
                val = float(r.get(col, -1))
            except (ValueError, TypeError):
                val = 0.0
            if val <= 0:
                continue
            logP = math.log10(val)
            if abs(logP - ref[T][col]) <= tol:
                matched += 1
            total += 1
    if total == 0:
        return 0.0
    return matched / total


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    rows = artifact
    pts = []
    for r in rows:
        try:
            rh = float(r['relative_humidity_pct'])
            occ = float(r['occupancy'])
            pts.append((rh, occ))
        except (ValueError, TypeError):
            continue
    if len(pts) == 0:
        return 0.0
    pts.sort(key=lambda x: x[0])
    monotonic = all(pts[i][1] <= pts[i+1][1] + 1e-6 for i in range(len(pts)-1))
    score = 0.0
    if monotonic:
        score += 0.5
    checks = step.get('checks', {})
    points = checks.get('points', {})
    for key, pt in points.items():
        target_rh = pt['relative_humidity_pct']
        target_occ = pt['occupancy_target']
        tol = pt['tolerance']
        best = min(pts, key=lambda x: abs(x[0]-target_rh))
        if abs(best[0] - target_rh) <= 2.0 and abs(best[1] - target_occ) <= tol:
            score += 0.25
    return min(score, 1.0)


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    rows = artifact
    pts = []
    for r in rows:
        try:
            p = float(r['pressure_Pa'])
            occ = float(r['occupancy'])
            pts.append((p, occ))
        except (ValueError, TypeError):
            continue
    if len(pts) == 0:
        return 0.0
    pts.sort(key=lambda x: x[0])
    monotonic = all(pts[i][1] <= pts[i+1][1] + 1e-6 for i in range(len(pts)-1))
    score = 0.0
    if monotonic:
        score += 0.5
    checks = step.get('checks', {})
    points = checks.get('points', {})
    for key, pt in points.items():
        target_p = pt['pressure_Pa']
        target_occ = pt['occupancy_target']
        tol = pt['tolerance']
        best = min(pts, key=lambda x: abs(x[0]-target_p))
        if abs(best[0] - target_p) <= 0.01 and abs(best[1] - target_occ) <= tol:
            score += 0.5
    return min(score, 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_04': score_2,
    'step_05': score_3,
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
