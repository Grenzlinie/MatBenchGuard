import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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


# === block: score_0 (check id='step_4') ===
def score_0(artifact, step, ctx):
    ref = step.get("reference", {})
    k300_ref = ref.get("k300", 645)
    tol_rel = ref.get("k300_tol_rel", 0.2)
    rta_ratio_ref = ref.get("rta_ratio_300", 0.5)
    rta_tol = ref.get("rta_ratio_tol", 0.1)
    temps_required = ref.get("temperatures", [300, 500, 700])
    holdout_temp = ref.get("holdout_temperature", None)
    holdout_value = ref.get("holdout_value", None)
    holdout_tol = ref.get("holdout_tol", 0.05)
    if not artifact or not isinstance(artifact, list):
        return 0.0
    rows = {}
    for row in artifact:
        try:
            t = float(row.get("T_K", ""))
            k_iter = float(row.get("K_lat_iterative_W_mK", "nan"))
            k_rta = float(row.get("K_lat_RTA_W_mK", "nan"))
            rows[t] = (k_iter, k_rta)
        except (ValueError, TypeError):
            continue
    missing = any(t not in rows for t in temps_required)
    if missing:
        return 0.0
    k300_iter = rows[300][0]
    k300_rta = rows[300][1]
    rel_err = abs(k300_iter - k300_ref) / k300_ref if k300_ref != 0 else abs(k300_iter - k300_ref)
    if rel_err <= tol_rel:
        score_k = 1.0
    else:
        score_k = max(0.0, 1.0 - (rel_err - tol_rel) / 0.3)
    k500_iter = rows[500][0]
    k700_iter = rows[700][0]
    monotonic = k300_iter > k500_iter > k700_iter
    score_mono = 1.0 if monotonic else 0.0
    if k300_iter == 0:
        ratio = None
    else:
        ratio = k300_rta / k300_iter
    if ratio is not None and abs(ratio - rta_ratio_ref) <= rta_tol:
        score_ratio = 1.0
    else:
        score_ratio = 0.0
    if holdout_temp is not None and holdout_value is not None:
        if holdout_temp not in rows:
            score_holdout = 0.0
        else:
            k_iter_holdout = rows[holdout_temp][0]
            rel_err_hold = abs(k_iter_holdout - holdout_value) / abs(holdout_value)
            if rel_err_hold <= holdout_tol:
                score_holdout = 1.0
            else:
                score_holdout = max(0.0, 1.0 - (rel_err_hold - holdout_tol) / 0.2)
        final = 0.4 * score_k + 0.2 * score_mono + 0.2 * score_ratio + 0.2 * score_holdout
    else:
        final = 0.5 * score_k + 0.25 * score_mono + 0.25 * score_ratio
    return min(max(final, 0.0), 1.0)


# === block: score_1 (check id='step_5') ===
def score_1(artifact, step, ctx):
    ref = step.get("reference", {})
    target_exp = ref.get("exponent", 0.735)
    tol = ref.get("tolerance", 0.1)
    text = artifact if isinstance(artifact, str) else ""
    try:
        val = float(text.strip().split()[0])
    except:
        return 0.0
    err = abs(val - target_exp)
    if err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (err - tol) / tol)


# === block: score_2 (check id='step_6') ===
def score_2(artifact, step, ctx):
    ref = step.get("reference", {})
    za_ref = ref.get("ZA_fraction", 0.6)
    za_tol = ref.get("ZA_tol", 0.15)
    sum_range = ref.get("sum_tol_range", [0.95, 1.05])
    if not artifact or not isinstance(artifact, list):
        return 0.0
    branches = {}
    for row in artifact:
        branch = str(row.get("branch", "")).strip().upper()
        try:
            ratio = float(row.get("contribution_ratio", "nan"))
        except:
            continue
        branches[branch] = ratio
    za_val = branches.get("ZA", None)
    if za_val is None:
        return 0.0
    za_score = 1.0 if abs(za_val - za_ref) <= za_tol else 0.0
    total = sum(branches.values())
    sum_score = 1.0 if sum_range[0] <= total <= sum_range[1] else 0.0
    final = 0.7 * za_score + 0.3 * sum_score
    return final


_SCORERS = {
    'step_4': score_0,
    'step_5': score_1,
    'step_6': score_2,
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
