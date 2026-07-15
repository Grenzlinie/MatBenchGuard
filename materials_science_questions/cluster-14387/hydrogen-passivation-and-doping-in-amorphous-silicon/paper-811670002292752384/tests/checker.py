import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def find_dos_gap(energies, dos):
    """Heuristically find VBM and CBM from DOS curve.
    Returns (gap, vbm_peak_val, cbm_peak_val, vbm_e, cbm_e).
    If gap not clearly identifiable, returns (0,0,0,0,0)."""
    # smooth slightly
    n = len(energies)
    if n < 5:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    # find global maximum as VBM
    idx_vbm = np.argmax(dos)
    vbm_peak = dos[idx_vbm]
    vbm_e = energies[idx_vbm]
    # after VBM, find first point where DOS drops below 5% of vbm_peak and stays low for a significant energy width
    threshold = 0.05 * vbm_peak
    # scan forward
    gap_start = None
    gap_end = None
    low_start = None
    for i in range(idx_vbm, n):
        if dos[i] < threshold:
            if low_start is None:
                low_start = i
        else:
            if low_start is not None:
                # check if low region width >= 0.2 eV
                width = energies[i-1] - energies[low_start]
                if width >= 0.2:
                    gap_end = i
                    break
                low_start = None
    if low_start is not None:
        # reached end with low region
        width = energies[-1] - energies[low_start]
        if width >= 0.2:
            gap_end = n
    if gap_end is None:
        # fallback: assume gap region after global max
        # try to find next peak after energy increase of 0.5 eV
        future = energies > vbm_e + 0.5
        if np.any(future):
            idx_cbm_candidates = np.where(future)[0]
            idx_cbm = idx_cbm_candidates[np.argmax(dos[idx_cbm_candidates])]
            cbm_e = energies[idx_cbm]
            cbm_peak = dos[idx_cbm]
            gap = cbm_e - vbm_e
            return gap, vbm_peak, cbm_peak, vbm_e, cbm_e
        else:
            return 0.0, vbm_peak, 0.0, vbm_e, 0.0
    # now from gap_end find next peak (CBM)
    if gap_end >= n:
        return 0.0, vbm_peak, 0.0, vbm_e, 0.0
    # find max in [gap_end, n-1]
    idx_cbm = np.argmax(dos[gap_end:]) + gap_end
    cbm_peak = dos[idx_cbm]
    cbm_e = energies[idx_cbm]
    # ensure we don't pick a tiny ripple; require cbm_peak > 0.1 * vbm_peak
    if cbm_peak < 0.1 * vbm_peak:
        return 0.0, vbm_peak, cbm_peak, vbm_e, cbm_e
    gap = cbm_e - vbm_e
    return gap, vbm_peak, cbm_peak, vbm_e, cbm_e


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
    hidden = {}
    for step in spec.get('steps', []):
        config = step.get('config', {})
        hidden[step['id']] = config
    return hidden


# === block: score_0 (check id='step04') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    energies = np.array([float(r['energy_eV']) for r in artifact])
    dos = np.array([float(r['total_DOS']) for r in artifact])
    gap, vbm, cbm, ve, ce = find_dos_gap(energies, dos)
    cfg = ctx.get('step04', {})
    gold = cfg.get('gold_gap_eV', 1.6)
    tol = cfg.get('tolerance_eV', 0.2)
    # gap score
    gap_score = 0.0
    if gap <= 0:
        gap_score = 0.0
    else:
        if abs(gap - gold) <= tol:
            gap_score = 1.0
        else:
            # partial credit outside tolerance
            if gap < gold - tol:
                # too small gap, penalize
                gap_score = max(0.0, 1.0 - (gold - tol - gap) / (0.5*gold))
            else:
                # too large gap, still plausible, give partial credit
                gap_score = max(0.0, 1.0 - (gap - gold - tol) / (0.5*gold))
    # mid-gap check: maximum DOS between VBM and CBM
    midgap_ratio_thresh = cfg.get('midgap_ratio_thresh', 0.2)
    midgap_score = 1.0
    if ve is not None and ce is not None and ce > ve:
        idx_between = np.where((energies >= ve + 0.05) & (energies <= ce - 0.05))[0]
        if len(idx_between) > 0:
            max_mid = np.max(dos[idx_between])
            if vbm > 0 and max_mid > midgap_ratio_thresh * vbm:
                midgap_score = 0.0
    score = 0.5 * gap_score + 0.5 * midgap_score
    return float(max(0.0, min(1.0, score)))


