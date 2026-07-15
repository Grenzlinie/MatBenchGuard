import os
import json
import csv

# === author imports / helpers ===
import json, math

def _compare_energies(reported, gold, tolerance):
    if isinstance(gold, list):
        total = len(gold)
        s = 0.0
        for a, g in zip(reported, gold):
            diff = abs(a - g)
            s += max(0.0, 1.0 - diff / max(tolerance, 1e-12)) / total
        return s
    elif isinstance(gold, dict):
        if any(isinstance(v, list) for v in gold.values()):
            items = list(gold.items())
            total = sum(len(v) for _, v in items)
            s = 0.0
            for trap, gvals in items:
                rvals = reported.get(trap, [])
                for a, g in zip(rvals, gvals):
                    diff = abs(a - g)
                    s += max(0.0, 1.0 - diff / max(tolerance, 1e-12)) / total
            return s
        else:
            total_points = 0
            total_score = 0.0
            for stoich, subtrap in gold.items():
                rep_stoich = reported.get(stoich, {})
                for trap, gvals in subtrap.items():
                    rvals = rep_stoich.get(trap, [])
                    for a, g in zip(rvals, gvals):
                        diff = abs(a - g)
                        total_score += max(0.0, 1.0 - diff / max(tolerance, 1e-12))
                        total_points += 1
            return total_score / total_points if total_points else 1.0
    return 0.0


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


# === block: score_0 (check id='defect_energies_check') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    rep = artifact.get('defect_energies', {})
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_1 (check id='unoccupied_trap_energies_check') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    rep = artifact.get('unoccupied_trap_energies', {})
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_2 (check id='trap_formation_energies_check') ===
def score_2(artifact, step, ctx):
    gold = step.get('gold', {})
    rep = artifact.get('trap_formation_energies', {})
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_3 (check id='solution_energies_pre_existent_check') ===
def score_3(artifact, step, ctx):
    gold = step.get('gold', {})
    rep = artifact.get('solution_energies_pre_existent', {})
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_4 (check id='solution_energies_equilibrium_check') ===
def score_4(artifact, step, ctx):
    gold = step.get('gold', {})
    rep = artifact.get('solution_energies_equilibrium', {})
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_5 (check id='migration_activation_check') ===
def score_5(artifact, step, ctx):
    gold = step.get('gold', [])
    rep = artifact.get('migration_activation_energies', [])
    tolerance = step.get('tolerance', 0.3)
    return _compare_energies(rep, gold, tolerance)


# === block: score_6 (check id='consistency_solution_pre') ===
def score_6(artifact, step, ctx):
    defect = artifact.get('defect_energies', {})
    unocc = artifact.get('unoccupied_trap_energies', {})
    reported = artifact.get('solution_energies_pre_existent', {})
    traps = ['Anion vacancy', 'Cation vacancy', 'Divacancy', 'Neutral trivacancy', 'Charged trivacancy', 'Tetravacancy']
    tol = 0.001
    total = 0.0
    count = 0
    for trap in traps:
        d = defect.get(trap, [])
        u = unocc.get(trap, [])
        r = reported.get(trap, [])
        for i in range(4):
            expected = d[i] - u[i] if i < len(d) and i < len(u) else None
            if expected is not None and i < len(r):
                diff = abs(expected - r[i])
                if diff <= tol:
                    total += 1.0
            count += 1
    return total / count if count else 0.0


# === block: score_7 (check id='consistency_trap_formation') ===
def score_7(artifact, step, ctx):
    basic = artifact.get('basic_energies', {})
    rep = artifact.get('trap_formation_energies', {})
    E_s = basic.get('schottky_trio_energy', [0]*4)
    E_f = basic.get('frenkel_pair_energy', [0]*4)
    B_dv = basic.get('binding_energy_divacancy', [0]*4)
    B_nt = basic.get('binding_energy_neutral_trivacancy', [0]*4)
    B_ct = basic.get('binding_energy_charged_trivacancy', [0]*4)
    B_tv = basic.get('binding_energy_tetravacancy', [0]*4)
    stoichs = ['anion_deficient', 'stoichiometric', 'anion_excess']
    traps = ['Anion vacancy', 'Cation vacancy', 'Divacancy', 'Neutral trivacancy', 'Charged trivacancy', 'Tetravacancy']
    tol = 0.001
    total = 0.0
    count = 0
    for stoich in stoichs:
        for trap in traps:
            rep_vals = rep.get(stoich, {}).get(trap, [])
            for i in range(4):
                if stoich == 'anion_deficient':
                    if trap == 'Anion vacancy':    expected = 0.0
                    elif trap == 'Cation vacancy': expected = E_s[i]
                    elif trap == 'Divacancy':      expected = E_s[i] - B_dv[i]
                    elif trap == 'Neutral trivacancy': expected = E_s[i] - B_nt[i]
                    elif trap == 'Charged trivacancy': expected = 2*E_s[i] - B_ct[i]
                    elif trap == 'Tetravacancy':   expected = 2*E_s[i] - B_tv[i]
                    else: expected = None
                elif stoich == 'stoichiometric':
                    if trap == 'Anion vacancy':    expected = 0.5 * E_f[i]
                    elif trap == 'Cation vacancy': expected = E_s[i] - E_f[i]
                    elif trap == 'Divacancy':      expected = E_s[i] - 0.5*E_f[i] - B_dv[i]
                    elif trap == 'Neutral trivacancy': expected = E_s[i] - B_nt[i]
                    elif trap == 'Charged trivacancy': expected = 2*E_s[i] - 1.5*E_f[i] - B_ct[i]
                    elif trap == 'Tetravacancy':   expected = 2*E_s[i] - E_f[i] - B_tv[i]
                    else: expected = None
                else:  # anion_excess
                    if trap == 'Anion vacancy':    expected = E_f[i]
                    elif trap == 'Cation vacancy': expected = E_s[i] - 2*E_f[i]
                    elif trap == 'Divacancy':      expected = E_s[i] - E_f[i] + B_dv[i]
                    elif trap == 'Neutral trivacancy': expected = E_s[i] - B_nt[i]
                    elif trap == 'Charged trivacancy': expected = 2*E_s[i] - 3*E_f[i] - B_ct[i]
                    elif trap == 'Tetravacancy':   expected = 2*E_s[i] - 2*E_f[i] - B_tv[i]
                    else: expected = None
                if expected is not None and i < len(rep_vals):
                    diff = abs(expected - rep_vals[i])
                    if diff <= tol:
                        total += 1.0
                count += 1
    return total / count if count else 0.0


# === block: score_8 (check id='neutral_trivacancy_independence') ===
def score_8(artifact, step, ctx):
    rep = artifact.get('trap_formation_energies', {})
    ad = rep.get('anion_deficient', {}).get('Neutral trivacancy', [])
    st = rep.get('stoichiometric', {}).get('Neutral trivacancy', [])
    ae = rep.get('anion_excess', {}).get('Neutral trivacancy', [])
    if len(ad) != 4 or len(st) != 4 or len(ae) != 4:
        return 0.0
    for i in range(4):
        if ad[i] != st[i] or st[i] != ae[i]:
            return 0.0
    return 1.0


_SCORERS = {
    'defect_energies_check': score_0,
    'unoccupied_trap_energies_check': score_1,
    'trap_formation_energies_check': score_2,
    'solution_energies_pre_existent_check': score_3,
    'solution_energies_equilibrium_check': score_4,
    'migration_activation_check': score_5,
    'consistency_solution_pre': score_6,
    'consistency_trap_formation': score_7,
    'neutral_trivacancy_independence': score_8,
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
