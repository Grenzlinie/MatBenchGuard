import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    ref = step.get('reference', {})
    tol_length = step.get('tol_length', 0.05)
    tol_angle = step.get('tol_angle', 2.0)
    if not ref:
        return 0.0
    submitted = {}
    for row in artifact_rows:
        name = row['bond_or_angle'].strip()
        try:
            val = float(row['value'])
            unit = row['unit'].strip()
            submitted[name] = (val, unit)
        except (KeyError, ValueError):
            continue
    matches = 0
    for name, exp_val in ref.items():
        if name not in submitted:
            continue
        val, unit = submitted[name]
        tol = tol_angle if unit == '°' else tol_length
        if abs(val - exp_val) <= tol + 1e-9:
            matches += 1
    return matches / len(ref) if ref else 0.0


# === block: score_1 (check id='step3') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step.get('reference', {})
    tol_pop = step.get('tol_pop', 0.05)
    tol_len = step.get('tol_length', 0.05)
    if not ref:
        return 0.0
    submitted = {}
    for row in rows:
        bond = row['bond'].strip()
        try:
            pop = float(row['population'])
            length = float(row['length'])
            submitted[bond] = (pop, length)
        except (KeyError, ValueError):
            continue
    matches = 0
    for name, v in ref.items():
        if name not in submitted:
            continue
        pop, length = submitted[name]
        if (abs(pop - v['population']) <= tol_pop + 1e-9 and
            abs(length - v['length']) <= tol_len + 1e-9):
            matches += 1
    return matches / len(ref) if ref else 0.0


# === block: score_2 (check id='step4') ===
def score_2(artifact, step, ctx):
    e_min, e_max = step['energy_range']
    # parse rows and sort by energy
    data = []
    for row in artifact:
        try:
            e = float(row['energy'])
            o = float(row['pdos_O_2p'])
            h = float(row['pdos_H_1s'])
            data.append((e, o, h))
        except (KeyError, ValueError):
            continue
    if not data:
        return 0.0
    data.sort(key=lambda x: x[0])
    energies = [d[0] for d in data]
    o_vals = [d[1] for d in data]
    h_vals = [d[2] for d in data]
    def has_local_peak(energies, vals, lo, hi):
        for i in range(1, len(energies)-1):
            if lo <= energies[i] <= hi:
                if vals[i] > vals[i-1] and vals[i] > vals[i+1]:
                    return True
        return False
    peak_o = has_local_peak(energies, o_vals, e_min, e_max)
    peak_h = has_local_peak(energies, h_vals, e_min, e_max)
    return 1.0 if peak_o and peak_h else 0.0


_SCORERS = {
    'step2': score_0,
    'step3': score_1,
    'step4': score_2,
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
