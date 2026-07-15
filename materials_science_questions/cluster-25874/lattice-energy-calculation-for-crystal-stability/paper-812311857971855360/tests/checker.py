import os
import json
import csv

# === author imports / helpers ===
import math
import json
import os


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


# === block: score_0 (check id='observed_energy') ===
def score_0(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', 'observed_lattice_energy.json')
    with open(artifact_path) as f:
        d = json.load(f)
    ref = step['reference']
    tol_total = step['tolerances']['total_abs']
    tol_comp_rel = step['tolerances']['component_rel']

    # total energy closeness score
    err_total = abs(d['total'] - ref['total'])
    if err_total <= tol_total:
        s_total = 1.0
    else:
        s_total = max(0.0, 1.0 - (err_total - tol_total) / tol_total)

    components = ['van_der_Waals', 'Coulombic', 'hydrogen_bond']
    comp_scores = []
    for c in components:
        t = abs(ref[c]) * tol_comp_rel
        err = abs(d[c] - ref[c])
        if err <= t:
            sc = 1.0
        else:
            sc = max(0.0, 1.0 - (err - t) / t)
        comp_scores.append(sc)
    s_comp = sum(comp_scores) / len(comp_scores)
    return 0.5 * s_total + 0.5 * s_comp


# === block: score_1 (check id='alternative_energy') ===
def score_1(artifact, step, ctx):
    # load alternative energy artifact
    artifact_path = os.path.join('/app/outputs', 'alternative_lattice_energy.json')
    with open(artifact_path) as f:
        d_alt = json.load(f)
    ref = step['reference']
    tol_total = step['tolerances']['total_abs']
    tol_comp_rel = step['tolerances']['component_rel']

    # component scores for alternative
    err_total = abs(d_alt['total'] - ref['total'])
    s_total_alt = 1.0 if err_total <= tol_total else max(0.0, 1.0 - (err_total - tol_total) / tol_total)
    components = ['van_der_Waals', 'Coulombic', 'hydrogen_bond']
    comp_scores = []
    for c in components:
        t = abs(ref[c]) * tol_comp_rel
        err = abs(d_alt[c] - ref[c])
        if err <= t:
            sc = 1.0
        else:
            sc = max(0.0, 1.0 - (err - t) / t)
        comp_scores.append(sc)
    s_comp_alt = sum(comp_scores) / len(comp_scores)

    # ordering checks
    obs_path = os.path.join('/app/outputs', 'observed_lattice_energy.json')
    if os.path.exists(obs_path):
        with open(obs_path) as f:
            d_obs = json.load(f)
        total_ordering = 1.0 if d_obs['total'] < d_alt['total'] else 0.0
        hbond_ordering = 1.0 if d_obs['hydrogen_bond'] < d_alt['hydrogen_bond'] else 0.0
    else:
        total_ordering = 0.0
        hbond_ordering = 0.0

    return 0.4 * s_total_alt + 0.3 * s_comp_alt + 0.15 * total_ordering + 0.15 * hbond_ordering


# === block: score_2 (check id='cell_params') ===
def score_2(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', 'minimized_cell_parameters.json')
    with open(artifact_path) as f:
        d = json.load(f)
    ref_obs = step['reference_observed']
    ref_alt = step['reference_alternative']
    tol_len = step['tolerances']['length_rel']
    tol_ang = step['tolerances']['angle_abs']

    lengths = ['a', 'b', 'c']
    angles = ['alpha', 'beta', 'gamma']
    scores = []

    for struct, ref in [('observed', ref_obs), ('alternative', ref_alt)]:
        if struct not in d:
            scores.extend([0.0] * 6)
            continue
        obj = d[struct]
        for l in lengths:
            r = ref[l]
            v = obj[l]
            rel_err = abs(v - r) / r if r != 0 else abs(v - r)
            if rel_err <= tol_len:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (rel_err - tol_len) / tol_len))
        for a in angles:
            r = ref[a]
            v = obj[a]
            abs_err = abs(v - r)
            if abs_err <= tol_ang:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (abs_err - tol_ang) / tol_ang))

    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'observed_energy': score_0,
    'alternative_energy': score_1,
    'cell_params': score_2,
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
