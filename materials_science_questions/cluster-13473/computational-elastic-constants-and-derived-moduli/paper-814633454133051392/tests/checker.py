import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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


# === block: score_0 (check id='stress_strain') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        gold_yield_sc = step['gold_yield_sc']
        gold_yield_am = step['gold_yield_am']
        tol = step['tol_yield_frac']

        def safe_float(v):
            try:
                return float(v)
            except (ValueError, TypeError):
                return None

        def clean_rows(rows):
            cleaned = []
            for r in rows:
                strain = safe_float(r.get('strain'))
                stress = safe_float(r.get('stress'))
                if strain is not None and stress is not None:
                    cleaned.append((r.get('sample_type', ''), strain, stress))
            return cleaned

        cleaned = clean_rows(rows)
        sc_rows = [(s, t) for (ty, s, t) in cleaned if ty == 'semicrystalline']
        am_rows = [(s, t) for (ty, s, t) in cleaned if ty == 'amorphous']

        def compute_sample_score(data, gold_yield):
            if not data:
                return 0.0
            data.sort(key=lambda x: x[0])
            strains = [d[0] for d in data]
            stresses = [d[1] for d in data]

            peak = None
            peaks = [s for e, s in zip(strains, stresses) if 0.05 <= e <= 0.5]
            if peaks:
                peak = max(peaks)

            yield_score = 0.0
            if peak is not None and abs(peak - gold_yield) / gold_yield <= tol:
                yield_score = 1.0

            mins = [s for e, s in zip(strains, stresses) if 0.6 <= e <= 1.2]
            min_stress = None if not mins else min(mins)

            soft_score = 0.0
            if min_stress is not None and peak is not None and min_stress < peak * 0.9:
                soft_score = 1.0

            max_strain_idx = strains.index(max(strains))
            stress_high = stresses[max_strain_idx]
            hard_score = 1.0 if (min_stress is not None and min_stress < stress_high) else 0.0

            return 0.4 * yield_score + 0.3 * soft_score + 0.3 * hard_score

        sc = compute_sample_score(sc_rows, gold_yield_sc)
        am = compute_sample_score(am_rows, gold_yield_am)
        return 0.5 * sc + 0.5 * am


# === block: score_1 (check id='crystallinity_order') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        gold_initial = step['gold_initial_XC_sc']
        tol_initial = step['tol_initial_XC']
        max_XC_min = step['max_XC_min']
        gold_final_min = step['gold_final_XC_sc_min']
        S_thresh = step['S_global_threshold']
        S_min_strain = step['S_global_min_strain']
        sc_rows = [r for r in rows if r['sample_type'] == 'semicrystalline']
        am_rows = [r for r in rows if r['sample_type'] == 'amorphous']
        def compute_sample(rows, is_semicrystalline):
            if not rows:
                return 0.0
            data = [(float(r['strain']), float(r['X_C']), float(r['S_global'])) for r in rows]
            data.sort(key=lambda x: x[0])
            strains = [d[0] for d in data]
            XCs = [d[1] for d in data]
            Sgs = [d[2] for d in data]
            scores = []
            if is_semicrystalline:
                # initial XC
                initial_rows = [x for e,x in zip(strains,XCs) if e <= 0.1]
                if not initial_rows:
                    scores.append(0.0)
                else:
                    init = initial_rows[0]  # first row with low strain
                    if abs(init - gold_initial) <= tol_initial:
                        scores.append(1.0)
                    else:
                        scores.append(0.0)
                # min XC must be low
                XC_min = min(XCs)
                if XC_min <= max_XC_min:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
                # final XC >= gold_final_min
                final_XC = XCs[-1]
                if final_XC >= gold_final_min:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
                # S_global at max strain
                S_final = Sgs[-1]
                if S_final >= S_thresh and strains[-1] >= S_min_strain:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
                return sum(scores)/len(scores)
            else:
                # amorphous: check S_global at high strain
                if strains[-1] >= S_min_strain and Sgs[-1] >= S_thresh:
                    return 1.0
                else:
                    return 0.0
        sc = compute_sample(sc_rows, True)
        am = compute_sample(am_rows, False)
        return 0.6*sc + 0.4*am


