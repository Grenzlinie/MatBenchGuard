import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, collections


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


# === block: score_0 (check id='fitted_params') ===
def score_0(artifact, step, ctx):
    required_params = {
      'A2_t','omega2_t','mu2_t','A3_t','omega3_t','mu3_t',
      'A2_h','omega2_h','mu2_h','A3_h','omega3_h','mu3_h',
      'a_t','b_t','c_t','a_h','b_h','c_h','r0','V','K','n'
    }
    rows = artifact  # list of dicts from fitted_parameters.csv
    by_pressure = collections.defaultdict(set)
    for r in rows:
        try:
            p = float(r['pressure'])
        except:
            continue
        by_pressure[p].add(r['parameter_name'].strip())
    pressures = list(by_pressure.keys())
    if len(pressures) < 3:
        return 0.0

    complete_count = 0
    for p in pressures:
        if required_params.issubset(by_pressure[p]):
            complete_count += 1
    completeness = complete_count / len(pressures) if pressures else 0.0

    # Build per-pressure param dicts
    by_pressure_params = collections.defaultdict(dict)
    for r in rows:
        try:
            p = float(r['pressure'])
        except:
            continue
        param = r['parameter_name'].strip()
        try:
            val = float(r['value'])
        except:
            continue
        by_pressure_params[p][param] = val

    # Recompute P_r from fitted parameters
    recomputed = {}
    for p, params in by_pressure_params.items():
        A2t = params.get('A2_t')
        om2t = params.get('omega2_t')
        A3t = params.get('A3_t')
        om3t = params.get('omega3_t')
        A2h = params.get('A2_h')
        om2h = params.get('omega2_h')
        A3h = params.get('A3_h')
        om3h = params.get('omega3_h')
        if None in (A2t, om2t, A3t, om3t, A2h, om2h, A3h, om3h):
            continue
        if om2t==0 or om3t==0 or om2h==0 or om3h==0:
            continue
        Ct = A2t/om2t + A3t/om3t
        Ch = A2h/om2h + A3h/om3h
        if Ct + Ch == 0:
            continue
        Pr = (Ct - Ch) / (Ct + Ch)
        recomputed[p] = Pr

    if len(recomputed) < 2:
        return 0.5 * completeness

    # Load agent's pr_vs_pressure.csv for consistency check
    pr_csv_path = '/app/outputs/pr_vs_pressure.csv'
    if not os.path.exists(pr_csv_path):
        consistency_score = 0.0
    else:
        with open(pr_csv_path, newline='') as f:
            reader = csv.DictReader(f)
            reported = {}
            for row in reader:
                try:
                    p = float(row['pressure'])
                    pr = float(row['Pr'])
                except:
                    continue
                reported[p] = pr
        matched = 0
        total = 0
        for p, pr_rec in recomputed.items():
            if p in reported:
                pr_rep = reported[p]
                if abs(pr_rec - pr_rep) <= 1e-4:
                    matched += 1
                total += 1
        consistency_score = matched / total if total > 0 else 0.0

    # Gold endpoint check (paper Fig. 3)
    gold_low  = 0.2
    tol_low   = 0.1
    gold_high = -0.38
    tol_high  = 0.1

    min_p = min(recomputed.keys())
    max_p = max(recomputed.keys())
    pr_min = recomputed[min_p]
    pr_max = recomputed[max_p]

    def score_value(value, gold, tol):
        if abs(value - gold) <= tol:
            return 1.0
        extra = abs(value - gold) - tol
        return max(0.0, 1.0 - extra / 0.15)

    score_low = score_value(pr_min, gold_low, tol_low)
    score_high = score_value(pr_max, gold_high, tol_high)
    pr_score = 0.5 * score_low + 0.5 * score_high

    # Combine: completeness (0.2), cross-consistency (0.2), Pr accuracy (0.6)
    return 0.2 * completeness + 0.2 * consistency_score + 0.6 * pr_score


