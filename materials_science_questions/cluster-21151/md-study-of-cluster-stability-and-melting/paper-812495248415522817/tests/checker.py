import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def find_peaks(x, height=None, prominence=None):
    """
    Minimal replacement for scipy.signal.find_peaks using only numpy.
    Returns (peaks, properties) where properties['peak_heights'] contains the heights.
    """
    x = np.asarray(x)
    n = len(x)
    # index of local maxima (strict greater than neighbours)
    peaks = []
    for i in range(1, n - 1):
        if x[i] > x[i - 1] and x[i] > x[i + 1]:
            peaks.append(i)
    if not peaks:
        return np.array([], dtype=int), {}
    peaks = np.array(peaks)
    heights = x[peaks]
    # height filter
    if height is not None:
        keep = heights >= height
        peaks, heights = peaks[keep], heights[keep]
        if len(peaks) == 0:
            return peaks, {}
    # prominence filter (approximate)
    if prominence is not None:
        prom = []
        for idx in peaks:
            left_val = np.min(x[:idx]) if idx > 0 else x[idx]
            right_val = np.min(x[idx+1:]) if idx < n-1 else x[idx]
            base = min(left_val, right_val) if (idx > 0 and idx < n-1) else x[idx]
            prom.append(x[idx] - base)
        prom = np.array(prom)
        keep = prom >= prominence
        peaks, heights = peaks[keep], heights[keep]
        if len(peaks) == 0:
            return peaks, {}
    props = {'peak_heights': heights}
    return peaks, props


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


