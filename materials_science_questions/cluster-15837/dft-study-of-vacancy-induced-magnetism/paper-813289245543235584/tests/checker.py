import os
import json
import csv

# === author imports / helpers ===
import json
import os


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


# === block: score_0 (check id='step_n_near') ===
def score_0(artifact, step, ctx):
    import json

    def graded_tol(val, target, tol):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 0.5
        return 0.0

    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    if not isinstance(artifact, dict):
        return 0.0
    t_moment = artifact.get("total_moment_per_Co")
    bond = artifact.get("Co_N_bond_length")
    if t_moment is None or bond is None:
        return 0.0

    targets = step.get("targets", {})
    mom = targets["total_moment"]
    bnd = targets["bond_length"]

    s_mom = graded_tol(t_moment, mom["value"], mom["tolerance"])
    s_bnd = graded_tol(bond, bnd["value"], bnd["tolerance"])
    return 0.5 * s_mom + 0.5 * s_bnd


# === block: score_1 (check id='step_formation') ===
def score_1(artifact, step, ctx):
    import json

    def graded_fixed(val, target, tol):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        elif diff <= 2*tol:
            return 0.5
        return 0.0

    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    if not isinstance(artifact, dict):
        return 0.0
    E_near = artifact.get("formation_energy_near")
    E_far = artifact.get("formation_energy_far")
    delta = artifact.get("delta_E_near_far")
    if None in (E_near, E_far, delta):
        return 0.0

    targets = step.get("targets", {})
    near = targets["formation_energy_near"]
    far = targets["formation_energy_far"]
    dlt = targets["delta_E_near_far"]

    s_near = graded_fixed(E_near, near["value"], near["tolerance"])
    s_far  = graded_fixed(E_far, far["value"], far["tolerance"])

    lower = dlt["lower_threshold"]
    if delta <= lower:
        s_delta = 1.0
    elif delta <= 0:
        s_delta = 0.5
    else:
        s_delta = 0.0

    return 0.2 * s_near + 0.2 * s_far + 0.6 * s_delta


# === block: score_2 (check id='step_exchange') ===
def score_2(artifact, step, ctx):
    import json

    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    if not isinstance(artifact, dict):
        return 0.0
    delta = artifact.get("delta_E_FM_AFM")
    if delta is None:
        return 0.0

    lower = step["targets"]["delta_E_FM_AFM"]["lower_threshold"]
    if delta <= lower:
        return 1.0
    elif delta <= 0:
        return 0.5
    return 0.0


_SCORERS = {
    'step_n_near': score_0,
    'step_formation': score_1,
    'step_exchange': score_2,
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
