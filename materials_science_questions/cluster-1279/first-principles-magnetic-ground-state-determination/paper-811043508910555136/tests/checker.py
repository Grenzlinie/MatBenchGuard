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


# === block: score_0 (check id='s2') ===
def score_0(artifact, step, ctx):
    # s2 scorer: validate magnetic ground state trends from magnetic_data.csv
    rows = artifact
    if not rows:
        return 0.0
    # Check required columns
    required_cols = ['a','configuration','total_energy','Fe_moment','Mn_moment']
    if not all(col in rows[0] for col in required_cols):
        return 0.0
    # Parse thresholds from step
    t = step.get('thresholds', {})
    a_low_max = t.get('a', {}).get('low_max', 7.0)
    a_high_min = t.get('a', {}).get('high_min', 7.1)
    mn_fm_low = t.get('Mn_moment_fm_low', 1.0)
    mn_fm_high = t.get('Mn_moment_fm_high', 1.5)
    fim_a_min = t.get('fim_a_min', 7.17)
    mn_fim_min = t.get('Mn_moment_fim_min', 1.7)
    diff_tol = t.get('energy_diff_tol', 0.001)

    # Parse data
    fm_rows = []
    fim_rows = []
    nm_rows = []
    for r in rows:
        cfg = r['configuration'].strip()
        a_val = float(r['a'])
        e = float(r['total_energy'])
        fe = float(r['Fe_moment'])
        mn = float(r['Mn_moment'])
        if cfg == 'FM':
            fm_rows.append((a_val, e, fe, mn))
        elif cfg == 'FIM':
            fim_rows.append((a_val, e, fe, mn))
        elif cfg == 'NM':
            nm_rows.append((a_val, e, fe, mn))

    # 1. Existence baseline (NM, FM, FIM)
    score_exist = 1.0 if (len(fm_rows)>0 and len(fim_rows)>0 and len(nm_rows)>0) else 0.0

    # 2. FM spin-state transition
    fm_low = any(a <= a_low_max and mn <= mn_fm_low for a, e, fe, mn in fm_rows)
    fm_high = any(a >= a_high_min and mn >= mn_fm_high for a, e, fe, mn in fm_rows)
    if fm_low and fm_high:
        fm_score = 1.0
    elif fm_low or fm_high:
        fm_score = 0.5
    else:
        fm_score = 0.0

    # 3. FIM existence: all rows must have a >= fim_a_min (with small tolerance)
    a_tol = 0.02
    fim_a_valid = all(a >= fim_a_min - a_tol for a, e, fe, mn in fim_rows) if fim_rows else False
    has_fim_a_high = any(a >= fim_a_min for a, e, fe, mn in fim_rows)
    if fim_rows and fim_a_valid and has_fim_a_high:
        fim_exist_score = 1.0
    elif fim_rows and fim_a_valid:
        fim_exist_score = 0.7
    elif fim_rows:
        fim_exist_score = 0.3
    else:
        fim_exist_score = 0.0

    # 4. FIM high-spin Mn moment
    mn_tol = 0.2
    if fim_rows:
        mn_ok = all(mn >= mn_fim_min - mn_tol for a, e, fe, mn in fim_rows)
        fim_high_score = 1.0 if mn_ok else 0.5 if any(mn >= mn_fim_min - mn_tol) else 0.0
    else:
        fim_high_score = 1.0  # no FIM rows, no violation

    # 5. No low-spin FIM
    low_mn_cut = 1.2
    if fim_rows:
        has_low = any(mn < low_mn_cut for a, e, fe, mn in fim_rows)
        fim_no_low_score = 0.0 if has_low else 1.0
    else:
        fim_no_low_score = 1.0

    # 6. Energy ordering: FM vs FIM crossing
    fm_dict = {a: e for a, e, fe, mn in fm_rows}
    fim_dict = {a: e for a, e, fe, mn in fim_rows}
    common_a_set = set(fm_dict.keys()) & set(fim_dict.keys())
    common_a = sorted(common_a_set)
    energy_score = 0.0
    if common_a:
        diffs = [(a, fim_dict[a] - fm_dict[a]) for a in common_a if a in fm_dict and a in fim_dict]
        diffs.sort(key=lambda x: x[0])
        if diffs:
            first_diff = diffs[0][1]
            last_diff = diffs[-1][1]
            if first_diff > -diff_tol and last_diff <= diff_tol:
                energy_score = 1.0
            elif first_diff > -diff_tol:
                energy_score = 0.6
            elif last_diff <= diff_tol:
                energy_score = 0.4
            else:
                energy_score = 0.2
    else:
        # no common a; if FIM exists alongside FM at some a this can't happen. Give 0.
        energy_score = 0.0

    # Weighted combination
    weights = {
        'exist': 0.05,
        'fm_spin': 0.25,
        'fim_exist': 0.20,
        'fim_high': 0.20,
        'fim_no_low': 0.05,
        'energy': 0.25
    }
    total = (score_exist * weights['exist'] +
             fm_score * weights['fm_spin'] +
             fim_exist_score * weights['fim_exist'] +
             fim_high_score * weights['fim_high'] +
             fim_no_low_score * weights['fim_no_low'] +
             energy_score * weights['energy'])
    return min(total, 1.0)


_SCORERS = {
    's2': score_0,
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
