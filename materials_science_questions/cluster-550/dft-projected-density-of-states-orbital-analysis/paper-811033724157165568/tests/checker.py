import os
import json
import csv

# === author imports / helpers ===
import os
import re
import subprocess
import sys
try:
    import numpy as np
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', 'numpy'])
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
    import json
    step = next((s for s in spec.get('steps', []) if s['id'] == 'check_effective_masses'), {})
    ctx = {}
    ctx['gold_masses'] = step.get('gold_masses', {})
    ctx['mass_tolerance'] = step.get('tolerance_abs', 0.1)
    return ctx


# === block: score_0 (check id='check_csv_valid') ===
def score_0(artifact, step, ctx):
    # artifact is the loaded CSV list of dicts (shape gate already passed)
    return 1.0


# === block: score_1 (check id='check_ib_range_recompute') ===
def score_1(artifact, step, ctx):
    import os
    csv_path = os.path.join('/app/outputs', 'total_dos_data.csv')
    csv_rows = load_artifact(csv_path)
    if not csv_rows:
        return 0.0
    results_json = artifact   # loaded dos_results.json
    if not isinstance(results_json, dict):
        return 0.0

    # config
    threshold_dos = 0.1
    smooth_window = 3
    tolerance_ev = 0.2
    compounds = ['Au2Cs2I6', 'Ag2GeBaS4', 'Ag2ZnSnS4']

    scores = []
    for comp in compounds:
        comp_rows = [r for r in csv_rows if r.get('compound') == comp]
        if not comp_rows:
            scores.append(0.0)
            continue
        # extract arrays
        energies = []
        dos = []
        for r in comp_rows:
            try:
                energies.append(float(r['energy_ev']))
                dos.append(float(r['total_dos']))
            except (ValueError, KeyError):
                continue
        if len(energies) < 10:
            scores.append(0.0)
            continue
        # sort by energy
        idxs = np.argsort(energies)
        energies = np.array(energies)[idxs]
        dos = np.array(dos)[idxs]
        # smooth
        if len(dos) >= smooth_window:
            kernel = np.ones(smooth_window) / smooth_window
            dos_smooth = np.convolve(dos, kernel, mode='same')
        else:
            dos_smooth = dos

        # find the main gap: largest contiguous low-DOS region
        low_mask = dos_smooth < threshold_dos
        # find contiguous blocks
        blocks = []
        start = None
        for i, val in enumerate(low_mask):
            if val and start is None:
                start = i
            elif not val and start is not None:
                blocks.append((start, i-1))
                start = None
        if start is not None:
            blocks.append((start, len(low_mask)-1))
        if not blocks:
            scores.append(0.0)
            continue
        # main gap: block with largest energy span
        main_gap = max(blocks, key=lambda b: energies[b[1]] - energies[b[0]])
        gap_start, gap_end = main_gap
        # within this gap, find where dos (unsmoothed) >= threshold
        unsmoothed = dos[gap_start:gap_end+1]
        above_mask = unsmoothed > threshold_dos
        # find first and last indices where above_mask is True
        above_idxs = np.where(above_mask)[0]
        if len(above_idxs) == 0:
            scores.append(0.0)
            continue
        ib_start = energies[gap_start + above_idxs[0]]
        ib_end   = energies[gap_start + above_idxs[-1]]

        # agent reported range
        comp_result = results_json.get(comp)
        if not comp_result or 'ib_energy_range' not in comp_result:
            scores.append(0.0)
            continue
        range_str = comp_result['ib_energy_range']
        # parse '0.64‑1.34 eV' or similar
        match = re.findall(r'[\d.]+', range_str.replace('‑', '-'))
        if len(match) < 2:
            scores.append(0.0)
            continue
        rep_start = float(match[0])
        rep_end   = float(match[1])
        diff_start = abs(rep_start - ib_start)
        diff_end   = abs(rep_end - ib_end)
        if diff_start <= tolerance_ev and diff_end <= tolerance_ev:
            scores.append(1.0)
        else:
            scores.append(0.0)

    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_2 (check id='check_dominant_orbitals') ===
