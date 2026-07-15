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
    return {}


# === block: score_0 (check id='main_result') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    sigma0_rows = []
    sigma06_rows = []
    sigma_large_rows = []

    for row in artifact:
        try:
            s = float(row['sigma'])
            r = float(row['r_mm'])
            z = float(row['z_mm'])
            u = float(row['u_degC'])
        except (KeyError, ValueError):
            continue
        if abs(s) < 1e-6:
            sigma0_rows.append((r, z, u))
        elif abs(s - 0.6) < 0.01:
            sigma06_rows.append((r, z, u))
        elif s > 10:
            sigma_large_rows.append((r, z, u))

    targets = step.get('target_values', {})
    alpha = step.get('alpha', 8.2e-5)
    tol_factor = 2.0
    scores = []

    def max_temp_and_dist(rows, tg):
        if not rows:
            return None, None, []
        max_temp = max(u for _, _, u in rows)
        # group by r for distortion integration
        r_dict = {}
        for r, z, u in rows:
            r_dict.setdefault(r, []).append((z, u))
        max_dist = 0.0
        for r, vals in r_dict.items():
            vals.sort(key=lambda x: x[0])
            if len(vals) < 2:
                continue
            zs, us = zip(*vals)
            integral = sum(0.5 * (us[i] + us[i+1]) * (zs[i+1] - zs[i]) for i in range(len(us)-1))
            dist = alpha * integral * 1000.0  # mm -> µm
            if dist > max_dist:
                max_dist = dist
        sc = []
        if tg.get('max_temp') is not None:
            diff = abs(max_temp - tg['max_temp'])
            tol = tg.get('max_temp_tol', 5.0)
            if diff <= tol:
                sc.append(1.0)
            else:
                sc.append(max(0.0, 1.0 - (diff - tol) / (tol * tol_factor)))
        if tg.get('max_dist') is not None:
            diff = abs(max_dist - tg['max_dist'])
            tol = tg.get('max_dist_tol', 0.05)
            if diff <= tol:
                sc.append(1.0)
            else:
                sc.append(max(0.0, 1.0 - (diff - tol) / (tol * tol_factor)))
        return max_temp, max_dist, sc

    temps = []
    dists = []
    for rows, gname in zip([sigma0_rows, sigma06_rows, sigma_large_rows], ['sigma0', 'sigma06', 'sigma_large']):
        tg = targets.get(gname, {})
        t, d, ss = max_temp_and_dist(rows, tg)
        if ss:
            scores.extend(ss)
        if t is not None and d is not None:
            temps.append(t)
            dists.append(d)

    # trend check
    trend_ok = True
    if len(temps) == 3 and len(dists) == 3:
        if not (temps[0] > temps[1] > temps[2]):
            trend_ok = False
        if not (dists[0] > dists[1] > dists[2]):
            trend_ok = False
    else:
        trend_ok = False
    scores.append(1.0 if trend_ok else 0.0)

    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'main_result': score_0,
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
