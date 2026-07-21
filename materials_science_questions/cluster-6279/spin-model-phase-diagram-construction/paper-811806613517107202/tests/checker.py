import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold_phase = []
    for step in spec.get('steps', []):
        if step.get('id') == 'step3_phase_diagram':
            gold_phase = step.get('gold', [])
            break
    return {'gold_phase': gold_phase}


# === block: score_0 (check id='step3_phase_diagram') ===
def score_0(artifact, step, ctx):
    gold_list = ctx.get('gold_phase', [])
    tolerance = 0.05
    if not gold_list or not isinstance(artifact, list):
        return 0.0
    total = len(gold_list)
    matches = 0
    for gold in gold_list:
        gp = float(gold['p'])
        gtype = gold['transition_type'].strip()
        gTc = float(gold['Tc'])
        found = False
        for row in artifact:
            try:
                rp = float(row['p'])
                rtype = str(row['transition_type']).strip()
                rTc = float(row['Tc'])
                if abs(rp - gp) < 1e-6 and rtype == gtype and abs(rTc - gTc) <= tolerance:
                    found = True
                    break
            except (ValueError, KeyError):
                continue
        if found:
            matches += 1
    return matches / total


# === block: score_1 (check id='step5_energy_autocorrelation') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    ts = [float(row['t']) for row in artifact if 't' in row and 'phi' in row]
    phis = [float(row['phi']) for row in artifact if 't' in row and 'phi' in row]
    if not ts or not phis:
        return 0.0
    sorted_pairs = sorted(zip(ts, phis))
    ts, phis = zip(*sorted_pairs)
    ts = list(ts)
    phis = list(phis)
    phi0_tol = step.get('phi0_tolerance', 0.05)
    min_t = step.get('min_t', 1000)
    phi_min_threshold = step.get('phi_min_threshold', 0.1)
    max_t = ts[-1]
    phi_at_min_t = None
    for i, t in enumerate(ts):
        if t >= min_t:
            phi_at_min_t = phis[i]
            break
    # Sub-checks equally weighted (0.25 each)
    sub = []
    # 1. phi(0) close to 1
    sub.append(1.0 if abs(phis[0] - 1.0) <= phi0_tol else 0.0)
    # 2. slow decay: phi(t >= min_t) > threshold
    sub.append(1.0 if max_t >= min_t and phi_at_min_t is not None and phi_at_min_t > phi_min_threshold else 0.0)
    # 3. monotonic decreasing (allow tiny noise)
    monotonic = True
    for i in range(1, len(phis)):
        if phis[i] > phis[i-1] + 0.01:
            monotonic = False
            break
    sub.append(1.0 if monotonic else 0.0)
    # 4. at least 20 data points
    sub.append(1.0 if len(ts) >= 20 else 0.0)
    return sum(sub) / len(sub)


# === block: score_2 (check id='step7_dielectric_function') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) < 5:
        return 0.0
    low_temp = step.get('low_temp', 0.1)
    epsilon_threshold_ordered_offpeak = step.get('epsilon_threshold_ordered_offpeak', 0.2)
    from collections import defaultdict
    data = defaultdict(lambda: defaultdict(list))
    for row in artifact:
        try:
            p = float(row['p'])
            T = float(row['T'])
            omega = float(row['omega'])
            eps = float(row['epsilon'])
            data[p][omega].append((T, eps))
        except (ValueError, KeyError):
            continue
    if not data:
        return 0.0
    sub = []

    # 1. Frequency dispersion at low T for p=0.5
    if 0.5 in data and data[0.5]:
        omegas = sorted(data[0.5].keys())
        if len(omegas) >= 2:
            eps_low = {}
            for omega in omegas:
                pts = sorted(data[0.5][omega], key=lambda x: abs(x[0]-low_temp))
                eps_low[omega] = pts[0][1]
            disp_ok = all(eps_low[om1] > eps_low[om2] for om1, om2 in zip(omegas[:-1], omegas[1:]))
            sub.append(1.0 if disp_ok else 0.0)
        else:
            sub.append(0.0)
    else:
        sub.append(0.0)

    # 2. Broader peak for disordered (p=0.5) compared to ordered (p=0)
    broader = False
    if 0.5 in data and 0.0 in data:
        common_omegas = set(data[0.5].keys()) & set(data[0.0].keys())
        for omega in common_omegas:
            def fwhm(pts):
                sorted_pts = sorted(pts, key=lambda x: x[0])
                if not sorted_pts:
                    return 0
                max_eps = max(p[1] for p in sorted_pts)
                if max_eps == 0:
                    return 0
                half = max_eps / 2.0
                left, right = None, None
                for T, eps in sorted_pts:
                    if eps >= half:
                        if left is None:
                            left = T
                        right = T
                return (right - left) if left is not None and right is not None else 0
            fwhm_ordered = fwhm(data[0.0][omega])
            fwhm_disordered = fwhm(data[0.5][omega])
            if fwhm_disordered > 2.0 * fwhm_ordered and fwhm_ordered > 0:
                broader = True
                break
    sub.append(1.0 if broader else 0.0)

    # 3. Ordered p=0 has sharp peak and low off-peak values
    sharp_ok = False
    if 0.0 in data and data[0.0]:
        omegas = list(data[0.0].keys())
        if omegas:
            ok = True
            for omega in omegas:
                pts = data[0.0][omega]
                max_eps = max(p[1] for p in pts)
                if max_eps < 10.0:
                    ok = False
                    break
                def val_at_temp(target):
                    nearest = min(pts, key=lambda x: abs(x[0]-target))
                    return nearest[1]
                if val_at_temp(0.5) >= epsilon_threshold_ordered_offpeak or val_at_temp(1.2) >= epsilon_threshold_ordered_offpeak:
                    ok = False
                    break
            if ok:
                sharp_ok = True
    sub.append(1.0 if sharp_ok else 0.0)

    # 4. Sufficient data rows
    sub.append(1.0 if len(artifact) >= 30 else 0.0)

    return sum(sub) / len(sub)


_SCORERS = {
    'step3_phase_diagram': score_0,
    'step5_energy_autocorrelation': score_1,
    'step7_dielectric_function': score_2,
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
