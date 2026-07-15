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


# === block: score_0 (check id='computed_properties_check') ===
def score_0(artifact, step, ctx):
    nv = artifact.get("neutral_vacancy", {})
    neg = artifact.get("negative_vacancy", {})
    cmp = artifact.get("comparison_experiment", "")

    def score_num(val, target, tol):
        if not isinstance(val, (int, float)):
            return 0.0
        dev = abs(val - target)
        if dev <= tol:
            return 1.0
        return max(0.0, 1.0 - (dev - tol) / (2.0 * tol))

    def check_str(val, expected):
        return 1.0 if isinstance(val, str) and val.strip() == expected else 0.0

    scores = []
    # Numeric fields
    scores.append(score_num(nv.get("lowest_excitation_energy_eV", None), 2.0, 0.05))
    scores.append(score_num(neg.get("first_excitation_energy_eV", None), 1.568, 0.05))
    scores.append(score_num(neg.get("second_excitation_energy_eV", None), 1.572, 0.05))
    scores.append(score_num(neg.get("relaxation_energy_eV", None), 0.1, 0.05))
    scores.append(score_num(neg.get("estimated_zero_phonon_line_eV", None), 1.47, 0.05))

    # Symmetry strings
    scores.append(check_str(nv.get("ground_state_symmetry", ""), "^3A_2"))
    scores.append(check_str(nv.get("lowest_excited_state_symmetry", ""), "^3E"))
    scores.append(check_str(neg.get("ground_state_symmetry", ""), "^4A_2"))
    scores.append(check_str(neg.get("first_excited_state_symmetry", ""), "^4A_2"))
    scores.append(check_str(neg.get("second_excited_state_symmetry", ""), "^4E"))

    # Polarization rules
    scores.append(check_str(nv.get("polarization_rules", ""), "perpendicular only"))
    scores.append(check_str(neg.get("polarization_rules", ""), "E||c for ^4A_2, E_perp_c for ^4E"))

    # Comparison statement keyword check
    cmp_text = cmp.lower() if isinstance(cmp, str) else ""
    c_checks = 0.0
    c_hits = 0
    if "negatively charged" in cmp_text and "v1" in cmp_text:
        c_hits += 1
    if "neutral" in cmp_text and ("not match" in cmp_text or "does not match" in cmp_text or "do not match" in cmp_text):
        c_hits += 1
    if c_hits >= 2:
        c_checks = 1.0
    else:
        c_checks = c_hits / 2.0
    scores.append(c_checks)

    denom = len(scores)
    total = sum(scores) / denom if denom > 0 else 0.0
    return round(total, 6)


_SCORERS = {
    'computed_properties_check': score_0,
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
