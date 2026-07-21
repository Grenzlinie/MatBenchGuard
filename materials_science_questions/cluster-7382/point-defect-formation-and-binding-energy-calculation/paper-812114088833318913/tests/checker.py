import os
import json
import csv

# === author imports / helpers ===
import math
import json


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
    def bisect_find_alpha(k, x_liq):
        def f(x_val, k_):
            return (1+x_val)*math.exp(-x_val) - (1+k_*x_val)*math.exp(-k_*x_val)
        target = f(x_liq, k)
        lo, hi = 1e-6, 0.5
        for _ in range(80):
            mid = (lo+hi)/2
            if f(12*mid, k) > target:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2

    inputs = spec['steps'][0]['config']['inputs']
    Tm, dH, eps0 = inputs['Tm_over_D'], inputs['dH_over_D'], inputs['eps0_over_D']
    ks = spec['steps'][0]['config']['ks']
    expected = {}
    for k in ks:
        x_liq = math.log(k)/(k-1)
        alpha = bisect_find_alpha(k, x_liq)
        n_over_v = x_liq / alpha
        V = eps0 - (dH/Tm) * n_over_v
        denom = math.exp(-x_liq) - math.exp(-k*x_liq)
        C = V / denom
        a_val = math.exp(V/Tm - 1)
        g_val = 1 + a_val / n_over_v
        f_x = (1+x_liq)*math.exp(-x_liq) - (1+k*x_liq)*math.exp(-k*x_liq)
        F_x_liq = C * f_x
        x_min = 12*alpha
        expected[k] = {
            'x_liq': x_liq, 'F_x_liq': F_x_liq, 'x_min': x_min,
            'alpha': alpha, 'n_over_v_liq': n_over_v,
            'V_v_liq_n': V, 'a': a_val, 'g_v_liq': g_val, 'C': C
        }
    return {'expected': expected, 'step_config': spec['steps'][0]['config']}


# === block: score_0 (check id='step_02_vacancy_params') ===
def score_0(artifact, step, ctx):
    gold_table = {
        2: {"x_liq": 0.693, "F_x_liq": 0.250, "x_min": 2.48, "alpha": 0.207, "n_over_v_liq": 3.35, "V_v_liq_n": 3.07, "a": 102, "g_v_liq": 340, "C": 12.3},
        3: {"x_liq": 0.549, "F_x_liq": 0.385, "x_min": 2.02, "alpha": 0.168, "n_over_v_liq": 3.27, "V_v_liq_n": 3.14, "a": 89, "g_v_liq": 290, "C": 8.2},
        6: {"x_liq": 0.358, "F_x_liq": 0.583, "x_min": 1.42, "alpha": 0.118, "n_over_v_liq": 3.03, "V_v_liq_n": 3.38, "a": 60, "g_v_liq": 180, "C": 5.8},
        10: {"x_liq": 0.256, "F_x_liq": 0.697, "x_min": 1.10, "alpha": 0.0921, "n_over_v_liq": 2.78, "V_v_liq_n": 3.63, "a": 39, "g_v_liq": 110, "C": 5.2}
    }

    config = ctx.get('step_config', {})
    ks = config.get('ks', [2, 3, 6, 10])
    fields = config.get('fields', ["x_liq", "F_x_liq", "x_min", "alpha", "n_over_v_liq", "V_v_liq_n", "a", "g_v_liq", "C"])
    tol_rel = config.get('tolerance_relative', 0.01)
    tol_abs = config.get('tolerance_absolute', 0.001)

    rows = {}
    for entry in artifact:
        rows[entry.get('k')] = entry

    score_sum = 0.0
    count = 0
    for k in ks:
        if k not in rows or k not in gold_table:
            continue
        row = rows[k]
        gold = gold_table[k]
        for field in fields:
            if field not in row or field not in gold:
                continue
            val = row[field]
            exp = gold[field]
            if not isinstance(val, (int, float)) or not isinstance(exp, (int, float)):
                continue
            if exp == 0:
                err = abs(val) if val != 0 else 0
            else:
                err = abs(val - exp) / max(abs(exp), 1e-12)
            if err <= tol_rel or abs(val - exp) <= tol_abs:
                score_sum += 1.0
            count += 1
    if count == 0:
        return 0.0
    return score_sum / count


_SCORERS = {
    'step_02_vacancy_params': score_0,
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