# === block: score_1 (check id='pr_curve') ===
def score_1(artifact, step, ctx):
    import math
    fitted_path = '/app/outputs/fitted_parameters.csv'
    if not os.path.exists(fitted_path):
        return 0.0
    with open(fitted_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # organize
    data = collections.defaultdict(dict)
    for r in rows:
        try:
            p = float(r['pressure'])
        except:
            continue
        param = r['parameter_name'].strip()
        try:
            val = float(r['value'])
        except:
            continue
        data[p][param] = val
    pressures = []
    prs = []
    for p, params in data.items():
        A2t = params.get('A2_t')
        om2t = params.get('omega2_t')
        A3t = params.get('A3_t')
        om3t = params.get('omega3_t')
        A2h = params.get('A2_h')
        om2h = params.get('omega2_h')
        A3h = params.get('A3_h')
        om3h = params.get('omega3_h')
        if None in (A2t, om2t, A3t, om3t, A2h, om2h, A3h, om3h):
            continue
        if om2t==0 or om3t==0 or om2h==0 or om3h==0:
            continue
        Ct = A2t/om2t + A3t/om3t
        Ch = A2h/om2h + A3h/om3h
        if Ct + Ch == 0:
            continue
        Pr = (Ct - Ch) / (Ct + Ch)
        pressures.append(p)
        prs.append(Pr)
    # sort by pressure
    pairs = sorted(zip(pressures, prs))
    if len(pairs) < 3:
        return 0.0
    sorted_p, sorted_pr = zip(*pairs)
    # monotonic decreasing check (allow tiny noise)
    mono_ok = True
    mono_pairs = 0
    for i in range(1, len(sorted_pr)):
        if sorted_pr[i] <= sorted_pr[i-1] + 1e-6:
            mono_pairs += 1
        else:
            mono_ok = False
    mono_score = mono_pairs / (len(sorted_pr)-1) if len(sorted_pr)>1 else 1.0
    # sign check: low pressure >0, high pressure <0
    sign_ok = (sorted_pr[0] > 0) and (sorted_pr[-1] < 0)
    sign_score = 1.0 if sign_ok else 0.0
    return 0.8 * mono_score + 0.2 * sign_score


# === block: score_2 (check id='crossover') ===
def score_2(artifact, step, ctx):
    import math
    fitted_path = '/app/outputs/fitted_parameters.csv'
    if not os.path.exists(fitted_path):
        return 0.0
    with open(fitted_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    data = collections.defaultdict(dict)
    for r in rows:
        try:
            p = float(r['pressure'])
        except:
            continue
        param = r['parameter_name'].strip()
        try:
            val = float(r['value'])
        except:
            continue
        data[p][param] = val
    pressures = []
    prs = []
    for p, params in data.items():
        A2t = params.get('A2_t')
        om2t = params.get('omega2_t')
        A3t = params.get('A3_t')
        om3t = params.get('omega3_t')
        A2h = params.get('A2_h')
        om2h = params.get('omega2_h')
        A3h = params.get('A3_h')
        om3h = params.get('omega3_h')
        if None in (A2t, om2t, A3t, om3t, A2h, om2h, A3h, om3h):
            continue
        if om2t==0 or om3t==0 or om2h==0 or om3h==0:
            continue
        Ct = A2t/om2t + A3t/om3t
        Ch = A2h/om2h + A3h/om3h
        if Ct + Ch == 0:
            continue
        Pr = (Ct - Ch) / (Ct + Ch)
        pressures.append(p / 1000.0)   # bar -> kbar
        prs.append(Pr)
    # sort
    pairs = sorted(zip(pressures, prs))
    if len(pairs) < 2:
        return 0.0
    # find sign change
    cross = None
    for i in range(len(pairs)-1):
        p1, pr1 = pairs[i]
        p2, pr2 = pairs[i+1]
        if pr1 * pr2 <= 0:
            # linear interpolation
            if abs(pr2 - pr1) < 1e-12:
                cross = p1
            else:
                cross = p1 - pr1 * (p2 - p1) / (pr2 - pr1)
            break
    if cross is None:
        return 0.0
    target = step.get('params', {}).get('target_crossover_kbar', 2.3)
    tol = step.get('params', {}).get('tolerance_abs', 0.5)
    diff = abs(cross - target)
    if diff <= tol:
        return 1.0
    else:
        # graded decay beyond tolerance
        score = max(0.0, 1.0 - (diff - tol) / (tol * 0.5))
        return score


_SCORERS = {
    'fitted_params': score_0,
    'pr_curve': score_1,
    'crossover': score_2,
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
