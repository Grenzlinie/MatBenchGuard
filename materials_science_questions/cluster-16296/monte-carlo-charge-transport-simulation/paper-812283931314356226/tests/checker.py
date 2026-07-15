import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    import os
    csv_path = os.path.join(outputs_dir, 'step_01_density_profiles.csv')
    if not os.path.exists(csv_path):
        return {'data': None}
    rows = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if not rows:
        return {'data': None}
    pos = np.array([float(r['position_nm']) for r in rows])
    classical = np.array([float(r['classical_density']) for r in rows])
    effective = np.array([float(r['effective_density']) for r in rows])
    sp = np.array([float(r['schrodinger_poisson_density']) for r in rows])
    return {'pos': pos, 'classical': classical, 'effective': effective, 'sp': sp}


# === block: score_0 (check id='effective_sp_closeness') ===
def score_0(artifact, step, ctx):
    if ctx.get('data') is None:
        return 0.0
    eff = ctx['effective']
    pos_agent = ctx['pos']

    # Hidden gold: digitized electron density from the Schrödinger-Poisson
    # reference calculation (paper's Fig. 3).  The profile is modelled as a
    # Gaussian peak in the GaN channel near the interface, matching the
    # known structure (interface at 20 nm, peak at ~23 nm).
    ref_pos_nm = np.arange(0.0, 120.1, 0.1)
    bg_doping = 1e17
    peak_center = 23.0
    peak_width = 3.0
    peak_amplitude = 0.9e19
    ref_density = bg_doping + peak_amplitude * np.exp(-((ref_pos_nm - peak_center) / peak_width) ** 2)

    # Interpolate the agent's effective density onto the reference grid.
    # If the agent's grid covers the region, linear interpolation works;
    # extrapolated values are clipped to prevent large errors.
    eff_on_ref = np.interp(ref_pos_nm, pos_agent, eff)

    # Compute normalised root-mean-square deviation (NRMSD).
    # Normalise by the span of the reference profile to obtain a relative error.
    nrmsd = np.sqrt(np.mean((eff_on_ref - ref_density) ** 2)) / (np.max(ref_density) - np.min(ref_density) + 1e-12)

    # Tolerances from the approved plan: a correct reimplementation is expected
    # to stay well below 5% NRMSD; anything above 20% is almost certainly wrong.
    threshold_better = 0.05
    threshold_worse = 0.2
    if nrmsd <= threshold_better:
        return 1.0
    score = max(0.0, 1.0 - (nrmsd - threshold_better) / (threshold_worse - threshold_better))
    return score


# === block: score_1 (check id='classical_sp_difference') ===
def score_1(artifact, step, ctx):
    if ctx.get('data') is None:
        return 0.0
    cl = ctx['classical']
    sp = ctx['sp']
    nrmsd = np.sqrt(np.mean((cl - sp)**2)) / (np.max(sp) - np.min(sp) + 1e-12)
    threshold = 0.15
    score = min(1.0, nrmsd / threshold)
    return score


# === block: score_2 (check id='peak_structure') ===
def score_2(artifact, step, ctx):
    if ctx.get('data') is None:
        return 0.0
    pos = ctx['pos']
    sp = ctx['sp']
    cl = ctx['classical']
    idx_sp_max = np.argmax(sp)
    idx_cl_max = np.argmax(cl)
    sp_peak_x = pos[idx_sp_max]
    cl_peak_x = pos[idx_cl_max]
    cl_max = cl[idx_cl_max]
    sp_max = sp[idx_sp_max]
    sub_scores = []
    weights = []
    if sp_peak_x > 21.0:
        sub_scores.append(1.0)
    else:
        sub_scores.append(0.0)
    weights.append(0.5)
    if cl_peak_x <= 20.5:
        sub_scores.append(1.0)
    else:
        sub_scores.append(0.0)
    weights.append(0.3)
    if cl_max > 1.5 * sp_max:
        sub_scores.append(1.0)
    else:
        sub_scores.append(0.0)
    weights.append(0.2)
    total = sum(s * w for s, w in zip(sub_scores, weights))
    return total


_SCORERS = {
    'effective_sp_closeness': score_0,
    'classical_sp_difference': score_1,
    'peak_structure': score_2,
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
