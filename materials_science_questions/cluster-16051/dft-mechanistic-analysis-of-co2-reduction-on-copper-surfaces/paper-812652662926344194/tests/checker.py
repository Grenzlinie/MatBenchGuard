import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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


# === block: score_0 (check id='step_adsorption') ===
def score_0(artifact, step, ctx):
    entry_list = artifact.get('adsorption_energies', [])
    if not entry_list:
        return 0.0
    gold = step['gold']
    tol_energy = step['tolerances']['energy_eV']
    tol_angle = step['tolerances']['angle_deg']
    lookup = {}
    for e in entry_list:
        key = (e.get('system',''), e.get('adsorbate',''), e.get('site',''))
        lookup[key] = e

    def score_val(val, gold_val, tol, decay=None):
        if val is None: return 0.0
        err = abs(val - gold_val)
        if err <= tol: return 1.0
        if decay is None: decay = tol
        return max(0.0, 1.0 - (err - tol) / decay)

    def chalc_from_sys(sys):
        """Extract the chalcogen symbol ('O','S','Se','Te') from a system string, or 'Cu' for clean Cu."""
        if '-' in sys:
            return sys.rsplit('-', 1)[-1]
        return 'Cu'

    # expected keys
    keys_co2_cu = [('Cu(111)','CO₂*','Cu')]
    keys_co2_x = [('Cu(111)-'+x, 'CO₂*', 'X') for x in ['O','S','Se','Te']]
    keys_h_cu = [('Cu(111)','H*','Cu')]
    keys_h_x = [('Cu(111)-'+x, 'H*', 'X') for x in ['O','S','Se','Te']]
    keys_adat = [('Cu(111)-'+x, 'X_adatom', 'Cu') for x in ['O','S','Se','Te']]
    all_keys = keys_co2_cu + keys_co2_x + keys_h_cu + keys_h_x + keys_adat
    ws = []
    for (sys, ads, site) in all_keys:
        entry = lookup.get((sys, ads, site))
        if entry is None:
            ws.append(0.0)
            continue
        chalc = chalc_from_sys(sys)
        if ads == 'CO₂*':
            g_energy = gold['CO2*'][chalc]
            g_angle = gold['CO2*_angle'][chalc]
            val_energy = entry.get('adsorption_free_energy_eV')
            val_angle = entry.get('activation_angle_deg')
            s_energy = score_val(val_energy, g_energy, tol_energy, 0.5)
            s_angle = score_val(val_angle, g_angle, tol_angle, 5.0)
            ws.append(0.5*s_energy + 0.5*s_angle)
        elif ads == 'H*':
            g_energy = gold['H*'][chalc]
            val_energy = entry.get('adsorption_free_energy_eV')
            s_energy = score_val(val_energy, g_energy, tol_energy, 0.5)
            # Trend: H* on S,Se,Te must be > 0
            if chalc in ('S', 'Se', 'Te') and val_energy is not None and val_energy <= 0.0:
                s_energy = 0.0
            ws.append(s_energy)
        elif ads == 'X_adatom':
            g_energy = gold['X_adatom'][chalc]
            val_energy = entry.get('adsorption_free_energy_eV')
            s_energy = score_val(val_energy, g_energy, tol_energy, 0.5)
            # Sign: O must be >0, S,Se,Te <0
            if chalc == 'O' and val_energy is not None and val_energy <= 0:
                s_energy = 0.0
            if chalc in ('S', 'Se', 'Te') and val_energy is not None and val_energy >= 0:
                s_energy = 0.0
            ws.append(s_energy)
    if not ws:
        return 0.0
    return sum(ws) / len(ws)


# === block: score_1 (check id='step_electronic') ===
def score_1(artifact, step, ctx):
    arr = artifact
    if not isinstance(arr, list):
        return 0.0
    lookup = {}
    for d in arr:
        chalc = d.get('chalcogen','')
        if chalc:
            lookup[chalc] = d
    gold = step['gold']
    tol_Bader = step['tolerances']['Bader_e']
    tol_pband = step['tolerances']['p_band_eV']
    tol_dband = step['tolerances']['d_band_eV']
    def score_val(val, gold_val, tol, decay=None):
        if val is None: return 0.0
        err = abs(val - gold_val)
        if err <= tol: return 1.0
        if decay is None: decay = tol
        return max(0.0, 1.0 - (err - tol) / decay)
    ws = []
    for chalc in ['O','S','Se','Te']:
        entry = lookup.get(chalc)
        if not entry:
            ws.append(0.0)
            continue
        g = gold[chalc]
        s_b = score_val(entry.get('Bader_charge_X_e'), g['Bader'], tol_Bader, 0.2)
        s_p = score_val(entry.get('p_band_center_X_eV'), g['p_band'], tol_pband, 0.4)
        s_d = score_val(entry.get('d_band_shift_Cu_eV'), g['d_band'], tol_dband, 0.1)
        ws.append((s_b + s_p + s_d) / 3.0)
    if not ws:
        return 0.0
    return sum(ws) / len(ws)


_SCORERS = {
    'step_adsorption': score_0,
    'step_electronic': score_1,
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
