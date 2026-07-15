import os
import json
import csv

# === author imports / helpers ===
import csv, os, math

def _compute_band_gap(rows, dos_threshold):
    energies = []
    dos_vals = []
    for r in rows:
        energies.append(float(r['energy']))
        dos_vals.append(float(r['dos_total']))
    groups = []
    cur = []
    for i in range(len(energies)):
        if dos_vals[i] >= dos_threshold:
            cur.append(i)
        else:
            if cur:
                groups.append(cur)
                cur = []
    if cur:
        groups.append(cur)
    if not groups:
        return None, None
    best_gap = -1
    best_vbm = None
    best_cbm = None
    for k in range(len(groups)-1):
        g1 = groups[k]
        g2 = groups[k+1]
        if energies[g1[-1]] < energies[g2[0]]:
            gap = energies[g2[0]] - energies[g1[-1]]
            if gap > best_gap:
                best_gap = gap
                best_vbm = energies[g1[-1]]
                best_cbm = energies[g2[0]]
    return best_vbm, best_cbm


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
    import csv, os, math

    def _compute_band_gap(rows, dos_threshold):
        energies = []
        dos_vals = []
        for r in rows:
            energies.append(float(r['energy']))
            dos_vals.append(float(r['dos_total']))
        groups = []
        cur = []
        for i in range(len(energies)):
            if dos_vals[i] >= dos_threshold:
                cur.append(i)
            else:
                if cur:
                    groups.append(cur)
                    cur = []
        if cur:
            groups.append(cur)
        if not groups:
            return None, None
        best_gap = -1
        best_vbm = None
        best_cbm = None
        for k in range(len(groups)-1):
            g1 = groups[k]
            g2 = groups[k+1]
            if energies[g1[-1]] < energies[g2[0]]:
                gap = energies[g2[0]] - energies[g1[-1]]
                if gap > best_gap:
                    best_gap = gap
                    best_vbm = energies[g1[-1]]
                    best_cbm = energies[g2[0]]
        return best_vbm, best_cbm

    lto_gap = None
    lto_path = os.path.join(outputs_dir, 'dos_LTO.csv')
    if os.path.exists(lto_path):
        with open(lto_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if rows:
            vbm, cbm = _compute_band_gap(rows, 0.01)
            if vbm is not None and cbm is not None:
                lto_gap = cbm - vbm
    return {'lto_gap': lto_gap}


# === block: score_0 (check id='dos_LTO') ===
def score_0(artifact, step, ctx):
    import sys

    def _compute_band_gap(rows, dos_threshold):
        energies = []
        dos_vals = []
        for r in rows:
            energies.append(float(r['energy']))
            dos_vals.append(float(r['dos_total']))
        groups = []
        cur = []
        for i in range(len(energies)):
            if dos_vals[i] >= dos_threshold:
                cur.append(i)
            else:
                if cur:
                    groups.append(cur)
                    cur = []
        if cur:
            groups.append(cur)
        if not groups:
            return None, None
        best_gap = -1
        best_vbm = None
        best_cbm = None
        for k in range(len(groups)-1):
            g1 = groups[k]
            g2 = groups[k+1]
            if energies[g1[-1]] < energies[g2[0]]:
                gap = energies[g2[0]] - energies[g1[-1]]
                if gap > best_gap:
                    best_gap = gap
                    best_vbm = energies[g1[-1]]
                    best_cbm = energies[g2[0]]
        return best_vbm, best_cbm

    # Inject helper into module globals so other scorers can use it
    globals()['_compute_band_gap'] = _compute_band_gap

    if artifact is None or not artifact:
        return 0.0
    vbm, cbm = _compute_band_gap(artifact, 0.01)
    if vbm is None or cbm is None:
        return 0.0
    gap = cbm - vbm
    lo, hi = step.get('check', {}).get('band_gap_range', [1.7, 2.3])
    if lo <= gap <= hi:
        return 1.0
    elif gap > 0:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='dos_LMTZO_Ov') ===
def score_1(artifact, step, ctx):
    if artifact is None or not artifact:
        return 0.0
    vbm, cbm = _compute_band_gap(artifact, 0.01)
    if vbm is None or cbm is None:
        gap_ov = None
    else:
        gap_ov = cbm - vbm
    # Fermi level check: find energy closest to 0
    energies = [float(r['energy']) for r in artifact]
    dos_vals = [float(r['dos_total']) for r in artifact]
    closest_idx = min(range(len(energies)), key=lambda i: abs(energies[i]))
    fermi_dos = dos_vals[closest_idx]
    lto_gap = ctx.get('lto_gap')
    score = 0.0
    if lto_gap is not None and gap_ov is not None and gap_ov <= lto_gap - 0.1:
        score += 0.5
    if fermi_dos > 0.01:
        score += 0.5
    return score


# === block: score_2 (check id='migration_barriers') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    ref = step.get('reference', {})
    tol = float(step.get('tolerance', 0.05))
    barrier_lmtzo = artifact.get('LMTZO')
    barrier_ov = artifact.get('LMTZO_Ov')
    if barrier_lmtzo is None or barrier_ov is None:
        return 0.0
    try:
        barrier_lmtzo = float(barrier_lmtzo)
        barrier_ov = float(barrier_ov)
    except (ValueError, TypeError):
        return 0.0
    err_lmtzo = abs(barrier_lmtzo - ref.get('LMTZO', 0.415))
    err_ov = abs(barrier_ov - ref.get('LMTZO_Ov', 0.345))
    within = (err_lmtzo <= tol and err_ov <= tol)
    ordering_ok = (barrier_ov < barrier_lmtzo)
    score = (0.6 if within else 0.0) + (0.4 if ordering_ok else 0.0)
    return score


_SCORERS = {
    'dos_LTO': score_0,
    'dos_LMTZO_Ov': score_1,
    'migration_barriers': score_2,
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
