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


# === block: score_0 (check id='band_gap_vs_concentration') ===
def score_0(artifact, step, ctx):
    rows = artifact   # list of dicts with concentration, structure_id, band_gap_eV

    # group by concentration
    groups = {}
    for r in rows:
        try:
            c = float(r['concentration'])
            g = float(r['band_gap_eV'])
        except (ValueError, TypeError):
            return 0.0
        groups.setdefault(c, []).append(g)

    if len(groups) < 2:
        return 0.0  # need at least two concentrations to check trend

    # sub-checks
    UB = 4.5  # eV upper bound coefficient
    eps = 1e-9

    # 1. all gaps positive and <= UB * concentration
    gaps_ok = True
    for conc, vals in groups.items():
        limit = UB * conc + eps
        for v in vals:
            if v <= 0 or v > limit:
                gaps_ok = False
                break
        if not gaps_ok:
            break

    # 2. average gap increases with concentration
    concentrations = sorted(groups.keys())
    avgs = [sum(groups[c])/len(groups[c]) for c in concentrations]
    increasing_avg = all(avgs[i] < avgs[i+1] for i in range(len(avgs)-1))

    # combine scores (weights: 0.6 for gaps, 0.4 for increasing trend)
    sub = 0.0
    if gaps_ok:
        sub += 0.6
    if increasing_avg:
        sub += 0.4

    return sub


# === block: score_1 (check id='band_gap_vs_strain') ===
def score_1(artifact, step, ctx):
    rows = artifact   # list of dicts with structure_id, strain_direction, strain, band_gap_eV

    # group by (structure_id, direction) sorted by strain
    series = {}
    for r in rows:
        sid = str(r['structure_id'])
        direc = str(r['strain_direction']).strip().lower()
        strain = float(r['strain'])
        gap = float(r['band_gap_eV'])
        key = (sid, direc)
        if key not in series:
            series[key] = []
        series[key].append((strain, gap))

    # sort by strain and extract gaps
    for key in series:
        sorted_pairs = sorted(series[key], key=lambda x: x[0])
        series[key] = [g for _, g in sorted_pairs]

    # must have exactly 4 curves (2 structures * 2 directions)
    if len(series) != 4:
        return 0.0

    # check each curve: non-monotonic and has interior local extremum
    per_curve_score = 0.0
    for (sid, direc), gaps in series.items():
        if len(gaps) < 3:
            continue
        diffs = [gaps[i+1] - gaps[i] for i in range(len(gaps)-1)]
        non_mono = (min(diffs) < 0 and max(diffs) > 0)  # sign change
        has_extremum = False
        for i in range(1, len(gaps)-1):
            if (gaps[i] > gaps[i-1] and gaps[i] > gaps[i+1]) or (gaps[i] < gaps[i-1] and gaps[i] < gaps[i+1]):
                has_extremum = True
                break
        per_curve_score += (0.1 if non_mono else 0.0) + (0.1 if has_extremum else 0.0)

    # global opposite anisotropy check
    # determine extremum type (peak or valley) per structure per direction
    types = {}  # sid -> {direction: 'peak'/'valley'}
    for (sid, direc), gaps in series.items():
        if len(gaps) < 3:
            continue
        peaks = valleys = False
        for i in range(1, len(gaps)-1):
            if gaps[i] > gaps[i-1] and gaps[i] > gaps[i+1]:
                peaks = True
            if gaps[i] < gaps[i-1] and gaps[i] < gaps[i+1]:
                valleys = True
        if peaks and not valleys:
            extype = 'peak'
        elif valleys and not peaks:
            extype = 'valley'
        else:
            extype = 'mixed'
        types.setdefault(sid, {})[direc] = extype

    # we need two structures
    sids = list(types.keys())
    if len(sids) != 2:
        opposite_ok = False
    else:
        a, b = sids
        dirs = ['armchair', 'zigzag']
        # check both directions have opposite extremum types across the two structures
        ok = True
        for d in dirs:
            ta = types[a].get(d)
            tb = types[b].get(d)
            if ta is None or tb is None or ta == tb or ta == 'mixed' or tb == 'mixed':
                ok = False
                break
        if ok:
            # also verify that the direction with peak for A is the one with valley for B
            # i.e., for armchair: A has peak, B has valley  -> (ta_arm == 'peak' and tb_arm == 'valley')
            # and zigzag: A has valley, B has peak -> (ta_zig == 'valley' and tb_zig == 'peak')
            # or the opposite swap.
            arm_a = types[a].get('armchair')
            zig_a = types[a].get('zigzag')
            arm_b = types[b].get('armchair')
            zig_b = types[b].get('zigzag')
            ok = (
                (arm_a == 'peak' and zig_a == 'valley' and arm_b == 'valley' and zig_b == 'peak') or
                (arm_a == 'valley' and zig_a == 'peak' and arm_b == 'peak' and zig_b == 'valley')
            )
        opposite_ok = ok

    # combine: per-curve shape (max 0.8) + opposite anisotropy (0.2)
    shape_score = per_curve_score
    # ensure max 0.8 (could be up to 0.2*4=0.8)
    shape_score = min(0.8, shape_score)
    global_score = 0.2 if opposite_ok else 0.0
    return shape_score + global_score


_SCORERS = {
    'band_gap_vs_concentration': score_0,
    'band_gap_vs_strain': score_1,
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
