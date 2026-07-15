import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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
    step = next(s for s in spec['steps'] if s['id'] == 'step_06')
    gold = step['gold']
    return {'gold_rows': gold['rows'], 'trends': gold['trends']}


# === block: score_0 (check id='step_06') ===
def score_0(artifact, step, ctx):
    # Artifact is list of dicts from CSV
        gold_rows = ctx['gold_rows']
        trends = ctx['trends']
        required_cols = ['defect','displacement_A','displacement_dir','born_charge','polarization_uCcm2','barrier_eV']
        if not artifact or not all(col in artifact[0] for col in required_cols):
            return 0.0
        agent_map = {}
        for row in artifact:
            d = row.get('defect','').strip()
            if d:
                agent_map[d] = row
        # per-row scores
        row_scores = []
        for gr in gold_rows:
            d = gr['defect']
            if d not in agent_map:
                row_scores.append(0.0)
                continue
            row = agent_map[d]
            dir_ok = 1.0 if row.get('displacement_dir','').strip() == gr['displacement_dir'] else 0.0
            num_ok = 0.0
            fields = ['displacement_A','born_charge','polarization_uCcm2','barrier_eV']
            for f in fields:
                try:
                    val = float(row[f])
                    target = float(gr[f])
                    tol = float(gr.get('tol_'+f, 0.0))
                    if abs(val - target) <= tol:
                        num_ok += 1.0
                except (ValueError, KeyError, TypeError):
                    pass
            row_score = (num_ok + dir_ok) / (len(fields) + 1.0)
            row_scores.append(row_score)
        rows_score = sum(row_scores) / len(row_scores) if row_scores else 0.0
        # trend score
        trend_score = 0.0
        try:
            p_ti = float(agent_map['Ti_Sr'].get('polarization_uCcm2', 0))
            p_sr = float(agent_map['Sr_Ti'].get('polarization_uCcm2', 0))
            b_ti = float(agent_map['Ti_Sr'].get('barrier_eV', 0))
            b_sr = float(agent_map['Sr_Ti'].get('barrier_eV', 0))
            b_tivo = float(agent_map['Ti_Sr_V_O'].get('barrier_eV', 0))
            checks = [
                (p_ti > p_sr),
                (b_ti > b_sr),
                (b_tivo > b_ti)
            ]
            trend_score = sum(1.0 for c in checks if c) / len(checks)
        except (KeyError, ValueError, TypeError):
            trend_score = 0.0
        final = 0.7 * rows_score + 0.3 * trend_score
        return min(1.0, max(0.0, final))


_SCORERS = {
    'step_06': score_0,
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
