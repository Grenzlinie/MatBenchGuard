import os
import json
import csv

# === author imports / helpers ===
import os
from collections import defaultdict


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
    return {}


# === block: score_0 (check id='check_beta_in_vacuo') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is list of dicts from beta_in_vacuo.csv
        if not artifact:
            return 0.0
        # Check all beta values negative
        all_neg = all(float(row['beta_J_m2']) < 0 for row in artifact)
        # Group by density
        density_vals = defaultdict(list)
        for row in artifact:
            dens = float(row['density_nm2'])
            density_vals[dens].append((row['surface'], float(row['beta_J_m2'])))
        # Check ordering per density
        top1_ok = 0
        top2_ok = 0
        last_ok = 0
        n_dens = 0
        for dens, rows in density_vals.items():
            n_dens += 1
            rows_sorted = sorted(rows, key=lambda x: x[1])  # ascending (most negative first)
            if rows_sorted[0][0] == 'A(100)':
                top1_ok += 1
            if len(rows_sorted) >= 2 and rows_sorted[1][0] == 'R(110)':
                top2_ok += 1
            if rows_sorted[-1][0] == 'A(001)':
                last_ok += 1
        # Compute sub-scores
        s_neg = 0.25 if all_neg else 0.0
        if n_dens == 0:
            s_top1 = 0.0
            s_top2 = 0.0
            s_last = 0.0
        else:
            s_top1 = 0.25 * (top1_ok / n_dens)
            s_top2 = 0.25 * (top2_ok / n_dens)
            s_last = 0.25 * (last_ok / n_dens)
        return min(1.0, s_neg + s_top1 + s_top2 + s_last)


# === block: score_1 (check id='check_beta_water_modified') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is list of dicts from beta_water_modified.csv
        if not artifact:
            return 0.0
        # Load beta in vacuo for spread comparison
        beta_in_vacuo_path = '/app/outputs/beta_in_vacuo.csv'
        beta_in_vacuo = None
        if os.path.exists(beta_in_vacuo_path):
            import csv
            with open(beta_in_vacuo_path, newline='') as f:
                beta_in_vacuo = list(csv.DictReader(f))
        # Check all beta_prime negative
        all_neg = all(float(row['beta_prime_J_m2']) < 0 for row in artifact)
        # Group by density
        from collections import defaultdict
        density_vals_prime = defaultdict(list)
        for row in artifact:
            dens = float(row['density_nm2'])
            density_vals_prime[dens].append((row['surface'], float(row['beta_prime_J_m2'])))
        # Ordering check
        top1_ok = 0
        top2_ok = 0
        last_ok = 0
        n_dens = 0
        for dens, rows in density_vals_prime.items():
            n_dens += 1
            rows_sorted = sorted(rows, key=lambda x: x[1])
            if rows_sorted[0][0] == 'A(100)':
                top1_ok += 1
            if len(rows_sorted) >= 2 and rows_sorted[1][0] == 'R(110)':
                top2_ok += 1
            if rows_sorted[-1][0] == 'A(001)':
                last_ok += 1
        # Spread reduction check
        spread_ok = 0
        if beta_in_vacuo:
            # Build density-based min/max for beta
            beta_density_vals = defaultdict(list)
            for row in beta_in_vacuo:
                dens = float(row['density_nm2'])
                beta_density_vals[dens].append(float(row['beta_J_m2']))
            for dens, vals_pr in density_vals_prime.items():
                if dens in beta_density_vals:
                    vals_beta = beta_density_vals[dens]
                    range_pr = max(vals_pr) - min(vals_pr)
                    range_beta = max(vals_beta) - min(vals_beta)
                    if range_pr < range_beta:
                        spread_ok += 1
            n_dens_spread = sum(1 for d in density_vals_prime if d in beta_density_vals)
        else:
            n_dens_spread = 0
        # Sub-scores: 5 checks each 0.2
        s_neg = 0.2 if all_neg else 0.0
        if n_dens == 0:
            s_top1 = 0.0
            s_top2 = 0.0
            s_last = 0.0
        else:
            s_top1 = 0.2 * (top1_ok / n_dens)
            s_top2 = 0.2 * (top2_ok / n_dens)
            s_last = 0.2 * (last_ok / n_dens)
        if n_dens_spread == 0:
            s_spread = 0.0
        else:
            s_spread = 0.2 * (spread_ok / n_dens_spread)
        return min(1.0, s_neg + s_top1 + s_top2 + s_last + s_spread)


_SCORERS = {
    'check_beta_in_vacuo': score_0,
    'check_beta_water_modified': score_1,
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
