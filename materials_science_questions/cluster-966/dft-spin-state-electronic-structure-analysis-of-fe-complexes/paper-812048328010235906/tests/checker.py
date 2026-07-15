import os
import json
import csv

# === author imports / helpers ===
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
        step = spec['steps'][0]
        gold = step['gold']
        return {'gold': gold}


# === block: score_0 (check id='adsorption_parameters') ===
def score_0(artifact, step, ctx):
        gold = ctx['gold']
        refs = gold['refs']
        tol = gold['tolerances']
        consist = gold['consistency']
        if not isinstance(artifact, dict):
            return 0.0
        for key in ['1Ads','2Ads','3Ads']:
            if key not in artifact:
                return 0.0
            # each config must be a dict
            if not isinstance(artifact[key], dict):
                return 0.0

        def field_score(val, ref, tol_val):
            dif = abs(val - ref)
            if dif <= tol_val:
                return 1.0
            elif dif >= 2*tol_val:
                return 0.0
            else:
                return 1.0 - (dif - tol_val) / tol_val

        geo_fields = [
            ('Fe_Ha', tol['distance_abs']),
            ('Fe_Hb', tol['distance_abs']),
            ('O_Ha', tol['distance_abs']),
            ('O_Hb', tol['distance_abs']),
            ('H_H', tol['distance_abs']),
            ('Fe_O', tol['distance_abs']),
            ('angle_O_Fe_Ha', tol['angle_abs']),
            ('angle_O_Fe_Hb', tol['angle_abs']),
            ('dihedral_O_Fe_Ha_Hb', tol['dihedral_abs'])
        ]
        geo_scores = []
        energy_scores = []
        freq_scores = []
        for cfg in ['1Ads','2Ads','3Ads']:
            cfg_data = artifact[cfg]
            ref_cfg = refs[cfg]
            geo_sum = 0.0
            for fname, ftol in geo_fields:
                v = cfg_data.get(fname)
                if v is None:
                    return 0.0
                geo_sum += field_score(float(v), ref_cfg[fname], ftol)
            geo_scores.append(geo_sum / len(geo_fields))

            e = cfg_data.get('adsorption_energy_kJ_mol')
            if e is None:
                return 0.0
            energy_scores.append(field_score(float(e), ref_cfg['adsorption_energy_kJ_mol'], tol['energy_abs']))

            f = cfg_data.get('HH_frequency_cm1')
            if f is None:
                return 0.0
            freq_scores.append(field_score(float(f), ref_cfg['HH_frequency_cm1'], tol['frequency_abs']))

        geo_avg = sum(geo_scores) / 3.0
        energy_avg = sum(energy_scores) / 3.0
        freq_avg = sum(freq_scores) / 3.0
        combined = 0.6 * geo_avg + 0.2 * energy_avg + 0.2 * freq_avg

        consist_ok = True
        for cfg in ['1Ads','2Ads','3Ads']:
            hh = artifact[cfg].get('H_H')
            if hh is None:
                consist_ok = False
                continue
            if float(hh) <= consist['h_h_min']:
                consist_ok = False
        for cfg in ['1Ads','2Ads','3Ads']:
            e = artifact[cfg].get('adsorption_energy_kJ_mol')
            if e is None:
                consist_ok = False
                continue
            if float(e) >= 0:
                consist_ok = False

        # safe extraction of adsorption energies for ordering check
        e1_val = artifact['1Ads'].get('adsorption_energy_kJ_mol')
        e2_val = artifact['2Ads'].get('adsorption_energy_kJ_mol')
        e3_val = artifact['3Ads'].get('adsorption_energy_kJ_mol')
        if e1_val is None or e2_val is None or e3_val is None:
            consist_ok = False
        else:
            try:
                e1 = float(e1_val)
                e2 = float(e2_val)
                e3 = float(e3_val)
            except (TypeError, ValueError):
                consist_ok = False
            else:
                if abs(e1 - e2) > consist['energy_ordering']['sextet_pair_max_diff_abs']:
                    consist_ok = False
                if not (e3 >= e1 + consist['energy_ordering']['quartet_less_stable_than_sextet_min_kJ']) \
                   or not (e3 >= e2 + consist['energy_ordering']['quartet_less_stable_than_sextet_min_kJ']):
                    consist_ok = False

        multiplier = 1.0 if consist_ok else 0.8
        final_score = combined * multiplier
        return final_score


_SCORERS = {
    'adsorption_parameters': score_0,
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