def score_2(artifact, step, ctx):
    import os
    csv_path = os.path.join('/app/outputs', 'total_dos_data.csv')
    csv_rows = load_artifact(csv_path)
    if not csv_rows:
        return 0.0
    results_json = artifact
    if not isinstance(results_json, dict):
        return 0.0

    threshold_dos = 0.1
    smooth_window = 3
    compounds = ['Au2Cs2I6', 'Ag2GeBaS4', 'Ag2ZnSnS4']
    match_scores = []

    for comp in compounds:
        comp_rows = [r for r in csv_rows if r.get('compound') == comp]
        if not comp_rows:
            match_scores.append(0.0)
            continue
        # parse columns
        cols = list(comp_rows[0].keys())
        orbital_cols = [c for c in cols if c not in ('compound', 'energy_ev', 'total_dos')]
        if not orbital_cols:
            match_scores.append(0.0)
            continue
        energies = []
        dos = []
        data = []
        for r in comp_rows:
            try:
                energies.append(float(r['energy_ev']))
                dos.append(float(r['total_dos']))
                row_vals = [float(r[c]) for c in orbital_cols]
                data.append(row_vals)
            except (ValueError, KeyError):
                continue
        if len(energies) < 10:
            match_scores.append(0.0)
            continue
        idxs = np.argsort(energies)
        energies = np.array(energies)[idxs]
        dos = np.array(dos)[idxs]
        data = np.array(data)[idxs]

        # smooth dos
        if len(dos) >= smooth_window:
            kernel = np.ones(smooth_window)/smooth_window
            dos_smooth = np.convolve(dos, kernel, mode='same')
        else:
            dos_smooth = dos
        # main gap as before
        low_mask = dos_smooth < threshold_dos
        blocks = []
        start_idx = None
        for i, val in enumerate(low_mask):
            if val and start_idx is None:
                start_idx = i
            elif not val and start_idx is not None:
                blocks.append((start_idx, i-1))
                start_idx = None
        if start_idx is not None:
            blocks.append((start_idx, len(low_mask)-1))
        if not blocks:
            match_scores.append(0.0)
            continue
        main_gap = max(blocks, key=lambda b: energies[b[1]] - energies[b[0]])
        gs, ge = main_gap
        gap_dos = dos[gs:ge+1]
        gap_data = data[gs:ge+1]
        above = gap_dos > threshold_dos
        if not np.any(above):
            match_scores.append(0.0)
            continue
        # integrate PDOS in IB region
        ib_data = gap_data[above]
        sums = np.sum(ib_data, axis=0)
        max_sum = np.max(sums)
        if max_sum == 0:
            match_scores.append(0.0)
            continue
        dominant_threshold = 0.3 * max_sum
        true_dominant = [orbital_cols[i] for i, s in enumerate(sums) if s >= dominant_threshold]
        reported_dominant = results_json.get(comp, {}).get('dominant_orbitals', [])
        if not true_dominant:
            match_scores.append(1.0)  # nothing to check
            continue
        # score as fraction of required columns present in agent list
        present = sum(1 for d in true_dominant if d in reported_dominant)
        match_scores.append(present / len(true_dominant))

    if not match_scores:
        return 0.0
    return np.mean(match_scores)


# === block: score_3 (check id='check_effective_masses') ===
def score_3(artifact, step, ctx):
    gold = ctx.get('gold_masses', {})
    tol = ctx.get('mass_tolerance', 0.1)
    if not isinstance(artifact, dict):
        return 0.0
    compounds = list(gold.keys())
    scores = []
    for comp in compounds:
        comp_data = artifact.get(comp, {})
        masses = comp_data.get('effective_masses', {})
        if not masses:
            scores.extend([0.0, 0.0, 0.0])
            continue
        gold_comp = gold[comp]
        for mass_key in ('m_lh', 'm_hh', 'm_e'):
            val = masses.get(mass_key)
            gold_val = gold_comp.get(mass_key)
            if val is None or gold_val is None:
                scores.append(0.0)
            else:
                diff = abs(float(val) - float(gold_val))
                if diff <= tol:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
    if not scores:
        return 0.0
    return np.mean(scores)


_SCORERS = {
    'check_csv_valid': score_0,
    'check_ib_range_recompute': score_1,
    'check_dominant_orbitals': score_2,
    'check_effective_masses': score_3,
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
