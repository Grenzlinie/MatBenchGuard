import os
import json
import csv

# === author imports / helpers ===
import os, csv, re, math, json


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
        ctx['phase_config'] = None
        ctx['bn_config'] = None
        ctx['sic_config'] = None
        ctx['trend_config'] = None
        for step in spec.get('steps', []):
            cfg = step.get('config', {})
            if step.get('id') == 'phase_diagram_check':
                ctx['phase_config'] = cfg
            elif step.get('id') == 'yield_bn_si3n4_check':
                ctx['bn_config'] = cfg
            elif step.get('id') == 'yield_sic_c_b4c_check':
                ctx['sic_config'] = cfg
            elif step.get('id') == 'trend_summary_check':
                ctx['trend_config'] = cfg
        return ctx


# === block: score_0 (check id='phase_diagram_check') ===
def score_0(artifact, step, ctx):
        config = ctx.get('phase_config', {})
        ref_regions = config.get('reference_regions', [])
        tol_T = config.get('tolerances', {}).get('T', 50)
        tol_delta = config.get('tolerances', {}).get('delta', 0.1)
        def parse_phases(s):
            return set(p.strip() for p in s.split(',') if p.strip())
        correct = 0
        total = 0
        for row in artifact:
            try:
                T = float(row.get('T', 0))
                delta = float(row.get('delta', 0))
                dom = parse_phases(row.get('dominant_phases', ''))
            except Exception:
                continue
            total += 1
            matched = False
            for region in ref_regions:
                if (T >= region['T_min'] - tol_T and T <= region['T_max'] + tol_T and
                    delta >= region['delta_min'] - tol_delta and delta <= region['delta_max'] + tol_delta):
                    expected = set(region['phases'])
                    if dom == expected:
                        matched = True
                        break
            if matched:
                correct += 1
        if total == 0:
            return 0.0
        return correct / total


# === block: score_1 (check id='yield_bn_si3n4_check') ===
def score_1(artifact, step, ctx):
        config = ctx.get('bn_config', {})
        bn_peak_delta = config.get('bn_peak_delta', 0.5)
        bn_peak_tol = config.get('bn_peak_tolerance', 0.15)
        si3n4_thresh = config.get('si3n4_threshold', 0.5)
        if not artifact:
            return 0.0
        # find BN peak location
        best_delta = None
        max_bn = -1
        points = []
        for row in artifact:
            try:
                delta = float(row.get('delta', 0))
                bn = float(row.get('BN_mol', 0))
                si3n4 = float(row.get('Si3N4_mol', 0))
            except Exception:
                continue
            points.append((delta, bn, si3n4))
        if not points:
            return 0.0
        # BN peak
        for delta, bn, _ in points:
            if bn > max_bn:
                max_bn = bn
                best_delta = delta
        score = 0.0
        if best_delta is not None and abs(best_delta - bn_peak_delta) <= bn_peak_tol:
            score += 0.5
        # Si3N4 trend: for delta <= 0.5, should be zero; for delta > 0.5, should be positive
        low_ok = True
        high_ok = True
        low_count = high_count = 0
        for delta, _, si3n4 in points:
            if delta <= si3n4_thresh:
                if si3n4 > 1e-6:
                    low_ok = False
                low_count += 1
            else:
                if si3n4 < 1e-6:
                    high_ok = False
                high_count += 1
        if low_count > 0 and low_ok:
            score += 0.25
        if high_count > 0 and high_ok:
            score += 0.25
        return score


# === block: score_2 (check id='yield_sic_c_b4c_check') ===
def score_2(artifact, step, ctx):
        config = ctx.get('sic_config', {})
        b4c_limit = config.get('b4c_delta_limit', 0.5)
        if not artifact:
            return 0.0
        # Check B4C is near zero for delta > limit
        b4c_high_zero = True
        b4c_low_present = False
        count_high = 0
        count_low = 0
        for row in artifact:
            try:
                delta = float(row.get('delta', 0))
                b4c = float(row.get('B4C_mol', 0))
            except Exception:
                continue
            if delta > b4c_limit:
                count_high += 1
                if b4c > 1e-6:
                    b4c_high_zero = False
            else:
                count_low += 1
                if b4c > 1e-6:
                    b4c_low_present = True
        score = 0.0
        if count_high > 0 and b4c_high_zero:
            score += 0.5
        if count_low > 0 and b4c_low_present:
            score += 0.5
        return score


# === block: score_3 (check id='trend_summary_check') ===
def score_3(artifact, step, ctx):
        config = ctx.get('trend_config', {})
        required_kw = config.get('required_keywords', [])
        min_len = config.get('min_length', 100)
        text = artifact if isinstance(artifact, str) else ''
        if len(text) < min_len:
            return 0.0
        lower = text.lower()
        hits = sum(1 for kw in required_kw if kw.lower() in lower)
        ratio = hits / len(required_kw) if required_kw else 1.0
        # also check that it mentions 'decrease' and 'phase'
        if 'decrease' in lower or 'fewer' in lower or 'reduce' in lower:
            ratio = min(1.0, ratio + 0.2)
        return min(1.0, ratio)


_SCORERS = {
    'phase_diagram_check': score_0,
    'yield_bn_si3n4_check': score_1,
    'yield_sic_c_b4c_check': score_2,
    'trend_summary_check': score_3,
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
