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
    import csv, json

    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        ctx = {}
        for step in steps:
            sid = step["id"]
            if sid == "equilibrium_positions":
                tol_rho = step.get("tolerance_rho", 0.01)
                ys = step.get("ys", [2,5,10,50,100])
                gold_compact = step.get("gold_compact", [])
                equil_rows = []
                for entry in gold_compact:
                    case = entry["case"]
                    phi = entry["phi"]
                    alpha = entry["alpha"]
                    rho = entry["rho"]
                    stab = entry["stability"]
                    char = entry["character"]
                    for y in ys:
                        equil_rows.append({
                            "case": case,
                            "phi": phi,
                            "alpha": alpha,
                            "y": y,
                            "rho": rho,
                            "stability": stab,
                            "character": char
                        })
                ctx["expected_equilibrium_rows"] = equil_rows
                ctx["tol_rho"] = tol_rho
            elif sid == "binding_energies":
                tol_Ub = step.get("tolerance_Ub", 0.02)
                gold_binding = step.get("gold_binding", [])
                ctx["expected_binding_rows"] = [dict(e) for e in gold_binding]
                ctx["tol_Ub"] = tol_Ub
        return ctx


# === block: score_0 (check id='equilibrium_positions') ===
def score_0(artifact, step, ctx):
    rows = artifact
    expected = ctx["expected_equilibrium_rows"]
    tol = ctx["tol_rho"]
    matched = 0
    total = len(expected)
    if total == 0:
        return 0.0
    for exp in expected:
        for r in rows:
            try:
                a_case = str(r.get("case",""))
                a_phi = int(float(r.get("phi","0")))
                a_alpha = int(float(r.get("alpha","0")))
                a_y = int(float(r.get("y","0")))
            except:
                continue
            if (a_case == exp["case"] and a_phi == exp["phi"] and a_alpha == exp["alpha"] and a_y == exp["y"]):
                try:
                    agent_rho = float(r.get("rho","0"))
                except:
                    break
                if (abs(agent_rho - exp["rho"]) <= tol and
                    r.get("stability","") == exp["stability"] and
                    r.get("character","") == exp["character"]):
                    matched += 1
                break
    return matched / total


# === block: score_1 (check id='binding_energies') ===
def score_1(artifact, step, ctx):
    rows = artifact
    expected = ctx["expected_binding_rows"]
    tol = ctx["tol_Ub"]
    matched = 0
    total = len(expected)
    if total == 0:
        return 0.0
    for exp in expected:
        for r in rows:
            try:
                a_case = str(r.get("case",""))
                a_phi = int(float(r.get("phi","0")))
                a_alpha = int(float(r.get("alpha","0")))
                a_y = int(float(r.get("y","0")))
            except:
                continue
            if (a_case == exp["case"] and a_phi == exp["phi"] and a_alpha == exp["alpha"] and a_y == exp["y"]):
                try:
                    agent_Ub = float(r.get("Ub","0"))
                except:
                    break
                if abs(agent_Ub - exp["Ub"]) <= tol:
                    matched += 1
                break
    return matched / total


_SCORERS = {
    'equilibrium_positions': score_0,
    'binding_energies': score_1,
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
