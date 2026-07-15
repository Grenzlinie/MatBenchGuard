import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    ref = step.get('reference', {})
    tol = step.get('tolerance', 0.05)
    scores = []
    for defect, target in ref.items():
        vals = [float(r['E_F_eV']) for r in rows if r['defect_id'].strip() == defect]
        if not vals:
            scores.append(0.0)
            continue
        val = vals[0]  # expect one row per defect
        err = abs(val - target)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='neb_profiles') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step.get('reference', {})
    tol = step.get('tolerance', 0.05)
    defect_energies = {}
    for r in rows:
        did = r['defect_id'].strip()
        idx = int(r['replica_index'])
        e = float(r['energy_eV'])
        defect_energies.setdefault(did, []).append((idx, e))
    scores = []
    for did, target in ref.items():
        if did not in defect_energies:
            scores.append(0.0)
            continue
        pairs = defect_energies[did]
        if len(pairs) < 2:
            scores.append(0.0)
            continue
        e0 = [e for i, e in pairs if i == 0]
        if not e0:
            scores.append(0.0)
            continue
        max_e = max(e for _, e in pairs)
        barrier = max_e - e0[0]
        err = abs(barrier - target)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='electronic_DOS') ===
def score_2(artifact, step, ctx):
    rows = artifact
    ref = step.get('reference', {})
    tol = step.get('tolerance', 0.1)
    cutoff_ratio = 0.01
    defect_data = {}
    for r in rows:
        did = r['defect_id'].strip()
        e = float(r['energy_eV'])
        dos = float(r['dos_arbunits'])
        defect_data.setdefault(did, []).append((e, dos))
    scores = []
    for did, target in ref.items():
        if did not in defect_data:
            scores.append(0.0)
            continue
        pairs = sorted(defect_data[did], key=lambda x: x[0])
        energies = [e for e, _ in pairs]
        dos_vals = [d for _, d in pairs]
        # use relative cutoff: 1% of maximum DOS to tolerate smearing/noise
        max_dos = max(dos_vals) if dos_vals else 0.0
        cutoff = max_dos * cutoff_ratio if max_dos > 0 else 1e-6
        # locate gap intervals where DOS < cutoff
        gap_intervals = []
        in_gap = False
        start = None
        for e, d in zip(energies, dos_vals):
            if d < cutoff:
                if not in_gap:
                    start = e
                    in_gap = True
            else:
                if in_gap:
                    gap_intervals.append((start, e))
                    in_gap = False
        if in_gap:
            gap_intervals.append((start, energies[-1]))
        if not gap_intervals:
            scores.append(0.0)
            continue
        # select the widest gap around the Fermi level (energy zero)
        best_gap = None
        best_width = 0.0
        for lo, hi in gap_intervals:
            if lo <= 0 <= hi:  # gap containing zero
                w = hi - lo
                if w > best_width:
                    best_gap = w
                    best_width = w
            else:
                w = hi - lo
                if w > best_width:
                    best_gap = w
                    best_width = w
        if best_gap is None:
            scores.append(0.0)
            continue
        err = abs(best_gap - target)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='charge_density_profiles') ===
def score_3(artifact, step, ctx):
    rows = artifact
    ref = step.get('reference', {})
    tol = step.get('tolerance', 0.02)
    defect_data = {}
    for r in rows:
        did = r['defect_id'].strip()
        d = float(r['distance_along_NN_bond_Angstrom'])
        rho = float(r['charge_density_e_Bohr3'])
        defect_data.setdefault(did, []).append(rho)
    scores = []
    for did, target in ref.items():
        if did not in defect_data:
            scores.append(0.0)
            continue
        vals = defect_data[did]
        if not vals:
            scores.append(0.0)
            continue
        min_rho = min(vals)
        err = abs(min_rho - target)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'formation_energies': score_0,
    'neb_profiles': score_1,
    'electronic_DOS': score_2,
    'charge_density_profiles': score_3,
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
