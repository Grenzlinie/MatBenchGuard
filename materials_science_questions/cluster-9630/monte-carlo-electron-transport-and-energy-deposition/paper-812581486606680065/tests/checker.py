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


# === block: score_0 (check id='thick_depth') ===
def score_0(artifact, step, ctx):
    import math

    expected_energies = set(step.get('expected_energies', []))
    expected_depths = set(step.get('expected_depths', []))
    ratio_first_min, ratio_first_max = step.get('ratio_first_bin', [0.18, 0.26])
    ratio_deep_max = step.get('ratio_deep_max', 0.03)
    deep_start = step.get('deep_depth_start', 10)

    rows_by_energy = {}
    for row in artifact:
        try:
            e = int(float(row['energy_MeV']))
            d = int(float(row['depth_mm']))
            ph = float(row['photonuclear_yield_per_e'])
            el = float(row['electronuclear_yield_per_e'])
            r = float(row['ratio'])
        except (ValueError, KeyError):
            continue
        rows_by_energy.setdefault(e, []).append((d, ph, el, r))

    if set(rows_by_energy.keys()) != expected_energies:
        return 0.0

    sub_scores = []
    for e in sorted(rows_by_energy.keys()):
        rows = sorted(rows_by_energy[e], key=lambda x: x[0])
        depths = [d for d,_,_,_ in rows]
        phs = [ph for _,ph,_,_ in rows]
        els = [el for _,_,el,_ in rows]
        ratios = [r for _,_,_,r in rows]

        # monotonic decrease of electronuclear yield
        el_decrease = all(els[i+1] <= els[i] + 1e-12 for i in range(len(els)-1))
        sub_scores.append(0.2 if el_decrease else 0.0)

        # photonuclear buildup: max not at depth 0 and increase in early bins
        ph_max_idx = phs.index(max(phs))
        has_buildup = ph_max_idx > 0 and any(phs[i+1] > phs[i] for i in range(0, min(5, len(phs)-1)))
        sub_scores.append(0.2 if has_buildup else 0.0)

        # ratio first bin
        if len(rows) > 0 and depths[0] == 0:
            r0 = ratios[0]
            first_ok = ratio_first_min <= r0 <= ratio_first_max
            sub_scores.append(0.2 if first_ok else 0.0)
        else:
            sub_scores.append(0.0)

        # ratio deep bins
        deep_ratios = [ratios[i] for i, d in enumerate(depths) if d >= deep_start]
        deep_ok = deep_ratios and all(rr <= ratio_deep_max for rr in deep_ratios)
        sub_scores.append(0.3 if deep_ok else 0.0)

        # non-negative yields
        nonneg = all(v >= 0 for v in phs + els)
        sub_scores.append(0.1 if nonneg else 0.0)

    # average over energies
    mean_score = sum(sub_scores) / (len(sub_scores) + 1e-12)
    return min(1.0, max(0.0, mean_score))


# === block: score_1 (check id='thin_depth') ===
def score_1(artifact, step, ctx):
    expected_energies = set(step.get('expected_energies', []))
    expected_depths_set = set(step.get('expected_depths', []))
    ratio_min, ratio_max = step.get('ratio_last_bin', [0.14, 0.26])

    rows_by_energy = {}
    for row in artifact:
        try:
            e = int(float(row['energy_MeV']))
            d = float(row['depth_mm'])
            ph = float(row['photonuclear_yield_per_e'])
            el = float(row['electronuclear_yield_per_e'])
            r = float(row['ratio'])
        except (ValueError, KeyError):
            continue
        rows_by_energy.setdefault(e, []).append((d, ph, el, r))

    if set(rows_by_energy.keys()) != expected_energies:
        return 0.0

    sub_scores = []
    for e in sorted(rows_by_energy.keys()):
        rows = sorted(rows_by_energy[e], key=lambda x: x[0])
        depths = [d for d,_,_,_ in rows]
        phs = [ph for _,ph,_,_ in rows]
        els = [el for _,_,el,_ in rows]
        ratios = [r for _,_,_,r in rows]

        # check depths cover expected
        if set(depths) != expected_depths_set:
            sub_scores.append(0.0)
            continue

        # photonuclear monotonic increase
        ph_increase = all(phs[i+1] >= phs[i] - 1e-12 for i in range(len(phs)-1))
        # electronuclear slight decrease (not strictly enforced but acceptable)
        el_decrease = all(els[i+1] <= els[i] + 1e-12 for i in range(len(els)-1))
        # ratio at last depth (0.9 mm)
        last_idx = depths.index(0.9) if 0.9 in depths else None
        if last_idx is not None:
            last_ratio = ratios[last_idx]
            ratio_ok = ratio_min <= last_ratio <= ratio_max
        else:
            ratio_ok = False
        # non-negative
        nonneg = all(v >= 0 for v in phs + els)
    
        sub = 0.0
        if ph_increase:
            sub += 0.25
        if el_decrease:
            sub += 0.15
        if ratio_ok:
            sub += 0.4
        if nonneg:
            sub += 0.2
        sub_scores.append(sub)

    mean_score = sum(sub_scores) / max(len(sub_scores), 1)
    return min(1.0, max(0.0, mean_score))


