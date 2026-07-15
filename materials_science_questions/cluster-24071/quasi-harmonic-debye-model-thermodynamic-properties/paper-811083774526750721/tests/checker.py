import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np


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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        try:
            N = int(lines[0].strip())
        except:
            return 0.0
        coord_lines = lines[2:2+N]
        coords = []
        for line in coord_lines:
            parts = line.strip().split()
            if len(parts) != 4 or parts[0] != 'C':
                return 0.0
            x, y, z = map(float, parts[1:4])
            coords.append([x, y, z])
        coords = np.array(coords)
        diff = coords[:, None, :] - coords[None, :, :]
        dist = np.sqrt(np.sum(diff**2, axis=2))
        np.fill_diagonal(dist, np.inf)
        cutoff = step['gold']['cutoff']
        neighbors = np.sum(dist < cutoff, axis=1)
        coord_mean = np.mean(neighbors)
        gold_coord = step['gold']['coordination']
        tol = step['gold']['coord_tol']
        scale = step['gold']['coord_scale']
        err = abs(coord_mean - gold_coord)
        coord_score = max(0.0, 1.0 - max(0.0, err - tol) / scale)
        n2 = np.sum(neighbors == 2)
        n3 = np.sum(neighbors == 3)
        n4 = np.sum(neighbors >= 4)
        fractions = {'sp': 100*n2/N, 'sp2': 100*n3/N, 'sp3': 100*n4/N}
        gold_frac = step['gold']['fractions']
        ftol = step['gold']['frac_tol']
        fscale = step['gold']['frac_scale']
        scores_frac = {}
        for key in ['sp2', 'sp3', 'sp']:
            err_frac = abs(fractions[key] - gold_frac[key])
            s = max(0.0, 1.0 - max(0.0, err_frac - ftol) / fscale)
            scores_frac[key] = s
        frac_score = np.mean(list(scores_frac.values()))
        return 0.4 * coord_score + 0.6 * frac_score


# === block: score_1 (check id='s2') ===
def score_1(artifact, step, ctx):
        lines = artifact.strip().split('\n')
        freqs = []
        for line in lines:
            try:
                f = float(line.strip())
            except:
                return 0.0
            freqs.append(f)
        freqs = np.array(freqs)
        mev = freqs * 0.12405
        mev = mev[mev > 1e-6]
        if len(mev) == 0:
            return 0.0
        sigma = step['gold']['sigma_mev']
        emax = math.ceil(np.max(mev) + 10)
        grid = np.arange(0, emax + 0.5, 0.5)
        vdos = np.zeros_like(grid)
        for e in mev:
            vdos += np.exp(-0.5 * ((grid - e) / sigma) ** 2)
        vdos /= np.trapz(vdos, grid) if np.trapz(vdos, grid) != 0 else 1
        vdos /= np.trapz(vdos, grid) if np.trapz(vdos, grid) != 0 else 1
        k_B_mev_per_K = 0.086173
        T = 300.0
        kT = k_B_mev_per_K * T
        x = grid / kT
        with np.errstate(over='ignore', divide='ignore'):
            exp_x = np.exp(x)
        denom = (exp_x - 1)**2
        mask = x < 1e-6
        factor = np.zeros_like(x)
        factor[mask] = 1.0
        factor[~mask] = (x[~mask]**2) * exp_x[~mask] / denom[~mask]
        I = np.trapz(factor * vdos, grid)
        R = 8.314
        Cv = 3 * R * I
        dp_limit = step['gold']['dulong_petit_limit']
        cv_tol_frac = step['gold']['cv_tol_frac']
        cv_scale_frac = step['gold']['cv_scale_frac']
        rel_err = abs(Cv - dp_limit) / dp_limit
        cv_score = max(0.0, 1.0 - max(0.0, rel_err - cv_tol_frac) / cv_scale_frac)
        idx_200 = np.searchsorted(grid, 200)
        idx_200 = min(idx_200, len(grid)-1)
        below_200 = np.trapz(vdos[:idx_200], grid[:idx_200])
        below_200_frac = below_200 / np.trapz(vdos, grid)
        threshold_frac = step['gold']['vdos_below_200_threshold']
        if below_200_frac >= threshold_frac:
            below_score = 1.0
        else:
            below_score = max(0.0, (below_200_frac - 0.8) / (threshold_frac - 0.8))
        peak_range = step['gold']['peak_range_mev']
        idx1 = np.searchsorted(grid, peak_range[0])
        idx2 = np.searchsorted(grid, peak_range[1])
        if idx1 >= len(grid) or idx2 > len(grid):
            peak_score = 0.0
        else:
            segment = vdos[idx1:idx2]
            overall_max = np.max(vdos)
            local_max = np.max(segment)
            if local_max > 0.5 * overall_max:
                peak_score = 1.0
            else:
                peak_score = local_max / overall_max
        return 0.6 * cv_score + 0.2 * below_score + 0.2 * peak_score


