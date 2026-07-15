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


# === block: score_0 (check id='deviation_analysis') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact
        if not rows:
            return 0.0
        # Parse rows, converting to float
        data = []
        for r in rows:
            Cv = float(r.get('C_v', '').strip())
            nc = float(r.get('n_c', '').strip())
            t1 = float(r.get('t1', '').strip())
            f = float(r.get('f', '').strip())
            f_inf = float(r.get('f_inf', '').strip())
            devp = float(r.get('deviation_percent', '').strip())
            data.append({'Cv': Cv, 'nc': nc, 't1': t1, 'f': f, 'f_inf': f_inf, 'devp': devp})
        if len(data) < 7:
            return 0.0
        # Sub-checks with normalized weights (summing to 1.0 internally, then multiplied by step weight later by harness, but we return a score between 0 and 1)
        # We'll compute a score from 0 to 1 based on subchecks.
        sub_scores = {}
        # 1. Row count check (minimal weight)
        has7 = 1.0 if len(data) >= 7 else 0.0
        sub_scores['count'] = has7 * 0.05
        # 2. All deviation_percent >= 0
        all_pos = all(d['devp'] >= 0.0 for d in data)
        sub_scores['positive'] = (1.0 if all_pos else 0.0) * 0.05
        # 3. Monotonic decreasing deviation with decreasing Cv.
        # Sort by Cv descending.
        sorted_data = sorted(data, key=lambda x: x['Cv'], reverse=True)
        devps = [d['devp'] for d in sorted_data]
        monoton = all(devps[i] >= devps[i+1] for i in range(len(devps)-1))
        sub_scores['monotonic'] = (1.0 if monoton else 0.0) * 0.15
        # 4. Threshold bounds: at Cv around 9.5e-4 (within 5% tolerance) deviation < 1.0
        # Find rows with Cv close to 9.5e-4.
        tol_Cv = 1e-6
        def find_row(target):
            matches = []
            for d in data:
                if abs(d['Cv'] - target) < tol_Cv:
                    matches.append(d)
            return matches[0] if matches else None
        row_1e3 = find_row(9.5e-4)  # closest to 1e-3
        if row_1e3:
            bound_pass_1e3 = row_1e3['devp'] < 1.0
        else:
            bound_pass_1e3 = False
        row_1e4 = find_row(3.7e-4)  # closest to 1e-4
        if row_1e4:
            bound_pass_1e4 = row_1e4['devp'] < 0.2
        else:
            bound_pass_1e4 = False
        sub_scores['thresholds'] = (1.0 if (bound_pass_1e3 and bound_pass_1e4) else 0.0) * 0.20
        # 5. t1 in plausible range (-0.123, -0.122)
        t1_ok = all(-0.123 <= d['t1'] <= -0.122 for d in data)
        sub_scores['t1_range'] = (1.0 if t1_ok else 0.0) * 0.10
        # 6. Self-consistency: recompute f from t1, n_c, and cross-validate f and deviation_pct
        def compute_f(t1, n):
            # Eq.8: f = (1+t1)/(1-t1) * [1 - (2*t1/n)*(1 - t1**n)/(1 - t1**2)]
            # Handle potential small numeric issues
            if abs(1 - t1) < 1e-12:
                return None
            factor = (1 + t1) / (1 - t1)
            if abs(1 - t1*t1) < 1e-12:
                return None
            # Compute t1**n; if n is large and |t1|<1, t1**n might underflow to 0.0 which is fine
            try:
                t1n = t1 ** n
            except OverflowError:
                t1n = 0.0
            bracket = 1.0 - (2.0 * t1 / n) * (1.0 - t1n) / (1.0 - t1 * t1)
            return factor * bracket
        consistency_fail = False
        dev_calc_ok = True
        for d in data:
            f_calc = compute_f(d['t1'], d['nc'])
            if f_calc is None:
                consistency_fail = True
                break
            # Compare f (should be very close)
            if abs(d['f'] - f_calc) > 1e-6:
                consistency_fail = True
                break
            # Compare deviation percent
            if d['f_inf'] == 0.0:
                consistency_fail = True
                break
            dev_calc = 100.0 * (f_calc - d['f_inf']) / d['f_inf']
            if abs(d['devp'] - dev_calc) > 1e-3:  # tolerance 0.001 pp
                consistency_fail = True
                break
        sub_scores['consistency'] = (0.0 if consistency_fail else 1.0) * 0.35
        # 7. f_inf consistency across rows (should be the same, within tiny tolerance)
        f_infs = [d['f_inf'] for d in data]
        f_inf_range = max(f_infs) - min(f_infs)
        f_inf_consistent = f_inf_range < 1e-8
        sub_scores['f_inf_stable'] = (1.0 if f_inf_consistent else 0.0) * 0.10
        total = sum(sub_scores.values())
        return total
    except Exception:
        return 0.0


_SCORERS = {
    'deviation_analysis': score_0,
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
