import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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


# === block: score_0 (check id='p63_gga_gap_reported') ===
def score_0(artifact, step, ctx):
    phase = next((p for p in artifact['phases'] if p['name'] == 'P6_3'), None)
    if phase is None:
        return 0.0
    gap = phase['band_gap_GGA']
    target = step['target']
    tol = step['tolerance_abs']
    return 1.0 if abs(gap - target) <= tol else 0.0


# === block: score_1 (check id='p63_gga_gap_recomputed') ===
def score_1(artifact, step, ctx):
    kpts = artifact['kpoints']
    eig = artifact['eigenvalues']
    if len(kpts) != len(eig):
        return 0.0
    # collect all eigenvalues from all k-points
    all_ev = []
    for band_list in eig:
        all_ev.extend(band_list)
    pos = [e for e in all_ev if e >= 0.0]
    neg = [e for e in all_ev if e < 0.0]
    if not pos or not neg:
        return 0.0
    cbm = min(pos)
    vbm = max(neg)
    recomputed = cbm - vbm
    target = step['target']
    tol = step['tolerance_abs']
    return 1.0 if abs(recomputed - target) <= tol else 0.0


# === block: score_2 (check id='hybrid_gap') ===
def score_2(artifact, step, ctx):
    hyb = artifact.get('p6_3_hybrid_gap')
    if hyb is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_abs']
    return 1.0 if abs(hyb - target) <= tol else 0.0


# === block: score_3 (check id='other_gaps_order') ===
def score_3(artifact, step, ctx):
    phases = artifact['phases']
    gaps = {p['name']: p['band_gap_GGA'] for p in phases}
    others = ['P6_3/mmc', 'P-3c1', 'P6_3cm']
    if 'P6_3' not in gaps:
        return 0.0
    p63_gap = gaps['P6_3']
    max_others = step['max_gap_others']
    min_p63 = step['min_p63_gap']
    # all others must be <= max_others
    for name in others:
        if name in gaps and gaps[name] > max_others:
            return 0.0
    # P6_3 gap must be > min_p63
    if p63_gap <= min_p63:
        return 0.0
    # Also P6_3 must be the largest gap
    if any(gaps[name] > p63_gap for name in others if name in gaps):
        return 0.0
    return 1.0


# === block: score_4 (check id='p63_phonon_stable') ===
def score_4(artifact, step, ctx):
    freq = artifact['frequencies']
    tol = step['negative_tolerance']
    for qpt_modes in freq:
        for f in qpt_modes:
            if f < -tol:
                return 0.0
    return 1.0


# === block: score_5 (check id='stability_flags') ===
def score_5(artifact, step, ctx):
    phases = artifact['phases']
    flags = {p['name']: p['dynamically_stable'] for p in phases}
    if 'P6_3' not in flags or flags['P6_3'] != True:
        return 0.0
    target_names = ['P6_3/mmc', 'P-3c1', 'P6_3cm']
    for name in target_names:
        if name in flags and flags[name] != False:
            return 0.0
    return 1.0


_SCORERS = {
    'p63_gga_gap_reported': score_0,
    'p63_gga_gap_recomputed': score_1,
    'hybrid_gap': score_2,
    'other_gaps_order': score_3,
    'p63_phonon_stable': score_4,
    'stability_flags': score_5,
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
