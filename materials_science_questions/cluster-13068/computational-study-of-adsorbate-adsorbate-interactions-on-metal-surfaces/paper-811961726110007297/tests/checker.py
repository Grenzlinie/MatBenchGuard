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


# === block: score_0 (check id='analytical_restoring_force') ===
def score_0(artifact, step, ctx):
        # artifact is dict
        score_total = 0.0
        # 1. Equilibrium restoring force
        eq_force = artifact.get('restoring_force_at_equilibrium_meV_per_Ang', None)
        if eq_force is None or not isinstance(eq_force, (int, float)):
            return 0.0
        target = step.get('equilibrium_force_target_meV_per_Ang', 9.0)
        tol = step.get('equilibrium_force_tolerance_abs', 3.0)
        diff = abs(eq_force - target)
        if diff <= tol:
            force_score = 1.0
        else:
            force_score = max(0.0, 1.0 - (diff - tol) / tol)
        score_total += 0.5 * force_score

        # 2. Critical distance
        crit_z = artifact.get('critical_z_Ang', None)
        if crit_z is not None and isinstance(crit_z, (int, float)):
            target_z = step.get('critical_z_target_Ang', 2.78)
            z_tol = step.get('critical_z_tolerance_abs', 0.1)
            if abs(crit_z - target_z) <= z_tol:
                score_total += 0.1

        # 3. z_vs_F trend
        z_list = artifact.get('z_vs_F', None)
        if isinstance(z_list, list) and len(z_list) > 0:
            # sort by z ascending (from eq to smaller values)
            sorted_list = sorted(z_list, key=lambda p: p.get('z_Ang', 0.0))
            forces = [p.get('restoring_force_meV_per_Ang', None) for p in sorted_list]
            if None not in forces and len(forces) > 1:
                # forces should not increase (non-increasing)
                non_increasing = all(forces[i] >= forces[i+1] - 1e-9 for i in range(len(forces)-1))
                if non_increasing:
                    # final force (lowest z) must be very small
                    if forces[-1] <= 0.5:
                        trend_score = 1.0
                    else:
                        trend_score = 0.5
                else:
                    trend_score = 0.0
                score_total += 0.4 * trend_score
        return min(1.0, score_total)


# === block: score_1 (check id='static_friction') ===
def score_1(artifact, step, ctx):
        friction_col = step.get('friction_column', 'static_friction_meV_per_Ang')
        if not artifact:
            return 0.0
        required = ['pressure_GPa', friction_col]
        if not all(col in artifact[0] for col in required):
            return 0.0
        score = 0.0
        # at least 5 points
        if len(artifact) >= 5:
            score += 0.1
        pressures = []
        frictions = []
        for row in artifact:
            try:
                p = float(row['pressure_GPa'])
                f = float(row[friction_col])
                pressures.append(p)
                frictions.append(f)
            except (ValueError, TypeError):
                return 0.0
        if len(pressures) < 2:
            return 0.0
        # pressure range
        if min(pressures) <= 1.0 and max(pressures) >= 5.5:
            score += 0.15
        # all positive
        if all(p > 0 for p in pressures) and all(f > 0 for f in frictions):
            score += 0.1
        # monotonic non-increasing after sorting by pressure
        sorted_pairs = sorted(zip(pressures, frictions), key=lambda x: x[0])
        sorted_f = [f for _, f in sorted_pairs]
        non_inc = all(sorted_f[i] >= sorted_f[i+1] - 1e-9 for i in range(len(sorted_f)-1))
        if non_inc:
            score += 0.3
        # near-vanishing at high pressure (>=4.5 GPa) friction <= 20% of max friction
        max_f = max(frictions)
        if max_f > 0:
            high_p_frictions = [f for p, f in zip(pressures, frictions) if p >= 4.5]
            if high_p_frictions:
                max_high = max(high_p_frictions)
                if max_high <= 0.2 * max_f:
                    score += 0.35
        return min(1.0, score)


# === block: score_2 (check id='kinetic_friction') ===
def score_2(artifact, step, ctx):
        friction_col = step.get('friction_column', 'kinetic_friction_meV_per_Ang')
        if not artifact:
            return 0.0
        required = ['pressure_GPa', friction_col]
        if not all(col in artifact[0] for col in required):
            return 0.0
        score = 0.0
        if len(artifact) >= 5:
            score += 0.1
        pressures = []
        frictions = []
        for row in artifact:
            try:
                p = float(row['pressure_GPa'])
                f = float(row[friction_col])
                pressures.append(p)
                frictions.append(f)
            except (ValueError, TypeError):
                return 0.0
        if len(pressures) < 2:
            return 0.0
        if min(pressures) <= 1.0 and max(pressures) >= 5.5:
            score += 0.15
        if all(p > 0 for p in pressures) and all(f > 0 for f in frictions):
            score += 0.1
        sorted_pairs = sorted(zip(pressures, frictions), key=lambda x: x[0])
        sorted_f = [f for _, f in sorted_pairs]
        non_inc = all(sorted_f[i] >= sorted_f[i+1] - 1e-9 for i in range(len(sorted_f)-1))
        if non_inc:
            score += 0.3
        max_f = max(frictions)
        if max_f > 0:
            high_p_frictions = [f for p, f in zip(pressures, frictions) if p >= 4.5]
            if high_p_frictions:
                max_high = max(high_p_frictions)
                if max_high <= 0.2 * max_f:
                    score += 0.35
        return min(1.0, score)


_SCORERS = {
    'analytical_restoring_force': score_0,
    'static_friction': score_1,
    'kinetic_friction': score_2,
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
