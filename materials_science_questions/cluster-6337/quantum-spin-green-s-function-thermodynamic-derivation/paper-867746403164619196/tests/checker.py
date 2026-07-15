import os
import json
import csv

# === author imports / helpers ===
import json, os, math
from fractions import Fraction


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
    return {"outputs_dir": outputs_dir, "spec": spec}


# === block: score_0 (check id='acf_averages') ===
def score_0(artifact, step, ctx):
    gold_half = step['gold']['half_integer']
    gold_int = step['gold']['integer']
    tol = step.get('tolerance', 1e-9)
    half_in = artifact.get('half_integer', [])
    int_in = artifact.get('integer', [])
    def check_list(gold_list, in_list):
        correct = 0
        for g in gold_list:
            target_s = g['s']
            gold_frac = Fraction(g['fraction'])
            target_avg = float(gold_frac)
            found = False
            for i in in_list:
                if abs(i['s'] - target_s) < 1e-12:
                    found = True
                    if abs(i['average'] - target_avg) < tol:
                        correct += 1
                        break
            if not found:
                pass
        return correct / len(gold_list) if gold_list else 1.0
    s1 = check_list(gold_half, half_in)
    s2 = check_list(gold_int, int_in)
    return 0.5 * s1 + 0.5 * s2


# === block: score_1 (check id='levin_acceleration') ===
def score_1(artifact, step, ctx):
    outputs_dir = ctx['outputs_dir']
    step01_path = os.path.join(outputs_dir, 'step_01_acf_time_averages.json')
    try:
        with open(step01_path) as f:
            step01 = json.load(f)
    except Exception:
        return 0.0
    half_in = step01.get('half_integer', [])
    int_in = step01.get('integer', [])
    M = step.get('M', 7)
    target_half = step['gold']['half_integer_estimate']
    target_int = step['gold']['integer_estimate']
    tol_half = step['gold'].get('half_tol', 1e-6)
    tol_int = step['gold'].get('int_tol', 1e-6)
    classical_target = step['gold']['classical_result']
    classical_tol = step['gold'].get('classical_tol', 1e-9)
    def levin_u(seq):
        U = seq[:M]
        u = [U[0]] + [U[k] - U[k-1] for k in range(1, M)]
        sum_num = 0.0
        sum_den = 0.0
        for k in range(1, M+1):
            coeff = ((-1)**(k-1)) * math.comb(M, k) * (k**(M-2))
            sum_num += coeff * U[k-1] / u[k-1]
            sum_den += coeff / u[k-1]
        return sum_num / sum_den if sum_den != 0 else float('nan')
    def extract_seq(data):
        sorted_items = sorted(data, key=lambda x: x['s'])
        return [item['average'] for item in sorted_items]
    try:
        half_avgs = extract_seq(half_in)
        int_avgs = extract_seq(int_in)
    except Exception:
        return 0.0
    if len(half_avgs) < M or len(int_avgs) < M:
        return 0.0
    comp_half = levin_u(half_avgs)
    comp_int = levin_u(int_avgs)
    err_half = abs(comp_half - target_half)
    s_half = 1.0 if err_half <= tol_half else max(0.0, 1.0 - (err_half - tol_half) / (10 * tol_half))
    err_int = abs(comp_int - target_int)
    s_int = 1.0 if err_int <= tol_int else max(0.0, 1.0 - (err_int - tol_int) / (10 * tol_int))
    classical_val = artifact.get('classical_result', None)
    if classical_val is None:
        classical_score = 0.0
    else:
        err_cl = abs(classical_val - classical_target)
        classical_score = 1.0 if err_cl <= classical_tol else max(0.0, 1.0 - (err_cl - classical_tol) / (10 * classical_tol))
    return 0.5 * s_half + 0.3 * s_int + 0.2 * classical_score


_SCORERS = {
    'acf_averages': score_0,
    'levin_acceleration': score_1,
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