# === block: score_2 (check id='micro_stretch') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        max_err = step['affine_max_error']
        lam_max = step['affine_lam_max']
        sc_rows = [r for r in rows if r['sample_type'] == 'semicrystalline']
        am_rows = [r for r in rows if r['sample_type'] == 'amorphous']
        def compute_sample(rows):
            if not rows:
                return 0.0
            data = [(float(r['macroscopic_stretch']), float(r['microscopic_stretch'])) for r in rows]
            # affine check for lam <= lam_max
            affine_rel_errors = []
            subaffine_ok = True
            for lam, lam_eff in data:
                if lam <= 0:
                    continue
                if lam <= lam_max:
                    affine_rel_errors.append(abs(lam_eff - lam) / lam)
                else:
                    if lam_eff >= lam:
                        subaffine_ok = False
            affine_score = 1.0 if affine_rel_errors and max(affine_rel_errors) <= max_err else 0.0
            sub_score = 1.0 if subaffine_ok else 0.0
            return 0.5*affine_score + 0.5*sub_score
        sc = compute_sample(sc_rows)
        am = compute_sample(am_rows)
        return 0.5*sc + 0.5*am


# === block: score_3 (check id='pair_dist_crys') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        shift_min = step['shift_min_frac']
        stab_tol = step['stability_tol']
        strains_ordered = [0.0, 0.5, 1.0, 1.6]
        positions = {}
        for strain in strains_ordered:
            subset = [r for r in rows if abs(float(r['strain']) - strain) < 0.01 and abs(float(r['y'])) < 1e-6]
            if not subset:
                subset = [r for r in rows if abs(float(r['strain']) - strain) < 0.01]
                subset = [r for r in subset if abs(float(r['y'])) < 0.01]
            if not subset:
                return 0.0
            # find second peak in g_crys_rho0: rho > 0.7
            rhos = [float(r['rho']) for r in subset]
            gs = [float(r['g_crys_rho0']) for r in subset]
            peak_idx = max(range(len(rhos)), key=lambda i: gs[i] if rhos[i] > 0.7 else -1.0)
            positions[strain] = rhos[peak_idx]
        pos0 = positions[0.0]
        pos05 = positions[0.5]
        pos10 = positions[1.0]
        pos16 = positions[1.6]
        shift_score = 1.0 if (pos0 - pos05) >= shift_min else 0.0
        stable_score = 0.0
        if abs(pos10 - pos16) <= stab_tol and pos10 < pos0 - 0.01 and pos16 < pos0 - 0.01:
            stable_score = 1.0
        return 0.5*shift_score + 0.5*stable_score


# === block: score_4 (check id='pair_dist_amor') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        max_var = step['max_position_variation']
        strains_ordered = [0.0, 0.5, 1.0, 1.6]
        positions = {}
        for strain in strains_ordered:
            subset = [r for r in rows if abs(float(r['strain']) - strain) < 0.01 and abs(float(r['y'])) < 1e-6]
            if not subset:
                subset = [r for r in rows if abs(float(r['strain']) - strain) < 0.01]
                subset = [r for r in subset if abs(float(r['y'])) < 0.01]
            if not subset:
                return 0.0
            rhos = [float(r['rho']) for r in subset]
            gs = [float(r['g_amorph_rho0']) for r in subset]
            # second peak: max g for rho > 0.7
            peak_idx = max(range(len(rhos)), key=lambda i: gs[i] if rhos[i] > 0.7 else -1.0)
            positions[strain] = rhos[peak_idx]
        pos_list = list(positions.values())
        if max(pos_list) - min(pos_list) <= max_var:
            return 1.0
        else:
            return 0.0


_SCORERS = {
    'stress_strain': score_0,
    'crystallinity_order': score_1,
    'micro_stretch': score_2,
    'pair_dist_crys': score_3,
    'pair_dist_amor': score_4,
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
