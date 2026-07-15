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
        ctx = {}
        for step in spec.get("steps", []):
            if step.get("output_file") == "step_01_full_model.csv":
                ctx["step01_gold"] = step.get("targets", {})
                ctx["step01_tolerances"] = step.get("tolerances", {})
                ctx["step01_abs_fields"] = step.get("tolerance_type", {}).get("absolute", [])
            elif step.get("output_file") == "step_02_ablation.csv":
                ctx["step02_threshold"] = step.get("threshold", 0.05)
        # Ensure c14 absolute tolerance is handled properly
        if "step01_gold" in ctx:
            ctx["step01_abs_fields"] = [k for k, v in spec.get("steps", [{}])[0].get("tolerance_type", {}).items() if v == "absolute"]
        return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        gold = ctx.get("step01_gold", {})
        tol_rel = ctx.get("step01_tolerances", {})
        abs_fields = ctx.get("step01_abs_fields", ["c14"])
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        row = artifact[0]
        scores = []
        for key in ["c11","c12","c13","c14","c44","K"]:
            val_str = row.get(key)
            if val_str is None:
                scores.append(0.0)
                continue
            try:
                val = float(val_str)
            except (ValueError, TypeError):
                scores.append(0.0)
                continue
            target = gold.get(key)
            if target is None:
                scores.append(0.0)
                continue
            if key in abs_fields:
                # absolute tolerance
                tol = tol_rel.get(key, 0.02)
                scores.append(1.0 if abs(val - target) <= tol else 0.0)
            else:
                # relative tolerance
                tol = tol_rel.get(key, 0.1)
                if target == 0:
                    scores.append(1.0 if abs(val) <= 1e-9 else 0.0)
                else:
                    rel_err = abs(val - target) / abs(target)
                    scores.append(1.0 if rel_err <= tol else 0.0)
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
        threshold = ctx.get("step02_threshold", 0.05)
        if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
            return 0.0
        row = artifact[0]
        val_str = row.get("K_ablated")
        if val_str is None:
            return 0.0
        try:
            K_ablated = float(val_str)
        except (ValueError, TypeError):
            return 0.0
        return 1.0 if K_ablated <= threshold else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
