import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    steps = spec.get("steps", [])
    gold = {}
    for step in steps:
        sid = step["id"]
        if "reference" in step:
            gold[sid] = step["reference"]
        if "reference_kp_delta_T" in step:
            gold[sid] = (step["reference_kp_delta_T"], step.get("rel_tol", 0.05), step.get("check_monotonic", False))
    return {"gold": gold}


# === block: score_0 (check id='step_1_wilson') ===
def score_0(artifact, step, ctx):
    gold_data = ctx["gold"].get(step["id"], {})
    if not gold_data:
        return 0.0
    values = {}
    for row in artifact:
        var = row.get("variable", "").strip()
        try:
            val = float(row.get("analytical_value", ""))
        except (ValueError, TypeError):
            continue
        values[var] = val
    vars_check = ["ΔT_W", "N_W", "r_30", "r_32", "Y_W"]
    total = len(vars_check)
    score_sum = 0.0
    for v in vars_check:
        if v not in gold_data:
            continue
        gv = gold_data[v]["value"]
        tol = gold_data[v]["rel_tol"]
        av = values.get(v, None)
        if av is None:
            continue
        rel_err = abs(av - gv) / abs(gv) if gv != 0 else abs(av - gv)
        if rel_err <= tol:
            score_sum += 1.0
        else:
            # linear decay to zero at 2*tol
            score_sum += max(0.0, 1.0 - (rel_err - tol) / tol)
    return score_sum / total if total > 0 else 0.0


# === block: score_1 (check id='step_2_sweep') ===
def score_1(artifact, step, ctx):
    ref_data, rel_tol, check_mono = ctx["gold"].get(step["id"], ([], 0.05, False))
    if not ref_data:
        return 0.0
    kps, dts = [], []
    for row in artifact:
        try:
            k = float(row["k_p"])
            dt = float(row["delta_T_W"])
        except (ValueError, TypeError, KeyError):
            continue
        kps.append(k)
        dts.append(dt)
    if len(kps) < 2:
        return 0.0
    sorted_pairs = sorted(zip(kps, dts), key=lambda x: x[0])
    kps_sorted, dts_sorted = zip(*sorted_pairs)
    mono_score = 1.0 if all(dts_sorted[i] <= dts_sorted[i+1] for i in range(len(dts_sorted)-1)) else 0.0
    ref_scores = []
    for ref in ref_data:
        kp_ref = ref["k_p"]
        dt_ref = ref["delta_T_W"]
        if kp_ref <= kps_sorted[0]:
            interp = dts_sorted[0]
        elif kp_ref >= kps_sorted[-1]:
            interp = dts_sorted[-1]
        else:
            idx = 0
            for i, k in enumerate(kps_sorted):
                if k > kp_ref:
                    idx = i-1
                    break
            x0, y0 = kps_sorted[idx], dts_sorted[idx]
            x1, y1 = kps_sorted[idx+1], dts_sorted[idx+1]
            interp = y0 + (y1 - y0) * (kp_ref - x0) / (x1 - x0)
        rel_err = abs(interp - dt_ref) / abs(dt_ref) if dt_ref != 0 else abs(interp - dt_ref)
        if rel_err <= rel_tol:
            ref_scores.append(1.0)
        else:
            ref_scores.append(max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol))
    ref_avg = sum(ref_scores) / len(ref_scores) if ref_scores else 0.0
    return 0.5 * mono_score + 0.5 * ref_avg


_SCORERS = {
    'step_1_wilson': score_0,
    'step_2_sweep': score_1,
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
