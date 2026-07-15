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
    gold_surfaces = spec.get('gold_reference', {}).get('surfaces', [])
    gold = {s['name']: s for s in gold_surfaces}
    return {'gold': gold}


# === block: score_0 (check id='main_results') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0

    # map agent entries
    agent = {}
    for entry in data:
        surf = entry.get('surface', '').strip()
        if surf in ['Mo2B2','Cr2B2','Fe2B2','Mn2B2','Cu(111)']:
            agent[surf] = entry

    if len(agent) < 5:
        return 0.0

    # --- Trend 1: adsorption energy ordering ---
    # Should be more negative (lower) in this order: Mo2B2 < Cr2B2 < {Mn2B2, Fe2B2} < Cu(111)
    pairs_t1 = [
        ('Mo2B2','Cr2B2'),
        ('Cr2B2','Mn2B2'),
        ('Cr2B2','Fe2B2'),
        ('Mo2B2','Mn2B2'),
        ('Mo2B2','Fe2B2'),
        ('Mo2B2','Cu(111)'),
        ('Cr2B2','Cu(111)'),
        ('Mn2B2','Cu(111)'),
        ('Fe2B2','Cu(111)')
    ]
    t1_correct = 0
    for a, b in pairs_t1:
        v_a = agent[a].get('adsorption_energy')
        v_b = agent[b].get('adsorption_energy')
        if v_a is not None and v_b is not None and v_a < v_b:
            t1_correct += 1
    score1 = t1_correct / len(pairs_t1)

    # --- Trend 2: OCO angles ---
    # All MBenes: angle < 180°; Cu(111): angle within 5° of 180
    mbene_surf = ['Mo2B2','Cr2B2','Fe2B2','Mn2B2']
    score2_parts = []
    for surf in mbene_surf:
        ang = agent[surf].get('OCO_angle')
        if ang is not None and ang < 180:
            score2_parts.append(1.0)
        else:
            score2_parts.append(0.0)
    cu_ang = agent['Cu(111)'].get('OCO_angle')
    if cu_ang is not None and abs(cu_ang - 180) <= 5:
        score2_parts.append(1.0)
    else:
        score2_parts.append(0.0)
    score2 = sum(score2_parts) / len(score2_parts)

    # --- Trend 3: CHO free energy change lower on Mo2B2 and Cr2B2 ---
    # check Mo2B2 < Fe2B2, Mn2B2, Cu(111)  and Cr2B2 < Fe2B2, Mn2B2, Cu(111)
    pairs_t3 = [
        ('Mo2B2','Fe2B2'),
        ('Mo2B2','Mn2B2'),
        ('Mo2B2','Cu(111)'),
        ('Cr2B2','Fe2B2'),
        ('Cr2B2','Mn2B2'),
        ('Cr2B2','Cu(111)')
    ]
    t3_correct = 0
    for a, b in pairs_t3:
        v_a = agent[a].get('CHO_free_energy_change')
        v_b = agent[b].get('CHO_free_energy_change')
        if v_a is not None and v_b is not None and v_a < v_b:
            t3_correct += 1
    score3 = t3_correct / len(pairs_t3)

    # --- Trend 4: HER free energy more negative on Mo2B2 and Cr2B2 ---
    # check Mo2B2 < Fe2B2, Mn2B2, Cu(111)  and Cr2B2 < Fe2B2, Mn2B2, Cu(111)
    pairs_t4 = [
        ('Mo2B2','Fe2B2'),
        ('Mo2B2','Mn2B2'),
        ('Mo2B2','Cu(111)'),
        ('Cr2B2','Fe2B2'),
        ('Cr2B2','Mn2B2'),
        ('Cr2B2','Cu(111)')
    ]
    t4_correct = 0
    for a, b in pairs_t4:
        v_a = agent[a].get('HER_free_energy_change')
        v_b = agent[b].get('HER_free_energy_change')
        if v_a is not None and v_b is not None and v_a < v_b:
            t4_correct += 1
    score4 = t4_correct / len(pairs_t4)

    overall = (score1 + score2 + score3 + score4) / 4
    return overall


_SCORERS = {
    'main_results': score_0,
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
