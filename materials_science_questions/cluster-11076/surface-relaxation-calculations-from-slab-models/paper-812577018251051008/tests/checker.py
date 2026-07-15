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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        ref_bulk = None
        ref_surface = None
        for step in steps:
            if step.get("id") == "bulk_properties":
                ref_bulk = step.get("reference", {})
            elif step.get("id") == "surface_results":
                ref_surface = step.get("reference", {})
        return {"ref_bulk": ref_bulk, "ref_surface": ref_surface}


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = ctx["ref_bulk"]
        tol_lattice = step["tolerances"]["lattice_constant_A"]
        tol_gap = step["tolerances"]["band_gap_eV"]
        tol_total = step["tolerances"]["total_moment_mu_B"]
        tol_atomic = step["tolerances"]["atomic_moment_mu_B"]
        scores = []

        lattice = artifact.get("equilibrium_lattice_constant_A")
        scores.append(1.0 if isinstance(lattice, (int, float)) and abs(lattice - ref["equilibrium_lattice_constant_A"]) <= tol_lattice else 0.0)

        gap = artifact.get("bulk_band_gap_majority_eV")
        scores.append(1.0 if isinstance(gap, (int, float)) and abs(gap - ref["bulk_band_gap_majority_eV"]) <= tol_gap else 0.0)

        total = artifact.get("total_magnetic_moment_mu_B")
        scores.append(1.0 if isinstance(total, (int, float)) and abs(total - ref["total_magnetic_moment_mu_B"]) <= tol_total else 0.0)

        atm = artifact.get("atomic_magnetic_moments", {})
        ref_atm = ref["atomic_magnetic_moments"]
        for key in ["Zr1", "Zr2", "V", "Ga"]:
            val = atm.get(key)
            scores.append(1.0 if isinstance(val, (int, float)) and abs(val - ref_atm[key]) <= tol_atomic else 0.0)

        return sum(scores) / len(scores)


# === block: score_1 (check id='surface_results') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref_surface = ctx["ref_surface"]
        ref_terminations = ref_surface["terminations"]
        tol_disp = step["tolerances"]["displacement_A"]
        tol_mag = step["tolerances"]["magnetic_moment_mu_B"]
        term_scores = []

        for tkey, ref_term in ref_terminations.items():
            if tkey not in artifact:
                term_scores.append(0.0)
                continue
            art_term = artifact[tkey]

            art_disp = art_term.get("relaxation_displacements_A", [])
            ref_disp = ref_term["relaxation_displacements_A"]
            if ref_disp:
                disp_correct = sum(1 for a, ref in zip(art_disp, ref_disp)
                                   if isinstance(a, (int, float)) and abs(a - ref) <= tol_disp)
                disp_score = disp_correct / len(ref_disp)
            else:
                disp_score = 1.0 if len(art_disp) == 0 else 0.0

            art_mag = art_term.get("atomic_magnetic_moments_mu_B", [])
            ref_mag = ref_term["atomic_magnetic_moments_mu_B"]
            if ref_mag:
                mag_correct = sum(1 for a, ref in zip(art_mag, ref_mag)
                                  if isinstance(a, (int, float)) and abs(a - ref) <= tol_mag)
                mag_score = mag_correct / len(ref_mag)
            else:
                mag_score = 1.0 if len(art_mag) == 0 else 0.0

            half_met = art_term.get("half_metallic", True)
            half_score = 1.0 if half_met is False else 0.0
            term_score = (disp_score + mag_score) / 2.0 * half_score
            term_scores.append(term_score)

        return sum(term_scores) / len(term_scores) if term_scores else 0.0


_SCORERS = {
    'bulk_properties': score_0,
    'surface_results': score_1,
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
