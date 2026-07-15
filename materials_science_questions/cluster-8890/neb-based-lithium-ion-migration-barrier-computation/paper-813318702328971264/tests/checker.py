import os
import json
import csv

# === author imports / helpers ===
import csv, math
from collections import defaultdict


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


# === block: score_0 (check id='step_01_energies') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gb = artifact.get("grain_boundary_energy")
    se = artifact.get("surface_energy")
    wc = artifact.get("work_of_cohesion")
    gold_gb = step.get("gold_grain_boundary_energy", 0.09)
    tol_gb = step.get("tol_grain_boundary_energy", 0.03)
    gold_se = step.get("gold_surface_energy", 0.92)
    tol_se = step.get("tol_surface_energy", 0.15)
    gold_wc = step.get("gold_work_of_cohesion", 1.75)
    tol_wc = step.get("tol_work_of_cohesion", 0.15)
    score_gb = 1.0 if (gb is not None and abs(gb - gold_gb) <= tol_gb) else 0.0
    score_se = 1.0 if (se is not None and abs(se - gold_se) <= tol_se) else 0.0
    score_wc = 1.0 if (wc is not None and abs(wc - gold_wc) <= tol_wc) else 0.0
    rel_ok = 0.0
    if gb is not None and se is not None and wc is not None:
        expected = 2 * se - gb
        if abs(wc - expected) <= 0.15:
            rel_ok = 1.0
    return 0.25 * score_gb + 0.25 * score_se + 0.25 * score_wc + 0.25 * rel_ok


# === block: score_1 (check id='step_02_barriers') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = artifact
    data = {}
    for row in rows:
        try:
            dist = float(row.get("distance_from_interface", ""))
            mech = str(row.get("mechanism", "")).strip()
            ener = float(row.get("activation_energy", ""))
        except (ValueError, TypeError):
            continue
        data[(dist, mech)] = ener

    bulk_oo = step.get("bulk_oo_target", 0.74)
    tol_bulk_oo = step.get("tol_bulk_oo", 0.1)
    bulk_oto = step.get("bulk_oto_target", 0.23)
    tol_bulk_oto = step.get("tol_bulk_oto", 0.1)
    boundary_oo_max = step.get("boundary_oo_max", 1.0)
    tol_oo_max = step.get("tol_oo_max", 0.15)
    boundary_oto_max = step.get("boundary_oto_max", 0.46)
    tol_oto_max = step.get("tol_oto_max", 0.15)

    expected_dists = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
    mechanisms = ["O-O", "O-T-O_boundary_vac", "O-T-O_bulk_vac"]

    present = sum(1 for d in expected_dists for m in mechanisms if (d,m) in data)
    total = len(expected_dists) * len(mechanisms)
    completeness = present / total if total>0 else 0.0

    def check_monotonic(vals, dists):
        m = len(vals)
        if m < 2:
            return 1.0
        violations = sum(1 for i in range(m-1) if vals[i] + 1e-6 < vals[i+1])
        return 1.0 - violations / (m-1)

    mono_scores = []
    for mech in mechanisms:
        mech_data = sorted([(d,data[(d,mech)]) for d in expected_dists if (d,mech) in data], key=lambda x: x[0])
        if not mech_data:
            continue
        dists = [x[0] for x in mech_data]
        energies = [x[1] for x in mech_data]
        mono_scores.append(check_monotonic(energies, dists))
    monotonic_score = sum(mono_scores)/len(mono_scores) if mono_scores else 0.0

    bulk_match_oo = 0.0
    if (1.2, "O-O") in data:
        if abs(data[(1.2, "O-O")] - bulk_oo) <= tol_bulk_oo:
            bulk_match_oo = 1.0
    elif (1.0, "O-O") in data:
        if abs(data[(1.0, "O-O")] - bulk_oo) <= tol_bulk_oo:
            bulk_match_oo = 1.0

    bulk_match_oto = 0.0
    for mech in ["O-T-O_boundary_vac", "O-T-O_bulk_vac"]:
        if (1.2, mech) in data:
            if abs(data[(1.2, mech)] - bulk_oto) <= tol_bulk_oto:
                bulk_match_oto += 0.5
        elif (1.0, mech) in data:
            if abs(data[(1.0, mech)] - bulk_oto) <= tol_bulk_oto:
                bulk_match_oto += 0.5
    bulk_match_oto = min(bulk_match_oto, 1.0)
    bulk_score = (bulk_match_oo + bulk_match_oto) / 2.0

    boundary_oo_ok = 0.0
    if (0.0, "O-O") in data:
        if abs(data[(0.0, "O-O")] - boundary_oo_max) <= tol_oo_max:
            boundary_oo_ok = 1.0

    boundary_oto_ok = 0.0
    for mech in ["O-T-O_boundary_vac", "O-T-O_bulk_vac"]:
        if (0.0, mech) in data:
            if abs(data[(0.0, mech)] - boundary_oto_max) <= tol_oto_max:
                boundary_oto_ok += 0.5
    boundary_oto_ok = min(boundary_oto_ok, 1.0)
    boundary_score = (boundary_oo_ok + boundary_oto_ok) / 2.0

    plausible_count = sum(1 for v in data.values() if 0.1 <= v <= 1.5)
    plaus_score = plausible_count / max(len(data), 1)

    score = 0.1*completeness + 0.25*monotonic_score + 0.15*bulk_score + 0.15*boundary_score + 0.15*plaus_score
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'step_01_energies': score_0,
    'step_02_barriers': score_1,
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
