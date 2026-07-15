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
    import os, math, csv

    outputs_dir = os.path.join('/app', 'outputs')

    # Load agent's computed_parameters.csv if exists
    agent_params = None
    try:
        with open(os.path.join(outputs_dir, 'computed_parameters.csv'), 'r') as f:
            agent_params = list(csv.DictReader(f))
    except Exception:
        pass

    # Gold Debye rows
    step1 = next(s for s in spec['steps'] if s['id'] == 'compute_debye_parameters')
    gold_rows = step1['gold_rows']

    # Gold W preparation (constants and function)
    step2 = next(s for s in spec['steps'] if s['id'] == 'compute_recoilless_fractions')
    k_B = step2['params']['k_B_eV_per_K']
    materials_config = step2['params']['materials']

    def integral(y, steps=100000):
        if y <= 0:
            return 0.0
        h = y / steps
        total = 0.0
        for i in range(steps):
            x = (i + 0.5) * h
            total += x / (math.exp(x) - 1.0)
        return total * h

    def W_alpha(T, Theta, R):
        if T == 0.0:
            return math.exp(-3 * R / (2 * k_B * Theta))
        y = Theta / T
        term = 1.0 + 4.0 * (T / Theta)**2 * integral(y)
        exponent = (3 * R) / (2 * k_B * Theta) * term
        return math.exp(-exponent)

    # Compute expected recoilless fractions from gold Thetas
    gold_recoilless = {}
    for gr in gold_rows:
        mat = gr['material']
        Theta_t = float(gr['Theta_t'])
        Theta_l = float(gr['Theta_l'])
        R_eV = materials_config[mat]['R_eV']
        temps = materials_config[mat]['temps_K']
        for T in temps:
            wt = W_alpha(T, Theta_t, R_eV)
            wl = W_alpha(T, Theta_l, R_eV)
            a = wt / wl if wl != 0 else float('inf')
            gold_recoilless[(mat, T)] = {'W_t': wt, 'W_l': wl, 'A': a}

    # Build map from material -> agent Thetas
    agent_thetas = {}
    if agent_params:
        for row in agent_params:
            mat = row.get('material', '').strip()
            try:
                agent_thetas[mat] = {
                    'Theta_t': float(row['Theta_t']),
                    'Theta_l': float(row['Theta_l'])
                }
            except (ValueError, KeyError):
                pass

    return {
        'gold_rows': gold_rows,
        'agent_thetas': agent_thetas,
        'gold_recoilless': gold_recoilless,
        'W_alpha': W_alpha,
        'integral': integral,
        'k_B': k_B,
        'materials_config': materials_config
    }


# === block: score_0 (check id='compute_debye_parameters') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    # fix gold for Sb Theta (paper Table 2: 214.6 K, not 21.46)
    gold_rows = step.get('gold_rows', [])
    for r in gold_rows:
        if r.get('material', '').strip() == 'Sb':
            r['Theta'] = 214.6   # correction
    gold_map = {r['material']: r for r in gold_rows}
    fields = ['I_t', 'I_l', 'I', 'Omega_t', 'Omega_l', 'Omega', 'Theta_t', 'Theta_l', 'Theta']
    tolerance_rel = step.get('tolerance_rel', 0.005)

    total_fields = 0
    passed_fields = 0

    for row in artifact:
        mat = row.get('material', '').strip()
        gold = gold_map.get(mat)
        if not gold:
            continue
        for f in fields:
            total_fields += 1
            try:
                val = float(row[f])
                g = float(gold[f])
                if abs(g) < 1e-20:
                    if abs(val) < 1e-20:
                        passed_fields += 1
                    continue
                if abs(val - g) <= tolerance_rel * abs(g):
                    passed_fields += 1
            except (ValueError, KeyError):
                pass

    if total_fields == 0:
        return 0.0
    return passed_fields / total_fields


# === block: score_1 (check id='compute_recoilless_fractions') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0

    W_alpha = ctx.get('W_alpha')
    materials_config = ctx.get('materials_config', {})
    agent_thetas = ctx.get('agent_thetas', {})
    gold_recoilless = ctx.get('gold_recoilless', {})

    tolerance_abs = step.get('tolerance_abs', 0.02)

    # Expected temperature lists per material
    rows_passing = 0
    total_rows = 0

    for row in artifact:
        mat = row.get('material', '').strip()
        try:
            T_val = float(row['temperature'])
        except (ValueError, KeyError):
            continue
        total_rows += 1

        # Get agent Thetas
        thetas = agent_thetas.get(mat)
        if thetas is None:
            continue

        R_eV = materials_config[mat]['R_eV']

        # Compute agent W from their own Thetas
        try:
            ag_wt = W_alpha(T_val, thetas['Theta_t'], R_eV)
            ag_wl = W_alpha(T_val, thetas['Theta_l'], R_eV)
        except Exception:
            continue
        ag_A = ag_wt / ag_wl if ag_wl != 0 else float('inf')

        # Compare to gold expected
        gold = gold_recoilless.get((mat, T_val))
        if gold is None:
            continue

        # Check all three values within absolute tolerance
        cond_wt = abs(ag_wt - gold['W_t']) <= tolerance_abs
        cond_wl = abs(ag_wl - gold['W_l']) <= tolerance_abs
        cond_A = abs(ag_A - gold['A']) <= tolerance_abs
        if cond_wt and cond_wl and cond_A:
            rows_passing += 1

    if total_rows == 0:
        return 0.0
    return rows_passing / total_rows


_SCORERS = {
    'compute_debye_parameters': score_0,
    'compute_recoilless_fractions': score_1,
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
