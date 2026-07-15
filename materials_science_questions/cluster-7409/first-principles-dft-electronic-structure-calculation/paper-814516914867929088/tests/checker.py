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


# === block: score_0 (check id='energy_ordering') ===
def score_0(artifact, step, ctx):
    nearest_e = artifact['nearest_fm']['total_energy_eV']
    next_e = artifact['nextnearest_fm']['total_energy_eV']
    afm_e = artifact['afm_nearest']['total_energy_eV']
    cond1 = nearest_e < next_e
    cond2 = afm_e - nearest_e > 0
    score = (float(cond1) + float(cond2)) * 0.5
    return score


# === block: score_1 (check id='lattice_parameters') ===
def score_1(artifact, step, ctx):
    a = artifact['nearest_fm']['a_Ang']
    c = artifact['nearest_fm']['c_Ang']
    target_a = step['target_a']
    target_c = step['target_c']
    tol_a = step.get('tolerance_a', 0.02)
    tol_c = step.get('tolerance_c', 0.02)
    def lin_score(val, target, tol):
        if tol <= 0:
            return 1.0
        return max(0.0, 1.0 - abs(val - target) / tol)
    s_a = lin_score(a, target_a, tol_a)
    s_c = lin_score(c, target_c, tol_c)
    score = (s_a + s_c) / 2.0
    return score


# === block: score_2 (check id='magnetic_moments') ===
def score_2(artifact, step, ctx):
    total = artifact['nearest_fm']['total_moment_muB']
    ti = artifact['nearest_fm']['ti_moment_muB']
    ce = artifact['nearest_fm']['ce_moment_muB']
    target_total = step['target_total_moment_muB']
    target_ti = step['target_ti_moment_muB']
    target_ce = step['target_ce_moment_muB']
    tol = step.get('tolerance_muB', 0.05)
    def lin_score(val, target, tol):
        if tol <= 0:
            return 1.0
        return max(0.0, 1.0 - abs(val - target) / tol)
    s_total = lin_score(total, target_total, tol)
    s_ti = lin_score(ti, target_ti, tol)
    s_ce = lin_score(ce, target_ce, tol)
    score = (s_total + s_ti + s_ce) / 3.0
    return score


# === block: score_3 (check id='dos_intermediate_band') ===
def score_3(artifact, step, ctx):
    dos = artifact['dos']
    energy = dos['energy_list']
    ti_pdos = dos['pdos_ti_3d']
    ce_pdos = dos['pdos_ce_4f']
    n_pdos = dos['pdos_n_2p']
    al_pdos = dos['pdos_al_3p']
    n_pts = len(energy)
    if n_pts == 0:
        return 0.0
    total_pdos = [ti_pdos[i] + ce_pdos[i] + n_pdos[i] + al_pdos[i] for i in range(n_pts)]
    max_total = max(total_pdos)
    if max_total <= 0.0:
        return 0.0
    noise = max_total * step.get('noise_floor_ratio', 0.01)
    ratio_thresh = step.get('ratio_threshold', 0.3)
    for i in range(n_pts):
        t = total_pdos[i]
        if t > noise:
            r = (ti_pdos[i] + ce_pdos[i]) / t
            if r >= ratio_thresh:
                return 1.0
    return 0.0


_SCORERS = {
    'energy_ordering': score_0,
    'lattice_parameters': score_1,
    'magnetic_moments': score_2,
    'dos_intermediate_band': score_3,
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
