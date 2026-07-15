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


# === block: score_0 (check id='band_structure') ===
def score_0(artifact, step, ctx):
    threshold = step["params"]["dirac_gap_threshold_eV"]
    kpoints = artifact.get("kpoints")
    fermi = artifact.get("fermi_energy")
    if not kpoints or fermi is None:
        return 0.0
    # Find indices of all Γ and Y labels
    gamma_indices = [i for i, kp in enumerate(kpoints) if kp.get("labels") == "Γ"]
    y_indices = [i for i, kp in enumerate(kpoints) if kp.get("labels") == "Y"]
    if len(gamma_indices) < 2 or not y_indices:
        return 0.0
    # The path is Γ-X-S-Γ-Y-X, so the second Γ (after S) precedes the first Y.
    second_gamma_idx = gamma_indices[1]
    first_y_idx = y_indices[0]
    if second_gamma_idx >= first_y_idx:
        return 0.0
    segment = kpoints[second_gamma_idx:first_y_idx+1]
    if not segment:
        return 0.0
    min_gap = float('inf')
    for kp in segment:
        eig = kp.get("eigenvalues")
        if not eig:
            continue
        rel_eig = [e - fermi for e in eig]
        min_abs = min(abs(e) for e in rel_eig)
        if min_abs < min_gap:
            min_gap = min_abs
    return 1.0 if min_gap < threshold else 0.0


# === block: score_1 (check id='phonon_dispersion') ===
def score_1(artifact, step, ctx):
    threshold = step["params"]["min_frequency_threshold"]
    qpoints = artifact.get("qpoints")
    if not qpoints:
        return 0.0
    min_freq = float('inf')
    for qp in qpoints:
        freqs = qp.get("frequencies_THz")
        if not freqs:
            continue
        q_min = min(freqs)
        if q_min < min_freq:
            min_freq = q_min
    if min_freq >= threshold:
        return 1.0
    return 0.0


# === block: score_2 (check id='strain_results') ===
def score_2(artifact, step, ctx):
    uniform_gap_max = step["params"]["uniform_gap_max_eV"]
    shear_gap_min = step["params"]["shear_gap_min_eV"]
    shear_angle_tol = step["params"]["shear_angle_tolerance_deg"]
    uniform_list = artifact.get("uniform_strain", [])
    shear_list = artifact.get("shear_strain", [])
    total_checks = 0
    passed = 0
    for entry in uniform_list:
        gap = entry.get("band_gap_eV")
        if gap is None:
            continue
        total_checks += 1
        if gap < uniform_gap_max:
            passed += 1
    for entry in shear_list:
        theta = entry.get("theta_deg")
        gap = entry.get("band_gap_eV")
        if theta is None or gap is None:
            continue
        if abs(theta - 90.0) > shear_angle_tol:
            total_checks += 1
            if gap > shear_gap_min:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'band_structure': score_0,
    'phonon_dispersion': score_1,
    'strain_results': score_2,
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
