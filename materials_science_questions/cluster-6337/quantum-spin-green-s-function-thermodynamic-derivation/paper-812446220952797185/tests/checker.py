import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    def prepare(artifact_dir, spec):
        # Load critical temperature for consistency checks
        critical_data = None
        try:
            with open(os.path.join(artifact_dir, 'critical_temperature.csv'), newline='') as f:
                reader = csv.DictReader(f)
                critical_data = [
                    {
                        'omega': float(row['omega_over_J']),
                        'kBTc': float(row['kBTc_over_J'])
                    } for row in reader
                ]
            # sort by omega
            critical_data.sort(key=lambda r: r['omega'])
        except Exception:
            critical_data = []
        ctx = {'critical_data': critical_data}
        return ctx


# === block: score_0 (check id='critical_temperature') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        # Filter and convert rows to float pairs, skip invalid
        valid = []
        for r in rows:
            try:
                omega = float(r['omega_over_J'])
                kbtc = float(r['kBTc_over_J'])
                valid.append((omega, kbtc))
            except (ValueError, TypeError, KeyError):
                continue
        if not valid:
            return 0.0
        # sort by omega
        valid.sort(key=lambda x: x[0])
        # 1. Tc at omega=0: find point with omega closest to 0
        target_tc = step['hidden']['tc_at_zero_target']
        tol_rel = step['hidden']['tc_at_zero_tol_rel']
        best = min(valid, key=lambda x: abs(x[0]))
        tc_val = best[1]
        score_tc = 1.0 if abs(tc_val - target_tc) <= target_tc * tol_rel else 0.0
        # 2. Monotonic decreasing
        kbtc_vals = [v[1] for v in valid]
        monotonic = all(kbtc_vals[i] >= kbtc_vals[i+1] - 1e-12 for i in range(len(kbtc_vals)-1))
        score_mono = 1.0 if monotonic else 0.0
        # 3. Critical field from curve (first omega where kBTc < 1e-4)
        target_omega_c = step['hidden']['critical_field_target']
        tol_rel_c = step['hidden']['critical_field_tol_rel']
        omega_c_approx = None
        for omega, kbtc in valid:
            if kbtc < 1e-4:
                omega_c_approx = omega
                break
        if omega_c_approx is not None:
            if abs(omega_c_approx - target_omega_c) <= target_omega_c * tol_rel_c:
                score_critical = 1.0
            else:
                score_critical = 0.0
        else:
            score_critical = 0.0
        overall = 0.4 * score_tc + 0.3 * score_mono + 0.3 * score_critical
        return overall


# === block: score_1 (check id='temperature_dependence') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        # 1. T=0 limits
        limits = step['hidden']['t0_limits']
        tol = step['hidden']['t0_tol_abs']
        # find row with kBT_over_J smallest
        def get_val(row, col):
            return float(row.get(col, 0.0))
        rows_sorted = sorted(rows, key=lambda r: get_val(r, 'kBT_over_J'))
        t0_row = rows_sorted[0] if rows_sorted else {}
        errors = []
        for col, target in limits.items():
            val = get_val(t0_row, col)
            if abs(val - target) > tol:
                errors.append(1.0)
        t0_score = max(0.0, 1.0 - sum(errors)/len(limits))
        # 2. Consistency with critical temperature for omega=1.5
        mz_zero_tol = step['hidden']['mz_zero_tol_abs']
        critical_data = ctx.get('critical_data', [])
        # find Tc for omega=1.5 in critical data
        tc_target = None
        for entry in critical_data:
            if abs(entry['omega'] - 1.5) < 0.001:
                tc_target = entry['kBTc']
                break
        if tc_target is None and critical_data:
            # interpolate
            omegas = [e['omega'] for e in critical_data]
            kbtcs = [e['kBTc'] for e in critical_data]
            from math import fsum
            # simple linear interp
            idx = sorted(range(len(omegas)), key=lambda i: abs(omegas[i]-1.5))
            if len(idx) >= 2:
                i1,i2 = idx[0], idx[1]
                if omegas[i1] == omegas[i2]:
                    tc_target = kbtcs[i1]
                else:
                    slope = (kbtcs[i2]-kbtcs[i1])/(omegas[i2]-omegas[i1])
                    tc_target = kbtcs[i1] + slope*(1.5-omegas[i1])
        if tc_target is not None:
            # find mz at temperature nearest tc_target
            rows_by_temp = sorted(rows, key=lambda r: abs(get_val(r,'kBT_over_J') - tc_target))
            nearest = rows_by_temp[0] if rows_by_temp else {}
            mz_at_tc = get_val(nearest, 'mz')
            tc_consistency = 1.0 if mz_at_tc <= mz_zero_tol else 0.0
        else:
            tc_consistency = 0.0
        overall = 0.6*t0_score + 0.4*tc_consistency
        return overall


# === block: score_2 (check id='field_dependence') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        # 1. Omega=0 limits
        limits = step['hidden']['omega0_limits']
        tol = step['hidden']['omega0_tol_abs']
        rows_sorted = sorted(rows, key=lambda r: float(r.get('omega_over_J', 1e9)))
        omega0_rows = [(float(r['omega_over_J']), float(r['mz']), float(r['mx'])) for r in rows_sorted]
        if not omega0_rows:
            base_score = 0.0
        else:
            best = min(omega0_rows, key=lambda x: abs(x[0]))
            mz_val, mx_val = best[1], best[2]
            err = 0
            if abs(mz_val - limits.get('mz',1.0)) > tol:
                err += 1
            if abs(mx_val - limits.get('mx',0.0)) > tol:
                err += 1
            base_score = max(0.0, 1.0 - err/2.0)
        # 2. Consistency with critical field
        mz_zero_tol = step['hidden']['mz_zero_tol_abs']
        critical_data = ctx.get('critical_data', [])
        # find omega where mz drops below tol
        omega_c_approx = None
        for omega, mz, mx in omega0_rows:
            if mz <= mz_zero_tol:
                omega_c_approx = omega
                break
        # target critical field from paper
        target_omega_c = 2.241
        if omega_c_approx is not None and target_omega_c is not None:
            if abs(omega_c_approx - target_omega_c) <= target_omega_c * 0.05:
                field_consistency = 1.0
            else:
                field_consistency = 0.0
        else:
            field_consistency = 0.0
        return 0.5*base_score + 0.5*field_consistency


_SCORERS = {
    'critical_temperature': score_0,
    'temperature_dependence': score_1,
    'field_dependence': score_2,
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
