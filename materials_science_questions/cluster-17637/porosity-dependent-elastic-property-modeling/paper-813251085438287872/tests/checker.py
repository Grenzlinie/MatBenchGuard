import os
import json
import csv

# === author imports / helpers ===
import math


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
    import math
    v0 = 0.33
    gamma = 0.7
    kappa = 1.0/(2.0*(1.0-v0))
    g2 = gamma*gamma
    if gamma > 1:
        s = math.sqrt(g2 - 1.0)
        g_val = (g2)/s * math.atan(s)
    elif gamma < 1:
        s = math.sqrt(1.0 - g2)
        g_val = (g2)/(2.0*s) * math.log((1.0 + s)/(1.0 - s))
    else:
        g_val = 1.0
    f0 = (1.0 - g_val) / (2.0*(1.0 - g2))
    f1 = ((2.0+g2)*g_val - 3.0*g2) / (4.0*(1.0-g2)*(1.0-g2))
    denom_h = 2.0*(4.0*kappa-1.0) * (2.0*kappa*(f0-f1) - (4.0*kappa-1.0)*f0*f0)
    h1 = kappa*(f0-f1) / denom_h
    h2 = 1.0 / (2.0*(1.0 - (2.0-kappa)*f0 - kappa*f1))
    h3 = h4 = -(2.0*kappa*f0 - f0 + 2.0*kappa*f1) / (4.0*(4.0*kappa-1.0)*(2.0*kappa*(f0-f1) - (4.0*kappa-1.0)*f0*f0))
    h5 = 4.0 / (4.0*(f0 + 4.0*kappa*f1))
    h6 = (4.0*kappa - 1.0 - 6.0*kappa*f0 + 2.0*f0 - 2.0*kappa*f1) / (4.0*(4.0*kappa-1.0)*(2.0*kappa*(f0-f1) - (4.0*kappa-1.0)*f0*f0))
    B = (2.0*(1.0+v0)/(1.0-2.0*v0)) * (38.0*h1 - h2 + 44.0*h3 + 2.0*h5 + 8.0*h6) / 30.0
    C = (2.0*h1 + 11.0*h2 - 4.0*h3 + 8.0*h5 + 2.0*h6) / 15.0
    phiK = (2.0/3.0)*(1.0-2.0*v0)/(1.0-v0)
    phiG = (1.0/15.0)*(7.0-5.0*v0)/(1.0-v0)
    hidden_porosities = [0.05, 0.15, 0.25, 0.40, 0.60, 0.75]
    hidden_points = []
    for p in hidden_porosities:
        K_ratio = (1.0 - p*B*phiK) / (1.0 + p*B*(1.0-phiK))
        G_ratio = (1.0 - p*C*phiG) / (1.0 + p*C*(1.0-phiG))
        term1 = (1.0-2.0*v0)/3.0 * (p*B)/(1.0-p*B*phiK)
        term2 = 2.0*(1.0+v0)/3.0 * (p*C)/(1.0-p*C*phiG)
        E_norm = 1.0 / (1.0 + term1 + term2)
        hidden_points.append((p, E_norm))
    return {'hidden_points': hidden_points, 'relative_tolerance': 0.02}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    try:
        porosities = [float(r['porosity']) for r in artifact]
        e_values = [float(r['E_eff_over_E0']) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    sorted_pairs = sorted(zip(porosities, e_values), key=lambda x: x[0])
    ps = [p for p, _ in sorted_pairs]
    es = [e for _, e in sorted_pairs]
    if ps[-1] < 0.799 or ps[0] > 0.001:
        return 0.0
    hidden = ctx['hidden_points']
    passed = 0
    for hp, hgold in hidden:
        if hp <= ps[0]:
            agent_val = es[0]
        elif hp >= ps[-1]:
            agent_val = es[-1]
        else:
            i = 0
            while i < len(ps)-1 and ps[i+1] < hp:
                i += 1
            t = (hp - ps[i]) / (ps[i+1] - ps[i])
            agent_val = es[i] + t * (es[i+1] - es[i])
        rel_err = abs(agent_val - hgold) / hgold
        if rel_err <= ctx['relative_tolerance']:
            passed += 1
    score = passed / len(hidden)
    return score


_SCORERS = {
    'step_01': score_0,
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
