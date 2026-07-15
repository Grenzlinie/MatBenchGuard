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


# === block: score_0 (check id='step_03_table') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get('gold_rows', [])
    tols = step.get('tolerances', {})
    tol_dist_pa = float(tols.get('distance_Angstrom', {}).get('PA', 0.2))
    tol_dist_ca = float(tols.get('distance_Angstrom', {}).get('CA', 0.1))
    tol_energy = float(tols.get('adsorption_energy_kcal_mol', 5.0))
    tol_charge = float(tols.get('charge_transfer', 0.05))
    tol_disp = float(tols.get('displacement_Angstrom', 0.2))

    def _parse_float(s):
        if s is None or str(s).strip() == '':
            return None
        try:
            return float(s)
        except:
            return None

    if not isinstance(artifact, list):
        return 0.0

    # group gold rows by radical
    gold_by_fr = {}
    for g in gold_rows:
        fr = str(g.get('fr','')).strip()
        gold_by_fr.setdefault(fr, []).append(g)
    # sort each group by distance
    for fr, rows in gold_by_fr.items():
        rows.sort(key=lambda g: float(g.get('distance_Angstrom', 0.0)))

    # group agent rows by radical
    agent_by_fr = {}
    for row in artifact:
        fr = str(row.get('fr','')).strip()
        agent_by_fr.setdefault(fr, []).append(row)

    total_checks = 0
    passed_checks = 0

    for fr, gold_list in gold_by_fr.items():
        agent_list = agent_by_fr.get(fr, [])
        # sort agent rows by distance (None distances go to end by using large number)
        agent_list.sort(key=lambda r: _parse_float(r.get('distance_Angstrom', None)) if _parse_float(r.get('distance_Angstrom', None)) is not None else float('inf'))
        for i, g in enumerate(gold_list):
            # pair gold row with corresponding sorted agent row
            agent_row = agent_list[i] if i < len(agent_list) else None

            gold_dist = float(g.get('distance_Angstrom', 0))
            is_ca = (gold_dist < 2.0)
            dist_tol = tol_dist_ca if is_ca else tol_dist_pa

            # distance
            total_checks += 1
            ag_dist = _parse_float(agent_row.get('distance_Angstrom', None) if agent_row else None)
            if ag_dist is not None and abs(ag_dist - gold_dist) <= dist_tol:
                passed_checks += 1

            # energy
            total_checks += 1
            gold_energy = float(g.get('adsorption_energy_kcal_mol', 0))
            ag_energy = _parse_float(agent_row.get('adsorption_energy_kcal_mol', None) if agent_row else None)
            if ag_energy is not None and abs(ag_energy - gold_energy) <= tol_energy:
                passed_checks += 1

            # charge transfer
            total_checks += 1
            gold_charge = float(g.get('charge_transfer', 0))
            ag_charge = _parse_float(agent_row.get('charge_transfer', None) if agent_row else None)
            if ag_charge is not None and abs(ag_charge - gold_charge) <= tol_charge:
                passed_checks += 1

            # displacement
            total_checks += 1
            gold_disp_str = str(g.get('displacement_Angstrom', '')).strip()
            if gold_disp_str == '' or gold_disp_str == 'None':
                # PA: displacement must be empty
                ag_disp_raw = agent_row.get('displacement_Angstrom', None) if agent_row else None
                ag_disp_val = str(ag_disp_raw).strip() if ag_disp_raw is not None else ''
                if ag_disp_val == '' or ag_disp_val == 'None':
                    passed_checks += 1
            else:
                gold_disp = float(gold_disp_str)
                ag_disp = _parse_float(agent_row.get('displacement_Angstrom', None) if agent_row else None)
                if ag_disp is not None and abs(ag_disp - gold_disp) <= tol_disp:
                    passed_checks += 1

    score = passed_checks / total_checks if total_checks > 0 else 0.0
    return score


_SCORERS = {
    'step_03_table': score_0,
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
