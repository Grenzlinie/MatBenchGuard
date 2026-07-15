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
    import json
    ctx = {}
    step = spec['steps'][0]
    ctx['delta_E'] = step['gold_delta_E']
    ctx['lattices'] = step['gold_lattices']
    ctx['energy_weight'] = step['energy_weight']
    ctx['lattice_weight'] = step['lattice_weight']
    ctx['tol_E_rel'] = step.get('tolerance_delta_E_rel', 0.15)
    ctx['tol_E_abs'] = step.get('tolerance_delta_E_abs', 10.0)
    ctx['tol_a'] = step.get('tolerance_lattice_a', 0.2)
    ctx['tol_ang'] = step.get('tolerance_lattice_angle', 2.0)
    ctx['tol_V'] = step.get('tolerance_volume', 10.0)
    return ctx


# === block: score_0 (check id='step_collect_results') ===
def score_0(artifact, step, ctx):
    gold_delta = ctx['delta_E']
    gold_lattices = ctx['lattices']
    w_energy = ctx['energy_weight']
    w_lattice = ctx['lattice_weight']
    tol_E_rel = ctx['tol_E_rel']
    tol_E_abs = ctx['tol_E_abs']
    tol_a = ctx['tol_a']
    tol_ang = ctx['tol_ang']
    tol_V = ctx['tol_V']
    conversion = 96.485
    if not isinstance(artifact, dict):
        return 0.0
    refs = artifact.get('references')
    compounds = artifact.get('compounds')
    if not isinstance(refs, dict) or not isinstance(compounds, list):
        return 0.0
    if 'FePO4' not in refs or 'total_energy_eV' not in refs['FePO4']:
        return 0.0
    E_FePO4 = refs['FePO4']['total_energy_eV']
    comp_by_A = {}
    for comp in compounds:
        A = comp.get('A')
        if A and 'total_energy_eV' in comp:
            comp_by_A[A] = comp
        else:
            return 0.0
    energy_scores = []
    latent_scores = []
    for A in ['Li','Na','K','NH4']:
        if A not in gold_delta:
            continue
        # energy
        if A not in refs or 'total_energy_eV' not in refs[A] or A not in comp_by_A:
            energy_scores.append(0.0)
        else:
            E_ref = refs[A]['total_energy_eV']
            E_comp = comp_by_A[A]['total_energy_eV']
            recomputed_delta = (E_comp - E_ref - E_FePO4) * conversion
            gold_val = gold_delta[A]
            tol = max(tol_E_abs, tol_E_rel * abs(gold_val))
            diff = abs(recomputed_delta - gold_val)
            score_e = max(0.0, 1.0 - diff / tol) if tol > 0 else (1.0 if diff == 0 else 0.0)
            energy_scores.append(score_e)
        # lattice
        lat_gold = gold_lattices.get(A)
        lat_comp = comp_by_A.get(A)
        if lat_gold and lat_comp:
            scores_lat = []
            for param in ['a','b','c']:
                val_comp = lat_comp.get(param)
                val_gold = lat_gold[param]
                if val_comp is not None:
                    diff_param = abs(val_comp - val_gold)
                    s = max(0.0, 1.0 - diff_param / tol_a)
                    scores_lat.append(s)
                else:
                    scores_lat.append(0.0)
            for param in ['alpha','beta','gamma']:
                val_comp = lat_comp.get(param)
                val_gold = lat_gold[param]
                if val_comp is not None:
                    diff_ang = abs(val_comp - val_gold)
                    s = max(0.0, 1.0 - diff_ang / tol_ang)
                    scores_lat.append(s)
                else:
                    scores_lat.append(0.0)
            V_comp = lat_comp.get('V')
            V_gold = lat_gold['V']
            if V_comp is not None:
                diff_V = abs(V_comp - V_gold)
                s_V = max(0.0, 1.0 - diff_V / tol_V)
                scores_lat.append(s_V)
            else:
                scores_lat.append(0.0)
            if scores_lat:
                latent_scores.append(sum(scores_lat) / len(scores_lat))
            else:
                latent_scores.append(0.0)
        else:
            latent_scores.append(0.0)
    energy_score = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0
    lattice_score = sum(latent_scores) / len(latent_scores) if latent_scores else 0.0
    total = w_energy * energy_score + w_lattice * lattice_score
    return total


_SCORERS = {
    'step_collect_results': score_0,
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
