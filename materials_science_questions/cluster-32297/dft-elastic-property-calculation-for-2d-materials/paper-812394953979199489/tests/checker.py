import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, statistics


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
    def prepare(outputs_dir, spec):
        return {}


# === block: score_0 (check id='bandstructure') ===
def score_0(artifact, step, ctx):
        target = step['target']
        pbe = artifact.get('pbe_bandgap')
        hse = artifact.get('hse_bandgap')
        quasi = artifact.get('quasi_direct_gap')
        type_ = artifact.get('bandgap_type')
        cbm = artifact.get('cbm_location')
        vbm = artifact.get('vbm_location')
        if pbe is None or hse is None or quasi is None or type_ is None or cbm is None or vbm is None:
            return 0.0
        pbe_ok = abs(pbe - target['pbe_bandgap']) <= target['pbe_tol_abs']
        hse_ok = abs(hse - target['hse_bandgap']) <= target['hse_tol_abs']
        quasi_ok = abs(quasi - target['quasi_direct_gap']) <= target['quasi_tol_abs']
        type_ok = (type_ == target['bandgap_type'])
        cbm_ok = (str(cbm).strip().lower() == target['cbm_location'].lower())
        vbm_ok = (str(vbm).strip().lower() == target['vbm_location'].lower())
        sub = [pbe_ok, hse_ok, quasi_ok, type_ok, cbm_ok, vbm_ok]
        return sum(sub) / len(sub)


# === block: score_1 (check id='strain') ===
def score_1(artifact, step, ctx):
    def score_strain(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        try:
            rows = sorted(artifact, key=lambda r: float(r['strain_x']))
        except Exception:
            return 0.0
        strains = [float(r['strain_x']) for r in rows]
        bandgaps = [float(r['hse_bandgap']) for r in rows]
        monotonic = all(bandgaps[i] <= bandgaps[i+1] + 1e-6 for i in range(len(bandgaps)-1))
        zero_gap = None
        for r in artifact:
            if abs(float(r['strain_x'])) < 0.001:
                zero_gap = float(r['hse_bandgap'])
                break
        zero_match = abs(zero_gap - step['zero_strain_gap_target']) <= step['zero_strain_gap_tol'] if zero_gap is not None else False
        score = 0.5 * monotonic + 0.5 * zero_match
        return score


# === block: score_2 (check id='layer') ===
def score_2(artifact, step, ctx):
    def score_layer(artifact, step, ctx):
        if not artifact:
            return 0.0
        try:
            rows = sorted(artifact, key=lambda r: int(r['n_layers']))
        except:
            return 0.0
        N = []
        gaps = []
        for r in rows:
            n = int(r['n_layers'])
            bg = float(r['hse_bandgap'])
            N.append(n)
            gaps.append(bg)
        if len(N) < 3:
            return 0.0
        B = step['bulk_gap_estimate']
        if any(g <= B for g in gaps):
            return 0.0
        log_N = [math.log(n) for n in N]
        log_E_B = [math.log(g - B) for g in gaps]
        n_pts = len(N)
        mean_x = sum(log_N) / n_pts
        mean_y = sum(log_E_B) / n_pts
        cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(log_N, log_E_B))
        var_x = sum((x - mean_x) ** 2 for x in log_N)
        if var_x == 0:
            return 0.0
        slope = cov / var_x
        alpha = -slope
        alpha_target = step['exponent_target']
        alpha_tol = step['exponent_tol']
        alpha_score = max(0.0, 1.0 - abs(alpha - alpha_target) / alpha_tol)
        mono_gap = None
        for g, n in zip(gaps, N):
            if n == 1:
                mono_gap = g
                break
        mono_target = step['monolayer_gap_target']
        mono_tol = step['monolayer_gap_tol']
        if mono_gap is None:
            mono_score = 0.0
        else:
            dev = abs(mono_gap - mono_target)
            if dev <= mono_tol:
                mono_score = 1.0
            else:
                mono_score = max(0.0, 1.0 - (dev - mono_tol) / 0.2)
        return 0.7 * alpha_score + 0.3 * mono_score


# === block: score_3 (check id='piezo') ===
def score_3(artifact, step, ctx):
    def score_piezo(artifact, step, ctx):
        if not artifact:
            return 0.0
        rows = artifact
        e11_3d_vals = []
        e12_3d_vals = []
        e11_2d_vals = []
        layers = []
        for r in rows:
            n = int(r['n_layers'])
            e11_2d = float(r['e11_2D'])
            e12_2d = float(r['e12_2D'])
            e11_3d = float(r['e11_3D'])
            e12_3d = float(r['e12_3D'])
            if n in [1, 2, 3]:
                layers.append(n)
                e11_3d_vals.append(e11_3d)
                e12_3d_vals.append(e12_3d)
                e11_2d_vals.append(e11_2d)
        if len(layers) < 3:
            return 0.0
        avg_e11_3d = sum(e11_3d_vals) / 3
        e11_3d_target = step['e11_3D_target']
        e11_3d_tol = step['e11_3D_tol']
        e11_dev_score = max(0.0, 1.0 - abs(avg_e11_3d - e11_3d_target) / e11_3d_tol)
        e11_std = statistics.stdev(e11_3d_vals)
        std_score = max(0.0, 1.0 - e11_std / step['constancy_std_max'])
        avg_e12_3d = sum(e12_3d_vals) / 3
        e12_3d_target = step['e12_3D_target']
        e12_3d_tol = step['e12_3D_tol']
        e12_dev_score = max(0.0, 1.0 - abs(avg_e12_3d - e12_3d_target) / e12_3d_tol)
        ratios = [e11_2d_vals[i] / layers[i] for i in range(len(layers))]
        if len(ratios) > 1:
            ratio_std = statistics.stdev(ratios)
            mean_ratio = sum(ratios) / len(ratios)
            ratio_score = max(0.0, 1.0 - (ratio_std / mean_ratio if mean_ratio > 0 else 1.0) / 0.1)
        else:
            ratio_score = 1.0
        score = 0.4 * e11_dev_score + 0.2 * std_score + 0.2 * e12_dev_score + 0.2 * ratio_score
        return min(max(score, 0.0), 1.0)


_SCORERS = {
    'bandstructure': score_0,
    'strain': score_1,
    'layer': score_2,
    'piezo': score_3,
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
