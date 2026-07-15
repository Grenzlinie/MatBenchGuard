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
    import csv, json, os
    outputs_dir = os.path.join(os.sep, 'app', 'outputs')

    mobility_data = []
    mobility_path = os.path.join(outputs_dir, 'mobility_vs_density.csv')
    if os.path.exists(mobility_path):
        with open(mobility_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['density'] = float(row['density'])
                    row['epsilon_top'] = float(row['epsilon_top'])
                    row['mobility'] = float(row['mobility'])
                    mobility_data.append(row)
                except (ValueError, TypeError):
                    continue

    seebeck_data = []
    seebeck_path = os.path.join(outputs_dir, 'seebeck_vs_EF.csv')
    if os.path.exists(seebeck_path):
        with open(seebeck_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['Fermi_energy'] = float(row['Fermi_energy'])
                    row['epsilon_top'] = float(row['epsilon_top'])
                    row['Seebeck'] = float(row['Seebeck'])
                    seebeck_data.append(row)
                except (ValueError, TypeError):
                    continue

    scaling_summary = {}
    scaling_path = os.path.join(outputs_dir, 'scaling_summary.json')
    if os.path.exists(scaling_path):
        with open(scaling_path) as f:
            try:
                scaling_summary = json.load(f)
            except (json.JSONDecodeError,):
                scaling_summary = {}

    return {"mobility_data": mobility_data, "seebeck_data": seebeck_data, "scaling_summary": scaling_summary}


# === block: score_0 (check id='mobility_vs_density') ===
def score_0(artifact, step, ctx):
    gold = step.get('paper_gold', {})
    if not gold:
        return 0.0

    density_ref = gold['density_ref']
    expected = gold['expected_mobility']
    rel_tol = gold['rel_tol']

    # Group data by epsilon_top
    groups = {}
    for row in artifact:
        eps = row['epsilon_top']
        groups.setdefault(eps, []).append((row['density'], row['mobility']))

    score = 0.0
    for eps_str, exp_mu in expected.items():
        eps_key = float(eps_str)
        pts_list = groups.get(eps_key, groups.get(str(eps_key), []))
        if not pts_list:
            continue  # missing condition contributes 0
        pts = sorted(pts_list, key=lambda x: x[0])
        # Interpolate/extrapolate to density_ref
        if pts[0][0] >= density_ref:
            interp_mu = pts[0][1]
        elif pts[-1][0] <= density_ref:
            interp_mu = pts[-1][1]
        else:
            interp_mu = None
            for i in range(len(pts)-1):
                if pts[i][0] <= density_ref <= pts[i+1][0]:
                    n1, mu1 = pts[i]
                    n2, mu2 = pts[i+1]
                    t = (density_ref - n1) / (n2 - n1)
                    interp_mu = mu1 + t * (mu2 - mu1)
                    break
            if interp_mu is None:
                interp_mu = (pts[0][1] + pts[-1][1]) / 2.0
        if interp_mu <= 0:
            score_i = 0.0
        else:
            # Directional error: higher mobility is better; meeting or beating
            # expected mobility yields full credit (error <= 0).
            e = max(0.0, (exp_mu - interp_mu) / exp_mu)
            if e <= rel_tol:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (e - rel_tol) / (0.5 - rel_tol))
        score += score_i
    score /= len(expected)
    return score


# === block: score_1 (check id='seebeck_vs_EF') ===
def score_1(artifact, step, ctx):
    gold = step.get('paper_gold', {})
    if not gold:
        return 0.0

    expected_max = gold['expected_max_seebeck']
    rel_tol = gold['rel_tol']

    # Group by epsilon_top, collecting absolute Seebeck values
    groups = {}
    for row in artifact:
        eps = row['epsilon_top']
        groups.setdefault(eps, []).append(abs(row['Seebeck']))

    score = 0.0
    for eps_str, exp_smax in expected_max.items():
        eps_key = float(eps_str)
        vals = groups.get(eps_key, groups.get(str(eps_key), []))
        if not vals:
            score_i = 0.0
        else:
            smax_agent = max(vals)
            e = abs(smax_agent - exp_smax) / exp_smax
            if e <= rel_tol:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (e - rel_tol) / (0.5 - rel_tol))
        score += score_i
    score /= len(expected_max)
    return score


# === block: score_2 (check id='scaling_summary') ===
def score_2(artifact, step, ctx):
    gold = step.get('paper_gold', {})
    if not gold:
        return 0.0

    exp_W = gold['expected_W_values']
    low = gold['exponent_tol_low']
    high = gold['exponent_tol_high']

    # W_values check: must equal expected list
    if not isinstance(artifact.get('W_values'), list) or len(artifact['W_values']) != len(exp_W):
        return 0.0
    for i, w in enumerate(exp_W):
        if abs(artifact['W_values'][i] - w) > 1e-6:
            return 0.0

    exponent = artifact.get('scaling_exponent')
    if exponent is None or not isinstance(exponent, (int, float)):
        return 0.0
    exp_score = 1.0 if (low <= exponent <= high) else 0.0

    # Cross-check mobility_at_1e12 with mobility CSV
    cross_score = 0.0
    mob_csv = ctx.get('mobility_data', [])
    if mob_csv:
        density_ref = 1e12
        eps_order = [1.0, 5.9, 20.6]  # same order as W_values
        computed_mus = []
        for eps in eps_order:
            pts = [(r['density'], r['mobility']) for r in mob_csv if abs(r['epsilon_top'] - eps) < 1e-3]
            if not pts:
                computed_mus.append(None)
                continue
            pts.sort(key=lambda x: x[0])
            if pts[0][0] >= density_ref:
                interp = pts[0][1]
            elif pts[-1][0] <= density_ref:
                interp = pts[-1][1]
            else:
                interp = None
                for i in range(len(pts)-1):
                    if pts[i][0] <= density_ref <= pts[i+1][0]:
                        n1, mu1 = pts[i]
                        n2, mu2 = pts[i+1]
                        t = (density_ref - n1) / (n2 - n1)
                        interp = mu1 + t * (mu2 - mu1)
                        break
                if interp is None:
                    interp = (pts[0][1] + pts[-1][1]) / 2.0
            computed_mus.append(interp)
        agent_mus = artifact.get('mobility_at_1e12')
        if isinstance(agent_mus, list) and len(agent_mus) == len(computed_mus):
            all_close = True
            for i in range(len(agent_mus)):
                if computed_mus[i] is not None and computed_mus[i] > 0:
                    if abs(agent_mus[i] - computed_mus[i]) / computed_mus[i] > 0.01:
                        all_close = False
                        break
            if all_close:
                cross_score = 1.0

    # Combine: exponent dominates (0.9), cross-check (0.1)
    return 0.9 * exp_score + 0.1 * cross_score


_SCORERS = {
    'mobility_vs_density': score_0,
    'seebeck_vs_EF': score_1,
    'scaling_summary': score_2,
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
