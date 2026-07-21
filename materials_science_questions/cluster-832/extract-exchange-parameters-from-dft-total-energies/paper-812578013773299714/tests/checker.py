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
    import math
    H0=5.5; p0=0.42; T0=5.0; phi=3.0; H=14.0; factor=0.0225
    pressures = [0,2,4,6,8,10]
    Tc_expected = []
    barrier_expected = []
    for p in pressures:
        val = (H/H0)**2 + p/p0 - 1
        if val > 0:
            Tc = T0 * (val**(1.0/phi))
        else:
            Tc = 0.0
        Tc_expected.append(Tc)
        barrier_expected.append(factor * val)
    ctx = {'pressures': pressures, 'Tc_expected': Tc_expected, 'barrier_expected': barrier_expected}
    return ctx


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    expected = ctx['Tc_expected']
    points = ctx['pressures']
    data = {}
    for row in artifact:
        p = float(row.get('pressure_kbar'))
        tc = float(row.get('critical_temp_K'))
        data[p] = tc
    ok = 0
    for i, p in enumerate(points):
        if p in data and abs(data[p] - expected[i]) <= 0.5:
            ok += 1
    score = ok / len(points) if points else 0.0
    return score


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    pressures = ctx['pressures']
    try:
        data = {}
        for row in artifact:
            p = float(row['pressure_kbar'])
            total = float(row['total_chirality'])
            ordered = float(row['ordered_contribution'])
            fluct = float(row['fluctuation_contribution'])
            ent = float(row['entanglement_entropy'])
            data[p] = (total, ordered, fluct, ent)
    except:
        return 0.0
    vals = {}
    present = True
    for p in pressures:
        if p not in data:
            present = False
            break
        vals[p] = data[p]
    if not present:
        return 0.0
    total = [vals[p][0] for p in pressures]
    ordered = [vals[p][1] for p in pressures]
    fluct = [vals[p][2] for p in pressures]
    ent = [vals[p][3] for p in pressures]
    checks = step.get('params', {}).get('checks', {})
    weights = step.get('params', {}).get('check_weights', {})
    if not weights:
        n = len(checks)
        w = 1.0/n
        weights = {k: w for k in checks}
    results = {}
    if 'ordered_monotonic_increase' in checks:
        inc = all(ordered[i] <= ordered[i+1] for i in range(len(ordered)-1))
        results['ordered_monotonic_increase'] = 1.0 if inc else 0.0
    if 'fluctuation_nonmonotonic' in checks:
        max_idx = fluct.index(max(fluct))
        if max_idx == 0 or max_idx == len(fluct)-1:
            nonmono = False
        else:
            decr = True
            for i in range(max_idx, len(fluct)-1):
                if fluct[i+1] > fluct[i]:
                    decr = False
                    break
            incr = True
            for i in range(0, max_idx):
                if fluct[i] > fluct[i+1]:
                    incr = False
                    break
            nonmono = incr and decr
        results['fluctuation_nonmonotonic'] = 1.0 if nonmono else 0.0
    if 'entropy_monotonic_decrease' in checks:
        dec = all(ent[i] >= ent[i+1] for i in range(len(ent)-1))
        results['entropy_monotonic_decrease'] = 1.0 if dec else 0.0
    if 'sum_check' in checks:
        ok_sum = True
        for i in range(len(pressures)):
            if abs(total[i] - (ordered[i] + fluct[i])) > 1e-6:
                ok_sum = False
                break
        results['sum_check'] = 1.0 if ok_sum else 0.0
    if 'fluctuation_fraction_at_p0' in checks:
        p0_idx = pressures.index(0)
        if fluct[p0_idx] >= 0.9 * total[p0_idx]:
            results['fluctuation_fraction_at_p0'] = 1.0
        else:
            results['fluctuation_fraction_at_p0'] = 0.0
    if 'peak_fluctuation_between_0_and_6' in checks:
        max_fluct = max(fluct)
        max_p = [p0 for p0, f in zip(pressures, fluct) if f == max_fluct][0]
        results['peak_fluctuation_between_0_and_6'] = 1.0 if max_p <= 6 else 0.0
    score = 0.0
    for k, w in weights.items():
        if k in results:
            score += w * results[k]
    return min(score, 1.0)


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    expected = ctx['barrier_expected']
    points = ctx['pressures']
    data = {}
    for row in artifact:
        p = float(row.get('pressure_kbar'))
        du = float(row.get('potential_barrier_J_per_m2'))
        data[p] = du
    ok = 0
    for i, p in enumerate(points):
        if p in data:
            ref = expected[i]
            if ref != 0 and abs(data[p] - ref) <= 0.20 * abs(ref):
                ok += 1
            elif ref == 0 and abs(data[p]) <= 1e-12:
                ok += 1
    score = ok / len(points) if points else 0.0
    return score


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
