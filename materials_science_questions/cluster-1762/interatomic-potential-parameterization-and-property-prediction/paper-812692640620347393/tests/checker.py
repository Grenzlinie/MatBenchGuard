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


# === block: score_0 (check id='step-2') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    count = 0
    for r in rows:
        try:
            aag = float(r['F_AgAg'])
            as_ = float(r['F_AgS'])
            sa = float(r['F_SAg'])
            ss = float(r['F_SS'])
        except (KeyError, ValueError):
            continue
        other_max = max(as_, sa, ss)
        if aag > 10.0 * other_max and aag > 0:
            count += 1
    return count / len(rows) if rows else 0.0


# === block: score_1 (check id='step-3') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    from collections import defaultdict
    data = defaultdict(dict)
    fwhm_data = {}
    for r in rows:
        try:
            temp = int(r['temperature'])
            q = (float(r['Q_h']), float(r['Q_k']), float(r['Q_l']))
            val = float(r['S_zero'])
            data[temp][q] = val
            # Extract FWHM only for (1.6,1,0) rows; tolerate null/empty values
            fwhm_str = str(r.get('FWHM_meV', '')).strip()
            if fwhm_str and fwhm_str.lower() != 'null':
                fwhm = float(fwhm_str)
                if q == (1.6, 1, 0):
                    fwhm_data[temp] = fwhm
        except (KeyError, ValueError):
            continue
    temperatures = [268, 339, 470]
    q_vectors = [
        (1.8, 1, 0),
        (1.6, 1, 0),
        (1.4, 1, 0),
        (1.6, 0.8, 0),
        (1.6, 1.2, 0)
    ]
    if not all(t in data for t in temperatures):
        return 0.0
    checks = []
    if 470 in data and (1.6,1,0) in data[470]:
        center = data[470][(1.6,1,0)]
        others = [data[470][q] for q in q_vectors if q != (1.6,1,0)]
        checks.append(center >= max(others))
    else:
        checks.append(False)
    if all(pos in data[470] for pos in [(1.8,1,0),(1.6,0.8,0),(1.4,1,0),(1.6,1.2,0),(1.6,1,0)]):
        center = data[470][(1.6,1,0)]
        d_h_18 = center - data[470][(1.8,1,0)]
        d_k_08 = center - data[470][(1.6,0.8,0)]
        d_h_14 = center - data[470][(1.4,1,0)]
        d_k_12 = center - data[470][(1.6,1.2,0)]
        checks.append(d_h_18 > d_k_08 and d_h_14 > d_k_12)
    else:
        checks.append(False)
    temp_mono = True
    for q in q_vectors:
        vals = [data[t].get(q) for t in temperatures]
        if None in vals:
            temp_mono = False
            break
        if not (vals[0] >= vals[1] >= vals[2]):
            temp_mono = False
            break
    checks.append(temp_mono)
    # FWHM monotonic increase for Q=(1.6,1,0)
    fwhm_vals = [fwhm_data.get(t) for t in temperatures]
    if all(isinstance(v, (int, float)) for v in fwhm_vals):
        checks.append(fwhm_vals[0] < fwhm_vals[1] < fwhm_vals[2])
    else:
        checks.append(False)
    passed = sum(1 for c in checks if c)
    return passed / len(checks) if checks else 0.0


# === block: score_2 (check id='step-4') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    from collections import defaultdict
    by_temp = defaultdict(list)
    for r in rows:
        try:
            t = int(r['temperature'])
            e = float(r['energy_meV'])
            s = float(r['S'])
            by_temp[t].append((e, s))
        except (KeyError, ValueError):
            continue
    def find_peak(en_s_list, low, high):
        subset = [(e,s) for e,s in en_s_list if low <= e <= high]
        if not subset:
            return None, None
        best = max(subset, key=lambda x: x[1])
        return best[0], best[1]
    score = 0.0
    if 268 in by_temp:
        e_peak, s_peak = find_peak(by_temp[268], 0, 5)
        s_0 = next((s for e,s in by_temp[268] if abs(e) < 0.001), None)
        s_5 = next((s for e,s in by_temp[268] if abs(e - 5) < 0.001), None)
        if e_peak is not None and s_0 is not None and s_5 is not None:
            if s_peak > s_0 and s_peak > s_5 and 2.5 <= e_peak <= 4.0:
                score += 0.4
    if 339 in by_temp:
        e_peak, s_peak = find_peak(by_temp[339], 0, 5)
        if e_peak is not None:
            s_0 = next((s for e,s in by_temp[339] if abs(e) < 0.001), None)
            s_5 = next((s for e,s in by_temp[339] if abs(e - 5) < 0.001), None)
            if s_0 is not None and s_5 is not None and s_peak > s_0 and s_peak > s_5:
                score += 0.3
    if 470 in by_temp:
        e_peak, s_peak = find_peak(by_temp[470], 0, 5)
        if e_peak is not None and e_peak <= 0.2:
            score += 0.3
    return min(score, 1.0)


# === block: score_3 (check id='step-5') ===
def score_3(artifact, step, ctx):
    data = artifact
    score = 0.0
    p268 = data.get('peak_energy_meV_268K')
    if isinstance(p268, (int, float)) and 2.5 <= p268 <= 4.0:
        score += 0.5
    p339 = data.get('peak_energy_meV_339K')
    if p339 is None:
        score += 0.3
    elif isinstance(p339, (int, float)) and 2.0 <= p339 <= 3.5:
        score += 0.3
    p470 = data.get('peak_energy_meV_470K')
    if p470 is None:
        score += 0.2
    return score


_SCORERS = {
    'step-2': score_0,
    'step-3': score_1,
    'step-4': score_2,
    'step-5': score_3,
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
