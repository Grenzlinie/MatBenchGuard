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
    return {'d_ab': spec.get('constants', {}).get('d_alpha_beta', 0.4714045)}


# === block: score_0 (check id='spacing_curve') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 8:
        return 0.0
    spacings = []
    velocities = []
    for row in artifact:
        try:
            s = float(row['spacing'])
            v = float(row['velocity'])
        except (ValueError, KeyError):
            continue
        spacings.append(s)
        velocities.append(v)
    n = len(spacings)
    if n < 8:
        return 0.0
    pairs = sorted(zip(spacings, velocities), key=lambda x: x[0])
    spacings, velocities = zip(*pairs)
    max_idx = max(range(n), key=lambda i: velocities[i])
    max_vel = velocities[max_idx]
    right_monotonic = True
    for i in range(max_idx+1, n):
        if velocities[i] > velocities[i-1]:
            right_monotonic = False
            break
    min_vel = min(velocities)
    steep_ok = (min_vel > 0) and (max_vel / min_vel >= 2.0)
    mag_ok = 1e-4 < max_vel < 1e-2
    score = 0.0
    if right_monotonic:
        score += 0.4
    if steep_ok:
        score += 0.3
    if mag_ok:
        score += 0.2
    if n >= 8:
        score += 0.1
    return min(score, 1.0)


# === block: score_1 (check id='db_alpha_beta_curve') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 5:
        return 0.0
    Db_vals = []
    velocities = []
    for row in artifact:
        try:
            db = float(row['D_b_alpha_beta'])
            v = float(row['velocity'])
        except (ValueError, KeyError):
            continue
        Db_vals.append(db)
        velocities.append(v)
    n = len(Db_vals)
    if n < 5:
        return 0.0
    pairs = sorted(zip(Db_vals, velocities), key=lambda x: x[0])
    Db_vals, vels = zip(*pairs)
    monotonic_dec = True
    for i in range(1, n):
        if vels[i] > vels[i-1]:
            monotonic_dec = False
            break
    steep_ok = (vels[0] > 0 and vels[-1] > 0 and vels[0] / vels[-1] >= 5.0)
    mag_ok = 1e-4 < vels[0] < 1e-2
    score = 0.0
    if monotonic_dec:
        score += 0.5
    if steep_ok:
        score += 0.3
    if mag_ok:
        score += 0.2
    return min(score, 1.0)


# === block: score_2 (check id='interface_profile') ===
def score_2(artifact, step, ctx):
    d_ab = ctx.get('d_ab', 0.4714045)
    if not isinstance(artifact, list) or len(artifact) < 10:
        return 0.0
    mus = []
    p_betas = []
    kappas = []
    for row in artifact:
        try:
            p = float(row['p_beta'])
            mu = float(row['mu'])
            kap = float(row['kappa'])
        except (ValueError, KeyError):
            continue
        p_betas.append(p)
        mus.append(mu)
        kappas.append(kap)
    interface_mus = []
    interface_mu_GT = []
    for p, mu, kap in zip(p_betas, mus, kappas):
        if 0.3 <= p <= 0.7:
            interface_mus.append(mu)
            interface_mu_GT.append(d_ab * kap)
    if not interface_mus:
        return 0.0
    min_mu = min(interface_mus)
    min_mu_GT = min(interface_mu_GT)
    if min_mu < min_mu_GT - 1e-6:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'spacing_curve': score_0,
    'db_alpha_beta_curve': score_1,
    'interface_profile': score_2,
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