# === block: score_1 (check id='step05') ===
def score_1(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    energies = np.array([float(r['energy_eV']) for r in artifact])
    dos = np.array([float(r['total_DOS']) for r in artifact])
    gap, vbm, cbm, ve, ce = find_dos_gap(energies, dos)
    cfg = ctx.get('step05', {})
    midgap_thresh = cfg.get('midgap_intensity_ratio_threshold', 0.3)
    max_gap_thresh = cfg.get('max_gap_eV', 0.5)
    # Find maximal DOS in mid-gap region (between VBM and CBM if identifiable, else use gap 0-1 eV region)
    midgap_max = 0.0
    if ve is not None and ce is not None and ve < ce:
        idx = np.where((energies >= ve + 0.05) & (energies <= ce - 0.05))[0]
        if len(idx) > 0:
            midgap_max = np.max(dos[idx])
    else:
        # fallback: use energy window around Fermi (assume 0)
        idx = np.where((energies >= -0.5) & (energies <= 0.5))[0]
        if len(idx) > 0:
            midgap_max = np.max(dos[idx])
    vbm_peak = np.max(dos)
    has_midgap = (vbm_peak > 0) and (midgap_max >= midgap_thresh * vbm_peak)
    gap_obscured = (gap > 0 and gap < max_gap_thresh)
    score = 0.0
    if has_midgap and gap_obscured:
        score = 1.0
    elif has_midgap:
        score = 0.7
    elif gap_obscured:
        score = 0.3
    return float(score)


# === block: score_2 (check id='step06') ===
def score_2(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    energies = np.array([float(r['energy_eV']) for r in artifact])
    dos = np.array([float(r['total_DOS']) for r in artifact])
    gap, vbm, cbm, ve, ce = find_dos_gap(energies, dos)
    cfg = ctx.get('step06', {})
    gold = cfg.get('gold_gap_eV', 1.6)
    tol = cfg.get('tolerance_eV', 0.2)
    midgap_thresh = cfg.get('midgap_ratio_thresh', 0.2)
    # gap score
    gap_score = 0.0
    if gap > 0:
        if abs(gap - gold) <= tol:
            gap_score = 1.0
        else:
            if gap < gold - tol:
                gap_score = max(0.0, 1.0 - (gold - tol - gap) / (0.5*gold))
            else:
                gap_score = max(0.0, 1.0 - (gap - gold - tol) / (0.5*gold))
    midgap_score = 1.0
    if ve is not None and ce is not None and ce > ve:
        idx_between = np.where((energies >= ve + 0.05) & (energies <= ce - 0.05))[0]
        if len(idx_between) > 0:
            max_mid = np.max(dos[idx_between])
            if vbm > 0 and max_mid > midgap_thresh * vbm:
                midgap_score = 0.0
    score = 0.5 * gap_score + 0.5 * midgap_score
    return float(max(0.0, min(1.0, score)))


# === block: score_3 (check id='step07') ===
def score_3(artifact, step, ctx):
    if artifact is None or len(artifact)==0:
        return 0.0
    rows = artifact
    cfg = ctx.get('step07', {})
    gold_gaps = cfg.get('gold_gaps', {})
    tolerance = cfg.get('tolerance_eV', 0.3)
    # parse table
    diams = []
    gaps = []
    for r in rows:
        try:
            d = float(r['diameter_A'])
            bg = float(r['band_gap_eV'])
            diams.append(d)
            gaps.append(bg)
        except:
            pass
    if len(diams) < 2:
        return 0.0
    # monotonic check
    mono = True
    for i in range(len(diams)-1):
        if gaps[i+1] >= gaps[i] + 0.01:
            mono = False
            break
    mono_score = 1.0 if mono else 0.0
    # value check against gold
    match_count = 0
    total = 0
    for d, g in zip(diams, gaps):
        key = str(round(d,1))
        if key in gold_gaps:
            target = gold_gaps[key]
            if abs(g - target) <= tolerance:
                match_count += 1
            total += 1
    if total == 0:
        val_score = 0.0
    else:
        val_score = match_count / total
    score = 0.3 * mono_score + 0.7 * val_score
    return float(max(0.0, min(1.0, score)))


_SCORERS = {
    'step04': score_0,
    'step05': score_1,
    'step06': score_2,
    'step07': score_3,
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
