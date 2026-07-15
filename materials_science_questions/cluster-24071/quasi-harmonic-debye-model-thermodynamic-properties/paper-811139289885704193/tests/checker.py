import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return spec


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    row = rows[0]
    ref = step['reference']
    tols = step['tolerances']
    vals = ['C11_GPa','C12_GPa','C44_GPa','B_GPa']
    passed = 0
    for k in vals:
        try:
            agent_val = float(row[k])
        except (KeyError, ValueError):
            continue
        gold = ref[k]
        tol = tols[k] * abs(gold) if gold != 0 else 0.01
        if abs(agent_val - gold) <= tol:
            passed += 1
    return passed / len(vals)


# === block: score_1 (check id='thermo_values') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_rows = step['gold_rows']
    temp_tol = step.get('temperature_tolerance_K', 2.0)
    tols = step['tolerances']
    props = ['Cv_J_mol_K','S_J_mol_K','alpha_per_K','Bs_GPa']
    total_points = len(gold_rows) * len(props)
    passed_points = 0
    # index agent rows by temperature
    agent_by_temp = {}
    for r in rows:
        try:
            t = float(r.get('temperature_K', ''))
        except (TypeError, ValueError):
            continue
        agent_by_temp[t] = r
    for gold in gold_rows:
        gold_temp = gold['temperature_K']
        best_t = None
        for t in agent_by_temp:
            if abs(t - gold_temp) <= temp_tol:
                best_t = t
                break
        if best_t is None:
            continue
        agent = agent_by_temp[best_t]
        for p in props:
            try:
                agent_val = float(agent[p])
            except (KeyError, ValueError):
                continue
            gold_val = gold[p]
            tol_cfg = tols[p]
            if tol_cfg['type'] == 'relative':
                thresh = tol_cfg['relative'] * abs(gold_val)
            else:
                thresh = max(tol_cfg['relative'] * abs(gold_val), tol_cfg.get('absolute_min', 0))
            if abs(agent_val - gold_val) <= thresh:
                passed_points += 1
    if total_points == 0:
        return 0.0
    return passed_points / total_points


# === block: score_2 (check id='thermo_trends') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # sort by temperature
    sorted_rows = sorted(rows, key=lambda r: float(r.get('temperature_K',0)))
    temps = [float(r['temperature_K']) for r in sorted_rows]
    chev = [float(r['Cv_J_mol_K']) for r in sorted_rows]
    s_vals = [float(r['S_J_mol_K']) for r in sorted_rows]
    bs_vals = [float(r['Bs_GPa']) for r in sorted_rows]
    trends = step.get('trend_checks', {})
    details = {}
    score = 0.0
    # Cv monotonic increasing
    def monotonic(arr, direction):
        if direction == 'increasing':
            return all(arr[i] <= arr[i+1] + 1e-12 for i in range(len(arr)-1))
        else:
            return all(arr[i] >= arr[i+1] - 1e-12 for i in range(len(arr)-1))
    if 'Cv_monotonic_increasing' in trends:
        w = trends['Cv_monotonic_increasing'].get('weight', 0.0)
        ok = monotonic(chev, 'increasing')
        score += w * (1.0 if ok else 0.0)
    if 'Cv_dulong_petit_limit' in trends:
        cfg = trends['Cv_dulong_petit_limit']
        w = cfg.get('weight', 0.0)
        target_temp = cfg['target_temp']
        target_val = cfg['target_value']
        rel_tol = cfg['relative_tol']
        # find row closest to target_temp
        idx = None
        min_diff = 1e9
        for i,t in enumerate(temps):
            diff = abs(t - target_temp)
            if diff < min_diff:
                min_diff = diff
                idx = i
        if idx is not None:
            cv = chev[idx]
            thresh = rel_tol * abs(target_val)
            ok = abs(cv - target_val) <= thresh
            score += w * (1.0 if ok else 0.0)
    if 'S_monotonic_increasing' in trends:
        w = trends['S_monotonic_increasing'].get('weight', 0.0)
        ok = monotonic(s_vals, 'increasing')
        score += w * (1.0 if ok else 0.0)
    if 'Bs_decreasing' in trends:
        w = trends['Bs_decreasing'].get('weight', 0.0)
        ok = monotonic(bs_vals, 'decreasing')
        score += w * (1.0 if ok else 0.0)
    return min(score, 1.0)


_SCORERS = {
    'elastic_constants': score_0,
    'thermo_values': score_1,
    'thermo_trends': score_2,
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
