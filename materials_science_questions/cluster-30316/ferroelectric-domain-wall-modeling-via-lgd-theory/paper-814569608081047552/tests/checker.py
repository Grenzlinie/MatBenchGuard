import os
import json
import csv

# === author imports / helpers ===
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
    def R(x, y):
        if y == 0.0:
            return 0.0
        c = math.cosh(4 * math.pi * y)
        cos_term = math.cos(2 * math.pi * x)
        log_arg = (c - cos_term) / (1.0 - cos_term)
        if log_arg <= 0:
            return 0.0
        term1 = math.log(log_arg)
        term2 = 8 * (math.pi * y) ** 2 * (c * cos_term - 1.0) / (c - cos_term) ** 2
        return term1 - term2

    expected = {}
    modes = ['h', 'sc', 'sa']
    d_over_D_vals = [0.3, 0.5, 0.7]
    D_over_H_vals = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    prefactor = math.sqrt(2.0) / math.pi
    for dods in d_over_D_vals:
        for Doh in D_over_H_vals:
            y = Doh / 2.0
            x1 = dods / 2.0
            x2 = x1 + 0.5
            x_half = 0.5
            R1 = R(x1, y)
            R2 = R(x2, y)
            Rhalf = R(x_half, y)
            expected[('h', dods, Doh)] = prefactor * (R1 + R2)
            expected[('sc', dods, Doh)] = prefactor * (R1 - Rhalf)
            expected[('sa', dods, Doh)] = prefactor * (R2 - Rhalf)
    return {'expected': expected, 'spec': spec}


# === block: score_0 (check id='force_constants') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    artifact_path = os.path.join('/app/outputs', 'force_constants.csv')
    if not os.path.exists(artifact_path):
        return 0.0

    try:
        reader = csv.DictReader(open(artifact_path))
        rows = list(reader)
    except Exception:
        return 0.0

    expected = ctx['expected']
    config = step['config']
    tol = config['absolute_tolerance']
    # row match
    correct = 0
    all_rows = 0
    for row in rows:
        try:
            mode = row['mode']
            dods = float(row['d_over_D'])
            Doh = float(row['D_over_H'])
            k_norm = float(row['k_norm'])
            key = (mode, dods, Doh)
            if key in expected:
                exp_val = expected[key]
                if abs(k_norm - exp_val) <= tol:
                    correct += 1
                all_rows += 1
        except (KeyError, ValueError):
            continue
    if all_rows == 0:
        return 0.0
    row_score = correct / all_rows

    # ordering check
    if config.get('enable_ordering_check', False):
        dods_list = [0.3, 0.5, 0.7]
        ordering_ok = 0
        total_dods = len(dods_list)
        for dods in dods_list:
            sc_vals = []
            sa_vals = []
            for r in rows:
                if r['mode'] == 'sc' and abs(float(r['d_over_D']) - dods) < 1e-9:
                    sc_vals.append(float(r['k_norm']))
                if r['mode'] == 'sa' and abs(float(r['d_over_D']) - dods) < 1e-9:
                    sa_vals.append(float(r['k_norm']))
            if sc_vals and sa_vals:
                sc_mean = sum(sc_vals) / len(sc_vals)
                sa_mean = sum(sa_vals) / len(sa_vals)
                if dods == 0.5:
                    if abs(sc_mean - sa_mean) <= tol:
                        ordering_ok += 1
                elif dods > 0.5:
                    if sc_mean < sa_mean - tol:
                        ordering_ok += 1
                else:
                    if sc_mean > sa_mean + tol:
                        ordering_ok += 1
        ordering_score = ordering_ok / total_dods
        # combine
        return 0.8 * row_score + 0.2 * ordering_score
    else:
        return row_score


# === block: score_1 (check id='dielectric_contribution') ===
def score_1(artifact, step, ctx):
    import csv
    import os

    artifact_path = os.path.join('/app/outputs', 'dielectric_contribution.csv')
    if not os.path.exists(artifact_path):
        return 0.0

    try:
        reader = csv.DictReader(open(artifact_path))
        rows = list(reader)
    except Exception:
        return 0.0

    gold = step['gold_values']
    rel_tol = step['relative_tolerance']

    scores = []
    for row in rows:
        try:
            h_norm_str = '{:.1f}'.format(float(row['H_norm']))
            val = float(row['delta_epsilon_norm'])
            if h_norm_str in gold:
                gold_val = gold[h_norm_str]
                rel_err = abs(val - gold_val) / gold_val
                if rel_err <= rel_tol:
                    score = 1.0
                else:
                    score = max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)
                scores.append(score)
        except (KeyError, ValueError):
            continue

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'force_constants': score_0,
    'dielectric_contribution': score_1,
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
