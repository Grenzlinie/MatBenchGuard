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
    ctx = {}
    total_path = os.path.join(outputs_dir, 'total_energies.json')
    ctx['total'] = load_artifact(total_path)
    ctx['sigma_low'] = 0.086
    ctx['sigma_high'] = 0.172
    ctx['epsilon0'] = 8.8541878128e-12
    steps = spec.get('steps', [])
    for step in steps:
        if step.get('id') == 'phase_stability':
            ctx['expected_low_state'] = step.get('expected_low_state', '1W')
            ctx['expected_high_state'] = step.get('expected_high_state', '2W')
    return ctx


# === block: score_0 (check id='total_energies_trends') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not data:
        return 0.0
    low = data.get('low_Na')
    high = data.get('high_Na')
    E_H2O = data.get('E_H2O_hartree')
    if not low or not high:
        return 0.0
    def check_trends(sys_entries):
        try:
            sorted_entries = sorted(sys_entries, key=lambda x: x['n'])
            n_vals = [e['n'] for e in sorted_entries]
            d_vals = [e['d_layer_A'] for e in sorted_entries]
            E_vals = [e['E_n_hartree'] for e in sorted_entries]
        except KeyError:
            return 0.0
        d_ok = all(d_vals[i] <= d_vals[i+1] for i in range(len(d_vals)-1))
        idx_zero = next((i for i, n in enumerate(n_vals) if n == 0), None)
        if idx_zero is None:
            return 0.0
        E0 = E_vals[idx_zero]
        E_ads_vals = []
        for i in range(len(n_vals)):
            if n_vals[i] == 0:
                continue
            eads = (E_vals[i] - E0 - n_vals[i]*E_H2O) / n_vals[i]
            E_ads_vals.append(eads)
        eads_ok = all(E_ads_vals[i] <= E_ads_vals[i+1] for i in range(len(E_ads_vals)-1))
        return (0.5 if d_ok else 0.0) + (0.5 if eads_ok else 0.0)
    score_low = check_trends(low)
    score_high = check_trends(high)
    return (score_low + score_high) / 2.0


# === block: score_1 (check id='dielectric_ordering') ===
def score_1(artifact, step, ctx):
    total = ctx.get('total')
    if not total:
        return 0.0
    def compute_epsilons(sys_data, sigma):
        eps = {}
        for e in sys_data:
            if e.get('n', 0) == 0:
                continue
            try:
                d_m = e['d_layer_A'] * 1e-10
            except KeyError:
                continue
            eps_val = sigma * d_m / ctx['epsilon0']
            eps[e['n']] = eps_val
        return eps
    low_eps = compute_epsilons(total.get('low_Na', []), ctx['sigma_low'])
    high_eps = compute_epsilons(total.get('high_Na', []), ctx['sigma_high'])
    common_n = set(low_eps.keys()) & set(high_eps.keys())
    if not common_n:
        return 0.0
    count = sum(1 for n in common_n if low_eps[n] < high_eps[n])
    return count / len(common_n)


# === block: score_2 (check id='phase_stability') ===
def score_2(artifact, step, ctx):
    expected_low = ctx.get('expected_low_state', '1W')
    expected_high = ctx.get('expected_high_state', '2W')
    low_data = artifact.get('low_Na', {})
    high_data = artifact.get('high_Na', {})
    low_state = low_data.get('stable_state')
    high_state = high_data.get('stable_state')
    state_score = 0.0
    if low_state == expected_low:
        state_score += 0.5
    if high_state == expected_high:
        state_score += 0.5
    total = ctx.get('total')
    if not total:
        return state_score
    def consistency_check(sys_entries, sys_phase):
        mini = sys_phase.get('Omega_minimizer', {})
        n_rep = mini.get('n')
        omega_rep = mini.get('Omega')
        if n_rep is None or omega_rep is None:
            return 0.0
        n_to_E = {e['n']: e['E_n_hartree'] for e in sys_entries}
        if n_rep not in n_to_E or 0 not in n_to_E:
            return 0.0
        E_rep = n_to_E[n_rep]
        mu = (E_rep - omega_rep) / n_rep
        min_omega = float('inf')
        best_n = None
        for n, E in n_to_E.items():
            Omega = E - n * mu
            if Omega < min_omega:
                min_omega = Omega
                best_n = n
        return 1.0 if best_n == n_rep else 0.0
    cons_low = consistency_check(total.get('low_Na', []), low_data)
    cons_high = consistency_check(total.get('high_Na', []), high_data)
    cons_score = (cons_low + cons_high) / 2.0
    return 0.5 * state_score + 0.5 * cons_score


_SCORERS = {
    'total_energies_trends': score_0,
    'dielectric_ordering': score_1,
    'phase_stability': score_2,
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
