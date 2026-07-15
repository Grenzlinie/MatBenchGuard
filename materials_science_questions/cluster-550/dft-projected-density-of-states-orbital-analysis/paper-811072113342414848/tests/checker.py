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
    return {}


# === block: score_0 (check id='structural_props') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step.get('reference', {})
        tol = step.get('tolerances', {})
        comp_scores = []
        for comp, vals in ref.items():
            if comp not in artifact:
                comp_scores.append(0.0)
                continue
            sub = []
            for field in ['a', 'B', 'B_prime']:
                r = vals.get(field)
                v = artifact[comp].get(field)
                if r is None or v is None:
                    sub.append(0.0)
                    continue
                err = abs(v - r) / (abs(r) if r != 0 else 1.0)
                t = tol.get(field, 0.0)
                sub.append(1.0 if err <= t else 0.0)
            comp_scores.append(sum(sub) / len(sub))
        return sum(comp_scores) / len(comp_scores) if comp_scores else 0.0


# === block: score_1 (check id='structural_ordering') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # order checks
        def get_a(comp):
            if comp not in artifact:
                return None
            return artifact[comp].get('a')
        score = 0.0
        # binary ordering: InN < InP < InAs
        a_InN = get_a('InN')
        a_InP = get_a('InP')
        a_InAs = get_a('InAs')
        if a_InN is not None and a_InP is not None and a_InAs is not None:
            if a_InN < a_InP < a_InAs:
                score += 0.5
        # quaternary ordering
        a_q1 = get_a('InAs0.25N0.5P0.25')
        a_q2 = get_a('InAs0.25N0.25P0.5')
        a_q3 = get_a('InAs0.5N0.25P0.25')
        if a_q1 is not None and a_q2 is not None and a_q3 is not None:
            if a_q1 < a_q2 < a_q3:
                score += 0.5
        return score


# === block: score_2 (check id='band_gaps') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step.get('reference', {})
        tol = step.get('tolerances', {})
        comp_scores = []
        for comp, vals in ref.items():
            if comp not in artifact:
                comp_scores.append(0.0)
                continue
            sub = []
            for key in ['E_g_direct', 'E_g_indirect']:
                r = vals.get(key)
                v = artifact[comp].get(key)
                if r is None or v is None:
                    sub.append(0.0)
                    continue
                abs_err = abs(v - r)
                t = tol.get('direct' if 'direct' in key else 'indirect', 0.2)
                sub.append(1.0 if abs_err <= t else 0.0)
            comp_scores.append(sum(sub) / len(sub))
        return sum(comp_scores) / len(comp_scores) if comp_scores else 0.0


# === block: score_3 (check id='refractive_index') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = step.get('reference', {})
        tol = step.get('tolerances', {}).get('n0', 0.2)
        comp_scores = []
        for comp, r in ref.items():
            if comp not in artifact:
                comp_scores.append(0.0)
                continue
            v = artifact[comp]
            if isinstance(v, dict):
                v = v.get('n0', None)
            if v is None or not isinstance(v, (int, float)):
                comp_scores.append(0.0)
                continue
            abs_err = abs(v - r)
            comp_scores.append(1.0 if abs_err <= tol else 0.0)
        return sum(comp_scores) / len(comp_scores) if comp_scores else 0.0


_SCORERS = {
    'structural_props': score_0,
    'structural_ordering': score_1,
    'band_gaps': score_2,
    'refractive_index': score_3,
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
