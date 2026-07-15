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


# === block: score_0 (check id='surface_energies') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # Gold values extracted from paper Figure 1 (digitised).
    # Format: (mu_Al_mu_Al_bulk_eV, surface_energy_C_J_m2, surface_energy_Al_J_m2)
    gold = [
        (-0.293, 2.89, 1.83),
        (-0.25,  2.86, 1.65),
        (-0.20,  2.81, 1.48),
        (-0.15,  2.76, 1.33),
        (-0.10,  2.71, 1.18),
        (-0.05,  2.66, 1.04),
        ( 0.0,   2.61, 0.91),
    ]

    tol_C = 0.5  # J/m^2
    tol_Al = 0.5
    mu_match_delta = 0.01  # eV

    # Parse agent rows
    agent = []
    for row in artifact:
        try:
            mu = float(row.get('mu_Al_mu_Al_bulk', None))
            sc = float(row.get('surface_energy_C', None))
            sa = float(row.get('surface_energy_Al', None))
            if mu is None or sc is None or sa is None:
                continue
            agent.append((mu, sc, sa))
        except (TypeError, ValueError):
            continue

    if not agent:
        return 0.0

    matched = 0
    for mu_a, c_a, al_a in agent:
        # nearest gold point by mu
        best = None
        best_d = float('inf')
        for g in gold:
            d = abs(mu_a - g[0])
            if d < best_d:
                best_d = d
                best = g
        if best_d <= mu_match_delta:
            c_g = best[1]
            al_g = best[2]
            if abs(c_a - c_g) <= tol_C and abs(al_a - al_g) <= tol_Al:
                matched += 1

    score = matched / len(agent)
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='work_of_adhesion') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list): return 0.0
    expected_keys = {('C','OT'):0.0, ('C','HCP'):0.0, ('Al','OT'):0.0, ('Al','HCP'):0.0}
    found = dict(expected_keys)
    for row in artifact:
        key = (row.get('termination',''), row.get('stacking',''))
        if key in found:
            try:
                found[key] = float(row.get('W_ad'))
            except Exception:
                continue
    if any(v == 0.0 for v in found.values()): return 0.0
    w_CO = found[('C','OT')]; w_CH = found[('C','HCP')]; w_AO = found[('Al','OT')]; w_AH = found[('Al','HCP')]
    # All must be positive
    if w_CO <= 0 or w_CH <= 0 or w_AO <= 0 or w_AH <= 0: return 0.0
    checks = [w_CO > w_CH, w_CO > w_AO, w_CO > w_AH]
    score = sum(checks) / 3.0
    return score if score >= 0.5 else 0.0


# === block: score_2 (check id='interfacial_energies') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0: return 0.0
    models = {}
    for row in artifact:
        term = row.get('termination','')
        stack = row.get('stacking','')
        try:
            mu = float(row.get('mu_Al_mu_Al_bulk'))
            gam = float(row.get('gamma'))
        except Exception:
            continue
        key = (term, stack)
        if key not in models:
            models[key] = {'gammas':[], 'mu':[]}
        models[key]['gammas'].append(gam)
        models[key]['mu'].append(mu)
    # 1. All gamma negative
    for key, data in models.items():
        if any(g >= 0 for g in data['gammas']):
            return 0.0
    # 2. C-terminated lower than Al-terminated at each mu
    mu_groups = {}
    for row in artifact:
        term = row.get('termination','')
        try:
            mu = float(row.get('mu_Al_mu_Al_bulk'))
            gam = float(row.get('gamma'))
        except Exception:
            continue
        if term not in ('C','Al'):
            continue
        if mu not in mu_groups:
            mu_groups[mu] = {'C':[], 'Al':[]}
        mu_groups[mu][term].append(gam)
    for mu, groups in mu_groups.items():
        if not groups['C'] or not groups['Al']:
            continue
        for c_val in groups['C']:
            for al_val in groups['Al']:
                if c_val >= al_val:
                    return 0.0
    # 3. Gamma constant across mu for each model
    for key, data in models.items():
        g = data['gammas']
        if len(g) > 1 and max(g) - min(g) > 1e-2:
            return 0.0
    return 1.0


_SCORERS = {
    'surface_energies': score_0,
    'work_of_adhesion': score_1,
    'interfacial_energies': score_2,
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
