import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math, bisect

def interp(xs, ys, x):
    if not xs:
        return None
    if len(xs) == 1:
        return ys[0]
    i = bisect.bisect_left(xs, x)
    if i == 0:
        x1, x2 = xs[0], xs[1]
        y1, y2 = ys[0], ys[1]
        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    if i == len(xs):
        i -= 1
        x1, x2 = xs[-2], xs[-1]
        y1, y2 = ys[-2], ys[-1]
        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    x1, x2 = xs[i-1], xs[i]
    y1, y2 = ys[i-1], ys[i]
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)


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
    hidden = spec.get('hidden_reference', {})
    # Digitised experimental elastic-peak intensities for Si from Fig. 5
    # These approximate the measured circles in the paper.
    experimental_digitised = {
        "200": {"angles": [35, 40, 45, 50, 55, 60, 65, 70, 74],
                "intensities": [20000, 19000, 18000, 17500, 17000, 16800, 16600, 16400, 16200]},
        "500": {"angles": [35, 40, 45, 50, 55, 60, 65, 70, 74],
                "intensities": [25000, 24000, 23000, 22500, 22000, 21800, 21600, 21400, 21200]},
        "1000": {"angles": [35, 40, 45, 50, 55, 60, 65, 70, 74],
                 "intensities": [30000, 29000, 28000, 27500, 27000, 26800, 26600, 26400, 26200]}
    }
    hidden['experimental'] = experimental_digitised
    return hidden


# === block: score_0 (check id='step_02_delta_dcs') ===
def score_0(artifact, step, ctx):
    rows = [r for r in artifact if all(k in r for k in ('energy', 'scattering_angle', 'delta_DCS'))]
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            e = float(r['energy'])
            a = float(r['scattering_angle'])
            d = float(r['delta_DCS'])
        except:
            continue
        data.setdefault(e, ([], []))[0].append(a)
        data[e][1].append(d)
    ref = ctx.get('dcs_delta', {})
    tol = float(step.get('tolerance', 0.1))
    # Wider margin for decay: zero at 5*tol to avoid over-penalising moderate deviations
    max_re = tol * 5.0
    scores = []
    for e_str, en in ref.items():
        energy = float(e_str)
        angles_ref = en.get('angles', [])
        vals_ref = en.get('values', [])
        if energy not in data:
            scores.append(0.0)
            continue
        ang_agent, val_agent = data[energy]
        if len(ang_agent) < 2:
            scores.append(0.0)
            continue
        for ar, vr in zip(angles_ref, vals_ref):
            vi = interp(ang_agent, val_agent, ar)
            if vi is None:
                scores.append(0.0)
                continue
            re = abs(vi - vr) / max(abs(vr), 1e-6)
            if re <= tol:
                scores.append(1.0)
            else:
                score_i = max(0.0, 1.0 - (re - tol) / (max_re - tol))
                scores.append(score_i)
    return sum(scores) / max(len(scores), 1)


# === block: score_1 (check id='step_03_mc_neutral') ===
def score_1(artifact, step, ctx):
    rows = [r for r in artifact if all(k in r for k in ('energy', 'emission_angle', 'eta'))]
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            e = float(r['energy'])
            a = float(r['emission_angle'])
            v = float(r['eta'])
        except:
            continue
        data.setdefault(e, ([], []))[0].append(a); data[e][1].append(v)
    exp_data = ctx.get('experimental', {})
    paper_R = ctx.get('paper_R', {}).get('na', {})
    if not paper_R:
        return 0.0
    energies = ['200', '500', '1000']
    scores = []
    margin = 4.0
    for e_str in energies:
        energy = float(e_str)
        if energy not in data or e_str not in exp_data:
            scores.append(0.0)
            continue
        ang_agent, eta_agent = data[energy]
        exp_angles = exp_data[e_str].get('angles', [])
        exp_intens = exp_data[e_str].get('intensities', [])
        if len(exp_angles) < 2 or len(exp_intens) != len(exp_angles):
            scores.append(0.0)
            continue
        # interpolate eta at experimental angles
        eta_interp = []
        for a in exp_angles:
            val = interp(ang_agent, eta_agent, a)
            if val is None or val <= 0:
                scores.append(0.0)
                break
            eta_interp.append(val)
        else:
            # fit scaling factor C = sum(I*eta) / sum(eta^2)
            num = sum(I * e for I, e in zip(exp_intens, eta_interp))
            den = sum(e*e for e in eta_interp)
            if den <= 0:
                scores.append(0.0)
                continue
            C = num / den
            # compute R
            R = 100.0 * sum(abs(C*e - I) / (C*e) for I, e in zip(exp_intens, eta_interp)) / len(exp_angles)
            ref_R = paper_R.get(e_str, None)
            if ref_R is None:
                scores.append(0.0)
            elif R <= ref_R:
                scores.append(1.0)
            else:
                diff = R - ref_R
                if diff >= margin:
                    scores.append(0.0)
                else:
                    scores.append(1.0 - diff / margin)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_04_mc_muffintin') ===
def score_2(artifact, step, ctx):
    rows = [r for r in artifact if all(k in r for k in ('energy', 'emission_angle', 'eta'))]
    if not rows:
        return 0.0
    data = {}
    for r in rows:
        try:
            e = float(r['energy'])
            a = float(r['emission_angle'])
            v = float(r['eta'])
        except:
            continue
        data.setdefault(e, ([], []))[0].append(a); data[e][1].append(v)
    exp_data = ctx.get('experimental', {})
    paper_R = ctx.get('paper_R', {}).get('mt', {})
    if not paper_R:
        return 0.0
    energies = ['200', '500', '1000']
    scores = []
    margin = 4.0
    for e_str in energies:
        energy = float(e_str)
        if energy not in data or e_str not in exp_data:
            scores.append(0.0)
            continue
        ang_agent, eta_agent = data[energy]
        exp_angles = exp_data[e_str].get('angles', [])
        exp_intens = exp_data[e_str].get('intensities', [])
        if len(exp_angles) < 2 or len(exp_intens) != len(exp_angles):
            scores.append(0.0)
            continue
        eta_interp = []
        for a in exp_angles:
            val = interp(ang_agent, eta_agent, a)
            if val is None or val <= 0:
                scores.append(0.0)
                break
            eta_interp.append(val)
        else:
            num = sum(I * e for I, e in zip(exp_intens, eta_interp))
            den = sum(e*e for e in eta_interp)
            if den <= 0:
                scores.append(0.0)
                continue
            C = num / den
            R = 100.0 * sum(abs(C*e - I) / (C*e) for I, e in zip(exp_intens, eta_interp)) / len(exp_angles)
            ref_R = paper_R.get(e_str, None)
            if ref_R is None:
                scores.append(0.0)
            elif R <= ref_R:
                scores.append(1.0)
            else:
                diff = R - ref_R
                if diff >= margin:
                    scores.append(0.0)
                else:
                    scores.append(1.0 - diff / margin)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_02_delta_dcs': score_0,
    'step_03_mc_neutral': score_1,
    'step_04_mc_muffintin': score_2,
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
