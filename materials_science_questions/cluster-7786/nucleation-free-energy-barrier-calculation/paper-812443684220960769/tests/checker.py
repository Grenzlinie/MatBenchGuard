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


# === block: score_0 (check id='compute_albon_dunning') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_cols = {'c', 'V_d2', 'V_d6', 'V_d10'}
    if not required_cols.issubset(set(artifact[0].keys())):
        return 0.0
    if len(artifact) != 101:
        return 0.0
    c_expected = [i * 0.01 for i in range(101)]
    V0 = 5.8e-7
    correct = 0
    total = 0
    for i, row in enumerate(artifact):
        try:
            c = float(row['c'])
        except (ValueError, KeyError):
            return 0.0
        if not math.isclose(c, c_expected[i], rel_tol=1e-9, abs_tol=1e-12):
            return 0.0
        for d in (2, 6, 10):
            expected = V0 * (d - (1 - c) * d + (1 - c)) * ((1 - c) ** d)
            try:
                val = float(row['V_d' + str(d)])
            except (ValueError, KeyError):
                return 0.0
            if math.isclose(val, expected, rel_tol=1e-12, abs_tol=1e-12):
                correct += 1
            total += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='compute_cabrera_vermilyea') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_cols = {
        'x',
        'V_squeezing_d2','V_squeezing_d5','V_squeezing_d10',
        'V_flux_d2','V_flux_d5','V_flux_d10',
        'V_combined_d2','V_combined_d5','V_combined_d10'
    }
    if not required_cols.issubset(set(artifact[0].keys())):
        return 0.0
    if len(artifact) != 1001:
        return 0.0
    x_expected = [i * 0.001 for i in range(1001)]
    V0 = 5.8e-7
    correct = 0
    total = 0
    for i, row in enumerate(artifact):
        try:
            x = float(row['x'])
        except (ValueError, KeyError):
            return 0.0
        if not math.isclose(x, x_expected[i], rel_tol=1e-9, abs_tol=1e-12):
            return 0.0
        for d in (2, 5, 10):
            arg_sq = 1 - d * math.sqrt(x)
            expected_sq = V0 * math.sqrt(arg_sq) if arg_sq >= 0 else 0.0
            expected_fl = V0 * (1 - x)
            expected_cb = V0 * (1 - x) * math.sqrt(arg_sq) if arg_sq >= 0 else 0.0
            try:
                val_sq = float(row['V_squeezing_d' + str(d)])
                val_fl = float(row['V_flux_d' + str(d)])
                val_cb = float(row['V_combined_d' + str(d)])
            except (ValueError, KeyError):
                return 0.0
            if math.isclose(val_sq, expected_sq, rel_tol=1e-12, abs_tol=1e-12):
                correct += 1
            total += 1
            if math.isclose(val_fl, expected_fl, rel_tol=1e-12, abs_tol=1e-12):
                correct += 1
            total += 1
            if math.isclose(val_cb, expected_cb, rel_tol=1e-12, abs_tol=1e-12):
                correct += 1
            total += 1
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='conclusion') ===
def score_2(artifact, step, ctx):
    import re
    if not isinstance(artifact, str) or not artifact.strip():
        return 0.0
    text = artifact.strip().lower()
    plateau_patterns = [
        r'no\s+plateau',
        r'plateau\s+not\s+observed',
        r'plateau\s+is\s+not\s+observed',
        r'plateau\s+not\s+found',
        r'absence\s+of\s+plateau',
        r'plateau\s+absent',
        r'no\s+plateau\s+region',
    ]
    for pat in plateau_patterns:
        if re.search(pat, text):
            return 1.0
    return 0.0


_SCORERS = {
    'compute_albon_dunning': score_0,
    'compute_cabrera_vermilyea': score_1,
    'conclusion': score_2,
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
