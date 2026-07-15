import os
import json
import csv


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


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    import csv, os, io

    def load_csv(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    artifact = load_csv(os.path.join('/app/outputs', step['output_file']))

    kappa1_vals = [5, 10, 20, 55, 70]
    theta_vals = [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    grid_points = [(k, t) for k in kappa1_vals for t in theta_vals]

    rows_by_key = {}
    for row in artifact:
        try:
            k = float(row['kappa1'])
            t = float(row['theta'])
            r = float(row['rho_star'])
            typ = row['transition_type'].strip()
        except Exception:
            return 0.0
        key = (k, t)
        rows_by_key.setdefault(key, []).append({'rho_star': r, 'type': typ})

    checks = step.get('structural_checks', [])
    total_weight = sum(c.get('weight_in_step', 0) for c in checks)
    if total_weight == 0:
        return 1.0

    score = 0.0

    for check in checks:
        cid = check['id']
        w = check.get('weight_in_step', 0)
        passed = False
        try:
            if cid == 'grid_completeness':
                passed = all(key in rows_by_key for key in grid_points)

            elif cid == 'kappa1_5_nunb_absent':
                # For kappa1=5, NuNb rows exist only for theta <= -0.6
                good = True
                for t in [-1.0, -0.8, -0.6]:
                    rows = rows_by_key.get((5, t), [])
                    if not any(r['type'] == 'NuNb' for r in rows):
                        good = False
                for t in [-0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
                    rows = rows_by_key.get((5, t), [])
                    if any(r['type'] == 'NuNb' for r in rows):
                        good = False
                passed = good

            elif cid == 'kappa1_10_nunb_present_low_theta':
                # NuNb rows exist at theta = -1.0, -0.5, 0.0 (we interpret as all non-positive theta)
                good = True
                for t in [-1.0, -0.8, -0.6, -0.4, -0.2, 0.0]:
                    rows = rows_by_key.get((10, t), [])
                    if not any(r['type'] == 'NuNb' for r in rows):
                        good = False
                for t in [0.2, 0.4, 0.6, 0.8, 1.0]:
                    rows = rows_by_key.get((10, t), [])
                    if any(r['type'] == 'NuNb' for r in rows):
                        good = False
                passed = good

            elif cid == 'kappa1_20_nunb_present_at_theta0':
                # NuNb row exists at theta = 0.0 and absent at theta = 1.0
                rows0 = rows_by_key.get((20, 0.0), [])
                rows1 = rows_by_key.get((20, 1.0), [])
                passed = (any(r['type'] == 'NuNb' for r in rows0) and
                          not any(r['type'] == 'NuNb' for r in rows1))

            elif cid == 'kappa1_55_reentrance':
                rows = rows_by_key.get((55, 1.0), [])
                nunb_rows = [r for r in rows if r['type'] == 'NuNb']
                nonuni_rows = [r for r in rows if r['type'] == 'nonuniform']
                if len(nunb_rows) == 2 and nonuni_rows:
                    nunb_rhos = sorted([r['rho_star'] for r in nunb_rows])
                    nonuni_rho = min(r['rho_star'] for r in nonuni_rows)
                    passed = (nunb_rhos[0] < nonuni_rho) and (nunb_rhos[1] < nonuni_rho)
                else:
                    passed = False

            elif cid == 'kappa1_70_nunb_all_theta':
                passed = all(
                    any(r['type'] == 'NuNb' for r in rows_by_key.get((70, t), []))
                    for t in theta_vals
                )

            elif cid == 'ordering_nunb_before_nonuniform':
                good = True
                for key, rows in rows_by_key.items():
                    nunb_rhos = [r['rho_star'] for r in rows if r['type'] == 'NuNb']
                    nonuni_rhos = [r['rho_star'] for r in rows if r['type'] == 'nonuniform']
                    if nunb_rhos and nonuni_rhos:
                        min_nunb = min(nunb_rhos)
                        min_nonuni = min(nonuni_rhos)
                        if min_nunb >= min_nonuni:
                            good = False
                            break
                passed = good

            elif cid == 'rho_star_positive':
                passed = all(
                    row['rho_star'] > 0 and row['rho_star'] <= 1000
                    for rows in rows_by_key.values() for row in rows
                )

            else:
                continue
        except Exception:
            passed = False

        if passed:
            score += w

    return min(1.0, score / total_weight)


_SCORERS = {
    'step_2': score_0,
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
