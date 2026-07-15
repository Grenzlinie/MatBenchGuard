import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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


# === block: score_0 (check id='eff_masses_check') ===
def score_0(artifact, step, ctx):
    target = step['target']
    tol_m = step['tolerances']['m_eff']
    tol_e = step['tolerances']['E_Fermi']
    total = 0
    correct = 0
    for bridge, gold_fields in target.items():
        if bridge not in artifact:
            continue
        entry = artifact[bridge]
        if abs(entry.get('m_eff', 0) - gold_fields['m_eff']) <= tol_m:
            correct += 1
        total += 1
        if abs(entry.get('E_Fermi', 0) - gold_fields['E_Fermi']) <= tol_e:
            correct += 1
        total += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='ctp_frequencies_check') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts with keys bridge, R_angstrom, frequency_eV
    rows = {}
    for r in artifact:
        b = r['bridge']
        if b not in rows:
            rows[b] = []
        rows[b].append((float(r['R_angstrom']), float(r['frequency_eV'])))

    score_spot = 0.0
    spot = step.get('spot_check')
    if spot:
        for r in artifact:
            if r['bridge'] == spot['bridge'] and abs(float(r['R_angstrom']) - spot['R']) < 1e-3:
                if abs(float(r['frequency_eV']) - spot['target']) <= spot['tolerance']:
                    score_spot = 1.0
                break

    score_mono = 0.0
    mono_count = 0
    for b, points in rows.items():
        points.sort(key=lambda x: x[0])
        dec = all(points[i][1] > points[i+1][1] for i in range(len(points)-1))
        if dec:
            mono_count += 1
    if rows:
        score_mono = mono_count / len(rows)

    score_cross = 0.0
    # check at R=7.41 (or closest) that polyacetylene > polypyrrole and > polythiophene
    target_R = 7.41
    def get_freq(bridge, Rtarget):
        if bridge not in rows:
            return None
        best = min(rows[bridge], key=lambda x: abs(x[0]-Rtarget))
        return best[1]
    f_poly = get_freq('polyacetylene', target_R)
    f_py = get_freq('polypyrrole', target_R)
    f_th = get_freq('polythiophene', target_R)
    if f_poly is not None and f_py is not None and f_th is not None:
        if f_poly > f_py and f_poly > f_th:
            score_cross = 1.0
    return (score_spot + score_mono + score_cross) / 3.0


# === block: score_2 (check id='seebeck_check') ===
def score_2(artifact, step, ctx):
    # artifact is list of dicts with bridge, S_uV_per_K
    # recompute S from E_Fermi in eff_masses.json
    eff_path = '/app/outputs/eff_masses.json'
    if not os.path.exists(eff_path):
        return 0.0
    with open(eff_path) as f:
        eff = json.load(f)
    # constants
    k_B = 1.380649e-23
    e = 1.602176634e-19
    T = 300.0
    factor = (math.pi**2 / 6.0) * ((k_B * T) / (e)) / (e) * 1e6  # µV·K / eV
    # actually compute S_uV_per_K = factor / E_Fermi_eV   factor = (π^2/6)*(k_B/e)*(k_B T)/e *1e6
    precomputed_factor = (math.pi**2/6.0) * (k_B / e) * (k_B * T / e) * 1e6  # ≈ 3.665
    n_correct = 0
    n_total = 0
    for row in artifact:
        bridge = row['bridge']
        if bridge not in eff:
            continue
        efermi = eff[bridge].get('E_Fermi')
        if efermi is None or efermi <= 0:
            continue
        expected = precomputed_factor / efermi
        actual = float(row['S_uV_per_K'])
        tol = 0.05 * abs(expected) + 1.0  # 5% relative + 1 µV/K floor
        if abs(actual - expected) <= tol:
            n_correct += 1
        n_total += 1
    return n_correct / n_total if n_total > 0 else 0.0


# === block: score_3 (check id='chi_vibr_check') ===
def score_3(artifact, step, ctx):
    target = step['target']
    tol = step['tolerance']
    val = artifact.get('chi_vibr_W_per_mK')
    if val is not None and abs(val - target) <= tol:
        return 1.0
    return 0.0


# === block: score_4 (check id='zt_check') ===
def score_4(artifact, step, ctx):
    artifact_list = artifact  # list of dicts with bridge, ZT
    thresholds = step.get('thresholds')  # dict bridge -> threshold value
    if not thresholds:
        thresholds = {
            'polyacetylene': 0.03,
            'polypyrrole': 0.40,
            'polythiophene': 0.35
        }
    trend_ok = False
    passed = 0
    total = 0
    zt_values = {}
    for row in artifact_list:
        b = row['bridge']
        zt = float(row['ZT'])
        zt_values[b] = zt
        if b in thresholds:
            if zt >= thresholds[b]:
                passed += 1
            total += 1

    base_score = passed / total if total > 0 else 0.0

    if 'polyacetylene' in zt_values and 'polypyrrole' in zt_values and 'polythiophene' in zt_values:
        if zt_values['polypyrrole'] > zt_values['polythiophene'] > zt_values['polyacetylene']:
            trend_ok = True

    if trend_ok and passed == total and total > 0:
        return 1.0
    elif passed == total and total > 0:
        return 0.8
    return base_score * 0.8


_SCORERS = {
    'eff_masses_check': score_0,
    'ctp_frequencies_check': score_1,
    'seebeck_check': score_2,
    'chi_vibr_check': score_3,
    'zt_check': score_4,
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
