import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
    return {}


# === block: score_0 (check id='step_elastic_constants') ===
def score_0(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        expected = step.get("expected", {})
        tol = step.get("tolerance", {}).get("relative", 0.10)
        keys = ["C11","C12","C13","C33","C44","C66"]
        phases = ["FM","AFM1","AFM2"]
        scores = []
        for phase in phases:
            if phase not in artifact:
                continue
            for k in keys:
                val = artifact.get(phase, {}).get(k)
                gold = expected.get(phase, {}).get(k)
                if val is None or gold is None:
                    scores.append(0.0)
                    continue
                if abs(gold) < 1e-6:
                    scores.append(1.0 if abs(val) < 1e-6 else 0.0)
                else:
                    rel_err = abs(val - gold) / abs(gold)
                    scores.append(max(0.0, 1.0 - rel_err / tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='step_magnetoelastic_constants') ===
def score_1(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        expected = step.get("expected", {})
        tol_cfg = step.get("tolerance", {})
        mag_thresh = tol_cfg.get("magnitude_threshold", 10.0)
        rel_large = tol_cfg.get("relative_large", 0.25)
        rel_small = tol_cfg.get("relative_small", 0.50)
        keys = ["b21","b22","b3","b4","b3p"]
        phases = ["FM","AFM1","AFM2"]
        scores = []
        for phase in phases:
            if phase not in artifact:
                continue
            for k in keys:
                val = artifact.get(phase, {}).get(k)
                gold = expected.get(phase, {}).get(k)
                if val is None or gold is None:
                    scores.append(0.0)
                    continue
                if abs(gold) < 1e-6:
                    scores.append(1.0 if abs(val) < 1e-6 else 0.0)
                    continue
                rel_tol = rel_small if abs(gold) < mag_thresh else rel_large
                rel_err = abs(val - gold) / abs(gold)
                scores.append(max(0.0, 1.0 - rel_err / rel_tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='step_polycrystalline_parameters') ===
def score_2(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        expected = step.get("expected", {})
        tol = step.get("tolerance", {}).get("relative", 0.25)
        keys = ["xi","eta"]
        phases = ["FM","AFM1","AFM2"]
        scores = []
        for phase in phases:
            if phase not in artifact:
                continue
            for k in keys:
                val = artifact.get(phase, {}).get(k)
                gold = expected.get(phase, {}).get(k)
                if val is None or gold is None:
                    scores.append(0.0)
                    continue
                if abs(gold) < 1e-6:
                    scores.append(1.0 if abs(val) < 1e-6 else 0.0)
                else:
                    rel_err = abs(val - gold) / abs(gold)
                    scores.append(max(0.0, 1.0 - rel_err / tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_3 (check id='step_lambda_recompute') ===
def score_3(artifact, step, ctx):
    def score_fn(artifact, step, ctx):
        out_dir = "/app/outputs"
        try:
            with open(os.path.join(out_dir, "elastic_constants.json")) as f:
                elas = json.load(f)
            with open(os.path.join(out_dir, "magnetoelastic_constants.json")) as f:
                magn = json.load(f)
        except Exception:
            return 0.0
        expected_lambda = step.get("expected_lambda", {})
        tol = step.get("tolerance", {}).get("relative", 0.25)
        phases = ["FM","AFM1","AFM2"]
        scores = []
        for phase in phases:
            c = elas.get(phase, {})
            b = magn.get(phase, {})
            keys_c = ["C11","C12","C13","C33","C44","C66"]
            keys_b = ["b21","b22","b3","b4","b3p"]
            if any(k not in c for k in keys_c) or any(k not in b for k in keys_b):
                for _ in range(5):
                    scores.append(0.0)
                continue
            denom = c["C33"]*(c["C11"]+c["C12"]) - 2*c["C13"]**2
            if abs(denom) < 1e-12:
                for _ in range(2):
                    scores.append(0.0)
            else:
                la1 = (-b["b21"]*c["C33"] + b["b22"]*c["C13"]) / denom
                la2 = (2*b["b21"]*c["C13"] - b["b22"]*(c["C11"]+c["C12"])) / denom
                comps = [
                    ("lambda_alpha1_2", la1),
                    ("lambda_alpha2_2", la2)
                ]
            diff = c["C11"] - c["C12"]
            lg = -b["b3"] / diff if abs(diff)>1e-12 else 0.0
            comps2 = ("lambda_gamma_2", lg)
            ld = -b["b3p"] / (2*c["C66"]) if abs(c["C66"])>1e-12 else 0.0
            comps3 = ("lambda_delta_2", ld)
            le = -b["b4"] / (2*c["C44"]) if abs(c["C44"])>1e-12 else 0.0
            comps4 = ("lambda_epsilon_2", le)
            comps = comps + [comps2, comps3, comps4]
            gold_phase = expected_lambda.get(phase, {})
            for name, val in comps:
                gold = gold_phase.get(name)
                if gold is None:
                    scores.append(0.0)
                    continue
                if abs(gold) < 1e-6:
                    scores.append(1.0 if abs(val) < 1e-6 else 0.0)
                else:
                    rel_err = abs(val - gold) / abs(gold)
                    scores.append(max(0.0, 1.0 - rel_err / tol))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'step_elastic_constants': score_0,
    'step_magnetoelastic_constants': score_1,
    'step_polycrystalline_parameters': score_2,
    'step_lambda_recompute': score_3,
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
