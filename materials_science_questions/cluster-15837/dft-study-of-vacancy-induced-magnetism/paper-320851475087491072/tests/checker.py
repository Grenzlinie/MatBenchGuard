import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        return {"steps_dict": {s["id"]: s for s in steps}}


# === block: score_0 (check id='magnetic_moment') ===
def score_0(artifact, step, ctx):
    # artifact is the raw text content (string) from magnetic_moment.txt
    val = float(artifact.strip())
    lower = step['lower']
    upper = step['upper']
    if lower <= val <= upper:
        return 1.0
    if val < lower:
        score = max(0.0, 1 - (lower - val) / (lower - step['lower_min']))
    else:
        score = max(0.0, 1 - (val - upper) / (step['upper_max'] - upper))
    return round(score, 4)


# === block: score_1 (check id='dos_half_metallic') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is a list of dicts (TSV parsed) or list of rows? The loader returns list of dicts for TSV.
        # We'll assume artifact is a list of dicts with keys: energy, majority_dos, minority_dos.
        if not artifact or not isinstance(artifact, list):
            return 0.0
        energies = []
        maj_dos = []
        min_dos = []
        for row in artifact:
            try:
                e = float(row['energy'])
                maj = float(row['majority_dos'])
                min_ = float(row['minority_dos'])
                energies.append(e)
                maj_dos.append(maj)
                min_dos.append(min_)
            except (KeyError, ValueError):
                continue
        if not energies:
            return 0.0
        win_low, win_high = step['energy_window']
        points_maj = []
        points_min = []
        for e, maj, min_ in zip(energies, maj_dos, min_dos):
            if win_low <= e <= win_high:
                points_maj.append(maj)
                points_min.append(min_)
        if points_maj:
            min_maj = min(points_maj)
            max_min = max(points_min)
        else:
            # fallback: pick closest energy to 0
            idx = min(range(len(energies)), key=lambda i: abs(energies[i]))
            min_maj = maj_dos[idx]
            max_min = min_dos[idx]
        maj_gap = min_maj < step['majority_spin_gap_threshold']
        min_metallic = max_min > step['minority_spin_metallic_threshold']
        if maj_gap and min_metallic:
            return 1.0
        if maj_gap or min_metallic:
            return 0.5
        return 0.0


_SCORERS = {
    'magnetic_moment': score_0,
    'dos_half_metallic': score_1,
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
