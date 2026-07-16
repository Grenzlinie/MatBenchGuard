import os
import json
import csv

# === author imports / helpers ===
import json
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
    def compute_gold():
        # Constants from the paper
        RAW_EN = {
            'TaC': {
                'V_alpha': 15.30, 'V_beta': 9.45, 'A_beta': 7.59, 'B_alpha': 11.78,
                'I_A': -0.27, 'I_B': -2.71, 'V_alpha_V_beta': 24.61, 'A_beta_B_alpha': 5.45,
                'V_alpha_B_alpha': 22.63, 'V_beta_A_beta': 15.62, 'V_alpha_V_beta^2_T': 34.08,
                'V_alpha_V_beta^2_L': 33.94, 'V_alpha_V_beta^3_IP': 43.60, 'V_alpha_V_beta^3_OP': 43.62,
                'V_alpha_V_beta^4_IP': 53.16, 'V_alpha_V_beta^4_OP': 53.13, 'V_alpha_V_beta^5': 62.60,
                'V_alpha_V_beta^6': 72.13
            },
            'HfC': {
                'V_alpha': 19.30, 'V_beta': 10.20, 'A_beta': 9.13, 'B_alpha': 13.80,
                'I_A': -0.31, 'I_B': -3.99, 'V_alpha_V_beta': 27.90, 'A_beta_B_alpha': 5.00,
                'V_alpha_B_alpha': 25.86, 'V_beta_A_beta': 18.27, 'V_beta_B_alpha': 20.46,
                'V_beta_I_B': 4.30, 'V_alpha_V_beta^2_T': 36.80, 'V_alpha_V_beta^2_L': 37.03,
                'V_alpha_V_beta^3_IP': 46.01, 'V_alpha_V_beta^3_OP': 46.17,
                'V_alpha_V_beta^4_IP': 55.39, 'V_alpha_V_beta^4_OP': 55.75,
                'V_alpha_V_beta^5': 65.19, 'V_alpha_V_beta^6': 75.01
            }
        }
        COHESIVE = {'TaC': -11.10, 'HfC': -10.53}
        NU = 8
        X = 0.02  # metal-rich x

        # Symmetry factors for clusters (both carbides, except HfC V_beta_A_beta=12, V_beta_I_B=8)
        SIGMA = {
            'V_alpha_V_beta': 6, 'A_beta_B_alpha': 6, 'V_alpha_B_alpha': 6,
            'V_alpha_V_beta^2_T': 12, 'V_alpha_V_beta^2_L': 3,
            'V_alpha_V_beta^3_IP': 12, 'V_alpha_V_beta^3_OP': 8,
            'V_alpha_V_beta^4_IP': 3, 'V_alpha_V_beta^4_OP': 12,
            'V_alpha_V_beta^5': 6, 'V_alpha_V_beta^6': 1
        }

        def get(carbide, defect):
            return RAW_EN[carbide][defect]

        def eps0(carbide):
            return COHESIVE[carbide]

        gold = {}
        for carbide in ['TaC', 'HfC']:
            gold[carbide] = {}
            e0 = eps0(carbide)
            eva = get(carbide, 'V_alpha')
            evb = get(carbide, 'V_beta')
            ea = get(carbide, 'A_beta')
            eb = get(carbide, 'B_alpha')
            eia = get(carbide, 'I_A')
            eib = get(carbide, 'I_B')

            # --- Stoichiometric x=0 ---
            x0 = {}
            if carbide == 'TaC':
                # Leading defects V_alpha & V_beta (Table 6 left)
                eva_vb = (eva + evb + 2*e0) / 2
                x0['V_alpha']   = {'prefactor': 1.0, 'formation_energy_eV': eva_vb}
                x0['V_beta']    = {'prefactor': 1.0, 'formation_energy_eV': eva_vb}
                x0['A_beta']    = {'prefactor': 1.0, 'formation_energy_eV': ea - evb + eva}
                x0['B_alpha']   = {'prefactor': 1.0, 'formation_energy_eV': eb + evb - eva}
                x0['I_A']       = {'prefactor': 1.0, 'formation_energy_eV': eia - e0 + (eva - evb)/2.0}
                x0['I_B']       = {'prefactor': 1.0, 'formation_energy_eV': eib - e0 + (evb - eva)/2.0}
                # Composition-conserving defects (same for both stoichiometric and metal-rich)
                x0['A_beta_B_alpha']    = {'prefactor': SIGMA['A_beta_B_alpha'], 'formation_energy_eV': get(carbide,'A_beta_B_alpha')}
                x0['V_alpha_V_beta']    = {'prefactor': SIGMA['V_alpha_V_beta'], 'formation_energy_eV': get(carbide,'V_alpha_V_beta') + 2*e0}
                # Clusters V_alpha_V_beta^2 (T/L) from Table 6 left
                for n, key in [(2,'T'), (2,'L')]:
                    tag = f'V_alpha_V_beta^{n}_{key}'
                    s = SIGMA[tag]
                    x0[tag] = {'prefactor': s, 'formation_energy_eV': get(carbide, tag) + (n+1)*e0 + (eva - evb)/2.0}
                # V_alpha_V_beta^3,4,5,6 (Table 6 left)
                for n in [3,4,5,6]:
                    configs = ['IP','OP'] if n in [3,4] else [None]
                    for cfg in configs:
                        tag = f'V_alpha_V_beta^{n}_{cfg}' if cfg else f'V_alpha_V_beta^{n}'
                        s = SIGMA[tag] if tag in SIGMA else 1  # fallback
                        x0[tag] = {'prefactor': s, 'formation_energy_eV': get(carbide, tag) + (n+1)*e0 + ((n-1)*(eva - evb))/2.0}
                # V_alpha_B_alpha, V_beta_A_beta from Table 6 left
                x0['V_alpha_B_alpha'] = {'prefactor': SIGMA['V_alpha_B_alpha'], 'formation_energy_eV': get(carbide,'V_alpha_B_alpha') + e0 + 1.5*(evb - eva)}
                x0['V_beta_A_beta']   = {'prefactor': 6, 'formation_energy_eV': get(carbide,'V_beta_A_beta') + e0 + 1.5*(eva - evb)}
            else:  # HfC
                # Leading defects V_beta & I_B (Table 6 right)
                sqrt2nu = math.sqrt(2*NU)
                x0['V_alpha']   = {'prefactor': 1.0/sqrt2nu, 'formation_energy_eV': eva + 2*e0 + (evb - eib)/2.0}
                x0['V_beta']    = {'prefactor': sqrt2nu, 'formation_energy_eV': (evb + eib)/2.0}
                x0['A_beta']    = {'prefactor': 2*NU, 'formation_energy_eV': ea - evb + eib - 2*e0}
                x0['B_alpha']   = {'prefactor': 1.0/(2*NU), 'formation_energy_eV': eb + evb - eib + 2*e0}
                x0['I_A']       = {'prefactor': sqrt2nu, 'formation_energy_eV': eia - 2*e0 + (eib - evb)/2.0}
                x0['I_B']       = {'prefactor': 1.0/sqrt2nu, 'formation_energy_eV': (evb + eib)/2.0}
                # A_beta_B_alpha, V_alpha_V_beta, V_beta_I_B (stable)
                x0['A_beta_B_alpha']    = {'prefactor': SIGMA['A_beta_B_alpha'], 'formation_energy_eV': get(carbide,'A_beta_B_alpha')}
                x0['V_alpha_V_beta']    = {'prefactor': SIGMA['V_alpha_V_beta'], 'formation_energy_eV': get(carbide,'V_alpha_V_beta') + 2*e0}
                x0['V_beta_I_B']        = {'prefactor': 8, 'formation_energy_eV': get(carbide,'V_beta_I_B')}
                # V_beta_B_alpha (stable)
                x0['V_beta_B_alpha']    = {'prefactor': 6.0/sqrt2nu, 'formation_energy_eV': get(carbide,'V_beta_B_alpha') + 2*e0 + (evb - eib)/2.0}
                # Vacancy clusters V_alpha_V_beta^n from Table 6 right
                for n, configs in [(2,['T','L']), (3,['IP','OP']), (4,['IP','OP']), (5,[]), (6,[])]:
                    for cfg in (configs if configs else [None]):
                        tag = f'V_alpha_V_beta^{n}_{cfg}' if cfg else f'V_alpha_V_beta^{n}'
                        sig = SIGMA[tag] if tag in SIGMA else 1
                        pref = sig * (sqrt2nu)**((n-1)/2)
                        form = get(carbide, tag) + 2*e0 + ((n-1)*(eib - evb))/2.0
                        x0[tag] = {'prefactor': pref, 'formation_energy_eV': form}
                # V_alpha_B_alpha, V_beta_A_beta
                sqrt23 = (2*NU)**1.5   # (2*ν)^(3/2)
                x0['V_alpha_B_alpha'] = {'prefactor': SIGMA['V_alpha_B_alpha']/sqrt23, 'formation_energy_eV': get(carbide,'V_alpha_B_alpha') + 4*e0 + 1.5*(evb - eib)}
                x0['V_beta_A_beta']   = {'prefactor': 12*sqrt23, 'formation_energy_eV': get(carbide,'V_beta_A_beta') - 2*e0 - 1.5*(evb - eib)}

            gold[carbide]['x=0'] = x0

            # --- Metal-rich x=0.02 (Table 5) ---
            xr = X
            pre_vac = 4*xr
            inv4x = 1.0/pre_vac
            inv4x2 = inv4x**2
            # Table 5 entries
            xmr = {}
            xmr['V_alpha'] = {'prefactor': inv4x, 'formation_energy_eV': eva + evb + 2*e0}
            xmr['V_beta']  = {'prefactor': pre_vac, 'formation_energy_eV': 0.0}
            xmr['A_beta']  = {'prefactor': pre_vac**2, 'formation_energy_eV': ea - 2*evb - 2*e0}
            xmr['B_alpha'] = {'prefactor': inv4x2, 'formation_energy_eV': eb + 2*evb + 2*e0}
            xmr['I_A']     = {'prefactor': pre_vac, 'formation_energy_eV': eia - evb - 2*e0}
            xmr['I_B']     = {'prefactor': inv4x, 'formation_energy_eV': eib + evb}
            # Composition-conserving: A_beta_B_alpha (same as x=0)
            xmr['A_beta_B_alpha'] = {'prefactor': 6, 'formation_energy_eV': get(carbide,'A_beta_B_alpha')}
            # V_alpha_V_beta (divacancy) m=1: prefactor sigma, formation = e_... + 2*e0
            xmr['V_alpha_V_beta'] = {'prefactor': SIGMA['V_alpha_V_beta'], 'formation_energy_eV': get(carbide,'V_alpha_V_beta') + 2*e0}
            # V_beta_I_B: if stable, prefactor sigma, formation = e_... (m=0)
            if carbide == 'HfC':
                xmr['V_beta_I_B'] = {'prefactor': 8, 'formation_energy_eV': get(carbide,'V_beta_I_B')}
            # V_beta_B_alpha in HfC: prefactor sigma/(4x), formation = e_... + evb + 2*e0
            if carbide == 'HfC':
                xmr['V_beta_B_alpha'] = {'prefactor': 6/(4*xr), 'formation_energy_eV': get(carbide,'V_beta_B_alpha') + evb + 2*e0}
            # V_alpha_B_alpha: prefactor sigma/(4*x)^3, formation = e_... + 3*evb + 4*e0
            xmr['V_alpha_B_alpha'] = {'prefactor': SIGMA['V_alpha_B_alpha']/((4*xr)**3), 'formation_energy_eV': get(carbide,'V_alpha_B_alpha') + 3*evb + 4*e0}
            # V_beta_A_beta: prefactor sigma*(4*x)^3, formation = e_... - 3*evb - 2*e0
            if carbide == 'TaC':
                xmr['V_beta_A_beta'] = {'prefactor': 6 * (4*xr)**3, 'formation_energy_eV': get(carbide,'V_beta_A_beta') - 3*evb - 2*e0}
            else:
                xmr['V_beta_A_beta'] = {'prefactor': 12 * (4*xr)**3, 'formation_energy_eV': get(carbide,'V_beta_A_beta') - 3*evb - 2*e0}
            # Vacancy clusters V_alpha_V_beta^n: prefactor sigma*(4*x)^(n-1), formation = e_... - (n-1)*evb + 2*e0
            for n in [2,3,4,5,6]:
                configs = []
                if n == 2: configs = ['T','L']
                elif n == 3: configs = ['IP','OP']
                elif n == 4: configs = ['IP','OP']
                else: configs = [None]
                for cfg in configs:
                    tag = f'V_alpha_V_beta^{n}_{cfg}' if cfg else f'V_alpha_V_beta^{n}'
                    sig = SIGMA[tag] if tag in SIGMA else 1
                    pref = sig * (4*xr)**(n-1)
                    form = get(carbide, tag) - (n-1)*evb + 2*e0
                    xmr[tag] = {'prefactor': pref, 'formation_energy_eV': form}
            gold[carbide]['x=0.02'] = xmr

        # Define stable defects per carbide/composition (those that must be present)
        stable_required = {}
        for carb in ['TaC','HfC']:
            for comp in ['x=0','x=0.02']:
                stable_required[f'{carb}/{comp}'] = set(gold[carb][comp].keys())
        # For TaC, remove unstable ones
        # V_beta_B_alpha and V_beta_I_B are unstable in TaC, so don't require them
        for comp in ['x=0','x=0.02']:
            stable_required[f'TaC/{comp}'].discard('V_beta_B_alpha')
            stable_required[f'TaC/{comp}'].discard('V_beta_I_B')
            # For HfC, all are stable

        return {'gold': gold, 'stable_required': stable_required}

    ctx = compute_gold()
    return ctx


