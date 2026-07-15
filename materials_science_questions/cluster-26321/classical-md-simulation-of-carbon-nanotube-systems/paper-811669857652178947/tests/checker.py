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


# === block: score_0 (check id='rdf_sp3_peak') ===
def score_0(artifact, step, ctx):
        groups = {}
        for row in artifact:
            try:
                temp = float(row['temperature'])
                dist = float(row['distance'])
                intens = float(row['intensity'])
                groups.setdefault(temp, []).append((dist, intens))
            except:
                pass
        if not groups:
            return 0.0
        all_intens = [intens for pairs in groups.values() for _, intens in pairs]
        global_max = max(all_intens) if all_intens else 0.0
        if global_max == 0.0:
            return 0.0
        target_temps = [0, 300, 800, 1600]
        score = 0.0
        for t in target_temps:
            if t not in groups:
                continue
            window_max = 0.0
            for dist, intens in groups[t]:
                if 1.5 <= dist <= 1.6:
                    if intens > window_max:
                        window_max = intens
            normalized = window_max / global_max
            if t == 0:
                if normalized <= 0.15:
                    score += 1
            else:
                if normalized >= 0.25:
                    score += 1
        return score / len(target_temps)


# === block: score_1 (check id='yielding_strain_trends') ===
def score_1(artifact, step, ctx):
        required_defects = ['sp3', 'rotation']
        required_temps = [300, 800, 1600]
        required_rates = [2.0, 0.1, 0.0125]
        data = {}
        for row in artifact:
            try:
                defect = row['defect_type'].strip().lower()
                temp = int(float(row['temperature']))
                rate = float(row['strain_rate'])
                strain = float(row['yielding_strain'])
                data[(defect, temp, rate)] = strain
            except:
                pass
        total = 0
        correct = 0
        for defect in required_defects:
            # Temperature monotonicity for each strain rate
            for rate in required_rates:
                vals = [data.get((defect, temp, rate)) for temp in required_temps]
                for i in range(len(vals)-1):
                    total += 1
                    if vals[i] is not None and vals[i+1] is not None and vals[i] >= vals[i+1]:
                        correct += 1
            # Strain‑rate monotonicity for each temperature
            for temp in required_temps:
                vals = [data.get((defect, temp, rate)) for rate in required_rates]
                for i in range(len(vals)-1):
                    total += 1
                    if vals[i] is not None and vals[i+1] is not None and vals[i] >= vals[i+1]:
                        correct += 1
        if total == 0:
            return 0.0
        return correct / total


_SCORERS = {
    'rdf_sp3_peak': score_0,
    'yielding_strain_trends': score_1,
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
