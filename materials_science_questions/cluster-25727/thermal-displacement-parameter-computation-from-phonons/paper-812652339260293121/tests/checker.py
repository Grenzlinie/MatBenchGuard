import os
import json
import csv

# === author imports / helpers ===
import math, csv, json, os


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
    filepath = os.path.join(outputs_dir, 'simon_fit.json')
    simon = None
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            simon = json.load(f)
    return {'agent_simon': simon}


# === block: score_0 (check id='melt_curve_shape') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) < 20:
        return 0.0
    for row in artifact:
        try:
            d = float(row['density_g_cm3'])
            t = float(row['temperature_K'])
            p = float(row['pressure_GPa'])
            if d <= 0 or p <= 0:
                return 0.0
        except (KeyError, ValueError):
            return 0.0
    return 1.0


# === block: score_1 (check id='melt_curve_self_consistency') ===
def score_1(artifact, step, ctx):
    agent_simon = ctx.get('agent_simon')
    if not agent_simon:
        return 0.0
    try:
        T0 = float(agent_simon['T0'])
        P0 = float(agent_simon['P0'])
        b = float(agent_simon['exponent'])
    except (KeyError, ValueError):
        return 0.0
    n = len(artifact)
    if n == 0:
        return 0.0
    good = 0
    for row in artifact:
        try:
            P = float(row['pressure_GPa'])
            T_agent = float(row['temperature_K'])
            if P <= 0:
                continue
            T_pred = T0 * (P / P0) ** b
            if T_pred <= 0:
                continue
            rel_err = abs(T_agent - T_pred) / T_pred
            if rel_err <= 0.05:
                good += 1
        except (KeyError, ValueError):
            pass
    proportion = good / n
    score = min(1.0, proportion / 0.8)
    return score


# === block: score_2 (check id='melt_curve_paper_curve_match') ===
def score_2(artifact, step, ctx):
    paper = step.get('paper_simon', {})
    T0 = float(paper.get('T0', 6279.0))
    P0 = float(paper.get('P0', 346.0))
    b = float(paper.get('b', 0.552))
    n = len(artifact)
    if n == 0:
        return 0.0
    good = 0
    for row in artifact:
        try:
            P = float(row['pressure_GPa'])
            T_agent = float(row['temperature_K'])
            if P <= 0:
                continue
            T_pred = T0 * (P / P0) ** b
            if T_pred <= 0:
                continue
            rel_err = abs(T_agent - T_pred) / T_pred
            if rel_err <= 0.05:
                good += 1
        except (KeyError, ValueError):
            pass
    proportion = good / n
    score = min(1.0, proportion / 0.8)
    return score


# === block: score_3 (check id='simon_fit_parameters') ===
def score_3(artifact, step, ctx):
    agent_simon = ctx.get('agent_simon')
    if not agent_simon:
        return 0.0
    try:
        T0_agent = float(agent_simon['T0'])
        exp_agent = float(agent_simon['exponent'])
    except (KeyError, ValueError):
        return 0.0
    paper = step.get('paper_simon', {})
    T0_target = float(paper.get('T0', 6279.0))
    exp_target = float(paper.get('exponent', 0.552))
    tol = float(step.get('tolerance_relative', 0.05))
    err_T0 = abs(T0_agent - T0_target) / T0_target
    if err_T0 <= tol:
        s_T0 = 1.0
    else:
        s_T0 = max(0.0, 1.0 - (err_T0 - tol) / (0.1 - tol))
    err_exp = abs(exp_agent - exp_target) / exp_target
    if err_exp <= tol:
        s_exp = 1.0
    else:
        s_exp = max(0.0, 1.0 - (err_exp - tol) / (0.1 - tol))
    return 0.5 * s_T0 + 0.5 * s_exp


_SCORERS = {
    'melt_curve_shape': score_0,
    'melt_curve_self_consistency': score_1,
    'melt_curve_paper_curve_match': score_2,
    'simon_fit_parameters': score_3,
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
