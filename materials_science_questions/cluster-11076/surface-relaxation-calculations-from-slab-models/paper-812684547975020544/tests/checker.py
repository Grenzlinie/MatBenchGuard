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


# === block: score_0 (check id='exchange_energies') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold_table", {})
    tol_mag = step.get("tolerance_magnetic", 0.2)
    tol_para = step.get("tolerance_paramagnetic", 0.3)
    internal_w = step.get("internal_weights", {})
    mag_w = internal_w.get("magnetic", 0.06)
    para_w = internal_w.get("paramagnetic", 0.1)
    mag_elements = ["Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn"]
    art_map = {}
    for row in artifact:
        el = row.get("element","").strip()
        try:
            val = float(row.get("delta_E_eV", None))
        except:
            continue
        art_map[el] = val
    total_score = 0.0
    weight_total = 0.0
    for el in mag_elements:
        expected = gold.get(el)
        weight = mag_w
        if el in art_map:
            val = art_map[el]
            diff = abs(val - expected) if expected is not None else float('inf')
            s = max(0.0, 1.0 - diff / tol_mag)
        else:
            s = 0.0
        total_score += s * weight
        weight_total += weight
    if "Co_paramagnetic" in gold:
        expected = gold["Co_paramagnetic"]
        weight = para_w
        if "Co_paramagnetic" in art_map:
            val = art_map["Co_paramagnetic"]
            diff = abs(val - expected)
            s = max(0.0, 1.0 - diff / tol_para)
        else:
            s = 0.0
        total_score += s * weight
        weight_total += weight
    if weight_total == 0.0:
        return 0.0
    return total_score / weight_total


# === block: score_1 (check id='interaction_energies') ===
def score_1(artifact, step, ctx):
    gold_table = step.get("gold_table", [])
    tol = step.get("tolerance", 0.05)
    art_map = {}
    for row in artifact:
        el = row.get("element","").strip()
        pos = row.get("position","").strip()
        try:
            val = float(row.get("interaction_energy_eV", None))
        except:
            continue
        art_map[(el, pos)] = val
    total_score = 0.0
    count = 0
    for entry in gold_table:
        el = entry.get("element")
        pos = entry.get("position")
        expected = entry.get("interaction_energy_eV")
        key = (el, pos)
        if key in art_map:
            val = art_map[key]
            diff = abs(val - expected)
            s = max(0.0, 1.0 - diff / tol)
        else:
            s = 0.0
        total_score += s
        count += 1
    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'exchange_energies': score_0,
    'interaction_energies': score_1,
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
