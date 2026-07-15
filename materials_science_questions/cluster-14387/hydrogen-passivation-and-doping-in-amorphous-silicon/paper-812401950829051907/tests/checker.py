import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, numpy as np, yaml


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
    gold = {'min_angle': 101.5, 'ratio': 0.90}
    theta_arr = np.arange(90, 120.25, 0.5)
    theta_values = np.round(theta_arr, 1).tolist()
    required_configs = ['Si Si4','Si NSi3','Si HSi3','Si HN3','Si HNSi2','Si H2N2','Si H2NSi','Si H2Si2']
    return {'gold': gold, 'theta_values': theta_values, 'required_configs': required_configs}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        gold = ctx['gold']
        theta_vals = ctx['theta_values']
        req_cfgs = ctx['required_configs']
        # Parse CSV into dict of config -> list of (theta, V) rounded
        data = {}
        for row in artifact:
            cfg = row.get('configuration')
            try:
                theta = float(row['theta'])
                v = float(row['V_theta'])
            except (KeyError, ValueError):
                return 0.0
            data.setdefault(cfg, []).append((round(theta,1), v))
        # Check all required configurations exist and have exactly all expected theta points
        for cfg in req_cfgs:
            if cfg not in data:
                return 0.0
            thetas_in_cfg = set(t for t,_ in data[cfg])
            if not all(abs(tv - t) < 0.01 for t in thetas_in_cfg for tv in theta_vals) or len(thetas_in_cfg) != len(theta_vals):
                # Better: require full set
                if not all(any(abs(t - tv) < 0.01 for t in thetas_in_cfg) for tv in theta_vals):
                    return 0.0
        # Extract Si HNSi2
        cfg_points = data.get('Si HNSi2')
        if not cfg_points:
            return 0.0
        cfg_points.sort(key=lambda x: x[0])
        thetas = np.array([p[0] for p in cfg_points])
        vs = np.array([p[1] for p in cfg_points])
        idx_min = np.argmin(vs)
        theta_min_approx = thetas[idx_min]
        # Fit quadratic in window of +/-5 deg around min
        mask = (thetas >= theta_min_approx - 5) & (thetas <= theta_min_approx + 5)
        if mask.sum() < 3:
            return 0.0
        sub_t = thetas[mask]
        sub_v = vs[mask]
        coeffs = np.polyfit(sub_t, sub_v, 2)
        a = coeffs[0]
        if abs(a) < 1e-12:
            return 0.0
        min_angle = -coeffs[1]/(2*a)
        target = gold['min_angle']
        err = abs(min_angle - target)
        # Read tolerance from the step config declared in grading_spec
        tolerance = step.get('config', {}).get('tolerance_deg', 0.5)
        max_err = tolerance * 4.0   # linear falloff range (was hardcoded 2.0)
        if err <= tolerance:
            return 1.0
        elif err <= max_err:
            return max(0.0, 1.0 - (err - tolerance) / (max_err - tolerance))
        else:
            return 0.0


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        # artifact is a string for 'other' format; parse YAML
        try:
            import yaml
            if isinstance(artifact, str):
                data = yaml.safe_load(artifact)
            else:
                data = artifact
            if not isinstance(data, dict):
                return 0.0
            ratio = data.get('si_h2nsi_perp_ratio')
            if ratio is None:
                return 0.0
            ratio_val = float(ratio)
        except Exception:
            return 0.0
        target = ctx['gold']['ratio']
        tol = 0.02
        return 1.0 if abs(ratio_val - target) <= tol else 0.0


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
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
