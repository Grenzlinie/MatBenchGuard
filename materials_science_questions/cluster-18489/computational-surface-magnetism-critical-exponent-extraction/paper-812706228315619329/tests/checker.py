import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math
def load_csv_file(path):
    if not os.path.exists(path):
        return []
    with open(path, newline='') as f:
        return list(csv.DictReader(f))
def extract_tc(data, case, threshold=0.005):
    rows = [r for r in data if r['case']==case]
    if not rows:
        return None
    rows.sort(key=lambda r: float(r['T']))
    ts = [float(r['T']) for r in rows]
    ms = [float(r['M_total']) for r in rows]
    for i in range(len(ts)-1, -1, -1):
        if abs(ms[i]) > threshold:
            if i+1 < len(ts) and ms[i]*ms[i+1] < 0:
                t0, t1 = ts[i], ts[i+1]
                m0, m1 = ms[i], ms[i+1]
                return t0 - m0*(t1-t0)/(m1-m0)
            return ts[i]
    return None
def extract_tcomp(data, case='SAFM', threshold=0.005):
    rows = [r for r in data if r['case']==case]
    if not rows:
        return None
    rows.sort(key=lambda r: float(r['T']))
    ts = [float(r['T']) for r in rows]
    ms = [float(r['M_total']) for r in rows]
    for i in range(len(ms)-1):
        if ms[i]*ms[i+1] < 0:
            t0, t1 = ts[i], ts[i+1]
            m0, m1 = ms[i], ms[i+1]
            return t0 - m0*(t1-t0)/(m1-m0)
    return None
def extract_all_hc_abs(data, case, T):
    rows = [r for r in data if r['case']==case and int(float(r['T']))==T]
    if not rows:
        return []
    # use original row order to preserve hysteresis loop direction
    hs = [float(r['H']) for r in rows]
    ms = [float(r['M_total']) for r in rows]
    crossings = []
    for i in range(len(ms)-1):
        if ms[i]*ms[i+1] < 0:
            h0, h1 = hs[i], hs[i+1]
            m0, m1 = ms[i], ms[i+1]
            hc = h0 - m0*(h1-h0)/(m1-m0)
            crossings.append(abs(hc))
    return sorted(set(round(v, 6) for v in crossings))


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


# === block: score_0 (check id='mt_Tc') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold = step['gold']
    tol_rel = step.get('tolerance_relative', 0.05)
    scores = []
    for case, target in gold.items():
        tc = extract_tc(data, case)
        if tc is None:
            scores.append(0.0)
            continue
        error = abs(tc - target)
        tol = tol_rel * abs(target)
        if error <= tol:
            scores.append(1.0)
        else:
            s = max(0.0, 1.0 - (error - tol) / tol)
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='mt_Tcomp') ===
def score_1(artifact, step, ctx):
    data = artifact
    gold = step['gold']
    tol_abs = step.get('tolerance_abs', 0.1)
    tcomp = extract_tcomp(data)
    if tcomp is None:
        return 0.0
    error = abs(tcomp - gold)
    if error <= tol_abs:
        return 1.0
    else:
        return max(0.0, 1.0 - (error - tol_abs) / tol_abs)


# === block: score_2 (check id='mh_Hc') ===
def score_2(artifact, step, ctx):
    data = artifact
    gold_map = step['gold']
    tol_rel = step.get('tolerance_relative', 0.1)
    tol_abs_floor = step.get('tolerance_abs_floor', 0.05)
    total = 0
    correct = 0
    for case, temps in gold_map.items():
        for T_str, expected in temps.items():
            T = int(T_str)
            total += 1
            cross = extract_all_hc_abs(data, case, T)
            if abs(expected) < 1e-9:
                if not cross or max(cross) <= tol_abs_floor:
                    correct += 1
            else:
                if any(abs(v - abs(expected)) <= max(tol_rel*abs(expected), tol_abs_floor) for v in cross):
                    correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_3 (check id='summary_consistent') ===
def score_3(artifact, step, ctx):
    summary = artifact
    mt_path = '/app/outputs/mt_data.csv'
    mh_path = '/app/outputs/mh_data.csv'
    mt_data = load_csv_file(mt_path)
    mh_data = load_csv_file(mh_path)
    tol = step.get('tolerances', {})
    tc_rel = tol.get('Tc_relative', 0.05)
    tcomp_abs = tol.get('Tcomp_abs', 0.1)
    hc_rel = tol.get('Hc_relative', 0.1)
    hc_abs_floor = tol.get('Hc_abs_floor', 0.05)
    gold_hc = step.get('gold_hc', {})
    checks = []
    # Tc
    for case, key in [('FM','Tc_FM'),('EAFM','Tc_EAFM'),('SAFM','Tc_SAFM')]:
        rep = summary.get(key)
        comp = extract_tc(mt_data, case)
        if comp is None or rep is None:
            checks.append(False)
        else:
            checks.append(abs(rep - comp) <= max(tc_rel*abs(comp), 0.01))
    # Tcomp
    rep_tc = summary.get('T_comp_SAFM')
    comp_tc = extract_tcomp(mt_data)
    if comp_tc is not None and rep_tc is not None:
        checks.append(abs(rep_tc - comp_tc) <= tcomp_abs)
    else:
        checks.append(False)
    # Hc consistency
    hc_entries = summary.get('Hc_values', [])
    if not isinstance(hc_entries, list):
        hc_entries = []
    total_hc = 0
    ok_hc = 0
    for entry in hc_entries:
        case = entry.get('case')
        T = entry.get('T')
        hc_rep = entry.get('Hc')
        if case is None or T is None:
            continue
        expected = gold_hc.get(case,{}).get(str(T))
        if expected is None:
            continue
        total_hc += 1
        # reported Hc absolute
        if isinstance(hc_rep, (int, float)):
            rep_abs = abs(hc_rep)
        elif isinstance(hc_rep, list):
            rep_abs = [abs(v) for v in hc_rep]
        else:
            continue
        # computed crossings
        cross = extract_all_hc_abs(mh_data, case, T)
        # extracted match
        if abs(expected) < 1e-9:
            ext_ok = not cross or max(cross) <= hc_abs_floor
        else:
            ext_ok = any(abs(v - abs(expected)) <= max(hc_rel*abs(expected), hc_abs_floor) for v in cross)
        # reported match
        if isinstance(rep_abs, list):
            rep_ok = any(abs(v - abs(expected)) <= max(hc_rel*abs(expected), hc_abs_floor) for v in rep_abs)
        else:
            rep_ok = abs(rep_abs - abs(expected)) <= max(hc_rel*abs(expected), hc_abs_floor)
        if ext_ok and rep_ok:
            ok_hc += 1
    if total_hc > 0:
        checks.append(ok_hc / total_hc)
    else:
        checks.append(False)
    passed = sum(1 for c in checks if c)
    return passed / len(checks) if checks else 0.0


_SCORERS = {
    'mt_Tc': score_0,
    'mt_Tcomp': score_1,
    'mh_Hc': score_2,
    'summary_consistent': score_3,
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
