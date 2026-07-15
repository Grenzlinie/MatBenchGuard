import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
import json


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
    steps = spec.get('steps', [])
    ctx = {'steps': steps}
    # Pre-index gold data for s3 and s4
    for step in steps:
        if step.get('id') == 's3':
            gold_points = step.get('gold_points', [])
            ctx['s3_gold'] = {p['field']: (p['vpeak_AlGaAs'], p['vpeak_InP']) for p in gold_points}
            ctx['s3_tol'] = step.get('tolerance_percent', 20) / 100.0
            ctx['s3_require_mono'] = step.get('require_monotonic_increase', True)
            ctx['s3_require_inp_gt'] = step.get('require_inp_greater', True)
        elif step.get('id') == 's4':
            ctx['s4_check_freqs'] = step.get('check_frequencies_thz', [])
            gold = step.get('gold', {})
            ctx['s4_gold'] = {
                float(k): {'R_AlGaAs': v['R_AlGaAs'], 'R_InP': v['R_InP']}
                for k, v in gold.items()
            }
            ctx['s4_tol'] = step.get('tolerance_percent', 30) / 100.0
            ctx['s4_require_inp_gt'] = step.get('require_inp_greater', True)
            ctx['s4_require_decay'] = step.get('require_decay_with_freq', True)
    return ctx


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    times = []
    currents = []
    for r in rows:
        try:
            t = float(r.get('time', 0))
            c = float(r.get('current', 0))
            times.append(t)
            currents.append(c)
        except (ValueError, TypeError):
            continue
    if len(times) < 2 or len(set(times)) < 2:
        return 0.0
    # Ensure times sorted
    sorted_pairs = sorted(zip(times, currents), key=lambda x: x[0])
    times = [p[0] for p in sorted_pairs]
    currents = [p[1] for p in sorted_pairs]
    # Check all currents positive
    if any(c < 0 for c in currents):
        return 0.0
    # Find max current and its time
    max_idx = np.argmax(currents)
    peak_time = times[max_idx]
    peak_current = currents[max_idx]
    if peak_time > 0.5:
        return 0.2  # peak exists but after 0.5 ps
    # Check that there is a clear peak: after peak, values decrease
    if max_idx < len(currents) - 1 and currents[max_idx+1] >= peak_current:
        return 0.3  # not a peak
    # Reward full if peak within 0.5 ps and positive
    return 1.0


# === block: score_1 (check id='s2') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    times = []
    currents = []
    for r in rows:
        try:
            t = float(r.get('time', 0))
            c = float(r.get('current', 0))
            times.append(t)
            currents.append(c)
        except (ValueError, TypeError):
            continue
    if len(times) < 2 or len(set(times)) < 2:
        return 0.0
    sorted_pairs = sorted(zip(times, currents), key=lambda x: x[0])
    times = [p[0] for p in sorted_pairs]
    currents = [p[1] for p in sorted_pairs]
    if any(c < 0 for c in currents):
        return 0.0
    max_idx = np.argmax(currents)
    peak_time = times[max_idx]
    peak_current = currents[max_idx]
    if peak_time > 0.5:
        return 0.2
    if max_idx < len(currents) - 1 and currents[max_idx+1] >= peak_current:
        return 0.3
    return 1.0


