import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, collections


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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    cols = set(artifact[0].keys()) if artifact else set()
    required = {'strain_a','strain_b','adsorbate','E_form'}
    if not required.issubset(cols):
        return 0.0
    if len(artifact) != 726:
        return 0.0
    return 1.0


# === block: score_1 (check id='relative_formation_energies') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    formation_path = '/app/outputs/formation_energies.csv'
    if not os.path.exists(formation_path):
        return 0.0
    with open(formation_path, newline='') as f:
        form_rows = list(csv.DictReader(f))
    form = {}
    for r in form_rows:
        key = (r['strain_a'].strip(), r['strain_b'].strip(), r['adsorbate'].strip())
        try:
            form[key] = float(r['E_form'])
        except:
            return 0.0
    refs = {}
    for (sa, sb, ad), e in form.items():
        if sa == '0' and sb == '0':
            refs[ad] = e
    rel = artifact
    if rel is None or len(rel) == 0:
        return 0.0
    mismatches = 0
    total_rows = 0
    trend_points = []
    for row in rel:
        sa = row['strain_a'].strip()
        sb = row['strain_b'].strip()
        ad = row['adsorbate'].strip()
        try:
            delta_reported = float(row['delta_E_form'])
        except:
            return 0.0
        if ad not in refs:
            return 0.0
        e_strain = form.get((sa, sb, ad))
        if e_strain is None:
            return 0.0
        computed_delta = e_strain - refs[ad]
        if abs(delta_reported - computed_delta) > 1e-4:
            mismatches += 1
        total_rows += 1
        try:
            sa_int = int(sa)
            sb_int = int(sb)
        except:
            continue
        if sa_int <= -5 and sb_int >= 5 and ad in ('OCCOH', 'CHO'):
            trend_points.append((sa, sb, ad, computed_delta))
    consistency_score = 1.0 if mismatches == 0 else 0.0
    pair_deltas = {}
    for sa, sb, ad, delta in trend_points:
        key2 = (sa, sb)
        if key2 not in pair_deltas:
            pair_deltas[key2] = {}
        pair_deltas[key2][ad] = delta
    satisfied = 0
    total_pairs = 0
    for (sa, sb), deltas in pair_deltas.items():
        if 'OCCOH' in deltas and 'CHO' in deltas:
            total_pairs += 1
            if deltas['OCCOH'] < deltas['CHO']:
                satisfied += 1
    if total_pairs == 0:
        trend_frac = 0.0
    else:
        trend_frac = satisfied / total_pairs
    final_score = 0.2 * consistency_score + 0.8 * trend_frac
    return final_score


# === block: score_2 (check id='activation_energies') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = step['gold']
    tolerance = step['tolerance_abs']
    gold_dict = {}
    for g in gold:
        gold_dict[(g['surface'], g['reaction'])] = (float(g['barrier']), float(g['reaction_energy']))
    correct_values = 0
    total_values = 2 * len(gold_dict)
    for row in artifact:
        surface = row['surface'].strip()
        reaction = row['reaction'].strip()
        try:
            barrier = float(row['barrier'])
            reaction_e = float(row['reaction_energy'])
        except:
            continue
        gold_entry = gold_dict.get((surface, reaction))
        if gold_entry is not None:
            if abs(barrier - gold_entry[0]) <= tolerance:
                correct_values += 1
            if abs(reaction_e - gold_entry[1]) <= tolerance:
                correct_values += 1
    score = correct_values / total_values if total_values > 0 else 0.0
    return score


_SCORERS = {
    'formation_energies': score_0,
    'relative_formation_energies': score_1,
    'activation_energies': score_2,
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
