import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
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
    # Extract gold values from grading_spec steps for use in scorers
    ctx = {}
    for step in spec.get('steps', []):
        sid = step.get('id')
        if sid == 'entropy':
            ctx['gold_entropy'] = step.get('gold_entropy', [])
            ctx['tol_rel_entropy'] = step.get('tolerance_rel', 0.15)
        elif sid == 'edwards_T':
            ctx['gold_T_edw'] = step.get('gold_T_edw', 0.25)
            ctx['tol_abs_T'] = step.get('tolerance_abs', 0.05)
        elif sid == 'dynamic_T':
            ctx['gold_T_dyn'] = step.get('gold_T_dyn', 0.25)
            ctx['tol_abs_T2'] = step.get('tolerance_abs', 0.05)
        elif sid == 'edwards_structure':
            ctx['gold_edw_structure'] = step.get('gold_edw_structure', [])
            ctx['tol_mae_edw'] = step.get('tolerance_mae', 0.005)
        elif sid == 'dynamic_structure':
            ctx['gold_dyn_structure'] = step.get('gold_dyn_structure', [])
            ctx['tol_mae_dyn'] = step.get('tolerance_mae', 0.005)
        else:
            pass
    return ctx


# === block: score_0 (check id='entropy') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts with keys density, s_edw
    gold_table = step.get('gold_entropy', [])
    tol_rel = step.get('tolerance_rel', 0.25)
    tol_abs = step.get('tolerance_abs', 0.04)   # floor to avoid unrealistically tight window at low entropy
    if not gold_table or not artifact:
        return 0.0
    scores = []
    for rho_g, s_gold in gold_table:
        best_s = None
        min_diff = float('inf')
        for row in artifact:
            try:
                rho_a = float(row.get('density', 0))
                s_a = float(row.get('s_edw', 0))
            except (ValueError, TypeError):
                continue
            diff = abs(rho_a - rho_g)
            if diff < min_diff:
                min_diff = diff
                best_s = s_a
        if best_s is not None:
            error = abs(best_s - s_gold)
            allowed = max(tol_rel * abs(s_gold), tol_abs)
            if error <= allowed:
                score_i = 1.0
            else:
                score_i = max(0.0, 2.0 - error / allowed)
            scores.append(score_i)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='edwards_T') ===
def score_1(artifact, step, ctx):
    # artifact is dict with key T_edw
    gold_T = step.get('gold_T_edw', 0.25)
    tol_abs = step.get('tolerance_abs', 0.05)
    if not isinstance(artifact, dict):
        return 0.0
    try:
        T_agent = float(artifact.get('T_edw', 0))
    except (ValueError, TypeError):
        return 0.0
    err = abs(T_agent - gold_T)
    if err <= tol_abs:
        return 1.0
    score = max(0.0, 1.0 - err / (tol_abs * 2))
    return score


# === block: score_2 (check id='dynamic_T') ===
def score_2(artifact, step, ctx):
    # artifact is dict with key T_dyn
    gold_T = step.get('gold_T_dyn', 0.25)
    tol_abs = step.get('tolerance_abs', 0.05)
    if not isinstance(artifact, dict):
        return 0.0
    try:
        T_agent = float(artifact.get('T_dyn', 0))
    except (ValueError, TypeError):
        return 0.0
    err = abs(T_agent - gold_T)
    if err <= tol_abs:
        return 1.0
    score = max(0.0, 1.0 - err / (tol_abs * 2))
    return score


# === block: score_3 (check id='edwards_structure') ===
def score_3(artifact, step, ctx):
    # artifact is list of dicts with keys r, g_edw
    gold_struct = step.get('gold_edw_structure', [])
    tol_mae = step.get('tolerance_mae', 0.005)
    if not gold_struct or not artifact:
        return 0.0
    errors = []
    for r_target, g_gold in gold_struct:
        g_agent = None
        for row in artifact:
            try:
                r_a = int(row.get('r', -1))
                if r_a == r_target:
                    g_agent = float(row.get('g_edw', 0))
                    break
            except (ValueError, TypeError):
                continue
        if g_agent is not None:
            errors.append(abs(g_agent - g_gold))
    if not errors:
        return 0.0
    mae = sum(errors) / len(errors)
    return max(0.0, 1.0 - mae / tol_mae)


# === block: score_4 (check id='dynamic_structure') ===
def score_4(artifact, step, ctx):
    # artifact is list of dicts with keys r, g_dyn
    gold_struct = step.get('gold_dyn_structure', [])
    tol_mae = step.get('tolerance_mae', 0.005)
    if not gold_struct or not artifact:
        return 0.0
    errors = []
    for r_target, g_gold in gold_struct:
        g_agent = None
        for row in artifact:
            try:
                r_a = int(row.get('r', -1))
                if r_a == r_target:
                    g_agent = float(row.get('g_dyn', 0))
                    break
            except (ValueError, TypeError):
                continue
        if g_agent is not None:
            errors.append(abs(g_agent - g_gold))
    if not errors:
        return 0.0
    mae = sum(errors) / len(errors)
    return max(0.0, 1.0 - mae / tol_mae)


_SCORERS = {
    'entropy': score_0,
    'edwards_T': score_1,
    'dynamic_T': score_2,
    'edwards_structure': score_3,
    'dynamic_structure': score_4,
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
