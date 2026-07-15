import os
import json
import csv

# === author imports / helpers ===
import itertools


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


# === block: score_0 (check id='energy_mass_ratios') ===
def score_0(artifact, step, ctx):
    rows = artifact
    # group by (temperature, dividing_surface)
    grouped = {}
    for r in rows:
        try:
            ts = (float(r['temperature']), r['dividing_surface'])
            R = int(r['R'])
            er = float(r['E_ratio'])
            mr = float(r['m_ratio'])
            if ts not in grouped:
                grouped[ts] = []
            grouped[ts].append((R, er, mr))
        except:
            continue

    valid_groups = []
    for (tau, surf), pts in grouped.items():
        if surf == 'tension':
            continue   # paper's 0.3 % claim applies to non-tension surfaces
        if not pts:
            continue
        # separate vectors
        rs = [p[0] for p in pts]
        ers = [p[1] for p in pts]
        mrs = [p[2] for p in pts]

        # 1. band
        band_ok = (all(0.997 <= e <= 1.003 for e in ers) and
                   all(0.997 <= m <= 1.003 for m in mrs))
        # 2. variation (non‑constant)
        er_range = max(ers) - min(ers)
        mr_range = max(mrs) - min(mrs)
        var_ok = (er_range > 0.001) and (mr_range > 0.001)
        # 3. peak existence, location and small‑R coincidence
        max_e, r_max_e = max(zip(ers, rs), key=lambda x: x[0])
        max_m, r_max_m = max(zip(mrs, rs), key=lambda x: x[0])
        peak_ok = False
        if 1 in rs:
            idx1 = rs.index(1)
            e1 = ers[idx1]
            m1 = mrs[idx1]
            pitch_ok = (r_max_e >= 2 and r_max_e <= 8 and max_e > e1 and
                        r_max_m >= 2 and r_max_m <= 8 and max_m > m1 and
                        0.999 <= e1 <= 1.001 and 0.999 <= m1 <= 1.001)
        else:
            # no R=1 data; fall back to only location
            pitch_ok = (r_max_e >= 2 and r_max_e <= 8 and
                        r_max_m >= 2 and r_max_m <= 8)

        group_score = (band_ok + var_ok + pitch_ok) / 3.0
        valid_groups.append(group_score)

    if not valid_groups:
        score = 0.0
    else:
        score = sum(valid_groups) / len(valid_groups)

    return score


# === block: score_1 (check id='local_property_ratios') ===
def score_1(artifact, step, ctx):
    rows = artifact
    grouped = {}
    for r in rows:
        try:
            ts = (float(r['temperature']), r['dividing_surface'])
            R = int(r['R'])
            tr = float(r['theta_ratio'])
            pr = float(r['pi_ratio'])
            dm = float(r['delta_mu'])
            sr = float(r['sigma_ratio'])
            if ts not in grouped:
                grouped[ts] = []
            grouped[ts].append((R, tr, pr, sr, dm))
        except:
            continue

    # surface combination check
    surf_ok = True
    present_taus = set(tau for tau,_ in grouped)
    if 0.55 in present_taus:
        # must not have tension
        if any(tau == 0.55 and surf == 'tension' for tau,surf in grouped):
            surf_ok = False
    if 0.89 in present_taus:
        # must have tension
        if not any(tau == 0.89 and surf == 'tension' for tau,surf in grouped):
            surf_ok = False

    peak_ok = True
    smallR_ok = True
    for (tau, surf), pts in grouped.items():
        # theta_ratio peak
        theta_vals = [(tr, R) for R, tr, _, _, _ in pts]
        max_tr, max_R_theta = max(theta_vals, key=lambda x: x[0])
        if not (3 <= max_R_theta <= 12):
            peak_ok = False
        # pi_ratio peak
        pi_vals = [(pr, R) for R, _, pr, _, _ in pts]
        max_pr, max_R_pi = max(pi_vals, key=lambda x: x[0])
        if not (3 <= max_R_pi <= 12):
            peak_ok = False
        # sigma_ratio peak (optional, but any peak should be in [3,12])
        sigma_vals = [(sr, R) for R, _, _, sr, _ in pts]
        max_sr, max_R_sigma = max(sigma_vals, key=lambda x: x[0])
        if not (3 <= max_R_sigma <= 12):
            peak_ok = False

        # R=1
        r1 = [pt for pt in pts if pt[0] == 1]
        if r1:
            _, tr1, pr1, _, _ = r1[0]
            if not (0.99 <= tr1 <= 1.01) or not (0.99 <= pr1 <= 1.01):
                smallR_ok = False

    score = 0.0
    if surf_ok:
        score += 0.2
    if peak_ok:
        score += 0.4
    if smallR_ok:
        score += 0.4
    return score


_SCORERS = {
    'energy_mass_ratios': score_0,
    'local_property_ratios': score_1,
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
