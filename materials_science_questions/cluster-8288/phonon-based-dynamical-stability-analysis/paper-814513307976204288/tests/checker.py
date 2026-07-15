import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math
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


# === block: score_0 (check id='check_phonon') ===
def score_0(artifact, step, ctx):
    rows = artifact   # list of dicts
    if not rows: return 0.0
    freqs = [float(r['frequency_THz']) for r in rows]
    min_f = min(freqs)
    max_f = max(freqs)
    thr_imag = step.get('imaginary_threshold_THz', -0.01)
    min_max_freq = step.get('min_max_freq_THz', 35.0)
    ok_no_imag = (min_f >= thr_imag)
    ok_high = (max_f >= min_max_freq)
    return (1.0 if ok_no_imag else 0.0) * (1.0 if ok_high else 0.0)


# === block: score_1 (check id='check_stability') ===
def score_1(artifact, step, ctx):
    raw_path = os.path.join('/app/outputs', step['raw_file'])
    rows = []
    with open(raw_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    freqs = [float(r['frequency_THz']) for r in rows]
    csv_min = min(freqs)
    csv_max = max(freqs)
    csv_neg = (csv_min < -0.001)
    verdict = artifact.get('negative_frequencies') == csv_neg
    rep_min = float(artifact.get('min_frequency_THz', 0.0))
    rep_max = float(artifact.get('max_frequency_THz', 0.0))
    tol = step.get('tolerance_THz', 0.1)
    min_ok = abs(rep_min - csv_min) <= tol
    max_ok = abs(rep_max - csv_max) <= tol
    return 1.0 if verdict and min_ok and max_ok else 0.0


# === block: score_2 (check id='check_nemd') ===
def score_2(artifact, step, ctx):
    rows = artifact
    data = defaultdict(list)
    for r in rows:
        d = r['direction'].strip().lower()
        L = float(r['length_nm'])
        k = float(r['kappa_WmK'])
        if k <= 0 or L <= 0: continue
        data[d].append((1.0/L, 1.0/k))

    def fit(xy):
        n = len(xy)
        if n < 2:
            return None, None
        sx = sy = sxx = sxy = 0.0
        for x, y in xy:
            sx += x; sy += y; sxx += x*x; sxy += x*y
        den = n*sxx - sx*sx
        if abs(den) < 1e-12:
            return None, None
        slope = (n*sxy - sx*sy) / den
        intercept = (sy - slope*sx) / n
        if abs(intercept) < 1e-12:
            return None, None
        kappa_inf = 1.0 / intercept
        mfp = slope / intercept
        return kappa_inf, mfp

    thr = step['thresholds']   # paper central values: kappa_WmK, mfp_nm
    # tolerance fraction for allowed relative deficit below reference; default 0.25
    tol_frac = float(step.get('tolerance_frac', 0.25))

    def dir_score(direction):
        if direction not in data or not data[direction]:
            return 0.0
        kinf, mfp = fit(data[direction])
        if kinf is None or mfp is None:
            return 0.0
        t = thr[direction]
        ref_k = float(t['kappa_WmK'])
        ref_m = float(t['mfp_nm'])
        if ref_k <= 0 or ref_m <= 0:
            return 0.0
        # directional: full credit for meeting or exceeding reference
        if kinf >= ref_k:
            kappa_score = 1.0
        else:
            deficit = (ref_k - kinf) / (tol_frac * ref_k) if tol_frac > 0 else float('inf')
            kappa_score = max(0.0, 1.0 - deficit)
        if mfp >= ref_m:
            mfp_score = 1.0
        else:
            deficit = (ref_m - mfp) / (tol_frac * ref_m) if tol_frac > 0 else float('inf')
            mfp_score = max(0.0, 1.0 - deficit)
        # combine kappa and mfp scores with weights reflecting importance
        return 0.7 * kappa_score + 0.3 * mfp_score

    return 0.5 * dir_score('armchair') + 0.5 * dir_score('zigzag')


# === block: score_3 (check id='check_fit') ===
def score_3(artifact, step, ctx):
    raw_path = os.path.join('/app/outputs', step['raw_file'])
    rows = []
    with open(raw_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    data = defaultdict(list)
    for r in rows:
        d = r['direction'].strip().lower()
        L = float(r['length_nm'])
        k = float(r['kappa_WmK'])
        if k <= 0 or L <= 0: continue
        data[d].append((1.0/L, 1.0/k))
    def fit(xy):
        n = len(xy)
        if n < 2: return None, None
        sx = sy = sxx = sxy = 0.0
        for x, y in xy:
            sx += x; sy += y; sxx += x*x; sxy += x*y
        den = n*sxx - sx*sx
        if abs(den) < 1e-12: return None, None
        slope = (n*sxy - sx*sy) / den
        intercept = (sy - slope*sx) / n
        if abs(intercept) < 1e-12: return None, None
        return 1.0 / intercept, slope / intercept
    ref_vals = {}
    for d in ['armchair', 'zigzag']:
        if d in data:
            ki, mfp = fit(data[d])
            if ki is not None:
                ref_vals[d] = {'k': ki, 'm': mfp}
    tol_frac = step.get('tolerance_frac', 0.3)
    scores = []
    for d in ['armchair', 'zigzag']:
        agent_d = artifact.get(d)
        if not agent_d or d not in ref_vals:
            scores.append(0.0)
            continue
        ak = float(agent_d.get('kappa_intrinsic_WmK', 0.0))
        am = float(agent_d.get('mfp_nm', 0.0))
        rk = ref_vals[d]['k']
        rm = ref_vals[d]['m']
        ek = abs(ak - rk) / (abs(rk) + 1e-9)
        em = abs(am - rm) / (abs(rm) + 1e-9)
        sk = max(0.0, 1.0 - ek / tol_frac)
        sm = max(0.0, 1.0 - em / tol_frac)
        scores.append((sk + sm) / 2.0)
    if not scores: return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='check_tensile') ===
def score_4(artifact, step, ctx):
    rows = artifact
    data = defaultdict(list)
    for r in rows:
        d = r['direction'].strip().lower()
        eps = float(r['strain'])
        sig = float(r['stress_GPa'])
        if sig < 0: continue
        data[d].append((eps, sig))

    def compute_mech(pairs):
        linear = [(e,s) for e,s in pairs if e <= 0.02]
        if len(linear) < 2:
            return None, None
        n = len(linear)
        sx = sy = sxx = sxy = 0.0
        for e, s in linear:
            sx += e; sy += s; sxx += e*e; sxy += e*s
        den = n*sxx - sx*sx
        if abs(den) < 1e-12:
            return None, None
        E = (n*sxy - sx*sy) / den
        TS = max(s for _,s in pairs)
        return E, TS

    # paper central values as hidden gold
    PAPER_VALUES = {
        'armchair': {'E_GPa': 870.0, 'TS_GPa': 85.0},
        'zigzag': {'E_GPa': 800.0, 'TS_GPa': 85.0},
    }
    tol_frac = float(step.get('tolerance_frac', 0.25))

    def dir_score(direction):
        if direction not in data or not data[direction]:
            return 0.0
        E, TS = compute_mech(data[direction])
        if E is None or TS is None:
            return 0.0
        ref = PAPER_VALUES[direction]
        ref_E = ref['E_GPa']
        ref_TS = ref['TS_GPa']
        # directional: meeting or exceeding reference earns full credit
        if E >= ref_E:
            score_E = 1.0
        else:
            deficit = (ref_E - E) / (tol_frac * ref_E) if tol_frac > 0 else 0.0
            score_E = max(0.0, 1.0 - deficit)
        if TS >= ref_TS:
            score_TS = 1.0
        else:
            deficit = (ref_TS - TS) / (tol_frac * ref_TS) if tol_frac > 0 else 0.0
            score_TS = max(0.0, 1.0 - deficit)
        return 0.5 * score_E + 0.5 * score_TS

    return 0.5 * dir_score('armchair') + 0.5 * dir_score('zigzag')


# === block: score_5 (check id='check_mech') ===
def score_5(artifact, step, ctx):
    raw_path = os.path.join('/app/outputs', step['raw_file'])
    rows = []
    with open(raw_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    data = defaultdict(list)
    for r in rows:
        d = r['direction'].strip().lower()
        eps = float(r['strain'])
        sig = float(r['stress_GPa'])
        if sig < 0: continue
        data[d].append((eps, sig))
    def compute_mech(pairs):
        linear = [(e,s) for e,s in pairs if e <= 0.02]
        if len(linear) < 2: return None, None
        n = len(linear)
        sx = sy = sxx = sxy = 0.0
        for e, s in linear:
            sx += e; sy += s; sxx += e*e; sxy += e*s
        den = n*sxx - sx*sx
        if abs(den) < 1e-12: return None, None
        E = (n*sxy - sx*sy) / den
        TS = max(s for _,s in pairs)
        return E, TS
    tol_frac = step.get('tolerance_frac', 0.3)
    scores = []
    for d in ['armchair', 'zigzag']:
        agent_d = artifact.get(d)
        if not agent_d or d not in data:
            scores.append(0.0)
            continue
        E_ref, TS_ref = compute_mech(data[d])
        if E_ref is None or TS_ref is None:
            scores.append(0.0)
            continue
        aE = float(agent_d.get('elastic_modulus_GPa', 0.0))
        aTS = float(agent_d.get('tensile_strength_GPa', 0.0))
        eE = abs(aE - E_ref) / (abs(E_ref) + 1e-9)
        eTS = abs(aTS - TS_ref) / (abs(TS_ref) + 1e-9)
        sE = max(0.0, 1.0 - eE / tol_frac)
        sTS = max(0.0, 1.0 - eTS / tol_frac)
        scores.append((sE + sTS) / 2.0)
    if not scores: return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'check_phonon': score_0,
    'check_stability': score_1,
    'check_nemd': score_2,
    'check_fit': score_3,
    'check_tensile': score_4,
    'check_mech': score_5,
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
