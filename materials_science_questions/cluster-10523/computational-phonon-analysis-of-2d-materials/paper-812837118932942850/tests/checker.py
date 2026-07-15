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


# === block: score_0 (check id='g_band_check') ===
def score_0(artifact, step, ctx):
    stoichs_order = ["graphite_AB", "NaC48", "NaC24", "NaC12", "NaC6"]
    ref = step["reference"]
    tol = step["tolerance_abs_cm1"]
    values = {}
    for item in artifact:
        s = item.get("stoichiometry")
        v = item.get("g_band_frequency_cm1")
        if s in ref and v is not None:
            values[s] = v
    scores = []
    for stoich in stoichs_order:
        r = ref.get(stoich)
        v = values.get(stoich)
        if v is None:
            scores.append(0.0)
            continue
        diff = abs(v - r)
        if diff <= tol:
            s = 1.0
        elif diff <= 2 * tol:
            s = 0.5
        else:
            s = 0.0
        scores.append(s)
    avg_score = sum(scores) / len(scores) if scores else 0.0
    # monotonic non-increasing check
    mono_ok = True
    sorted_vals = [values[s] for s in stoichs_order if s in values]
    if len(sorted_vals) >= 2:
        prev = sorted_vals[0]
        for v in sorted_vals[1:]:
            if v > prev + 1e-6:
                mono_ok = False
                break
            prev = v
    mono_factor = 1.0 if mono_ok else 0.7
    return avg_score * mono_factor


# === block: score_1 (check id='k_point_check') ===
def score_1(artifact, step, ctx):
    ref = step["reference"]
    tol = step["tolerance_abs_eV"]
    sign_rules = step["sign_rules"]
    stoichs = ["graphite_AB", "NaC48", "NaC24", "NaC12", "NaC6"]
    scores = []
    for stoich in stoichs:
        item = next((i for i in artifact if i.get("stoichiometry") == stoich), None)
        v = item.get("k_point_crossing_energy_eV") if item else None
        r = ref.get(stoich)
        if v is None or r is None:
            scores.append(0.0)
            continue
        rule = sign_rules.get(stoich)
        if rule == "nonnegative":
            sign_ok = (v >= -1e-6)
        elif rule == "negative":
            sign_ok = (v < 0)
        else:
            sign_ok = True
        diff = abs(v - r)
        if sign_ok and diff <= tol:
            s = 1.0
        elif sign_ok and diff <= 2 * tol:
            s = 0.5
        elif sign_ok:
            s = 0.3
        else:
            s = 0.0
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='voltage_check') ===
def score_2(artifact, step, ctx):
    ref = step["reference"]
    tol = step["tolerance_abs_V"]
    sign_rules = step["sign_rules"]
    stoichs = ["NaC48", "NaC24", "NaC12", "NaC6"]
    scores = []
    for stoich in stoichs:
        item = next((i for i in artifact if i.get("stoichiometry") == stoich), None)
        v = item.get("intercalation_voltage_V") if item else None
        r = ref.get(stoich)
        if v is None or r is None or not isinstance(v, (int, float)):
            scores.append(0.0)
            continue
        rule = sign_rules.get(stoich)
        if rule == "positive":
            sign_ok = (v > 1e-6)
        elif rule == "negative":
            sign_ok = (v < -1e-6)
        else:
            sign_ok = True
        diff = abs(v - r)
        if sign_ok and diff <= tol:
            s = 1.0
        elif sign_ok and diff <= 2 * tol:
            s = 0.5
        elif sign_ok:
            s = 0.3
        else:
            s = 0.0
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'g_band_check': score_0,
    'k_point_check': score_1,
    'voltage_check': score_2,
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