# === block: score_2 (check id='thick_total') ===
def score_2(artifact, step, ctx):
    expected_energies = set(step.get('expected_energies', []))
    max_ratio = step.get('max_ratio', 0.05)
    decay_max_ratio = step.get('decay_max_ratio', 0.15)

    rows_by_energy = {}
    for row in artifact:
        try:
            e = int(float(row['energy_MeV']))
            ph = float(row['total_photonuclear_yield_per_e'])
            el = float(row['total_electronuclear_yield_per_e'])
            ratio = float(row['ratio_total'])
        except (ValueError, KeyError):
            continue
        rows_by_energy[e] = (ph, el, ratio)

    if set(rows_by_energy.keys()) != expected_energies:
        return 0.0

    scores = []
    for e in expected_energies:
        if e not in rows_by_energy:
            scores.append(0.0)
            continue
        ph, el, ratio = rows_by_energy[e]
        # positivity
        if ph <= 0 or el <= 0:
            scores.append(0.0)
            continue
        # ratio threshold: full if <= max_ratio, decaying to 0 at decay_max_ratio
        if ratio <= max_ratio:
            scores.append(1.0)
        elif ratio >= decay_max_ratio:
            scores.append(0.0)
        else:
            scores.append(1.0 - (ratio - max_ratio) / (decay_max_ratio - max_ratio))

    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='fraction_vs_thickness') ===
def score_3(artifact, step, ctx):
    expected_thicknesses = set(step.get('expected_thicknesses', []))
    fraction_1mm_min, fraction_1mm_max = step.get('fraction_1mm_range', [0.15, 0.25])
    fraction_01mm_min = step.get('fraction_01mm_min', 0.65)

    rows = []
    for row in artifact:
        try:
            t = float(row['thickness_mm'])
            ph = float(row['total_photonuclear_yield_per_e'])
            el = float(row['total_electronuclear_yield_per_e'])
            fra = float(row['fraction_electronuclear'])
        except (ValueError, KeyError):
            continue
        rows.append((t, ph, el, fra))

    # verify required thicknesses present
    present_thicknesses = set(t for t,_,_,_ in rows)
    if not expected_thicknesses.issubset(present_thicknesses):
        return 0.0

    # sort by thickness
    rows_sorted = sorted(rows, key=lambda x: x[0])
    thicknesses = [t for t,_,_,_ in rows_sorted]
    phs = [ph for _,ph,_,_ in rows_sorted]
    els = [el for _,_,el,_ in rows_sorted]
    fractions = [fra for _,_,_,fra in rows_sorted]

    score = 0.0

    # fraction at 1 mm
    row_1mm = None
    for row in rows_sorted:
        if abs(row[0] - 1.0) < 1e-6:
            row_1mm = row
            break
    if row_1mm and fraction_1mm_min <= row_1mm[3] <= fraction_1mm_max:
        score += 0.3

    # fraction at 0.1 mm
    row_01mm = None
    for row in rows_sorted:
        if abs(row[0] - 0.1) < 1e-6:
            row_01mm = row
            break
    if row_01mm and row_01mm[3] > fraction_01mm_min:
        score += 0.3

    # fraction decreasing with thickness
    if len(fractions) >= 2:
        dec = all(fractions[i+1] <= fractions[i] + 1e-12 for i in range(len(fractions)-1))
        if dec:
            score += 0.2

    # photonuclear yield increasing
    ph_inc = all(phs[i+1] >= phs[i] - 1e-12 for i in range(len(phs)-1))
    if ph_inc:
        score += 0.1

    # non-negative yields
    nonneg = all(v >= 0 for v in phs + els) and all(0 <= f <= 1 for f in fractions)
    if nonneg:
        score += 0.1

    return min(1.0, max(0.0, score))


_SCORERS = {
    'thick_depth': score_0,
    'thin_depth': score_1,
    'thick_total': score_2,
    'fraction_vs_thickness': score_3,
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
