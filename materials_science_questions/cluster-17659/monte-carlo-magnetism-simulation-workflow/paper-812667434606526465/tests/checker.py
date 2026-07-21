import os
import json
import csv

# === author imports / helpers ===
import csv
import re
import io


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


# === block: score_0 (check id='phase_diagram') ===
def score_0(artifact, step, ctx):
    # artifact is parsed CSV: list of dicts
    if not isinstance(artifact, list) or not artifact:
        return 0.0

    rows = artifact

    # Find all boundary points (boundary_flag == 1)
    boundary_rows = []
    for r in rows:
        try:
            bf = int(r.get('boundary_flag', 0))
            if bf == 1:
                T_val = float(r['T'])
                H_val = float(r['H'])
                M_perp = float(r['M_perp'])
                M_z = float(r['M_z'])
                order = int(r['transition_order'])
                boundary_rows.append({'T': T_val, 'H': H_val, 'M_perp': M_perp, 'M_z': M_z, 'order': order})
        except (ValueError, KeyError, TypeError):
            continue

    if not boundary_rows:
        return 0.0

    # T_N(0): find row with H=0 (or closest to 0)
    h0_row = None
    min_abs_h = None
    for r in boundary_rows:
        h = r['H']
        if abs(h) < 1e-6:
            h0_row = r
            break
        if min_abs_h is None or abs(h) < min_abs_h:
            min_abs_h = abs(h)
            h0_row = r
    if h0_row is None:
        return 0.0
    T_N0 = h0_row['T']

    # T_star: highest T with transition_order == 1
    first_order_rows = [r for r in boundary_rows if r['order'] == 1]
    if first_order_rows:
        T_star = max(r['T'] for r in first_order_rows)
    else:
        T_star = None

    # score T_N0
    target = step['target']
    tol_tn = target['tol_TN']
    diff_tn = abs(T_N0 - target['T_N0'])
    score_tn = max(0.0, 1.0 - diff_tn / tol_tn)

    # score T_star
    if T_star is not None:
        tol_ts = target['tol_Tstar']
        diff_ts = abs(T_star - target['T_star'])
        score_ts = max(0.0, 1.0 - diff_ts / tol_ts)
    else:
        score_ts = 0.0

    # structural check: presence of both orders
    orders = set(r['order'] for r in boundary_rows)
    has_first = 1 in orders
    has_second = 2 in orders
    score_struct = 1.0 if (has_first and has_second) else 0.0

    score = 0.5 * score_tn + 0.3 * score_ts + 0.2 * score_struct
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='isentropes') ===
def score_1(artifact, step, ctx):
    # artifact is parsed CSV: list of dicts
    if not isinstance(artifact, list) or not artifact:
        return 0.0

    target_map = step['target']
    rows_by_S = {}
    for row in artifact:
        try:
            s_val = float(row['S'])
            s_key = round(s_val, 1)
            h_val = float(row['H'])
            t_val = float(row['T'])
            rows_by_S.setdefault(s_key, []).append((h_val, t_val))
        except (ValueError, KeyError, TypeError):
            continue

    scores = []
    # S=-3.0
    s_target_neg3 = target_map['S_neg3']
    if -3.0 in rows_by_S:
        entries = rows_by_S[-3.0]
        if entries:
            min_h_entry = min(entries, key=lambda x: x[0])
            T_h0 = min_h_entry[1]
            diff = abs(T_h0 - s_target_neg3['T_at_H0'])
            tol = s_target_neg3['tol']
            scores.append(max(0.0, 1.0 - diff / tol))
        else:
            scores.append(0.0)
    else:
        candidates = []
        for key, entries in rows_by_S.items():
            if abs(key + 3.0) < 0.1:
                for h, t in entries:
                    candidates.append((h, t))
        if candidates:
            min_h = min(candidates, key=lambda x: x[0])
            diff = abs(min_h[1] - s_target_neg3['T_at_H0'])
            tol = s_target_neg3['tol']
            scores.append(max(0.0, 1.0 - diff / tol))
        else:
            scores.append(0.0)

    # S=-1.4
    s_target_neg1_4 = target_map['S_neg1_4']
    if -1.4 in rows_by_S:
        entries = rows_by_S[-1.4]
        if entries:
            min_h_entry = min(entries, key=lambda x: x[0])
            T_h0 = min_h_entry[1]
            diff = abs(T_h0 - s_target_neg1_4['T_at_H0'])
            tol = s_target_neg1_4['tol']
            scores.append(max(0.0, 1.0 - diff / tol))
        else:
            scores.append(0.0)
    else:
        candidates = []
        for key, entries in rows_by_S.items():
            if abs(key + 1.4) < 0.1:
                for h, t in entries:
                    candidates.append((h, t))
        if candidates:
            min_h = min(candidates, key=lambda x: x[0])
            diff = abs(min_h[1] - s_target_neg1_4['T_at_H0'])
            tol = s_target_neg1_4['tol']
            scores.append(max(0.0, 1.0 - diff / tol))
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='growth_exponent') ===
def score_2(artifact, step, ctx):
    text = artifact.strip()
    try:
        n = float(text.split()[0])  # first token
        target = float(step['target'])
        tol = float(step['tolerance_abs'])
        diff = abs(n - target)
        score = max(0.0, 1.0 - diff / tol)
        return score
    except (ValueError, IndexError):
        return 0.0


_SCORERS = {
    'phase_diagram': score_0,
    'isentropes': score_1,
    'growth_exponent': score_2,
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
