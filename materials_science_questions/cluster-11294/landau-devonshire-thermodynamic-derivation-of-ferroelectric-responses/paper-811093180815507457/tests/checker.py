import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    def prepare(outputs_dir, spec):
        def load_csv(path):
            if not os.path.exists(path):
                return None
            with open(path, newline='') as f:
                return list(csv.DictReader(f))
        stress_free = load_csv(os.path.join(outputs_dir, 'deltaT_stress_free.csv'))
        strained = load_csv(os.path.join(outputs_dir, 'deltaT_strained.csv'))
        ctx = {}
        if stress_free:
            sf_peaks = {}
            for field in sorted(set(r['field'] for r in stress_free)):
                rows_f = [r for r in stress_free if r['field'] == field]
                max_dT = max(float(r['deltaT']) for r in rows_f)
                sf_peaks[field] = max_dT
            ctx['stress_free_peaks'] = sf_peaks
            rows_500 = [r for r in stress_free if r['field'] == '500']
            if rows_500:
                max_dT = sf_peaks['500']
                half = max_dT / 2.0
                temps_above = sorted([float(r['temperature']) for r in rows_500 if float(r['deltaT']) >= half])
                if temps_above:
                    ctx['stress_free_fwhm_500'] = temps_above[-1] - temps_above[0]
                else:
                    ctx['stress_free_fwhm_500'] = 0.0
            high_temp_rows = [r for r in stress_free if float(r['temperature']) >= 900]
            neg_count = sum(1 for r in high_temp_rows if float(r['deltaT']) < 0)
            total = len(high_temp_rows)
            ctx['stress_free_high_neg_frac'] = neg_count / total if total > 0 else 0.0
        if strained:
            strn_peaks = {}
            for field in sorted(set(r['field'] for r in strained)):
                rows_f = [r for r in strained if r['field'] == field]
                max_dT = max(float(r['deltaT']) for r in rows_f)
                strn_peaks[field] = max_dT
            ctx['strained_peaks'] = strn_peaks
            if '500' in strn_peaks:
                max_dT = strn_peaks['500']
                half = max_dT / 2.0
                rows_500 = [r for r in strained if r['field'] == '500']
                temps_above = sorted([float(r['temperature']) for r in rows_500 if float(r['deltaT']) >= half])
                if temps_above:
                    ctx['strained_fwhm_500'] = temps_above[-1] - temps_above[0]
                else:
                    ctx['strained_fwhm_500'] = 0.0
            high_temp_rows = [r for r in strained if float(r['temperature']) >= 900]
            neg_count = sum(1 for r in high_temp_rows if float(r['deltaT']) < 0)
            total = len(high_temp_rows)
            ctx['strained_high_neg_frac'] = neg_count / total if total > 0 else 0.0
        return ctx


# === block: score_0 (check id='step3') ===
def score_0(artifact, step, ctx):
    try:
        gold = step.get('gold', {})
        peak_dT_target = gold.get('peak_deltaT', 13.0)
        peak_dT_tol = gold.get('peak_deltaT_tol', 2.0)
        peak_dS_target = gold.get('peak_deltaS', 9.0)
        peak_dS_tol = gold.get('peak_deltaS_tol', 2.0)
        room_dT_target = gold.get('room_temp_deltaT', 7.0)
        room_dT_tol = gold.get('room_temp_deltaT_tol', 1.5)

        # sanitise column names (strip whitespace)
        sanitized = []
        for row in artifact:
            new_row = {}
            for k, v in row.items():
                new_row[k.strip()] = v
            sanitized.append(new_row)

        rows_500 = []
        for r in sanitized:
            if str(r.get('field', '')).strip() == '500':
                try:
                    dt = float(r['deltaT'])
                    ds = float(r['deltaS'])
                    temp = float(r['temperature'])
                except (ValueError, TypeError, KeyError):
                    continue
                rows_500.append((temp, dt, ds))

        if not rows_500:
            return 0.0

        computed_peak_dT = max(dt for _, dt, _ in rows_500)
        computed_peak_dS = max(ds for _, _, ds in rows_500)

        # room-temperature row (exact 300 K)
        room_rows = [(t, dt) for t, dt, ds in rows_500 if abs(t - 300.0) < 1e-6]
        room_dT = room_rows[0][1] if room_rows else None

        s1 = 1.0 if abs(computed_peak_dT - peak_dT_target) <= peak_dT_tol else 0.0
        s2 = 1.0 if abs(computed_peak_dS - peak_dS_target) <= peak_dS_tol else 0.0
        s3 = 1.0 if room_dT is not None and abs(room_dT - room_dT_target) <= room_dT_tol else 0.0

        w1, w2, w3 = 0.5, 0.3, 0.2
        return s1 * w1 + s2 * w2 + s3 * w3
    except Exception:
        return 0.0


# === block: score_1 (check id='step4') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows_500 = [r for r in artifact if r['field'] == '500']
        if not rows_500:
            return 0.0
        peak_dT = max(float(r['deltaT']) for r in rows_500)
        sf_peaks = ctx.get('stress_free_peaks', {})
        sf_peak_500 = sf_peaks.get('500', 13.0)
        s_peak = 1.0 if peak_dT <= sf_peak_500 + 0.5 else 0.0
        sf_fwhm = ctx.get('stress_free_fwhm_500', 317)
        str_fwhm = ctx.get('strained_fwhm_500', 0.0)
        s_fwhm = 1.0 if str_fwhm > sf_fwhm * 1.1 else 0.0
        high_rows = [r for r in artifact if float(r['temperature']) >= 900]
        neg_count = sum(1 for r in high_rows if float(r['deltaT']) < 0)
        total_high = len(high_rows)
        neg_frac = neg_count / total_high if total_high > 0 else 0.0
        s_neg = min(1.0, neg_frac / 0.8)
        w1, w2, w3 = 0.5, 0.3, 0.2
        return s_peak * w1 + s_fwhm * w2 + s_neg * w3


_SCORERS = {
    'step3': score_0,
    'step4': score_1,
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
