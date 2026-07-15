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


# === block: score_0 (check id='compute_table_5_4') ===
def score_0(artifact, step, ctx):
    ref_rows = step.get('reference', [])
    if not ref_rows:
        return 0.0

    # Build gold lookup: temperature -> (Seebeck_uVK, ratio, p_prime)
    gold_map = {}
    for r in ref_rows:
        T = int(r['Temperature_C'])
        S = float(r['Seebeck_uVK'])
        ratio = float(r['ratio'])
        p_prime = float(r['p_prime'])
        gold_map[T] = (S, ratio, p_prime)

    n = len(gold_map)
    seebeck_ok = 0
    ratio_score_sum = 0.0
    pprime_score_sum = 0.0
    consistency_ok = 0

    for row in artifact:
        try:
            T = int(row['Temperature_C'])
            S_sub = float(row['Seebeck_uVK'])
            ratio_sub = float(row['MnB4_MnB3_ratio'])
            p_prime_sub = float(row['p_prime'])
            Ni_A = float(row['Ni_A'])
            Mn_A = float(row['Mn_A'])
            Ni_B = float(row['Ni_B'])
            Mn_B3 = float(row['Mn_B3'])
            Mn_B4 = float(row['Mn_B4'])
        except:
            continue
        if T not in gold_map:
            continue
        S_gold, ratio_gold, p_prime_gold = gold_map[T]

        # Seebeck exactness
        if abs(S_sub - S_gold) < 1e-6:
            seebeck_ok += 1

        # ratio scoring: relative error within 1%
        if ratio_gold != 0:
            rel_err = abs(ratio_sub - ratio_gold) / abs(ratio_gold)
        else:
            rel_err = abs(ratio_sub)
        tol = 0.01
        if rel_err <= tol:
            ratio_score_sum += 1.0
        else:
            ratio_score_sum += max(0.0, 1.0 - (rel_err - tol) / (2 * tol))

        # p_prime scoring: absolute error within 0.01
        abs_err = abs(p_prime_sub - p_prime_gold)
        tol_abs = 0.01
        if abs_err <= tol_abs:
            pprime_score_sum += 1.0
        else:
            pprime_score_sum += max(0.0, 1.0 - (abs_err - tol_abs) / (2 * tol_abs))

        # internal consistency of site occupancies with submitted p_prime
        if (abs(Ni_A + p_prime_sub - 1.0) < 0.001 and
            abs(Mn_A - p_prime_sub) < 0.001 and
            abs(Ni_B - p_prime_sub) < 0.001 and
            abs(Mn_B3 + 2 * p_prime_sub - 2.0) < 0.001 and
            abs(Mn_B4 - p_prime_sub) < 0.001 and
            abs(Ni_A + Mn_A - 1.0) < 0.001 and
            abs(Ni_B + Mn_B3 + Mn_B4 - 2.0) < 0.001):
            consistency_ok += 1

    seebeck_score = seebeck_ok / n
    ratio_score = ratio_score_sum / n
    pprime_score = pprime_score_sum / n
    consistency_score = consistency_ok / n
    score = 0.4 * ratio_score + 0.4 * pprime_score + 0.05 * seebeck_score + 0.15 * consistency_score
    score = max(0.0, min(1.0, score))
    return score


# === block: score_1 (check id='compute_table_10_4') ===
def score_1(artifact, step, ctx):
    ref_rows = step.get('reference', [])
    ref_map = {(r['Temperature_C'], round(r['Seebeck_uVK'], 6)): r for r in ref_rows}
    n = len(ref_rows)
    if n == 0:
        return 0.0

    seebeck_ok = 0
    ratio_score_sum = 0.0
    pprime_score_sum = 0.0
    consistency_ok = 0

    for row in artifact:
        try:
            T = int(row['Temperature_C'])
            S = float(row['Seebeck_uVK'])
            ratio = float(row['MnB4_MnB3_ratio'])
            p_prime = float(row['p_prime'])
            Ni_A = float(row['Ni_A'])
            Mn_A = float(row['Mn_A'])
            Ni_B = float(row['Ni_B'])
            Mn_B3 = float(row['Mn_B3'])
            Mn_B4 = float(row['Mn_B4'])
        except:
            continue
        ref = ref_map.get((T, S), ref_map.get((T, round(S, 6)), None))
        if ref is None:
            continue
        if abs(S - ref['Seebeck_uVK']) < 1e-8:
            seebeck_ok += 1
        gold_ratio = ref['ratio']
        rel_err = abs(ratio - gold_ratio) / (abs(gold_ratio) if abs(gold_ratio) > 1e-12 else 1e-12)
        tol = 0.01
        if rel_err <= tol:
            ratio_score_sum += 1.0
        else:
            ratio_score_sum += max(0.0, 1.0 - (rel_err - tol) / (2*tol))
        gold_pp = ref['p_prime']
        abs_err = abs(p_prime - gold_pp)
        tol_abs = 0.01
        if abs_err <= tol_abs:
            pprime_score_sum += 1.0
        else:
            pprime_score_sum += max(0.0, 1.0 - (abs_err - tol_abs) / (2*tol_abs))
        c = ratio / (1.0 + ratio)
        expected_pp = 2.0 * c / (1.0 + 2.0 * c)
        if abs(p_prime - expected_pp) < 0.001 and abs(Ni_A + p_prime - 1.0) < 0.001 and abs(Mn_A - p_prime) < 0.001 \
           and abs(Ni_B - p_prime) < 0.001 and abs(Mn_B3 + 2*p_prime - 2.0) < 0.001 and abs(Mn_B4 - p_prime) < 0.001 \
           and abs(Ni_A + Mn_A - 1.0) < 0.001 and abs(Ni_B + Mn_B3 + Mn_B4 - 2.0) < 0.001:
            consistency_ok += 1

    if n == 0:
        score = 0.0
    else:
        seebeck_score = seebeck_ok / n
        ratio_score = ratio_score_sum / n
        pprime_score = pprime_score_sum / n
        consistency_score = consistency_ok / n
        score = 0.4*ratio_score + 0.4*pprime_score + 0.05*seebeck_score + 0.15*consistency_score
    score = min(max(score, 0.0), 1.0)
    return score


_SCORERS = {
    'compute_table_5_4': score_0,
    'compute_table_10_4': score_1,
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
