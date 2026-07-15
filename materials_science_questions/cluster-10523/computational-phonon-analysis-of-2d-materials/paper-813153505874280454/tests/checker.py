import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tols = step.get("tolerance", {"a":0.02,"c":0.02})
    rows = [r for r in artifact if r.get("functional") in ("LDA","GGA")]
    total = 0.0
    count = 0
    for r in rows:
        func = r["functional"]
        if func not in gold:
            continue
        a_ok = abs(float(r["a"]) - gold[func]["a"]) <= tols["a"]
        c_ok = abs(float(r["c"]) - gold[func]["c"]) <= tols["c"]
        total += (a_ok + c_ok) / (2 * len(gold))
        count += 1
    score = total if count == len(gold) else 0.0
    return score


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]["frequency"]
    modes_order = step.get("modes_order", ["E2_l","B1_l","A1_TO","E1_TO","E2_h","B1_h","A1_LO","E1_LO"])
    num_entries = len(gold) * len(modes_order)
    ok = 0
    for func, expected in gold.items():
        for mode in modes_order:
            exp = expected[mode]
            found = False
            for r in artifact:
                if r.get("functional") == func and r.get("mode") == mode:
                    if abs(float(r["frequency"]) - exp) <= tol:
                        ok += 1
                    found = True
                    break
            if not found:
                pass
    return ok / num_entries if num_entries else 0.0


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    gold = step["gold"]
    tols = step.get("tolerance", {})
    fields = ["Zp_star","Zperp_star","epsilon_p","epsilon_perp"]
    total_fields = len(gold) * len(fields)
    ok = 0
    for func, exp in gold.items():
        for fld in fields:
            tol = tols.get(fld, 0.5)
            found = False
            for r in artifact:
                if r.get("functional") == func and fld in r:
                    if abs(float(r[fld]) - exp[fld]) <= tol:
                        ok += 1
                    found = True
                    break
            if not found:
                pass
    return ok / total_fields if total_fields else 0.0


# === block: score_3 (check id='step4') ===
def score_3(artifact, step, ctx):
    gold = step.get("gold", {})
    tolerances = step.get("tolerance_absolute", {"entropy":10.0,"specific_heat":5.0})
    check_temps = [300,500,800]

    def check_monotonic(rows, key):
        sorted_rows = sorted([r for r in rows if key in r], key=lambda x: float(x["temperature"]))
        vals = [float(r[key]) for r in sorted_rows]
        for i in range(1, len(vals)):
            if vals[i] < vals[i-1] - 1e-12:
                return False
        return len(vals) >= 2

    monotonic_score = 0.0
    for func in ("LDA","GGA"):
        rows_func = [r for r in artifact if r.get("functional") == func]
        if not rows_func: continue
        if check_monotonic(rows_func, "entropy") and check_monotonic(rows_func, "specific_heat"):
            monotonic_score += 0.5
    monotonic_score = monotonic_score / 2.0

    value_score = 0.0
    num_checks = 0
    for func in ("LDA","GGA"):
        if func not in gold:
            continue
        for T in check_temps:
            T_str = str(T)
            if T_str not in gold[func]:
                continue
            ref = gold[func][T_str]
            best_ent, best_cv = None, None
            for r in artifact:
                if r.get("functional") == func and "temperature" in r:
                    if abs(float(r["temperature"]) - T) < 5.0:
                        best_ent = float(r["entropy"]) if "entropy" in r else None
                        best_cv = float(r["specific_heat"]) if "specific_heat" in r else None
                        break
            if best_ent is not None and "entropy" in ref:
                if abs(best_ent - ref["entropy"]) <= tolerances["entropy"]:
                    value_score += 1
                num_checks += 1
            if best_cv is not None and "specific_heat" in ref:
                if abs(best_cv - ref["specific_heat"]) <= tolerances["specific_heat"]:
                    value_score += 1
                num_checks += 1
    value_score = value_score / num_checks if num_checks > 0 else 0.0

    total_step_score = 0.5 * monotonic_score + 0.5 * value_score
    return total_step_score


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
    'step4': score_3,
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
