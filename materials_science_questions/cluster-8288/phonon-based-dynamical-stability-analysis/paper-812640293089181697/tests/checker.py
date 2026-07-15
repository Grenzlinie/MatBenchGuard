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
    return {}


# === block: score_0 (check id='phonon_stability') ===
def score_0(artifact, step, ctx):
    materials = ["FeS", "MnS", "VS"]
    threshold = step.get("params", {}).get("imaginary_threshold_cm1", -10.0)
    count = 0
    if not isinstance(artifact, dict):
        return 0.0
    phonon = artifact.get("phonon", {})
    for mat in materials:
        mat_data = phonon.get(mat)
        if not isinstance(mat_data, dict):
            continue
        freqs_list = mat_data.get("frequencies")
        if not freqs_list:
            continue
        all_freqs = []
        for band in freqs_list:
            if isinstance(band, list):
                all_freqs.extend(band)
            elif isinstance(band, (int, float)):
                all_freqs.append(band)
        if not all_freqs:
            continue
        min_freq = min(all_freqs)
        if min_freq >= threshold:
            count += 1
    return count / 3


# === block: score_1 (check id='thermal_stability') ===
def score_1(artifact, step, ctx):
    def compute_total_drift(time_vals, energy_vals):
        if len(time_vals) < 3:
            return float('inf')
        n = len(time_vals)
        sx = sum(time_vals)
        sy = sum(energy_vals)
        sxy = sum(x*y for x, y in zip(time_vals, energy_vals))
        sx2 = sum(x*x for x in time_vals)
        denominator = n * sx2 - sx * sx
        if abs(denominator) < 1e-12:
            slope = 0.0
        else:
            slope = (n * sxy - sx * sy) / denominator
        time_range = time_vals[-1] - time_vals[0]
        drift = abs(slope * time_range)
        return drift
    max_drift = step.get("params", {}).get("max_drift_ev", 2.0)
    systems = ["FeS_673K", "VS_673K", "MnS_300K"]
    count = 0
    aimd = artifact.get("aimd_potential", {})
    for sys in systems:
        data = aimd.get(sys)
        if not isinstance(data, dict):
            continue
        t = data.get("time_ps")
        e = data.get("potential_energy_eV")
        if not t or not e or len(t) != len(e):
            continue
        drift = compute_total_drift(t, e)
        if drift < max_drift:
            count += 1
    return count / 3


# === block: score_2 (check id='mechanical_stability') ===
def score_2(artifact, step, ctx):
    materials = ["FeS", "MnS", "VS"]
    elastic = artifact.get("elastic_constants", {})
    count = 0
    for mat in materials:
        data = elastic.get(mat)
        if not isinstance(data, dict):
            continue
        c11 = data.get("c11")
        c12 = data.get("c12")
        c66 = data.get("c66")
        if c11 is None or c12 is None or c66 is None:
            continue
        if c66 > 0 and c11 > abs(c12):
            count += 1
    return count / 3


# === block: score_3 (check id='magnetic_moments') ===
def score_3(artifact, step, ctx):
    gold = step.get("params", {}).get("gold", {})
    tol = step.get("params", {}).get("tolerance", 0.2)
    materials = ["FeS", "MnS", "VS"]
    mag = artifact.get("magnetic_moments", {})
    count = 0
    for mat in materials:
        gold_mat = gold.get(mat, {})
        if not gold_mat:
            continue
        data = mag.get(mat)
        if not isinstance(data, dict):
            continue
        M = data.get("M_moment_muB")
        S = data.get("S_moment_muB")
        if M is None or S is None:
            continue
        if abs(M - gold_mat.get("M", 0.0)) <= tol and abs(S - gold_mat.get("S", 0.0)) <= tol:
            count += 1
    return count / 3


# === block: score_4 (check id='her_activity') ===
def score_4(artifact, step, ctx):
    threshold = step.get("params", {}).get("threshold_ev", 0.2)
    her = artifact.get("her_gibbs", {})
    count = 0
    targets = ["FeS", "VS"]
    for mat in targets:
        data = her.get(mat)
        if not isinstance(data, dict):
            continue
        dg_list = data.get("differential_dG_H")
        if not isinstance(dg_list, list) or not dg_list:
            continue
        try:
            min_abs = min(abs(v) for v in dg_list)
        except TypeError:
            continue
        if min_abs <= threshold:
            count += 1
    return count / 2


_SCORERS = {
    'phonon_stability': score_0,
    'thermal_stability': score_1,
    'mechanical_stability': score_2,
    'magnetic_moments': score_3,
    'her_activity': score_4,
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
