import os
import json
import csv

# === author imports / helpers ===
import json, re


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


# === block: score_0 (check id='ima2_instability') ===
def score_0(artifact, step, ctx):
    import json
    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    has_imag = artifact.get("has_imaginary_modes", False)
    freq_list = artifact.get("imaginary_frequencies_at_qpoints", [])
    min_freq = artifact.get("minimum_frequency_cm", 0)
    target_qpoints = step.get("hidden", {}).get("qpoints", [[0,0,0],[0.5,0,0]])
    checks = []
    checks.append(1 if has_imag else 0)
    gamma_found = any(item.get("qpoint") == target_qpoints[0] and any(f < 0 for f in item.get("frequencies", [])) for item in freq_list)
    checks.append(1 if gamma_found else 0)
    s_found = any(item.get("qpoint") == target_qpoints[1] and any(f < 0 for f in item.get("frequencies", [])) for item in freq_list)
    checks.append(1 if s_found else 0)
    checks.append(1 if min_freq < 0 else 0)
    score = sum(checks) / len(checks)
    return score


# === block: score_1 (check id='energy_minima') ===
def score_1(artifact, step, ctx):
    import json
    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    targets = step.get("hidden", {}).get("targets", {})
    tol = step.get("hidden", {}).get("tolerance", 0.02)
    gamma = artifact.get("gamma_mode", {})
    s_mode = artifact.get("S_mode", {})
    passes = []
    for elem in ["Ta", "Re", "Si"]:
        passes.append(1 if abs(gamma.get(elem, 0) - targets.get("gamma_mode", {}).get(elem, 0)) <= tol else 0)
    for elem in ["Ta", "Re", "Si"]:
        passes.append(1 if abs(s_mode.get(elem, 0) - targets.get("S_mode", {}).get(elem, 0)) <= tol else 0)
    score = sum(passes) / len(passes)
    return score


# === block: score_2 (check id='relax_s_cm') ===
def score_2(artifact, step, ctx):
    cif_text = artifact if isinstance(artifact, str) else ""
    space_group = None
    for line in cif_text.splitlines():
        if line.startswith("_symmetry_space_group_name_H-M") or line.startswith("_space_group_name_H-M"):
            parts = line.split()
            if len(parts) > 1:
                space_group = " ".join(parts[1:]).strip().replace("'", "").replace('"', "")
            break
    if space_group is None:
        for line in cif_text.splitlines():
            if line.startswith("_space_group_IT_number"):
                parts = line.split()
                if len(parts) > 1 and parts[1].strip() == "8":
                    space_group = "8"
                break
    if space_group:
        norm = space_group.replace("(", "").replace(")", "").replace(" ", "").lower()
        if "cm" in norm or space_group == "8":
            score = 1.0
        else:
            score = 0.0
    else:
        score = 0.0
    return score


# === block: score_3 (check id='cm_stability') ===
def score_3(artifact, step, ctx):
    import json
    artifact = json.loads(artifact) if isinstance(artifact, str) else artifact
    all_pos = artifact.get("all_frequencies_positive", False)
    no_imag = artifact.get("no_imaginary_modes_confirmed", False)
    min_freq = artifact.get("minimum_phonon_frequency_cm", -100)
    threshold = step.get("hidden", {}).get("min_frequency_threshold", -1)
    score = 1.0 if (all_pos and no_imag and min_freq >= threshold) else 0.0
    return score


_SCORERS = {
    'ima2_instability': score_0,
    'energy_minima': score_1,
    'relax_s_cm': score_2,
    'cm_stability': score_3,
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
