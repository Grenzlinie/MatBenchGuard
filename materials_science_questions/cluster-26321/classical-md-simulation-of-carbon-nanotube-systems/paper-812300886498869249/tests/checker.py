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
    gold_coeffs = {
        "50K": {"a": 59.22, "b": 0.17, "c": -8.44},
        "300K": {"a": 65.36, "b": 0.63, "c": -8.39},
        "600K": {"a": 67.98, "b": 1.02, "c": -8.32},
        "900K": {"a": 74.22, "b": 1.52, "c": -8.26}
    }
    gold_epsilon0 = {
        "(10,10)": {"50K": -0.0029, "300K": -0.0096, "600K": -0.0150, "900K": -0.0204},
        "(8,8)": {"50K": -0.0036, "300K": -0.009, "600K": -0.0154, "900K": -0.0194},
        "(12,12)": {"50K": -0.0050, "300K": -0.0101, "600K": -0.0156, "900K": -0.0181},
        "(17,0)": {"50K": -0.0073, "300K": -0.0150, "600K": -0.0179, "900K": -0.0232}
    }
    return {"gold_coeffs": gold_coeffs, "gold_epsilon0": gold_epsilon0}


# === block: score_0 (check id='table_data') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold_coeffs = ctx['gold_coeffs']
    gold_eps = ctx['gold_epsilon0']
    temps = ["50K", "300K", "600K", "900K"]

    # 1) (10,10) coefficients relative tolerance 10%
    coeff_pass = 0
    coeff_total = 12
    for t in temps:
        for p in ["a", "b", "c"]:
            val = data.get("(10,10)", {}).get(t, {}).get(p)
            gold = gold_coeffs[t][p]
            if val is not None:
                if gold != 0:
                    rel_err = abs(val - gold) / abs(gold)
                else:
                    rel_err = abs(val)
                if rel_err <= 0.10:
                    coeff_pass += 1
    score_coeff = coeff_pass / coeff_total if coeff_total else 0.0

    # 2) epsilon0 for (10,10) derived consistency (abs tol 0.001)
    eps10_pass = 0
    for t in temps:
        a_val = data.get("(10,10)", {}).get(t, {}).get("a")
        b_val = data.get("(10,10)", {}).get(t, {}).get("b")
        if a_val is None or b_val is None or a_val == 0:
            continue
        eps_calc = -b_val / a_val
        eps_gold = gold_eps["(10,10)"][t]
        if abs(eps_calc - eps_gold) <= 0.001:
            eps10_pass += 1
    score_eps10 = eps10_pass / 4

    # 3) epsilon0 for other tubes (abs tol 0.001)
    other_tubes = ["(8,8)", "(12,12)", "(17,0)"]
    eps_other_pass = 0
    eps_other_total = 3 * 4
    for tube in other_tubes:
        for t in temps:
            val = data.get(tube, {}).get(t, {}).get("epsilon0")
            if val is not None:
                if abs(val - gold_eps[tube][t]) <= 0.001:
                    eps_other_pass += 1
    score_eps_other = eps_other_pass / eps_other_total if eps_other_total else 0.0

    # 4) monotonic trend: epsilon0 must decrease (more negative) as T increases
    def get_eps_series(tube):
        if tube == "(10,10)":
            series = []
            for t in temps:
                a_val = data.get("(10,10)", {}).get(t, {}).get("a")
                b_val = data.get("(10,10)", {}).get(t, {}).get("b")
                if a_val is None or b_val is None or a_val == 0:
                    return None
                series.append(-b_val / a_val)
            return series
        else:
            series = []
            for t in temps:
                val = data.get(tube, {}).get(t, {}).get("epsilon0")
                if val is None:
                    return None
                series.append(val)
            return series

    tubes_all = ["(10,10)", "(8,8)", "(12,12)", "(17,0)"]
    trend_pass = 0
    for tube in tubes_all:
        series = get_eps_series(tube)
        if series is None:
            continue
        if all(series[i] > series[i+1] for i in range(len(series)-1)):
            trend_pass += 1
    score_trend = trend_pass / len(tubes_all) if tubes_all else 0.0

    w_coeff = 0.5
    w_eps10 = 0.1
    w_eps_other = 0.3
    w_trend = 0.1

    total_score = w_coeff * score_coeff + w_eps10 * score_eps10 + w_eps_other * score_eps_other + w_trend * score_trend
    return max(0.0, min(1.0, total_score))


_SCORERS = {
    'table_data': score_0,
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
