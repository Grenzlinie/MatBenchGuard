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
    steps = spec.get('steps', []) or []
    step = steps[0] if steps else {}
    gold = step.get('model_gold', {})
    tols = step.get('tolerances', {})
    trend = step.get('trend_required', '')
    return {'gold': gold, 'tolerances': tols, 'trend': trend}


# === block: score_0 (check id='check_moments_and_trend') ===
def score_0(artifact, step, ctx):
    import collections

    def score(artifact, step, ctx):
        rows = artifact
        agent_dict = {}
        for r in rows:
            name = str(r.get('model_name', '')).strip()
            try:
                val = float(r.get('total_magnetic_moment_muB_per_fu', 0))
            except Exception:
                val = None
            if name and val is not None:
                agent_dict[name] = val

        if not agent_dict:
            return 0.0

        gold = ctx['gold']
        tols = ctx['tolerances']
        per_model_scores = []
        for model in ['γ-Ga₂₁□₃O₃₂', 'γ-Ga₂₀Fe₁□₃O₃₂', 'γ-Ga₁₉Fe₂□₃O₃₂']:
            gval = gold.get(model)
            tol = tols.get(model, 1.0)
            aval = agent_dict.get(model)
            if aval is None or gval is None:
                per_model_scores.append(0.0)
                continue
            err = abs(aval - gval)
            if err <= tol:
                s = 1.0
            elif err >= 2 * tol:
                s = 0.0
            else:
                s = 1.0 - (err - tol) / tol
            per_model_scores.append(s)

        if not per_model_scores:
            return 0.0
        avg_score = sum(per_model_scores) / len(per_model_scores)

        # trend check: undoped < single Fe < double Fe
        trend_ok = True
        v1 = agent_dict.get('γ-Ga₂₁□₃O₃₂')
        v2 = agent_dict.get('γ-Ga₂₀Fe₁□₃O₃₂')
        v3 = agent_dict.get('γ-Ga₁₉Fe₂□₃O₃₂')
        if v1 is not None and v2 is not None and v3 is not None:
            if not (v1 < v2 < v3):
                trend_ok = False
        else:
            # can't verify trend with missing data
            trend_ok = False

        penalty = 0.5 if not trend_ok else 1.0
        final = avg_score * penalty
        return round(max(0.0, min(1.0, final)), 6)


_SCORERS = {
    'check_moments_and_trend': score_0,
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
