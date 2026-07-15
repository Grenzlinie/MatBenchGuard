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
    import json, csv, os
    bulk_path = os.path.join('/app/outputs','bulk_reference.json')
    slab_path = os.path.join('/app/outputs','slab_energies.csv')
    analysis_path = os.path.join('/app/outputs','surface_energy_analysis.json')
    ctx = {}
    if os.path.isfile(bulk_path):
        with open(bulk_path) as f:
            ctx['bulk_data'] = json.load(f)
    else:
        ctx['bulk_data'] = None
    if os.path.isfile(slab_path):
        with open(slab_path, newline='') as f:
            ctx['slab_data'] = list(csv.DictReader(f))
    else:
        ctx['slab_data'] = None
    if os.path.isfile(analysis_path):
        with open(analysis_path) as f:
            ctx['analysis_data'] = json.load(f)
    else:
        ctx['analysis_data'] = None
    return ctx


# === block: score_0 (check id='bulk_reference') ===
def score_0(artifact, step, ctx):
    bulk = artifact
    if bulk is None:
        return 0.0
    target_h = 0.142
    tol_h = 0.05
    delta_h = bulk['E_bulk_Cu3Au'] - (3*bulk['E_bulk_Cu'] + bulk['E_bulk_Au'])
    if abs(delta_h - target_h) <= tol_h:
        sc_h = 1.0
    elif abs(delta_h - target_h) <= 2*tol_h:
        sc_h = 0.5
    else:
        sc_h = 0.0
    lat = bulk['lattice_constant_Cu3Au']
    lat_target = 3.79
    lat_tol = 0.05
    sc_lat = 1.0 if abs(lat - lat_target) <= lat_tol else 0.0
    return 0.5*sc_h + 0.5*sc_lat


# === block: score_1 (check id='slab_relaxation') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if rows is None or len(rows) != 19:
        return 0.0
    cols = {'composition_label','total_energy','N_Cu','N_Au','surface_area'}
    if not cols <= set(rows[0].keys()):
        return 0.0
    bulk = ctx['bulk_data']
    if bulk is None:
        return 0.0
    E_Cu = bulk['E_bulk_Cu']
    E_Au = bulk['E_bulk_Au']
    E_Cu3Au = bulk['E_bulk_Cu3Au']
    delta_h = (3*E_Cu + E_Au) - E_Cu3Au
    mu_upper = E_Cu
    mu_lower = E_Cu - delta_h/3.0
    gam_upp = {}
    gam_low = {}
    for r in rows:
        try:
            lbl = r['composition_label']
            E = float(r['total_energy'])
            nCu = int(r['N_Cu'])
            nAu = int(r['N_Au'])
            A = float(r['surface_area'])
            if A <= 0:
                return 0.0
            gu = (E - nAu*E_Cu3Au - mu_upper*(nCu - 3*nAu)) / (2.0*A)
            gl = (E - nAu*E_Cu3Au - mu_lower*(nCu - 3*nAu)) / (2.0*A)
            gam_upp[lbl] = gu
            gam_low[lbl] = gl
        except:
            return 0.0
    min_up = min(gam_upp, key=gam_upp.get)
    min_lo = min(gam_low, key=gam_low.get)
    sc = 0.0
    if min_up == '50/25':
        sc += 0.5
    if min_lo == '75/25':
        sc += 0.5
    return sc


# === block: score_2 (check id='surface_energy_analysis') ===
def score_2(artifact, step, ctx):
    analysis = artifact
    if analysis is None or not isinstance(analysis, dict):
        return 0.0
    bulk = ctx['bulk_data']
    slab = ctx['slab_data']
    if bulk is None or slab is None:
        return 0.0
    E_Cu = bulk['E_bulk_Cu']
    E_Au = bulk['E_bulk_Au']
    E_Cu3Au = bulk['E_bulk_Cu3Au']
    delta_h = E_Cu3Au - (3*E_Cu + E_Au)
    mu_upper = E_Cu
    mu_lower = E_Cu - delta_h/3.0
    gam_upp = {}
    gam_low = {}
    for r in slab:
        try:
            lbl = r['composition_label']
            E = float(r['total_energy'])
            nCu = int(r['N_Cu'])
            nAu = int(r['N_Au'])
            A = float(r['surface_area'])
            if A <= 0:
                return 0.0
            gu = (E - nAu*E_Cu3Au - mu_upper*(nCu - 3*nAu)) / (2.0*A)
            gl = (E - nAu*E_Cu3Au - mu_lower*(nCu - 3*nAu)) / (2.0*A)
            gam_upp[lbl] = gu
            gam_low[lbl] = gl
        except:
            return 0.0
    min_up = min(gam_upp, key=gam_upp.get)
    min_lo = min(gam_low, key=gam_low.get)
    sc = 0.0
    if analysis.get('stable_at_upper') == min_up and min_up == '50/25':
        sc += 0.4
    elif analysis.get('stable_at_upper') == '50/25':
        sc += 0.2
    if analysis.get('stable_at_lower') == min_lo and min_lo == '75/25':
        sc += 0.4
    elif analysis.get('stable_at_lower') == '75/25':
        sc += 0.2
    if 'mu_Cu_upper' in analysis and abs(analysis['mu_Cu_upper'] - 0.0) < 0.02:
        sc += 0.1
    if 'mu_Cu_lower' in analysis and abs(analysis['mu_Cu_lower'] - (-delta_h/3.0)) < 0.02:
        sc += 0.1
    return min(sc, 1.0)


_SCORERS = {
    'bulk_reference': score_0,
    'slab_relaxation': score_1,
    'surface_energy_analysis': score_2,
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
