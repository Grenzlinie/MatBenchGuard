import os
import json
import csv

# === author imports / helpers ===
import json, math
def validate_entries(agent_entries, expected, tolerances, trend_fn=None):
    if not isinstance(agent_entries, list):
        return 0.0
    lookup = {}
    for e in agent_entries:
        k = (e.get('oxide',''), e.get('functional',''), e.get('property',''))
        lookup[k] = e.get('value')
    total = len(expected)
    if total == 0:
        return 1.0 if trend_fn is None else (1.0 if trend_fn(lookup) else 0.9)
    ok = 0
    for exp in expected:
        k = (exp['oxide'], exp['functional'], exp['property'])
        val = lookup.get(k)
        if val is None:
            continue
        tol = tolerances.get(exp['property'], 0.1)
        if abs(val - exp['value']) <= tol:
            ok += 1
    val_score = ok / total
    if trend_fn is None:
        return val_score
    trend_ok = trend_fn(lookup)
    return 0.9 * val_score + 0.1 * (1.0 if trend_ok else 0.0)


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


# === block: score_0 (check id='check_bulk') ===
def score_0(artifact, step, ctx):
    oxide_order = ['MgO','CaO','SrO','BaO']
    funcs = ['LDA','PBE','RPBE','PBEsol','BEEF-vdW','HSE']
    lookup = {}
    for e in artifact:
        if not isinstance(e, dict):
            continue
        k = (e.get('oxide',''), e.get('functional',''), e.get('property',''))
        lookup[k] = e.get('value')
    for f in funcs:
        a_vals = [lookup.get((ox,f,'lattice_constant_A')) for ox in oxide_order]
        if any(v is None for v in a_vals):
            return 0.0
        if not all(a_vals[i] < a_vals[i+1] for i in range(len(a_vals)-1)):
            return 0.0
        m_vals = [lookup.get((ox,f,'bulk_modulus_GPa')) for ox in oxide_order]
        if any(v is None for v in m_vals):
            return 0.0
        if not all(m_vals[i] > m_vals[i+1] for i in range(len(m_vals)-1)):
            return 0.0
        ae_vals = [lookup.get((ox,f,'atomization_energy_eV')) for ox in oxide_order]
        if any(v is None for v in ae_vals):
            return 0.0
        if not (ae_vals[1] > ae_vals[0] and ae_vals[1] > ae_vals[2] and ae_vals[1] > ae_vals[3]):
            return 0.0
    # HSE band gaps decreasing
    bg_vals = [lookup.get((ox,'HSE','band_gap_eV')) for ox in oxide_order]
    if any(v is None for v in bg_vals):
        return 0.0
    if not all(bg_vals[i] > bg_vals[i+1] for i in range(len(bg_vals)-1)):
        return 0.0
    return 1.0


# === block: score_1 (check id='check_surface_energies') ===
def score_1(artifact, step, ctx):
    expected = step.get('gold', [])
    tolerances = step.get('tolerances', {})
    def surf_trend(lookup):
        oxides = ['MgO','CaO','SrO','BaO']
        props = ['surface_energy_100_eV_per_1x1','surface_energy_110_eV_per_1x1','surface_energy_111_Moct_eV_per_1x1','surface_energy_111_Ooct_eV_per_1x1']
        funcs = ['LDA','PBE','RPBE','PBEsol','BEEF-vdW','HSE']
        for p in props:
            for f in funcs:
                vals = [lookup.get((ox,f,p)) for ox in oxides]
                if any(v is None for v in vals):
                    continue
                if not (vals[0] > vals[1] > vals[2] > vals[3]):
                    return False
        return True
    return validate_entries(artifact, expected, tolerances, surf_trend)


# === block: score_2 (check id='check_mgo100_adsorption') ===
def score_2(artifact, step, ctx):
    expected = step.get('gold', [])
    tolerances = step.get('tolerances', {})
    def mgo_trend(lookup):
        funcs = ['LDA','PBE','RPBE','PBEsol','BEEF-vdW','HSE']
        for f in funcs:
            co = lookup.get(('MgO',f,'adsorption_energy_CO_MgO100_eV'))
            no = lookup.get(('MgO',f,'adsorption_energy_NO_MgO100_eV'))
            if co is None or no is None:
                return False
            if not (no <= co):
                return False
        return True
    return validate_entries(artifact, expected, tolerances, mgo_trend)


# === block: score_3 (check id='check_co_no_mapping') ===
def score_3(artifact, step, ctx):
    expected = step.get('gold', [])
    tolerances = step.get('tolerances', {})
    def comap_trend(lookup):
        oxides = ['MgO','CaO','SrO','BaO']
        surf_props = [('100','adsorption_energy_CO_on(100)_eV','adsorption_energy_NO_on(100)_eV'),
                      ('110','adsorption_energy_CO_on(110)_eV','adsorption_energy_NO_on(110)_eV'),
                      ('111_Moct','adsorption_energy_CO_on(111)_Moct_eV','adsorption_energy_NO_on(111)_Moct_eV')]
        for sf, co_prop, no_prop in surf_props:
            co_vals = [lookup.get((ox,'BEEF-vdW',co_prop)) for ox in oxides]
            no_vals = [lookup.get((ox,'BEEF-vdW',no_prop)) for ox in oxides]
            if any(v is None for v in co_vals) or any(v is None for v in no_vals):
                return False
            # NO stronger than CO on each oxide
            for cv, nv in zip(co_vals, no_vals):
                if not (nv <= cv):
                    return False
            # CO adsorption weakens (less negative) across series
            if not (co_vals[0] <= co_vals[1] <= co_vals[2] <= co_vals[3]):
                return False
        # NO on (100) strengthens (more negative)
        no100 = [lookup.get((ox,'BEEF-vdW','adsorption_energy_NO_on(100)_eV')) for ox in oxides]
        if any(v is None for v in no100):
            return False
        if not (no100[0] >= no100[1] >= no100[2] >= no100[3]):
            return False
        return True
    return validate_entries(artifact, expected, tolerances, comap_trend)


# === block: score_4 (check id='check_oxygen_chem') ===
def score_4(artifact, step, ctx):
    expected = step.get('gold', [])
    tolerances = step.get('tolerances', {})
    def ochem_trend(lookup):
        oxides = ['MgO','CaO','SrO','BaO']
        funcs = ['LDA','PBE','RPBE','PBEsol','BEEF-vdW','HSE']
        for f in funcs:
            ads = [lookup.get((ox,f,'oxygen_adsorption_MOM_on(100)_eV')) for ox in oxides]
            vac = [lookup.get((ox,f,'oxygen_vacancy_formation_on(100)_eV')) for ox in oxides]
            if any(v is None for v in ads) or any(v is None for v in vac):
                continue
            # adsorption more exothermic (more negative) -> decreasing values
            if not (ads[0] >= ads[1] >= ads[2] >= ads[3]):
                return False
            # vacancy formation decreasing
            if not (vac[0] >= vac[1] >= vac[2] >= vac[3]):
                return False
        return True
    return validate_entries(artifact, expected, tolerances, ochem_trend)


_SCORERS = {
    'check_bulk': score_0,
    'check_surface_energies': score_1,
    'check_mgo100_adsorption': score_2,
    'check_co_no_mapping': score_3,
    'check_oxygen_chem': score_4,
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
