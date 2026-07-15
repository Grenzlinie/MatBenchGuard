import os
import json
import csv

# === author imports / helpers ===
import json
import os
import csv
import math


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
    def prepare(outputs_dir, spec):
        steps_by_id = {s['id']: s for s in spec['steps']}
        return {'steps_by_id': steps_by_id}


# === block: score_0 (check id='step02') ===
def score_0(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        if artifact is None:
            return 0.0

        gold = step['gold']
        tols = step['tolerances']
        data = artifact

        def safe_float(val, default=0.0):
            if val is None:
                return default
            try:
                return float(val)
            except (TypeError, ValueError):
                return default

        scores = []

        # lattice constants
        lat = data.get('lattice_constants', {})
        gold_lat = gold['lattice_constants']
        lat_ok = 0
        for k in ['a','b','c','volume']:
            lat_val = safe_float(lat.get(k))
            gold_val = gold_lat[k]
            if abs(lat_val - gold_val) <= tols['lattice_abs']:
                lat_ok += 1
        scores.append(lat_ok / 4.0)

        # magnetic moments
        moments_list = data.get('co_magnetic_moments', [])
        gold_mom = {m['label']: m['moment_muB'] for m in gold['co_magnetic_moments']}
        mom_ok = 0
        for item in moments_list:
            lbl = item.get('label')
            val = safe_float(item.get('moment_muB'))
            if lbl in gold_mom and abs(val - gold_mom[lbl]) <= tols['moment_abs']:
                mom_ok += 1
        scores.append(mom_ok / max(len(gold_mom), 1))

        # Bader charges
        charges_list = data.get('co_bader_charges', [])
        gold_chg = {m['label']: m['charge_e'] for m in gold['co_bader_charges']}
        chg_ok = 0
        for item in charges_list:
            lbl = item.get('label')
            val = safe_float(item.get('charge_e'))
            if lbl in gold_chg and abs(val - gold_chg[lbl]) <= tols['charge_abs']:
                chg_ok += 1
        scores.append(chg_ok / max(len(gold_chg), 1))

        # band gap
        gap = data.get('band_gap_GGA+U')
        if gap is not None:
            gap_val = safe_float(gap)
        else:
            gap_val = None
        gold_gap = gold['band_gap_GGA+U']
        gap_ok = 0.0
        if gap_val is not None and abs(gap_val - gold_gap) <= tols['gap_abs']:
            gap_ok = 1.0
        scores.append(gap_ok)

        return sum(scores) / len(scores)


# === block: score_1 (check id='step04') ===
def score_1(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold_sites = step['gold']['sites']
        tol = step['tolerance_abs']
        rows = artifact
        site_vals = {}
        for row in rows:
            site_vals[row['site']] = float(row['formation_energy_eV'])
        scores = []
        for site, ge in gold_sites.items():
            if site in site_vals:
                if abs(site_vals[site] - ge) <= tol:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
            else:
                scores.append(0.0)
        avg = sum(scores) / max(len(scores), 1)
        order_correct = False
        if site_vals:
            min_site = min(site_vals, key=site_vals.get)
            order_correct = (min_site == 'O5')
        order_score = 1.0 if order_correct else 0.0
        return 0.7 * avg + 0.3 * order_score


# === block: score_2 (check id='step06') ===
def score_2(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold_rows = {r['adsorption_site']: r for r in step['gold']['rows']}
        tols = step['tolerances']
        rows = artifact
        site_rows = {}
        for r in rows:
            site_rows[r['adsorption_site']] = r
        total = 0.0
        nrows = 0
        for site, gr in gold_rows.items():
            if site not in site_rows:
                continue
            row = site_rows[site]
            row_score = 0.0
            checks = 0
            if abs(float(row['E_ads_eV']) - gr['E_ads_eV']) <= tols['energy_abs']:
                row_score += 1
            checks += 1
            for col in ['charge_Oa_e','charge_Ob_e','charge_Ba_star_e','charge_O_star_e','charge_Co_e']:
                if abs(float(row[col]) - gr[col]) <= tols['charge_abs']:
                    row_score += 1
                checks += 1
            if abs(float(row['Oa_Ob_bond_length_A']) - gr['Oa_Ob_bond_length_A']) <= tols['bond_abs']:
                row_score += 1
            checks += 1
            total += row_score / checks
            nrows += 1
        avg_row = total / nrows if nrows > 0 else 0.0
        order = 0.0
        if 'Bridge' in site_rows and 'Ba' in site_rows and 'O' in site_rows:
            e_br = float(site_rows['Bridge']['E_ads_eV'])
            e_ba = float(site_rows['Ba']['E_ads_eV'])
            e_o = float(site_rows['O']['E_ads_eV'])
            if e_br < e_ba < e_o:
                order = 1.0
        return 0.7 * avg_row + 0.3 * order


# === block: score_3 (check id='step08') ===
def score_3(artifact, step, ctx):
    def scorer(artifact, step, ctx):
        gold_rows = {r['adsorption_site']: r for r in step['gold']['rows']}
        tols = step['tolerances']
        rows = artifact
        site_rows = {}
        for r in rows:
            site_rows[r['adsorption_site']] = r
        total = 0.0
        nrows = 0
        for site, gr in gold_rows.items():
            if site not in site_rows:
                continue
            row = site_rows[site]
            row_score = 0.0
            checks = 0
            if abs(float(row['E_ads_eV']) - gr['E_ads_eV']) <= tols['energy_abs']:
                row_score += 1
            checks += 1
            for col in ['charge_Oa_e','charge_Ob_e','charge_Ba_star_e','charge_O_star_e','charge_Co_e']:
                if abs(float(row[col]) - gr[col]) <= tols['charge_abs']:
                    row_score += 1
                checks += 1
            if abs(float(row['Oa_Ob_bond_length_A']) - gr['Oa_Ob_bond_length_A']) <= tols['bond_abs']:
                row_score += 1
            checks += 1
            if 'Oa_vacancy_distance_A' in row and 'Oa_vacancy_distance_A' in gr:
                if abs(float(row['Oa_vacancy_distance_A']) - gr['Oa_vacancy_distance_A']) <= tols.get('dist_abs', 0.1):
                    row_score += 1
                checks += 1
            total += row_score / checks
            nrows += 1
        avg_row = total / nrows if nrows > 0 else 0.0
        order = 0.0
        if 'Bridge' in site_rows and 'Ba' in site_rows and 'O' in site_rows:
            e_br = float(site_rows['Bridge']['E_ads_eV'])
            e_ba = float(site_rows['Ba']['E_ads_eV'])
            e_o = float(site_rows['O']['E_ads_eV'])
            if e_br < e_ba < e_o:
                order = 1.0
        return 0.7 * avg_row + 0.3 * order


_SCORERS = {
    'step02': score_0,
    'step04': score_1,
    'step06': score_2,
    'step08': score_3,
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
