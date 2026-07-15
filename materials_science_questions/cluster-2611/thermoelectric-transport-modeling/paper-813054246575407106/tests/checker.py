import os
import json
import csv

# === author imports / helpers ===
import json, math, csv


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


# === block: score_0 (check id='band_Ba2PdO3_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'kpath' not in artifact or 'bands' not in artifact:
        return 0.0
    kpath = artifact['kpath']
    bands_raw = artifact.get('bands', [])
    tol = 1e-6

    # Find Gamma point (k = (0,0,0) within tolerance)
    gamma_idx = None
    for i, entry in enumerate(kpath):
        k = entry.get('k')
        if k is not None and all(abs(x) < tol for x in k):
            gamma_idx = i
            break
    if gamma_idx is None:
        return 0.0

    # Identify conduction band by largest band gap
    bands_list = [(b['band_index'], b['eigenvalues']) for b in bands_raw
                  if 'band_index' in b and isinstance(b.get('eigenvalues'), list) and b['eigenvalues']]
    if not bands_list:
        return 0.0
    # compute min and max eigenvalues per band
    band_ranges = []
    for idx, eig in bands_list:
        band_ranges.append((idx, min(eig), max(eig)))
    # find largest gap between lower band max and upper band min
    best_gap = -1.0
    cond_idx = None
    for i, (idx_i, _, max_i) in enumerate(band_ranges):
        for j, (idx_j, min_j, _) in enumerate(band_ranges):
            if idx_i == idx_j:
                continue
            if min_j > max_i and (min_j - max_i) > best_gap:
                best_gap = min_j - max_i
                cond_idx = idx_j
    # fallback: use band with highest mean eigenvalue if no gap found
    if cond_idx is None:
        bands_sorted = sorted(bands_list, key=lambda item: sum(item[1])/len(item[1]) if item[1] else 0.0)
        cond_idx = bands_sorted[-1][0]

    # extract conduction band eigenvalues
    cond_eig = None
    for idx, eig in bands_list:
        if idx == cond_idx:
            cond_eig = eig
            break
    if cond_eig is None or not cond_eig:
        return 0.0

    # Helper: find index of farthest point along a given axis direction from Gamma,
    # but only if the segment between Gamma and that point lies on the axis.
    def find_axis_endpoint_idx(axis_constraint):
        best_idx = None
        best_dist = -1.0
        for i, entry in enumerate(kpath):
            if i == gamma_idx:
                continue
            k = entry.get('k')
            if k is None or not axis_constraint(k[0], k[1], k[2]):
                continue
            dist = sum((k[j])**2 for j in range(3))
            if dist > best_dist:
                start = min(gamma_idx, i)
                end = max(gamma_idx, i)
                valid = True
                for j in range(start, end+1):
                    q = kpath[j].get('k')
                    if q is None or not axis_constraint(q[0], q[1], q[2]):
                        valid = False
                        break
                if valid:
                    best_dist = dist
                    best_idx = i
        return best_idx

    # b* axis: kx=0, kz=0, ky can be anything (dispersive direction)
    # c* axis: kx=0, ky=0, kz can be anything (flat direction)
    dispersive_idx = find_axis_endpoint_idx(lambda x,y,z: abs(x)<tol and abs(z)<tol)
    flat_idx       = find_axis_endpoint_idx(lambda x,y,z: abs(x)<tol and abs(y)<tol)

    if dispersive_idx is None or flat_idx is None:
        return 0.0

    try:
        params = step['parameters']
        disp_min = params['dispersive_min_diff_eV']
        flat_max = params['flat_max_diff_eV']

        # eigenvalues for dispersive segment
        start, end = sorted([gamma_idx, dispersive_idx])
        eig_disp = cond_eig[start:end+1]
        if len(eig_disp) < 2:
            return 0.0
        disp_diff = max(eig_disp) - min(eig_disp)

        # eigenvalues for flat segment
        start, end = sorted([gamma_idx, flat_idx])
        eig_flat = cond_eig[start:end+1]
        if len(eig_flat) < 2:
            return 0.0
        flat_diff = max(eig_flat) - min(eig_flat)

        score = 0.0
        if disp_diff >= disp_min:
            score += 0.6
        else:
            score += 0.6 * max(0.0, min(1.0, disp_diff / disp_min))
        if flat_diff <= flat_max:
            score += 0.4
        else:
            score += 0.4 * max(0.0, min(1.0, flat_max / flat_diff if flat_diff > 0 else 1.0))
        return score
    except Exception:
        return 0.0


