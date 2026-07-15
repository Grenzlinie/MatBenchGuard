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


# === block: score_0 (check id='energy_deposition_powerlaw') ===
def score_0(artifact, step, ctx):
    if len(artifact) != 30:
        return 0.0
    try:
        altitudes = []
        proton_vals = {g:[] for g in [0,1,2,3]}
        electron_vals = {g:[] for g in [0,1,2,3]}
        for row in artifact:
            alt = float(row['altitude_km'])
            altitudes.append(alt)
            for g in [0,1,2,3]:
                proton_vals[g].append(float(row[f'p_gamma{g}']))
                electron_vals[g].append(float(row[f'e_gamma{g}']))
    except (KeyError, ValueError):
        return 0.0
    sorted_indices = sorted(range(len(altitudes)), key=lambda i: altitudes[i])
    altitudes = [altitudes[i] for i in sorted_indices]
    for g in [0,1,2,3]:
        proton_vals[g] = [proton_vals[g][i] for i in sorted_indices]
        electron_vals[g] = [electron_vals[g][i] for i in sorted_indices]
    def centroid(alts, vals):
        total = sum(vals)
        if total == 0:
            return 0.0
        return sum(a*v for a,v in zip(alts, vals)) / total
    p_centroids = [centroid(altitudes, proton_vals[g]) for g in [0,1,2,3]]
    e_centroids = [centroid(altitudes, electron_vals[g]) for g in [0,1,2,3]]
    pairs = [(0,1),(1,2),(2,3)]
    correct_p = sum(1 for a,b in pairs if p_centroids[a] < p_centroids[b])
    p_order_score = correct_p / len(pairs)
    correct_e = sum(1 for a,b in pairs if e_centroids[a] < e_centroids[b])
    e_order_score = correct_e / len(pairs)
    cross_pairs = sum(1 for a,b in zip(e_centroids, p_centroids) if a < b)
    cross_score = cross_pairs / 4.0
    score = 0.5 * p_order_score + 0.3 * e_order_score + 0.2 * cross_score
    return score


# === block: score_1 (check id='ion_production_oct1989') ===
def score_1(artifact, step, ctx):
    if len(artifact) != 30:
        return 0.0
    try:
        rows = artifact
        altitudes = [float(r['altitude_km']) for r in rows]
        proton = [float(r['proton_rate']) for r in rows]
        electron = [float(r['electron_rate']) for r in rows]
        total = [float(r['total_rate']) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    max_rel_diff = 0.0
    total_max = max(total) if total else 1.0
    for p,e,t in zip(proton, electron, total):
        diff = abs(t - (p+e))
        rel = diff / max(total_max, 1e-30)
        if rel > max_rel_diff:
            max_rel_diff = rel
    consistency_score = max(0.0, 1.0 - max_rel_diff / 0.01)
    max_e = max(electron) if electron else 0
    if max_e == 0:
        peak_alt = 0
    else:
        max_idx = electron.index(max_e)
        peak_alt = altitudes[max_idx]
    peak_score = 1.0 if 50.0 <= peak_alt <= 70.0 else 0.0
    low_idx = None
    for i,a in enumerate(altitudes):
        if a <= 10.0:
            low_idx = i
        else:
            break
    if low_idx is None:
        low_ratio_score = 0.0
    else:
        r_low = electron[low_idx] / (proton[low_idx] + electron[low_idx] + 1e-30)
        low_ratio_score = 1.0 if r_low < 0.1 else 0.0
    ratios_50_70 = []
    for i,a in enumerate(altitudes):
        if 50.0 <= a <= 70.0:
            r = electron[i] / (proton[i] + electron[i] + 1e-30)
            ratios_50_70.append(r)
    if not ratios_50_70:
        mid_ratio_score = 0.0
    else:
        max_ratio = max(ratios_50_70)
        mid_ratio_score = 1.0 if 0.2 <= max_ratio <= 0.5 else 0.0
    score = 0.3 * consistency_score + 0.3 * peak_score + 0.2 * low_ratio_score + 0.2 * mid_ratio_score
    return score


# === block: score_2 (check id='ion_production_jun1989') ===
def score_2(artifact, step, ctx):
    if len(artifact) != 30:
        return 0.0
    try:
        rows = artifact
        altitudes = [float(r['altitude_km']) for r in rows]
        proton = [float(r['proton_rate']) for r in rows]
        electron = [float(r['electron_rate']) for r in rows]
        total = [float(r['total_rate']) for r in rows]
    except (KeyError, ValueError):
        return 0.0
    max_rel_diff = 0.0
    total_max = max(total) if total else 1.0
    for p,e,t in zip(proton, electron, total):
        diff = abs(t - (p+e))
        rel = diff / max(total_max, 1e-30)
        if rel > max_rel_diff:
            max_rel_diff = rel
    consistency_score = max(0.0, 1.0 - max_rel_diff / 0.01)
    idx_70 = None
    for i,a in enumerate(altitudes):
        if a >= 70.0:
            idx_70 = i
            break
    if idx_70 is None:
        idx_70 = len(altitudes)-1
    electron_dom_score = 1.0 if (electron[idx_70] > proton[idx_70]) else 0.0
    max_e = max(electron) if electron else 0
    if max_e == 0:
        peak_alt = 0
    else:
        max_idx = electron.index(max_e)
        peak_alt = altitudes[max_idx]
    peak_score = 1.0 if 50.0 <= peak_alt <= 70.0 else 0.0
    score = 0.3 * consistency_score + 0.4 * electron_dom_score + 0.3 * peak_score
    return score


_SCORERS = {
    'energy_deposition_powerlaw': score_0,
    'ion_production_oct1989': score_1,
    'ion_production_jun1989': score_2,
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
