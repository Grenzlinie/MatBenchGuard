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
    return {}


# === block: score_0 (check id='torsion_angles') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance_deg', 5.0)
    mol_list = artifact.get('molecules', [])
    scores = []
    for mol in mol_list:
        name = mol.get('name')
        val = mol.get('omega_deg')
        if name not in gold or val is None:
            scores.append(0.0)
            continue
        diff = abs(val - gold[name])
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / (2 * tol)))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='xps_shifts') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance_eV', 0.2)
    bes = artifact.get('binding_energies', [])
    # absolute comparison
    abs_score = 0.0
    count = 0
    for item in bes:
        mol = item.get('molecule')
        val = item.get('s2p3_2_eV')
        if mol in gold and val is not None:
            diff = abs(val - gold[mol])
            if diff <= tol:
                abs_score += 1.0
            count += 1
    if count > 0:
        abs_score /= count
    else:
        abs_score = 0.0
    # trend check
    vals = {item.get('molecule'): item.get('s2p3_2_eV') for item in bes}
    trend_score = 0.0
    pairs = [('BP3T_H', 'BP2T_L'), ('BP5T_H', 'BP4T_L')]
    for odd, even in pairs:
        if odd in vals and even in vals and vals[odd] is not None and vals[even] is not None:
            if vals[odd] > vals[even]:
                trend_score += 1.0
    if pairs:
        trend_score /= len(pairs)
    return 0.5 * abs_score + 0.5 * trend_score


# === block: score_2 (check id='rairs_modes') ===
def score_2(artifact, step, ctx):
    gold_shifts = step.get('gold_shifts_cm', {})
    gold_int_changes = step.get('gold_int_changes_pct', {})
    freq_frac = step.get('freq_tol_relative', 0.2)
    int_frac = step.get('int_tol_relative', 0.3)
    modes = artifact.get('modes', [])
    from collections import defaultdict
    by_label = defaultdict(lambda: {'BP3T_H': None, 'BP4T_L': None})
    for m in modes:
        lbl = m.get('label')
        mol = m.get('molecule')
        if lbl and mol:
            by_label[lbl][mol] = m
    score_parts = []
    for lbl, pair in by_label.items():
        bp3 = pair['BP3T_H']
        bp4 = pair['BP4T_L']
        if bp3 is None or bp4 is None or lbl not in gold_shifts:
            score_parts.append(0.0)
            continue
        f1 = bp3.get('frequency_cm-1')
        i1 = bp3.get('intensity_arb')
        f2 = bp4.get('frequency_cm-1')
        i2 = bp4.get('intensity_arb')
        if None in (f1, f2, i1, i2) or i1 == 0:
            score_parts.append(0.0)
            continue
        if f1 >= 1600 or f2 >= 1600:
            score_parts.append(0.0)
            continue
        freq_shift = f2 - f1
        int_change = (i2 - i1) / i1 * 100.0
        gs = gold_shifts[lbl]
        gi = gold_int_changes[lbl]
        ftol = max(0.5, freq_frac * abs(gs))
        itol = max(1.0, int_frac * abs(gi))
        ok = (abs(freq_shift - gs) <= ftol) and (abs(int_change - gi) <= itol)
        score_parts.append(1.0 if ok else 0.0)
    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


_SCORERS = {
    'torsion_angles': score_0,
    'xps_shifts': score_1,
    'rairs_modes': score_2,
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
