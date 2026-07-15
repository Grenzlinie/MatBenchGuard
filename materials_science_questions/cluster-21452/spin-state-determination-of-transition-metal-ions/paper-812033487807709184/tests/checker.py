import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    spec = locals().get('spec', {})  # grading_spec_json passed by framework
    steps = spec.get('steps', [])
    ctx = {}
    for step in steps:
        if step.get('output_file') == 'zeeman_splitting.json':
            ctx['zeeman_ref'] = step.get('reference', [])
            ctx['zeeman_tol'] = step.get('tolerance_energy', 1.0)
            break
    return ctx


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    score = 0.0
    fields = ['gamma_cm1','D_cm1','hw_E_cm1','V_over_alpha_cm1']
    if not isinstance(artifact, dict):
        return 0.0
    for key in fields:
        val = artifact.get(key)
        if val is None:
            continue
        target = step['target'][key]
        tol = step['tolerance'][key]
        diff = abs(val - target)
        if diff <= tol:
            score += 1.0
        else:
            # partial credit: decay from 1 to 0 over an additional 10 cm^-1 range
            extra = diff - tol
            score += max(0.0, 1.0 - extra / 10.0)
    return score / len(fields)


# === block: score_1 (check id='step3') ===
def score_1(artifact, step, ctx):
    ref = ctx.get('zeeman_ref', [])

    tol = ctx.get('zeeman_tol', 1.0)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    ref_matched = [False] * len(ref)
    for sub in artifact:
        sub_en = sub.get('energy_cm1')
        sub_pol = sub.get('polarization')
        if sub_en is None or sub_pol is None:
            continue
        best_idx = -1
        best_diff = float('inf')
        for i, r in enumerate(ref):
            if r['polarization'] != sub_pol:
                continue
            diff = abs(sub_en - r['energy_cm1'])
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        if best_idx >= 0 and best_diff <= tol:
            ref_matched[best_idx] = True
    recall = sum(ref_matched) / len(ref) if len(ref) > 0 else 1.0
    # precision penalizes extra unmatched components
    precision = sum(ref_matched) / len(artifact) if len(artifact) > 0 else 0.0
    # harmonic mean of recall and precision
    if recall + precision == 0:
        return 0.0
    return 2 * recall * precision / (recall + precision)


_SCORERS = {
    'step2': score_0,
    'step3': score_1,
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
