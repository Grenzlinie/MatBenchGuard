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


# === block: score_0 (check id='pressure_composition') ===
def score_0(artifact, step, ctx):
    import json
    gold = step.get("gold")
    tol = step.get("tolerance_abs_percent", 10)
    fields = []
    for pressure in ["P10", "P50"]:
        target = gold[pressure]
        actual = artifact.get(pressure, {})
        for species in ["fcc_percent", "hcp_percent", "bcc_percent"]:
            target_val = target[species]
            actual_val = actual.get(species, None)
            if actual_val is None or not isinstance(actual_val, (int, float)):
                return 0.0
            diff = abs(actual_val - target_val)
            if diff <= tol:
                score = 1.0
            elif diff <= 2*tol:
                score = 1.0 - (diff - tol) / tol
            else:
                score = 0.0
            fields.append(score)
    # trend checks
    p10_bcc = artifact["P10"]["bcc_percent"]
    p50_bcc = artifact["P50"]["bcc_percent"]
    p10_fcc = artifact["P10"]["fcc_percent"]
    p50_fcc = artifact["P50"]["fcc_percent"]
    trend_score = 0.0
    if p50_bcc > p10_bcc:
        trend_score += 0.5
    if p10_fcc > p50_fcc:
        trend_score += 0.5
    # combine 70% field accuracy, 30% trends
    field_acc = sum(fields) / len(fields) if fields else 0.0
    total = 0.7 * field_acc + 0.3 * trend_score
    return min(1.0, max(0.0, total))


# === block: score_1 (check id='temperature_hcp_counts') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    sizes = []
    for row in artifact:
        try:
            size = int(row["crystallite_size"])
            hcp22 = float(row["hcp_22pct"])
            hcp10 = float(row["hcp_10pct"])
            sizes.append((size, hcp22, hcp10))
        except (ValueError, KeyError):
            continue
    if not sizes:
        return 0.0
    sizes.sort(key=lambda x: x[0])
    # trend1: hcp22 >= 1.5 * hcp10 at max size
    _, hcp22_max, hcp10_max = sizes[-1]
    trend1 = 1.0 if hcp22_max >= 1.5 * hcp10_max else 0.0
    # trend2: slope(10%) < 0.5 * slope(22%)
    if len(sizes) >= 2:
        size0, hcp22_0, hcp10_0 = sizes[0]
        size1, hcp22_1, hcp10_1 = sizes[-1]
        if size1 != size0:
            slope22 = (hcp22_1 - hcp22_0) / (size1 - size0)
            slope10 = (hcp10_1 - hcp10_0) / (size1 - size0)
            trend2 = 1.0 if slope10 < 0.5 * slope22 else 0.0
        else:
            trend2 = 0.0
    else:
        trend2 = 0.0
    total = (trend1 + trend2) / 2.0
    return total


_SCORERS = {
    'pressure_composition': score_0,
    'temperature_hcp_counts': score_1,
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