# === block: score_0 (check id='check_arrhenius_params') ===
def score_0(artifact, step, ctx):
    def score_arrhenius(agent_json, gold, stable_required):
        total_pairs = 0
        passed_pairs = 0
        # Tolerance: formation energy: max(0.01, 0.02*abs(gold)) eV; prefactor: max(1e-10, 0.02*max(abs(gold),1e-10))
        for carbide in ['TaC','HfC']:
            if carbide not in agent_json:
                # missing top-level key counts as zero for all
                return 0.0
            for comp in ['x=0','x=0.02']:
                if comp not in agent_json[carbide]:
                    return 0.0
                agent_comp = agent_json[carbide][comp]
                gold_comp = gold[carbide][comp]
                required_set = stable_required[f'{carbide}/{comp}']
                for defect in required_set:
                    # check if agent has this defect (non-null, present)
                    agent_def = agent_comp.get(defect)
                    if agent_def is None or not isinstance(agent_def, dict):
                        passed_pairs += 0  # missing stable defect
                    else:
                        gold_def = gold_comp[defect]
                        # check prefactor
                        agent_p = agent_def.get('prefactor')
                        gold_p = gold_def['prefactor']
                        if agent_p is not None:
                            tol_p = max(1e-10, 0.02 * max(abs(gold_p), 1e-10))
                            if abs(agent_p - gold_p) <= tol_p:
                                passed_pairs += 1
                        # check formation energy
                        agent_e = agent_def.get('formation_energy_eV')
                        gold_e = gold_def['formation_energy_eV']
                        if agent_e is not None:
                            tol_e = max(0.01, 0.02 * abs(gold_e))
                            if abs(agent_e - gold_e) <= tol_e:
                                passed_pairs += 1
                        total_pairs += 2  # we count each parameter separately
                # additional non-required defects (if any) are ignored, not penalized
        if total_pairs == 0:
            return 0.0
        return passed_pairs / total_pairs

    return score_arrhenius(artifact, ctx['gold'], ctx['stable_required'])


_SCORERS = {
    'check_arrhenius_params': score_0,
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
