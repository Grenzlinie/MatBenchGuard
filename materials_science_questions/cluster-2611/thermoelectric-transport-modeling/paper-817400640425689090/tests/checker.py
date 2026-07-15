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
    gold_pf = spec.get('gold_pf', {})
    gold_zt = spec.get('gold_zt', {})
    ring_gold = spec.get('ring_gold', {})
    return {'gold_pf': gold_pf, 'gold_zt': gold_zt, 'ring_gold': ring_gold}


# === block: score_0 (check id='pf_compare') ===
def score_0(artifact, step, ctx):
    entries = artifact
    gold_pf = ctx['gold_pf']
    tol = 1.0 - step.get('tolerance', 0.15)
    scoring = []
    for mat_sct, gold_val in gold_pf.items():
        gold_val = gold_val / 1000.0  # convert from mW/m-K² to W/m-K² to match output contract
        mat, sct = mat_sct.split('|', 1)
        entry = next((e for e in entries if e.get('material')==mat and e.get('scattering')==sct), None)
        if entry is None or entry.get('peak_pf') is None:
            scoring.append(0.0)
        else:
            val = entry['peak_pf']
            score = min(1.0, max(0.0, val / (gold_val * tol))) if gold_val > 0 else (1.0 if val <= gold_val else 0.0)
            scoring.append(score)
    return sum(scoring) / len(scoring) if scoring else 0.0


# === block: score_1 (check id='zt_compare') ===
def score_1(artifact, step, ctx):
    entries = artifact
    gold_zt = ctx['gold_zt']
    tol = 1.0 - step.get('tolerance', 0.10)
    scoring = []
    for mat_sct, gold_val in gold_zt.items():
        mat, sct = mat_sct.split('|', 1)
        entry = next((e for e in entries if e.get('material')==mat and e.get('scattering')==sct), None)
        if entry is None or entry.get('peak_zt') is None:
            scoring.append(0.0)
        else:
            val = entry['peak_zt']
            score = min(1.0, max(0.0, val / (gold_val * tol))) if gold_val > 0 else (1.0 if val <= gold_val else 0.0)
            scoring.append(score)
    return sum(scoring) / len(scoring) if scoring else 0.0


# === block: score_2 (check id='ring_energies') ===
def score_2(artifact, step, ctx):
    entries = artifact
    ring_gold = ctx['ring_gold']
    tol = step.get('tolerance', 0.01)
    score = 0.0
    count = 0
    for mat, gold_dict in ring_gold.items():
        entry = next((e for e in entries if e.get('material')==mat), None)
        if entry is None:
            continue
        ok = True
        for field in ['inner_ring_energy', 'outer_ring_energy', 'moat_energy']:
            val = entry.get(field)
            if val is None or abs(val - gold_dict[field]) > tol:
                ok = False
        score += 1.0 if ok else 0.0
        count += 1
    return score / count if count > 0 else 0.0


# === block: score_3 (check id='pf_ordering') ===
def score_3(artifact, step, ctx):
    entries = artifact
    orders = {
        '1QL Bi2Te3': {'dos': '>', 'others': ['cmfp','crt']},
        '1QL Bi2Se3': {'dos': '>', 'others': ['cmfp','crt']},
        '1QL Sb2Te3': {'dos': '<', 'others': ['cmfp','crt']}
    }
    score = 0.0
    count = 0
    for mat, cond in orders.items():
        dos_entry = next((e for e in entries if e['material']==mat and e['scattering']=='dos'), None)
        cmfp_entry = next((e for e in entries if e['material']==mat and e['scattering']=='cmfp'), None)
        crt_entry = next((e for e in entries if e['material']==mat and e['scattering']=='crt'), None)
        if dos_entry is None or cmfp_entry is None or crt_entry is None:
            continue
        dos_pf = dos_entry['peak_pf']
        cmfp_pf = cmfp_entry['peak_pf']
        crt_pf = crt_entry['peak_pf']
        if cond['dos'] == '>':
            ok = dos_pf > cmfp_pf and dos_pf > crt_pf
        else:
            ok = dos_pf < cmfp_pf and dos_pf < crt_pf
        score += 1.0 if ok else 0.0
        count += 1
    return score / count if count > 0 else 0.0


_SCORERS = {
    'pf_compare': score_0,
    'zt_compare': score_1,
    'ring_energies': score_2,
    'pf_ordering': score_3,
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
