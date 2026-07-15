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
    # No pre-processing needed; gold values are accessed directly from the step dict.
    return {}


# === block: score_0 (check id='normal_modes') ===
def score_0(artifact, step, ctx):
    g = step.get("gold", {})
    tol = g.get("tolerance", 0.10)
    gold_rows = g.get("rows", [])
    if not gold_rows:
        return 0.0

    # Build a mapping from E0 value to the artifact row
    artifact_by_e0 = {}
    for row in artifact:
        try:
            e0 = float(row["E0_V_per_nm"])
            artifact_by_e0[e0] = row
        except (ValueError, KeyError, TypeError):
            pass

    scores = []
    for gr in gold_rows:
        e0_target = float(gr["E0_V_per_nm"])
        art_row = artifact_by_e0.get(e0_target)
        if art_row is None:
            scores.extend([0.0, 0.0])
            continue
        for col in ["Omega_plus_meV", "Omega_minus_meV"]:
            try:
                v_agent = float(art_row[col])
            except (ValueError, KeyError, TypeError):
                scores.append(0.0)
                continue
            v_gold = float(gr.get(col, 0))
            if abs(v_gold) < 1e-9:
                point_score = 1.0 if abs(v_agent) < 1e-9 else 0.0
            else:
                rel_err = abs(v_agent - v_gold) / abs(v_gold)
                if rel_err <= tol:
                    point_score = 1.0
                else:
                    point_score = max(0.0, 1.0 - (rel_err - tol) / tol)
            scores.append(point_score)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='critical_field') ===
def score_1(artifact, step, ctx):
    g = step.get("gold", {})
    tol = g.get("tolerance", 0.20)
    col = g.get("column", "E_crit_V_per_nm")
    gold_val = float(g.get("value", 0))

    if not artifact or not isinstance(artifact, list):
        return 0.0

    try:
        row = artifact[0]
        v_agent = float(row[col])
    except (IndexError, KeyError, ValueError, TypeError):
        return 0.0

    if abs(gold_val) < 1e-9:
        return 1.0 if abs(v_agent) < 1e-9 else 0.0

    rel_err = abs(v_agent - gold_val) / abs(gold_val)
    if rel_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol) / tol)


_SCORERS = {
    'normal_modes': score_0,
    'critical_field': score_1,
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
