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
    return {'gold_props': spec['gold']['properties'], 'gold_dos': spec['gold']['dos']}


# === block: score_0 (check id='check_properties') ===
def score_0(artifact, step, ctx):
    import math

    gold_props = ctx['gold_props']
    artifact_polyms = artifact.get('polymorphs', [])

    gold_by_id = {p['polymorph_id']: p for p in gold_props}

    def within_tol(val, gold, tol_rel, tol_abs=0.0):
        if gold == 0:
            return abs(val) <= tol_abs
        return abs(val - gold) <= max(tol_rel * abs(gold), tol_abs)

    field_weights = {
        'Z': 0.1,
        'a': 0.2,
        'c': 0.1,
        'V_uc': 0.2,
        'ΔE_tot': 0.2,
        'ρ': 0.1,
        'B': 0.05,
        'ΔE_g': 0.05
    }

    tolerances = {
        'Z': ('exact', 0),
        'a': ('rel', 0.05),
        'c': ('rel', 0.05),
        'V_uc': ('rel', 0.10),
        'ΔE_tot': ('abs', 0.1),
        'ρ': ('rel', 0.10),
        'B': ('rel', 0.10),
        'ΔE_g': ('abs', 0.1)
    }

    scores = []
    for pm in artifact_polyms:
        pid = pm['polymorph_id']
        gold = gold_by_id.get(pid)
        if gold is None:
            continue
        fs = 0.0
        for field, w in field_weights.items():
            val = pm.get(field)
            gval = gold.get(field)
            if val is None or gval is None:
                if field == 'c' and val is None and gval is None:
                    fs += w
                continue
            tol_type, tol = tolerances[field]
            ok = False
            if tol_type == 'exact':
                ok = (val == gval)
            elif tol_type == 'rel':
                ok = within_tol(val, gval, tol)
            elif tol_type == 'abs':
                ok = within_tol(val, gval, 0.0, tol)
            if ok:
                fs += w
        scores.append(fs)

    if scores:
        base_score = sum(scores) / len(scores)
    else:
        base_score = 0.0

    # Trend checks
    trend_ok = True
    # V_uc should increase from id 1 to 6
    vols = [pm.get('V_uc') for pm in sorted(artifact_polyms, key=lambda x: x['polymorph_id']) if pm.get('V_uc') is not None]
    if len(vols) == 6:
        for i in range(1, len(vols)):
            if vols[i] <= vols[i-1]:
                trend_ok = False
                break
    else:
        trend_ok = False

    # ΔE_tot ordering: ids 1<2<5<6<4<3
    energy_order = [1,2,5,6,4,3]
    energies_dict = {pm['polymorph_id']: pm.get('ΔE_tot') for pm in artifact_polyms if pm.get('ΔE_tot') is not None}
    vals = [energies_dict.get(eid) for eid in energy_order]
    if None in vals:
        trend_ok = False
    else:
        for i in range(1, len(vals)):
            if vals[i] < vals[i-1]:
                trend_ok = False
                break

    trend_factor = 1.0 if trend_ok else 0.8

    score = base_score * trend_factor
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='check_dos') ===
def score_1(artifact, step, ctx):
    dos_gold = ctx['gold_dos']
    expected_vbm = dos_gold['expected_character']['VBM']
    expected_cbm = dos_gold['expected_character']['CBM']
    expected_match = dos_gold['match_paper']

    polymorphs = artifact.get('polymorphs', [])
    orb_match = artifact.get('orbital_character_matches_paper', False)

    correct = 0
    total = len(polymorphs)
    for pm in polymorphs:
        if pm.get('VBM_orbital') == expected_vbm and pm.get('CBM_orbital') == expected_cbm:
            correct += 1

    orb_score = correct / total if total > 0 else 0.0
    bool_score = 1.0 if orb_match == expected_match else 0.0
    score = 0.9 * orb_score + 0.1 * bool_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'check_properties': score_0,
    'check_dos': score_1,
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
