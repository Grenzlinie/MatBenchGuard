import os
import json
import csv

# === author imports / helpers ===
import json
import os
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
    path = os.path.join(outputs_dir, 'dft_results.json')
    if not os.path.exists(path):
        return {'artifact': None}
    with open(path) as f:
        artifact = json.load(f)
    return {'artifact': artifact}


# === block: score_0 (check id='reaction_delta_G') ===
def score_0(artifact, step, ctx):
            artifact = ctx.get('artifact')
            if artifact is None:
                return 0.0
            field = step.get('field', 'reaction_delta_G_kJ_per_mol')
            gold = float(step.get('gold', -374.16))
            tol_rel = float(step.get('tolerance_rel', 0.1))
            val = artifact.get(field)
            if val is None:
                return 0.0
            max_error = 2.0 * tol_rel * abs(gold)
            if max_error == 0:
                return 1.0 if abs(val - gold) < 1e-6 else 0.0
            score = max(0.0, 1.0 - abs(val - gold) / max_error)
            return float(round(score, 6))
        


# === block: score_1 (check id='homo_lumo') ===
def score_1(artifact, step, ctx):
            artifact = ctx.get('artifact')
            if artifact is None:
                return 0.0
            rubric = step.get('rubric', {})
            fields = rubric.get('fields', [])
            val_weight = rubric.get('value_weight', 0.6)
            ord_weight = rubric.get('ordering_weight', 0.4)
            total = 0.0
            count = 0
            for fspec in fields:
                name = fspec['name']
                gold = fspec['gold']
                tol_rel = fspec['tol_rel']
                val = artifact.get(name)
                if val is None:
                    continue
                max_err = 2.0 * tol_rel * abs(gold)
                if max_err == 0:
                    s = 1.0 if abs(val - gold) < 1e-6 else 0.0
                else:
                    s = max(0.0, 1.0 - abs(val - gold) / max_err)
                total += s
                count += 1
            val_score = total / max(count, 1)
            # ordering
            lumo_cn2 = artifact.get('LUMO_Li2CN2_eV')
            lumo_co3 = artifact.get('LUMO_Li2CO3_eV')
            lumo_lif = artifact.get('LUMO_LiF_eV')
            ord_score = 0.0
            if lumo_cn2 is not None and lumo_co3 is not None and lumo_lif is not None:
                if lumo_cn2 > lumo_co3 > lumo_lif:
                    ord_score = 1.0
                elif lumo_cn2 > lumo_lif and lumo_cn2 > lumo_co3:
                    ord_score = 0.5  # partial
            return float(round(val_weight * val_score + ord_weight * ord_score, 6))
        


# === block: score_2 (check id='li_adsorption') ===
def score_2(artifact, step, ctx):
            artifact = ctx.get('artifact')
            if artifact is None:
                return 0.0
            rubric = step.get('rubric', {})
            fields = rubric.get('fields', [])
            total = 0.0
            count = 0
            for fspec in fields:
                name = fspec['name']
                gold = fspec['gold']
                tol_rel = fspec['tol_rel']
                val = artifact.get(name)
                if val is None:
                    continue
                max_err = 2.0 * tol_rel * abs(gold)
                if max_err == 0:
                    s = 1.0 if abs(val - gold) < 1e-6 else 0.0
                else:
                    s = max(0.0, 1.0 - abs(val - gold) / max_err)
                total += s
                count += 1
            score = total / max(count, 1) if count else 0.0
            return float(round(score, 6))
        


# === block: score_3 (check id='interface_bulk') ===
def score_3(artifact, step, ctx):
            artifact = ctx.get('artifact')
            if artifact is None:
                return 0.0
            rubric = step.get('rubric', {})
            fields = rubric.get('fields', [])
            total = 0.0
            count = 0
            for fspec in fields:
                name = fspec['name']
                gold = fspec['gold']
                tol_rel = fspec['tol_rel']
                val = artifact.get(name)
                if val is None:
                    continue
                max_err = 2.0 * tol_rel * abs(gold)
                if max_err == 0:
                    s = 1.0 if abs(val - gold) < 1e-6 else 0.0
                else:
                    s = max(0.0, 1.0 - abs(val - gold) / max_err)
                total += s
                count += 1
            score = total / max(count, 1) if count else 0.0
            return float(round(score, 6))
        


# === block: score_4 (check id='gamma_E') ===
def score_4(artifact, step, ctx):
            artifact = ctx.get('artifact')
            if artifact is None:
                return 0.0
            config = step.get('config', {})
            materials = config.get('materials', ['Li2CN2', 'Li2CO3', 'LiF'])
            gold_gamma_E = config.get('gold_gamma_E', {})
            tol_rel = config.get('tol_rel', 0.1)
            ordering = config.get('ordering', '')
        
            # collect interfacial energies and bulk moduli
            score_items = []
            for mat in materials:
                gamma_f = f'interfacial_energy_{mat}_meV_per_A2'
                E_f = f'bulk_modulus_{mat}_GPa'
                gammaE_f = f'gamma_E_{mat}_meV_per_A2_GPa'
                gamma = artifact.get(gamma_f)
                E = artifact.get(E_f)
                agent_gammaE = artifact.get(gammaE_f)
                if None in (gamma, E, agent_gammaE):
                    continue
                recomputed = gamma * E
                # check consistency: agent's gammaE should be close to product
                if abs(recomputed) < 1e-12:
                    consistency = 1.0 if abs(agent_gammaE) < 1e-6 else 0.0
                else:
                    rel_err = abs(agent_gammaE - recomputed) / abs(recomputed)
                    consistency = max(0.0, 1.0 - rel_err / 0.05)  # within 5% full, degrade
            
                # check against gold gamma_E
                gold_ge = gold_gamma_E.get(mat)
                if gold_ge is not None:
                    max_err = 2.0 * tol_rel * abs(gold_ge)
                    if max_err == 0:
                        val_score = 1.0 if abs(agent_gammaE - gold_ge) < 1e-6 else 0.0
                    else:
                        val_score = max(0.0, 1.0 - abs(agent_gammaE - gold_ge) / max_err)
                else:
                    val_score = 0.0
                score_items.append(0.5 * consistency + 0.5 * val_score)
        
            gammaE_score = sum(score_items) / max(len(score_items), 1) if score_items else 0.0
        
            # trend: gamma_E_Li2CN2 should be highest
            trend_score = 0.0
            if all(artifact.get(f'gamma_E_{m}_meV_per_A2_GPa') is not None for m in materials):
                g_cn2 = artifact['gamma_E_Li2CN2_meV_per_A2_GPa']
                g_co3 = artifact['gamma_E_Li2CO3_meV_per_A2_GPa']
                g_lif = artifact['gamma_E_LiF_meV_per_A2_GPa']
                if g_cn2 > g_co3 and g_cn2 > g_lif:
                    trend_score = 1.0
                elif g_cn2 > g_lif or g_cn2 > g_co3:
                    trend_score = 0.5
        
            final = 0.7 * gammaE_score + 0.3 * trend_score
            return float(round(final, 6))
        


_SCORERS = {
    'reaction_delta_G': score_0,
    'homo_lumo': score_1,
    'li_adsorption': score_2,
    'interface_bulk': score_3,
    'gamma_E': score_4,
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
