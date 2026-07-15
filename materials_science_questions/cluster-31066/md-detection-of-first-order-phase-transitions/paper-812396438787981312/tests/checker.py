import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import statistics


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


# === block: score_0 (check id='check_diffusion') ===
def score_0(artifact, step, ctx):
    try:
        rows = [r for r in artifact if r.get('H_nm') and r.get('diffusion_coefficient_cm2_s')]
        liquid_rows = [float(r['diffusion_coefficient_cm2_s']) for r in rows if float(r['H_nm']) <= 0.50]
        if not liquid_rows:
            return 0.0
        liquid_avg = statistics.mean(liquid_rows)
        # Find H=0.51 row
        d051 = None
        for r in rows:
            h = float(r['H_nm'])
            if abs(h - 0.51) < 0.005:
                d051 = float(r['diffusion_coefficient_cm2_s'])
                break
        if d051 is None or d051 <= 0 or liquid_avg <= 0:
            return 0.0
        drop_factor = liquid_avg / d051
        threshold = float(step.get('params', {}).get('threshold_drop_factor', 500))
        score = min(1.0, drop_factor / threshold)
        return score
    except Exception:
        return 0.0


# === block: score_1 (check id='check_density') ===
def score_1(artifact, step, ctx):
    def find_peaks(z_vals, dens, smooth_win=9, threshold_frac=0.05, min_dist=0.05):
        # simple moving average smoothing
        smoothed = []
        for i in range(len(dens)):
            win = dens[max(0,i-smooth_win//2):min(len(dens),i+smooth_win//2+1)]
            smoothed.append(statistics.mean(win))
        max_dens = max(smoothed) if smoothed else 1.0
        if max_dens <= 0:
            max_dens = 1.0
        # detect local maxima
        candidate_indices = []
        for i in range(1, len(smoothed)-1):
            if smoothed[i] > smoothed[i-1] and smoothed[i] > smoothed[i+1]:
                if smoothed[i] >= threshold_frac * max_dens:
                    candidate_indices.append(i)
        # filter out peaks that are too close (keep the highest)
        candidates_sorted = sorted(candidate_indices, key=lambda i: smoothed[i], reverse=True)
        kept = []
        for i in candidates_sorted:
            z_i = z_vals[i]
            if not kept:
                kept.append(i)
            elif all(abs(z_i - z_vals[j]) > min_dist for j in kept):
                kept.append(i)
        return len(kept)

    try:
        import collections
        # group rows by H_nm
        groups = collections.defaultdict(list)
        for r in artifact:
            try:
                h = round(float(r['H_nm']), 2)
                z = float(r['z_nm'])
                d = float(r['density_g_ml'])
                groups[h].append((z, d))
            except (ValueError, KeyError):
                continue
        # sort each group by z
        for h in groups:
            groups[h].sort(key=lambda x: x[0])
        params = step.get('params', {})
        unimodal_h = params.get('unimodal_H', 0.47)
        bimodal_h = params.get('bimodal_H', 0.53)
        smooth_win = params.get('smoothing_window', 9)
        peak_frac = params.get('peak_threshold_frac', 0.05)
        min_dist = params.get('peak_min_dist', 0.05)
        score = 0.0
        # check unimodal
        if unimodal_h in groups:
            zs, ds = zip(*groups[unimodal_h])
            npeaks = find_peaks(zs, ds, smooth_win, peak_frac, min_dist)
            if npeaks == 1:
                score += 0.5
        # check bimodal
        if bimodal_h in groups:
            zs, ds = zip(*groups[bimodal_h])
            npeaks = find_peaks(zs, ds, smooth_win, peak_frac, min_dist)
            if npeaks == 2:
                score += 0.5
        return score
    except Exception:
        return 0.0


# === block: score_2 (check id='check_isotherm') ===
def score_2(artifact, step, ctx):
    try:
        # filter rows
        rows = []
        for r in artifact:
            try:
                A = float(r['A_nm2'])
                p = float(r['lateral_pressure_bar'])
                e = float(r['potential_energy_kJ_mol'])
                rows.append((A, p, e))
            except (ValueError, KeyError):
                continue
        rows.sort(key=lambda x: x[0])
        # restrict to area range
        params = step.get('params', {})
        A_min = params.get('A_min', 54.0)
        A_max = params.get('A_max', 60.4)
        range_rows = [(A,p,e) for A,p,e in rows if A_min <= A <= A_max]
        if len(range_rows) < 4:
            return 0.0
        As = [r[0] for r in range_rows]
        Ps = [r[1] for r in range_rows]
        Es = [r[2] for r in range_rows]
        # check vdW loop: compute slopes
        slopes = [(Ps[i+1]-Ps[i])/(As[i+1]-As[i]) for i in range(len(As)-1)]
        has_max = False
        has_min = False
        neg_exists = any(s < 0 for s in slopes)
        for i in range(len(slopes)-1):
            if slopes[i] > 0 and slopes[i+1] < 0:
                has_max = True
            if slopes[i] < 0 and slopes[i+1] > 0:
                has_min = True
        vdW_loop = has_max and has_min and neg_exists
        # check energy linearity: Pearson correlation
        n = len(As)
        if n < 3:
            energy_linear = False
        else:
            meanA = statistics.mean(As)
            meanE = statistics.mean(Es)
            num = sum((As[i]-meanA)*(Es[i]-meanE) for i in range(n))
            denA = sum((a-meanA)**2 for a in As)
            denE = sum((e-meanE)**2 for e in Es)
            if denA > 0 and denE > 0:
                r = num / (math.sqrt(denA) * math.sqrt(denE))
                energy_linear = (r <= params.get('correlation_threshold', -0.8))
            else:
                energy_linear = False
        score = 0.0
        if vdW_loop:
            score += 0.5
        if energy_linear:
            score += 0.5
        return score
    except Exception:
        return 0.0


_SCORERS = {
    'check_diffusion': score_0,
    'check_density': score_1,
    'check_isotherm': score_2,
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
