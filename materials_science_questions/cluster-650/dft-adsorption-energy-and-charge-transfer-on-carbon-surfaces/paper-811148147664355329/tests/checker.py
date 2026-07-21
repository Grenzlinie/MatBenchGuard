import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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
    return {"gold_table": spec["steps"][0]["gold_table"], "tolerances": spec["steps"][0]["tolerances"]}


# === block: score_0 (check id='results_table_check') ===
def score_0(artifact, step, ctx):
    agent_data = {}
    for row in artifact:
        sys = row.get("system", "").strip()
        if sys:
            agent_data[sys] = row

    gold_table = ctx["gold_table"]
    tolerances = ctx["tolerances"]
    # Use a wider tolerance for HOMO-LUMO gaps to account for DFT code/basis-set differences.
    e_g_tol = max(tolerances.get("E_g", 0.05), 0.15)  # ensure tolerance is at least 0.15 eV
    num_correct = 0
    for gold in gold_table:
        sys = gold["system"]
        if sys in agent_data:
            row = agent_data[sys]
            try:
                e_ads = float(row["E_ads"])
                e_g = float(row["E_g"])
                ct = float(row["charge_transfer"])
                within = (abs(e_ads - gold["E_ads"]) <= tolerances["E_ads"] and
                          abs(e_g - gold["E_g"]) <= e_g_tol and
                          abs(ct - gold["charge_transfer"]) <= tolerances["charge_transfer"])
                if within:
                    num_correct += 1
            except (ValueError, KeyError):
                pass
    acc = num_correct / len(gold_table) if gold_table else 0.0

    # Ordering check: expect E_ads(HCN_A) < E_ads(NO_A) < E_ads(CO_A) on isomer-1
    ordering_score = 0.0
    required = ["isomer1_CO_A", "isomer1_NO_A", "isomer1_HCN_A"]
    if all(s in agent_data for s in required):
        try:
            co = float(agent_data["isomer1_CO_A"]["E_ads"])
            no = float(agent_data["isomer1_NO_A"]["E_ads"])
            hcn = float(agent_data["isomer1_HCN_A"]["E_ads"])
            if hcn < no < co:
                ordering_score = 1.0
            elif hcn < no or no < co:
                ordering_score = 0.5
            else:
                ordering_score = 0.0
        except (ValueError, KeyError):
            pass

    total = min(1.0, 0.8 * acc + 0.2 * ordering_score)
    return total


_SCORERS = {
    'results_table_check': score_0,
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
