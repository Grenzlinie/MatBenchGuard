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


# === block: score_0 (check id='numeric_accuracy') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    data = artifact
    pass_count = 0
    total = 0

    # Mn2(CO)10_rt
    if "Mn2(CO)10_rt" in data:
        for k, v in gold["Mn2(CO)10_rt"].items():
            if k in data["Mn2(CO)10_rt"]:
                val = data["Mn2(CO)10_rt"][k]
                if isinstance(val, (int, float)):
                    if abs(val - v) <= tol:
                        pass_count += 1
                total += 1

    # Ir6(CO)16_black
    if "Ir6(CO)16_black" in data:
        black_data = data["Ir6(CO)16_black"]
        black_gold = gold["Ir6(CO)16_black"]
        # O–O and O–C per molecule if possible
        if "molecules" in black_data and isinstance(black_data["molecules"], list) and "molecules" in black_gold and isinstance(black_gold["molecules"], list):
            gold_mols = black_gold["molecules"]
            if len(black_data["molecules"]) == len(gold_mols):
                for i, gmol in enumerate(gold_mols):
                    amol = black_data["molecules"][i]
                    for k, v in gmol.items():
                        if k in ("IAM_C_C_rep", "IAM_C_C_attr"):
                            continue  # skip split C–C check
                        if k in amol:
                            val = amol[k]
                            if isinstance(val, (int, float)):
                                if abs(val - v) <= tol:
                                    pass_count += 1
                            total += 1
        # total C–C intra from all molecules compared to single gold total
        if "IAM_C_C_total" in black_gold:
            total_cc_artifact = 0.0
            if "molecules" in black_data and isinstance(black_data["molecules"], list):
                for mol in black_data["molecules"]:
                    total_cc_artifact += mol.get("IAM_C_C_rep", 0) + mol.get("IAM_C_C_attr", 0)
            if abs(total_cc_artifact - black_gold["IAM_C_C_total"]) <= tol:
                pass_count += 1
            total += 1

    # Ir6(CO)16_red
    if "Ir6(CO)16_red" in data:
        for k, v in gold["Ir6(CO)16_red"].items():
            if k in data["Ir6(CO)16_red"]:
                val = data["Ir6(CO)16_red"][k]
                if isinstance(val, (int, float)):
                    if abs(val - v) <= tol:
                        pass_count += 1
                total += 1

    score = pass_count / total if total else 0.0
    return score


# === block: score_1 (check id='trend_IEM') ===
def score_1(artifact, step, ctx):
    data = artifact

    try:
        red_iem = data["Ir6(CO)16_red"]["IEM"]
        black_mols = data["Ir6(CO)16_black"]["molecules"]
        total_black_iem = sum(mol["IEM"] for mol in black_mols)
        return 1.0 if total_black_iem < red_iem else 0.0
    except (KeyError, TypeError, IndexError):
        return 0.0


# === block: score_2 (check id='trend_IAM') ===
def score_2(artifact, step, ctx):
    data = artifact

    try:
        red = data["Ir6(CO)16_red"]
        red_iam = red["IAM_O_O"] + red["IAM_O_C"] + red["IAM_C_C"]
        black_mols = data["Ir6(CO)16_black"]["molecules"]
        mol_iams = []
        for mol in black_mols:
            iam = mol["IAM_O_O"] + mol["IAM_O_C"] + mol["IAM_C_C_rep"] + mol["IAM_C_C_attr"]
            mol_iams.append(iam)
        avg_black = sum(mol_iams) / len(mol_iams)
        return 1.0 if red_iam < avg_black else 0.0
    except (KeyError, TypeError, IndexError, ZeroDivisionError):
        return 0.0


_SCORERS = {
    'numeric_accuracy': score_0,
    'trend_IEM': score_1,
    'trend_IAM': score_2,
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
