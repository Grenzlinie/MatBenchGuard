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
    return {}


# === block: score_0 (check id='step_band_gaps') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol_abs = step.get("tolerance_abs_eV", 0.2)
    if not isinstance(artifact, dict):
        return 0.0
    def score_one(key, gval):
        if key not in artifact:
            return 0.0
        val = artifact[key]
        if not isinstance(val, (int, float)):
            return 0.0
        diff = abs(val - gval)
        if diff <= tol_abs:
            return 1.0
        else:
            return max(0.0, 1.0 - (diff - tol_abs) / tol_abs)
    s1 = score_one("PBE_band_gap_eV", gold["PBE_band_gap_eV"])
    s2 = score_one("HSE06_band_gap_eV", gold["HSE06_band_gap_eV"])
    return (s1 + s2) / 2.0


# === block: score_1 (check id='step_defect_formation_energies') ===
def score_1(artifact, step, ctx):
    gold_list = step["gold"]
    tol_abs = step.get("tolerance_abs_eV", 0.15)
    if not isinstance(artifact, list):
        return 0.0
    artifact_lookup = {item["defect"]: item.get("energy_eV", None) for item in artifact if isinstance(item, dict) and "defect" in item}
    scores = []
    for gitem in gold_list:
        dname = gitem["defect"]
        gval = gitem["energy_eV"]
        aval = artifact_lookup.get(dname)
        if aval is None or not isinstance(aval, (int, float)):
            scores.append(0.0)
            continue
        diff = abs(aval - gval)
        if diff <= tol_abs:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol_abs) / tol_abs))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_diffusion_barriers') ===
def score_2(artifact, step, ctx):
    gold_list = step["gold"]
    tol_default = step.get("tolerance_mapping", {}).get("default", 0.1)
    low_thresh = step.get("tolerance_mapping", {}).get("low_barrier_threshold_eV", 0.1)
    low_tol = step.get("tolerance_mapping", {}).get("low_tolerance", 0.05)
    if not isinstance(artifact, list):
        return 0.0
    artifact_lookup = {}
    for item in artifact:
        if isinstance(item, dict) and "defect" in item and "direction" in item:
            key = (item["defect"], item["direction"])
            artifact_lookup[key] = item.get("barrier_eV", None)
    scores = []
    for gitem in gold_list:
        dname = gitem["defect"]
        ddir = gitem["direction"]
        gval = gitem["barrier_eV"]
        aval = artifact_lookup.get((dname, ddir))
        if aval is None or not isinstance(aval, (int, float)):
            scores.append(0.0)
            continue
        tol = low_tol if gval < low_thresh else tol_default
        diff = abs(aval - gval)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='step_mobility_conductivity') ===
def score_3(artifact, step, ctx):
    gold = step["gold"]
    tol_factor = step.get("tolerance_factor", 10.0)
    if not isinstance(artifact, dict):
        return 0.0
    keys = ["mobility_V_Li_minus_cm2_Vs", "mobility_p_plus_cm2_Vs", "ionic_conductivity_S_cm", "electronic_conductivity_S_cm"]
    scores = []
    for key in keys:
        gval = gold.get(key)
        aval = artifact.get(key)
        if aval is None or not isinstance(aval, (int, float)):
            scores.append(0.0)
            continue
        if aval <= 0 or gval <= 0:
            scores.append(1.0 if aval == gval else 0.0)
            continue
        factor = max(aval / gval, gval / aval)
        log_factor = math.log10(factor)
        log_tol = math.log10(tol_factor)
        log_max = 2 * log_tol
        if log_factor <= log_tol:
            scores.append(1.0)
        elif log_factor >= log_max:
            scores.append(0.0)
        else:
            scores.append(1.0 - (log_factor - log_tol) / (log_max - log_tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_band_gaps': score_0,
    'step_defect_formation_energies': score_1,
    'step_diffusion_barriers': score_2,
    'step_mobility_conductivity': score_3,
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
