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
    return {}


# === block: score_0 (check id='check_excitation') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_map = {g['T']: g['nu_empirical'] for g in step['gold']}
    scored_Ts = step.get('scored_temperatures', list(gold_map.keys()))
    tol = step.get('tolerance', 0.0)
    passed = 0
    total = 0
    for row in rows:
        try:
            T_val = float(row['T'])
            nu_val = float(row['nu_empirical'])
        except (ValueError, KeyError):
            continue
        if T_val in scored_Ts:
            total += 1
            if abs(nu_val - gold_map[T_val]) <= tol:
                passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='check_thermal') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # extract r and w columns
    r_vals = []
    wp_vals = []
    wh_vals = []
    we_vals = []
    for row in rows:
        try:
            r = float(row['r'])
            wp = float(row['w_paired_phonon'])
            wh = float(row['w_hydrodynamic'])
            we = float(row['w_empirical'])
        except (ValueError, KeyError):
            continue
        r_vals.append(r)
        wp_vals.append(wp)
        wh_vals.append(wh)
        we_vals.append(we)
    if len(r_vals) < 2:
        return 0.0
    # sub-check 1: at smallest r, wp > wh > we
    min_idx = r_vals.index(min(r_vals))
    ordering_ok = (wp_vals[min_idx] > wh_vals[min_idx] > we_vals[min_idx])
    # sub-check 2: we has a local maximum between 2 and 5 Å
    peak_found = False
    for i in range(1, len(r_vals)-1):
        if 2.0 <= r_vals[i] <= 5.0:
            if we_vals[i-1] < we_vals[i] > we_vals[i+1]:
                peak_found = True
                break
    score = 0.0
    if ordering_ok:
        score += 0.5
    if peak_found:
        score += 0.5
    return score


# === block: score_2 (check id='check_condensate') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_rows = {g['T']: g for g in step['gold']}
    tol = step.get('tolerance', 0.0)
    passed = 0
    total = 0
    for row in rows:
        try:
            T_val = float(row['T'])
            n_p = float(row['n_paired_phonon'])
            n_h = float(row['n_hydrodynamic'])
            n_e = float(row['n_empirical'])
        except (ValueError, KeyError):
            continue
        gold = gold_rows.get(T_val)
        if gold is None:
            continue
        total += 1
        p_ok = abs(n_p - gold['n_paired_phonon']) <= tol
        h_ok = abs(n_h - gold['n_hydrodynamic']) <= tol
        e_ok = abs(n_e - gold['n_empirical']) <= tol
        if p_ok and h_ok and e_ok:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'check_excitation': score_0,
    'check_thermal': score_1,
    'check_condensate': score_2,
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
