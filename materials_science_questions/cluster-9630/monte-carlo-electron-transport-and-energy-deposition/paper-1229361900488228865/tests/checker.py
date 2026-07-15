import os
import json
import csv


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


# === block: score_0 (check id='photon_fluence_vs_Ta') ===
def score_0(artifact, step, ctx):
    # hidden reference curve from digitised Fig. 5 (fluence in 1/cm^2 per source electron)
    _ref_fluence = {
        0.1: 2.0e-06,
        0.2: 5.0e-06,
        0.5: 1.2e-05,
        1.0: 2.0e-05,
        1.5: 2.5e-05,
        2.0: 2.3e-05,
        3.0: 1.8e-05,
        5.0: 8.0e-06,
        10.0: 1.0e-06
    }

    rows = artifact
    if not rows:
        return 0.0
    if not all(k in rows[0] for k in ('Ta_thickness_mm','photon_fluence_1percm2','total_photons_produced')):
        return 0.0
    try:
        data = [(float(r['Ta_thickness_mm']), float(r['photon_fluence_1percm2']), float(r['total_photons_produced'])) for r in rows]
    except (ValueError, KeyError):
        return 0.0
    data.sort(key=lambda x: x[0])
    thicknesses = [d[0] for d in data]
    fluences = [d[1] for d in data]
    totals = [d[2] for d in data]

    # ----------------------------------------------------------------------------------
    # check 1: fluence peak location (30% of step weight)
    max_idx = max(range(len(fluences)), key=lambda i: fluences[i])
    peak_fluence = fluences[max_idx]
    peak_thickness = thicknesses[max_idx]
    peak_in_range = 1.0 <= peak_thickness <= 2.0
    peak_score = 0.3 if peak_in_range else 0.0
    if peak_fluence < 1e-6:
        peak_score = 0.0

    # check 2: total_photons_produced monotonically non‑decreasing with small slack (20%)
    mono_penalty = 0.0
    n = len(totals)
    if n > 1:
        for i in range(n-1):
            if totals[i] > 0 and totals[i+1] < totals[i] * 0.99:
                mono_penalty += 1.0
        mono_score_val = 0.2 * max(0.0, 1.0 - mono_penalty/(n-1))
    else:
        mono_score_val = 0.0

    # check 3: basic shape – at least 4 thickness points, fluence not all identical (20%)
    shape_ok = n >= 4 and max(fluences) > min(fluences)
    shape_score = 0.2 if shape_ok else 0.0

    # ----------------------------------------------------------------------------------
    # check 4: reference curve match (30%) – each fluence within factor 3 of hidden gold
    matched = 0
    for d in data:
        t, fl, _ = d
        if t in _ref_fluence and fl > 0 and _ref_fluence[t] > 0:
            ratio = fl / _ref_fluence[t]
            if 1.0/3.0 <= ratio <= 3.0:
                matched += 1
    possible = sum(1 for d in data if d[0] in _ref_fluence)
    ref_score = (0.3 * (matched / possible)) if possible else 0.0

    return peak_score + mono_score_val + shape_score + ref_score


# === block: score_1 (check id='neutron_yield_vs_ErD3') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    if not all(k in rows[0] for k in ('ErD3_thickness_cm','configuration','total_neutrons_per_source_electron','directional_neutrons_per_source_electron')):
        return 0.0
    try:
        by_config = {'without_Ta':[], 'with_Ta':[]}
        for r in rows:
            cfg = r['configuration'].strip()
            if cfg not in by_config:
                by_config[cfg] = []
            by_config[cfg].append((float(r['ErD3_thickness_cm']), float(r['total_neutrons_per_source_electron']), float(r['directional_neutrons_per_source_electron'])))
    except (ValueError, KeyError):
        return 0.0
    if not by_config['without_Ta'] or not by_config['with_Ta']:
        return 0.0

    def monotonic_ratio(data):
        # data sorted by thickness
        data.sort(key=lambda x: x[0])
        vals = [x[1] for x in data]
        if len(vals) < 2:
            return 0.0
        n = len(vals)
        viol = 0.0
        for i in range(n-1):
            if vals[i] > 0 and vals[i+1] < vals[i] * 0.99:
                viol += 1.0
        return max(0.0, 1.0 - viol/(n-1))

    # Check 1: monotonic total_neutrons for both configs (40%)
    mono_without = monotonic_ratio(by_config['without_Ta'])
    mono_with = monotonic_ratio(by_config['with_Ta'])
    mono_score = 0.4 * ((mono_without + mono_with) / 2.0)

    # Check 2: directional yield peak within 9-15 cm (40%)
    def directional_peak_ok(data):
        d = sorted(data, key=lambda x: x[0])
        max_d = max(d, key=lambda x: x[2])
        if 9.0 <= max_d[0] <= 15.0:
            return 1.0
        return 0.0
    dir_without = directional_peak_ok(by_config['without_Ta'])
    dir_with = directional_peak_ok(by_config['with_Ta'])
    dir_score = 0.4 * ((dir_without + dir_with) / 2.0)

    # Check 3: total neutron yields with and without Ta are within factor 2 (20%)
    try:
        max_total_wo = max(x[1] for x in by_config['without_Ta'])
        max_total_w  = max(x[1] for x in by_config['with_Ta'])
        if max_total_wo <= 0 or max_total_w <= 0:
            ratio_score = 0.0
        else:
            ratio = max_total_wo / max_total_w
            if 0.5 <= ratio <= 2.0:
                ratio_score = 1.0
            else:
                ratio_score = 0.0
    except:
        ratio_score = 0.0
    ratio_score_val = 0.2 * ratio_score

    return mono_score + dir_score + ratio_score_val


# === block: score_2 (check id='summary_results') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, str):
        return 0.0
    try:
        lines = artifact.strip().splitlines()
        vals = {}
        for line in lines:
            if ':' in line:
                k, v = line.split(':', 1)
                vals[k.strip()] = float(v.strip())
    except:
        return 0.0

    # each of four items contributes 0.25 to score
    score = 0.0

    # optimal_Ta_thickness_mm
    if 'optimal_Ta_thickness_mm' in vals:
        if 1.0 <= vals['optimal_Ta_thickness_mm'] <= 2.0:
            score += 0.25
    # overall_neutrons_per_source_electron
    if 'overall_neutrons_per_source_electron' in vals:
        if 1e-5 <= vals['overall_neutrons_per_source_electron'] <= 1e-3:
            score += 0.25
    # directional_neutrons_per_source_electron
    if 'directional_neutrons_per_source_electron' in vals:
        if 1e-7 <= vals['directional_neutrons_per_source_electron'] <= 1e-5:
            score += 0.25
    # optimal_ErD3_thickness_for_directional_cm
    if 'optimal_ErD3_thickness_for_directional_cm' in vals:
        if 8.0 <= vals['optimal_ErD3_thickness_for_directional_cm'] <= 16.0:
            score += 0.25

    return score


_SCORERS = {
    'photon_fluence_vs_Ta': score_0,
    'neutron_yield_vs_ErD3': score_1,
    'summary_results': score_2,
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
