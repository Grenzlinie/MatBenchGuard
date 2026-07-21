import os
import json
import csv

# === author imports / helpers ===
import math
import os


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
    params = spec['gold_parameters']
    a = params['a']
    n = params['n']
    D = params['D']
    r = params['r']
    h = params['h']
    d = params['d']
    D_star = params['D_star']
    n_D = params['n_D']
    eta = params['eta']
    sigma = params['sigma']

    # compute expected values
    v = D * a**2 * h * n / r
    t_SD = h**2 / (6 * D)
    V_strength = sigma * d**2 / (D_star * eta)
    L_star = 1.0 / (a**2 * n)    # a*(a^{-3}/n) = 1/(a^2 n)
    L_radial = math.sqrt(D * t_SD)
    L_dstar = d * (D_star / a)**1.5 / math.sqrt(32 * n_D)

    ctx = {}
    ctx['gold'] = {
        'step_v': v,
        'step_t_SD': t_SD,
        'step_V_strength': V_strength,
        'step_L_star': L_star,
        'step_L_radial': L_radial,
        'step_L_dstar': L_dstar
    }
    return ctx


# === block: score_0 (check id='step_v') ===
def score_0(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_v']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


# === block: score_1 (check id='step_t_SD') ===
def score_1(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_t_SD']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


# === block: score_2 (check id='step_V_strength') ===
def score_2(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_V_strength']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


# === block: score_3 (check id='step_L_star') ===
def score_3(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_L_star']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


# === block: score_4 (check id='step_L_radial') ===
def score_4(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_L_radial']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


# === block: score_5 (check id='step_L_dstar') ===
def score_5(artifact, step, ctx):
    val = float(artifact.strip())
    gold = ctx['gold']['step_L_dstar']
    rel_tol = step.get('tolerance_rel', 1e-6)
    abs_tol = step.get('tolerance_abs', 1e-15)
    max_denom = max(1.0, abs(gold))
    err = abs(val - gold)
    return 1.0 if err <= max_denom * rel_tol + abs_tol else 0.0


_SCORERS = {
    'step_v': score_0,
    'step_t_SD': score_1,
    'step_V_strength': score_2,
    'step_L_star': score_3,
    'step_L_radial': score_4,
    'step_L_dstar': score_5,
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
