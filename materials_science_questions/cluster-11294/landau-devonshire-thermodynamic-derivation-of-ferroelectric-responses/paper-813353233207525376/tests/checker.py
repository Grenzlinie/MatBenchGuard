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
    return {}


# === block: score_0 (check id='shape_and_content') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    req_cols = {'N','lambda','kBT_K','e_z_over_K','mean_polarization','dielectric_susceptibility','tunability_percentage'}
    first = rows[0]
    if not req_cols.issubset(first.keys()):
        return 0.0
    # Expected 4 configurations × 21 field points each = 84 rows
    if len(rows) < 84:
        return 0.0
    # Build the exact set of required (N, lambda, e_z_over_K) keys
    expected = set()
    for lam in (0.0, 0.261):
        for i in range(21):
            ez = round(i / 10.0, 1)   # 0.0, 0.1, ..., 2.0
            expected.add((5, lam, ez))
    for lam in (0.0, 0.01):
        for i in range(21):
            ez = round(i / 10.0, 1)
            expected.add((50, lam, ez))
    seen = set()
    for r in rows:
        try:
            N = int(r['N'])
            lam = float(r['lambda'])
            ez = round(float(r['e_z_over_K']), 1)
            kbt = float(r['kBT_K'])
        except:
            continue
        if kbt != 1.0:
            continue
        seen.add((N, lam, ez))
    return 1.0 if seen == expected else 0.0


# === block: score_1 (check id='tunability_consistency') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    groups = {}
    for r in rows:
        try:
            N = int(r['N'])
            lam = float(r['lambda'])
            ez = float(r['e_z_over_K'])
            chi = float(r['dielectric_susceptibility'])
            eta = float(r['tunability_percentage'])
            kbt = float(r['kBT_K'])
        except:
            return 0.0
        if kbt != 1.0:
            continue
        key = (N, lam)
        groups.setdefault(key, []).append((ez, chi, eta))
    total = 0
    ok = 0
    for key, points in groups.items():
        chi0 = None
        for ez, chi, eta in points:
            if ez == 0.0:
                chi0 = chi
                break
        if chi0 is None or chi0 == 0:
            continue
        for ez, chi, eta in points:
            expected = 100.0 * (chi0 - chi) / chi0
            if abs(expected - eta) <= 0.5:
                ok += 1
            total += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='monotonicity_and_enhancement') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    groups = {}
    for r in rows:
        try:
            N = int(r['N'])
            lam = float(r['lambda'])
            ez = float(r['e_z_over_K'])
            chi = float(r['dielectric_susceptibility'])
            eta = float(r['tunability_percentage'])
            kbt = float(r['kBT_K'])
        except:
            return 0.0
        if kbt != 1.0:
            continue
        key = (N, lam)
        groups.setdefault(key, []).append((ez, eta))
    # sort each group by ez
    for key in groups:
        groups[key].sort(key=lambda x: x[0])
    score = 0.0
    checks_total = 0
    # (a) monotonic non-decreasing
    for key, pts in groups.items():
        prev = -1
        for ez, eta in pts:
            if eta < prev - 0.1:  # small slack
                checks_total += 1
                score += 0.0
            else:
                checks_total += 1
                score += 1.0
            prev = eta
    # (b) enhancement by grading at e_z=1
    for N in (5, 50):
        if N == 5:
            lam_graded = 0.261
            lam_ungraded = 0.0
        else:
            lam_graded = 0.01
            lam_ungraded = 0.0
        eta_g = None
        eta_ug = None
        for ez, eta in groups.get((N, lam_graded), []):
            if ez == 1.0:
                eta_g = eta
                break
        for ez, eta in groups.get((N, lam_ungraded), []):
            if ez == 1.0:
                eta_ug = eta
                break
        if eta_g is not None and eta_ug is not None:
            checks_total += 1
            if eta_g > eta_ug + 0.1:
                score += 1.0
    # (c) size enhancement for lambda=0.01
    eta_N5 = None
    eta_N50 = None
    for ez, eta in groups.get((5, 0.01), []):
        if ez == 1.0:
            eta_N5 = eta
            break
    for ez, eta in groups.get((50, 0.01), []):
        if ez == 1.0:
            eta_N50 = eta
            break
    if eta_N5 is not None and eta_N50 is not None:
        checks_total += 1
        if eta_N50 > eta_N5 + 0.1:
            score += 1.0
    if checks_total == 0:
        return 1.0
    return score / checks_total


# === block: score_3 (check id='plausibility') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    total = 0
    ok = 0
    for r in rows:
        try:
            pol = float(r['mean_polarization'])
            chi = float(r['dielectric_susceptibility'])
            eta = float(r['tunability_percentage'])
            kbt = float(r['kBT_K'])
        except:
            continue
        if kbt != 1.0:
            continue
        total += 1
        if 0.0 <= pol <= 1.0 and chi >= 0 and 0.0 <= eta <= 100.0:
            ok += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'shape_and_content': score_0,
    'tunability_consistency': score_1,
    'monotonicity_and_enhancement': score_2,
    'plausibility': score_3,
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
