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
    def prepare(outputs_dir, spec):
        ctx = {}
        for step in spec.get('steps', []):
            if step['id'] == 'step_03_formation_energies':
                ctx['target03'] = step.get('target')
            elif step['id'] == 'step_05_neb_barriers':
                ctx['target05'] = step.get('target')
        return ctx


# === block: score_0 (check id='step_03_formation_energies') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    t = ctx['target03']
    ref_c = t['stoichiometric_corner_ref']
    ref_e = t['stoichiometric_edge_ref']
    ref_dc = t['li_deficient_corner_ref']
    ref_de = t['li_deficient_edge_ref']
    tol_c = t['tolerance_abs']['stoichiometric_corner']
    tol_e = t['tolerance_abs']['stoichiometric_edge']
    tol_dc = t['tolerance_abs']['li_deficient_corner']
    tol_de = t['tolerance_abs']['li_deficient_edge']
    stoi_c = artifact.get('stoichiometric_corner_energy_eV')
    stoi_e = artifact.get('stoichiometric_edge_energy_eV')
    li_c = artifact.get('li_deficient_corner_energy_eV')
    li_e = artifact.get('li_deficient_edge_energy_eV')
    if any(v is None for v in [stoi_c, stoi_e, li_c, li_e]):
        return 0.0
    score = 0.0
    if li_c < stoi_c:
        score += 0.2
    if li_e < stoi_e:
        score += 0.2
    if li_c < li_e:
        score += 0.2
    if abs(stoi_c - ref_c) <= tol_c:
        score += 0.1
    if abs(stoi_e - ref_e) <= tol_e:
        score += 0.1
    if abs(li_c - ref_dc) <= tol_dc:
        score += 0.1
    if abs(li_e - ref_de) <= tol_de:
        score += 0.1
    return score


# === block: score_1 (check id='step_05_neb_barriers') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        t = ctx['target05']
        ref_wo = t['barrier_without_ref']
        ref_w = t['barrier_with_ref']
        tol = t['tolerance_abs']
        ptol = t['profile_max_tolerance']
        bar_wo = artifact.get('barrier_without_electron_eV')
        bar_w = artifact.get('barrier_with_electron_eV')
        prof_wo = artifact.get('energy_profile_without_electron_eV')
        prof_w = artifact.get('energy_profile_with_electron_eV')
        if None in (bar_wo, bar_w, prof_wo, prof_w):
            return 0.0
        if not isinstance(prof_wo, list) or not isinstance(prof_w, list) or len(prof_wo)==0 or len(prof_w)==0:
            return 0.0
        max_wo = max(prof_wo)
        max_w = max(prof_w)
        score = 0.0
        if bar_w < bar_wo:
            score += 0.3
        if abs(bar_wo - ref_wo) <= tol:
            score += 0.3
        if abs(bar_w - ref_w) <= tol:
            score += 0.2
        if abs(max_wo - bar_wo) <= ptol:
            score += 0.1
        if abs(max_w - bar_w) <= ptol:
            score += 0.1
        return score


_SCORERS = {
    'step_03_formation_energies': score_0,
    'step_05_neb_barriers': score_1,
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
