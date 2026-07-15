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
        constants = spec.get('constants', {})
        ctx = dict(constants)
        ctx['outputs_dir'] = outputs_dir
        return ctx


# === block: score_0 (check id='physical_properties') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        const = ctx
        dens_o = const['density_oxides']
        M_o = const['molar_mass_oxides']
        n_o = const['oxygen_per_mole']
        comp_list = const['composition']
        tol = const['tolerances']['physical_relative']
        # Build lookup
        rows = {row['glass_code']: row for row in artifact}
        scores = []
        for comp in comp_list:
            code = comp['code']
            if code not in rows:
                scores.append(0.0)
                continue
            row = rows[code]
            x = comp['x']
            # W_glass
            W = sum(x[ox]*M_o[ox] for ox in x)
            # density: 1/rho = sum( x_i * M_i / (W * rho_i) )? Actually use mass fractions
            # f_i = (x_i * M_i) / W
            # rho = 1 / sum( f_i / rho_i )
            f = {ox: x[ox]*M_o[ox]/W for ox in x}
            inv_rho = sum(f[ox]/dens_o[ox] for ox in x)
            rho_exp = 1.0 / inv_rho
            Vm_exp = W / rho_exp
            N = sum(x[ox]*n_o[ox] for ox in x)
            VO_exp = Vm_exp / N
            OPD_exp = 1000.0 / VO_exp
        
            # compare
            d = abs(float(row['density_g_cm3']) - rho_exp) / rho_exp
            if d <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (d - tol) / (2*tol)))
            # For other properties we could also check but density is key; we could add other checks separately
        return float(sum(scores)/len(scores)) if scores else 0.0


# === block: score_1 (check id='mechanical_moduli') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        const = ctx
        M_o = const['molar_mass_oxides']
        dens_o = const['density_oxides']
        comp_list = const['composition']
        Gi = const['makishima_constants']['Gi_kcal_per_cm3']
        Vi = const['makishima_constants']['Vi_packing_factor']
        tol = const['tolerances']['mechanical_relative']
        # Load physical properties to get density (since we recompute, but we can use agent's density if consistent? Better to recompute ourselves for gold.
        # We'll recompute density for each glass using same method.
        # We'll build expected values
        rows = {row['glass_code']: row for row in artifact}
        scores = []
        for comp in comp_list:
            code = comp['code']
            if code not in rows:
                scores.append(0.0)
                continue
            row = rows[code]
            x = comp['x']
            W = sum(x[ox]*M_o[ox] for ox in x)
            f = {ox: x[ox]*M_o[ox]/W for ox in x}
            inv_rho = sum(f[ox]/dens_o[ox] for ox in x)
            rho = 1.0 / inv_rho
            Vm = W / rho
            # Makishima calculation
            G_t = sum(x[ox]*Gi[ox] for ox in x)  # kcal/cm3
            # convert to GPa: 1 kcal/cm3 = 4.184 GPa
            G_t_GPa = G_t * 4.184
            sum_Vi_xi = sum(x[ox]*Vi[ox] for ox in x)
            V_t = (rho / W) * sum_Vi_xi  # dimensionless
            E_exp = 2.0 * V_t * G_t_GPa
            B_exp = 1.2 * V_t * E_exp
            S_exp = (3.0 * E_exp * B_exp) / (9.0 * B_exp - E_exp) if (9.0*B_exp - E_exp) != 0 else 0.0
            L_exp = B_exp + (4.0/3.0) * S_exp
        
            # compare
            d_E = abs(float(row['Young_modulus_GPa']) - E_exp) / E_exp if E_exp != 0 else 1.0
            d_B = abs(float(row['bulk_modulus_GPa']) - B_exp) / B_exp if B_exp != 0 else 1.0
            d_S = abs(float(row['shear_modulus_GPa']) - S_exp) / S_exp if S_exp != 0 else 1.0
            d_L = abs(float(row['longitudinal_modulus_GPa']) - L_exp) / L_exp if L_exp != 0 else 1.0
            # combine
            avg_d = (d_E + d_B + d_S + d_L) / 4.0
            if avg_d <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (avg_d - tol) / (2*tol)))
        return float(sum(scores)/len(scores)) if scores else 0.0


