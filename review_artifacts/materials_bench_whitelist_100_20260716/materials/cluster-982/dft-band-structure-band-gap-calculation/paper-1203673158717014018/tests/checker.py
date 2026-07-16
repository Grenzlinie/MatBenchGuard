import os
import json
import csv

# === author imports / helpers ===
import os, json, math


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


# === block: score_0 (check id='step_total_energies') ===
def score_0(artifact, step, ctx):
    ternary = ['LiAgF3-1','LiAgF3-2','Li2AgF4-1','Li2AgF4-2','Li2AgF4-3']
    if not isinstance(artifact, dict):
        return 0.0
    count = 0
    for name in ternary:
        d = artifact.get(name, {})
        e_fm = d.get('E_FM')
        e_afm = d.get('E_AFM')
        if isinstance(e_fm, (int,float)) and isinstance(e_afm, (int,float)) and e_afm < e_fm:
            count += 1
    return count / len(ternary) if ternary else 0.0


# === block: score_1 (check id='step_j_values') ===
def score_1(artifact, step, ctx):
    # Load total_energies.json
    path_te = os.path.join('/app/outputs', 'total_energies.json')
    if not os.path.exists(path_te):
        return 0.0
    with open(path_te, 'r') as f:
        totals = json.load(f)

    # Formulas for J (meV) from total energies (eV)
    def get_j(totals):
        j = {}
        try:
            # LiAgF3-1
            d = totals['LiAgF3-1']
            j['LiAgF3-1'] = (d['E_AFM'] - d['E_FM']) / 2.0 * 1000.0
            # LiAgF3-2
            d = totals['LiAgF3-2']
            efm = d['E_FM']; eafm = d['E_AFM']; eafm2 = d['E_AFM2']
            j['LiAgF3-2_J1'] = (eafm2 - efm) / 2.0 * 1000.0
            j['LiAgF3-2_J2'] = (eafm - eafm2) / 2.0 * 1000.0
            # Li2AgF4-1
            d = totals['Li2AgF4-1']
            j['Li2AgF4-1'] = (d['E_AFM'] - d['E_FM']) / 4.0 * 1000.0
            # Li2AgF4-2
            d = totals['Li2AgF4-2']
            j['Li2AgF4-2'] = (d['E_AFM'] - d['E_FM']) * 1000.0
            # Li2AgF4-3
            d = totals['Li2AgF4-3']
            j['Li2AgF4-3'] = (d['E_AFM'] - d['E_FM']) * 1000.0
        except (KeyError, TypeError):
            return None
        return j

    recomputed = get_j(totals)
    if recomputed is None:
        return 0.0

    gold = step.get('gold', {})
    tol_abs = step.get('tolerance_abs', 5.0)
    tol_rel = step.get('tolerance_rel', 0.10)
    keys = ['LiAgF3-1','LiAgF3-2_J1','LiAgF3-2_J2','Li2AgF4-1','Li2AgF4-2','Li2AgF4-3']
    score = 0.0
    parts = 0
    for k in keys:
        r = recomputed.get(k)
        g = gold.get(k)
        if r is None or g is None:
            continue
        allowed = max(tol_rel * abs(g), tol_abs)
        if abs(r - g) <= allowed:
            score += 1.0
        parts += 1

    if parts > 0:
        score /= parts
    else:
        score = 0.0

    # Ordering check
    ordering = step.get('ordering', [])
    values = []
    for k in ordering:
        r = recomputed.get(k)
        if r is not None:
            values.append(abs(r))
    ok = len(values) == len(ordering) and all(values[i] > values[i+1] for i in range(len(values)-1))
    score += 0.1 if ok else 0.0

    # Threshold
    thr_key = step.get('threshold_key')
    thr_val = step.get('threshold_value', -240)
    if thr_key and thr_key in recomputed:
        if recomputed[thr_key] < thr_val:  # more negative than -240 meV
            score += 0.1

    return min(score, 1.0)


# === block: score_2 (check id='step_convex_hull') ===
def score_2(artifact, step, ctx):
    # Load total_energies.json
    path_te = os.path.join('/app/outputs', 'total_energies.json')
    if not os.path.exists(path_te):
        return 0.0
    with open(path_te, 'r') as f:
        totals = json.load(f)

    EV_TO_KJ_MOL = 96.48533212

    # Extract reference energies
    lif = totals.get('LiF', {}).get('E_FM')
    agf2 = totals.get('AgF2', {}).get('E_FM')
    if lif is None or agf2 is None:
        return 0.0

    def delta_e(ternary_name, n_lif, n_agf2):
        d = totals.get(ternary_name, {})
        e_afm = d.get('E_AFM')
        if e_afm is None:
            return None
        # Energy of decomposition: n_lif * E_FM(LiF) + n_agf2 * E_FM(AgF2)
        ref = n_lif * lif + n_agf2 * agf2
        return (e_afm - ref) * EV_TO_KJ_MOL

    gold = step.get('gold', {})
    tol = step.get('tolerance_abs', 3.0)

    mapping = [
        ('LiAgF3-1', 1, 1),
        ('LiAgF3-2', 1, 1),
        ('Li2AgF4-1', 2, 1),
        ('Li2AgF4-2', 2, 1),
        ('Li2AgF4-3', 2, 1)
    ]

    score = 0.0
    count = 0
    for name, nLi, nAg in mapping:
        calc = delta_e(name, nLi, nAg)
        if calc is None:
            continue
        target = gold.get(name)
        if target is None:
            continue
        if abs(calc - target) <= tol:
            score += 1.0
        count += 1

    return score / count if count else 0.0


_SCORERS = {
    'step_total_energies': score_0,
    'step_j_values': score_1,
    'step_convex_hull': score_2,
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
