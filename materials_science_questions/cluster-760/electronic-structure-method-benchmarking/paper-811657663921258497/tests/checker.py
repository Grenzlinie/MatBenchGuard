import os
import json
import csv

# === author imports / helpers ===
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
        ctx = {}
        import csv
        step01 = None
        for step in spec.get("steps", []):
            if step["id"] == "step_01_geometries":
                step01 = step
                break
        if step01:
            gold_rows = step01.get("gold_rows", [])
            geom_gold = {}
            for row in gold_rows:
                key = (str(row["reaction"]).strip(), row["functional"].strip().upper())
                geom_gold[key] = row
            ctx["geom_gold"] = geom_gold
            ctx["geom_tol"] = step01.get("tolerances", {})
        step03 = None
        for step in spec.get("steps", []):
            if step["id"] == "step_03_energies":
                step03 = step
                break
        if step03:
            gold_rxn = step03.get("gold_per_reaction", {})
            ctx["energy_gold"] = gold_rxn
            ctx["energy_tol"] = step03.get("tolerances", {})
        return ctx


# === block: score_0 (check id='step_01_geometries') ===
def score_0(artifact, step, ctx):
            if not artifact:
                return 0.0
            gold_rows = step.get("gold_rows", [])
            tolerances = step.get("tolerances", {})
            if not gold_rows:
                return 0.0
            required_cols = ["reaction", "functional", "Cl_H", "H_C", "Cl_C", "imag_freq"]
            if not all(col in artifact[0] for col in required_cols):
                return 0.0
            # Build gold map from gold_rows
            geom_gold = {}
            for row in gold_rows:
                key = (str(row["reaction"]).strip(), row["functional"].strip().upper())
                geom_gold[key] = row
            total_expected = len(geom_gold) * 4  # 4 numeric fields per reaction
            if total_expected == 0:
                return 0.0
            agent_map = {}
            for row in artifact:
                key = (str(row.get("reaction","")).strip(), str(row.get("functional","")).strip().upper())
                agent_map[key] = row
            correct = 0
            for gold_key, gold in geom_gold.items():
                if gold_key not in agent_map:
                    continue
                ag = agent_map[gold_key]
                for field in ["Cl_H", "H_C", "Cl_C", "imag_freq"]:
                    try:
                        av = float(ag.get(field, None))
                        gv = float(gold[field])
                        tol = tolerances.get(field, 0.0)
                        if abs(av - gv) <= tol:
                            correct += 1
                    except (ValueError, TypeError):
                        pass
            return correct / float(total_expected)


# === block: score_1 (check id='step_03_energies') ===
def score_1(artifact, step, ctx):
            if not artifact:
                return 0.0
            gold_rxn = ctx.get("energy_gold", {})
            tolerances = ctx.get("energy_tol", {})
            if not gold_rxn:
                return 0.0
            required_cols = ["reaction", "method", "basis", "barrier", "reaction_energy"]
            if not all(col in artifact[0] for col in required_cols):
                return 0.0
            total = len(artifact) * 2  # barrier and reaction_energy per row
            if total == 0:
                return 0.0
            correct = 0
            for row in artifact:
                rxn = str(row.get("reaction", "")).strip()
                if rxn not in gold_rxn:
                    continue
                gold = gold_rxn[rxn]
                for field in ["barrier", "reaction_energy"]:
                    try:
                        av = float(row.get(field, None))
                        gv = float(gold[field])
                        tol = tolerances.get(field, 0.0)
                        if abs(av - gv) <= tol:
                            correct += 1
                    except (ValueError, TypeError):
                        pass
            return correct / float(total)
    


_SCORERS = {
    'step_01_geometries': score_0,
    'step_03_energies': score_1,
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
