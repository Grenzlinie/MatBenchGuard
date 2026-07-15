import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    gold_rows = []
    steps = spec.get("steps", [])
    for step in steps:
        if step.get("id") == "mo_table_contents":
            gold_rows = step.get("gold_table", [])
            break
    return {"gold_rows": gold_rows}


# === block: score_0 (check id='mo_table_contents') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx["gold_rows"]
    if not gold_rows:
        return 0.0

    # load and validate agent CSV
    csv_path = os.path.join("/app/outputs", step.get("output_file", "mo_energies_compositions.csv"))
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        agent_rows = list(reader)

    required_cols = ["MO", "epsilon_eV", "Pd_5s_pct", "Pd_5p_pct", "Pd_4d_pct", "Cl_3s_pct", "Cl_3p_pct", "region_II_pct", "region_III_pct", "photoionization_cross_section"]
    if not all(col in agent_rows[0] for col in required_cols):
        return 0.0

    # build agent lookup by MO
    agent_by_mo = {}
    for row in agent_rows:
        mo = row.get("MO").strip()
        try:
            entry = {
                "epsilon_eV": float(row["epsilon_eV"]),
                "Pd_5s_pct": float(row["Pd_5s_pct"]),
                "Pd_5p_pct": float(row["Pd_5p_pct"]),
                "Pd_4d_pct": float(row["Pd_4d_pct"]),
                "Cl_3s_pct": float(row["Cl_3s_pct"]),
                "Cl_3p_pct": float(row["Cl_3p_pct"]),
                "region_II_pct": float(row["region_II_pct"]),
                "region_III_pct": float(row["region_III_pct"]),
                "photoionization_cross_section": float(row["photoionization_cross_section"]),
            }
        except (ValueError, TypeError):
            continue
        agent_by_mo[mo] = entry

    EPS_EV_TOL = 0.2
    PCT_TOL = 5.0

    def cross_section_ok(agent_val, gold_val, rel_tol=0.05, abs_floor=0.02):
        if abs(gold_val) < 1e-9 and abs(agent_val) < 1e-9:
            return True
        if gold_val < 0.1 and gold_val >= 0.0:
            return abs(agent_val - gold_val) <= abs_floor
        rel_err = abs(agent_val - gold_val) / max(abs(gold_val), 1e-9)
        return rel_err <= rel_tol

    passed = 0
    for gold in gold_rows:
        mo = gold["MO"]
        agent = agent_by_mo.get(mo)
        if agent is None:
            continue
        ok = True
        if abs(agent["epsilon_eV"] - gold["epsilon_eV"]) > EPS_EV_TOL:
            ok = False
        for col in ["Pd_5s_pct", "Pd_5p_pct", "Pd_4d_pct", "Cl_3s_pct", "Cl_3p_pct", "region_II_pct", "region_III_pct"]:
            if abs(agent[col] - gold[col]) > PCT_TOL:
                ok = False
                break
        if not cross_section_ok(agent["photoionization_cross_section"], gold["photoionization_cross_section"]):
            ok = False
        if ok:
            passed += 1

    return passed / len(gold_rows) if gold_rows else 0.0


_SCORERS = {
    'mo_table_contents': score_0,
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
