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
    steps = spec.get("steps", [])
    main_config = None
    for step in steps:
        if step.get("id") == "results_main":
            main_config = step.get("config", {})
            break
    return {"main_config": main_config}


# === block: score_0 (check id='results_main') ===
def score_0(artifact, step, ctx):
    main_config = ctx.get("main_config", {})
    gold = main_config.get("gold_values", {})
    tol_ea = main_config.get("tolerances", {}).get("EA", 0.05)
    tol_gap = main_config.get("tolerances", {}).get("S_T_gap", 0.10)
    ha_to_ev = main_config.get("Ha_to_eV", 27.2114)
    trend_checks = main_config.get("trend_checks", [])

    molecules_list = artifact.get("molecules", [])
    mol_dict = {}
    for m in molecules_list:
        name = m.get("name", "").strip()
        if name:
            mol_dict[name] = m

    total_props = 0
    correct_props = 0
    for name, gold_vals in gold.items():
        mol = mol_dict.get(name)
        if mol is None:
            continue
        try:
            E_neut = float(mol.get("E_neutral", 0))
            ZPVE_neut = float(mol.get("ZPVE_neutral", 0))
            E_an = float(mol.get("E_anion", 0))
            ZPVE_an = float(mol.get("ZPVE_anion", 0))
            E_neut_an_geom = float(mol.get("E_neutral_at_anion_geom", 0))
            E_an_neut_geom = float(mol.get("E_anion_at_neutral_geom", 0))
            E_trip = float(mol.get("E_triplet", 0))
        except (ValueError, TypeError):
            continue

        ea_ad = (E_neut - E_an) * ha_to_ev
        ea_ad_zpve = ((E_neut + ZPVE_neut) - (E_an + ZPVE_an)) * ha_to_ev
        vea = (E_neut - E_an_neut_geom) * ha_to_ev
        vde = (E_neut_an_geom - E_an) * ha_to_ev
        st_gap = (E_trip - E_neut) * ha_to_ev

        computed = {
            "EA_ad": ea_ad,
            "EA_ad_ZPVE": ea_ad_zpve,
            "VEA": vea,
            "VDE": vde,
            "S_T_gap": st_gap
        }
        for prop in ["EA_ad", "EA_ad_ZPVE", "VEA", "VDE"]:
            total_props += 1
            if abs(computed[prop] - gold_vals[prop]) <= tol_ea:
                correct_props += 1
        total_props += 1
        if abs(computed["S_T_gap"] - gold_vals["S_T_gap"]) <= tol_gap:
            correct_props += 1

    property_score = correct_props / total_props if total_props > 0 else 0.0

    trend_score = 1.0
    if trend_checks:
        total_comparisons = 0
        correct_comparisons = 0
        for tc in trend_checks:
            ordered_names = tc.get("molecules_order", [])
            prop = tc.get("property", "")
            values = []
            for name in ordered_names:
                mol = mol_dict.get(name)
                if mol is None:
                    values.append(None)
                else:
                    v = mol.get(prop)
                    values.append(v)
            for i in range(len(values)-1):
                if values[i] is None or values[i+1] is None:
                    continue
                total_comparisons += 1
                try:
                    if float(values[i]) < float(values[i+1]):
                        correct_comparisons += 1
                except (ValueError, TypeError):
                    pass
        if total_comparisons > 0:
            trend_score = correct_comparisons / total_comparisons
        else:
            trend_score = 0.0
    else:
        trend_score = 1.0

    weight_prop = 0.8
    weight_trend = 0.2
    final_score = weight_prop * property_score + weight_trend * trend_score
    return final_score


# === block: score_1 (check id='results_structure') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    molecules = artifact.get("molecules")
    if not isinstance(molecules, list) or len(molecules) < 10:
        return 0.0
    required_fields = [
        "name", "E_neutral", "ZPVE_neutral", "E_anion", "ZPVE_anion",
        "E_neutral_at_anion_geom", "E_anion_at_neutral_geom", "E_triplet",
        "EA_ad", "EA_ad_ZPVE", "VEA", "VDE", "S_T_gap"
    ]
    for mol in molecules:
        if not isinstance(mol, dict):
            return 0.0
        for field in required_fields:
            if field not in mol:
                return 0.0
    return 1.0


_SCORERS = {
    'results_main': score_0,
    'results_structure': score_1,
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
