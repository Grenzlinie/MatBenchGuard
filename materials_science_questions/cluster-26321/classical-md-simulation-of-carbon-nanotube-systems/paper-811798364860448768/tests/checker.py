import os
import json
import csv

# === author imports / helpers ===
import math
import itertools

class _NpNamespace:
    pi = math.pi

    @staticmethod
    def mean(iterable):
        lst = list(iterable)
        return sum(lst) / len(lst) if lst else 0.0

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError("Only deg=1 supported")
        n = len(x)
        sx = sum(x)
        sy = sum(y)
        sxx = sum(xi*xi for xi in x)
        sxy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n * sxx - sx * sx
        if denom == 0:
            return (0.0, 0.0)  # fallback
        slope = (n * sxy - sx * sy) / denom
        intercept = (sy * sxx - sx * sxy) / denom
        return (slope, intercept)

    @staticmethod
    def argmax(iterable):
        lst = list(iterable)
        if not lst:
            raise ValueError("empty sequence")
        max_val = lst[0]
        max_idx = 0
        for i, v in enumerate(lst):
            if v > max_val:
                max_val = v
                max_idx = i
        return max_idx

np = _NpNamespace()


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
    # Load all required artifacts
    import os, json, csv
    def prepare(outputs_dir, spec):
        ctx = {}
        for fname, key in [('deceleration_phase.csv', 'deceleration_data'),
                           ('steady_velocity.csv', 'steady_data'),
                           ('radial_density.csv', 'radial_data')]:
            path = os.path.join(outputs_dir, fname)
            if os.path.exists(path):
                with open(path, newline='') as f:
                    ctx[key] = list(csv.DictReader(f))
        meta_path = os.path.join(outputs_dir, 'system_metadata.json')
        if os.path.exists(meta_path):
            with open(meta_path) as f:
                ctx['metadata'] = json.load(f)
        return ctx


# === block: score_0 (check id='step_tau_eta') ===
def score_0(artifact, step, ctx):
    # Recompute tau and eta, compare to gold
    if ctx is None:
        return 0.0
    decel_data = ctx.get('deceleration_data')
    steady_data = ctx.get('steady_data')
    meta = ctx.get('metadata')
    if decel_data is None or steady_data is None or meta is None:
        return 0.0
    v_steady = [float(r['mean_axial_velocity']) for r in steady_data]
    if not v_steady:
        return 0.0
    v_bar = np.mean(v_steady)
    times = [float(r['time']) for r in decel_data]
    vels = [float(r['mean_axial_velocity']) for r in decel_data]
    if len(times) < 3:
        return 0.0
    slope, _ = np.polyfit(times, vels, 1)
    decel = -slope   # m/s per ps
    a_si = decel * 1e12   # m/s^2
    total_mass = float(meta['total_mass_kg'])
    D = float(meta['diameter_m'])
    L = float(meta['length_m'])
    tau = total_mass * a_si / (np.pi * D * L)   # Pa
    tau_MPa = tau * 1e-6
    target = float(step['target'])
    tol_tau = float(step.get('tolerance_relative', 0.2))
    rel_err = abs(tau_MPa - target) / target
    if rel_err <= tol_tau:
        score_tau = 1.0
    elif rel_err <= 2*tol_tau:
        score_tau = 0.5
    else:
        score_tau = 0.0
    R = D / 2.0
    eta_target_si = target * 1e6 * R / (4 * 216)   # paper's v_ref = 216 m/s
    eta_actual_si = tau * R / (4 * v_bar) if v_bar != 0 else 0
    rel_err_eta = abs(eta_actual_si - eta_target_si) / eta_target_si
    tol_eta = 0.3
    if rel_err_eta <= tol_eta:
        score_eta = 1.0
    elif rel_err_eta <= 2*tol_eta:
        score_eta = 0.5
    else:
        score_eta = 0.0
    return (score_tau + score_eta) / 2.0


# === block: score_1 (check id='step_radial') ===
def score_1(artifact, step, ctx):
    # Check first solvation shell peak
    radial_data = ctx.get('radial_data')
    if not radial_data:
        return 0.0
    rs = [float(r['r_angstrom']) for r in radial_data]
    ds = [float(r['density_kg_per_m3']) for r in radial_data]
    idx_max = np.argmax(ds)
    r_peak = rs[idx_max]
    peak_dens = ds[idx_max]
    if 8.0 <= r_peak <= 8.8 and peak_dens > 1500.0:
        return 1.0
    return 0.0


_SCORERS = {
    'step_tau_eta': score_0,
    'step_radial': score_1,
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
