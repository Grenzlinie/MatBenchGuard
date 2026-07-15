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
    def compute_gold(m, n):
        d = {}
        # Original indices (Theorem 2)
        d['R1'] = 164*m*n - 40*m - 40*n + 20
        d['Rm1'] = 1.2778*m*n + 0.8333*m + 0.8333*n + 2.1667
        d['R12'] = 47.5118*m*n - 7.3722*m - 7.3722*n + 2.1593
        d['Rm12'] = 4.1950*m*n + 1.0641*m + 1.0641*n + 0.4408
        d['ABC'] = 9.4860*m*n + 0.2464*m + 0.2464*n + 0.1911
        d['GA'] = 13.07998*m*n + 0.1890*m + 0.1890*n - 0.8728
        d['F'] = 430*m*n - 96*m - 96*n + 72
        d['AZI'] = 153.3818*m*n - 23.296*m - 23.296*n + 4.796
        d['M1'] = 102*m*n - 16*m - 16*n + 8
        d['M2'] = 164*m*n - 40*m - 40*n + 20
        d['ReZG1'] = 11.6667*m*n + 2*m + 2*n + 2
        d['ReZG2'] = 22.1905*m*n - 3.3905*m - 3.3905*n + 0.2571
        d['ReZG3'] = 1236*m*n - 344*m - 344*n + 232
        # Coindices (Theorem 3)
        d['CR1'] = 358*m*m*n*n - 384*m*m*n + 10*m*n*n + 564*m*n + 8*m*m - 8*n*n - 320*m + 176*n + 124
        d['CRm1'] = (5.556*m*m*n*n - 7.6667*m*m*n + 5.6667*m*n*n + 31.611*m*n + m*m - n*n - 26.333*m + 22.6667*n + 35.8333)
        d['CR12'] = (116.7631*m*m*n*n + 16.0897*m*m*n + 65.4523*m*n*n + 241.1257*m*n + 22.6274*m*m - 22.6274*n*n - 157.7649*m - 22.0004*n + 105.7230)
        d['CRm12'] = (14.5013*m*m*n*n - 20.3869*m*m*n + 12.4207*m*n*n + 56.8750*m*n + 2.8284*m*m - 2.8284*n*n - 45.1768*m + 38.0554*n + 56.6045)
        d['CABC'] = (27.708*m*m*n*n + 31.3591*m*m*n + 20.0454*m*n*n + 81.1132*m*n + 5.6569*m*m - 5.6569*n*n - 58.2292*m + 40.7658*n + 53.5490)
        d['CGA'] = (38.0393*m*m*n*n - 49.8105*m*m*n + 26.8076*m*n*n + 104.8371*m*n + 7.5425*m*m - 7.5425*n*n - 78.9863*m + 56.0*n + 73.6701)
        d['CF'] = 928*m*m*n*n - 972*m*m*n + 452*m*n*n + 790*m*n + 16*m*m - 16*n*n - 752*m + 368*n + 248
        d['CAZI'] = (379.3077*m*m*n*n - 881.0*m*m*n + 200.704*m*n*n + 1803.9942*m*n + 64*m*m - 64*n*n - 632.704*m + 486.816*n + 603.204)
        d['CM1'] = 248*m*m*n*n - 292*m*m*n + 140*m*n*n + 518*m*n + 48*m*m - 48*n*n - 328*m + 200*n + 360
        d['CM2'] = 358*m*m*n*n - 384*m*m*n + 160*m*n*n + 564*m*n + 8*m*m - 8*n*n - 320*m + 176*n + 124
        d['CReZG1'] = (35.6667*m*m*n*n - 47.6667*m*m*n + 31.0*m*n*n + 129.6667*m*n + 6*m*m - 6*n*n - 67*m + 74*n + 100)
        d['CReZG2'] = (49.1230*m*m*n*n - 65.7908*m*m*n + 30.7429*m*n*n + 112.533*m*n + 10.6667*m*m - 10.6667*n*n - 82.6095*m + 48.0571*n + 67.7429)
        d['CReZG3'] = 2504*m*m*n*n - 2368*m*m*n + 928*m*n*n + 3068*m*n + 389*m*m - 389*n*n - 1410*m + 696*n + 1240
        # Reverse indices (Theorem 4)
        d['RR1'] = 136*m*n + 72*m + 72*n - 36
        d['RRm1'] = 1.9*m*n - 0.24*m - 0.24*n + 0.18
        d['RR12'] = 42.2926*m*n + 8.5402*m + 8.5402*n - 4.9239
        d['RRm12'] = 4.9764*m*n - 0.4931*m - 0.4931*n + 0.3954
        d['RABC'] = 10.4216*m*n + 0.4957*m + 0.4957*n - 2.5028
        d['RGA'] = 12.4134*m*n + 0.1433*m + 0.1433*n - 0.2159
        d['RF'] = 374*m*n + 128*m + 128*n - 40
        d['RAZI'] = 130.3493*m*n + 9.7612*m + 9.7612*n + 118.8296
        d['RM1'] = 90*m*n + 16*m + 16*n - 8
        d['RM2'] = 136*m*n + 72*m + 72*n + 144
        d['RReZG1'] = 11.7667*m*n + 0.2*m + 0.2*n + 0.8
        d['RReZG2'] = 15.5405*m*n + 6.7540*m + 6.7540*n - 2.9115
        d['RReZG3'] = 976*m*n + 904*m + 904*n - 344
        return d

    ctx = {}
    test_points = [(1,1), (2,2), (100,100), (50,50)]
    gold_values = {}
    for mp, np in test_points:
        gold_values[(mp,np)] = compute_gold(mp, np)
    ctx["gold_values"] = gold_values
    ctx["test_points"] = test_points
    ctx["ref_set_feat"] = set(["GA", "RGA", "RABC", "RRm12", "RReZG1", "ABC", "CF", "RRm1", "CReZG3", "CM2"])
    ctx["ref_set_reg"] = set(["GA", "RGA", "RABC", "RRm12", "RReZG1", "ABC", "CF", "RRm1", "CReZG3", "CM2"])
    return ctx


