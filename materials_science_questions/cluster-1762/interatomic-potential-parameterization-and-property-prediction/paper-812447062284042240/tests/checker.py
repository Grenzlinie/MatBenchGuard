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
    return {}


# === block: score_0 (check id='check_multiple_ionization') ===
def score_0(artifact, step, ctx):
    params = step['params']
    halides_info = params['halides']
    M = params['M']
    rho = params['rho']
    e_sq = params['e_sq']
    Z = params['Z']
    A = params['A']
    count = len(artifact)
    if count == 0:
        return 0.0
    valid = 0
    for row in artifact:
        halide = str(row.get('alkali_halide',''))
        n = float(row['n'])
        p = int(row['p'])
        info = halides_info.get(halide)
        if info is None:
            continue
        p_target = info['p_target']
        if p != p_target:
            continue
        if not (p-1 <= n < p):
            continue
        d = info['d']
        r_anion = info['r_anion']
        r_cation = info['r_cation']
        alpha_minus = info['alpha_minus']
        alpha_plus = info['alpha_plus']
        lhs = (M - (2/3)**0.5) * n * e_sq / d
        rep_cation = math.exp(-(r_anion - r_cation) / rho)
        rep_anion = 1.0
        rep_sum = A * (2 * rep_cation + 2 * rep_anion)
        rep = (1 - (n+1)/Z) * rep_sum
        pol = n*n * e_sq / (4 * d**4) * (15*alpha_minus + 7*alpha_plus)
        rhs = rep - pol
        res = abs(lhs - rhs)
        avg = (abs(lhs) + abs(rhs)) / 2.0
        if avg > 0 and (res / avg) <= 0.10:
            valid += 1
        elif avg == 0:
            valid += 1
    return valid / count


# === block: score_1 (check id='check_energy_per_f_centre') ===
def score_1(artifact, step, ctx):
    gold = step['gold_values']
    tol_rel = step['tolerance_relative']
    count = len(artifact)
    if count == 0:
        return 0.0
    valid = 0
    for row in artifact:
        halide = str(row.get('alkali_halide',''))
        if halide not in gold:
            continue
        ef = float(row['E_F'])
        target = gold[halide]
        if target == 0:
            valid += 1
            continue
        if abs(ef - target) / target <= tol_rel:
            valid += 1
    return valid / count


# === block: score_2 (check id='check_room_temperature') ===
def score_2(artifact, step, ctx):
    gold_delta = step['gold_delta_l_over_l']
    gold_nv = step['gold_N_v']
    tol_rel = step['tolerance_relative']
    if not artifact:
        return 0.0
    row = artifact[0]
    delta = float(row['delta_l_over_l'])
    nv = float(row['N_v'])
    ok = True
    if gold_delta != 0 and abs(delta - gold_delta) / abs(gold_delta) > tol_rel:
        ok = False
    if gold_nv != 0 and abs(nv - gold_nv) / abs(gold_nv) > tol_rel:
        ok = False
    return 1.0 if ok else 0.0


_SCORERS = {
    'check_multiple_ionization': score_0,
    'check_energy_per_f_centre': score_1,
    'check_room_temperature': score_2,
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
