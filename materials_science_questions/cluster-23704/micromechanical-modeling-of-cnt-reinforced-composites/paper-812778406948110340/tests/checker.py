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
    return {}


# === block: score_0 (check id='linear_and_nonlinear_frequencies') ===
def score_0(artifact, step, ctx):
        gold_table = step.get('gold_table', [])
        tol_l = float(step.get('tol_linear', 0.02))
        tol_nl = float(step.get('tol_nonlinear', 0.03))
        # Build lookup dict from gold rows: key = (bc, hc_hf, kw, ks, q, w_max)
        gold_dict = {}
        for g in gold_table:
            key = (str(g['boundary_condition']), float(g['hc_hf']), float(g['kw']), float(g['ks']),
                   int(g['q']), float(g['w_max']))
            gold_dict[key] = (float(g['omega_l']), float(g['omega_nl']))
        rows = artifact  # list of dict
        if not rows:
            return 0.0
        sum_score = 0.0
        n = 0
        for row in rows:
            try:
                key = (str(row['boundary_condition']).strip(), float(row['hc_hf']), float(row['kw']),
                       float(row['ks']), int(float(row['q'])), float(row['w_max']))
                if key not in gold_dict:
                    continue
                gold_l, gold_nl = gold_dict[key]
                omega_l = float(row['omega_l'])
                omega_nl = float(row['omega_nl'])
                # Relative error
                err_l = abs(omega_l - gold_l) / max(abs(gold_l), 1e-9)
                err_nl = abs(omega_nl - gold_nl) / max(abs(gold_nl), 1e-9)
                # Score each: full credit if within tol, else linear decay to 0 at 3*tol
                def score_one(err, tol):
                    if err <= tol: return 1.0
                    return max(0.0, 1.0 - (err - tol) / (2*tol))
                sc_l = score_one(err_l, tol_l)
                sc_nl = score_one(err_nl, tol_nl)
                row_score = 0.5 * sc_l + 0.5 * sc_nl
                sum_score += row_score
                n += 1
            except (KeyError, ValueError, TypeError):
                continue
        if n == 0:
            return 0.0
        return sum_score / n


# === block: score_1 (check id='aggregation_effect') ===
def score_1(artifact, step, ctx):
        rows = artifact  # list of dict with eta, mu, w_max, omega_l, omega_nl, ratio
        if not rows:
            return 0.0
        checks = step.get('checks', {})
        w_const = float(checks.get('omega_l_constant', 0.25))
        w_ratio_one = float(checks.get('ratio_one_at_zero', 0.25))
        w_ord_l = float(checks.get('omega_l_ordering', 0.25))
        w_ord_r = float(checks.get('ratio_ordering', 0.25))
        # Group by (eta, mu)
        groups = {}
        for r in rows:
            key = (float(r['eta']), float(r['mu']))
            groups.setdefault(key, []).append(r)
        score_omega_l_const = 0.0
        score_ratio_one = 0.0
        score_ord_l = 0.0
        score_ord_r = 0.0
        # Check 1: omega_l constant across w_max for each group (coefficient of variation < 1%)
        n_groups = 0
        for key, grp in groups.items():
            vals = [float(r['omega_l']) for r in grp]
            if len(vals) < 2:
                continue
            mean = sum(vals)/len(vals)
            if mean == 0:
                continue
            max_dev = max(abs(v-mean) for v in vals)
            if max_dev / mean <= 0.005:  # 0.5% tolerance
                score_omega_l_const += 1.0
            n_groups += 1
        if n_groups > 0:
            score_omega_l_const /= n_groups
        # Check 2: for rows where w_max == 0, ratio should be 1.0 (within 1e-4)
        zero_rows = [r for r in rows if abs(float(r['w_max'])) < 1e-8]
        if zero_rows:
            ok = all(abs(float(r['ratio']) - 1.0) < 1e-4 for r in zero_rows)
            score_ratio_one = 1.0 if ok else 0.0
        else:
            score_ratio_one = 0.0
        # Check 3: omega_l(0.4,0.4) > omega_l(0.4,0.1) for each w_max
        try:
            data_by_wmax = {}
            for r in rows:
                w = float(r['w_max'])
                eta = float(r['eta'])
                mu = float(r['mu'])
                if not (abs(eta-0.4)<1e-6 and (abs(mu-0.4)<1e-6 or abs(mu-0.1)<1e-6)):
                    continue
                data_by_wmax.setdefault(w, {})
            pairs = {}
            for w, items in data_by_wmax.items():
                if 0.4 in items and 0.1 in items:
                    pairs[w] = (items[0.4], items[0.1])
            if pairs:
                passed = 0
                for w, (v_disp, v_clus) in pairs.items():
                    if v_disp > v_clus:
                        passed += 1
                score_ord_l = passed / len(pairs)
        except (KeyError, ValueError):
            score_ord_l = 0.0
        # Check 4: ratio(0.4,0.4) < ratio(0.4,0.1) for each w_max > 0
        try:
            data_by_wmax_r = {}
            for r in rows:
                w = float(r['w_max'])
                if w <= 0:
                    continue
                eta = float(r['eta'])
                mu = float(r['mu'])
                if not (abs(eta-0.4)<1e-6 and (abs(mu-0.4)<1e-6 or abs(mu-0.1)<1e-6)):
                    continue
                data_by_wmax_r.setdefault(w, {})
            pairs_r = {}
            for w, items in data_by_wmax_r.items():
                if 0.4 in items and 0.1 in items:
                    pairs_r[w] = (items[0.4], items[0.1])
            if pairs_r:
                passed = 0
                for w, (r_disp, r_clus) in pairs_r.items():
                    if r_disp < r_clus:
                        passed += 1
                score_ord_r = passed / len(pairs_r)
        except (KeyError, ValueError):
            score_ord_r = 0.0
        total = w_const * score_omega_l_const + w_ratio_one * score_ratio_one + w_ord_l * score_ord_l + w_ord_r * score_ord_r
        return min(1.0, total)


_SCORERS = {
    'linear_and_nonlinear_frequencies': score_0,
    'aggregation_effect': score_1,
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
