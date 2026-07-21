import os
import json
import csv

# === author imports / helpers ===
import json, math
from statistics import mean, stdev


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


# === block: score_0 (check id='check_segment_stats') ===
def score_0(artifact, step, ctx):
    segs = artifact.get('trajectory_segments', {})
    if not segs:
        return 0.0
    segment_keys = ['PBE+D3', 'PBE+U+D3']
    scores = []
    for key in segment_keys:
        seg = segs.get(key, {})
        ts = seg.get('time_series', [])
        if not ts:
            scores.extend([0.0, 0.0])
            continue
        ds_vals = []
        for entry in ts:
            if isinstance(entry, dict) and 'ds_vs_vbm_eV' in entry and isinstance(entry['ds_vs_vbm_eV'], (int, float)):
                ds_vals.append(entry['ds_vs_vbm_eV'])
        if len(ds_vals) < 2:
            scores.extend([0.0, 0.0])
            continue
        m = mean(ds_vals)
        s = stdev(ds_vals) if len(ds_vals) > 1 else 0.0
        target = step['target'][key]
        gold_mean = target['mean']
        gold_std = target['std']
        tol_mean = target['tolerance_mean']
        tol_std = target['tolerance_std']
        sc_mean = max(0.0, 1.0 - abs(m - gold_mean) / tol_mean)
        sc_std = max(0.0, 1.0 - abs(s - gold_std) / tol_std)
        scores.append(sc_mean)
        scores.append(sc_std)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='check_alignment') ===
def score_1(artifact, step, ctx):
    align = artifact.get('alignment', {})
    if not align:
        return 0.0
    vbm = align.get('vbm_vs_rhe_V')
    ds = align.get('ds_level_vs_rhe_V')
    if vbm is None or ds is None:
        return 0.0
    target = step['target']
    gold_vbm = target['vbm_vs_rhe_V']
    gold_ds = target['ds_level_vs_rhe_V']
    tol = target['tolerance_V']
    sc_vbm = max(0.0, 1.0 - abs(vbm - gold_vbm) / tol)
    sc_ds = max(0.0, 1.0 - abs(ds - gold_ds) / tol)
    return (sc_vbm + sc_ds) / 2.0


# === block: score_2 (check id='check_duration_gap') ===
def score_2(artifact, step, ctx):
    segs = artifact.get('trajectory_segments', {})
    if not segs:
        return 0.0
    tar = step['target']
    ok = True
    for key, bounds in tar.items():
        seg = segs.get(key, {})
        dur = seg.get('duration_ps')
        if not isinstance(dur, (int, float)) or dur < bounds['duration_ps_min'] or dur > bounds['duration_ps_max']:
            ok = False
            break
        ts = seg.get('time_series', [])
        gaps = []
        for entry in ts:
            if isinstance(entry, dict) and 'vbm_cbm_gap_eV' in entry and isinstance(entry['vbm_cbm_gap_eV'], (int, float)):
                gaps.append(entry['vbm_cbm_gap_eV'])
        if not gaps:
            ok = False
            break
        avg_gap = sum(gaps) / len(gaps)
        if avg_gap < bounds['gap_min'] or avg_gap > bounds['gap_max']:
            ok = False
            break
    return 1.0 if ok else 0.0


_SCORERS = {
    'check_segment_stats': score_0,
    'check_alignment': score_1,
    'check_duration_gap': score_2,
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
