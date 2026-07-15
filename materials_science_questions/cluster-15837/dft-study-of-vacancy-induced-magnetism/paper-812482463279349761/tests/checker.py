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


# === block: score_0 (check id='check_electronic_properties') ===
def score_0(artifact, step, ctx):
    fields = step.get("fields", {})
    total = 0.0
    count = 0
    for key, spec in fields.items():
        val = artifact.get(key)
        if val is None:
            continue
        target = spec.get("target") or spec.get("targets")
        tol = spec.get("abs_tol")
        if isinstance(target, list):
            if not isinstance(val, list) or len(val) != len(target):
                pass
            else:
                if isinstance(tol, list):
                    elem_tols = tol
                else:
                    elem_tols = [tol] * len(target)
                sub_scores = []
                for v, t, atol in zip(val, target, elem_tols):
                    sub_scores.append(1.0 if abs(v - t) <= atol else 0.0)
                total += sum(sub_scores) / len(target)
                count += 1
        else:
            if isinstance(val, (int, float)):
                total += 1.0 if abs(val - target) <= tol else 0.0
                count += 1
    score = total / count if count else 0.0
    return score


# === block: score_1 (check id='check_quantum_capacitance') ===
def score_1(artifact, step, ctx):
    rows = artifact
    get = lambda r, k: float(r[k])
    systems = {"pristine": [], "V_C": [], "V_F": [], "V_Sc": []}
    for r in rows:
        sys = r["system"].strip()
        if sys in systems:
            systems[sys].append(r)

    t = step.get("targets", {})

    def find_closest(rows, key, value):
        return min(range(len(rows)), key=lambda i: abs(get(rows[i], key) - value))

    score_cint = score_q06 = score_cneg = score_cpos = 0.0
    cnt_cint = cnt_q06 = cnt_cneg = cnt_cpos = 0

    # C_int at 0 V
    cint0 = t.get("Cint0", {})
    rel_tol = cint0.get("rel_tol", 0.3)
    for sys, rows in systems.items():
        if sys not in cint0 or not rows:
            continue
        idx = find_closest(rows, "V", 0.0)
        val = get(rows[idx], "C_int")
        target = cint0[sys]
        if abs(val - target) <= rel_tol * abs(target):
            score_cint += 1.0
        cnt_cint += 1

    # Q at 0.6 V
    q06 = t.get("Q06", {})
    rel_tol_q = q06.get("rel_tol", 0.25)
    for sys in ["V_Sc", "V_F", "V_C"]:
        if sys not in systems or not systems[sys]:
            continue
        idx = find_closest(systems[sys], "V", 0.6)
        val = get(systems[sys][idx], "Q")
        target = q06[sys]
        if abs(val - target) <= rel_tol_q * abs(target):
            score_q06 += 1.0
        cnt_q06 += 1

    # max C_diff negative
    neg_t = t.get("Cdiff_max_neg", {})
    frac_neg = neg_t.get("abs_tol_frac", 0.3)
    for sys in ["pristine", "V_Sc"]:
        if sys not in systems or not systems[sys]:
            continue
        vals = [get(r, "C_diff") for r in systems[sys] if get(r, "V") < 0]
        if not vals:
            continue
        maxv = max(vals)
        target = neg_t[sys]
        if abs(maxv - target) <= frac_neg * target:
            score_cneg += 1.0
        cnt_cneg += 1

    # max C_diff positive
    pos_t = t.get("Cdiff_max_pos", {})
    frac_pos = pos_t.get("abs_tol_frac", 0.3)
    for sys in ["V_Sc", "V_F", "V_C"]:
        if sys not in systems or not systems[sys]:
            continue
        vals = [get(r, "C_diff") for r in systems[sys] if get(r, "V") > 0]
        if not vals:
            continue
        maxv = max(vals)
        target = pos_t[sys]
        if abs(maxv - target) <= frac_pos * target:
            score_cpos += 1.0
        cnt_cpos += 1

    total = cnt_cint + cnt_q06 + cnt_cneg + cnt_cpos
    return (score_cint + score_q06 + score_cneg + score_cpos) / total if total else 0.0


_SCORERS = {
    'check_electronic_properties': score_0,
    'check_quantum_capacitance': score_1,
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
