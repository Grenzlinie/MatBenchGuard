import os
import json
import csv

# === author imports / helpers ===
import os, csv, math


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
    def read_csv(fname):
        path = os.path.join(outputs_dir, fname)
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    return {
        'isotherms': read_csv('isotherms_gcmc.csv'),
        'coexistence': read_csv('coexistence.csv'),
        'gcmc_compare': read_csv('gcmc_comparison.csv')
    }


# === block: score_0 (check id='monotonicity') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if rows is None:
        return 0.0
    try:
        temp180 = [r for r in rows if float(r['temperature']) == 180.0]
    except Exception:
        return 0.0
    if not temp180:
        return 0.0
    sorted_rows = sorted(temp180, key=lambda r: float(r['beta_mu_c']))
    prev = None
    for r in sorted_rows:
        d = float(r['density'])
        if prev is not None and d < prev - 1e-6:
            return 0.0
        prev = d
    return 1.0


# === block: score_1 (check id='coexistence_consistency') ===
def score_1(artifact, step, ctx):
    coex = artifact
    iso = ctx.get('isotherms')
    if iso is None or coex is None:
        return 0.0
    mu_tol = float(step.get('mu_tol', 0.01))
    density_tol = float(step.get('density_tol', 0.02))
    temps = []
    for row in coex:
        try:
            t = float(row['temperature'])
            mu = float(row['saturation_mu_c'])
            vd = float(row['vapor_density'])
            ld = float(row['liquid_density'])
            temps.append((t, mu, vd, ld))
        except Exception:
            continue
    if not temps:
        return 0.0
    def find_closest(points, target_mu, target_density):
        for p in points:
            try:
                mu_p = float(p['beta_mu_c'])
                d_p = float(p['density'])
                if abs(mu_p - target_mu) <= mu_tol and abs(d_p - target_density) <= density_tol:
                    return True
            except Exception:
                continue
        return False
    pass_count = 0
    for t, mu, vd, ld in temps:
        iso_t = [r for r in iso if abs(float(r['temperature']) - t) < 0.5]
        if find_closest(iso_t, mu, vd) and find_closest(iso_t, mu, ld):
            pass_count += 1
    return pass_count / len(temps)


# === block: score_2 (check id='critical_params') ===
def score_2(artifact, step, ctx):
    coex = artifact
    if coex is None:
        return 0.0
    Tc_val = None
    Gammac_val = None
    for row in coex:
        if row.get('temperature', '').strip().lower() == 'critical_temperature':
            try:
                Tc_val = float(row['saturation_mu_c'])
            except Exception:
                pass
        if row.get('temperature', '').strip().lower() == 'critical_density':
            try:
                Gammac_val = float(row['saturation_mu_c'])
            except Exception:
                pass
    Tc_target = float(step.get('Tc', 169.8))
    Tc_tol = float(step.get('Tc_tol', 5.0))
    Gammac_target = float(step.get('Gammac', 0.200))
    Gammac_tol = float(step.get('Gammac_tol', 0.01))
    if Tc_val is None or Gammac_val is None:
        return 0.0
    Tc_ok = abs(Tc_val - Tc_target) <= Tc_tol
    Gc_ok = abs(Gammac_val - Gammac_target) <= Gammac_tol
    if Tc_ok and Gc_ok:
        return 1.0
    elif Tc_ok or Gc_ok:
        return 0.5
    else:
        return 0.0


# === block: score_3 (check id='gcmc_compare') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if rows is None:
        return 0.0
    max_diff = float(step.get('max_diff', 0.02))
    total = len(rows)
    if total == 0:
        return 0.0
    passing = 0
    for r in rows:
        try:
            d_gcmc = float(r['density_gcmc'])
            d_gauge = float(r['density_gaugecell'])
            diff_reported = float(r['difference'])
            true_diff = d_gcmc - d_gauge
            if abs(true_diff - diff_reported) < 1e-4 and abs(true_diff) <= max_diff:
                passing += 1
        except Exception:
            continue
    return passing / total


_SCORERS = {
    'monotonicity': score_0,
    'coexistence_consistency': score_1,
    'critical_params': score_2,
    'gcmc_compare': score_3,
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
