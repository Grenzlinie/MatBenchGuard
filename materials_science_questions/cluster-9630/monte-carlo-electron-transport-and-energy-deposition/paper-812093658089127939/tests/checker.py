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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    ct_20 = ref.get('contrast_at_20keV', {})
    target = float(ct_20.get('target', 30.0))
    tol = float(ct_20.get('tolerance_abs', 5.0))
    score_ref = 0.0
    try:
        data = artifact
        rows_20 = [r for r in data if float(r.get('E0_keV',0)) == 20.0]
        if rows_20:
            val = float(rows_20[0].get('contrast_percent',0))
            if abs(val - target) <= tol:
                score_ref = 0.5
            else:
                score_ref = 0.0
        pairs = []
        for r in data:
            try:
                e = float(r['E0_keV'])
                c = float(r['contrast_percent'])
                pairs.append((e, c))
            except:
                pass
        pairs.sort(key=lambda x: x[0])
        if len(pairs) >= 2:
            dec_fail = 0
            total_comp = len(pairs)-1
            for i in range(1, len(pairs)):
                if pairs[i-1][1] >= pairs[i][1] - 1e-6:
                    pass
                else:
                    dec_fail += 1
            trend_score = 0.5 * (1.0 - dec_fail/max(1,total_comp))
        else:
            trend_score = 0.0
        return score_ref + trend_score
    except:
        return 0.0


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    pos_range = ref.get('peak_position_range_nm', [40,60])
    energy_target = float(ref.get('energy', 20.0))
    peak_ratio_min = float(ref.get('peak_min_ratio', 1.2))
    try:
        data = artifact
        # filter for target energy
        rows = [r for r in data if abs(float(r.get('E0_keV',0)) - energy_target) < 0.1]
        if not rows:
            return 0.0
        pos_vals = []
        int_vals = []
        for r in rows:
            try:
                pos_vals.append(float(r['beam_position_nm']))
                int_vals.append(float(r['net_intensity']))
            except:
                pass
        if not int_vals:
            return 0.0
        max_int = max(int_vals)
        min_int = min(int_vals)
        max_idx = int_vals.index(max_int)
        peak_pos = pos_vals[max_idx]
        # score peak location
        loc_score = 0.3 if pos_range[0] <= peak_pos <= pos_range[1] else 0.0
        # peak magnitude vs average
        avg_int = sum(int_vals)/len(int_vals)
        peak_mag_score = 0.3 if max_int > avg_int*peak_ratio_min and max_int > 0 else 0.0
        # check single peak structure across all energies
        energies = set()
        for r in data:
            try:
                energies.add(float(r['E0_keV']))
            except:
                pass
        structure_score = 0.0
        total_e = 0
        ok_e = 0
        for e in energies:
            rows_e = [r for r in data if abs(float(r.get('E0_keV',0)) - e) < 0.1]
            ints = []
            for r in rows_e:
                try:
                    ints.append(float(r['net_intensity']))
                except:
                    pass
            if len(ints) >= 2:
                total_e += 1
                if (max(ints) / max(min(ints), 1e-12)) >= peak_ratio_min:
                    ok_e += 1
        if total_e > 0:
            structure_score = 0.4 * (ok_e / total_e)
        return min(1.0, loc_score + peak_mag_score + structure_score)
    except:
        return 0.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    low_cfg = ref.get('low_energy_eta_range_at_ends', {})
    low_E_list = low_cfg.get('E_list', [1,2,5])
    eta_D1_min = float(low_cfg.get('eta_D1_min', 0.4))
    eta_D1000_max = float(low_cfg.get('eta_D1000_max', 0.15))
    high_cfg = ref.get('high_energy_flat', {})
    high_E_list = high_cfg.get('E_list', [10,20])
    flat_tol = float(high_cfg.get('flat_tol', 0.05))
    try:
        data = artifact
        # build per-energy dict
        from collections import defaultdict
        edata = defaultdict(list)
        for r in data:
            try:
                e = round(float(r['E0_keV']), 1)
                d = float(r['D_nm'])
                eta = float(r['eta'])
                edata[e].append((d, eta))
            except:
                pass
        total_score = 0.0
        # low energy checks
        low_scores = 0.0
        for e in low_E_list:
            ekey = round(e,1)
            pts = sorted(edata.get(ekey, []), key=lambda x: x[0])
            if not pts:
                continue
            d_min = pts[0][0]
            d_max = pts[-1][0]
            eta_dmin = pts[0][1]
            eta_dmax = pts[-1][1]
            sub = 0.0
            if eta_dmin > eta_D1_min:
                sub += 0.2
            if eta_dmax < eta_D1000_max:
                sub += 0.2
            # peak detection
            max_eta = max(p[1] for p in pts)
            min_eta = min(p[1] for p in pts)
            # if max > eta at ends, it's a peak
            if max_eta > eta_dmin and max_eta > eta_dmax:
                sub += 0.1
            low_scores += sub
        low_scores = min(low_scores / len(low_E_list), 1.0) if low_E_list else 0.0
        total_score += 0.6 * low_scores
        # high energy flatness
        high_scores = 0.0
        for e in high_E_list:
            ekey = round(e,1)
            pts = edata.get(ekey, [])
            if not pts:
                continue
            etas = [p[1] for p in pts]
            span = max(etas) - min(etas)
            if span <= flat_tol:
                high_scores += 0.5
        high_scores = min(high_scores, 1.0)
        total_score += 0.4 * high_scores
        return min(1.0, total_score)
    except:
        return 0.0


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    D1_ratio_max = float(ref.get('D1_ratio_max', 0.1))
    D1000_ratio_min = float(ref.get('D1000_ratio_min', 0.7))
    energies = ref.get('energies', [1,2,5,10,20])
    try:
        data = artifact
        from collections import defaultdict
        edata = defaultdict(list)
        for r in data:
            try:
                e = round(float(r['E0_keV']), 1)
                d = float(r['D_nm'])
                int_val = float(r['net_intensity'])
                edata[e].append((d, int_val))
            except:
                pass
        total_score = 0.0
        for e in energies:
            ekey = round(e,1)
            pts = sorted(edata.get(ekey, []), key=lambda x: x[0])
            if not pts:
                continue
            max_int = max(p[1] for p in pts)
            if max_int == 0:
                continue
            d_first = pts[0][0]
            int_first = pts[0][1]
            d_last = pts[-1][0]
            int_last = pts[-1][1]
            sub = 0.0
            if int_first < D1_ratio_max * max_int:
                sub += 0.3
            if int_last > D1000_ratio_min * max_int:
                sub += 0.3
            # peak check
            if any(p[1] > max(int_first, int_last) for p in pts):
                sub += 0.4
            total_score += sub
        if energies:
            total_score = total_score / len(energies)
        return min(1.0, total_score)
    except:
        return 0.0


