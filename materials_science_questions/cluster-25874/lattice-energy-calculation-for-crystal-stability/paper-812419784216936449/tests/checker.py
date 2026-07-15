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
    step = spec['steps'][0]
    return {
        'gold': step['gold'],
        'tolerances': step['tolerances'],
        'sub_weights': step.get('sub_weights', {})
    }


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    step_gold = ctx['gold']
    step_tolerances = ctx['tolerances']
    sub_weights = ctx.get('sub_weights', {})

    def clamp(x, lo, hi):
        return max(lo, min(x, hi))

    score = 0.0
    if not isinstance(artifact, dict):
        return 0.0

    try:
        a_art = float(artifact['lattice_constants']['a'])
        b_art = float(artifact['lattice_constants']['b'])
        c_art = float(artifact['lattice_constants']['c'])
        gold_latt = step_gold['lattice_constants']
        tol_rel = step_tolerances['lattice_constants_rel']
        err_a = abs(a_art - gold_latt['a']) / gold_latt['a']
        err_b = abs(b_art - gold_latt['b']) / gold_latt['b']
        err_c = abs(c_art - gold_latt['c']) / gold_latt['c']
        s_a = max(0.0, 1.0 - err_a / tol_rel)
        s_b = max(0.0, 1.0 - err_b / tol_rel)
        s_c = max(0.0, 1.0 - err_c / tol_rel)
        latt_score = (s_a + s_b + s_c) / 3.0
    except (KeyError, TypeError, ZeroDivisionError):
        latt_score = 0.0

    try:
        bn = float(artifact['BN_bond_length']['crystal'])
        gold_bn = step_gold['BN_bond_length']
        diff = abs(bn - gold_bn)
        tol_abs = step_tolerances['bn_length_abs']
        if diff <= tol_abs:
            bn_score = 1.0
        elif diff <= 2 * tol_abs:
            bn_score = 0.5
        else:
            bn_score = 0.0
    except (KeyError, TypeError):
        bn_score = 0.0

    try:
        hf_val = float(artifact['lattice_energy_hf']['value'])
        gold_hf = step_gold['lattice_energy_hf']
        err_rel = abs(hf_val - gold_hf) / abs(gold_hf)
        tol_energy = step_tolerances['energy_rel']
        hf_score = max(0.0, 1.0 - err_rel / tol_energy)
    except (KeyError, TypeError, ZeroDivisionError):
        hf_score = 0.0

    try:
        mp2_val = float(artifact['lattice_energy_mp2']['value'])
        gold_mp2 = step_gold['lattice_energy_mp2']
        err_rel = abs(mp2_val - gold_mp2) / abs(gold_mp2)
        mp2_score = max(0.0, 1.0 - err_rel / tol_energy)
    except (KeyError, TypeError, ZeroDivisionError):
        mp2_score = 0.0

    pair_score = 0.0
    try:
        pairs_art = artifact['pair_energies']
        gold_pairs = step_gold['pair_energies']
        tol_pair_abs = step_tolerances['pair_energy_abs']
        pair_keys = ["(1)-(2)", "(1)-(3)", "(1)-(4)", "(1)-(5)", "(1)-(6)", "(1)-(7)", "(1)-(8)"]
        diffs = []
        for k in pair_keys:
            v = float(pairs_art[k])
            g = float(gold_pairs[k])
            diffs.append((k, abs(v - g), v))
        within = sum(1 for d in diffs if d[1] <= tol_pair_abs)
        pair_accuracy = within / len(pair_keys)

        def rank_dict(d):
            sorted_items = sorted(d.items(), key=lambda x: x[1])
            rank = {}
            prev_val = None
            prev_rank = None
            for i, (k, v) in enumerate(sorted_items):
                if v == prev_val:
                    rank[k] = prev_rank
                else:
                    rank[k] = i + 1
                    prev_val = v
                    prev_rank = i + 1
            return rank
        gold_rank = rank_dict(gold_pairs)
        art_rank = rank_dict(pairs_art)
        matches = sum(1 for k in pair_keys if gold_rank.get(k) == art_rank.get(k))
        ordering_score = matches / len(pair_keys)

        pair_score = 0.7 * pair_accuracy + 0.3 * ordering_score
    except (KeyError, TypeError):
        pair_score = 0.0

    score = (sub_weights.get('lattice_constants', 0.2) * latt_score +
             sub_weights.get('bn_length', 0.1) * bn_score +
             sub_weights.get('hf_energy', 0.2) * hf_score +
             sub_weights.get('mp2_energy', 0.2) * mp2_score +
             sub_weights.get('pair_energies', 0.3) * pair_score)
    return score


_SCORERS = {
    'results': score_0,
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
