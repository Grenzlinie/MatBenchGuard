import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
    def load_file(path):
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            return f.read().strip()

    def parse_energy(txt):
        if txt is None:
            return None
        try:
            return float(txt)
        except:
            return None

    def parse_csv(path):
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        return rows

    output_dir = '/app/outputs'
    perfect_energy = parse_energy(load_file(os.path.join(output_dir, 'perfect_cell_energy.txt')))
    isolated_H = parse_energy(load_file(os.path.join(output_dir, 'isolated_H_energy.txt')))
    interstitial_rows = parse_csv(os.path.join(output_dir, 'interstitial_results.csv'))
    return {'perfect_energy': perfect_energy, 'isolated_H': isolated_H, 'interstitial_rows': interstitial_rows}


# === block: score_0 (check id='perfect_cell_energy') ===
def score_0(artifact, step, ctx):
    target = step.get('target', -8000.0)
    tolerance = step.get('tolerance_abs', 5000.0)
    val = ctx.get('perfect_energy')
    if val is None:
        return 0.0
    if abs(val - target) <= tolerance:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='isolated_H_energy') ===
def score_1(artifact, step, ctx):
    target = step.get('target', -12.3456)
    tolerance = step.get('tolerance_abs', 10.0)
    val = ctx.get('isolated_H')
    if val is None:
        return 0.0
    if abs(val - target) <= tolerance:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='interstitial_ordering') ===
def score_2(artifact, step, ctx):
    rows = ctx.get('interstitial_rows')
    if rows is None or len(rows) != 3:
        return 0.0
    site_data = {}
    for row in rows:
        site = row.get('site', '').strip()
        try:
            e = float(row.get('E_H_f', 0))
            dv = float(row.get('delta_V', 0))
        except:
            return 0.0
        site_data[site] = (e, dv)
    required_sites = ['I-Ti', 'I-SiTi', 'I-SiC']
    if any(s not in site_data for s in required_sites):
        return 0.0
    e_ti, dv_ti = site_data['I-Ti']
    e_siti, dv_siti = site_data['I-SiTi']
    e_sic, dv_sic = site_data['I-SiC']
    # check formation energy ordering: I-SiC and I-SiTi should be lower (more negative) than I-Ti
    e_list = [e_ti, e_siti, e_sic]
    max_e_idx = e_list.index(max(e_list))
    if max_e_idx != 0:
        return 0.0
    # volume ordering: I-SiC < I-SiTi < I-Ti
    vol_ok = (dv_sic < dv_siti < dv_ti)
    return 0.6 * 1.0 + 0.4 * (1.0 if vol_ok else 0.0)


# === block: score_3 (check id='interstitial_absolute') ===
def score_3(artifact, step, ctx):
    rows = ctx.get('interstitial_rows')
    if rows is None:
        return 0.0
    gold = {
        'I-Ti': (-2.228, 1.45),
        'I-SiTi': (-2.850, 0.90),
        'I-SiC': (-2.853, 0.55),
    }
    tol_e = 1.0
    tol_dv = 1.0
    e_ok = 0
    dv_ok = 0
    total_sites = 0
    for row in rows:
        site = row.get('site', '').strip()
        if site not in gold:
            continue
        ref_e, ref_dv = gold[site]
        try:
            e = float(row.get('E_H_f', 0))
            dv = float(row.get('delta_V', 0))
        except:
            continue
        if abs(e - ref_e) <= tol_e:
            e_ok += 1
        if abs(dv - ref_dv) <= tol_dv:
            dv_ok += 1
        total_sites += 1
    if total_sites == 0:
        return 0.0
    return 0.5 * (e_ok / total_sites) + 0.5 * (dv_ok / total_sites)


_SCORERS = {
    'perfect_cell_energy': score_0,
    'isolated_H_energy': score_1,
    'interstitial_ordering': score_2,
    'interstitial_absolute': score_3,
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
