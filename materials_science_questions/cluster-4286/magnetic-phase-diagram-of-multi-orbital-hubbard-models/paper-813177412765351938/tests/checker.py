import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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


# === block: score_0 (check id='step_spectral_function') ===
def score_0(artifact, step, ctx):
    import math
    pocket_cx, pocket_cy = math.pi/2, math.pi/2
    antinode_cx, antinode_cy = math.pi, 0
    radius = 0.2
    max_pocket = 0.0
    max_antinode = 0.0
    for row in artifact:
        kx, ky = float(row['kx']), float(row['ky'])
        A = float(row['A'])
        if math.hypot(kx - pocket_cx, ky - pocket_cy) < radius and A > max_pocket:
            max_pocket = A
        if math.hypot(kx - antinode_cx, ky - antinode_cy) < radius and A > max_antinode:
            max_antinode = A
    # Absolute spectral-weight requirements for a genuine hole pocket and pseudogap
    min_pocket_weight = 0.2
    max_antinode_weight = 0.15
    if max_pocket < 1e-12 or max_antinode < 1e-12:
        return 0.0
    pocket_factor = min(max_pocket / min_pocket_weight, 1.0)
    antinode_penalty = 1.0 if max_antinode <= max_antinode_weight else max(0.0, 1.0 - (max_antinode - max_antinode_weight) / 0.05)
    ratio = max_pocket / max_antinode
    ratio_thr = 2.0
    ratio_score = min(1.0, ratio / ratio_thr)
    return ratio_score * pocket_factor * antinode_penalty


# === block: score_1 (check id='step_quasiparticle_bands') ===
def score_1(artifact, step, ctx):
    import math
    pocket_x, pocket_y = math.pi/2, math.pi/2
    antinode_x, antinode_y = math.pi, 0
    best_p_dist = float('inf')
    best_a_dist = float('inf')
    omega_pocket = 0.0
    omega_antinode = 0.0
    for row in artifact:
        kx, ky = float(row['kx']), float(row['ky'])
        o1 = float(row['omega1'])
        dp = math.hypot(kx - pocket_x, ky - pocket_y)
        if dp < best_p_dist:
            best_p_dist = dp
            omega_pocket = o1
        da = math.hypot(kx - antinode_x, ky - antinode_y)
        if da < best_a_dist:
            best_a_dist = da
            omega_antinode = o1
    pocket_thr = 0.1
    s_pocket = 1.0 if abs(omega_pocket) < pocket_thr else max(0.0, 1.0 - (abs(omega_pocket) - pocket_thr) / 0.05)
    antinode_thr = 0.05
    s_antinode = 1.0 if abs(omega_antinode) > antinode_thr else abs(omega_antinode) / antinode_thr
    return 0.5 * s_pocket + 0.5 * s_antinode


# === block: score_2 (check id='step_gap_temperature') ===
def score_2(artifact, step, ctx):
    import math
    config = step.get('config', {})
    gold = config.get('gold', {})
    delta0_gold = gold.get('delta0', 0.082)
    Tc_gold = gold.get('Tc', 0.058)
    delta0_tol_pct = gold.get('delta0_tol_pct', 15)
    Tc_tol_pct = gold.get('Tc_tol_pct', 15)
    upturn_min = gold.get('upturn_min', 0.015)
    Ts, Ds = [], []
    for row in artifact:
        Ts.append(float(row['T']))
        Ds.append(float(row['Delta']))
    if len(Ts) < 5:
        return 0.0
    data = sorted(zip(Ts, Ds))
    Ts, Ds = [d[0] for d in data], [d[1] for d in data]
    delta0 = Ds[0]
    max_D = max(Ds)
    thresh = max(0.01 * max_D, 1e-4)
    Tc = Ts[-1]
    for i, D in enumerate(Ds):
        if D < thresh:
            Tc = Ts[i]
            break
    low_T_limit = min(Tc * 0.5, 0.03)
    max_low = delta0
    for t, d in data:
        if t <= low_T_limit and d > max_low:
            max_low = d
    upturn = max_low - delta0
    s_delta0 = max(0.0, 1.0 - abs(delta0 - delta0_gold) / (delta0_gold * delta0_tol_pct / 100.0))
    s_Tc = max(0.0, 1.0 - abs(Tc - Tc_gold) / (Tc_gold * Tc_tol_pct / 100.0))
    s_upturn = 1.0 if upturn >= upturn_min else max(0.0, upturn / upturn_min)
    return 0.4 * s_delta0 + 0.4 * s_Tc + 0.2 * s_upturn


_SCORERS = {
    'step_spectral_function': score_0,
    'step_quasiparticle_bands': score_1,
    'step_gap_temperature': score_2,
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
