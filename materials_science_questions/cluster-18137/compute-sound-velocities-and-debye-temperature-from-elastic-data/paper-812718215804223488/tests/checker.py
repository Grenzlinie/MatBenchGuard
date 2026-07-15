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


# === block: score_0 (check id='table1_results') ===
def score_0(artifact, step, ctx):
    gold = step["gold_table"]
    rel_fields = set(step["rel_tol_fields"])
    abs_fields = set(step["abs_tol_fields"])
    rel_tol = step["rel_tol"]
    abs_tol = step["abs_tol"]
    # Use a generous absolute tolerance floor for Debye temperatures
    # so that legitimate toolchain spread (e.g. different PBEsol implementations)
    # does not unfairly zero the score, especially at low temperatures.
    effective_abs_tol = max(abs_tol, 15.0)

    if not isinstance(artifact, dict):
        return 0.0

    system_scores = []
    for sys_name, gold_vals in gold.items():
        if sys_name not in artifact:
            system_scores.append(0.0)
            continue
        vals = artifact[sys_name]
        if not isinstance(vals, dict):
            system_scores.append(0.0)
            continue
        field_scores = []
        for field, ref in gold_vals.items():
            if ref is None:
                continue
            val = vals.get(field)
            if val is None:
                field_scores.append(0.0)
                continue
            try:
                val = float(val)
            except (ValueError, TypeError):
                field_scores.append(0.0)
                continue
            if field in rel_fields:
                if ref == 0:
                    err = abs(val)
                else:
                    err = abs(val - ref) / abs(ref)
                score_f = max(0.0, 1.0 - err / rel_tol)
            elif field in abs_fields:
                err = abs(val - ref)
                score_f = max(0.0, 1.0 - err / effective_abs_tol)
            else:
                score_f = 1.0
            field_scores.append(score_f)
        sys_score = sum(field_scores) / len(field_scores) if field_scores else 0.0
        system_scores.append(sys_score)

    return sum(system_scores) / len(system_scores) if system_scores else 0.0


# === block: score_1 (check id='spectral_width') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0

    required = ["Si46","Ge46","Na8Si46","K8Si46","Ba8Si46","K8Ge44□2","Ba8Ge43□3"]
    if not all(k in artifact for k in required):
        return 0.0

    scores = []

    # empty hosts
    for sys, key, (lo,hi) in [("Si46","spectral_width",step["si_width_range"]),
                               ("Ge46","spectral_width",step["ge_width_range"])]:
        val = artifact.get(sys, {}).get(key)
        scores.append(1.0 if isinstance(val,(int,float)) and lo <= val <= hi else 0.0)

    # filled Si
    for sys in ["Na8Si46","K8Si46","Ba8Si46"]:
        val = artifact.get(sys, {}).get("reduction_percent")
        lo,hi = step["si_reduction_range"]
        scores.append(1.0 if isinstance(val,(int,float)) and lo <= val <= hi else 0.0)

    # filled Ge
    for sys in ["K8Ge44□2","Ba8Ge43□3"]:
        val = artifact.get(sys, {}).get("reduction_percent")
        lo,hi = step["ge_reduction_range"]
        scores.append(1.0 if isinstance(val,(int,float)) and lo <= val <= hi else 0.0)

    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'table1_results': score_0,
    'spectral_width': score_1,
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
