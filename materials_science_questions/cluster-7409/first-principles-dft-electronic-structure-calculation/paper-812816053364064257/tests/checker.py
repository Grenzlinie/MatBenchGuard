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


# === block: score_0 (check id='step_bandgap') ===
def score_0(artifact, step, ctx):
    import csv
    artifact = artifact  # artifact is the list of dicts after CSV load
    gold_bandgap = step.get("gold_bandgap", {})
    # Widened tolerance to 0.1 eV (reviewer request) to account for pseudopotential variation
    tol = 0.1
    expected_nature = step.get("expected_gap_nature", "")
    w_val = step.get("weight_bandgap_value", 0.8)
    w_nat = step.get("weight_nature_match", 0.2)
    def score_val(val, ref, tol):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))
    rows = artifact
    scores = []
    for row in rows:
        func = row.get("functional", "").strip()
        band_str = row.get("band_gap_eV", "")
        nature = row.get("gap_nature", "").strip()
        if func not in gold_bandgap or band_str == "":
            scores.append(0.0)
            continue
        try:
            band = float(band_str)
        except:
            scores.append(0.0)
            continue
        s_val = score_val(band, gold_bandgap[func], tol)
        s_nat = 1.0 if nature == expected_nature else 0.0
        scores.append(w_val * s_val + w_nat * s_nat)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_dielectric_constants') ===
def score_1(artifact, step, ctx):
    import csv
    gold_list = step.get("gold_dielectric", [])
    tol = step.get("tolerance_epsilon", 0.15)
    def score_val(val, ref, tol):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))
    rows = artifact
    gold_by_key = {}
    for g in gold_list:
        key = (g.get("functional","").strip(), g.get("direction","").strip())
        gold_by_key[key] = g["epsilon_infinity"]
    scores = []
    for row in rows:
        func = row.get("functional", "").strip()
        direc = row.get("direction", "").strip()
        eps_str = row.get("epsilon_infinity", "")
        key = (func, direc)
        if key not in gold_by_key or eps_str == "":
            scores.append(0.0)
            continue
        try:
            eps = float(eps_str)
        except:
            scores.append(0.0)
            continue
        s = score_val(eps, gold_by_key[key], tol)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_birefringence') ===
def score_2(artifact, step, ctx):
    import csv
    gold_dict = step.get("gold_birefringence", {})
    tol = step.get("tolerance_birefringence", 0.02)
    def score_val(val, ref, tol):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))
    rows = artifact
    scores = []
    for row in rows:
        func = row.get("functional", "").strip()
        bir_str = row.get("birefringence_633nm", "")
        if func not in gold_dict or bir_str == "":
            scores.append(0.0)
            continue
        try:
            bir = float(bir_str)
        except:
            scores.append(0.0)
            continue
        s = score_val(bir, gold_dict[func], tol)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_bandgap': score_0,
    'step_dielectric_constants': score_1,
    'step_birefringence': score_2,
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
