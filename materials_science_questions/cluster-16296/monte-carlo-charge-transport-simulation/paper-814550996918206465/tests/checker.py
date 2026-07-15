import os
import json
import csv

# === author imports / helpers ===
import json


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


# === block: score_0 (check id='velocity_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    velocities = data.get("velocities", [])
    if not velocities:
        return 0.0
    gold_velocities = step.get("gold_velocities", [])
    tol_rel = step.get("tolerance_rel", 0.05)
    tol_abs = step.get("tolerance_abs_vel", 500000.0)
    ratio_min = step.get("wire_bulk_min_ratio_300K", 1.8)
    ratio_max = step.get("wire_bulk_max_ratio_300K", 2.5)
    subscores = []
    for gold in gold_velocities:
        T = gold["T"]
        match = next((v for v in velocities if v.get("T") == T and v.get("Fx") == gold["Fx"]), None)
        if match is None:
            continue
        wire = match.get("velocity_cm_s")
        bulk = match.get("bulk_velocity_cm_s")
        for (val, target) in [(wire, gold["wire"]), (bulk, gold["bulk"])]:
            if val is not None:
                tol = max(tol_rel * target, tol_abs)
                diff = abs(val - target)
                if diff <= tol:
                    subscores.append(1.0)
                else:
                    subscores.append(max(0.0, 1.0 - (diff - tol) / tol))
        if wire is not None and bulk is not None and wire > bulk:
            subscores.append(1.0)
        else:
            subscores.append(0.0)
    # 300K ratio check
    v300 = next((v for v in velocities if v.get("T") == 300 and v.get("Fx") == 500), None)
    if v300:
        w = v300.get("velocity_cm_s")
        b = v300.get("bulk_velocity_cm_s")
        if w is not None and b is not None and b > 0:
            ratio = w / b
            if ratio_min <= ratio <= ratio_max:
                subscores.append(1.0)
            else:
                subscores.append(max(0.0, 1.0 - min(abs(ratio - ratio_min), abs(ratio - ratio_max)) / ratio_min))
    if not subscores:
        return 0.0
    return sum(subscores) / len(subscores)


# === block: score_1 (check id='distribution_check') ===
def score_1(artifact, step, ctx):
    data = artifact
    resonance_data = data.get("resonance_data", [])
    if not resonance_data:
        return 0.0
    gold_fractions = step.get("gold_fractions", {})
    tol = step.get("tolerance_abs_fraction", 0.02)
    scores = []
    cases = {"off_resonance": 28, "resonance": 36, "above_resonance": 44}
    for case_key, target_delta in cases.items():
        gold = gold_fractions.get(case_key)
        if gold is None:
            continue
        match = next((item for item in resonance_data if item.get("case") == case_key and abs(item.get("delta_E_meV", 0) - target_delta) <= 2), None)
        if match is None:
            continue
        for field, gval in [("fraction_subband_1", gold["f1"]), ("fraction_subband_2", gold["f2"]), ("fraction_subband_3", gold["f3"])]:
            val = match.get(field)
            if val is not None:
                diff = abs(val - gval)
                if diff <= tol:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    # sum to 1 check
    for item in resonance_data:
        f1 = item.get("fraction_subband_1", 0)
        f2 = item.get("fraction_subband_2", 0)
        f3 = item.get("fraction_subband_3", 0)
        total = f1 + f2 + f3
        diff_sum = abs(total - 1.0)
        if diff_sum <= 0.01:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff_sum - 0.01) / 0.01))
    # structural resonance > off resonance
    off = next((x for x in resonance_data if x.get("case") == "off_resonance"), None)
    res = next((x for x in resonance_data if x.get("case") == "resonance"), None)
    if off and res:
        off_f2 = off.get("fraction_subband_2", 0)
        res_f2 = res.get("fraction_subband_2", 0)
        if res_f2 > off_f2:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'velocity_check': score_0,
    'distribution_check': score_1,
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
