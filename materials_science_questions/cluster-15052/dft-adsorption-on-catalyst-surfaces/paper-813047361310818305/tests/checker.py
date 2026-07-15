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
    return {}


# === block: score_0 (check id='step_01_pristine') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        w_band = 0.05
        w_geom = 0.65
        w_order = 0.30
        score_val = 0.0
        # Band gap
        slab = artifact.get('pristine_slab', {})
        if isinstance(slab, dict):
            bg = slab.get('band_gap_eV')
            if bg is not None and abs(bg - step['gold_band_gap']) <= step['tolerance_band_gap']:
                score_val += w_band
        # Adsorption list
        ads = artifact.get('adsorption', [])
        if not isinstance(ads, list) or len(ads) < 3:
            return score_val
        # Map by molecule
        mol_map = {}
        for entry in ads:
            if isinstance(entry, dict) and 'molecule' in entry:
                mol_map[entry['molecule']] = entry
        gold_mols = step['gold_molecules']
        tol_len = step['tolerance_length']
        tol_ang = step['tolerance_angle']
        tol_dq = step['tolerance_deltaQ']
        n_correct = 0
        n_checks = 0
        for g in gold_mols:
            mol = g['molecule']
            entry = mol_map.get(mol)
            if not entry:
                n_checks += 5; continue
            # site
            if entry.get('site') == g['site']:
                n_correct += 1
            n_checks += 1
            # lengths
            lengths = entry.get('bond_lengths_ang', [])
            gold_lens = g['bond_lengths']
            if len(lengths) == len(gold_lens):
                if all(abs(a - b) <= tol_len for a, b in zip(lengths, gold_lens)):
                    n_correct += 1
            n_checks += 1
            # angle
            ang = entry.get('bond_angle_deg')
            if ang is not None and abs(ang - g['bond_angle']) <= tol_ang:
                n_correct += 1
            n_checks += 1
            # delta_Q
            dq = entry.get('delta_Q_e')
            if dq is not None and abs(dq - g['delta_Q']) <= tol_dq:
                n_correct += 1
            n_checks += 1
        if n_checks:
            score_val += w_geom * (n_correct / n_checks)
        # Adsorption energy ordering
        e_ads = {}
        for mol, entry in mol_map.items():
            val = entry.get('E_ads_eV')
            if isinstance(val, (int, float)):
                e_ads[mol] = val
        if len(e_ads) == 3:
            order = step.get('ads_ordering', [])
            if order and len(order) == 3:
                vals = {m: abs(e_ads[m]) for m in order}
                sorted_order = sorted(order, key=lambda m: vals[m], reverse=True)
                if sorted_order == order:
                    score_val += w_order
        return min(score_val, 1.0)


