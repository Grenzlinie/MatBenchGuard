import os
import json
import csv

# === author imports / helpers ===
import math, csv, os
from collections import defaultdict


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
    steps = spec.get("steps", spec.get("checks", [])) or []
    gold_by_output = {}
    for step in steps:
        fname = step["output_file"]
        if "gold" in step:
            gold_by_output[fname] = step["gold"]
    return {"gold_by_output": gold_by_output}


# === block: score_0 (check id='check_A_orbit_lattice') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    rows = artifact
    if not rows:
        return 0.0
    gold = step.get('gold', {})
    A_R = gold.get('A_R', 92.57)
    points_gold = gold.get('points', [])
    tol_abs = gold.get('tolerance_abs', 0.5)
    tol_rel = gold.get('tolerance_rel', 0.10)
    # load phonon_integrals.csv
    evidence_path = os.path.join('/app/outputs', 'phonon_integrals.csv')
    if not os.path.exists(evidence_path):
        return 0.0
    with open(evidence_path, newline='') as f:
        evidence = list(csv.DictReader(f))
    if not evidence:
        return 0.0
    # build dict from evidence by T
    evidence_dict = {}
    for row in evidence:
        try:
            T = float(row['T'])
            F_ac = float(row.get('F_ac', 0))
            F_op = float(row.get('F_op', 0))
            evidence_dict[T] = (F_ac, F_op)
        except:
            continue
    # build submitted dict from artifact
    submitted_dict = {}
    for row in rows:
        try:
            T = float(row['T'])
            A_th = float(row['A_theory'])
            submitted_dict[T] = A_th
        except:
            continue
    if not submitted_dict:
        return 0.0
    # scoring
    n = len(points_gold)
    if n == 0:
        return 0.0
    point_scores = []
    for pg in points_gold:
        T = pg['T']
        D = pg['D']
        A_gold = pg['A_gold']
        ev = evidence_dict.get(T)
        if ev is None:
            point_scores.append(0.0)
            continue
        F_ac, F_op = ev
        # recompute A from evidence: A = A_R * (1 - D*F_ac + F_op)
        try:
            A_recomp = A_R * (1.0 - D * F_ac + F_op)
        except:
            point_scores.append(0.0)
            continue
        # tolerance check vs gold
        diff = abs(A_recomp - A_gold)
        if A_gold != 0 and abs(A_gold) >= 1.0:
            ok_gold = diff <= tol_rel * abs(A_gold)
        else:
            ok_gold = diff <= tol_abs
        # consistency check: submitted value vs recomputed
        A_sub = submitted_dict.get(T)
        if A_sub is not None:
            cons_diff = abs(A_sub - A_recomp)
            ok_cons = cons_diff <= 1e-3
        else:
            ok_cons = False
        # combine
        point_score = 0.5 * (1.0 if ok_gold else 0.0) + 0.5 * (1.0 if ok_cons else 0.0)
        point_scores.append(point_score)
    mean_point = sum(point_scores) / n
    # monotonic decreasing
    sorted_T = sorted(submitted_dict.keys())
    if len(sorted_T) > 1:
        decreasing = True
        prev = submitted_dict[sorted_T[0]]
        for t in sorted_T[1:]:
            curr = submitted_dict[t]
            if curr > prev + 1e-6:
                decreasing = False
                break
            prev = curr
    else:
        decreasing = False
    mono_score = 1.0 if decreasing else 0.0
    final = 0.8 * mean_point + 0.2 * mono_score
    return max(0.0, min(1.0, final))


# === block: score_1 (check id='check_A_covalency') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    rows = artifact
    if not rows:
        return 0.0
    gold = step.get('gold', {})
    points_gold = gold.get('points', [])
    tol_abs = gold.get('tolerance_abs', 0.5)
    tol_rel = gold.get('tolerance_rel', 0.10)
    submitted_dict = {}
    for row in rows:
        try:
            T = float(row['T'])
            val = float(row['Delta_A_cov'])
            submitted_dict[T] = val
        except:
            continue
    if not submitted_dict:
        return 0.0
    n = len(points_gold)
    if n == 0:
        return 0.0
    point_scores = []
    for pg in points_gold:
        T = pg['T']
        gold_val = pg['Delta_A_cov_gold']
        sub_val = submitted_dict.get(T)
        if sub_val is None:
            point_scores.append(0.0)
            continue
        diff = abs(sub_val - gold_val)
        if gold_val != 0 and abs(gold_val) >= 1.0:
            ok = diff <= tol_rel * abs(gold_val)
        else:
            ok = diff <= tol_abs
        point_scores.append(1.0 if ok else 0.0)
    mean_point = sum(point_scores) / n
    # monotonic increasing
    sorted_T = sorted(submitted_dict.keys())
    if len(sorted_T) > 1:
        increasing = True
        prev = submitted_dict[sorted_T[0]]
        for t in sorted_T[1:]:
            curr = submitted_dict[t]
            if curr < prev - 1e-6:
                increasing = False
                break
            prev = curr
    else:
        increasing = False
    mono_score = 1.0 if increasing else 0.0
    final = 0.8 * mean_point + 0.2 * mono_score
    return max(0.0, min(1.0, final))


# === block: score_2 (check id='check_b2_vibronic') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    rows = artifact
    if not rows:
        return 0.0
    gold = step.get('gold', {})
    points_gold = gold.get('points', [])
    tol_abs = gold.get('tolerance_abs', 0.5)
    tol_rel = gold.get('tolerance_rel', 0.10)
    submitted_dict = {}
    for row in rows:
        try:
            T = float(row['T'])
            val = float(row['b2_vibronic_theory'])
            submitted_dict[T] = val
        except:
            continue
    if not submitted_dict:
        return 0.0
    n = len(points_gold)
    if n == 0:
        return 0.0
    point_scores = []
    for pg in points_gold:
        T = pg['T']
        gold_val = pg['b2_gold']
        sub_val = submitted_dict.get(T)
        if sub_val is None:
            point_scores.append(0.0)
            continue
        diff = abs(sub_val - gold_val)
        if gold_val != 0 and abs(gold_val) >= 1.0:
            ok = diff <= tol_rel * abs(gold_val)
        else:
            ok = diff <= tol_abs
        point_scores.append(1.0 if ok else 0.0)
    mean_point = sum(point_scores) / n
    # monotonic increasing and sign crossing
    sorted_T = sorted(submitted_dict.keys())
    if len(sorted_T) > 1:
        values = [submitted_dict[t] for t in sorted_T]
        increasing = all(values[i] <= values[i+1] + 1e-6 for i in range(len(values)-1))
        neg_present = any(v < -1e-6 for v in values)
        pos_present = any(v > 1e-6 for v in values)
        sign_ok = neg_present and pos_present
    else:
        increasing = False
        sign_ok = False
    structural_score = 1.0 if (increasing and sign_ok) else 0.0
    final = 0.8 * mean_point + 0.2 * structural_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'check_A_orbit_lattice': score_0,
    'check_A_covalency': score_1,
    'check_b2_vibronic': score_2,
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