# === block: score_2 (check id='mac_table') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        const = ctx
        # Load physical_properties.csv to get density
        outputs_dir = ctx['outputs_dir']
        import os
        from pathlib import Path
        phys_path = os.path.join(outputs_dir, 'physical_properties.csv')
        from csv import DictReader
        if not os.path.exists(phys_path):
            return 0.0
        with open(phys_path, newline='') as f:
            phys_rows = list(DictReader(f))
        density_map = {r['glass_code']: float(r['density_g_cm3']) for r in phys_rows}
        gold = const['gold_lac_points']
        energies_needed = ['0.015','0.3'] # MeV as string keys
        tol = const['tolerances']['mac_lac_relative']
        # Build dict from agent's mac_table
        mac_rows = { (r['glass_code'], float(r['energy_MeV'])): float(r['mac_cm2_g']) for r in artifact }
        checks = []
        for code in ['BVBL0','BVBL3']:
            if code not in density_map:
                checks.append(0.0)
                continue
            rho = density_map[code]
            for en in energies_needed:
                e = float(en)
                key = (code, e)
                if key not in mac_rows:
                    checks.append(0.0)
                    continue
                mac = mac_rows[key]
                lac = mac * rho
                lac_gold = gold[code][en]
                err = abs(lac - lac_gold) / lac_gold
                if err <= tol:
                    checks.append(1.0)
                else:
                    checks.append(max(0.0, 1.0 - (err - tol) / tol))
        # minimal check: at least two points per glass
        if len(checks) < 4:
            return 0.0
        return float(sum(checks)/len(checks))


# === block: score_3 (check id='shielding_trends') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        const = ctx
        outputs_dir = ctx['outputs_dir']
        import os
        from csv import DictReader
        phys_path = os.path.join(outputs_dir, 'physical_properties.csv')
        mac_path = os.path.join(outputs_dir, 'mac_table.csv')
        if not os.path.exists(phys_path) or not os.path.exists(mac_path):
            return 0.0
        with open(phys_path, newline='') as f:
            phys_rows = list(DictReader(f))
        with open(mac_path, newline='') as f:
            mac_rows = list(DictReader(f))
        density_map = {r['glass_code']: float(r['density_g_cm3']) for r in phys_rows}
        # build mac dict
        mac_dict = {}
        for r in mac_rows:
            code = r['glass_code']
            e = float(r['energy_MeV'])
            mac = float(r['mac_cm2_g'])
            mac_dict.setdefault(code, {})[e] = mac
        energies = const['photon_energies']
        # Check 1: LAC monotonic increase with Bi2O3 content for each energy
        # Order glasses by composition Bi2O3 content: BVBL0,3,6,9,12,15
        codes = ['BVBL0','BVBL3','BVBL6','BVBL9','BVBL12','BVBL15']
        ok_energy = 0
        total_energy = len(energies)
        for e in energies:
            lac_list = []
            valid = True
            for code in codes:
                if code not in density_map or code not in mac_dict or e not in mac_dict[code]:
                    valid = False
                    break
                lac_list.append(mac_dict[code][e] * density_map[code])
            if valid and all(lac_list[i] <= lac_list[i+1] for i in range(len(lac_list)-1)):
                ok_energy += 1
        score1 = ok_energy / total_energy if total_energy > 0 else 0.0
        # Check 2: HVL ratio BVBL0/BVBL15 > 1 for each energy
        ok_hvl = 0
        if 'BVBL0' in density_map and 'BVBL15' in density_map:
            rho0 = density_map['BVBL0']
            rho15 = density_map['BVBL15']
            for e in energies:
                if 'BVBL0' in mac_dict and e in mac_dict['BVBL0'] and 'BVBL15' in mac_dict and e in mac_dict['BVBL15']:
                    lac0 = mac_dict['BVBL0'][e] * rho0
                    lac15 = mac_dict['BVBL15'][e] * rho15
                    if lac0 > 0 and lac15 > 0:
                        hvl0 = math.log(2) / lac0
                        hvl15 = math.log(2) / lac15
                        if hvl0 / hvl15 > 1.0:
                            ok_hvl += 1
            score2 = ok_hvl / total_energy if total_energy > 0 else 0.0
        else:
            score2 = 0.0
        # combine equally
        return (score1 + score2) / 2.0


_SCORERS = {
    'physical_properties': score_0,
    'mechanical_moduli': score_1,
    'mac_table': score_2,
    'shielding_trends': score_3,
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