# === block: score_1 (check id='step_02_doped') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        w_band = 0.10
        w_geom = 0.50
        w_order = 0.40
        score_val = 0.0
        # Doped slabs band gaps
        slabs = artifact.get('doped_slabs', [])
        gold_slabs = step.get('gold_doped_slabs', [])
        tol_bg = step['tolerance_band_gap']
        n_bg = 0
        for gs in gold_slabs:
            dop = gs['dopant']
            tgt = gs['band_gap_eV']
            for s in slabs:
                if isinstance(s, dict) and s.get('dopant') == dop:
                    val = s.get('band_gap_eV')
                    if val is not None and abs(val - tgt) <= tol_bg:
                        n_bg += 1
                    break
        if len(gold_slabs):
            score_val += w_band * (n_bg / len(gold_slabs))
        # Adsorption
        ads = artifact.get('adsorption', [])
        if not isinstance(ads, list):
            return score_val
        gold_ads = step.get('gold_adsorption', {})
        tol_len = step['tolerance_length']
        tol_ang = step['tolerance_angle']
        tol_dq = step['tolerance_deltaQ']
        n_correct = 0
        n_checks = 0
        for dopant, mols in gold_ads.items():
            for mol, g in mols.items():
                entry = None
                for a in ads:
                    if a.get('dopant') == dopant and a.get('molecule') == mol:
                        entry = a
                        break
                if not entry:
                    n_checks += 5; continue
                # site
                n_checks += 1
                # lengths
                lengths = entry.get('bond_lengths_ang', [])
                gold_lens = g['bond_lengths']
                if len(lengths) == len(gold_lens):
                    if all(abs(a - b) <= tol_len for a, b in zip(lengths, gold_lens)):
                        n_correct += 1
                n_checks += 1
                # angle
                ang = entry.get('bond_angle_deg')
                if ang is not None and abs(ang - g['bond_angle']) <= tol_ang:
                    n_correct += 1
                n_checks += 1
                # delta_Q
                dq = entry.get('delta_Q_e')
                if dq is not None and abs(dq - g['delta_Q']) <= tol_dq:
                    n_correct += 1
                n_checks += 1
        if n_checks:
            score_val += w_geom * (n_correct / n_checks)
        # Adsorption energy ordering per dopant (H2S > H2O > CO2)
        ordering = step.get('ads_ordering', [])
        if ordering and len(ordering) == 3:
            e_map = {}
            for a in ads:
                dop = a.get('dopant')
                mol = a.get('molecule')
                e = a.get('E_ads_eV')
                if dop and mol and isinstance(e, (int, float)):
                    e_map.setdefault(dop, {})[mol] = e
            n_order_ok = 0
            n_dopants = 0
            for dop, mol_vals in e_map.items():
                if all(m in mol_vals for m in ordering):
                    vals = {m: abs(mol_vals[m]) for m in ordering}
                    sorted_order = sorted(ordering, key=lambda m: vals[m], reverse=True)
                    if sorted_order == ordering:
                        n_order_ok += 1
                    n_dopants += 1
            if n_dopants:
                score_val += w_order * (n_order_ok / n_dopants)
        return min(score_val, 1.0)


# === block: score_2 (check id='step_03_field') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        w_order = 0.60
        w_sign = 0.40
        score_val = 0.0
        data = artifact.get('electric_field_adsorption', [])
        if not isinstance(data, list) or not data:
            return 0.0
        # Group by (dopant, field_strength) -> list of (molecule, E_ads, delta_Q)
        groups = {}
        for item in data:
            dop = item.get('dopant')
            f = item.get('field_strength')
            mol = item.get('molecule')
            e = item.get('E_ads_eV')
            dq = item.get('delta_Q_e')
            if None in (dop, f, mol, e, dq):
                continue
            groups.setdefault((dop, f), []).append((mol, e, dq))
        # Ordering check only for Mo and W
        order_dops = step.get('ordering_dopants', [])
        order_mols = step.get('ordering_molecules', [])
        n_order_total = 0
        n_order_ok = 0
        for (dop, f), items in groups.items():
            if dop not in order_dops:
                continue
            mol_vals = {m: e for m, e, dq in items}
            if all(m in mol_vals for m in order_mols):
                vals = {m: abs(mol_vals[m]) for m in order_mols}
                sorted_order = sorted(order_mols, key=lambda m: vals[m], reverse=True)
                if sorted_order == order_mols:
                    n_order_ok += 1
                n_order_total += 1
        if n_order_total:
            score_val += w_order * (n_order_ok / n_order_total)
        # Sign check for CO2 charge
        sign_co2 = step.get('sign_co2', {})
        n_sign_total = 0
        n_sign_ok = 0
        for item in data:
            if item.get('molecule') != 'CO2':
                continue
            dop = item.get('dopant')
            dq = item.get('delta_Q_e')
            if dop not in sign_co2 or dq is None:
                continue
            exp = sign_co2[dop]  # 'positive' or 'negative'
            n_sign_total += 1
            if exp == 'positive' and dq > 0:
                n_sign_ok += 1
            elif exp == 'negative' and dq < 0:
                n_sign_ok += 1
        if n_sign_total:
            score_val += w_sign * (n_sign_ok / n_sign_total)
        return min(score_val, 1.0)


_SCORERS = {
    'step_01_pristine': score_0,
    'step_02_doped': score_1,
    'step_03_field': score_2,
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
