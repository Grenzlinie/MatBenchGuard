import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='lattice_constant') ===
def score_0(artifact, step, ctx):
    target = step['params']['target']
    tol = step['params']['tolerance']
    val = artifact.get('lattice_constant')
    if val is None:
        return 0.0
    return 1.0 if abs(val - target) <= tol else 0.0


# === block: score_1 (check id='single_li_adsorption') ===
def score_1(artifact, step, ctx):
    params = step['params']
    gold = params['gold_table']
    tol = params['tolerance']
    # build dict from CSV rows
    site_energy = {}
    for row in artifact:
        site = row.get('site', '').strip()
        try:
            energy = float(row.get('energy_eV', None))
        except (ValueError, TypeError):
            energy = None
        if site and energy is not None:
            site_energy[site] = energy
    # numeric match
    correct = 0
    total = 0
    for site, gval in gold.items():
        total += 1
        if site in site_energy and abs(site_energy[site] - gval) <= tol:
            correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    # trend checks
    s_sites = params['s_sites']
    mo_sites = params['mo_sites']
    middle_sites = params['middle_sites']
    def get_energy(site):
        return site_energy.get(site)
    s_vals = [get_energy(s) for s in s_sites if get_energy(s) is not None]
    mo_vals = [get_energy(s) for s in mo_sites if get_energy(s) is not None]
    middle_vals = [get_energy(s) for s in middle_sites if get_energy(s) is not None]
    mo_top = get_energy('Mo-top')
    trends_passed = 0
    trends_total = 2
    # trend 1: all S energies > all Mo energies
    if s_vals and mo_vals and min(s_vals) > max(mo_vals):
        trends_passed += 1
    # trend 2: all ribbon (S+Mo+middle) energies > 2D Mo-top
    all_ribbon = s_vals + mo_vals + middle_vals
    if all_ribbon and mo_top is not None and all(v > mo_top for v in all_ribbon):
        trends_passed += 1
    trend_score = trends_passed / trends_total if trends_total > 0 else 0.0
    nw = params.get('numeric_weight', 0.8)
    tw = params.get('trend_weight', 0.2)
    return nw * numeric_score + tw * trend_score


# === block: score_2 (check id='two_li_adsorption') ===
def score_2(artifact, step, ctx):
    params = step['params']
    gold = params['gold_table']
    tol = params['tolerance']
    cfg_energy = {}
    for row in artifact:
        cfg = row.get('configuration', '').strip()
        try:
            energy = float(row.get('energy_eV', None))
        except (ValueError, TypeError):
            energy = None
        if cfg and energy is not None:
            cfg_energy[cfg] = energy
    correct = 0
    total = 0
    for cfg, gval in gold.items():
        total += 1
        if cfg in cfg_energy and abs(cfg_energy[cfg] - gval) <= tol:
            correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    s_configs = params['s_configs']
    mo_configs = params['mo_configs']
    def e(c):
        return cfg_energy.get(c)
    s_vals = [e(c) for c in s_configs if e(c) is not None]
    mo_vals = [e(c) for c in mo_configs if e(c) is not None]
    trends_passed = 0
    trends_total = 3
    # S_terminal_1-1s highest among S configs
    sym_s = e('S_terminal_1-1s')
    if sym_s is not None and s_vals and sym_s == max(s_vals):
        trends_passed += 1
    # Mo_terminal_7'-7s' highest among Mo configs
    sym_mo = e("Mo_terminal_7'-7s'")
    if sym_mo is not None and mo_vals and sym_mo == max(mo_vals):
        trends_passed += 1
    # all S configs > all Mo configs
    if s_vals and mo_vals and min(s_vals) > max(mo_vals):
        trends_passed += 1
    trend_score = trends_passed / trends_total if trends_total > 0 else 0.0
    nw = params.get('numeric_weight', 0.8)
    tw = params.get('trend_weight', 0.2)
    return nw * numeric_score + tw * trend_score


# === block: score_3 (check id='diffusion_barriers') ===
def score_3(artifact, step, ctx):
    params = step['params']
    gold = params['gold_table']
    tol = params['tolerance']
    path_energy = {}
    for row in artifact:
        path = row.get('path', '').strip()
        try:
            barrier = float(row.get('barrier_eV', None))
        except (ValueError, TypeError):
            barrier = None
        if path and barrier is not None:
            path_energy[path] = barrier
    correct = 0
    total = 0
    for p, gval in gold.items():
        total += 1
        if p in path_energy and abs(path_energy[p] - gval) <= tol:
            correct += 1
    numeric_score = correct / total if total > 0 else 0.0
    def b(p):
        return path_energy.get(p)
    s_edge = b('S_edge_T1_T2')
    mo_edge = b('Mo_edge_T1_T2')
    mid_s = b('middle_to_S_edge')
    mid_mo = b('middle_to_Mo_edge')
    trends_passed = 0
    trends_total = 3
    if s_edge is not None and mo_edge is not None and s_edge < mo_edge:
        trends_passed += 1
    if mid_s is not None and s_edge is not None and mid_s < s_edge:
        trends_passed += 1
    if mid_mo is not None and mo_edge is not None and mid_mo < mo_edge:
        trends_passed += 1
    trend_score = trends_passed / trends_total if trends_total > 0 else 0.0
    nw = params.get('numeric_weight', 0.8)
    tw = params.get('trend_weight', 0.2)
    return nw * numeric_score + tw * trend_score


_SCORERS = {
    'lattice_constant': score_0,
    'single_li_adsorption': score_1,
    'two_li_adsorption': score_2,
    'diffusion_barriers': score_3,
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
