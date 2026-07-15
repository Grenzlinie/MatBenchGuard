import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os
from statistics import mean, stdev

def _read_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def _check_columns(row_dicts, required):
    if not row_dicts:
        return False
    return all(col in row_dicts[0] for col in required)

def _pearson(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx = mean(x)
    my = mean(y)
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sx = math.sqrt(sum((a - mx)**2 for a in x))
    sy = math.sqrt(sum((b - my)**2 for b in y))
    if sx == 0.0 or sy == 0.0:
        return 0.0
    return cov / (sx * sy)

def _linear_fit(x, y):
    n = len(x)
    if n < 2:
        return 0.0, 0.0, 0.0
    mx = mean(x)
    my = mean(y)
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y))
    varx = sum((a - mx)**2 for a in x)
    if varx == 0.0:
        return 0.0, my, 0.0
    slope = cov / varx
    intercept = my - slope * mx
    ss_res = sum((b - (slope * a + intercept))**2 for a, b in zip(x, y))
    ss_tot = sum((b - my)**2 for b in y)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot != 0.0 else 0.0
    return slope, intercept, r2


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
    output_dir = "/app/outputs"
    return {"output_dir": output_dir}


# === block: score_0 (check id='defect_analysis_structural') ===
def score_0(artifact, step, ctx):
    rows = _read_csv(os.path.join(ctx["output_dir"], step["output_file"]))
    if not rows or not _check_columns(rows, step.get("required_columns", [])):
        return 0.0
    sample_ids = set()
    for r in rows:
        sid = r.get("sample_id")
        if sid is not None:
            sample_ids.add(sid)
    if len(rows) < step.get("min_rows", 0) or len(sample_ids) < step.get("min_distinct_sample_ids", 0):
        return 0.0
    return 1.0


# === block: score_1 (check id='stress_drop_structural') ===
def score_1(artifact, step, ctx):
    rows = _read_csv(os.path.join(ctx["output_dir"], step["output_file"]))
    if not rows or not _check_columns(rows, step.get("required_columns", [])):
        return 0.0
    sample_ids = set()
    for r in rows:
        sid = r.get("sample_id")
        if sid is not None:
            sample_ids.add(sid)
    if len(rows) < step.get("min_rows", 0) or len(sample_ids) < step.get("min_distinct_sample_ids", 0):
        return 0.0
    return 1.0


# === block: score_2 (check id='summary_metrics') ===
def score_2(artifact, step, ctx):
    out_dir = ctx["output_dir"]
    defect_path = os.path.join(out_dir, "defect_analysis.csv")
    stress_path = os.path.join(out_dir, "stress_drop_predictions.csv")
    if not os.path.isfile(defect_path) or not os.path.isfile(stress_path):
        return 0.0

    # --- recompute from raw CSVs ---
    defect_rows = _read_csv(defect_path)
    stress_rows = _read_csv(stress_path)
    if not defect_rows or not stress_rows:
        return 0.0

    # extract arrays for defect analysis
    phi_fit = []
    phi_loc = []
    eps_star = []
    u_na = []
    for r in defect_rows:
        try:
            pf = float(r["phi_fit"])
            pl = float(r["phi_esh_loc"])
            ep = float(r["epsilon_star_fit"])
            un = float(r["u_na_avg"])
            phi_fit.append(pf)
            phi_loc.append(pl)
            eps_star.append(ep)
            u_na.append(un)
        except (ValueError, KeyError):
            continue

    if len(phi_fit) < 2 or len(phi_loc) < 2 or len(eps_star) < 2 or len(u_na) < 2:
        return 0.0

    rho_phi = _pearson(phi_fit, phi_loc)
    slope, intercept, r2 = _linear_fit(u_na, eps_star)

    # extract stress drop arrays
    dm = []
    dg = []
    dl = []
    for r in stress_rows:
        try:
            d0 = float(r["Delta_sigma_MD"])
            gf = float(r["Delta_sigma_global_fit"])
            ld = float(r["Delta_sigma_local_descriptor"])
            dm.append(d0)
            dg.append(gf)
            dl.append(ld)
        except (ValueError, KeyError):
            continue
    if len(dm) < 2 or len(dg) < 2 or len(dl) < 2:
        return 0.0

    rho_global = _pearson(dm, dg)
    rho_local = _pearson(dm, dl)

    # --- score each metric directionally ---
    thresh = step.get("thresholds", {})

    def _dir_score(value, lower_bound):
        if value >= lower_bound:
            return 1.0
        # linear scaling from 0 at 0 to 1 at lower_bound (never negative)
        denom = lower_bound
        if denom <= 0:
            return 0.0
        return max(0.0, min(1.0, value / denom))

    score_phi   = _dir_score(rho_phi, thresh.get("rho_phi_lower", 0.15))
    score_r2    = _dir_score(r2, thresh.get("R2_lower", 0.5))
    score_glbl  = _dir_score(rho_global, thresh.get("rho_stress_global_lower", 0.85))
    score_local = _dir_score(rho_local, thresh.get("rho_stress_local_lower", 0.80))

    # slope structural check: must be positive
    score_slope = 1.0 if slope > 0.0 and math.isfinite(slope) else 0.0

    # combine sub-scores with fixed internal weights
    w_phi   = 0.20
    w_slope = 0.10
    w_r2    = 0.20
    w_glbl  = 0.25
    w_local = 0.25
    step_score = w_phi*score_phi + w_slope*score_slope + w_r2*score_r2 + w_glbl*score_glbl + w_local*score_local
    return step_score


_SCORERS = {
    'defect_analysis_structural': score_0,
    'stress_drop_structural': score_1,
    'summary_metrics': score_2,
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
