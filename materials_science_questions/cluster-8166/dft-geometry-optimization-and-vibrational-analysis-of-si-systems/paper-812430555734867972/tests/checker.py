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


# === block: score_0 (check id='dft_results_score') ===
def score_0(artifact, step, ctx):
        gold_rows = step["config"]["gold_table"]
        gold_lookup = {}
        for gr in gold_rows:
            key = (int(gr["model"]), gr["state"])
            gold_lookup[key] = gr

        energy_tol = float(step["config"].get("energy_tol", 1.5))
        bond_tol   = float(step["config"].get("bond_tol", 0.02))
        angle_tol  = float(step["config"].get("angle_tol", 2.0))

        agent_data = {}
        correct_count = 0
        total_gold = len(gold_rows)  # 12

        for row in artifact:
            row = {k.strip(): v for k, v in row.items()}
            try:
                model = int(row["model"])
                state = row["state"]
            except (ValueError, KeyError):
                continue
            key = (model, state)
            agent_data[key] = row
            gold = gold_lookup.get(key)
            if gold is None:
                continue
            ok = True
            try:
                energy    = float(row["relative_energy_kcal_mol"])
                nb_h      = float(row["Nb_H_A"])
                cendo_h   = float(row["Cendo_H_A"])
                cc        = float(row["C_C_A"])
                nb_cexo   = float(row["Nb_Cexo_A"])
                inter_ring = float(row["inter_ring_angle_deg"])
            except (ValueError, KeyError):
                ok = False
            if ok:
                if abs(energy - float(gold["energy"])) > energy_tol:
                    ok = False
                elif abs(nb_h - float(gold["Nb_H"])) > bond_tol:
                    ok = False
                elif abs(cendo_h - float(gold["Cendo_H"])) > bond_tol:
                    ok = False
                elif abs(cc - float(gold["C_C"])) > bond_tol:
                    ok = False
                elif abs(nb_cexo - float(gold["Nb_Cexo"])) > bond_tol:
                    ok = False
                elif abs(inter_ring - float(gold["inter_ring"])) > angle_tol:
                    ok = False
            if ok:
                correct_count += 1

        row_fraction = correct_count / total_gold if total_gold > 0 else 0.0

        ordering_pass = 0.0
        if (7, "b") in agent_data and (6, "b") in agent_data and (8, "b") in agent_data \
           and (7, "c") in agent_data and (6, "c") in agent_data and (8, "c") in agent_data:
            try:
                e7b = float(agent_data[(7, "b")]["relative_energy_kcal_mol"])
                e6b = float(agent_data[(6, "b")]["relative_energy_kcal_mol"])
                e8b = float(agent_data[(8, "b")]["relative_energy_kcal_mol"])
                e7c = float(agent_data[(7, "c")]["relative_energy_kcal_mol"])
                e6c = float(agent_data[(6, "c")]["relative_energy_kcal_mol"])
                e8c = float(agent_data[(8, "c")]["relative_energy_kcal_mol"])
                if e7b < e6b and e7b < e8b and e7c < e6c and e7c < e8c:
                    ordering_pass = 1.0
            except (ValueError, KeyError):
                pass

        weight_row = 0.8
        weight_ord = 0.2
        score = weight_row * row_fraction + weight_ord * ordering_pass
        return score


_SCORERS = {
    'dft_results_score': score_0,
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
