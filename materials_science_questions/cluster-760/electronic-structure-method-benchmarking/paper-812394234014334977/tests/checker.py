import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    return {'gold': spec['steps'][0]['gold'], 'tolerances': spec['steps'][0]['tolerances']}


# === block: score_0 (check id='computed_results') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    tols = ctx['tolerances']
    halogens = ['F','Cl','Br','I']
    if not isinstance(artifact, dict):
        return 0.0
    if not all(k in artifact for k in halogens + ['energetics','looseness_parameters']):
        return 0.0

    # ----- structural parameter checks (bond lengths, frequencies, dipole) -----
    struct_checks = []
    for x in halogens:
        if x not in artifact:
            continue
        a = artifact[x]
        g = gold[x]
        # LiX bond length
        if 'LiX' in a and 'bond_lengths' in a['LiX'] and 'Li-X' in a['LiX']['bond_lengths'] and 'LiX' in g:
            try:
                if abs(a['LiX']['bond_lengths']['Li-X'] - g['LiX']['bond_lengths']['Li-X']) <= tols['bond_length']:
                    struct_checks.append(1)
                else:
                    struct_checks.append(0)
            except:
                struct_checks.append(0)
        # N-X bond length
        if 'NH2X' in a and 'bond_lengths' in a['NH2X'] and 'N-X' in a['NH2X']['bond_lengths'] and 'NH2X' in g and 'bond_lengths' in g['NH2X']:
            try:
                if abs(a['NH2X']['bond_lengths']['N-X'] - g['NH2X']['bond_lengths']['N-X']) <= tols['bond_length']:
                    struct_checks.append(1)
                else:
                    struct_checks.append(0)
            except:
                struct_checks.append(0)
        # LiX frequency
        if 'LiX' in a and 'frequencies' in a['LiX'] and len(a['LiX']['frequencies'])>0 and 'LiX' in g and 'frequencies' in g['LiX']:
            try:
                if abs(a['LiX']['frequencies'][0] - g['LiX']['frequencies'][0]) <= tols['frequency']:
                    struct_checks.append(1)
                else:
                    struct_checks.append(0)
            except:
                struct_checks.append(0)
        # LiX dipole moment
        if 'LiX' in a and 'dipole_moment' in a['LiX'] and 'LiX' in g and 'dipole_moment' in g['LiX']:
            try:
                if abs(a['LiX']['dipole_moment'] - g['LiX']['dipole_moment']) <= tols['dipole_moment']:
                    struct_checks.append(1)
                else:
                    struct_checks.append(0)
            except:
                struct_checks.append(0)
        # additional bond lengths in complexes/TS (low weight)
        for species in ['complex_inv','complex_ret','ts_inv','ts_ret']:
            if species in a and species in g and 'bond_lengths' in g[species]:
                for bond_key in g[species]['bond_lengths']:
                    try:
                        aval = a[species].get('bond_lengths',{}).get(bond_key)
                        if aval is not None and abs(aval - g[species]['bond_lengths'][bond_key]) <= tols['bond_length']:
                            struct_checks.append(1)
                        else:
                            struct_checks.append(0)
                    except:
                        struct_checks.append(0)
    struct_score = (sum(struct_checks) / len(struct_checks)) * 0.2 if struct_checks else 0.0

    # ----- dissociation energy checks -----
    disso_checks = []
    for x in halogens:
        a = artifact.get(x,{})
        g = gold[x]
        if 'LiX' in a and 'dissociation_energy' in a['LiX'] and 'LiX' in g:
            try:
                if abs(a['LiX']['dissociation_energy'] - g['LiX']['dissociation_energy']) <= tols['energy_kj_per_mol']:
                    disso_checks.append(1)
                else:
                    disso_checks.append(0)
            except:
                disso_checks.append(0)
        if 'NH2X' in a and 'dissociation_energy' in a['NH2X'] and 'NH2X' in g:
            try:
                if abs(a['NH2X']['dissociation_energy'] - g['NH2X']['dissociation_energy']) <= tols['energy_kj_per_mol']:
                    disso_checks.append(1)
                else:
                    disso_checks.append(0)
            except:
                disso_checks.append(0)
    disso_score = (sum(disso_checks)/len(disso_checks))*0.15 if disso_checks else 0.0

    # ----- energetic value checks -----
    energy_checks = []
    energetics = artifact.get('energetics',{})
    for x in halogens:
        g_ener = gold.get('energetics',{}).get(x,[])
        a_ener = energetics.get(x,[])
        if not g_ener or not a_ener:
            continue
        entry_g = g_ener[0]
        entry_a = a_ener[0] if a_ener else {}
        for key in ['complexation_energy_inv','complexation_energy_ret','central_barrier_inv','central_barrier_ret','overall_barrier_inv','overall_barrier_ret']:
            try:
                if abs(entry_a[key] - entry_g[key]) <= tols['energy_kj_per_mol']:
                    energy_checks.append(1)
                else:
                    energy_checks.append(0)
            except:
                energy_checks.append(0)
    energy_score = (sum(energy_checks)/len(energy_checks))*0.4 if energy_checks else 0.0

    # ----- looseness recompute (consistency) -----
    looseness_checks = []
    for x in halogens:
        a_species = artifact.get(x,{})
        g_loose = gold.get('looseness_parameters',{}).get(x,{})
        for pathway, comp_key, ts_key in [('inv','complex_inv','ts_inv'),('ret','complex_ret','ts_ret')]:
            comp = a_species.get(comp_key,{})
            ts = a_species.get(ts_key,{})
            if not comp or not ts:
                continue
            # recompute N-X looseness
            try:
                nx_comp = comp['bond_lengths']['N-X']
                nx_ts = ts['bond_lengths']['N-X']
                nx_pct = 100*(nx_ts - nx_comp)/nx_comp
                gt_key_nx = '%N-X^neq_'+pathway
                if gt_key_nx in g_loose and abs(nx_pct - g_loose[gt_key_nx]) <= tols['looseness_pct']:
                    looseness_checks.append(1)
                else:
                    looseness_checks.append(0)
            except:
                looseness_checks.append(0)
            # recompute Li-X looseness
            try:
                lix_comp = comp['bond_lengths']['Li-X']
                lix_ts = ts['bond_lengths']['Li-X']
                lix_pct = 100*(lix_ts - lix_comp)/lix_comp
                gt_key_lix = '%Li-X^neq_'+pathway
                if gt_key_lix in g_loose and abs(lix_pct - g_loose[gt_key_lix]) <= tols['looseness_pct']:
                    looseness_checks.append(1)
                else:
                    looseness_checks.append(0)
            except:
                looseness_checks.append(0)
    looseness_score = (sum(looseness_checks)/len(looseness_checks))*0.1 if looseness_checks else 0.0

    # ----- trend verification -----
    trends_ok = 0
    total_trends = 5
    energetics_present = artifact.get('energetics') and all(x in energetics for x in halogens)
    if energetics_present:
        inv_barriers = [energetics[x][0].get('overall_barrier_inv') for x in halogens]
        # inversion overall barriers decreasing F > Cl > Br > I
        if None not in inv_barriers and sorted(inv_barriers, reverse=True) == inv_barriers:
            trends_ok += 1
        # inversion complexation energies increasing I > Br > Cl > F
        inv_comp = [energetics[x][0].get('complexation_energy_inv') for x in halogens]
        if None not in inv_comp and sorted(inv_comp) == inv_comp:
            trends_ok += 1
        # retention complexation energies decreasing F > Cl > Br > I
        ret_comp = [energetics[x][0].get('complexation_energy_ret') for x in halogens]
        if None not in ret_comp and sorted(ret_comp, reverse=True) == ret_comp:
            trends_ok += 1
        # retention overall barriers higher than inversion for each X
        ret_higher = all(
            energetics[x][0].get('overall_barrier_ret', -999) > energetics[x][0].get('overall_barrier_inv', -998)
            for x in halogens
        )
        if ret_higher:
            trends_ok += 1
    # Li-X dissociation energies decreasing F > Cl > Br > I
    if all(x in artifact for x in halogens):
        disso_vals = [artifact[x]['LiX'].get('dissociation_energy') for x in halogens]
        if None not in disso_vals and sorted(disso_vals, reverse=True) == disso_vals:
            trends_ok += 1
    # Li-X looseness decreasing F > Cl > Br > I
    loose = artifact.get('looseness_parameters')
    if loose and all(x in loose for x in halogens):
        lix_loose = [loose[x].get('%Li-X^neq_inv') for x in halogens]
        if None not in lix_loose and sorted(lix_loose, reverse=True) == lix_loose:
            trends_ok += 1
            total_trends += 1  # add one more trend if looseness present
        else:
            total_trends += 1
    trend_score = (trends_ok / total_trends) * 0.15 if total_trends>0 else 0.0

    total = struct_score + disso_score + energy_score + looseness_score + trend_score
    return min(total, 1.0)


_SCORERS = {
    'computed_results': score_0,
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
