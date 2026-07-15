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


# === block: score_0 (check id='binding_energies_check') ===
def score_0(artifact, step, ctx):
    art = artifact  # list of dicts
    step = step or {}
    gold_rows = step.get('gold', [])
    tols = step.get('tolerances', {})
    cons_eps = step.get('consistency_eps', 0.01)

    if not isinstance(art, list) or not gold_rows:
        return 0.0

    # build a dict keyed by (impurity, surface) for the artifact
    art_map = {}
    for row in art:
        try:
            imp = str(row['impurity']).strip().upper()
            surf = str(row['surface']).strip().upper()
            art_map[(imp, surf)] = {
                'binding_energy': float(row['binding_energy']),
                'mechanical': float(row['mechanical']),
                'chemical': float(row['chemical'])
            }
        except (KeyError, ValueError):
            continue

    num_ok = 0
    for g in gold_rows:
        key = (g['impurity'].upper(), g['surface'].upper())
        a = art_map.get(key)
        if a is None:
            continue
        be_ok = abs(a['binding_energy'] - g['binding_energy']) <= tols.get('binding_energy', 0.1)
        me_ok = abs(a['mechanical'] - g['mechanical']) <= tols.get('mechanical', 0.15)
        ch_ok = abs(a['chemical'] - g['chemical']) <= tols.get('chemical', 0.15)
        if be_ok and me_ok and ch_ok:
            num_ok += 1

    value_score = num_ok / len(gold_rows) if gold_rows else 0.0

    # consistency: binding_energy approx mechanical+chemical
    cons_ok = 0
    for a in art_map.values():
        if abs(a['binding_energy'] - (a['mechanical'] + a['chemical'])) <= cons_eps:
            cons_ok += 1
    cons_ratio = cons_ok / max(len(art_map), 1)

    # weight: 0.8 for value match, 0.2 for consistency
    score = 0.8 * value_score + 0.2 * cons_ratio
    return float(max(0.0, min(1.0, score)))


# === block: score_1 (check id='strengthening_energies_check') ===
def score_1(artifact, step, ctx):
    art = artifact  # list of dicts
    step = step or {}
    gold_rows = step.get('gold', [])
    tol = step.get('tolerance', 0.05)

    if not isinstance(art, list) or not gold_rows:
        return 0.0

    art_map = {}
    for row in art:
        try:
            imp = str(row['impurity']).strip().upper()
            val = float(row['delta_EB'])
            art_map[imp] = val
        except (KeyError, ValueError):
            continue

    total = 0
    for g in gold_rows:
        imp = g['impurity'].upper()
        gold_val = g['delta_EB']
        exp_sign = g['expected_sign']
        a = art_map.get(imp)
        if a is None:
            continue
        # check value within tolerance and sign matches expected
        if abs(a - gold_val) <= tol and ((a > 0 and exp_sign == 1) or (a < 0 and exp_sign == -1) or (abs(a) <= 1e-6 and exp_sign == 0)):
            total += 1

    score = total / len(gold_rows) if gold_rows else 0.0
    return float(max(0.0, min(1.0, score)))


_SCORERS = {
    'binding_energies_check': score_0,
    'strengthening_energies_check': score_1,
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
