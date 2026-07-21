import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    st1 = spec['steps'][0]
    ref_dg = st1['reference_dG']
    temps = st1['temperature_list']
    tol = st1['tolerance_kJ_per_mol']

    st2 = spec['steps'][1]
    homog = st2['homogeneity_range']
    cthr = st2['c_threshold']
    gold_samps = {s['sample']: s for s in st2['gold_samples']}

    return {'ref_dg': ref_dg, 'temps': temps, 'tol': tol,
            'homog': homog, 'cthr': cthr, 'gold_samps': gold_samps}


# === block: score_0 (check id='step_01_enthalpies') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = ctx['ref_dg']
    temps = ctx['temps']
    tol = ctx['tol']
    if not rows:
        return 0.0
    by_react = {}
    for row in rows:
        r = row['Reaction']
        T = int(row['Temperature_K'])
        dg = float(row['DeltaG_kJ_per_mol_R'])
        if r not in by_react:
            by_react[r] = {}
        by_react[r][T] = dg

    # accuracy
    total = 0
    ok = 0
    for rx, ref_vec in gold.items():
        if rx not in by_react:
            continue
        for i, T in enumerate(temps):
            total += 1
            if T in by_react[rx]:
                diff = abs(by_react[rx][T] - ref_vec[i])
                if diff <= tol:
                    ok += 1
    if total == 0:
        acc = 0.0
    else:
        acc = ok / total

    # ordering check: for each temperature, In and Zn reductions must be the most negative
    in_rx = 'RuO2 + (2/3)In -> Ru + (1/3)In2O3'
    zn_rx = 'RuO2 + (2/3)Zn -> Ru + (1/3)ZnO'
    other_rx = [
        'RuO2 + (4/3)Rh -> Ru + (2/3)Rh2O3',
        'RuO2 + Ir -> Ru + IrO2',
        'RuO2 + (1/2)Re -> Ru + (1/2)ReO2'
    ]
    ord_ok = 0
    ord_total = len(temps)
    for i, T in enumerate(temps):
        vals = {}
        all_present = True
        for rx in [in_rx, zn_rx] + other_rx:
            if rx in by_react and T in by_react[rx]:
                vals[rx] = by_react[rx][T]
            else:
                all_present = False
                break
        if all_present:
            if vals[in_rx] < min(vals[rx] for rx in other_rx) and vals[zn_rx] < min(vals[rx] for rx in other_rx):
                ord_ok += 1
    ord_score = ord_ok / ord_total if ord_total > 0 else 0.0

    return 0.6 * acc + 0.4 * ord_score


# === block: score_1 (check id='step_02_redox_analysis') ===
def score_1(artifact, step, ctx):
    samples = artifact
    homog = ctx['homog']
    cthr = ctx['cthr']
    gold_samps = ctx['gold_samps']
    if not isinstance(samples, list):
        return 0.0
    n = len(samples)
    if n == 0:
        return 0.0
    total = 0
    for obj in samples:
        sname = obj.get('sample', '')
        gold = gold_samps.get(sname)
        if gold is None:
            continue
        local = 0.0
        # predicted fields
        if obj.get('predicted_reduction') == gold['predicted_reduction']:
            local += 0.25
        if obj.get('predicted_secondary_phase') == gold['predicted_secondary_phase']:
            local += 0.25
        if obj.get('expected_c_side') == gold['expected_c_side']:
            local += 0.25
        # experimental_side from c value
        c = obj.get('experimental_c_A')
        if isinstance(c, (int, float)):
            exp_side = 'In-poor' if c <= cthr else 'In-rich'
            if obj.get('experimental_side') == exp_side:
                local += 0.125
            # consistency
            exp_expected = obj.get('expected_c_side')
            cons = (exp_expected == exp_side)
            if obj.get('consistency') == cons:
                local += 0.125
        else:
            # cannot determine experimental_side, skip those sub-points
            pass
        total += local
    return total / n


_SCORERS = {
    'step_01_enthalpies': score_0,
    'step_02_redox_analysis': score_1,
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
