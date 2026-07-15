import os
import json
import csv

# === author imports / helpers ===
import csv, math
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


# === block: score_0 (check id='step2_dos') ===
def score_0(artifact, step, ctx):
    target = float(step.get('target', 1.0))
    tol = float(step.get('tolerance_abs', 0.2))
    # artifact is list of dicts with 'energy' and 'total_DOS'
    energies = [float(row['energy']) for row in artifact]
    dos_vals = [float(row['total_DOS']) for row in artifact]
    if not energies:
        return 0.0
    idx = min(range(len(energies)), key=lambda i: abs(energies[i]))
    total_dos_ef = dos_vals[idx]
    # total DOS per formula unit includes both spin channels;
    # paper target is per spin (1.0 eV⁻¹ spin⁻¹), so divide by 2
    n_ef = total_dos_ef / 2.0
    if abs(n_ef - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step3_band') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dict with kpoint_label, band_index, energy
    if not rows:
        return 0.0
    # enhance with integer band_index and float energy, preserve order
    enhanced = []
    for i, r in enumerate(rows):
        try:
            bi = int(r['band_index'])
        except (ValueError, KeyError):
            return 0.0
        try:
            energy = float(r['energy'])
        except (ValueError, KeyError):
            return 0.0
        label = r.get('kpoint_label', '').strip()
        enhanced.append({'row_idx': i, 'band': bi, 'label': label, 'energy': energy})
    bands = defaultdict(list)
    for e in enhanced:
        bands[e['band']].append(e)
    # sort band rows by row_idx
    for bi in bands:
        bands[bi].sort(key=lambda x: x['row_idx'])
    saddle_found = False
    for bi, band_rows in bands.items():
        # first Gamma point
        gfirst = None
        for r in band_rows:
            if r['label'] == 'Gamma':
                gfirst = r
                break
        if gfirst is None:
            continue
        if not (-1.0 <= gfirst['energy'] <= 1.0):
            continue
        # Gamma-A curvature
        gamma_A_energies = []
        found_gamma = False
        for r in band_rows:
            if r['label'] == 'Gamma' and not found_gamma:
                found_gamma = True
                gamma_A_energies = [r['energy']]
            elif found_gamma:
                gamma_A_energies.append(r['energy'])
                if r['label'] == 'A':
                    break
        if len(gamma_A_energies) < 3:
            continue
        e0, e1, e2 = gamma_A_energies[:3]
        curv_A = e2 - 2*e1 + e0
        pos_curv = curv_A > 0.001
        # Z-Gamma curvature (using last Gamma and preceding Z)
        glast = None
        for r in reversed(band_rows):
            if r['label'] == 'Gamma':
                glast = r
                break
        if glast is None or glast == gfirst:
            continue
        z_rows = [r for r in band_rows if r['label'] == 'Z' and r['row_idx'] < glast['row_idx']]
        if not z_rows:
            continue
        z_last = z_rows[-1]
        segment = [r for r in band_rows if z_last['row_idx'] <= r['row_idx'] <= glast['row_idx']]
        if len(segment) < 3:
            continue
        e_last2 = segment[-3]['energy']
        e_last1 = segment[-2]['energy']
        e_last0 = segment[-1]['energy']
        curv_Z = e_last2 - 2*e_last1 + e_last0
        neg_curv = curv_Z < -0.001
        if pos_curv and neg_curv:
            saddle_found = True
            break
    return 1.0 if saddle_found else 0.0


# === block: score_2 (check id='step4_frozen') ===
def score_2(artifact, step, ctx):
    rows = artifact
    elongation_ok = False
    rotation_ok = False
    for row in rows:
        d = row.get('distortion', '').strip().lower()
        try:
            shift = float(row['energy_shift'])
        except (ValueError, KeyError):
            return 0.0
        if d == 'elongation':
            if shift < 0 and abs(shift) >= 0.2:
                elongation_ok = True
        elif d == 'rotation':
            if shift > 0 and shift >= 0.2:
                rotation_ok = True
    score = 0.0
    if elongation_ok:
        score += 0.5
    if rotation_ok:
        score += 0.5
    return score


_SCORERS = {
    'step2_dos': score_0,
    'step3_band': score_1,
    'step4_frozen': score_2,
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