# === block: score_2 (check id='s3') ===
def score_2(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        try:
            r = np.array([float(row['r']) for row in artifact])
            gr = np.array([float(row['g(r)']) for row in artifact])
        except:
            return 0.0
        idx1 = np.where((r >= 1.0) & (r <= 2.0))[0]
        peak1 = float(r[idx1][np.argmax(gr[idx1])]) if len(idx1) > 0 else None
        idx2 = np.where((r >= 2.0) & (r <= 3.0))[0]
        peak2 = float(r[idx2][np.argmax(gr[idx2])]) if len(idx2) > 0 else None
        gold_first = step['gold']['first_peak']
        gold_second = step['gold']['second_peak']
        tol = step['gold']['tolerance']
        scale = step['gold']['scale']
        scores = []
        for val, gold in [(peak1, gold_first), (peak2, gold_second)]:
            if val is None:
                scores.append(0.0)
            else:
                err = abs(val - gold)
                if err <= tol:
                    s = 1.0
                else:
                    s = max(0.0, 1.0 - (err - tol) / scale)
                scores.append(s)
        return float(np.mean(scores))


# === block: score_3 (check id='s4') ===
def score_3(artifact, step, ctx):
        if not artifact:
            return 0.0
        try:
            energy = np.array([float(row['energy_eV']) for row in artifact])
            total_dos = np.array([float(row['total_dos']) for row in artifact])
            p_dos = np.array([float(row['p_dos']) for row in artifact])
        except:
            return 0.0
        range_gap = step['gold']['pseudogap_range']
        range_ref = step['gold']['reference_range']
        mask_gap = (energy >= range_gap[0]) & (energy <= range_gap[1])
        mask_ref = (energy >= range_ref[0]) & (energy <= range_ref[1])
        if np.sum(mask_gap) == 0 or np.sum(mask_ref) == 0:
            gap_score = 0.0
        else:
            avg_gap = np.mean(total_dos[mask_gap])
            avg_ref = np.mean(total_dos[mask_ref])
            ratio = avg_gap / avg_ref if avg_ref != 0 else 1.0
            max_ratio = step['gold']['dip_ratio_max']
            if ratio <= max_ratio:
                gap_score = 1.0
            else:
                gap_score = max(0.0, 1.0 - (ratio - max_ratio) / max_ratio)
        p_range = step['gold']['p_dominance_range']
        mask_p = (energy >= p_range[0]) & (energy <= p_range[1])
        if np.sum(mask_p) == 0:
            p_score = 0.0
        else:
            avg_p = np.mean(p_dos[mask_p])
            avg_tot = np.mean(total_dos[mask_p])
            if avg_tot == 0:
                p_score = 0.0
            else:
                p_ratio = avg_p / avg_tot
                min_ratio = step['gold']['p_ratio_min']
                if p_ratio >= min_ratio:
                    p_score = 1.0
                else:
                    p_score = max(0.0, p_ratio / min_ratio)
        return 0.5 * gap_score + 0.5 * p_score


_SCORERS = {
    's1': score_0,
    's2': score_1,
    's3': score_2,
    's4': score_3,
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
