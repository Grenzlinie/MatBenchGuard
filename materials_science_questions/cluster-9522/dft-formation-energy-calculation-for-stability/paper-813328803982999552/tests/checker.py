import os
import json
import csv

# === author imports / helpers ===
import csv, os


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
        gold_binding = {}
        gold_formation = {}
        gold_dos = {}
        tolerances = {}
        for step in spec.get("steps", []):
            out_file = step.get("output_file", "")
            if step.get("kind") == "numeric":
                gold_list = step.get("gold", [])
                for item in gold_list:
                    carbide = item["carbide"]
                    val = float(item["value"])
                    if out_file == "binding_energies.csv":
                        gold_binding[carbide] = val
                    elif out_file == "formation_energies.csv":
                        gold_formation[carbide] = val
                    elif out_file == "dos_n_ef.csv":
                        gold_dos[carbide] = val
                tolerances[out_file] = step.get("tolerance", 0.0)
        ctx = {
            "gold_binding": gold_binding,
            "gold_formation": gold_formation,
            "gold_dos": gold_dos,
            "tolerances": tolerances,
        }
        return ctx


# === block: score_0 (check id='check_binding') ===
def score_0(artifact, step, ctx):
        gold_map = ctx["gold_binding"]
        tol = ctx["tolerances"].get("binding_energies.csv", 0.1)
        key_col = step.get("key_column", "carbide")
        val_col = step.get("field", "binding_energy_eV_per_atom")
        scores = []
        for row in artifact:
            carbide = row.get(key_col, "")
            if not carbide:
                continue
            try:
                val = float(row.get(val_col, 0))
            except (ValueError, TypeError):
                return 0.0
            gold = gold_map.get(carbide)
            if gold is None:
                scores.append(0.0)
                continue
            err = abs(val - gold)
            if err <= tol:
                scores.append(1.0)
            else:
                excess = err - tol
                score = max(0.0, 1.0 - excess / (2 * tol))
                scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='check_formation_values') ===
def score_1(artifact, step, ctx):
        gold_map = ctx["gold_formation"]
        tol = ctx["tolerances"].get("formation_energies.csv", 0.05)
        key_col = step.get("key_column", "carbide")
        val_col = step.get("field", "formation_energy_eV_per_atom")
        scores = []
        for row in artifact:
            carbide = row.get(key_col, "")
            if not carbide:
                continue
            try:
                val = float(row.get(val_col, 0))
            except (ValueError, TypeError):
                return 0.0
            gold = gold_map.get(carbide)
            if gold is None:
                scores.append(0.0)
                continue
            err = abs(val - gold)
            if err <= tol:
                scores.append(1.0)
            else:
                excess = err - tol
                score = max(0.0, 1.0 - excess / (2 * tol))
                scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_2 (check id='check_formation_ordering') ===
def score_2(artifact, step, ctx):
        formation_map = {}
        for row in artifact:
            carbide = row.get("carbide", "")
            if not carbide:
                continue
            try:
                val = float(row.get("formation_energy_eV_per_atom", 0))
            except (ValueError, TypeError):
                return 0.0
            formation_map[carbide] = val
        if "Fe2C" not in formation_map or "NbC" not in formation_map:
            return 0.0
        score = 0.0
        if formation_map["Fe2C"] > 0:
            score += 0.5
        all_vals = list(formation_map.values())
        if all_vals:
            min_val = min(all_vals)
            if formation_map.get("NbC") == min_val and all(formation_map.get("NbC") <= v for v in all_vals):
                score += 0.5
        return score


# === block: score_3 (check id='check_dos') ===
def score_3(artifact, step, ctx):
        gold_map = ctx["gold_dos"]
        tol = ctx["tolerances"].get("dos_n_ef.csv", 5.0)
        key_col = step.get("key_column", "carbide")
        val_col = step.get("field", "N_EF_electrons_per_eV")
        scores = []
        for row in artifact:
            carbide = row.get(key_col, "")
            if not carbide:
                continue
            try:
                val = float(row.get(val_col, 0))
            except (ValueError, TypeError):
                return 0.0
            gold = gold_map.get(carbide)
            if gold is None:
                scores.append(0.0)
                continue
            err = abs(val - gold)
            if err <= tol:
                scores.append(1.0)
            else:
                excess = err - tol
                score = max(0.0, 1.0 - excess / (2 * tol))
                scores.append(score)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


_SCORERS = {
    'check_binding': score_0,
    'check_formation_values': score_1,
    'check_formation_ordering': score_2,
    'check_dos': score_3,
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
