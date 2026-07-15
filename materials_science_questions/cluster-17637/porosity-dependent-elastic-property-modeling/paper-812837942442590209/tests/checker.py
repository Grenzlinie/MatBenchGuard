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
    return {
        "baseline_ref": {"K_apparent": 1.89, "strength_reduction": 0.471},
        "ref_curve": {0.05: 0.10, 0.10: 0.22, 0.15: 0.35, 0.20: 0.471, 0.25: 0.55},
        "baseline_K_tol": 0.05,
        "baseline_sr_tol": 0.02,
        "mae_threshold": 0.03
    }


# === block: score_0 (check id='check_base_case') ===
def score_0(artifact, step, ctx):
    artifact = step.get('artifact')  # Injected by harness
    ctx = step.get('ctx')
    if not isinstance(artifact, dict):
        return 0.0
    K = artifact.get('K_apparent')
    sr = artifact.get('strength_reduction')
    if K is None or sr is None:
        return 0.0
    if abs(K) < 1e-12:
        return 0.0
    expected_sr = (K - 1.0) / K
    if abs(expected_sr - sr) > 1e-5:
        return 0.0
    ref = ctx['baseline_ref']
    if abs(K - ref['K_apparent']) <= ctx['baseline_K_tol'] and abs(sr - ref['strength_reduction']) <= ctx['baseline_sr_tol']:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='check_parametric') ===
def score_1(artifact, step, ctx):
    artifact = step.get('artifact')  # List of dicts from CSV
    ctx = step.get('ctx')
    ref = ctx['ref_curve']
    if not isinstance(artifact, list) or len(artifact) < 5:
        return 0.0
    # Build map: porosity -> strength_reduction
    agent_sr = {}
    for row in artifact:
        try:
            p = float(row.get('porosity', None))
            sr_val = float(row.get('strength_reduction', None))
            if p is not None and sr_val is not None:
                agent_sr[p] = sr_val
        except (ValueError, TypeError):
            continue
    total_err = 0.0
    count = 0
    for p_str, ref_sr in ref.items():
        p = float(p_str)
        # Find closest porosity within eps
        closest_p = None
        min_dist = float('inf')
        for ap in agent_sr.keys():
            d = abs(ap - p)
            if d < 0.005 and d < min_dist:
                min_dist = d
                closest_p = ap
        if closest_p is None:
            # Missing porosity => huge error
            total_err += 1.0
            count += 1
            continue
        total_err += abs(agent_sr[closest_p] - ref_sr)
        count += 1
    if count == 0:
        return 0.0
    mae = total_err / count
    if mae <= ctx['mae_threshold']:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'check_base_case': score_0,
    'check_parametric': score_1,
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
