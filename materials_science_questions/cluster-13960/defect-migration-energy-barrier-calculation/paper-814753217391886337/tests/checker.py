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
    steps = spec.get("steps", [])
    step_mig = None
    for s in steps:
        if s.get("id") == "migration_barriers":
            step_mig = s
            break
    if step_mig is None:
        raise ValueError("step not found")
    return {"step": step_mig}


# === block: score_0 (check id='migration_barriers') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    step = ctx["step"]
    if artifact is None:
        return 0.0
    required_cols = ["Cr_count","migrating_atom","initial_energy","saddle_energy","final_energy","migration_barrier"]
    header = artifact[0].keys() if artifact else []
    for col in required_cols:
        if col not in header:
            return 0.0
    total_rows = len(artifact)
    expected_rows = 43
    shape_score = 1.0 if total_rows == expected_rows else 0.0
    rows_fe = []
    rows_cr = []
    for row in artifact:
        try:
            cr = int(row["Cr_count"])
            mig = row["migrating_atom"].strip()
            ini = float(row["initial_energy"])
            sad = float(row["saddle_energy"])
            fin = float(row["final_energy"])
            barr = float(row["migration_barrier"])
        except (ValueError, KeyError):
            return 0.0
        if mig == "Fe":
            rows_fe.append((cr, ini, sad, fin, barr))
        elif mig == "Cr":
            rows_cr.append((cr, ini, sad, fin, barr))
        else:
            return 0.0
    all_consist = True
    for rlist in (rows_fe, rows_cr):
        for cr, ini, sad, fin, barr in rlist:
            if not (sad > ini and sad > fin):
                all_consist = False
                break
        if not all_consist:
            break
    internal_score = 1.0 if all_consist else 0.0
    fe_bar = {cr: barr for cr, ini, sad, fin, barr in rows_fe}
    cr_bar = {cr: barr for cr, ini, sad, fin, barr in rows_cr}
    gold_fe = step.get("gold_fe", {})
    gold_cr = step.get("gold_cr", {})
    tol = step.get("tolerance_barrier", 0.15)
    def barrier_score(bar_dict, gold_dict):
        total = len(gold_dict)
        if total == 0:
            return 1.0
        ok = 0
        for cr, gold_val in gold_dict.items():
            cr_int = int(cr)
            agent_val = bar_dict.get(cr_int)
            if agent_val is not None and abs(agent_val - gold_val) <= tol:
                ok += 1
        return ok / total
    fe_value_score = barrier_score(fe_bar, gold_fe)
    cr_value_score = barrier_score(cr_bar, gold_cr)
    total_value_score = (fe_value_score + cr_value_score) / 2.0
    trend_satisfied = 0
    total_trends = 6
    if 0 in fe_bar and 6 in fe_bar and fe_bar[0] > fe_bar[6]:
        trend_satisfied += 1
    if 6 in fe_bar and 7 in fe_bar and fe_bar[6] < fe_bar[7]:
        trend_satisfied += 1
    if 14 in fe_bar and 21 in fe_bar and fe_bar[14] < fe_bar[21]:
        trend_satisfied += 1
    if 1 in cr_bar and 7 in cr_bar and cr_bar[1] < cr_bar[7]:
        trend_satisfied += 1
    if 14 in cr_bar and 17 in cr_bar and cr_bar[14] < cr_bar[17]:
        trend_satisfied += 1
    if 17 in cr_bar and 21 in cr_bar and cr_bar[17] > cr_bar[21]:
        trend_satisfied += 1
    trend_score = trend_satisfied / total_trends
    w1 = 0.7
    w2 = 0.15
    w3 = 0.1
    w4 = 0.05
    total = w1 * total_value_score + w2 * trend_score + w3 * internal_score + w4 * shape_score
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'migration_barriers': score_0,
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
