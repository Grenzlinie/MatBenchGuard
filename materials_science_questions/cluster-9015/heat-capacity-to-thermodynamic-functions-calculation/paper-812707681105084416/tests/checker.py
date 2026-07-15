import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict
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
    return {}


# === block: score_0 (check id='phase_stability') ===
def score_0(artifact, step, ctx):
    TARGET_TEMP = 1804.0
    TEMP_TOL = 20.0
    rows = artifact   # artifact is list of dicts loaded by framework
    # filter stoichiometric ratio 1:1 (n_B_n_N == 1.0)
    stoich_rows = []
    for r in rows:
        try:
            if float(r.get('n_B_n_N', 3)) == 1.0:
                stoich_rows.append(r)
        except:
            pass

    # Check for any w-BN presence anywhere
    any_wbn = any(r.get('stable_phase', '').strip() == 'w-BN' for r in rows)

    if not stoich_rows:
        return 0.0

    # Group by (P, n_Cl_n_H, n_He_n_N)
    groups = defaultdict(list)
    for r in stoich_rows:
        key = (round(float(r['P']), 0), round(float(r['n_Cl_n_H']), 6), round(float(r['n_He_n_N']), 6))
        groups[key].append((float(r['T']), r['stable_phase'].strip()))

    transition_temps = []
    for key, entries in groups.items():
        # sort by T
        entries.sort(key=lambda x: x[0])
        found = None
        for i in range(len(entries)-1):
            T1, ph1 = entries[i]
            T2, ph2 = entries[i+1]
            if ph1 == 'c-BN' and ph2 == 'h-BN':
                mid = (T1 + T2) / 2.0
                found = mid
                break
        if found is not None:
            transition_temps.append(found)

    if not transition_temps:
        return 0.0

    avg_transition = sum(transition_temps) / len(transition_temps)
    diff = abs(avg_transition - TARGET_TEMP)
    if diff <= TEMP_TOL:
        temp_score = 1.0
    else:
        temp_score = max(0.0, 1.0 - (diff - TEMP_TOL) / TEMP_TOL)

    # structural bonus: no w-BN anywhere
    struc_score = 0.0 if any_wbn else 1.0

    return 0.8 * temp_score + 0.2 * struc_score


# === block: score_1 (check id='gas_composition') ===
def score_1(artifact, step, ctx):
    data = artifact  # list of dicts
    ref_conditions = step.get('reference_data', {}).get('conditions', [])
    tol_abs = step.get('tolerance', {}).get('abs', 0.005)
    tol_rel = step.get('tolerance', {}).get('rel', 0.1)

    # Fix erroneous reference NH3 value for 1400 K, 101300 Pa (paper reports 1.3e-8, not 1.3e-9)
    for cond in ref_conditions:
        if cond.get('T') == 1400 and cond.get('P') == 101300:
            sp = cond.get('species', {})
            if 'NH3' in sp and sp['NH3'] == 1.3e-9:
                sp['NH3'] = 1.3e-8

    # Build lookup: (T, P, species) -> mole_fraction
    lookup = {}
    for row in data:
        try:
            T = round(float(row['T']), 0)
            P = round(float(row['P']), -1)  # round to nearest 10 Pa
            species = row['species'].strip()
            mf = float(row['mole_fraction'])
            lookup[(T, P, species)] = mf
        except:
            continue

    condition_scores = []
    for cond in ref_conditions:
        T = cond['T']
        P_ref = cond['P']
        P = round(float(P_ref), -1)
        species_ref = cond['species']
        total = 0
        count = 0
        for sp, ref_val in species_ref.items():
            if ref_val is None:
                continue
            agent_val = lookup.get((T, P, sp), 0.0)
            abs_diff = abs(agent_val - ref_val)
            rel_diff = abs_diff / ref_val if ref_val != 0 else abs_diff
            allowed = max(tol_abs, tol_rel * ref_val)
            if abs_diff <= allowed or rel_diff <= tol_rel:
                total += 1.0
            count += 1
        if count > 0:
            condition_scores.append(total / count)
    if not condition_scores:
        return 0.0
    # average over conditions
    return sum(condition_scores) / len(condition_scores)


_SCORERS = {
    'phase_stability': score_0,
    'gas_composition': score_1,
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
