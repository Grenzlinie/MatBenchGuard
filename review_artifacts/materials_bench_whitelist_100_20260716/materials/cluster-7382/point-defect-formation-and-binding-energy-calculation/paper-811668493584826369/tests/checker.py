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
    return {}


# === block: score_0 (check id='ed_accuracy') ===
def score_0(artifact, step, ctx):
    systems = {
        "pristine": ("E_total_pristine_minus_H", "E_total_pristine"),
        "ti_na": ("E_total_Ti_Na_minus_H", "E_total_Ti_Na"),
        "na_vacancy": ("E_total_Na_vacancy_minus_H", "E_total_Na_vacancy"),
        "al_vacancy": ("E_total_Al_vacancy_minus_H", "E_total_Al_vacancy"),
    }
    gold_ed = step.get("gold_ed", {})
    tol = float(step.get("tolerance", 0.5))
    decay = float(step.get("decay", 1.0))
    total_score = 0.0
    count = 0
    for sys_name, (minus_h_key, intact_key) in systems.items():
        if minus_h_key not in artifact or intact_key not in artifact:
            continue
        ed = artifact[minus_h_key] - artifact[intact_key]
        target = gold_ed.get(sys_name)
        if target is None:
            continue
        error = abs(ed - target)
        if error <= tol:
            sub = 1.0
        else:
            sub = max(0.0, 1.0 - (error - tol) / decay)
        total_score += sub
        count += 1
    if count == 0:
        return 0.0
    return total_score / count


# === block: score_1 (check id='ordering') ===
def score_1(artifact, step, ctx):
    keys = [
        ("E_total_pristine_minus_H", "E_total_pristine"),
        ("E_total_Ti_Na_minus_H", "E_total_Ti_Na"),
        ("E_total_Al_vacancy_minus_H", "E_total_Al_vacancy"),
        ("E_total_Na_vacancy_minus_H", "E_total_Na_vacancy"),
    ]
    eds = []
    try:
        for minus_h_key, intact_key in keys:
            if minus_h_key not in artifact or intact_key not in artifact:
                return 0.0
            ed = artifact[minus_h_key] - artifact[intact_key]
            eds.append(ed)
    except Exception:
        return 0.0
    if len(eds) < 4:
        return 0.0
    if eds[0] > eds[1] > eds[2] > eds[3]:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='sign') ===
def score_2(artifact, step, ctx):
    systems = {
        "pristine": ("E_total_pristine_minus_H", "E_total_pristine"),
        "ti_na": ("E_total_Ti_Na_minus_H", "E_total_Ti_Na"),
        "na_vacancy": ("E_total_Na_vacancy_minus_H", "E_total_Na_vacancy"),
        "al_vacancy": ("E_total_Al_vacancy_minus_H", "E_total_Al_vacancy"),
    }
    sgn_map = step.get("signs", {})
    if "E_total_H2" not in artifact:
        return 0.0
    h2_energy = artifact["E_total_H2"]
    all_match = True
    for sys_name, (minus_h_key, intact_key) in systems.items():
        if minus_h_key not in artifact or intact_key not in artifact:
            all_match = False
            break
        ed = artifact[minus_h_key] - artifact[intact_key]
        ed_ref = ed + 0.5 * h2_energy
        expected_sign = sgn_map.get(sys_name)
        if expected_sign == "positive" and ed_ref <= 0:
            all_match = False
            break
        elif expected_sign == "negative" and ed_ref >= 0:
            all_match = False
            break
    return 1.0 if all_match else 0.0


_SCORERS = {
    'ed_accuracy': score_0,
    'ordering': score_1,
    'sign': score_2,
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
