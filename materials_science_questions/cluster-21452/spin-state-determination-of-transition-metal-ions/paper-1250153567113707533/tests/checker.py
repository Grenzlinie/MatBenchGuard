import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
    def prepare(outputs_dir, spec):
        golds = {}
        for step in spec.get('steps', []):
            sid = step['id']
            if 'gold' in step:
                golds[sid] = step['gold']
        return {'golds': golds}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        golds = ctx.get('golds', {})
        gold = golds.get(step.get('id', ''), {})
        if not gold:
            return 0.0
        entries = artifact if isinstance(artifact, list) else []
        if not entries:
            return 0.0
        metals = ['Mn', 'Co', 'Ni']
        by_metal = {}
        for e in entries:
            m = e.get('metal')
            if m is None:
                continue
            if m not in metals:
                continue
            if m not in by_metal:
                by_metal[m] = []
            by_metal[m].append(e)
        for m in metals:
            if m not in by_metal or not by_metal[m]:
                return 0.0

        total_score = 0.0
        for metal in metals:
            metal_gold = gold.get(metal, {})
            expected_ground = metal_gold.get('expected_ground', '')
            other_states = metal_gold.get('other_states', [])
            entries_metal = by_metal[metal]
            ground_entry = None
            others_found = {}
            for e in entries_metal:
                en_raw = e.get('relative_energy_cm1')
                try:
                    en = float(en_raw)
                except (TypeError, ValueError):
                    en = None
                if en is not None and math.isclose(en, 0.0, abs_tol=1e-9):
                    ground_entry = e
                else:
                    sp = e.get('spin_state', '')
                    if sp is None:
                        sp = ''
                    sp = sp.strip().lower()
                    for ospec in other_states:
                        target_spin = ospec.get('spin', '').strip().lower()
                        if target_spin and target_spin in sp:
                            others_found[target_spin] = e
            score_metal = 0.0
            if ground_entry is not None:
                gs = ground_entry.get('spin_state', '')
                if gs is not None:
                    gs = gs.strip().lower()
                    if expected_ground in gs:
                        score_metal += 0.4
            num_other = len(other_states)
            if num_other == 0:
                score_metal += 0.6
            else:
                each_weight = 0.6 / num_other
                for ospec in other_states:
                    target = ospec.get('spin', '').strip().lower()
                    ref_en_raw = ospec.get('ref_energy')
                    tol_raw = ospec.get('tolerance')
                    try:
                        ref_en = float(ref_en_raw)
                    except (TypeError, ValueError):
                        continue
                    try:
                        tol = float(tol_raw)
                    except (TypeError, ValueError):
                        tol = 0.0
                    other_entry = others_found.get(target)
                    if other_entry is None:
                        continue
                    en_raw2 = other_entry.get('relative_energy_cm1')
                    try:
                        en = float(en_raw2)
                    except (TypeError, ValueError):
                        en = None
                    if en is not None and abs(en - ref_en) <= tol:
                        score_metal += each_weight
            total_score += score_metal
        return total_score / len(metals)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['golds'].get(step['id'], {})
        if not gold:
            return 0.0
        entries = artifact if isinstance(artifact, list) else []
        by_metal = {}
        for e in entries:
            m = e.get('metal', '')
            if m not in by_metal:
                by_metal[m] = {}
            coord = e.get('coordination')
            if coord is not None:
                by_metal[m][coord] = e.get('relative_energy_cm1')
        metals = ['Co', 'Cu', 'Zn']
        if not all(m in by_metal for m in metals):
            return 0.0
        total_score = 0.0
        for metal in metals:
            metal_gold = gold.get(metal, {})
            refs = metal_gold.get('reference', {})
            tols = metal_gold.get('tolerances', {})
            coords_present = by_metal[metal]
            # check coordination=5 is zero
            en5 = coords_present.get(5)
            if en5 is None or not math.isclose(en5, 0.0, abs_tol=tols.get(5, 1.0)):
                continue
            # check coordination=6 is within tolerance of ref and >0
            en6 = coords_present.get(6)
            if en6 is None or abs(en6 - refs.get(6, 9999)) > tols.get(6, 9999):
                continue
            # check coordination=4 is within tolerance and >6
            en4 = coords_present.get(4)
            if en4 is None or abs(en4 - refs.get(4, 99999)) > tols.get(4, 99999):
                continue
            if not (en4 > en6 > en5):
                continue
            total_score += 1.0
        return total_score / len(metals)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold = ctx['golds'].get(step['id'], {})
        if not gold:
            return 0.0
        entries = artifact if isinstance(artifact, list) else []
        by_metal = {}
        for e in entries:
            m = e.get('metal', '')
            if m not in by_metal:
                by_metal[m] = {}
            coord = e.get('coordination')
            freq = e.get('frequency_cm1')
            if coord is not None and freq is not None:
                by_metal[m][coord] = freq
        metals = ['Co', 'Cu', 'Zn']
        if not all(m in by_metal for m in metals):
            return 0.0
        total_score = 0.0
        for metal in metals:
            metal_gold = gold.get(metal, {})
            ref_freqs = metal_gold.get('freqs', {})
            tol = metal_gold.get('tolerance', 50.0)
            present = by_metal[metal]
            f6 = present.get(6)
            f5 = present.get(5)
            f4 = present.get(4)
            if None in (f6, f5, f4):
                continue
            # ordering check: hexa < penta < tetra with at least 5 cm-1 step
            if not (f6 + 4.99 <= f5 <= f4 - 4.99):
                continue
            # optional numeric agreement within tolerance
            match = True
            for c in [6, 5, 4]:
                if abs(present[c] - ref_freqs.get(str(c), 0)) > tol:
                    match = False
                    break
            if match:
                total_score += 1.0
        return total_score / len(metals)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
