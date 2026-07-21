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
    tric_ref = {}
    w_star_ref = None
    abs_tol_w = 0.02
    for s in spec['steps']:
        if s['id'] == 'tricritical':
            tric_ref = s['target']['reference']
        elif s['id'] == 'w_star':
            w_star_ref = s['target']['reference']
            abs_tol_w = s['target']['abs_tol']
    return {'tric_ref': tric_ref, 'w_star_ref': w_star_ref, 'w_star_abs_tol': abs_tol_w}


# === block: score_0 (check id='tricritical') ===
def score_0(artifact, step, ctx):
    import math

    def check_monotonic_decreasing(vals):
        if len(vals) < 2:
            return True
        for i in range(1, len(vals)):
            if vals[i] >= vals[i-1]:
                return False
        return True

    ref = ctx['tric_ref']
    rows = artifact
    data = {}
    for row in rows:
        lat = row['lattice'].strip()
        ry_str = str(row['r_y']).strip()
        try:
            H0 = float(row['H0_over_J'])
            Tc = float(row['kBTc_over_J'])
        except:
            H0, Tc = float('nan'), float('nan')
        data[(lat, ry_str)] = (H0, Tc)

    expected_keys = [('SC','1.0'), ('SC','1.5'), ('SC','2.0'), ('BCC','1.0'), ('BCC','1.5'), ('BCC','2.0')]
    rel_tol = step['target']['rel_tol']
    coord_score = 0.0
    total_coord = 0
    for (lat, ry) in expected_keys:
        if (lat, ry) in ref:
            r_H0 = ref[lat][ry]['H0_over_J']
            r_Tc = ref[lat][ry]['kBTc_over_J']
            if (lat, ry) in data:
                H0, Tc = data[(lat, ry)]
                if not (math.isnan(H0) or math.isnan(Tc)):
                    if r_H0 != 0:
                        if abs(H0 - r_H0) / r_H0 <= rel_tol:
                            coord_score += 1
                    else:
                        if abs(H0 - r_H0) <= rel_tol:
                            coord_score += 1
                    if r_Tc != 0:
                        if abs(Tc - r_Tc) / r_Tc <= rel_tol:
                            coord_score += 1
                    else:
                        if abs(Tc - r_Tc) <= rel_tol:
                            coord_score += 1
                total_coord += 2

    if total_coord == 0:
        coord_ratio = 0.0
    else:
        coord_ratio = coord_score / total_coord

    mono_pass = 0
    mono_checks = 0
    for lat in ['SC','BCC']:
        ry_order = ['1.0','1.5','2.0']
        H0_vals = []
        Tc_vals = []
        for ry in ry_order:
            if (lat, ry) in data:
                H0, Tc = data[(lat, ry)]
                if not math.isnan(H0): H0_vals.append(H0)
                else: H0_vals.append(float('inf'))
                if not math.isnan(Tc): Tc_vals.append(Tc)
                else: Tc_vals.append(float('inf'))
            else:
                H0_vals.append(float('inf'))
                Tc_vals.append(float('inf'))
        if check_monotonic_decreasing(H0_vals):
            mono_pass += 1
        mono_checks += 1
        if check_monotonic_decreasing(Tc_vals):
            mono_pass += 1
        mono_checks += 1

    order_pass = 0
    order_checks = 0
    for ry in ['1.0','1.5','2.0']:
        if ('SC', ry) in data and ('BCC', ry) in data:
            H0_sc, Tc_sc = data[('SC', ry)]
            H0_bcc, Tc_bcc = data[('BCC', ry)]
            if not (math.isnan(H0_sc) or math.isnan(H0_bcc)):
                if H0_bcc > H0_sc:
                    order_pass += 1
                order_checks += 1
            else:
                order_checks += 1
            if not (math.isnan(Tc_sc) or math.isnan(Tc_bcc)):
                if Tc_bcc > Tc_sc:
                    order_pass += 1
                order_checks += 1
            else:
                order_checks += 1
        else:
            order_checks += 2

    mono_ratio = mono_pass / max(mono_checks, 1)
    order_ratio = order_pass / max(order_checks, 1)
    score = 0.6 * coord_ratio + 0.2 * mono_ratio + 0.2 * order_ratio
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='w_star') ===
def score_1(artifact, step, ctx):
    ref = ctx['w_star_ref']
    abs_tol = ctx['w_star_abs_tol']
    row = artifact[0]
    w = float(row['w_star'])
    if abs(w - ref) <= abs_tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'tricritical': score_0,
    'w_star': score_1,
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
