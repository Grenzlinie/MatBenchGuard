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


# === block: score_0 (check id='equilibrium_concentrations') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    ref = step.get('reference', {})
    abs_small = step.get('tolerance_abs_small', 0.0001)
    rel_large = step.get('tolerance_rel_large', 0.1)
    i5_thr = step.get('i5_threshold', 34.0)
    fields = ['C_eq', 'Cr_eq', 'Nb_eq', 'NbC_eq', 'Cr23C6_eq']
    score = 0.0
    total = 0
    for entry in data:
        t = str(entry.get('temperature_C', ''))
        if t not in ref:
            continue
        r = ref[t]
        for f in fields:
            val = entry.get(f)
            gold = r.get(f)
            if gold is None:
                continue
            total += 1
            if gold > 0.001:
                if abs(val - gold) / gold <= rel_large:
                    score += 1.0
            else:
                if abs(val - gold) <= abs_small:
                    score += 1.0
        i5 = entry.get('i5_over_i1')
        if i5 is not None:
            total += 1
            if i5 >= i5_thr:
                score += 1.0
    if total == 0:
        return 0.0
    return score / total


# === block: score_1 (check id='rate_constants') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    k0 = artifact.get('k0')
    En = artifact.get('En')
    if k0 is None or En is None:
        return 0.0
    k0_target = step.get('k0_target', 67400)
    En_target = step.get('En_target', 92800)
    factor = step.get('factor', 2.0)
    ok_k0 = (k0_target/factor <= k0 <= k0_target*factor)
    ok_En = (En_target/factor <= En <= En_target*factor)
    return 1.0 if (ok_k0 and ok_En) else 0.0


# === block: score_2 (check id='kinetic_curve') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    points = step.get('points', {})
    if not points:
        return 0.0
    tol_rel = step.get('tolerance_rel', 0.20)
    lookup = {}
    for r in rows:
        try:
            t = int(float(r['temperature_C']))
            time_h = int(float(r['time_h']))
            val = float(r['Cr23C6_mass_fraction'])
        except (KeyError, ValueError):
            continue
        key = f"{t}_{time_h}"
        if key not in lookup:
            lookup[key] = []
        lookup[key].append(val)
    score_points = 0
    total_points = len(points)
    for key, ref_val in points.items():
        vals = lookup.get(key, [])
        if not vals:
            continue
        used = vals[0]
        err = abs(used - ref_val) / ref_val if ref_val != 0 else abs(used)
        if err <= tol_rel:
            score_points += 1.0
        else:
            partial = max(0.0, 1.0 - (err - tol_rel) / tol_rel)
            score_points += partial
    if total_points == 0:
        return 0.0
    return score_points / total_points


# === block: score_3 (check id='stabilization_time') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    tau_ref = step.get('tau_ref', {})
    tol_factor = step.get('tolerance_factor', 2.0)
    lookup = {}
    for r in rows:
        try:
            t = str(int(float(r['temperature_C'])))
            tau = float(r['tau_star_h'])
        except (KeyError, ValueError):
            continue
        lookup[t] = tau
    total = len(tau_ref)
    if total == 0:
        return 0.0
    score = 0.0
    for t, ref_tau in tau_ref.items():
        tau = lookup.get(t)
        if tau is None:
            continue
        low = ref_tau / tol_factor
        high = ref_tau * tol_factor
        if low <= tau <= high:
            score += 1.0
    return score / total


_SCORERS = {
    'equilibrium_concentrations': score_0,
    'rate_constants': score_1,
    'kinetic_curve': score_2,
    'stabilization_time': score_3,
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
