import os
import json
import csv

# === author imports / helpers ===
import csv
from collections import defaultdict


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


# === block: score_0 (check id='check_energy_moment') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # group by a
    data_by_a = defaultdict(list)
    for r in rows:
        try:
            a_val = float(r['a'])
            phi = float(r['phi'])
            energy = float(r['total_energy'])
            moment = float(r['fe_spin_moment'])
        except (KeyError, ValueError):
            return 0.0
        data_by_a[a_val].append((phi, energy, moment))

    a_vals = [3.97, 3.85, 3.75, 3.70]
    tol_phi_zero = 0.02
    min_deltaE_fm = -0.005   # allow tiny negative due to numerical noise

    phi_mins = {}
    deltaE_mins = {}
    moment_at_min = {}
    for a in a_vals:
        if a not in data_by_a:
            return 0.0
        points = data_by_a[a]
        e0 = None
        for phi, energy, _ in points:
            if abs(phi) < 1e-6:
                e0 = energy
                break
        if e0 is None:
            return 0.0
        best_phi = None
        best_dE = None
        best_moment = None
        for phi, energy, moment in points:
            dE = energy - e0
            if best_dE is None or dE < best_dE or (abs(dE - best_dE) < 1e-9 and phi < best_phi):
                best_dE = dE
                best_phi = phi
                best_moment = moment
        phi_mins[a] = best_phi
        deltaE_mins[a] = best_dE
        moment_at_min[a] = best_moment

    score = 0.0

    # Helical classification: a=3.97,3.85,3.75 must have φ_min>0 and ΔE_min<0
    for a in [3.97, 3.85, 3.75]:
        if phi_mins[a] > 0 and deltaE_mins[a] < 0:
            score += 0.15

    # FM at a=3.70: φ_min near 0 and ΔE_min not significantly negative
    if abs(phi_mins[3.70]) <= tol_phi_zero and deltaE_mins[3.70] >= min_deltaE_fm:
        score += 0.20

    # Trend: φ_min increases as a decreases (3.97 < 3.85 < 3.75)
    if phi_mins[3.97] + 1e-9 < phi_mins[3.85] and phi_mins[3.85] + 1e-9 < phi_mins[3.75]:
        score += 0.20

    # Moment trend: M(3.97) >= M(3.85) >= M(3.75) >= M(3.70) within tolerance
    m = [moment_at_min[a] for a in a_vals]
    trend_ok = True
    for i in range(3):
        if m[i] + 0.1 < m[i+1]:  # tolerance 0.1 μ_B to absorb fluctuations
            trend_ok = False
            break
    if trend_ok:
        score += 0.15

    return score


_SCORERS = {
    'check_energy_moment': score_0,
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
