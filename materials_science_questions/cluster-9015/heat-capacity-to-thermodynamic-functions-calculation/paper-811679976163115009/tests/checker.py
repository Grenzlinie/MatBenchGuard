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
    gold_list = spec.get('gold_values', [])
    gold = {}
    for g in gold_list:
        key = (g['compound'], g['interval_end'])
        gold[key] = g
    return {'gold': gold}


# === block: score_0 (check id='check_coefficients') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx['gold']
    total = len(artifact)
    passed = 0
    for row in artifact:
        try:
            compound = row['compound']
            end = int(float(row['interval_end']))
            key = (compound, end)
            if key not in gold:
                continue
            g = gold[key]
            a = float(row['a']); b = float(row['b']); c = float(row['c'])
            # recompute predicted Cp from coefficients
            cp100 = a * (1.0 - 1.0 / (1.0 + b * 100.0**2)) + c * 100.0
            cp200 = a * (1.0 - 1.0 / (1.0 + b * 200.0**2)) + c * 200.0
            cp298 = a * (1.0 - 1.0 / (1.0 + b * 298.15**2)) + c * 298.15
            # compare to hidden benchmark Cp values (tolerance 0.1 J/(mol·K))
            if (abs(cp100 - g['Cp_100']) <= 0.1 and
                abs(cp200 - g['Cp_200']) <= 0.1 and
                abs(cp298 - g['Cp_298']) <= 0.1):
                passed += 1
        except Exception:
            pass
    return passed / total if total else 0.0


# === block: score_1 (check id='check_delta_R') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx['gold']
    total = len(artifact)
    passed = 0
    for row in artifact:
        try:
            compound = row['compound']
            end = int(float(row['interval_end']))
            key = (compound, end)
            if key not in gold:
                continue
            g = gold[key]
            pred_cp = [float(row['Cp_100']), float(row['Cp_200']), float(row['Cp_298'])]
            gold_cp = [g['Cp_100'], g['Cp_200'], g['Cp_298']]
            # recompute mean square deviation Δ
            n = len(pred_cp)
            delta = sum((p - c)**2 for p, c in zip(pred_cp, gold_cp)) / n
            # recompute Pearson R
            mean_pred = sum(pred_cp) / n
            mean_gold = sum(gold_cp) / n
            cov = sum((p - mean_pred)*(c - mean_gold) for p, c in zip(pred_cp, gold_cp))
            var_pred = sum((p - mean_pred)**2 for p in pred_cp)
            var_gold = sum((c - mean_gold)**2 for c in gold_cp)
            if var_pred > 0 and var_gold > 0:
                r_val = cov / math.sqrt(var_pred * var_gold)
            else:
                # if either variance zero, correlation is undefined; treat as fail
                continue
            if abs(delta - g['Delta']) <= 0.001 and abs(r_val - g['R']) <= 0.0001:
                passed += 1
        except Exception:
            pass
    return passed / total if total else 0.0


# === block: score_2 (check id='check_ordering') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx['gold']
    compounds = ['LiBO2', 'BaS']
    all_ok = True
    for comp in compounds:
        rows = [r for r in artifact if r['compound'] == comp]
        if not rows:
            all_ok = False
            break
        deltas = {}  # interval_end -> recomputed Delta
        for r in rows:
            try:
                end = int(float(r['interval_end']))
                key = (comp, end)
                if key not in gold:
                    continue
                g = gold[key]
                cp_pred = [float(r['Cp_100']), float(r['Cp_200']), float(r['Cp_298'])]
                cp_bench = [g['Cp_100'], g['Cp_200'], g['Cp_298']]
                n = len(cp_pred)
                delta_recomp = sum((p - b)**2 for p, b in zip(cp_pred, cp_bench)) / n
                deltas[end] = delta_recomp
            except Exception:
                pass
        if 700 not in deltas:
            all_ok = False
            break
        delta_700 = deltas[700]
        if not all(delta_700 <= d + 1e-9 for d in deltas.values()):
            all_ok = False
            break
    return 1.0 if all_ok else 0.0


# === block: score_3 (check id='check_cp_values') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    total = len(artifact)
    passed = 0
    for row in artifact:
        try:
            a = float(row['a'])
            b = float(row['b'])
            c = float(row['c'])
            cp100 = a * (1.0 - 1.0 / (1.0 + b * 100.0**2)) + c * 100.0
            cp200 = a * (1.0 - 1.0 / (1.0 + b * 200.0**2)) + c * 200.0
            cp298 = a * (1.0 - 1.0 / (1.0 + b * 298.15**2)) + c * 298.15
            if (abs(float(row['Cp_100']) - cp100) <= 1e-5 and
                abs(float(row['Cp_200']) - cp200) <= 1e-5 and
                abs(float(row['Cp_298']) - cp298) <= 1e-5):
                passed += 1
        except Exception:
            pass
    return passed / total if total else 0.0


_SCORERS = {
    'check_coefficients': score_0,
    'check_delta_R': score_1,
    'check_ordering': score_2,
    'check_cp_values': score_3,
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
