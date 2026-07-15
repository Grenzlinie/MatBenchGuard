import os
import json
import csv

# === author imports / helpers ===
import math

def compute_density(compound, a, b, c):
    Na = 6.02214076e23
    M_V = 50.9415
    M_Si = 28.0855
    if compound == 'V3Si':
        Z = 2
        mass = Z * (3*M_V + M_Si)
        vol_A3 = a**3
    elif compound == 'VSi2':
        Z = 3
        mass = Z * (M_V + 2*M_Si)
        # Correct hexagonal volume for a=b, γ=120°
        vol_A3 = (math.sqrt(3)/2) * (a**2) * c
    elif compound == 'V5Si3':
        Z = 4
        mass = Z * (5*M_V + 3*M_Si)
        vol_A3 = (a**2) * c
    elif compound == 'V6Si5':
        Z = 3  # paper's B, G, Vp, Vs imply ρ ≈ 3502 kg m⁻³; Z=3 matches that density
        mass = Z * (6*M_V + 5*M_Si)
        vol_A3 = a * b * c
    else:
        return None
    density_kgm3 = (mass * 1e-3) / (Na * vol_A3 * 1e-30)
    return density_kgm3


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
    import os
    output_dir = '/app/outputs'
    struc_path = os.path.join(output_dir, 'structural_properties.csv')
    if not os.path.exists(struc_path):
        return {'densities': {}}
    import csv
    with open(struc_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    densities = {}
    for row in rows:
        comp = row.get('compound', '').strip()
        if not comp:
            continue
        try:
            a = float(row['a(Å)'])
        except (ValueError, KeyError):
            continue
        b_str = row.get('b(Å)', '').strip()
        b = float(b_str) if b_str else None
        c_str = row.get('c(Å)', '').strip()
        c = float(c_str) if c_str else None
        if comp in ('V3Si', 'V5Si3'):
            if c is None:
                c = a  # fallback, not used
        else:
            if b is None or c is None:
                continue
        dens = compute_density(comp, a, b, c)
        if dens is not None:
            densities[comp] = dens
    return {'densities': densities}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    compounds = ['V3Si', 'VSi2', 'V5Si3', 'V6Si5']
    artifact_by_comp = {row['compound'].strip(): row for row in artifact}
    scores = []
    for comp in compounds:
        g = gold.get(comp)
        if g is None:
            continue
        row = artifact_by_comp.get(comp)
        if row is None:
            scores.append(0.0)
            continue
        checks = 0
        passed = 0
        for field, tol in tols.items():
            gold_val = g.get(field)
            if gold_val is None:
                continue
            try:
                val_str = row.get(field, '').strip()
                if val_str == '':
                    # missing cell; treat as 0? but gold may expect empty
                    if comp == 'V3Si' and field == 'b(Å)':
                        # allow missing b
                        passed += 1
                    else:
                        pass  # don't count
                else:
                    val = float(val_str)
                    if abs(val - gold_val) <= tol:
                        passed += 1
            except (ValueError, KeyError):
                pass
            checks += 1
        if checks > 0:
            scores.append(passed / checks)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step2a') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_Cij', {})
    rel_tol = step.get('base_tolerance', 0.10)
    compounds = ['V3Si', 'VSi2', 'V5Si3', 'V6Si5']
    artifact_by_comp = {row['compound'].strip(): row for row in artifact}
    scores = []
    for comp in compounds:
        g = gold.get(comp)
        if g is None:
            continue
        row = artifact_by_comp.get(comp)
        if row is None:
            scores.append(0.0)
            continue
        checks = 0
        passed = 0
        for field, gold_val in g.items():
            try:
                val_str = row.get(field, '').strip()
                if val_str == '':
                    continue
                val = float(val_str)
                if abs(gold_val) < 1e-6:
                    # avoid division by zero; use absolute tolerance 1e-3
                    if abs(val - gold_val) < 1e-3:
                        passed += 1
                else:
                    if abs(val - gold_val) <= rel_tol * abs(gold_val):
                        passed += 1
                checks += 1
            except (ValueError, KeyError):
                pass
        if checks > 0:
            scores.append(passed / checks)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step2b') ===