# === block: score_0 (check id='scored_analysis') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        temps = data['temperatures']
        # helper to extract item by index
        def get_item(collection, idx):
            return collection[idx]
    
        # ========== 1) g(r) features ==========
        gr = data['total_g_r']
        r = [np.array(it['r']) for it in gr]
        g = [np.array(it['g']) for it in gr]
    
        def find_peak(r, g, low, high):
            mask = (r >= low) & (r <= high)
            if not np.any(mask):
                return None, None
            idx_max = np.argmax(g[mask])
            return r[mask][idx_max], g[mask][idx_max]
    
        first_pos = []
        first_h = []
        second_pos = []
        for i in range(4):
            p, h = find_peak(r[i], g[i], 2.0, 3.0)
            if p is None:
                raise ValueError('No first g(r) peak')
            first_pos.append(p)
            first_h.append(h)
            p2, _ = find_peak(r[i], g[i], 4.0, 5.0)
            second_pos.append(p2)
    
        c1_ok = True
        if not all(2.50 <= p <= 2.54 for p in first_pos):
            c1_ok = False
        if not all(4.50 <= p <= 4.66 for p in second_pos):
            c1_ok = False
        if not (first_h[0] < first_h[1] < first_h[2] < first_h[3]):
            c1_ok = False
    
        def count_peaks_in_range(r, g, low, high):
            mask = (r >= low) & (r <= high)
            peaks, _ = find_peaks(g[mask], prominence=0.01)
            return len(peaks)
    
        for idx in [2, 3]:
            if count_peaks_in_range(r[idx], g[idx], 4.3, 5.5) < 2:
                c1_ok = False
                break
        crit1 = c1_ok
    
        # ========== 2) S(q) features ==========
        sq = data['total_S_q']
        q = [np.array(it['q']) for it in sq]
        S = [np.array(it['S']) for it in sq]
    
        pre_h = []
        for i in range(4):
            p, h = find_peak(q[i], S[i], 1.78, 1.82)
            if p is None:
                crit2 = False; break
            pre_h.append(h)
        else:
            c2_1 = pre_h[0] < pre_h[1] < pre_h[2] < pre_h[3]
        
            first_main_h = []
            for i in range(4):
                p, h = find_peak(q[i], S[i], 2.90, 3.05)
                if p is None:
                    crit2 = False; break
                first_main_h.append(h)
            else:
                c2_2 = first_main_h[0] < first_main_h[1] < first_main_h[2] < first_main_h[3]
                # second peak splitting at 1473 K (index 1)
                mask = (q[1] >= 4.8) & (q[1] <= 6.5)
                peaks_sec, _ = find_peaks(S[1][mask], prominence=0.01)
                c2_3 = len(peaks_sec) >= 2
                crit2 = all([c2_1, c2_2, c2_3])
    
        # ========== 3) bond-angle distributions ==========
        bad = data['bond_angle_distributions']
        target = ['Ni-Ni-Ni', 'Ni-Ni-Nb']
        crit3 = True
        for bond in target:
            if bond not in bad:
                crit3 = False; break
            dists = bad[bond]
            angles = [np.array(d['angle']) for d in dists]
            probs = [np.array(d['probability']) for d in dists]
            def peak_near(arr, prob, low, high):
                mask = (arr >= low) & (arr <= high)
                if not np.any(mask):
                    return None, None
                idx = np.argmax(prob[mask])
                return arr[mask][idx], prob[mask][idx]
            pos55 = []; h55 = []
            pos110 = []; h110 = []
            for i in range(4):
                p, h = peak_near(angles[i], probs[i], 50, 60)
                if p is None:
                    crit3 = False; break
                pos55.append(p); h55.append(h)
                p, h = peak_near(angles[i], probs[i], 105, 115)
                if p is None:
                    crit3 = False; break
                pos110.append(p); h110.append(h)
            if not crit3:
                break
            # shift ~2° at 1233 K (index 3) vs 1873 K (index 0)
            if not (1.0 <= pos55[3] - pos55[0] <= 3.0):
                crit3 = False; break
            if not (1.0 <= pos110[3] - pos110[0] <= 3.0):
                crit3 = False; break
            # height increase (sharpening)
            if not (h55[0] < h55[1] < h55[2] < h55[3]):
                crit3 = False; break
            if not (h110[0] < h110[1] < h110[2] < h110[3]):
                crit3 = False; break
    
        # ========== 4) CSRO parameters ==========
        csro = data['csro_parameters']
        crit4 = True
        for d in csro:
            if not (d['Ni-Ni'] > 0.05 and d['Nb-Nb'] > 0.05 and d['Ni-Nb'] < -0.05 and d['Nb-Ni'] < -0.05):
                crit4 = False; break
    
        # ========== 5) diffusion coefficients ==========
        diff = data['diffusion_coefficients']
        D_Ni = [d['D_Ni'] for d in diff]
        D_Nb = [d['D_Nb'] for d in diff]
        D_tot = [d['D_total'] for d in diff]
        crit5 = True
        if not (D_Ni[0] > D_Ni[1] > D_Ni[2] > D_Ni[3]):
            crit5 = False
        if not (D_Nb[0] > D_Nb[1] > D_Nb[2] > D_Nb[3]):
            crit5 = False
        if not all(D_Ni[i] > D_Nb[i] for i in range(4)):
            crit5 = False
        if not (D_tot[0] > D_tot[1] > D_tot[2] > D_tot[3]):
            crit5 = False
    
        # ========== 6) DOS features ==========
        dos_list = data['dos']
        crit6 = True
        for idx, d in enumerate(dos_list):
            energy = np.array(d['energy'])
            total = np.array(d['total_dos'])
            Ni_d = np.array(d['Ni_d'])
            Nb_d = np.array(d['Nb_d'])
            neg = energy < 0
            peaks, props = find_peaks(total[neg], height=0)
            if len(peaks) < 2:
                crit6 = False; break
            peak_e = energy[neg][peaks]
            peak_h = props['peak_heights']
            order = np.argsort(peak_h)[-2:]
            top2 = sorted(peak_e[order])
            if not (-2.65 <= top2[0] <= -2.05):
                crit6 = False; break
            if not (-1.79 <= top2[1] <= -1.19):
                crit6 = False; break
            # Ni d dominates <0 eV
            max_Ni_neg = np.max(Ni_d[neg]) if np.any(neg) else 0
            max_Nb_neg = np.max(Nb_d[neg]) if np.any(neg) else 0
            if max_Ni_neg <= max_Nb_neg:
                crit6 = False; break
            # Nb d dominates >0 eV
            pos = energy > 0
            max_Ni_pos = np.max(Ni_d[pos]) if np.any(pos) else 0
            max_Nb_pos = np.max(Nb_d[pos]) if np.any(pos) else 0
            if max_Nb_pos <= max_Ni_pos:
                crit6 = False; break
            # Fermi level edge check
            z = np.argmin(np.abs(energy))
            if Ni_d[z] > 0.1 * max_Ni_neg or Nb_d[z] < 0.3 * max_Nb_neg:
                crit6 = False; break
    
        results = [crit1, crit2, crit3, crit4, crit5, crit6]
        return sum(results) / 6.0
    except Exception as e:
        return 0.0


_SCORERS = {
    'scored_analysis': score_0,
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
