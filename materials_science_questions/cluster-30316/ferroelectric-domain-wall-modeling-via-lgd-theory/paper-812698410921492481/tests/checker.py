import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='check_energies') ===
def score_0(artifact, step, ctx):
        fields = step.get('fields_config', {}).get('fields', [])
        n = len(fields)
        if n == 0:
            return 0.0
        passing = 0
        for fdef in fields:
            name = fdef['name']
            if name not in artifact:
                continue
            value = float(artifact[name])
            kind = fdef.get('kind', 'analytic')
            if kind == 'analytic':
                # ----- analytic recompute -----
                if name == 'p4_continuum_wall_energy':
                    alpha, beta, kappa = -1.0, 1.0, 0.5
                    exp_val = 2.0/(3.0*beta) * math.sqrt(-2.0*kappa*alpha**3)
                elif name == 'p4_activation_energy':
                    alpha, beta, kappa, a = -1.0, 1.0, 0.5, 1.0
                    p_s = math.sqrt(-alpha/beta)
                    K = math.sqrt(-alpha/(2.0*kappa))
                    lam = 2.0*math.pi/(K*a)
                    term = (math.pi/3.0)*(lam**3 + 4.0*lam)/(1.0 - math.exp(-lam*math.pi)) * math.exp(-lam*math.pi/2.0)
                    exp_val = 4.0*kappa*K*p_s**2 * term
                elif name in ('p6_thick_continuum_wall_energy','p6_thin_continuum_wall_energy'):
                    alpha, beta, gamma = -1.0, -1.0, 1.0
                    p_s2 = (1.0 + math.sqrt(5.0))/2.0
                    p_s6 = math.sqrt(p_s2)
                    b = (2.0*gamma*p_s2) / (3.0*beta + 4.0*gamma*p_s2)
                    kappa = 4.0 if name == 'p6_thick_continuum_wall_energy' else 0.5
                    K = math.sqrt((beta + 2.0*gamma*p_s2)/(2.0*kappa)) * p_s6
                    term1 = 2.0*b - 1.0
                    term2 = (4.0*b + 1.0)/math.sqrt(b*(b+1.0)) * math.log(math.sqrt(1.0+b) - math.sqrt(b))
                    exp_val = (kappa * K * p_s2) / (4.0*b) * (term1 - term2)
                elif name in ('p6_thick_activation_energy','p6_thin_activation_energy'):
                    alpha, beta, gamma, a = -1.0, -1.0, 1.0, 1.0
                    p_s2 = (1.0 + math.sqrt(5.0))/2.0
                    p_s6 = math.sqrt(p_s2)
                    b = (2.0*gamma*p_s2) / (3.0*beta + 4.0*gamma*p_s2)
                    kappa = 4.0 if name == 'p6_thick_activation_energy' else 0.5
                    K = math.sqrt((beta + 2.0*gamma*p_s2)/(2.0*kappa)) * p_s6
                    lam = 2.0*math.pi/(K*a)
                    xp = math.asinh(math.sqrt(b))
                    prefactor = 4.0 * kappa * K * p_s6**2 * math.exp(-math.pi**2/(K*a))
                    coeff = -math.pi/(4.0*b)
                    inside = ( (1.0-2.0*b) * lam * math.cos(xp*lam)
                             - ((1.0+4.0*b + lam**2 * b * (1.0+b))/math.sqrt(b*(1.0+b))) * math.sin(xp*lam) )
                    exp_val = prefactor * coeff * inside
                else:
                    continue
                tol_rel = 1e-12
                tol_abs = 1e-12
                if abs(value - exp_val) <= max(tol_abs, tol_rel * abs(exp_val)):
                    passing += 1
            elif kind == 'reference':
                gold = float(fdef['gold'])
                tol_rel = float(fdef.get('tol_rel', 0.001))
                tol_abs = float(fdef.get('tol_abs', 1e-8))
                if abs(value - gold) <= max(tol_abs, tol_rel * abs(gold)):
                    passing += 1
        return passing / n


_SCORERS = {
    'check_energies': score_0,
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