def score_2(artifact, step, ctx):
    densities = ctx.get('densities', {})
    tols = step.get('tolerances', {})
    sigma_tol = tols.get('sigma_abs', 0.01)
    e_rel_tol = tols.get('E_relative', 0.05)
    vel_rel_tol = tols.get('velocity_relative', 0.05)
    compounds = ['V3Si', 'VSi2', 'V5Si3', 'V6Si5']
    artifact_by_comp = {row['compound'].strip(): row for row in artifact}
    scores = []
    for comp in compounds:
        row = artifact_by_comp.get(comp)
        if row is None:
            scores.append(0.0)
            continue
        try:
            B = float(row['B(GPa)'])
            G = float(row['G(GPa)'])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        rho = densities.get(comp)
        if rho is None:
            scores.append(0.0)
            continue
        # compute expected derived properties
        # sigma
        denom = 2.0*(3.0*B + G)
        if denom == 0:
            scores.append(0.0)
            continue
        exp_sigma = (3.0*B - 2.0*G) / denom
        exp_E = 9.0*B*G / (3.0*B + G) if (3.0*B + G) != 0 else 0.0
        # velocities: B and G in GPa, need to convert to Pa: 1 GPa = 1e9 Pa
        B_Pa = B * 1e9
        G_Pa = G * 1e9
        exp_Vp = math.sqrt((B_Pa + 4.0*G_Pa/3.0) / rho)
        exp_Vs = math.sqrt(G_Pa / rho)
        exp_Vm = ( (2.0/(exp_Vs**3) + 1.0/(exp_Vp**3)) / 3.0 ) ** (-1.0/3.0)
        # get agent's reported
        try:
            rep_sigma = float(row['sigma'])
            rep_E = float(row['E(GPa)'])
            rep_Vp = float(row['Vp(m/s)'])
            rep_Vs = float(row['Vs(m/s)'])
            rep_Vm = float(row['Vm(m/s)'])
        except (KeyError, ValueError):
            scores.append(0.0)
            continue
        # check each
        ok = 0
        if abs(rep_sigma - exp_sigma) <= sigma_tol:
            ok += 1
        if abs(exp_E) > 1e-6 and abs(rep_E - exp_E) <= e_rel_tol * abs(exp_E):
            ok += 1
        else:
            # if exp_E is tiny, use absolute
            if abs(rep_E - exp_E) <= e_rel_tol * max(abs(exp_E), 1e-6):
                ok += 1
        if abs(exp_Vp) > 1e-6 and abs(rep_Vp - exp_Vp) <= vel_rel_tol * abs(exp_Vp):
            ok += 1
        if abs(exp_Vs) > 1e-6 and abs(rep_Vs - exp_Vs) <= vel_rel_tol * abs(exp_Vs):
            ok += 1
        if abs(exp_Vm) > 1e-6 and abs(rep_Vm - exp_Vm) <= vel_rel_tol * abs(exp_Vm):
            ok += 1
        scores.append(ok / 5.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='step3') ===
def score_3(artifact, step, ctx):
    gold = step.get('gold', {})
    rel_tol = step.get('base_tolerance', 0.10)
    compounds = ['V3Si', 'VSi2', 'V5Si3', 'V6Si5']
    artifact_by_comp = {row['compound'].strip(): row for row in artifact}
    scores = []
    for comp in compounds:
        g = gold.get(comp)
        if g is None:
            continue
        row = artifact_by_comp.get(comp)
        if row is None:
            scores.append(0.0)
            continue
        checks = 0
        passed = 0
        for field, gold_val in g.items():
            try:
                val_str = row.get(field, '').strip()
                if val_str == '':
                    continue
                val = float(val_str)
                if abs(gold_val) < 1e-6:
                    if abs(val - gold_val) < 1e-3:
                        passed += 1
                else:
                    if abs(val - gold_val) <= rel_tol * abs(gold_val):
                        passed += 1
                checks += 1
            except (ValueError, KeyError):
                pass
        if checks > 0:
            scores.append(passed / checks)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step1': score_0,
    'step2a': score_1,
    'step2b': score_2,
    'step3': score_3,
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
