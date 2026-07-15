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


# === block: score_0 (check id='step_1_zero_field') ===
def score_0(artifact, step, ctx):
    artifact_rows = list(artifact)
    if not artifact_rows:
        return 0.0
    try:
        for r in artifact_rows:
            r['separation_angstrom'] = float(r['separation_angstrom'])
            r['dipole_D'] = float(r['dipole_D'])
    except (ValueError, KeyError):
        return 0.0

    gold_rows = step['gold']['rows']
    tol = step['gold']['tolerance_dipole']

    # Build a lookup key -> value
    key_fn = lambda r: (r['X'], r['separation_angstrom'])
    gold_map = {key_fn(g): g['dipole_D'] for g in gold_rows}

    # Numeric accuracy: for each agent row, if key in gold, check within tolerance
    num_correct = 0
    num_total = len(gold_rows)
    agent_keys_seen = set()
    for row in artifact_rows:
        k = key_fn(row)
        if k in gold_map:
            agent_keys_seen.add(k)
            if abs(row['dipole_D'] - gold_map[k]) <= tol:
                num_correct += 1
    numeric_score = num_correct / num_total if num_total > 0 else 0.0

    # Trend checks
    trend_checks_passed = 0
    trend_total = 0

    # Sign: H positive, F negative, Br negative
    def sign(val):
        if val > 1e-9:
            return 1
        elif val < -1e-9:
            return -1
        else:
            return 0

    for X in ['H', 'F', 'Br']:
        for sep in [7.81, 11.7]:
            k = (X, sep)
            if k in agent_keys_seen:
                # find the row
                row = next((r for r in artifact_rows if key_fn(r) == k), None)
                if row:
                    trend_total += 1
                    val = row['dipole_D']
                    if X == 'H' and sign(val) == 1:
                        trend_checks_passed += 1
                    if X in ('F', 'Br') and sign(val) == -1:
                        trend_checks_passed += 1
                    # Check spacing dependence: net dipole magnitude is smaller at smaller spacing
                    if sep == 7.81:
                        k_large = (X, 11.7)
                        if k_large in agent_keys_seen:
                            row_large = next((r for r in artifact_rows if key_fn(r) == k_large), None)
                            if row_large:
                                trend_total += 1
                                if abs(val) < abs(row_large['dipole_D']):
                                    trend_checks_passed += 1

    # Ordering: |Br| < |F| for both spacings
    for sep in [7.81, 11.7]:
        k_Br = ('Br', sep)
        k_F  = ('F', sep)
        if k_Br in agent_keys_seen and k_F in agent_keys_seen:
            trend_total += 1
            val_Br = next(r['dipole_D'] for r in artifact_rows if key_fn(r) == k_Br)
            val_F  = next(r['dipole_D'] for r in artifact_rows if key_fn(r) == k_F)
            if abs(val_Br) < abs(val_F):
                trend_checks_passed += 1

    trend_score = trend_checks_passed / trend_total if trend_total > 0 else 0.0

    return 0.5 * numeric_score + 0.5 * trend_score


# === block: score_1 (check id='step_2_field_dependence') ===
def score_1(artifact, step, ctx):
    artifact_rows = list(artifact)
    if not artifact_rows:
        return 0.0
    try:
        for r in artifact_rows:
            r['separation_angstrom'] = float(r['separation_angstrom'])
            r['field_V_Ang'] = float(r['field_V_Ang'])
            r['dipole_D'] = float(r['dipole_D'])
            # energy_gap_eV may be empty string; convert to float or None
            gap_str = r.get('energy_gap_eV', '')
            r['energy_gap_eV'] = float(gap_str) if gap_str != '' else None
    except (ValueError, KeyError):
        return 0.0

    gold_rows = step['gold']['rows']
    tol_dipole = step['gold']['tolerance_dipole']
    tol_gap = step['gold']['tolerance_gap']

    # Build gold map keyed by (X, sep, field)
    key_fn = lambda r: (r['X'], r['separation_angstrom'], r['field_V_Ang'])
    gold_map = {key_fn(g): g for g in gold_rows}

    # Numeric accuracy: check dipole for all, gap for those with gold value non-null
    num_correct = 0
    num_dipole_checked = 0
    num_gap_checked = 0
    for row in artifact_rows:
        k = key_fn(row)
        if k not in gold_map:
            continue
        gold = gold_map[k]
        num_dipole_checked += 1
        if abs(row['dipole_D'] - gold['dipole_D']) <= tol_dipole:
            num_correct += 1
        # gap check only when gold has a non-null energy_gap_eV (i.e., a=7.81)
        if gold['energy_gap_eV'] is not None:
            num_gap_checked += 1
            agent_gap = row['energy_gap_eV']
            if agent_gap is not None and abs(agent_gap - gold['energy_gap_eV']) <= tol_gap:
                num_correct += 1  # count gap correct separately; we'll combine later
            # if agent_gap missing (None), no correct for that gap
        # else optional field; ignore

    # For dipoles we have num_dipole_checked rows, for gaps num_gap_checked rows
    # Avoid divide by zero
    num_possible = num_dipole_checked + num_gap_checked
    if num_possible == 0:
        numeric_score = 0.0
    else:
        numeric_score = num_correct / num_possible

    # Trend checks: monotonic decrease with field for each X, spacing series
    # Build series: group by (X, sep), sort by field, check monotonicity for dipoles and for gaps where applicable
    from collections import defaultdict
    series = defaultdict(list)
    for row in artifact_rows:
        k = (row['X'], row['separation_angstrom'])
        series[k].append(row)

    # Sort each series by field_V_Ang
    for k in series:
        series[k].sort(key=lambda r: r['field_V_Ang'])

    trend_total = 0
    trend_passed = 0

    for (X, sep), rows in series.items():
        if len(rows) < 2:
            continue
        # dipole monotonic decreasing (each next <= previous)
        dipoles = [r['dipole_D'] for r in rows]
        trend_total += 1
        if all(dipoles[i+1] <= dipoles[i] + 1e-6 for i in range(len(dipoles)-1)):
            trend_passed += 1
    
        # gap monotonic decreasing for a=7.81 (only those rows that have gap)
        if sep == 7.81:
            gaps = [r['energy_gap_eV'] for r in rows if r['energy_gap_eV'] is not None]
            if len(gaps) >= 2:
                trend_total += 1
                if all(gaps[i+1] <= gaps[i] + 1e-6 for i in range(len(gaps)-1)):
                    trend_passed += 1

    trend_score = trend_passed / trend_total if trend_total > 0 else 0.0

    return 0.5 * numeric_score + 0.5 * trend_score


_SCORERS = {
    'step_1_zero_field': score_0,
    'step_2_field_dependence': score_1,
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
