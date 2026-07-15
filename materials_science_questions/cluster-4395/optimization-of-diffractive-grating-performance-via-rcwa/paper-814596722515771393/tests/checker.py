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
    ctx = {}
    for step in spec.get('steps', []):
        sid = step.get('id', '')
        if sid == 'step_01':
            ctx['step_01'] = {
                'expected_texture': step.get('expected_texture'),
                'expected_period': step.get('expected_period'),
                'expected_depth': step.get('expected_depth')
            }
        elif sid == 'step_02':
            ctx['step_02'] = {
                'reference_enhancements': step.get('reference_enhancements', {}),
                'tolerance_rel': step.get('tolerance_rel', 0.15)
            }
        elif sid == 'step_03':
            ctx['step_03'] = {
                'peak_wavelength_window': step.get('peak_wavelength_window', [540, 560]),
                'expected_490_value': step.get('expected_490_value', 20.0),
                'tolerance_490_abs': step.get('tolerance_490_abs', 5.0)
            }
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    cfg = ctx.get('step_01', {})
    if not isinstance(artifact, dict):
        return 0.0
    t = artifact.get('texture')
    p = artifact.get('period_nm')
    d = artifact.get('depth_nm')
    if (t == cfg.get('expected_texture') and p == cfg.get('expected_period') and d == cfg.get('expected_depth')):
        return 1.0
    return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import csv, os, json
    def score(artifact, step, ctx):
        cfg = ctx.get('step_02', {})
        ref = cfg.get('reference_enhancements', {})
        tol = cfg.get('tolerance_rel', 0.15)
        # artifact is a list of dicts from csv.DictReader
        rows = artifact
        if not rows:
            return 0.0
        found = {}
        for row in rows:
            wl = str(row.get('wavelength_nm', '')).strip()
            if wl in ('455', '550'):
                try:
                    val = float(row['enhancement_percent'])
                    found[wl] = val
                except Exception:
                    continue
        if len(found) < 2:
            return 0.0
        scores = []
        for wl in ('455', '550'):
            target = ref.get(wl)
            if target is None:
                continue
            actual = found.get(wl)
            if actual is None:
                scores.append(0.0)
                continue
            # relative error
            if abs(target) < 1e-9:
                s = 1.0 if abs(actual) < 1e-9 else 0.0
            else:
                e = abs(actual - target) / abs(target)
                s = max(0.0, 1.0 - e / tol)
            scores.append(s)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    import csv, os, math
    def score(artifact, step, ctx):
        cfg = ctx.get('step_03', {})
        peak_win = cfg.get('peak_wavelength_window', [540, 560])
        target_490 = cfg.get('expected_490_value', 20.0)
        tol_490 = cfg.get('tolerance_490_abs', 5.0)
        rows = artifact  # list of dicts
        if not rows:
            return 0.0
        # 1. shape check: required columns present
        if any(c not in (rows[0].keys() if rows else {}) for c in ('wavelength_nm', 'enhancement_percent')):
            return 0.0
        # parse data
        data = []
        for row in rows:
            try:
                wl = int(row['wavelength_nm'])
                val = float(row['enhancement_percent'])
                data.append((wl, val))
            except Exception:
                continue
        if not data:
            return 0.0
        data.sort()
        # 2. grid: should cover 400-700 inclusive, step <= 10
        wls = [d[0] for d in data]
        if wls[0] != 400 or wls[-1] != 700:
            return 0.0
        steps = [wls[i+1]-wls[i] for i in range(len(wls)-1)]
        if any(s > 10 or s <= 0 for s in steps):
            return 0.0
        # 3. peak location
        max_val = -float('inf')
        peak_wl = None
        for wl, val in data:
            if val > max_val:
                max_val = val
                peak_wl = wl
        if peak_wl is None:
            return 0.0
        score_peak = 1.0 if (peak_win[0] <= peak_wl <= peak_win[1]) else 0.0
        # 4. monotonic decrease after peak (allow tiny increase < 0.5)
        dec_ok = True
        for i in range(len(data)-1):
            if data[i][0] < peak_wl:
                continue
            if data[i+1][0] <= data[i][0]:
                continue
            if data[i+1][1] > data[i][1] + 0.5:
                dec_ok = False
                break
        score_mono = 1.0 if dec_ok else 0.0
        # 5. value at 490 nm
        val_490 = None
        for wl, val in data:
            if wl == 490:
                val_490 = val
                break
        if val_490 is None:
            score_490 = 0.0
        else:
            diff = abs(val_490 - target_490)
            if diff <= tol_490:
                score_490 = 1.0
            else:
                score_490 = 0.0
        # Weighted sub-scores: format 0.1, peak 0.3, mono 0.3, 490 value 0.3
        # format always 1.0 if we pass initial checks; otherwise return 0.
        # So overall: 0.1*1 + 0.3*score_peak + 0.3*score_mono + 0.3*score_490
        return 0.1 + 0.3*score_peak + 0.3*score_mono + 0.3*score_490


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
