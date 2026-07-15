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
    import csv, os

    bg_path = os.path.join(outputs_dir, "bandgap_vs_strain.csv")
    bandgap_rows = []
    if os.path.exists(bg_path):
        with open(bg_path, newline='') as f:
            bandgap_rows = list(csv.DictReader(f))
    be_path = os.path.join(outputs_dir, "band_edges_vs_strain.csv")
    be_rows = []
    if os.path.exists(be_path):
        with open(be_path, newline='') as f:
            be_rows = list(csv.DictReader(f))
    return {"bandgap_rows": bandgap_rows, "be_rows": be_rows}


# === block: score_0 (check id='bandgap_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    data = {}
    for row in rows:
        s = row['structure'].strip()
        try:
            strain = float(row['strain'])
            gap = float(row['bandgap'])
        except Exception:
            continue
        data.setdefault(s, []).append((strain, gap))

    gold = step.get('gold', {})
    tol = gold.get('tolerance', 0.1)
    scores = []

    # HPSi range
    if 'HPSi' in data:
        vals = [g for st, g in data['HPSi'] if -10.0 <= st <= 10.0]
        if vals:
            target_min, target_max = gold['hpsi_range']
            scores.append(1.0 if abs(min(vals) - target_min) <= tol else 0.0)
            scores.append(1.0 if abs(max(vals) - target_max) <= tol else 0.0)
        else:
            scores.extend([0.0, 0.0])
    else:
        scores.extend([0.0, 0.0])

    # HSiP specific points
    if 'HSiP' in data:
        hsip_dict = {st: g for st, g in data['HSiP']}
        pts = gold['hsip_points']
        pt_ok = 0
        pt_n = 0
        for strain_str, target in pts.items():
            strain_val = float(strain_str)
            if strain_val in hsip_dict:
                if abs(hsip_dict[strain_val] - target) <= tol:
                    pt_ok += 1
                pt_n += 1
        scores.append(pt_ok / pt_n if pt_n else 0.0)
        # HSiP compression range
        comp_v = [g for st, g in data['HSiP'] if -10.0 <= st <= -3.0]
        if comp_v:
            t_min, t_max = gold['hsip_compression_range']
            scores.append(1.0 if abs(min(comp_v) - t_min) <= tol else 0.0)
            scores.append(1.0 if abs(max(comp_v) - t_max) <= tol else 0.0)
        else:
            scores.extend([0.0, 0.0])
    else:
        scores.extend([0.0, 0.0, 0.0])

    # HSiPbp ranges
    if 'HSiPbp' in data:
        # compression
        cvals = [g for st, g in data['HSiPbp'] if -10.0 <= st <= -5.0]
        if cvals:
            tmin, tmax = gold['hsipbp_compression_range']
            scores.append(1.0 if abs(min(cvals) - tmin) <= tol else 0.0)
            scores.append(1.0 if abs(max(cvals) - tmax) <= tol else 0.0)
        else:
            scores.extend([0.0, 0.0])
        # tensile
        tvals = [g for st, g in data['HSiPbp'] if 5.0 <= st <= 10.0]
        if tvals:
            tmin, tmax = gold['hsipbp_tensile_range']
            scores.append(1.0 if abs(min(tvals) - tmin) <= tol else 0.0)
            scores.append(1.0 if abs(max(tvals) - tmax) <= tol else 0.0)
        else:
            scores.extend([0.0, 0.0])
    else:
        scores.extend([0.0, 0.0, 0.0, 0.0])

    if scores:
        return sum(scores) / len(scores)
    return 0.0


# === block: score_1 (check id='bandedge_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    # build band-edge dict
    be_data = {}
    for row in rows:
        s = row['structure'].strip()
        try:
            strain = float(row['strain'])
            cbm = float(row['CBM'])
            vbm = float(row['VBM'])
        except Exception:
            continue
        be_data.setdefault(s, []).append((strain, cbm, vbm))

    # build bandgap dict from ctx
    bg_rows = ctx.get('bandgap_rows', [])
    bg_data = {}
    for row in bg_rows:
        s = row['structure'].strip()
        try:
            strain = float(row['strain'])
            gap = float(row['bandgap'])
        except Exception:
            continue
        bg_data.setdefault(s, []).append((strain, gap))

    gold = step.get('gold', {})
    cons_tol = gold['consistency_tolerance']
    redox_h = gold['redox_h']
    redox_o = gold['redox_o']
    straddle_tol = gold.get('straddle_tol', 0.0001)

    # consistency sub-score
    cons_count = 0
    total_count = 0
    for struct in ['HPSi', 'HSiP', 'HSiPbp']:
        bg_map = {st: gap for st, gap in bg_data.get(struct, [])}
        for st, cbm, vbm in be_data.get(struct, []):
            if st in bg_map:
                gap_from_edges = cbm - vbm
                diff = abs(gap_from_edges - bg_map[st])
                total_count += 1
                if diff <= cons_tol:
                    cons_count += 1

    consist_score = cons_count / total_count if total_count else 0.0

    # zero-strain straddle
    straddle_ok = 0
    for struct in ['HPSi', 'HSiP', 'HSiPbp']:
        match = [(cbm, vbm) for st, cbm, vbm in be_data.get(struct, []) if abs(st) < 1e-4]
        if match:
            cbm, vbm = match[0]
            if cbm >= redox_h - straddle_tol and vbm <= redox_o + straddle_tol:
                straddle_ok += 1
    straddle_score = straddle_ok / 3.0

    return 0.6 * consist_score + 0.4 * straddle_score


_SCORERS = {
    'bandgap_check': score_0,
    'bandedge_check': score_1,
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