# === block: score_4 (check id='step_06') ===
def score_4(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    energies = ref.get('energies', [4,5,6])
    start_K_max = float(ref.get('start_K_max', 0.01))
    end_K_min = float(ref.get('end_K_min', 0.99))
    end_thickness_min = float(ref.get('end_thickness_min', 500))
    try:
        data = artifact
        from collections import defaultdict
        edata = defaultdict(list)
        for r in data:
            try:
                e = round(float(r['E0_keV']), 1)
                t = float(r['thickness_nm'])
                k = float(r['K_ratio'])
                edata[e].append((t, k))
            except:
                pass
        total_score = 0.0
        for e in energies:
            ekey = round(e,1)
            pts = sorted(edata.get(ekey, []), key=lambda x: x[0])
            if not pts:
                continue
            t_vals = [p[0] for p in pts]
            k_vals = [p[1] for p in pts]
            # monotonic increasing
            mono = True
            for i in range(1, len(k_vals)):
                if k_vals[i] < k_vals[i-1] - 1e-6:
                    mono = False
                    break
            sub = 0.4 if mono else 0.0
            # start near zero
            start_k = k_vals[0]
            if start_k <= start_K_max:
                sub += 0.3
            # end near one and thickness sufficient
            if t_vals[-1] >= end_thickness_min and k_vals[-1] >= end_K_min:
                sub += 0.3
            total_score += sub
        if energies:
            total_score = total_score / len(energies)
        return min(1.0, total_score)
    except:
        return 0.0


# === block: score_5 (check id='step_07') ===
def score_5(artifact, step, ctx):
    ref = step.get('hidden_reference', {})
    energies = ref.get('energies', [4,5,6])
    start_R_max = float(ref.get('start_R_max', 0.05))
    end_R_min = float(ref.get('end_R_min', 0.99))
    end_thickness_min = float(ref.get('end_thickness_min', 500))
    try:
        data = artifact
        from collections import defaultdict
        edata = defaultdict(list)
        for r in data:
            try:
                e = round(float(r['E0_keV']), 1)
                t = float(r['thickness_nm'])
                r_val = float(r['R_ratio'])
                edata[e].append((t, r_val))
            except:
                pass
        total_score = 0.0
        for e in energies:
            ekey = round(e,1)
            pts = sorted(edata.get(ekey, []), key=lambda x: x[0])
            if not pts:
                continue
            r_vals = [p[1] for p in pts]
            t_vals = [p[0] for p in pts]
            mono = True
            for i in range(1, len(r_vals)):
                if r_vals[i] < r_vals[i-1] - 1e-6:
                    mono = False
                    break
            sub = 0.4 if mono else 0.0
            if r_vals[0] <= start_R_max:
                sub += 0.3
            if t_vals[-1] >= end_thickness_min and r_vals[-1] >= end_R_min:
                sub += 0.3
            total_score += sub
        if energies:
            total_score = total_score / len(energies)
        return min(1.0, total_score)
    except:
        return 0.0


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
    'step_06': score_4,
    'step_07': score_5,
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
