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
    return {}


# === block: score_0 (check id='qtaim_bcps') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerances', {})
    gold_interactions = step.get('gold_interactions', [])
    if not gold_interactions:
        return 1.0
    by_key = {}
    for entry in artifact.get('entries', artifact) if isinstance(artifact, dict) else artifact:
        if not isinstance(entry, dict):
            continue
        k = (entry.get('molecule'), entry.get('interaction'))
        by_key[k] = entry

    count = len(gold_interactions)
    score_sum = 0.0
    for g in gold_interactions:
        k = (g['molecule'], g['interaction'])
        a = by_key.get(k)
        if a is None:
            continue
        ok = True
        for field, rtol in [('bond_path_RX', tol.get('bond_path_R', 0.10)),
                             ('bond_path_RY', tol.get('bond_path_R', 0.10)),
                             ('rho_b', tol.get('rho_b', 0.10)),
                             ('laplacian_rho', tol.get('laplacian_rho', 0.10)),
                             ('ellipticity', tol.get('ellipticity', 0.20)),
                             ('Vr', tol.get('Vr', 0.15)),
                             ('Gr', tol.get('Gr', 0.15))]:
            gold_val = g[field]
            agent_val = a.get(field)
            if agent_val is None:
                ok = False
                break
            if abs(gold_val) < 1e-12:
                if abs(agent_val) > 1e-9:
                    ok = False
                    break
            else:
                if abs(agent_val - gold_val) > rtol * abs(gold_val):
                    ok = False
                    break
        if ok:
            score_sum += 1.0
    return score_sum / count if count > 0 else 1.0


# === block: score_1 (check id='hirshfeld_results') ===
def score_1(artifact, step, ctx):
    gold_contacts = step.get('gold_contact_percentages', {})
    abs_tol = step.get('contact_tolerance_abs', 2.0)
    gold_energies = step.get('gold_interaction_energies', [])
    energy_rtol = step.get('energy_relative_tol', 0.10)

    artifact = artifact if isinstance(artifact, dict) else {}
    contact_scores = {}
    for mol in ['8', '9a', '9b']:
        mol_data = artifact.get(mol)
        if mol_data is None:
            contact_scores[mol] = 0.0
            continue
        perc = mol_data.get('contact_percentages')
        gold = gold_contacts.get(mol)
        if perc is None or gold is None:
            contact_scores[mol] = 0.0
            continue
        ok = 0
        for key in ['HH', 'CH', 'NH']:
            g = gold.get(key)
            a = perc.get(key)
            if a is not None and abs(a - g) <= abs_tol:
                ok += 1
        contact_scores[mol] = ok / 3.0
    contacts_total = sum(contact_scores.values()) / 3.0

    energy_score_total = 0.0
    energy_count = len(gold_energies)
    if energy_count > 0:
        for gold in gold_energies:
            polym = gold['polymorph']
            symop = gold['symop_AB']
            R_gold = gold['R_AB']
            mol_entries = artifact.get(polym, {}).get('interaction_energies', [])
            match = None
            for entry in mol_entries:
                if entry.get('symop_AB', '').replace(' ', '') != symop.replace(' ', ''):
                    continue
                R_agent = entry.get('R_AB')
                if R_agent is None:
                    continue
                if abs(R_agent - R_gold) <= 0.1:
                    match = entry
                    break
            if match is None:
                continue
            ok = True
            for field in ['E_ele', 'E_pol', 'E_dis', 'E_rep', 'E_tot']:
                g_val = gold[field]
                a_val = match.get(field)
                if a_val is None:
                    ok = False
                    break
                if abs(g_val) < 1e-6:
                    if abs(a_val) > 1e-3:
                        ok = False
                        break
                else:
                    if abs(a_val - g_val) > energy_rtol * abs(g_val):
                        ok = False
                        break
            if ok:
                energy_score_total += 1.0
        energy_score = energy_score_total / energy_count
    else:
        energy_score = 1.0

    return 0.5 * contacts_total + 0.5 * energy_score


_SCORERS = {
    'qtaim_bcps': score_0,
    'hirshfeld_results': score_1,
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
