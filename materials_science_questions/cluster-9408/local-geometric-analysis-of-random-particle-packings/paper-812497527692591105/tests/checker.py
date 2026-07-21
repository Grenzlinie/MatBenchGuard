import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import json
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
    def _load_csv(path):
        with open(path, 'r') as f:
            return list(csv.DictReader(f))
    def _load_json(path):
        with open(path, 'r') as f:
            return json.load(f)

    free_theo_path = os.path.join(outputs_dir, 'free_theoretical.csv')
    stick_theo_path = os.path.join(outputs_dir, 'sticking_theoretical.csv')
    free_sim_path = os.path.join(outputs_dir, 'free_simulation.csv')
    stick_sim_path = os.path.join(outputs_dir, 'sticking_simulation.csv')
    summary_path = os.path.join(outputs_dir, 'results_summary.json')

    ctx = {}
    ctx['free_theoretical'] = _load_csv(free_theo_path) if os.path.exists(free_theo_path) else None
    ctx['sticking_theoretical'] = _load_csv(stick_theo_path) if os.path.exists(stick_theo_path) else None
    ctx['free_simulation'] = _load_csv(free_sim_path) if os.path.exists(free_sim_path) else None
    ctx['sticking_simulation'] = _load_csv(stick_sim_path) if os.path.exists(stick_sim_path) else None
    ctx['summary'] = _load_json(summary_path) if os.path.exists(summary_path) else None
    return ctx


# === block: score_0 (check id='step_theoretical_free') ===
def score_0(artifact, step, ctx):
    params = step['parameters']
    tolerance = params['tolerance']
    s = params['s']
    if not artifact:
        return 0.0
    passed = 0
    for row in artifact:
        omega = float(row['omega'])
        rho = float(row['coverage_fraction'])
        expected = omega * math.exp(-2 * omega * (1 + s**2))
        if abs(rho - expected) <= tolerance:
            passed += 1
    if len(artifact) == 0:
        return 0.0
    return passed / len(artifact)


# === block: score_1 (check id='step_theoretical_sticking') ===
def score_1(artifact, step, ctx):
    params = step['parameters']
    tolerance = params['tolerance']
    s = params['s']
    if not artifact:
        return 0.0
    passed = 0
    for row in artifact:
        omega = float(row['omega'])
        rho = float(row['coverage_fraction'])
        expected = (1 - math.exp(-2 * (1 + s**2) * omega)) / (2 * (1 + s**2))
        if abs(rho - expected) <= tolerance:
            passed += 1
    if len(artifact) == 0:
        return 0.0
    return passed / len(artifact)


# === block: score_2 (check id='step_simulation_free') ===
def score_2(artifact, step, ctx):
    params = step['parameters']
    check_omegas = params['check_omegas']
    tol_abs = params['tolerance_abs']
    peak_omega_expected = params['peak_omega_expected']
    peak_tol = params['peak_tolerance_abs']
    s = 1.2

    if not artifact:
        return 0.0

    data = {}
    for row in artifact:
        omega = round(float(row['omega']), 6)
        data[omega] = float(row['coverage_fraction'])

    if not data:
        return 0.0

    # peak location
    max_rho = -1
    max_omega = None
    for omega, rho in data.items():
        if rho > max_rho:
            max_rho = rho
            max_omega = omega
    peak_ok = 1.0 if max_omega is not None and abs(max_omega - peak_omega_expected) <= peak_tol else 0.0

    # interpolation helper
    def interp(target, omegas_sorted, rhos_dict):
        if not omegas_sorted:
            return None
        if target <= omegas_sorted[0]:
            if len(omegas_sorted) >= 2:
                o1 = omegas_sorted[0]
                o2 = omegas_sorted[1]
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
            else:
                return rhos_dict[omegas_sorted[0]]
        if target >= omegas_sorted[-1]:
            if len(omegas_sorted) >= 2:
                o1 = omegas_sorted[-2]
                o2 = omegas_sorted[-1]
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
            else:
                return rhos_dict[omegas_sorted[-1]]
        # find interval
        for i, o in enumerate(omegas_sorted):
            if o > target:
                o1 = omegas_sorted[i-1]
                o2 = o
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
        return None

    omegas_sorted = sorted(data.keys())
    pass_count = 0
    for omega in check_omegas:
        sim_rho = interp(omega, omegas_sorted, data)
        if sim_rho is None:
            continue
        theoretical_rho = omega * math.exp(-2 * omega * (1 + s**2))
        if abs(sim_rho - theoretical_rho) <= tol_abs:
            pass_count += 1

    trend_score = pass_count / len(check_omegas) if check_omegas else 1.0
    return trend_score * 0.7 + peak_ok * 0.3


