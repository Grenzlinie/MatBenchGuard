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


# === block: score_0 (check id='elastic_check') ===
def score_0(artifact, step, ctx):
    if 'gold' not in step:
        return 0.0
    gold = step['gold']
    C11 = artifact.get('C11')
    C12 = artifact.get('C12')
    C44 = artifact.get('C44')
    B0 = artifact.get('B0')
    v = artifact.get('v')
    if any(x is None for x in [C11, C12, C44, B0, v]):
        return 0.0
    # Cubic mechanical stability
    if not (C11 - C12 > 0 and C44 > 0 and C11 + 2*C12 > 0 and C12 < C11):
        return 0.0
    tol_rel = float(step.get('tolerance_rel', 0.1))
    tol_abs_v = float(step.get('tolerance_abs_v', 0.01))
    def rel_score(val, ref, tol):
        err = abs(val - ref)
        max_err = tol * abs(ref)
        if err <= max_err:
            return 1.0
        return max(0.0, 1.0 - (err - max_err) / (max_err + 1e-15))
    sC11 = rel_score(C11, gold['C11'], tol_rel)
    sC12 = rel_score(C12, gold['C12'], tol_rel)
    sC44 = rel_score(C44, gold['C44'], tol_rel)
    sB0 = rel_score(B0, gold['B0'], tol_rel)
    if abs(v - gold['v']) <= tol_abs_v:
        sv = 1.0
    else:
        sv = max(0.0, 1.0 - (abs(v - gold['v']) - tol_abs_v) / 0.1)
    score = (sC11 + sC12 + sC44 + sB0 + sv) / 5.0
    return score


# === block: score_1 (check id='dielectric_check') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0
    energies = []
    eps2 = []
    for row in artifact:
        try:
            e = float(row['energy (eV)'])
            e2 = float(row['epsilon2'])
            energies.append(e)
            eps2.append(e2)
        except (ValueError, KeyError):
            continue
    if len(energies) < 3:
        return 0.0
    peaks = []
    for i in range(1, len(energies)-1):
        if eps2[i] > eps2[i-1] and eps2[i] > eps2[i+1]:
            peaks.append(energies[i])
    low_range = step.get('peaks', {}).get('low_energy_range', [0.0, 15.0])
    high_range = step.get('peaks', {}).get('high_energy_range', [25.0, 35.0])
    has_low = any(low_range[0] <= p <= low_range[1] for p in peaks)
    has_high = any(high_range[0] <= p <= high_range[1] for p in peaks)
    score = (0.5 if has_low else 0.0) + (0.5 if has_high else 0.0)
    return score


_SCORERS = {
    'elastic_check': score_0,
    'dielectric_check': score_1,
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
