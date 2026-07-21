import os
import json
import csv

# === author imports / helpers ===
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
    # Material constants and dimensions (public from the paper)
    Ep = 60.6e9
    d31 = -274.0e-12
    d311 = 2.85e-17
    m31_prime = -3.70e-16
    L = 0.04
    b = 0.007

    # Bimorph
    tp_bimorph = 0.5e-3
    t_bimorph = 2 * tp_bimorph

    # Unimorph
    tp_unimorph = 0.68e-3
    ts_unimorph = 0.38e-3
    Em = 210e9
    t_unimorph = tp_unimorph + ts_unimorph
    B_unimorph = ts_unimorph / tp_unimorph
    A_unimorph = Em / Ep

    def compute_bimorph(Ez):
        factor = 1.0 + d311 * Ez * Ep
        delta = (3.0 * L**2 / (2.0 * t_bimorph)) * factor * d31 * Ez
        Fbl   = (3.0 * b * t_bimorph**2 * Ep / (8.0 * L)) * factor * d31 * Ez
        return delta, Fbl

    def compute_unimorph(Ez):
        B = B_unimorph
        A = A_unimorph
        D = (1.0 + A**2 * B**4
             + 2.0 * A * (2.0*B + 3.0*B**2 + 2.0*B**3) * (1.0 + d311*Ez*Ep)
             + A**2 * B**4 * d311 * Ez * Ep * (2.0 + d311*Ez*Ep))
        delta = (3.0 * L**2 / t_unimorph) * A * B * (1.0+B)**2 \
                * (1.0 + d311*Ez*Ep)**2 * (d31*Ez + 0.5*m31_prime*Ez**2) / D
        Fbl   = (3.0 * b * t_unimorph**2 * Ep / (4.0 * L)) * A * B \
                * (1.0 + A**2 * B**4 + 2.0*A*(2.0*B + 3.0*B**2 + 2.0*B**3)) \
                * (1.0 + d311*Ez*Ep)**2 * (d31*Ez + 0.5*m31_prime*Ez**2) \
                / ((1.0+B) * (1.0+A*B) * D)
        return delta, Fbl

    ref_grid = [i * 50000.0 for i in range(0, 21)]
    bimorph_expected = [{"electric_field": Ez, "tip_deflection": delta, "blocking_force": Fbl}
                        for Ez in ref_grid for delta, Fbl in [compute_bimorph(Ez)]]
    unimorph_expected = [{"electric_field": Ez, "tip_deflection": delta, "blocking_force": Fbl}
                         for Ez in ref_grid for delta, Fbl in [compute_unimorph(Ez)]]

    return {
        "bimorph": bimorph_expected,
        "unimorph": unimorph_expected,
        "ref_grid": ref_grid
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    expected = ctx["bimorph"]
    field_tol = step.get("field_tolerance", 1.0)
    tolerances = step.get("tolerances", {})
    rel_def = tolerances.get("tip_deflection_relative", 0.02)
    rel_force = tolerances.get("blocking_force_relative", 0.03)
    abs_def = tolerances.get("tip_deflection_absolute", 1e-12)
    abs_force = tolerances.get("blocking_force_absolute", 1e-10)

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    agent_points = sorted(artifact, key=lambda r: r.get("electric_field", 0.0))

    def check(val, ref_val, rel_tol, abs_tol):
        if abs(ref_val) < 1e-30:
            return abs(val) < abs_tol
        else:
            return abs(val - ref_val) <= max(rel_tol * abs(ref_val), abs_tol)

    hits = 0
    for ref in expected:
        ref_Ez = ref["electric_field"]
        closest = None
        min_dist = float("inf")
        for r in agent_points:
            dist = abs(r.get("electric_field", 0.0) - ref_Ez)
            if dist < min_dist:
                min_dist = dist
                closest = r
        if closest is None or min_dist > field_tol:
            continue
        agent_def = closest.get("tip_deflection", 0.0)
        agent_force = closest.get("blocking_force", 0.0)
        ref_def = ref["tip_deflection"]
        ref_force = ref["blocking_force"]
        if check(agent_def, ref_def, rel_def, abs_def) and check(agent_force, ref_force, rel_force, abs_force):
            hits += 1
    return hits / len(expected)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    expected = ctx["unimorph"]
    field_tol = step.get("field_tolerance", 1.0)
    tolerances = step.get("tolerances", {})
    rel_def = tolerances.get("tip_deflection_relative", 0.02)
    rel_force = tolerances.get("blocking_force_relative", 0.03)
    abs_def = tolerances.get("tip_deflection_absolute", 1e-12)
    abs_force = tolerances.get("blocking_force_absolute", 1e-10)

    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    agent_points = sorted(artifact, key=lambda r: r.get("electric_field", 0.0))

    def check(val, ref_val, rel_tol, abs_tol):
        if abs(ref_val) < 1e-30:
            return abs(val) < abs_tol
        else:
            return abs(val - ref_val) <= max(rel_tol * abs(ref_val), abs_tol)

    hits = 0
    for ref in expected:
        ref_Ez = ref["electric_field"]
        closest = None
        min_dist = float("inf")
        for r in agent_points:
            dist = abs(r.get("electric_field", 0.0) - ref_Ez)
            if dist < min_dist:
                min_dist = dist
                closest = r
        if closest is None or min_dist > field_tol:
            continue
        agent_def = closest.get("tip_deflection", 0.0)
        agent_force = closest.get("blocking_force", 0.0)
        ref_def = ref["tip_deflection"]
        ref_force = ref["blocking_force"]
        if check(agent_def, ref_def, rel_def, abs_def) and check(agent_force, ref_force, rel_force, abs_force):
            hits += 1
    return hits / len(expected)


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
