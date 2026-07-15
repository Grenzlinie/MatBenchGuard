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
    # Build reference mapping from the custom step
    md_ref = {}
    for st in spec.get('steps', []):
        if st.get('reference_md'):
            for r in st['reference_md']:
                md_ref[float(r[0])] = (float(r[1]), float(r[2]))
    return {'md_ref': md_ref}


# === block: score_0 (check id='transition_results') ===
def score_0(artifact, step, ctx):
    # artifact is a dict; step['fields'] holds targets and tolerances
    fields = step.get('fields', {})
    count = 0
    total = len(fields)
    if total == 0:
        return 0.0
    for key, spec in fields.items():
        if key in artifact and isinstance(artifact[key], (int, float)):
            if abs(float(artifact[key]) - spec['target']) <= spec['tolerance']:
                count += 1
    return count / total


# === block: score_1 (check id='md_pressure_table') ===
def score_1(artifact, step, ctx):
    # artifact is a list of dicts (CSV rows)
    rows = artifact
    if not rows:
        return 0.0

    # recompute analytic columns
    analytic_ok = True
    for row in rows:
        tau = float(row['tau'])
        # free volume
        s = math.sqrt(tau)
        expected_fv = s / (s - 1.0)
        # Pade' approximant
        ti = 1.0 / tau
        ti2 = ti * ti
        ti3 = ti2 * ti
        num = 1.0 - 0.98164*ti + 0.32755*ti2 - 0.0276113*ti3
        den = 1.0 - 2.98164*ti + 3.2908*ti2 - 1.3310*ti3
        expected_pade = num / den
        if abs(float(row['pv_free_volume']) - expected_fv) > 1e-8 or abs(float(row['pv_pade']) - expected_pade) > 1e-8:
            analytic_ok = False
            break

    # MD pressure deviation scores
    ref_map = ctx.get('md_ref', {})
    md_scores = []
    for row in rows:
        tau = float(row['tau'])
        pv_md = float(row['pv_md'])
        ref = ref_map.get(tau)
        if ref is None:
            md_scores.append(0.0)
        else:
            ref_pv, _ = ref
            diff = abs(pv_md - ref_pv)
            if diff <= 0.3:
                md_scores.append(1.0)
            elif diff <= 1.0:
                md_scores.append(1.0 - (diff - 0.3)/0.7)
            else:
                md_scores.append(0.0)
    md_score = sum(md_scores) / max(len(md_scores), 1)

    # structural checks
    # monotonic decreasing
    sorted_rows = sorted(rows, key=lambda r: float(r['tau']))
    monotonic_ok = True
    for i in range(len(sorted_rows)-1):
        if float(sorted_rows[i+1]['pv_md']) > float(sorted_rows[i]['pv_md']) + 0.1:
            monotonic_ok = False
            break
    mono_score = 1.0 if monotonic_ok else 0.5

    # high-density agreement with free-volume (tau <= 1.4)
    hd_ok = True
    for row in rows:
        tau = float(row['tau'])
        if tau <= 1.4:
            pfv = math.sqrt(tau)/(math.sqrt(tau)-1.0)
            if abs(float(row['pv_md']) - pfv) > 0.5:
                hd_ok = False
                break
    hd_score = 1.0 if hd_ok else 0.5

    # std sanity check
    std_ok = True
    for row in rows:
        std_val = float(row['pv_md_std'])
        if std_val < 0 or std_val > 0.3:
            std_ok = False
            break
    std_score = 1.0 if std_ok else 0.5

    # weighted composite
    score = 0.3 * (1.0 if analytic_ok else 0.0) + 0.5 * md_score + 0.1 * mono_score + 0.05 * hd_score + 0.05 * std_score
    return score


_SCORERS = {
    'transition_results': score_0,
    'md_pressure_table': score_1,
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
