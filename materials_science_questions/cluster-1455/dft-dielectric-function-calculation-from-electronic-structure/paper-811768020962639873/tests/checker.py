import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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


# === block: score_0 (check id='optical_summary') ===
def score_0(artifact, step, ctx):
        # step contains 'gold' and 'tolerances' dicts
        gold = step.get('gold', {})
        tol = step.get('tolerances', {})
        if not isinstance(artifact, dict):
            return 0.0
        # define field scoring functions
        def score_abs(val, g, tol_abs):
            if val is None:
                return 0.0
            diff = abs(val - g)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / tol_abs)

        def score_rel(val, g, tol_rel):
            if val is None or g == 0:
                return 0.0
            allowed = abs(g) * tol_rel
            diff = abs(val - g)
            if diff <= allowed:
                return 1.0
            return max(0.0, 1.0 - (diff - allowed) / allowed)

        fields = [
            ('n_perp',              'n_perp_abs',                          score_abs),
            ('n_par',               'n_par_abs',                           score_abs),
            ('epsilon2_peak_perp_position_eV', 'epsilon2_peak_perp_position_abs', score_abs),
            ('epsilon2_peak_par_position_eV',  'epsilon2_peak_par_position_abs',  score_abs),
            ('epsilon2_peak_perp_magnitude',   'epsilon2_peak_perp_magnitude_rel', score_rel),
            ('epsilon2_peak_par_magnitude',    'epsilon2_peak_par_magnitude_rel',  score_rel),
        ]
        scores = []
        for field, tol_key, fn in fields:
            val = artifact.get(field)
            g_val = gold.get(field)
            if g_val is None:
                # gold missing => skip (should not happen)
                continue
            tol_val = tol.get(tol_key)
            if tol_val is None:
                continue
            if val is None:
                scores.append(0.0)
            else:
                scores.append(fn(val, g_val, tol_val))
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='reflectivity_structure') ===
def score_1(artifact, step, ctx):
        # step['config'] contains structural check parameters
        cfg = step.get('config', {})
        mono_start = cfg.get('mono_start_eV', 0.0)
        mono_end   = cfg.get('mono_end_eV', 5.0)
        min_window = cfg.get('local_min_window_eV', [2.0, 3.0])
        lo, hi = min_window
        # artifact is list of dicts (rows)
        if not isinstance(artifact, list) or len(artifact) < 2:
            return 0.0
        try:
            energies = [float(row['energy_eV']) for row in artifact]
            Rperp = [float(row['R_perp']) for row in artifact]
            Rpar = [float(row['R_par']) for row in artifact]
        except (KeyError, ValueError):
            return 0.0

        # 1) values in [0,1] for both polarizations
        range_ok = all(0.0 <= r <= 1.0 for r in Rperp) and all(0.0 <= r <= 1.0 for r in Rpar)
        score_range = 1.0 if range_ok else 0.0

        # 2) monotonic decrease in [mono_start, mono_end] eV
        def is_monotonic_decreasing(en, r):
            paired = [(e, v) for e, v in zip(en, r) if mono_start <= e <= mono_end]
            if len(paired) < 2:
                return True  # not enough points, treat as ok
            # sort by energy just in case
            paired.sort(key=lambda x: x[0])
            for i in range(len(paired)-1):
                if paired[i][1] + 1e-12 < paired[i+1][1]:   # increase (allowing tiny noise)
                    return False
            return True
        mono_ok = is_monotonic_decreasing(energies, Rperp) and is_monotonic_decreasing(energies, Rpar)
        score_mono = 1.0 if mono_ok else 0.0

        # 3) local minimum near 2.5 eV (within window) for both polarizations
        def has_local_min_in_window(en, r):
            # collect points in window, find min and check it's lower than immediate neighbours
            idx_in = [i for i, e in enumerate(en) if lo <= e <= hi]
            if len(idx_in) < 3:
                return False
            min_idx = min(idx_in, key=lambda i: r[i])
            # local minimum: lower than previous and next if they exist
            left = r[min_idx-1] if min_idx-1 >= 0 else float('inf')
            right = r[min_idx+1] if min_idx+1 < len(r) else float('inf')
            return r[min_idx] < left and r[min_idx] < right
        min_ok = has_local_min_in_window(energies, Rperp) and has_local_min_in_window(energies, Rpar)
        score_min = 1.0 if min_ok else 0.0

        # equal weight for three criteria
        return (score_range + score_mono + score_min) / 3.0


_SCORERS = {
    'optical_summary': score_0,
    'reflectivity_structure': score_1,
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
