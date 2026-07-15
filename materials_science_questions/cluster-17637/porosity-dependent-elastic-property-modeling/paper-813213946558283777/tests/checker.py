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
    Es = 110.0
    sigma_ys = 220.0
    data = [
        (900, 0.61, 19.33, 22.80),
        (1000, 0.62, 19.52, 23.25),
        (1100, 0.60, 19.57, 22.88),
        (1200, 0.62, 19.69, 24.20),
        (1300, 0.64, 19.33, 24.43),
    ]
    expected = {}
    for fst, rhor, d, t in data:
        l_oct = d / 2.41
        l_dc = d / 3.08
        C1_oct = 1.0 / (rhor ** 2 * (t / l_oct) ** 4)
        C1_dc = 1.0 / (rhor ** 2 * (t / l_dc) ** 4)
        E_oct = C1_oct * rhor ** 2 * Es
        E_dc = C1_dc * rhor ** 2 * Es
        sigma_mod = sigma_ys * rhor ** 2.5
        expected[fst] = {
            'E_oct': E_oct,
            'E_dc': E_dc,
            'sigma_mod': sigma_mod,
        }
    return {'expected': expected}


# === block: score_0 (check id='predict_properties') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    expected_map = ctx['expected']
    tol_E = 0.05
    tol_sig = 1.0
    total = 0
    correct = 0
    for fst, exp in expected_map.items():
        row = None
        for r in artifact_rows:
            if str(r.get('FST', '')).strip() == str(fst):
                row = r
                break
        if row is None:
            total += 3
            continue
        try:
            E_oc_val = float(row.get('E_oc_predicted', 0))
            E_dc_val = float(row.get('E_dc_predicted', 0))
            sigma_mod_val = float(row.get('sigma_modified_predicted', 0))
        except (ValueError, TypeError):
            total += 3
            continue
        if abs(E_oc_val - exp['E_oct']) <= tol_E:
            correct += 1
        if abs(E_dc_val - exp['E_dc']) <= tol_E:
            correct += 1
        if abs(sigma_mod_val - exp['sigma_mod']) <= tol_sig:
            correct += 1
        total += 3
    score = correct / total if total > 0 else 0.0
    return score


_SCORERS = {
    'predict_properties': score_0,
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
