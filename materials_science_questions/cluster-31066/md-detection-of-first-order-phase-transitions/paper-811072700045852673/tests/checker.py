import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
    return {
        "gold": {
            "B": {"mu_kT": 1.75, "p_over_rho0kT": 1.94, "density_gap": 0.75},
            "C": {"mu_kT": 5.0, "p_over_rho0kT": 5.0, "density_gap": 0.9}
        },
        "tolerances": {"mu_kT": 0.02, "p_over_rho0kT": 0.02, "density_gap": 0.05},
        "peak_cross_tol": 0.1,
        "max_compress_min": 10,
        "peak_mu_tol": 0.1,
        "gold_mu_kT_B": 1.75,
        "gold_mu_kT_C": 5.0
    }


# === block: score_0 (check id='step1_case_B_compressibility') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    if 'mu_kT' not in artifact[0] or 'compressibility' not in artifact[0]:
        return 0.0
    try:
        mu_vals = [float(row['mu_kT']) for row in artifact]
        comp_vals = [float(row['compressibility']) for row in artifact]
    except:
        return 0.0
    max_comp = max(comp_vals)
    peak_mu = mu_vals[comp_vals.index(max_comp)]
    max_comp_min = step.get('max_compress_min', 10)
    if max_comp < max_comp_min:
        return 0.0
    gold_mu = step.get('gold_mu_kT', None)
    if gold_mu is None:
        return 0.0
    tol = step.get('peak_mu_tol', 0.1)
    diff = abs(peak_mu - gold_mu)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='step2_case_C_compressibility') ===
def score_1(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    if 'mu_kT' not in artifact[0] or 'compressibility' not in artifact[0]:
        return 0.0
    try:
        mu_vals = [float(row['mu_kT']) for row in artifact]
        comp_vals = [float(row['compressibility']) for row in artifact]
    except:
        return 0.0
    max_comp = max(comp_vals)
    peak_mu = mu_vals[comp_vals.index(max_comp)]
    max_comp_min = step.get('max_compress_min', 10)
    if max_comp < max_comp_min:
        return 0.0
    gold_mu = step.get('gold_mu_kT', None)
    if gold_mu is None:
        return 0.0
    tol = step.get('peak_mu_tol', 0.1)
    diff = abs(peak_mu - gold_mu)
    if diff <= tol:
        return 1.0
    elif diff <= 2 * tol:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='step3_transition_parameters') ===
def score_2(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    required_cols = ['case', 'mu_kT', 'p_over_rho0kT', 'density_gap']
    if not all(c in artifact[0] for c in required_cols):
        return 0.0
    rows = {row['case']: row for row in artifact if row['case'] in ('B', 'C')}
    if len(rows) != 2:
        return 0.0
    gold = ctx['gold']
    tol = ctx['tolerances']  # base tolerances from grading spec
    cross_tol = ctx['peak_cross_tol']
    # Per-case overrides: relax for case C per paper's "around 5"
    tolerances_per_case = {
        'B': tol,
        'C': {
            'mu_kT': max(tol.get('mu_kT', 0.02), 0.05),
            'p_over_rho0kT': max(tol.get('p_over_rho0kT', 0.02), 0.05),
            'density_gap': tol.get('density_gap', 0.05)  # keep as is
        }
    }
    scores = []
    for case in ['B', 'C']:
        if case not in rows:
            scores.append(0.0)
            continue
        row = rows[case]
        try:
            mu = float(row['mu_kT'])
            p = float(row['p_over_rho0kT'])
            dg = float(row['density_gap'])
        except:
            scores.append(0.0)
            continue
        g = gold[case]
        t = tolerances_per_case[case]
        ok_mu = 1.0 if abs(mu - g['mu_kT']) <= t['mu_kT'] else 0.0
        ok_p = 1.0 if abs(p - g['p_over_rho0kT']) <= t['p_over_rho0kT'] else 0.0
        ok_dg = 1.0 if abs(dg - g['density_gap']) <= t['density_gap'] else 0.0
        # cross-check compressibility peak
        comp_file = f"case_{case}_compressibility_n{'12' if case=='B' else '14'}.csv"
        comp_path = os.path.join('/app/outputs', comp_file)
        ok_peak = 0.0
        if os.path.exists(comp_path):
            try:
                with open(comp_path, newline='') as f:
                    reader = csv.DictReader(f)
                    comp_data = list(reader)
                if comp_data:
                    mu_vals = [float(r['mu_kT']) for r in comp_data]
                    comp_vals = [float(r['compressibility']) for r in comp_data]
                    max_idx = comp_vals.index(max(comp_vals))
                    peak_mu = mu_vals[max_idx]
                    if abs(peak_mu - mu) <= cross_tol:
                        ok_peak = 1.0
            except:
                ok_peak = 0.0
        case_score = (ok_mu + ok_p + ok_dg + ok_peak) / 4.0
        scores.append(case_score)
    return sum(scores) / 2.0


_SCORERS = {
    'step1_case_B_compressibility': score_0,
    'step2_case_C_compressibility': score_1,
    'step3_transition_parameters': score_2,
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
