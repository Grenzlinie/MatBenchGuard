import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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


# === block: score_0 (check id='bulk_conductivity') ===
def score_0(artifact, step, ctx):
    import json, math
    gold_GaN = step['fields']['GaN']['gold']
    tol_GaN = step['fields']['GaN']['tolerance']
    gold_SiC = step['fields']['SiC']['gold']
    tol_SiC = step['fields']['SiC']['tolerance']
    if not isinstance(artifact, dict):
        return 0.0
    val_GaN = artifact.get('GaN')
    val_SiC = artifact.get('SiC')
    if val_GaN is None or val_SiC is None:
        return 0.0
    try:
        err_GaN = abs(float(val_GaN) - gold_GaN) / abs(gold_GaN)
        err_SiC = abs(float(val_SiC) - gold_SiC) / abs(gold_SiC)
    except (TypeError, ValueError):
        return 0.0
    max_err = max(err_GaN, err_SiC)
    if max_err <= tol_GaN:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (max_err - tol_GaN) / 0.3)
    return score


# === block: score_1 (check id='itc_trend') ===
def score_1(artifact, step, ctx):
    import csv, math, io
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    required = ['defect_concentration', 'defect_location', 'heat_flux', 'temperature_drop', 'itc']
    if not all(c in rows[0] for c in required):
        return 0.0
    checks = step['checks']
    w_cons = checks[0]['weight']
    w_mono = checks[1]['weight']
    w_pct = checks[2]['weight']
    tol_rel = checks[0]['tolerance_rel']
    pass_count = 0
    total = 0
    for row in rows:
        try:
            Q = float(row['heat_flux'])
            dT = float(row['temperature_drop'])
            itc = float(row['itc'])
            if dT == 0:
                continue
            calc = Q / dT
            if abs(calc) < 1e-12:
                continue
            err = abs(itc - calc) / abs(calc)
            if err <= tol_rel:
                pass_count += 1
            total += 1
        except (ValueError, KeyError):
            continue
    score_cons = pass_count / total if total > 0 else 0.0
    data = {}
    for row in rows:
        loc = row.get('defect_location', '')
        if loc in ('GaN', 'SiC'):
            try:
                c = float(row['defect_concentration'])
                itc = float(row['itc'])
                data.setdefault(loc, []).append((c, itc))
            except (ValueError, KeyError):
                continue
    def pearson_r(x, y):
        n = len(x)
        if n < 2:
            return 0.0
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xx = sum(v*v for v in x)
        sum_yy = sum(v*v for v in y)
        sum_xy = sum(x[i]*y[i] for i in range(n))
        denom = ((n*sum_xx - sum_x**2) * (n*sum_yy - sum_y**2))**0.5
        if denom == 0:
            return 0.0
        return (n*sum_xy - sum_x*sum_y) / denom
    scores = []
    thresh_r = checks[1].get('correlation_threshold', 0.8)
    for loc in ['GaN', 'SiC']:
        if loc not in data or len(data[loc]) < 2:
            scores.append(0.0)
            continue
        cs, itcs = zip(*data[loc])
        r = pearson_r(cs, itcs)
        if loc == 'GaN':
            if r <= -thresh_r:
                scores.append(1.0)
            elif r < 0:
                scores.append((-r) / thresh_r)
            else:
                scores.append(0.0)
        else:
            if r >= thresh_r:
                scores.append(1.0)
            elif r > 0:
                scores.append(r / thresh_r)
            else:
                scores.append(0.0)
    score_mono = sum(scores) / 2.0 if scores else 0.0
    gold_pct_GaN = checks[2]['gold_pct_GaN']
    gold_pct_SiC = checks[2]['gold_pct_SiC']
    tol_pct = checks[2]['tolerance_pct_rel']
    itc0 = None
    for row in rows:
        if row.get('defect_location') == 'none':
            try:
                itc0 = float(row['itc'])
            except (ValueError, KeyError):
                pass
            break
    if itc0 is None or abs(itc0) < 1e-12:
        score_pct = 0.0
    else:
        pct_scores = []
        for loc, gold_pct in [('GaN', gold_pct_GaN), ('SiC', gold_pct_SiC)]:
            pct_val = None
            for row in rows:
                if row.get('defect_location') == loc and float(row['defect_concentration']) == 0.05:
                    try:
                        itc_c = float(row['itc'])
                        pct_val = 100.0 * (itc_c - itc0) / itc0
                    except (ValueError, KeyError):
                        pass
                    break
            if pct_val is None:
                pct_scores.append(0.0)
                continue
            lo = gold_pct * (1.0 - tol_pct)
            hi = gold_pct * (1.0 + tol_pct)
            if gold_pct < 0:
                lo, hi = sorted([lo, hi])
            else:
                lo, hi = sorted([lo, hi])
            if lo <= pct_val <= hi:
                pct_scores.append(1.0)
            else:
                pct_scores.append(0.0)
        score_pct = sum(pct_scores) / 2.0 if pct_scores else 0.0
    final = w_cons * score_cons + w_mono * score_mono + w_pct * score_pct
    return max(0.0, min(1.0, final))


_SCORERS = {
    'bulk_conductivity': score_0,
    'itc_trend': score_1,
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
