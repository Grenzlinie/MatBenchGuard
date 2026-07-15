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
    return {}


# === block: score_0 (check id='ufg_curves') ===
def score_0(artifact, step, ctx):
    params = step['params']
    ref_E = params['ref_E']
    ref_no = params['ref_no_ni']
    ref_wi = params['ref_with_ni']
    art_by_E = {}
    for row in artifact:
        try:
            e = int(float(row.get('E', 0)))
            no = float(row['Ufg_no_ni'])
            wi = float(row['Ufg_with_ni'])
            art_by_E[e] = (no, wi)
        except:
            continue
    for e in ref_E:
        if e not in art_by_E:
            return 0.0
    err_no = 0.0
    err_wi = 0.0
    n = len(ref_E)
    for e in ref_E:
        ano, awi = art_by_E[e]
        err_no += abs(ano - ref_no[e])
        err_wi += abs(awi - ref_wi[e])
    mae_no = err_no / n
    mae_wi = err_wi / n
    th_no = params['mae_threshold_no']
    mx_no = params['mae_max_loss_no']
    th_wi = params['mae_threshold_wi']
    mx_wi = params['mae_max_loss_wi']
    def score_err(mae, th, mx):
        if mae <= th:
            return 1.0
        elif mae >= mx:
            return 0.0
        else:
            return 1.0 - (mae - th) / (mx - th)
    s_no = score_err(mae_no, th_no, mx_no)
    s_wi = score_err(mae_wi, th_wi, mx_wi)
    composite = 0.5 * s_no + 0.5 * s_wi
    e5 = 5
    e16 = 16
    if e5 not in art_by_E or e16 not in art_by_E:
        bonus = 0.0
    else:
        no_5, _ = art_by_E[e5]
        no_16, _ = art_by_E[e16]
        _, wi_5 = art_by_E[e5]
        _, wi_16 = art_by_E[e16]
        delta_E = e16 - e5
        slope_no = (no_16 - no_5) / delta_E if delta_E != 0 else 0
        slope_wi = (wi_16 - wi_5) / delta_E if delta_E != 0 else 0
        if slope_wi < slope_no:
            bonus = params.get('slope_trend_bonus', 0.05)
        else:
            bonus = 0.0
    final_score = min(1.0, composite + bonus)
    return final_score


_SCORERS = {
    'ufg_curves': score_0,
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
