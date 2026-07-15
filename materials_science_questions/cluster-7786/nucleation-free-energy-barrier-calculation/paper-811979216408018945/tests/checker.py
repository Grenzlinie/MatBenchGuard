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
    IS = 1714.0
    C_erg_cm = 5e-6
    R1_cm = 1e-4
    R2_cm = 10e-4

    def compute_r_d(R):
        C_star = C_erg_cm / (R**2 * IS**2)
        d = 0.5 * (math.pi * C_star) ** (1.0/3.0)
        r = 4.0 * ((7.0/20.0) * C_star / (math.pi * d)) ** 0.25
        return r, d

    exp_r1, exp_d1 = compute_r_d(R1_cm)
    exp_r10, exp_d10 = compute_r_d(R2_cm)
    exp_Hs = 2.0 * math.pi * IS
    exp_scaling = 0.5 * (exp_d1/(exp_r1**2) + exp_d10/(exp_r10**2))

    return {
        "exp_r1": exp_r1, "exp_d1": exp_d1, "exp_Hs1": exp_Hs,
        "exp_r10": exp_r10, "exp_d10": exp_d10, "exp_Hs10": exp_Hs,
        "exp_scaling": exp_scaling
    }


# === block: score_0 (check id='nucleus_results_check') ===
def score_0(artifact, step, ctx):
    def _score_field(reported, expected, tol_rel=None, tol_abs=None):
        if tol_abs is not None:
            diff = abs(reported - expected)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / tol_abs)
        else:
            if expected == 0:
                return 1.0 if reported == 0 else 0.0
            rel_err = abs(reported - expected) / abs(expected)
            if rel_err <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)

    data = artifact
    total = 0.0
    for fspec in step.get("fields", []):
        path = fspec["json_path"]
        parts = path.split(".")
        val = data
        try:
            for p in parts:
                val = val[p]
            val = float(val)
        except (KeyError, TypeError, ValueError):
            continue
        exp_key_map = {
            "R_1um.r": "exp_r1", "R_1um.d": "exp_d1", "R_1um.Hs": "exp_Hs1",
            "R_10um.r": "exp_r10", "R_10um.d": "exp_d10", "R_10um.Hs": "exp_Hs10",
            "scaling_coefficient": "exp_scaling"
        }
        exp_key = exp_key_map.get(path)
        if exp_key is None or exp_key not in ctx:
            continue
        expected = ctx[exp_key]
        tol_rel = fspec.get("tolerance_rel")
        tol_abs = fspec.get("tolerance_abs")
        sw = fspec.get("sub_weight", 0.0)
        score = _score_field(val, expected, tol_rel=tol_rel, tol_abs=tol_abs)
        total += score * sw
    return min(total, 1.0)


_SCORERS = {
    'nucleus_results_check': score_0,
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