# === block: score_2 (check id='s3') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold = ctx['s3_gold']
    tol = ctx['s3_tol']
    require_mono = ctx['s3_require_mono']
    require_inp_gt = ctx['s3_require_inp_gt']
    fields = []
    vals_gaas = []
    vals_inp = []
    for r in rows:
        try:
            f = float(r.get('field', 0))
            vgaas = float(r.get('vpeak_AlGaAs', 0))
            vip = float(r.get('vpeak_InP', 0))
            fields.append(f)
            vals_gaas.append(vgaas)
            vals_inp.append(vip)
        except (ValueError, TypeError):
            continue
    if not fields:
        return 0.0
    # Check InP > AlGaAs for every field
    score_inp_gt = 1.0
    if require_inp_gt:
        for gaas, inp in zip(vals_gaas, vals_inp):
            if inp <= gaas:
                score_inp_gt = 0.0
                break
    # Check monotonic increase for both
    score_mono = 1.0
    if require_mono:
        # check gaas
        for i in range(1, len(vals_gaas)):
            if vals_gaas[i] < vals_gaas[i-1] - 1e-3*abs(vals_gaas[i-1]):
                score_mono = 0.0
                break
        if score_mono > 0:
            for i in range(1, len(vals_inp)):
                if vals_inp[i] < vals_inp[i-1] - 1e-3*abs(vals_inp[i-1]):
                    score_mono = 0.0
                    break
    # Pointwise comparison at gold fields (interpolate)
    def interp(x, xp, fp):
        return np.interp(x, xp, fp)
    score_vals = 1.0
    if gold:
        n = 0
        sum_err = 0.0
        for f_gold, (rgaas, rinp) in sorted(gold.items()):
            if f_gold in fields:
                idx = fields.index(f_gold)
                vgaas_agent = vals_gaas[idx]
                v_inp_agent = vals_inp[idx]
            else:
                vgaas_agent = interp(f_gold, fields, vals_gaas)
                v_inp_agent = interp(f_gold, fields, vals_inp)
            err_gaas = abs(vgaas_agent - rgaas) / max(1e-6, rgaas)
            err_inp = abs(v_inp_agent - rinp) / max(1e-6, rinp)
            sum_err += err_gaas + err_inp
            n += 2
        if n > 0:
            avg_err = sum_err / n
            if avg_err <= tol:
                score_vals = 1.0
            else:
                # linear decay beyond tolerance
                score_vals = max(0.0, 1.0 - (avg_err - tol) / (2*tol))
        else:
            score_vals = 1.0
    # Combine scores: pointwise main, structural modifiers
    base = score_vals
    base = min(base, score_inp_gt)
    base = min(base, score_mono)
    return base


# === block: score_3 (check id='s4') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_freqs = ctx['s4_check_freqs']
    gold = ctx['s4_gold']
    tol = ctx['s4_tol']
    require_inp_gt = ctx.get('s4_require_inp_gt', False)
    require_decay = ctx.get('s4_require_decay', False)
    freqs = []
    r_gaas = []
    r_inp = []
    for r in rows:
        try:
            f = float(r.get('freq', 0))
            rgaas = float(r.get('R_AlGaAs', 0))
            rinp = float(r.get('R_InP', 0))
            freqs.append(f)
            r_gaas.append(rgaas)
            r_inp.append(rinp)
        except (ValueError, TypeError):
            continue
    if not freqs:
        return 0.0
    # Sort by frequency
    sorted_data = sorted(zip(freqs, r_gaas, r_inp), key=lambda x: x[0])
    freqs = [d[0] for d in sorted_data]
    r_gaas = [d[1] for d in sorted_data]
    r_inp = [d[2] for d in sorted_data]
    # Check InP > AlGaAs for every frequency
    score_inp_gt = 1.0
    if require_inp_gt:
        for gaas, inp in zip(r_gaas, r_inp):
            if inp <= gaas:
                score_inp_gt = 0.0
                break
    # Check decay with frequency: overall downward trend
    score_decay = 1.0
    if require_decay and len(freqs) > 1:
        # compute linear fit slope
        if len(freqs) >= 2:
            x = np.array(freqs)
            y_gaas = np.array(r_gaas)
            slope_gaas, _ = np.polyfit(x, y_gaas, 1)
            y_inp = np.array(r_inp)
            slope_inp, _ = np.polyfit(x, y_inp, 1)
            if slope_gaas > 1e-6 or slope_inp > 1e-6:
                score_decay = 0.0
        else:
            score_decay = 1.0
    # Pointwise comparison at check frequencies
    score_vals = 1.0
    if gold_freqs and gold:
        n = 0
        sum_err = 0.0
        for f_check in gold_freqs:
            if f_check not in gold:
                continue
            ref_gaas = gold[f_check]['R_AlGaAs']
            ref_inp = gold[f_check]['R_InP']
            # find closest frequency in agent data
            idx = (np.abs(np.array(freqs) - f_check)).argmin()
            agent_gaas = r_gaas[idx]
            agent_inp = r_inp[idx]
            err_gaas = abs(agent_gaas - ref_gaas) / max(1e-6, ref_gaas)
            err_inp = abs(agent_inp - ref_inp) / max(1e-6, ref_inp)
            sum_err += err_gaas + err_inp
            n += 2
        if n > 0:
            avg_err = sum_err / n
            if avg_err <= tol:
                score_vals = 1.0
            else:
                score_vals = max(0.0, 1.0 - (avg_err - tol) / (2*tol))
        else:
            score_vals = 1.0
    base = score_vals
    base = min(base, score_inp_gt)
    base = min(base, score_decay)
    return base


_SCORERS = {
    's1': score_0,
    's2': score_1,
    's3': score_2,
    's4': score_3,
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
