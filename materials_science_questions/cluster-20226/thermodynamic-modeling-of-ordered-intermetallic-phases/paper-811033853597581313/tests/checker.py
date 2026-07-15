import os
import json
import csv

# === author imports / helpers ===
import math

def scalar_score(actual, expected, abs_tol, rel_tol):
    if abs(expected) < 1e-12:
        return 1.0 if abs(actual) < abs_tol else 0.0
    diff = abs(actual - expected)
    tol = abs_tol + rel_tol * abs(expected)
    if diff <= tol:
        return 1.0
    decay_range = 5 * tol
    return max(0.0, 1.0 - (diff - tol) / decay_range)


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
    import os, json

    def prepare(outputs_dir, spec):
        ctx = {}
        f1 = os.path.join(outputs_dir, 'delta_g_coefficients.json')
        if os.path.exists(f1):
            with open(f1) as f:
                ctx['delta_g'] = json.load(f)
        else:
            ctx['delta_g'] = None
        f2 = os.path.join(outputs_dir, 'delta_T0_eta_coefficient.json')
        if os.path.exists(f2):
            with open(f2) as f:
                ctx['delta_T0_eta'] = json.load(f)
        else:
            ctx['delta_T0_eta'] = None
        f3 = os.path.join(outputs_dir, 'final_coefficient.json')
        if os.path.exists(f3):
            with open(f3) as f:
                ctx['final_coefficient'] = json.load(f)
        else:
            ctx['final_coefficient'] = None
        return ctx


# === block: score_0 (check id='step_01_assemble_delta_g_coefficients') ===
def score_0(artifact, step, ctx):
        try:
            ref = step.get('reference', {})
            tols = step.get('tolerances', {})
            if not ref or not tols:
                return 0.0
            scores = []
            for key in ('A', 'B', 'C'):
                expected = ref.get(key)
                tol = tols.get(key)
                if expected is None or tol is None:
                    scores.append(0.0)
                    continue
                if not isinstance(artifact, dict):
                    scores.append(0.0)
                    continue
                actual = artifact.get(key)
                if actual is None:
                    scores.append(0.0)
                    continue
                try:
                    actual = float(actual)
                except (TypeError, ValueError):
                    scores.append(0.0)
                    continue
                try:
                    s = scalar_score(actual, expected, tol.get('abs_tol', 0.0), tol.get('rel_tol', 0.0))
                except Exception:
                    s = 0.0
                scores.append(s)
            if not scores:
                return 0.0
            return sum(scores) / len(scores)
        except Exception:
            return 0.0


# === block: score_1 (check id='step_02_delta_t0_eta_coefficient') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        delta_g = ctx.get('delta_g')
        if delta_g is None or artifact is None:
            return 0.0
        B = delta_g.get('B')
        C = delta_g.get('C')
        if B is None or C is None or C == 0:
            return 0.0
        expected = -B / C
        actual = artifact.get('coefficient_eta2')
        if actual is None:
            return 0.0
        tol = step['tolerances']
        return scalar_score(actual, expected, tol['abs_tol'], tol['rel_tol'])


# === block: score_2 (check id='step_03_final_coefficient_phi') ===
def score_2(artifact, step, ctx):
        delta_T0_eta = ctx.get('delta_T0_eta')
        if delta_T0_eta is None or artifact is None:
            return 0.0
        eta2_coeff = delta_T0_eta.get('coefficient_eta2')
        if eta2_coeff is None:
            return 0.0
        c = step.get('c', 0.312)
        expected = eta2_coeff * (2 * c) ** 2
        actual = artifact.get('coefficient_phi2')
        if actual is None:
            return 0.0
        tol = step['tolerances']
        return scalar_score(actual, expected, tol['abs_tol'], tol['rel_tol'])


_SCORERS = {
    'step_01_assemble_delta_g_coefficients': score_0,
    'step_02_delta_t0_eta_coefficient': score_1,
    'step_03_final_coefficient_phi': score_2,
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
