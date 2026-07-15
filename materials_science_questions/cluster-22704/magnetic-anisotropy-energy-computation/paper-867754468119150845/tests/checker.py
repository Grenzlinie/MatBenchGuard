import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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


# === block: score_0 (check id='step_02_mae') ===
def score_0(artifact, step, ctx):
    # artifact: list of csv dicts (columns: strain_state, spin_angle_deg, total_energy_eV, MAE_meV_per_fu)
    # step: dict with gold_mae_max, tolerance_meV_per_fu, angles_deg

    gold = step['gold_mae_max_meV_per_fu']
    tol = step['tolerance_meV_per_fu']
    angles_set = set(step['angles_deg'])

    groups = defaultdict(list)
    for row in artifact:
        state = row['strain_state']
        try:
            ang = int(float(row['spin_angle_deg']))
            E = float(row['total_energy_eV'])
        except (ValueError, KeyError):
            continue
        if ang not in angles_set:
            continue
        groups[state].append((ang, E))

    # compute E_min per strain state
    state_min_e = {}
    for state, pairs in groups.items():
        energies = [e for (_, e) in pairs]
        if energies:
            state_min_e[state] = min(energies)

    row_scores = []
    trend_scores = {}

    for state in ['relaxed', 'tensile_1pct', 'compressive_1pct']:
        if state not in groups or state not in gold:
            continue
        pairs = sorted(groups[state], key=lambda x: x[0])
        max_mae = gold[state]
        recomputed = []
        for ang, E in pairs:
            if state not in state_min_e:
                continue
            mae = (E - state_min_e[state]) * 1000.0 / 4.0  # eV -> meV/f.u.
            expected = max_mae * (math.sin(math.radians(ang)) ** 2)
            diff = abs(mae - expected)
            if diff <= tol:
                row_scores.append(1.0)
            else:
                row_scores.append(max(0.0, 1.0 - diff / tol))
            recomputed.append((ang, mae))
        # monotonic trend for relaxed and tensile
        if state in ('relaxed', 'tensile_1pct'):
            mae_vals = [m for (_, m) in recomputed]
            nondec = all(mae_vals[i] <= mae_vals[i+1] + 1e-9 for i in range(len(mae_vals)-1))
            trend_scores[state] = 1.0 if nondec else 0.0
        # for compressive, we do not enforce monotonic increase

    if row_scores:
        avg_row = sum(row_scores) / len(row_scores)
    else:
        avg_row = 0.0

    if trend_scores:
        trend_avg = sum(trend_scores.values()) / len(trend_scores)
    else:
        trend_avg = 1.0

    overall = 0.8 * avg_row + 0.2 * trend_avg
    return min(1.0, max(0.0, overall))


_SCORERS = {
    'step_02_mae': score_0,
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