# === block: score_0 (check id='indices_values_check') ===
def score_0(artifact, step, ctx):
    test_points = step["test_points"]
    tolerance = step["relative_tolerance"]
    gold_dict = ctx["gold_values"]
    good_cols = 0
    all_cols = 0
    for mp, np in test_points:
        row = next((r for r in artifact if int(r["m"])==mp and int(r["n"])==np), None)
        if row is None:
            continue
        gold = gold_dict[(mp,np)]
        for col in gold:
            if col in ("m","n"):
                continue
            try:
                val = float(row[col])
                g = gold[col]
                rel_err = abs(val - g) / max(1.0, abs(g))
                if rel_err <= tolerance:
                    good_cols += 1
                all_cols += 1
            except (KeyError, ValueError):
                pass
    if all_cols == 0:
        return 0.0
    return good_cols / all_cols


# === block: score_1 (check id='feature_selection_ranking') ===
def score_1(artifact, step, ctx):
    ref_set = ctx["ref_set_feat"]
    top10 = [row["idx"] for row in artifact[:10]]
    if len(top10) == 0:
        return 0.0
    intersection = set(top10) & ref_set
    return len(intersection) / len(ref_set)


# === block: score_2 (check id='regression_ranking') ===
def score_2(artifact, step, ctx):
    ref_set = ctx["ref_set_reg"]
    top10 = [row["idx"] for row in artifact[:10]]
    if len(top10) == 0:
        return 0.0
    intersection = set(top10) & ref_set
    return len(intersection) / len(ref_set)


_SCORERS = {
    'indices_values_check': score_0,
    'feature_selection_ranking': score_1,
    'regression_ranking': score_2,
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
