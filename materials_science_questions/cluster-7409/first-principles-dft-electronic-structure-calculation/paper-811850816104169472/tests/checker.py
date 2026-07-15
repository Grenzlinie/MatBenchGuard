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


# === block: score_0 (check id='check_surface_Ti_displacement') ===
def score_0(artifact, step, ctx):
    field = step.get("field", "surface_Ti_displacement")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.0)
    tolerance = step.get("tolerance", 0.02)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_1 (check id='check_interlayer_d12') ===
def score_1(artifact, step, ctx):
    field = step.get("field", "interlayer_relaxation_d12")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.0)
    tolerance = step.get("tolerance", 2.0)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_2 (check id='check_interlayer_d23') ===
def score_2(artifact, step, ctx):
    field = step.get("field", "interlayer_relaxation_d23")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.0)
    tolerance = step.get("tolerance", 2.0)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_3 (check id='check_outermost_bond_contraction') ===
def score_3(artifact, step, ctx):
    field = step.get("field", "outermost_Ti-O_bond_contraction")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.0)
    tolerance = step.get("tolerance", 1.0)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_4 (check id='check_subsurface_bond_expansion') ===
def score_4(artifact, step, ctx):
    field = step.get("field", "subsurface_Ti-O_bond_expansion")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.0)
    tolerance = step.get("tolerance", 1.0)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_5 (check id='check_rumpling_PbO3') ===
def score_5(artifact, step, ctx):
    field = step.get("field", "rumpling_second_PbO3_layer")
    value = artifact.get(field)
    if not isinstance(value, (int, float)):
        return 0.0
    target = step.get("target_value", 0.448)
    tolerance = step.get("tolerance", 0.02)
    if abs(value - target) <= tolerance:
        return 1.0
    return 0.0


# === block: score_6 (check id='check_layer_displacements') ===
def score_6(artifact, step, ctx):
    layers = artifact.get("layer_displacements", [])
    if not isinstance(layers, list) or len(layers) == 0:
        return 0.0
    for item in layers:
        if not isinstance(item, dict):
            return 0.0
        if "layer" not in item or "atom_type" not in item or "displacement" not in item:
            return 0.0
    surface_Ti_disp = artifact.get("surface_Ti_displacement")
    if isinstance(surface_Ti_disp, (int, float)):
        layer1_Ti = None
        for item in layers:
            if item.get("layer") == 1 and item.get("atom_type") == "Ti":
                layer1_Ti = item.get("displacement")
                break
        if layer1_Ti is not None:
            tol = step.get("displacement_tolerance", 0.02)
            if abs(layer1_Ti - surface_Ti_disp) <= tol:
                return 1.0
            else:
                return 0.0
    # structure is present but consistency check not possible (no layer 1 Ti entry); partial credit
    return 0.5


_SCORERS = {
    'check_surface_Ti_displacement': score_0,
    'check_interlayer_d12': score_1,
    'check_interlayer_d23': score_2,
    'check_outermost_bond_contraction': score_3,
    'check_subsurface_bond_expansion': score_4,
    'check_rumpling_PbO3': score_5,
    'check_layer_displacements': score_6,
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
