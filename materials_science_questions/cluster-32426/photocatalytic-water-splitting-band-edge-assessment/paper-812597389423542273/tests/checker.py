import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    try:
        val = float(artifact.strip())
    except Exception:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance_abs', 0.0)
    if abs(val - target) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    try:
        val = float(artifact.strip())
    except Exception:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance_abs', 0.0)
    if abs(val - target) <= tol:
        return 1.0
    return 0.0


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    rows = artifact
    ranges = step.get('ranges', {})
    expected = {}
    for key, rng in ranges.items():
        parts = key.split('_')
        if len(parts) >= 2:
            typ = parts[0]
            dirn = parts[1]
            expected[(typ, dirn)] = (rng['min'], rng['max'])
    count = 0
    correct = 0
    for row in rows:
        typ = row.get('type', '').strip().lower()
        dirn = row.get('direction', '').strip().lower()
        mob = float(row.get('mobility', 0))
        key = (typ, dirn)
        if key in expected:
            lo, hi = expected[key]
            count += 1
            if lo <= mob <= hi:
                correct += 1
    if count == 0:
        return 0.0
    return correct / count


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    rows = artifact
    n_data = []
    p_data = []
    for row in rows:
        dtype = row.get('doping_type', '').strip()
        conc = float(row.get('carrier_concentration', 0))
        pfx = float(row.get('power_factor_x', 0))
        pfy = float(row.get('power_factor_y', 0))
        if dtype == 'n':
            n_data.append((conc, max(pfx, pfy)))
        elif dtype == 'p':
            p_data.append((conc, pfx))
    if not n_data or not p_data:
        return 0.0
    n_peak_pf = max(n_data, key=lambda x: x[1])[1]
    n_peak_conc = [x[0] for x in n_data if x[1] == n_peak_pf][0]
    p_peak_pf = max(p_data, key=lambda x: x[1])[1]
    p_peak_conc = [x[0] for x in p_data if x[1] == p_peak_pf][0]
    n_pf_range = step.get('n_peak_pf_range', [33.7, 49.8])
    n_conc_target = step.get('n_opt_conc_target', 4.0e20)
    n_tol_factor = step.get('n_opt_conc_tolerance_factor', 1.5)
    pf_n_score = 0.0
    if n_pf_range[0] <= n_peak_pf <= n_pf_range[1]:
        pf_n_score = 1.0
    else:
        lo, hi = n_pf_range
        if n_peak_pf < lo:
            diff = lo - n_peak_pf
        else:
            diff = n_peak_pf - hi
        pf_n_score = max(0.0, 1.0 - diff / 5.0)
    log_conc = math.log10(n_peak_conc)
    log_target = math.log10(n_conc_target)
    log_tol = math.log10(n_tol_factor)
    conc_n_score = 0.0
    if abs(log_conc - log_target) <= log_tol:
        conc_n_score = 1.0
    else:
        conc_n_score = max(0.0, 1.0 - (abs(log_conc - log_target) - log_tol) / (0.5 * log_tol))
    p_pf_range = step.get('p_peak_pf_range', [15.0, 16.0])
    p_conc_target = step.get('p_opt_conc_target', 2.5e19)
    p_tol_factor = step.get('p_opt_conc_tolerance_factor', 1.5)
    pf_p_score = 0.0
    if p_pf_range[0] <= p_peak_pf <= p_pf_range[1]:
        pf_p_score = 1.0
    else:
        lo, hi = p_pf_range
        if p_peak_pf < lo:
            diff = lo - p_peak_pf
        else:
            diff = p_peak_pf - hi
        pf_p_score = max(0.0, 1.0 - diff / 2.0)
    log_conc_p = math.log10(p_peak_conc)
    log_target_p = math.log10(p_conc_target)
    log_tol_p = math.log10(p_tol_factor)
    conc_p_score = 0.0
    if abs(log_conc_p - log_target_p) <= log_tol_p:
        conc_p_score = 1.0
    else:
        conc_p_score = max(0.0, 1.0 - (abs(log_conc_p - log_target_p) - log_tol_p) / (0.5 * log_tol_p))
    score = (pf_n_score + conc_n_score + pf_p_score + conc_p_score) / 4.0
    return score


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_05': score_2,
    'step_06': score_3,
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
