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


# === block: score_0 (check id='check_relative_energies') ===
def score_0(artifact, step, ctx):
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    rel_tol = tolerances.get("relative_energy", 0.05)
    form_tol = tolerances.get("formation_energy", 0.5)
    field_scores = []
    for comp in ["Mg3Pd5","Al3Pd5","Ga3Pd5"]:
        comp_data = artifact.get(comp)
        exp_comp = expected.get(comp)
        if not isinstance(comp_data, dict) or not isinstance(exp_comp, dict):
            continue
        for key in ["conf1","conf2","conf3","conf4"]:
            val = comp_data.get(key)
            exp_val = exp_comp.get(key)
            if val is None or exp_val is None:
                field_scores.append(0.0)
                continue
            diff = abs(val - exp_val)
            s = max(0.0, 1.0 - diff / rel_tol)
            field_scores.append(s)
        f_val = comp_data.get("formation_energy_fu")
        f_exp = exp_comp.get("formation_energy_fu")
        if f_val is not None and f_exp is not None:
            diff = abs(f_val - f_exp)
            s = max(0.0, 1.0 - diff / form_tol)
            field_scores.append(s)
        else:
            field_scores.append(0.0)
    if not field_scores:
        return 0.0
    return sum(field_scores) / len(field_scores)


# === block: score_1 (check id='check_icohp') ===
def score_1(artifact, step, ctx):
    expected = step.get("expected", {})
    tolerances = step.get("tolerances", {})
    total_tol = tolerances.get("total_icohp_per_cell", 0.5)
    perc_tol = tolerances.get("percentage_contribution", 2.0)
    field_scores = []
    for comp in ["Mg3Pd5","Al3Pd5","Ga3Pd5"]:
        comp_data = artifact.get(comp)
        exp_comp = expected.get(comp)
        if not isinstance(comp_data, dict) or not isinstance(exp_comp, dict):
            continue
        for btype in ["A_A","A_Pd","Pd_Pd"]:
            bdata = comp_data.get(btype)
            exp_b = exp_comp.get(btype)
            if not isinstance(bdata, dict) or not isinstance(exp_b, dict):
                field_scores.append(0.0)
                continue
            val = bdata.get("total_icohp_per_cell")
            exp_val = exp_b.get("total_icohp_per_cell")
            if val is not None and exp_val is not None:
                diff = abs(val - exp_val)
                s = max(0.0, 1.0 - diff / total_tol)
                field_scores.append(s)
            else:
                field_scores.append(0.0)
            pval = bdata.get("percentage_contribution")
            pexp = exp_b.get("percentage_contribution")
            if pval is not None and pexp is not None:
                diff = abs(pval - pexp)
                s = max(0.0, 1.0 - diff / perc_tol)
                field_scores.append(s)
            else:
                field_scores.append(0.0)
    if not field_scores:
        return 0.0
    return sum(field_scores) / len(field_scores)


_SCORERS = {
    'check_relative_energies': score_0,
    'check_icohp': score_1,
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
