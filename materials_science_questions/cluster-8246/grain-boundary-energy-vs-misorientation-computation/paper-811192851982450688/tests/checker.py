import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
    import numpy as np
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


# === block: score_0 (check id='local_rdf') ===
def score_0(artifact, step, ctx):
        # Parse two-column txt: r (Angstrom), G(r)
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        data = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('//'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    data.append((float(parts[0]), float(parts[1])))
                except ValueError:
                    continue
        if len(data) < 40:
            return 0.0
        r = np.array([d[0] for d in data])
        g = np.array([d[1] for d in data])
        # Ensure sorted
        sort_idx = np.argsort(r)
        r = r[sort_idx]
        g = g[sort_idx]
        # Points count check (≥200) – soft penalty only if dramatically short
        n_points = len(r)
        point_score = min(1.0, n_points / 200.0) if n_points < 200 else 1.0
        target = step.get('target', {})
        # First peak region [2.0,2.7] Å
        mask1 = (r >= 2.0) & (r <= 2.7)
        if not np.any(mask1):
            peak1_score = 0.0
            peak1_r = None
        else:
            idx1 = np.argmax(g[mask1])
            peak1_r = r[mask1][idx1]
            peak1_g = g[mask1][idx1]
            t1 = target.get('first_peak_position', 2.35)
            tol1 = target.get('first_peak_tol', 0.2)
            dev1 = abs(peak1_r - t1)
            peak1_score = max(0.0, 1.0 - (dev1 - tol1) / (0.5 * tol1)) if dev1 > tol1 else 1.0
        # Second peak region [3.4,4.2] Å
        mask2 = (r >= 3.4) & (r <= 4.2)
        if not np.any(mask2):
            peak2_score = 0.0
            peak2_r = None
            peak2_g = None
        else:
            idx2 = np.argmax(g[mask2])
            peak2_r = r[mask2][idx2]
            peak2_g = g[mask2][idx2]
            t2 = target.get('second_peak_position', 3.84)
            tol2 = target.get('second_peak_tol', 0.25)
            dev2 = abs(peak2_r - t2)
            peak2_score = max(0.0, 1.0 - (dev2 - tol2) / (0.5 * tol2)) if dev2 > tol2 else 1.0
        # Amorphous background: minimum between first and second peak should be non-zero
        if peak1_r is not None and peak2_r is not None and peak1_r < peak2_r:
            between = (r >= peak1_r) & (r <= peak2_r)
            if np.any(between):
                min_g = np.min(g[between])
                if peak2_g is not None and peak2_g > 0:
                    ratio = min_g / peak2_g
                    bg_target = target.get('min_ratio', 0.08)
                    if ratio >= bg_target:
                        bg_score = 1.0
                    else:
                        bg_score = ratio / bg_target
                else:
                    bg_score = 0.0
            else:
                bg_score = 0.0
        else:
            bg_score = 0.0
        # Absence of third sharp peak: max in [5.5,6.5] should be low relative to second peak
        mask3 = (r >= 5.5) & (r <= 6.5)
        if np.any(mask3) and peak2_g is not None and peak2_g > 0:
            third_max = np.max(g[mask3])
            ratio3 = third_max / peak2_g
            ratio_max = target.get('third_peak_ratio_max', 0.6)
            if ratio3 <= ratio_max:
                third_score = 1.0
            else:
                third_score = max(0.0, 1.0 - (ratio3 - ratio_max) / (0.5 * ratio_max))
        else:
            third_score = 0.0
        # Combine sub-scores (weights: peak pos 0.3+0.2, background 0.3, third 0.2)
        sub_scores = [
            (peak1_score, 0.3),
            (peak2_score, 0.2),
            (bg_score, 0.3),
            (third_score, 0.2)
        ]
        weighted = sum(s * w for s, w in sub_scores)
        weighted *= point_score  # apply points penalty
        return max(0.0, min(1.0, weighted))


# === block: score_1 (check id='angular_distribution') ===
def score_1(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        data = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('//'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    data.append((float(parts[0]), float(parts[1])))
                except ValueError:
                    continue
        if len(data) < 20:
            return 0.0
        cos = np.array([d[0] for d in data])
        p = np.array([d[1] for d in data])
        # Sort
        idx = np.argsort(cos)
        cos = cos[idx]
        p = p[idx]
        target = step.get('target', {})
        # Normalize if sum of bin areas = 1 (assume bins equal width)
        # but we don't strictly require; we just work with raw p.
        # Peak near cos = -1/3
        mask_peak = (cos >= -0.36) & (cos <= -0.30)
        if not np.any(mask_peak):
            return 0.0
        peak_idx = np.argmax(p[mask_peak])
        peak_cos = cos[mask_peak][peak_idx]
        peak_val = p[mask_peak][peak_idx]
        t_pos = target.get('cos_peak_position', -0.333)
        tol_pos = target.get('cos_peak_tol', 0.03)
        dev_pos = abs(peak_cos - t_pos)
        pos_score = 1.0 if dev_pos <= tol_pos else max(0.0, 1.0 - (dev_pos - tol_pos) / tol_pos)
        # FWHM
        half_max = peak_val / 2.0
        left_idx = np.where(p[:peak_idx] >= half_max)[0]
        right_idx = np.where(p[peak_idx:] >= half_max)[0]
        if len(left_idx) > 0 and len(right_idx) > 0:
            left_cos = cos[left_idx[0]]
            right_cos = cos[peak_idx + right_idx[-1]]
            fwhm = right_cos - left_cos
        else:
            fwhm = 0.0
        fwhm_target = target.get('fwhm_min', 0.12)
        fwhm_score = min(1.0, fwhm / fwhm_target) if fwhm_target > 0 else 0.0
        # Max bin height (smoothness)
        max_height = np.max(p)
        max_h_target = target.get('max_bin_height_max', 0.4)
        if max_height <= max_h_target:
            height_score = 1.0
        else:
            height_score = max(0.0, 1.0 - (max_height - max_h_target) / (2.0 * max_h_target))
        # Combine weights: pos 0.3, fwhm 0.4, height 0.3
        total = pos_score * 0.3 + fwhm_score * 0.4 + height_score * 0.3
        return max(0.0, min(1.0, total))


# === block: score_2 (check id='gb_energy_profile') ===
def score_2(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        data = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('//'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    data.append((float(parts[0]), float(parts[1])))
                except ValueError:
                    continue
        if len(data) < 10:
            return 0.0
        d = np.array([p[0] for p in data])
        e = np.array([p[1] for p in data])
        # Ensure sorted by distance
        idx = np.argsort(d)
        d = d[idx]
        e = e[idx]
        # Compute excess energy: energy minus minimum (assume crystal interior is lowest)
        e_min = np.min(e)
        excess = e - e_min
        e_max = np.max(excess)
        if e_max <= 0.0:
            return 0.0
        target = step.get('target', {})
        peak_target = target.get('peak_excess_energy', 0.20)
        tol_excess = target.get('excess_tol', 0.06)
        dev_excess = abs(e_max - peak_target)
        if dev_excess <= tol_excess:
            excess_score = 1.0
        else:
            excess_score = max(0.0, 1.0 - (dev_excess - tol_excess) / tol_excess)
        # FWHM: find distance range where excess >= e_max/2
        half_max = e_max / 2.0
        above = excess >= half_max
        if not np.any(above):
            fwhm = 0.0
        else:
            left_d = d[np.argmax(above)]
            right_d = d[len(d) - np.argmax(above[::-1]) - 1]
            fwhm = right_d - left_d
        fwhm_min = target.get('fwhm_distance_min', 1.0)
        fwhm_max = target.get('fwhm_distance_max', 2.5)
        if fwhm_min <= fwhm <= fwhm_max:
            fwhm_score = 1.0
        elif fwhm < fwhm_min:
            fwhm_score = fwhm / fwhm_min if fwhm_min > 0 else 0.0
        else:  # fwhm > fwhm_max
            fwhm_score = max(0.0, 1.0 - (fwhm - fwhm_max) / fwhm_max)
        # Combine (excess weight 0.6, fwhm 0.4)
        total = excess_score * 0.6 + fwhm_score * 0.4
        return max(0.0, min(1.0, total))


_SCORERS = {
    'local_rdf': score_0,
    'angular_distribution': score_1,
    'gb_energy_profile': score_2,
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
