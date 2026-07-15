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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    data_by_delta = {}
    for row in artifact:
        try:
            d = float(row['δ'])
            T = float(row['T'])
            Mz = float(row['M_z'])
        except (ValueError, KeyError):
            continue
        if d not in data_by_delta:
            data_by_delta[d] = []
        data_by_delta[d].append((T, Mz))
    for d in data_by_delta:
        data_by_delta[d].sort(key=lambda x: x[0])

    gold = step['hidden_gold']['compensation']
    weights = {c['id']: c['weight_in_step'] for c in step['checks']}
    scores = {}

    # δ=0.0
    if 0.0 in data_by_delta:
        temps_mz = data_by_delta[0.0]
        found_comp = None
        for i in range(1, len(temps_mz)):
            s1 = temps_mz[i-1][1]
            s2 = temps_mz[i][1]
            if s1 * s2 <= 0:
                t1, t2 = temps_mz[i-1][0], temps_mz[i][0]
                if abs(s2 - s1) > 1e-12:
                    found_comp = t1 - s1 * (t2 - t1) / (s2 - s1)
                else:
                    found_comp = (t1 + t2) / 2
                break
        if found_comp is not None and abs(found_comp - 0.29) <= 0.02:
            scores['comp_0'] = 1.0
        elif found_comp is not None and abs(found_comp - 0.29) <= 0.04:
            scores['comp_0'] = 0.5
        else:
            scores['comp_0'] = 0.0
    else:
        scores['comp_0'] = 0.0

    # δ=0.2
    if 0.2 in data_by_delta:
        temps_mz = data_by_delta[0.2]
        found_comp = None
        for i in range(1, len(temps_mz)):
            s1 = temps_mz[i-1][1]
            s2 = temps_mz[i][1]
            if s1 * s2 <= 0:
                t1, t2 = temps_mz[i-1][0], temps_mz[i][0]
                if abs(s2 - s1) > 1e-12:
                    found_comp = t1 - s1 * (t2 - t1) / (s2 - s1)
                else:
                    found_comp = (t1 + t2) / 2
                break
        if found_comp is not None and found_comp > 0.30:
            scores['comp_2'] = 1.0
        elif found_comp is not None and found_comp > 0.29:
            scores['comp_2'] = 0.5
        else:
            scores['comp_2'] = 0.0
    else:
        scores['comp_2'] = 0.0

    # δ=0.4
    if 0.4 in data_by_delta:
        temps_mz = data_by_delta[0.4]
        sign = None
        has_sign_change = False
        for T, Mz in temps_mz:
            if Mz == 0:
                has_sign_change = True
                break
            cur_sign = 1 if Mz > 0 else -1
            if sign is None:
                sign = cur_sign
            elif sign != cur_sign:
                has_sign_change = True
                break
        if not has_sign_change:
            scores['comp_4'] = 1.0
        else:
            scores['comp_4'] = 0.0
    else:
        scores['comp_4'] = 0.0

    total = sum(weights[c] * scores.get(c, 0.0) for c in weights)
    return min(max(total, 0.0), 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import math

    data_by_T = {}
    for row in artifact:
        try:
            T = float(row['T'])
            d = float(row['δ'])
            Mz = float(row['M_z'])
        except (ValueError, KeyError):
            continue
        if T not in data_by_T:
            data_by_T[T] = []
        data_by_T[T].append((d, Mz))
    for T in data_by_T:
        data_by_T[T].sort(key=lambda x: x[0])

    gold = step['hidden_gold']
    weights = {c['id']: c['weight_in_step'] for c in step['checks']}
    scores = {}

    # T=0.1
    if 0.1 in data_by_T:
        points = data_by_T[0.1]
        max_Mz = -float('inf')
        max_delta = None
        for d, Mz in points:
            if Mz > max_Mz:
                max_Mz = Mz
                max_delta = d
        if max_delta is not None and abs(max_delta - 0.26) <= 0.03:
            scores['delta_T01_max'] = 1.0
        elif max_delta is not None and abs(max_delta - 0.26) <= 0.05:
            scores['delta_T01_max'] = 0.5
        else:
            scores['delta_T01_max'] = 0.0

        found_zero = None
        for i in range(1, len(points)):
            d1, Mz1 = points[i-1]
            d2, Mz2 = points[i]
            if Mz1 * Mz2 <= 0:
                if abs(Mz2 - Mz1) > 1e-12:
                    found_zero = d1 - Mz1 * (d2 - d1) / (Mz2 - Mz1)
                else:
                    found_zero = (d1 + d2) / 2
                break
        if found_zero is not None and abs(found_zero - 0.456) <= 0.02:
            scores['delta_T01_zero'] = 1.0
        elif found_zero is not None and abs(found_zero - 0.456) <= 0.04:
            scores['delta_T01_zero'] = 0.5
        else:
            scores['delta_T01_zero'] = 0.0
    else:
        scores['delta_T01_max'] = 0.0
        scores['delta_T01_zero'] = 0.0

    # T=0.35
    if 0.35 in data_by_T:
        points = data_by_T[0.35]
        monotonic = True
        prev = None
        for d, Mz in points:
            if prev is not None and Mz > prev + 1e-9:
                monotonic = False
                break
            prev = Mz
        found_zero = None
        for i in range(1, len(points)):
            d1, Mz1 = points[i-1]
            d2, Mz2 = points[i]
            if Mz1 * Mz2 <= 0:
                if abs(Mz2 - Mz1) > 1e-12:
                    found_zero = d1 - Mz1 * (d2 - d1) / (Mz2 - Mz1)
                else:
                    found_zero = (d1 + d2) / 2
                break
        subscore = 0.0
        if monotonic:
            subscore += 0.5
        if found_zero is not None and abs(found_zero - 0.245) <= 0.02:
            subscore += 0.5
        scores['delta_T035'] = min(subscore, 1.0)
    else:
        scores['delta_T035'] = 0.0

    total = sum(weights[c] * scores.get(c, 0.0) for c in weights)
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