# === block: score_1 (check id='band_La4PdO7_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'kpath' not in artifact or 'bands' not in artifact:
        return 0.0
    kpath = artifact['kpath']
    bands_raw = artifact.get('bands', [])
    tol = 1e-6

    # Find Gamma point (k = (0,0,0) within tolerance)
    gamma_idx = None
    for i, entry in enumerate(kpath):
        k = entry.get('k')
        if k is not None and all(abs(x) < tol for x in k):
            gamma_idx = i
            break
    if gamma_idx is None:
        return 0.0

    # Identify conduction band as the band with the highest mean eigenvalue
    bands_list = [(b['band_index'], b['eigenvalues']) for b in bands_raw
                  if 'band_index' in b and isinstance(b.get('eigenvalues'), list)]
    if not bands_list:
        return 0.0
    bands_sorted = sorted(bands_list, key=lambda item: sum(item[1])/len(item[1]) if item[1] else 0.0)
    cond_idx, cond_eig = bands_sorted[-1]   # highest mean -> conduction

    # Helper: find index of farthest point along a given axis direction from Gamma,
    # but only if the segment between Gamma and that point lies on the axis.
    def find_axis_endpoint_idx(axis_constraint):
        best_idx = None
        best_dist = -1.0
        for i, entry in enumerate(kpath):
            if i == gamma_idx:
                continue
            k = entry.get('k')
            if k is None or not axis_constraint(k[0], k[1], k[2]):
                continue
            dist = sum((k[j])**2 for j in range(3))
            if dist > best_dist:
                start = min(gamma_idx, i)
                end = max(gamma_idx, i)
                valid = True
                for j in range(start, end+1):
                    q = kpath[j].get('k')
                    if q is None or not axis_constraint(q[0], q[1], q[2]):
                        valid = False
                        break
                if valid:
                    best_dist = dist
                    best_idx = i
        return best_idx

    # b* axis: kx=0, kz=0, ky can be anything (dispersive direction)
    # c* axis: kx=0, ky=0, kz can be anything (flat direction)
    dispersive_idx = find_axis_endpoint_idx(lambda x,y,z: abs(x)<tol and abs(z)<tol)
    flat_idx       = find_axis_endpoint_idx(lambda x,y,z: abs(x)<tol and abs(y)<tol)

    if dispersive_idx is None or flat_idx is None:
        return 0.0

    try:
        params = step['parameters']
        disp_min = params['dispersive_min_diff_eV']
        flat_max = params['flat_max_diff_eV']

        # eigenvalues for dispersive segment
        start, end = sorted([gamma_idx, dispersive_idx])
        eig_disp = cond_eig[start:end+1]
        if len(eig_disp) < 2:
            return 0.0
        disp_diff = max(eig_disp) - min(eig_disp)

        # eigenvalues for flat segment
        start, end = sorted([gamma_idx, flat_idx])
        eig_flat = cond_eig[start:end+1]
        if len(eig_flat) < 2:
            return 0.0
        flat_diff = max(eig_flat) - min(eig_flat)

        score = 0.0
        if disp_diff >= disp_min:
            score += 0.6
        else:
            score += 0.6 * max(0.0, min(1.0, disp_diff / disp_min))
        if flat_diff <= flat_max:
            score += 0.4
        else:
            score += 0.4 * max(0.0, min(1.0, flat_max / flat_diff if flat_diff > 0 else 1.0))
        return score
    except Exception:
        return 0.0


# === block: score_2 (check id='pf_check') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    try:
        params = step['parameters']
        compounds = params['compounds']
        doping_type = params['doping_type']
        golds = params['peak_gold_W_per_mK2s']
        threshold_factor = params['peak_threshold_factor']
        ref_peak = params['reference_Bi2PdO4_peak_W_per_mK2s']
        conc_check = params['concentration_check_cm3']
        min_ratio = params['min_ratio_to_Bi2PdO4']

        # extract rows for given compound and doping type
        rows_by_compound = {}
        for row in artifact:
            comp = row.get('compound', '').strip()
            dtype = row.get('doping_type', '').strip()
            if comp not in compounds or dtype != doping_type:
                continue
            try:
                conc = float(row['carrier_concentration_cm3'])
                pf = float(row['sigmaS2_tau_W_mK2s'])
            except (KeyError, ValueError):
                continue
            rows_by_compound.setdefault(comp, []).append((conc, pf))

        peak_score = 0.0
        interp_score = 0.0
        for comp in compounds:
            rows = rows_by_compound.get(comp, [])
            if not rows:
                continue
            # peak
            peak = max(r[1] for r in rows)
            gold = golds.get(comp)
            if gold is None:
                continue
            threshold = gold * threshold_factor
            if peak >= threshold:
                peak_score += 1.0 / len(compounds)
            else:
                # linear decay from threshold down to 0
                peak_score += max(0.0, (peak / threshold)) / len(compounds)
            # interpolation at conc_check
            rows_sorted = sorted(rows, key=lambda x: x[0])
            if rows_sorted[-1][0] < conc_check or rows_sorted[0][0] > conc_check:
                continue
            # find bracket
            lower = None
            upper = None
            for r in rows_sorted:
                if r[0] <= conc_check:
                    lower = r
                else:
                    upper = r
                    break
            if lower is None or upper is None:
                pf_at_check = None
            else:
                frac = (math.log10(conc_check) - math.log10(lower[0])) / (math.log10(upper[0]) - math.log10(lower[0])) if upper[0] != lower[0] else 0.0
                pf_at_check = lower[1] + frac * (upper[1] - lower[1])
            if pf_at_check is not None:
                req = ref_peak * min_ratio
                if pf_at_check >= req:
                    interp_score += 1.0 / len(compounds)
                else:
                    interp_score += max(0.0, pf_at_check / req) / len(compounds)

        return 0.7 * peak_score + 0.3 * interp_score
    except Exception:
        return 0.0


_SCORERS = {
    'band_Ba2PdO3_check': score_0,
    'band_La4PdO7_check': score_1,
    'pf_check': score_2,
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