# === block: score_3 (check id='step_simulation_sticking') ===
def score_3(artifact, step, ctx):
    params = step['parameters']
    check_omegas = params['check_omegas']
    tol_abs = params['tolerance_abs']
    s = 1.2

    if not artifact:
        return 0.0

    data = {}
    for row in artifact:
        omega = round(float(row['omega']), 6)
        data[omega] = float(row['coverage_fraction'])

    if not data:
        return 0.0

    omegas_sorted = sorted(data.keys())
    def interp(target, omegas_sorted, rhos_dict):
        if not omegas_sorted:
            return None
        if target <= omegas_sorted[0]:
            if len(omegas_sorted) >= 2:
                o1 = omegas_sorted[0]
                o2 = omegas_sorted[1]
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
            else:
                return rhos_dict[omegas_sorted[0]]
        if target >= omegas_sorted[-1]:
            if len(omegas_sorted) >= 2:
                o1 = omegas_sorted[-2]
                o2 = omegas_sorted[-1]
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
            else:
                return rhos_dict[omegas_sorted[-1]]
        for i, o in enumerate(omegas_sorted):
            if o > target:
                o1 = omegas_sorted[i-1]
                o2 = o
                return rhos_dict[o1] + (rhos_dict[o2] - rhos_dict[o1])/(o2 - o1)*(target - o1)
        return None

    pass_count = 0
    for omega in check_omegas:
        sim_rho = interp(omega, omegas_sorted, data)
        if sim_rho is None:
            continue
        theoretical_rho = (1 - math.exp(-2 * (1 + s**2) * omega)) / (2 * (1 + s**2))
        if abs(sim_rho - theoretical_rho) <= tol_abs:
            pass_count += 1

    return pass_count / len(check_omegas) if check_omegas else 1.0


# === block: score_4 (check id='step_summary') ===
def score_4(artifact, step, ctx):
    params = step['parameters']
    paper_free_max = params['paper_free_max']
    tol_free_max = params['tol_free_max']
    paper_stick = params['paper_stick_at_0.5']
    tol_stick = params['tol_stick_at_0.5']
    theoretical_max_tol = params['theoretical_max_tol']
    s = 1.2

    if not artifact:
        return 0.0

    checks = 0

    # 1. theoretical free max
    free_theo_csv = ctx.get('free_theoretical')
    if free_theo_csv:
        omegas = [float(r['omega']) for r in free_theo_csv]
        rhos = [float(r['coverage_fraction']) for r in free_theo_csv]
        if omegas:
            max_idx = max(range(len(rhos)), key=lambda i: rhos[i])
            max_rhos = rhos[max_idx]
            reported = artifact.get('free_max_theoretical')
            if reported is not None and abs(reported - max_rhos) < 1e-6:
                expected_max = math.exp(-1) / (2 * (1 + s**2))
                if abs(max_rhos - expected_max) <= theoretical_max_tol:
                    checks += 1

    # 2. free simulation max
    free_sim_csv = ctx.get('free_simulation')
    if free_sim_csv:
        omegas_sim = [float(r['omega']) for r in free_sim_csv]
        rhos_sim = [float(r['coverage_fraction']) for r in free_sim_csv]
        if omegas_sim:
            max_idx_sim = max(range(len(rhos_sim)), key=lambda i: rhos_sim[i])
            max_rhos_sim = rhos_sim[max_idx_sim]
            reported_sim = artifact.get('free_max_simulation')
            if reported_sim is not None and abs(reported_sim - max_rhos_sim) < 1e-6:
                if abs(max_rhos_sim - paper_free_max) <= tol_free_max:
                    checks += 1

    # 3. sticking theoretical at omega=0.5
    if 'stick_at_0.5_theoretical' in artifact:
        expected_stick = (1 - math.exp(-2*(1+s**2)*0.5)) / (2*(1+s**2))
        if abs(artifact['stick_at_0.5_theoretical'] - expected_stick) <= theoretical_max_tol:
            checks += 1

    # 4. sticking simulation at omega=0.5
    stick_sim_csv = ctx.get('sticking_simulation')
    if stick_sim_csv and 'stick_at_0.5_simulation' in artifact:
        omegas_stick = [float(r['omega']) for r in stick_sim_csv]
        rhos_stick = [float(r['coverage_fraction']) for r in stick_sim_csv]
        if omegas_stick:
            # interpolation
            target = 0.5
            interp_rho = None
            # copy of interpolation logic (could use same helper but we'll inline simple version)
            # sort
            zipped = sorted(zip(omegas_stick, rhos_stick))
            osorted, rsorted = zip(*zipped) if zipped else ([], [])
            if osorted:
                if target <= osorted[0]:
                    if len(osorted) >= 2:
                        interp_rho = rsorted[0] + (rsorted[1]-rsorted[0])/(osorted[1]-osorted[0])*(target - osorted[0])
                    else:
                        interp_rho = rsorted[0]
                elif target >= osorted[-1]:
                    if len(osorted) >= 2:
                        interp_rho = rsorted[-2] + (rsorted[-1]-rsorted[-2])/(osorted[-1]-osorted[-2])*(target - osorted[-2])
                    else:
                        interp_rho = rsorted[-1]
                else:
                    for i, o in enumerate(osorted):
                        if o > target:
                            o1 = osorted[i-1]
                            o2 = o
                            interp_rho = rsorted[i-1] + (rsorted[i]-rsorted[i-1])/(o2 - o1)*(target - o1)
                            break
                if interp_rho is not None:
                    if abs(artifact['stick_at_0.5_simulation'] - interp_rho) < 1e-6 and abs(interp_rho - paper_stick) <= tol_stick:
                        checks += 1

    return checks / 4.0


_SCORERS = {
    'step_theoretical_free': score_0,
    'step_theoretical_sticking': score_1,
    'step_simulation_free': score_2,
    'step_simulation_sticking': score_3,
    'step_summary': score_4,
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
