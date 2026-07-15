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


# === block: score_0 (check id='step_02_orbital_populations') ===
def score_0(artifact, step, ctx):
    ref = step.get('population_reference', {})
    tol_rel = step.get('tolerance_rel', 0.4)
    overlap_thresh = step.get('overlap_threshold', 0.5)

    def check_value(val, target):
        if val is None:
            return False
        return abs(val - target) <= tol_rel * max(abs(target), 1e-9)

    total_checks = 0
    passed = 0

    # gamma_Fe6
    for key in ['Fe_3d','Fe_4s','Fe_4p']:
        total_checks += 1
        val = artifact.get('gamma_Fe6_orbital_population', {}).get(key)
        if val is not None and check_value(val, ref['gamma_Fe6_orbital_population'][key]):
            passed += 1

    # gamma_prime_Fe6N
    for key in ['N_2s','N_2p','Fe_3s','Fe_3p','Fe_3d','Fe_4s','Fe_4p']:
        total_checks += 1
        val = artifact.get('gamma_prime_Fe6N_orbital_population', {}).get(key)
        if val is not None and check_value(val, ref['gamma_prime_Fe6N_orbital_population'][key]):
            passed += 1

    # N_Fe_overlap_population
    overlap_ref = ref['N_Fe_overlap_population']
    for key in ['N_Fe_3s','N_Fe_3p','N_Fe_3d','N_Fe_4s','N_Fe_4p']:
        total_checks += 1
        val = artifact.get('N_Fe_overlap_population', {}).get(key)
        if val is not None and check_value(val, overlap_ref[key]):
            passed += 1

    # total overlap check
    n_fe_total = artifact.get('N_Fe_overlap_population', {}).get('N_Fe_total')
    total_checks += 1
    if n_fe_total is not None and n_fe_total > overlap_thresh:
        passed += 1

    return passed / total_checks if total_checks else 0.0


# === block: score_1 (check id='step_03_binding_energies') ===
def score_1(artifact, step, ctx):
    alpha = step.get('alpha_phase', 'alpha-Fe')
    fe_n_order = step.get('fe_n_order', [])
    fe_c_order = step.get('fe_c_order', [])

    # convert artifact list of dicts to mapping phase -> binding_energy
    phase_map = {}
    for row in artifact:
        ph = row.get('phase', '').strip()
        if ph:
            try:
                be = float(row.get('binding_energy', None))
                phase_map[ph] = be
            except (ValueError, TypeError):
                continue

    # canonicalize phase names: map Greek and prime symbols, then clean
    import re
    def canonical(p):
        p = p.lower()
        # replace prime symbols (actual prime or apostrophe) with 'prime'
        p = p.replace('′', 'prime')
        p = p.replace("'", 'prime')
        # remove any remaining quotes
        p = re.sub(r"['\"]", '', p)
        # replace underscores with hyphens
        p = p.replace('_', '-')
        # map common Greek letter prefixes
        p = p.replace('α', 'alpha').replace('β', 'beta').replace('γ', 'gamma').replace('ε', 'epsilon')
        # collapse whitespace
        p = re.sub(r'\s+', '', p)
        return p

    # build canonical map
    can_map = {}
    for orig_ph, be in phase_map.items():
        can_map[canonical(orig_ph)] = be

    def get_be(ph):
        return can_map.get(canonical(ph))

    # --- Build list of checks ---
    checks = []
    # 1) alpha-Fe exists
    alpha_be = get_be(alpha)
    if alpha_be is None:
        return 0.0

    # 2) all nitride/carbide phases > alpha
    all_n = fe_n_order
    all_c = fe_c_order
    all_other = all_n + all_c
    for ph in all_other:
        be = get_be(ph)
        checks.append( (be is not None) and (be > alpha_be) )

    # 3) ordering within N series
    for i in range(len(all_n)-1):
        be_i = get_be(all_n[i])
        be_j = get_be(all_n[i+1])
        checks.append( (be_i is not None and be_j is not None) and (be_i < be_j) )

    # 4) ordering within C series
    for i in range(len(all_c)-1):
        be_i = get_be(all_c[i])
        be_j = get_be(all_c[i+1])
        checks.append( (be_i is not None and be_j is not None) and (be_i < be_j) )

    if not checks:
        return 0.0
    passed = sum(checks)
    return passed / len(checks)


_SCORERS = {
    'step_02_orbital_populations': score_0,
    'step_03_binding_energies': score_1,
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
