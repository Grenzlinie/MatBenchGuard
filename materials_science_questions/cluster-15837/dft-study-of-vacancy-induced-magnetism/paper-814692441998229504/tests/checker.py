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


# === block: score_0 (check id='schema') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 4:
        return 0.0
    required_configs = {"B15N16/C32", "B16N16/C31", "B15CN16/C31", "B16N15C/C31"}
    seen = set()
    for entry in artifact:
        if not isinstance(entry, dict):
            return 0.0
        if not all(k in entry for k in ("configuration", "total_magnetic_moment_muB", "majority_band_gap_eV", "minority_band_gap_eV", "spin_polarization_percent")):
            return 0.0
        seen.add(entry["configuration"])
    return 1.0 if seen == required_configs else 0.0


# === block: score_1 (check id='magnetic_moments') ===
def score_1(artifact, step, ctx):
    gold = step.get("gold", {})
    tol = step.get("tolerance", 0.2)
    pass_count = 0
    for entry in artifact:
        cfg = entry.get("configuration")
        if cfg in gold:
            val = entry.get("total_magnetic_moment_muB")
            if isinstance(val, (int, float)) and abs(val - gold[cfg]) <= tol:
                pass_count += 1
    return pass_count / 4.0 if gold else 0.0


# === block: score_2 (check id='band_gaps') ===
def score_2(artifact, step, ctx):
    gold = step.get("gold", {})
    tol = step.get("tolerance", 0.5)
    total_checks = 0
    pass_checks = 0
    for entry in artifact:
        cfg = entry.get("configuration")
        if cfg in gold:
            for spin in ("majority", "minority"):
                target = gold[cfg].get(spin)
                if target is not None:
                    key = "majority_band_gap_eV" if spin == "majority" else "minority_band_gap_eV"
                    val = entry.get(key)
                    if isinstance(val, (int, float)) and abs(val - target) <= tol:
                        pass_checks += 1
                    total_checks += 1
    return pass_checks / total_checks if total_checks > 0 else 0.0


# === block: score_3 (check id='half_metallic') ===
def score_3(artifact, step, ctx):
    target_cfg = "B15CN16/C31"
    for entry in artifact:
        if entry.get("configuration") == target_cfg:
            val = entry.get("spin_polarization_percent")
            if isinstance(val, (int, float)) and val >= 95:
                return 1.0
            else:
                return 0.0
    return 0.0


# === block: score_4 (check id='asymmetric_semiconductor') ===
def score_4(artifact, step, ctx):
    target_cfg = "B16N15C/C31"
    for entry in artifact:
        if entry.get("configuration") == target_cfg:
            maj = entry.get("majority_band_gap_eV")
            min_ = entry.get("minority_band_gap_eV")
            if isinstance(maj, (int, float)) and isinstance(min_, (int, float)):
                if maj > 0 and min_ > 0 and maj < min_:
                    return 1.0
            return 0.0
    return 0.0


_SCORERS = {
    'schema': score_0,
    'magnetic_moments': score_1,
    'band_gaps': score_2,
    'half_metallic': score_3,
    'asymmetric_semiconductor': score_4,
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
