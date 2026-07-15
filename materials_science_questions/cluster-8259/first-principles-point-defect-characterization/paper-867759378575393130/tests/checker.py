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


# === block: score_0 (check id='check_antimonene_data') ===
def score_0(artifact, step, ctx):
    structures = artifact.get('structures', None)
    if not isinstance(structures, list) or len(structures) != 6:
        return 0.0

    gold = {s['name']: s for s in step['structures_gold']}
    tol = step['tolerances']
    field_low_w = step['field_weights']['low']
    field_high_w = step['field_weights']['high']
    trend_form_w = step['trend_weights']['formation_ordering']
    trend_bg_w = step['trend_weights']['band_gap_lowering']

    total_score = 0.0
    for struct in structures:
        name = struct.get('name')
        if name not in gold:
            continue
        g = gold[name]
        for field in ['diameter_ang', 'tube_length_ang', 'd_Sb_Sb_min_ang', 'd_Sb_Sb_max_ang', 'orientation_angle_deg', 'formation_energy_eV', 'band_gap_eV']:
            val = struct.get(field)
            if val is None:
                continue
            gold_val = g.get(field, None)
            if gold_val is None:
                continue
            diff = abs(val - gold_val)
            if diff <= tol[field]:
                if field in ('formation_energy_eV', 'band_gap_eV'):
                    total_score += field_high_w
                else:
                    total_score += field_low_w

    # formation energy ordering
    sw1_zb = next((s for s in structures if s.get('name') == 'SW1-ZbNT'), None)
    sw2_zb = next((s for s in structures if s.get('name') == 'SW2-ZbNT'), None)
    if sw1_zb and sw2_zb and sw1_zb.get('formation_energy_eV', 0) < sw2_zb.get('formation_energy_eV', 0):
        total_score += trend_form_w

    sw1_ab = next((s for s in structures if s.get('name') == 'SW1-ASbNT'), None)
    sw2_ab = next((s for s in structures if s.get('name') == 'SW2-ASbNT'), None)
    if sw1_ab and sw2_ab and sw1_ab.get('formation_energy_eV', 0) < sw2_ab.get('formation_energy_eV', 0):
        total_score += trend_form_w

    # band gap lowering: each defective vs pristine
    zb_pristine = next((s for s in structures if s.get('name') == 'ZbNT'), None)
    ab_pristine = next((s for s in structures if s.get('name') == 'ASbNT'), None)
    if zb_pristine:
        for def_name in ['SW1-ZbNT', 'SW2-ZbNT']:
            def_s = next((s for s in structures if s.get('name') == def_name), None)
            if def_s and def_s.get('band_gap_eV', None) is not None and zb_pristine.get('band_gap_eV', None) is not None:
                if def_s['band_gap_eV'] < zb_pristine['band_gap_eV']:
                    total_score += trend_bg_w
    if ab_pristine:
        for def_name in ['SW1-ASbNT', 'SW2-ASbNT']:
            def_s = next((s for s in structures if s.get('name') == def_name), None)
            if def_s and def_s.get('band_gap_eV', None) is not None and ab_pristine.get('band_gap_eV', None) is not None:
                if def_s['band_gap_eV'] < ab_pristine['band_gap_eV']:
                    total_score += trend_bg_w

    return min(1.0, total_score)


_SCORERS = {
    'check_antimonene_data': score_0,
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
