import os
import json
import csv

# === author imports / helpers ===
import csv
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
    csv_path = os.path.join(outputs_dir, 'equilibrium_compositions.csv')
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    species_cols = [col for col in rows[0].keys() if col not in ('Q_NH3','case','T_K')]

    # Organise by (Q, case) -> list of (T, row_dict)
    data = defaultdict(list)
    for row in rows:
        Q = float(row['Q_NH3'])
        case = row['case']
        T = float(row['T_K'])
        data[(Q, case)].append((T, row))

    # Compute Si(l) existence ranges for case 'with_Si_liquid'
    si_l_ranges = {}
    for Q in [2.5, 5.0, 10.0, 15.0, 20.0]:
        key = (Q, 'with_Si_liquid')
        if key in data:
            entries = sorted(data[key], key=lambda x: x[0])
            Ts_pos = [T for T, r in entries if float(r.get('Si_l_mol', 0.0)) > 0.0]
            if Ts_pos:
                si_l_ranges[Q] = (min(Ts_pos), max(Ts_pos))
            else:
                si_l_ranges[Q] = (None, None)
        else:
            si_l_ranges[Q] = (None, None)

    # Compute supersaturation proxy for without_Si_liquid (max Si_g/total moles)
    supersat_info = {}
    for Q in [2.5, 5.0, 10.0, 15.0, 20.0]:
        key = (Q, 'without_Si_liquid')
        if key in data:
            entries = sorted(data[key], key=lambda x: x[0])
            ratios = []
            for T, r in entries:
                total = sum(float(r.get(c, 0.0)) for c in species_cols)
                si_g = float(r.get('Si_g_mol', 0.0))
                ratio = si_g / total if total > 0 else 0.0
                ratios.append((T, ratio))
            if ratios:
                best_T, best_val = max(ratios, key=lambda x: x[1])
                supersat_info[Q] = (best_T, best_val)
            else:
                supersat_info[Q] = (None, 0.0)
        else:
            supersat_info[Q] = (None, 0.0)

    return {
        'si_l_ranges': si_l_ranges,
        'supersat_info': supersat_info,
        'data': dict(data),
        'species_cols': species_cols,
    }


# === block: score_0 (check id='check_si_l_range') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    Q = float(params.get('Q_NH3', 15.0))
    gold_low = float(params['gold_low_K'])
    gold_high = float(params['gold_high_K'])
    tol = float(params['tolerance_K'])
    low, high = ctx['si_l_ranges'].get(Q, (None, None))
    if low is None or high is None:
        return 0.0
    d_low = abs(low - gold_low)
    d_high = abs(high - gold_high)
    if d_low <= tol and d_high <= tol:
        return 1.0
    elif d_low <= tol or d_high <= tol:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='check_supersat_structural') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    Q = float(params.get('Q_NH3', 15.0))
    T_min = float(params['T_min_peak'])
    T_max = float(params['T_max_peak'])
    min_val = float(params['min_ratio'])
    peak_T, peak_val = ctx['supersat_info'].get(Q, (None, 0.0))
    if peak_T is None:
        return 0.0
    if T_min <= peak_T <= T_max and peak_val > min_val:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='check_width_trend') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    Q_vals = [float(q) for q in params.get('Q_values', [])]
    widths = {}
    for Q in Q_vals:
        low, high = ctx['si_l_ranges'].get(Q, (None, None))
        if low is not None and high is not None:
            widths[Q] = high - low
        else:
            widths[Q] = None
    # expected trend: w10 > w15, w5 < w10, w2.5 < w5
    w15 = widths.get(15.0)
    w10 = widths.get(10.0)
    w5 = widths.get(5.0)
    w2_5 = widths.get(2.5)
    if None in (w15, w10, w5, w2_5):
        return 0.0
    if w10 > w15 and w5 < w10 and w2_5 < w5:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'check_si_l_range': score_0,
    'check_supersat_structural': score_1,
    'check_width_trend': score_2,
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
