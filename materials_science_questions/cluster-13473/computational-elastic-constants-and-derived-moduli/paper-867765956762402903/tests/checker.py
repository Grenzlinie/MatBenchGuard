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
    ctx = {}
    ctx['configs'] = {}
    for s in spec['steps']:
        ctx['configs'][s['id']] = s.get('config', {})
    return ctx


# === block: score_0 (check id='helicity_modulus_check') ===
def score_0(artifact, step, ctx):
    config = ctx['configs']['helicity_modulus_check']
    low_T = config['low_T']
    zero_threshold = config['zero_threshold']
    downturn_gamma_threshold = config['downturn_gamma_threshold']

    closed_data = {}
    open_data = []
    for row in artifact:
        m = int(row['m'])
        bc = row['boundary_condition'].strip().lower()
        T = float(row['temperature_J_over_kB'])
        gamma = float(row['gamma'])
        gamma_err = float(row['gamma_error'])
        if bc == 'closed':
            if m not in closed_data:
                closed_data[m] = []
            closed_data[m].append((T, gamma, gamma_err))
        elif bc == 'open' and m == 6:
            open_data.append((T, gamma, gamma_err))

    scores = []
    # 1. low-T monotonic decrease for closed BC (m=4,5,6,7)
    ms = [4,5,6,7]
    low_gammas = {}
    for m in ms:
        if m not in closed_data:
            scores.append(0.0)
            break
        ts_gammas = closed_data[m]
        best = min(ts_gammas, key=lambda x: abs(x[0] - low_T))
        low_gammas[m] = best
    else:
        vals = [low_gammas[m][1] for m in ms]
        monotonic = True
        for i in range(3):
            if vals[i] < vals[i+1] - 0.01:
                monotonic = False
                break
        if monotonic:
            scores.append(1.0)
        else:
            violations = sum(1 for i in range(3) if vals[i] < vals[i+1] - 0.01)
            scores.append(max(0, 1 - violations/3))

    # 2. open BC gamma ~0 for m=6
    if open_data:
        all_zero = True
        for T, gamma, err in open_data:
            if abs(gamma) > zero_threshold + err:
                all_zero = False
                break
        if all_zero:
            scores.append(1.0)
        else:
            within = sum(1 for T, gamma, err in open_data if abs(gamma) <= zero_threshold + err)
            total = len(open_data)
            scores.append(within / total if total else 0)
    else:
        scores.append(0.0)

    # 3. downturn onset shift (temperature where gamma first falls below threshold)
    onset_temps = {}
    for m in ms:
        if m not in closed_data:
            continue
        ts_gammas = sorted(closed_data[m], key=lambda x: x[0])
        onset = None
        for T, gamma, err in ts_gammas:
            if gamma < downturn_gamma_threshold:
                onset = T
                break
        if onset is not None:
            onset_temps[m] = onset
    if len(onset_temps) == 4:
        temps = [onset_temps[m] for m in ms]
        monotonic = True
        for i in range(3):
            if temps[i] < temps[i+1] - 0.02:
                monotonic = False
                break
        if monotonic:
            scores.append(1.0)
        else:
            violations = sum(1 for i in range(3) if temps[i] < temps[i+1] - 0.02)
            scores.append(max(0, 1 - violations/3))
    else:
        scores.append(0.0)

    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='heat_capacity_check') ===
def score_1(artifact, step, ctx):
    config = ctx['configs']['heat_capacity_check']
    check_T = config['check_temperature']
    max_var = config['max_variation_fraction']

    closed_C = {}
    for row in artifact:
        m = int(row['m'])
        bc = row['boundary_condition'].strip().lower()
        T = float(row['temperature_J_over_kB'])
        C = float(row['heat_capacity_per_site'])
        if bc == 'closed' and m in (4,5,6,7):
            if m not in closed_C:
                closed_C[m] = []
            closed_C[m].append((T, C))

    vals = []
    for m in (4,5,6,7):
        if m not in closed_C:
            return 0.0
        best = min(closed_C[m], key=lambda x: abs(x[0] - check_T))
        vals.append(best[1])
    if len(vals) < 2:
        return 0.0
    mean_val = sum(vals)/len(vals)
    if mean_val == 0:
        return 0.0
    variation = (max(vals) - min(vals)) / mean_val
    if variation <= max_var:
        return 1.0
    else:
        return max(0.0, 1.0 - (variation - max_var) / (max_var * 2))


# === block: score_2 (check id='susceptibility_check') ===
def score_2(artifact, step, ctx):
    pos_ok = True
    for row in artifact:
        chi = float(row['susceptibility_per_site'])
        err = float(row['susceptibility_error'])
        if not (chi > 0 and err > 0):
            pos_ok = False
            break

    if not pos_ok:
        return 0.0

    closed_errs = []
    open_errs = []
    for row in artifact:
        m = int(row['m'])
        bc = row['boundary_condition'].strip().lower()
        err = float(row['susceptibility_error'])
        if m == 6:
            if bc == 'closed':
                closed_errs.append(err)
            elif bc == 'open':
                open_errs.append(err)

    if not closed_errs or not open_errs:
        return 0.0

    mean_closed = sum(closed_errs) / len(closed_errs)
    mean_open = sum(open_errs) / len(open_errs)

    if mean_open > mean_closed:
        return 1.0
    else:
        return 0.5


_SCORERS = {
    'helicity_modulus_check': score_0,
    'heat_capacity_check': score_1,
    'susceptibility_check': score_2,
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
