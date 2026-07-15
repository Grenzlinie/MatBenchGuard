import os
import json
import csv

# === author imports / helpers ===
import csv
import math

def linear_fit(x_vals, y_vals):
    n = len(x_vals)
    if n < 2:
        return None, None
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xx = sum(x*x for x in x_vals)
    sum_xy = sum(x*y for x,y in zip(x_vals, y_vals))
    denom = n * sum_xx - sum_x * sum_x
    if denom == 0:
        return None, None
    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept


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


# === block: score_0 (check id='step1_pure_relaxation') ===
def score_0(artifact, step, ctx):
    def linear_fit(x_vals, y_vals):
        n = len(x_vals)
        if n < 2:
            return None, None
        sum_x = sum(x_vals)
        sum_y = sum(y_vals)
        sum_xx = sum(x*x for x in x_vals)
        sum_xy = sum(x*y for x,y in zip(x_vals, y_vals))
        denom = n * sum_xx - sum_x * sum_x
        if denom == 0:
            return None, None
        slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y - slope * sum_x) / n
        return slope, intercept

    globals()['linear_fit'] = linear_fit

    ref = step.get('reference', {})
    tol = step.get('tolerances', {})
    if not isinstance(artifact, dict):
        return 0.0

    # helper to check a single parameter
    def within_tol(val, ref_val, abs_tol):
        try:
            return abs(float(val) - float(ref_val)) <= abs_tol
        except (ValueError, TypeError):
            return False

    checks = []
    if 'M' in artifact and 'T' in artifact:
        m = artifact['M']
        t = artifact['T']
        ref_m = ref.get('M', {})
        ref_t = ref.get('T', {})
        # M phase
        if isinstance(m, dict):
            checks.append(within_tol(m.get('a'), ref_m.get('a'), tol.get('a', 0.06)))
            checks.append(within_tol(m.get('b_a'), ref_m.get('b_a'), tol.get('b_a', 0.01)))
            checks.append(within_tol(m.get('c_a'), ref_m.get('c_a'), tol.get('c_a', 0.01)))
            checks.append(within_tol(m.get('beta_deg'), ref_m.get('beta_deg'), tol.get('beta_deg', 0.8)))
            pos = m.get('positions', {})
            ref_pos = ref_m.get('positions', {})
            for atom in ['Zr','OI','OII']:
                atom_coord = pos.get(atom)
                ref_coord = ref_pos.get(atom)
                if isinstance(atom_coord, list) and isinstance(ref_coord, list) and len(atom_coord) == 3 and len(ref_coord) == 3:
                    for i in range(3):
                        checks.append(within_tol(atom_coord[i], ref_coord[i], tol.get('coord', 0.03)))
                else:
                    checks.extend([False]*3)
        else:
            checks.extend([False]*13)
        # T phase
        if isinstance(t, dict):
            checks.append(within_tol(t.get('a'), ref_t.get('a'), tol.get('a', 0.06)))
            checks.append(within_tol(t.get('c_a'), ref_t.get('c_a'), tol.get('c_a', 0.01)))
            checks.append(within_tol(t.get('dz'), ref_t.get('dz'), tol.get('dz', 0.01)))
        else:
            checks.extend([False]*3)
        if not checks:
            return 0.0
        score = sum(1 for c in checks if c) / len(checks)
        return score
    else:
        return 0.0


# === block: score_1 (check id='step3_energy_differences') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 5:
        return 0.0
    # required columns
    req_cols = [step.get('doping_column','doping_concentration'),
                step.get('m_column','E_M'),
                step.get('e_t_column','E_T'),
                step.get('delta_e_column','delta_E')]
    cols = artifact[0].keys()
    for col in req_cols:
        if col not in cols:
            return 0.0
    # parse rows
    x_vals = []
    # we need delta_E; if present use it, else compute from E_M - E_T
    has_delta = step.get('delta_e_column','delta_E') in cols
    has_em = step.get('e_m_column','E_M') in cols
    has_et = step.get('e_t_column','E_T') in cols
    if not has_delta and (not has_em or not has_et):
        return 0.0
    for row in artifact:
        try:
            x = float(row[step.get('doping_column','doping_concentration')])
            if has_delta:
                y = float(row[step.get('delta_e_column','delta_E')])
            else:
                y = float(row[step.get('e_m_column','E_M')]) - float(row[step.get('e_t_column','E_T')])
            x_vals.append((x, y))
        except (ValueError, KeyError):
            continue
    if len(x_vals) < 3:
        return 0.0
    xs = [p[0] for p in x_vals]
    ys = [p[1] for p in x_vals]
    slope, intercept = linear_fit(xs, ys)
    if slope is None or abs(slope) < 1e-9:
        return 0.0
    # corrected delta_E zero crossing: corrected_line = slope*x + 0.063, find x such that =0 -> x = -0.063 / slope
    try:
        offset = intercept - step.get('experimental_offset', 0.063)
        x_crit = -step.get('experimental_offset', 0.063) / slope
    except ZeroDivisionError:
        return 0.0
    target = step.get('target', 7.5)
    tol = step.get('tolerance', 1.5)
    diff = abs(x_crit - target)
    if diff <= tol:
        return 1.0
    # linear decay to 0 at diff=6.0
    if diff <= 6.0:
        return max(0.0, 1.0 - (diff - tol) / 4.5)
    return 0.0


_SCORERS = {
    'step1_pure_relaxation': score_0,
    'step3_energy_differences': score_1,
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
