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
    reference_densities = {
        "4006": 0.00897,
        "5005": 0.0649,
        "6004": 0.250
    }
    return {
        "ref_densities": reference_densities,
        "density_tol": 0.05,
        "target_T0": 2500.0,
        "T0_tol": 300.0
    }


# === block: score_0 (check id='step_size_dist') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    from collections import defaultdict
    temps = ["4006", "5005", "6004"]
    temp_data = defaultdict(lambda: defaultdict(float))
    temp_k_max = defaultdict(int)
    for row in rows:
        try:
            T = str(int(float(row['temperature'])))
            k = int(row['cluster_size'])
            nk = float(row['number_density'])
        except (ValueError, KeyError):
            return 0.0
        temp_data[T][k] = nk
        temp_k_max[T] = max(temp_k_max[T], k)
    # total density check
    ref = ctx["ref_densities"]
    tol = ctx["density_tol"]
    total_score = 0.0
    for T in temps:
        if T not in temp_data or temp_k_max[T] < 2:
            total_score += 0.0
            continue
        calc_dens = sum(k * nk for k, nk in temp_data[T].items() if k > 0)
        expected = ref.get(T)
        if expected is None:
            continue
        if expected == 0:
            if calc_dens == 0:
                total_score += 1.0 / len(temps)
            continue
        rel_err = abs(calc_dens - expected) / expected
        if rel_err <= tol:
            total_score += 1.0 / len(temps)
        else:
            total_score += max(0.0, (2.0 * tol - rel_err) / tol) / len(temps)  # linear decay beyond
    # monotonicity check
    mono_score = 0.0
    for T in temps:
        if T not in temp_data:
            continue
        ks = sorted([k for k in temp_data[T] if k >= 1])
        if len(ks) < 2:
            continue
        nks = [temp_data[T][k] for k in ks]
        # allow up to 10% violation of strict monotonic decrease
        violations = 0
        for i in range(len(nks)-1):
            if nks[i+1] > nks[i] * 1.1:
                violations += 1
        if violations == 0:
            mono_score += 1.0 / len(temps)
        else:
            mono_score += max(0.0, 1.0 - violations / (len(ks)-1)) / len(temps)
    # combine
    score = 0.6 * total_score + 0.4 * mono_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step_structure_param') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    temps = ["4006", "5005", "6004"]
    # verify keys
    for T in temps:
        if T not in data or not isinstance(data[T], list):
            return 0.0
    # extract eta arrays
    eta = {}
    for T in temps:
        arr = data[T]
        valid = {}
        for item in arr:
            if not isinstance(item, dict):
                continue
            k = item.get('k')
            e = item.get('eta')
            if k is None or e is None:
                continue
            try:
                k = int(k)
                e = float(e)
            except (ValueError, TypeError):
                continue
            if k >= 2 and k <= 26:
                valid[k] = e
        eta[T] = valid
    # Check 1: all eta within [1.0, 3.5]
    range_ok = 0
    total_k = 0
    for T in temps:
        for k, e in eta[T].items():
            total_k += 1
            if 1.0 <= e <= 3.5:
                range_ok += 1
    # Check 2: for each k present in at least two temps, eta(6004) >= eta(5005) >= eta(4006) with 0.05 tolerance
    order_ok = 0
    order_count = 0
    ks_ordered = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    for k in ks_ordered:
        vals = []
        for T in temps:
            if k in eta[T]:
                vals.append(eta[T][k])
        if len(vals) >= 2:
            order_count += 1
            # check non-decreasing with T (higher T => higher eta)
            if all(vals[i] <= vals[i+1] + 0.05 for i in range(len(vals)-1)):
                order_ok += 1
    # Score
    range_score = range_ok / total_k if total_k > 0 else 0.0
    order_score = order_ok / order_count if order_count > 0 else 1.0
    score = 0.5 * range_score + 0.5 * order_score
    return min(1.0, max(0.0, score))


# === block: score_2 (check id='step_transition_T') ===
def score_2(artifact, step, ctx):
    text = artifact
    if not isinstance(text, str):
        text = str(text) if text is not None else ''
    lines = text.strip().split('\n')
    if not lines:
        return 0.0
    try:
        val = float(lines[0].strip())
    except ValueError:
        return 0.0
    target = ctx["target_T0"]
    tol = ctx["T0_tol"]
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_size_dist': score_0,
    'step_structure_param': score_1,
    'step_transition_T': score_2,
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
