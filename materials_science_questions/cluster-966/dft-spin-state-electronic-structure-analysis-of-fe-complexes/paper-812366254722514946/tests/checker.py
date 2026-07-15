import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    return {'spec': spec}


# === block: score_0 (check id='oscillator_strengths_check') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list): return 0.0
    if not artifact: return 0.0
    cols = artifact[0].keys()
    required = ['initial_state','final_state','vibration_mode','oscillator_strength']
    if not all(c in cols for c in required): return 0.0
    gold_rows = step.get('gold', [])
    if not gold_rows: return 1.0
    tol_abs = step.get('tolerance_abs', 1e-9)
    matches = 0
    for gr in gold_rows:
        found = False
        for row in artifact:
            try:
                row_init = str(row.get('initial_state','')).strip()
                row_fin = str(row.get('final_state','')).strip()
                row_mode = str(row.get('vibration_mode','')).strip()
            except:
                continue
            if row_init == gr['initial_state'] and row_fin == gr['final_state'] and row_mode == gr['vibration_mode']:
                try:
                    val = float(row['oscillator_strength'])
                except (ValueError, TypeError):
                    continue
                if abs(val - gr['oscillator_strength']) <= tol_abs:
                    matches += 1
                found = True
                break
    return matches / len(gold_rows)


# === block: score_1 (check id='faraday_parameters_check') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list): return 0.0
    if not artifact: return 0.0
    cols = artifact[0].keys()
    required = ['transition','vibration_mode','A','B','C','B_plus_C_over_kT']
    if not all(c in cols for c in required): return 0.0
    gold_rows = step.get('gold', [])
    if not gold_rows: return 1.0
    rel_tol = step.get('tolerance_rel', 0.01)
    fields = ['A','B','C','B_plus_C_over_kT']
    total_score = 0.0
    for gr in gold_rows:
        found_any = False
        row_score = 0.0
        for row in artifact:
            try:
                row_trans = str(row.get('transition','')).strip()
                row_mode = str(row.get('vibration_mode','')).strip()
            except:
                continue
            if row_trans == gr['transition'] and row_mode == gr['vibration_mode']:
                found_any = True
                for f in fields:
                    try:
                        val = float(row[f])
                    except (ValueError, TypeError):
                        continue
                    expected = float(gr[f])
                    if abs(expected) < 1e-12:
                        ok = abs(val - expected) <= 1e-12
                    else:
                        ok = abs(val - expected) <= max(rel_tol * abs(expected), 1e-12)
                    if ok:
                        row_score += 1.0 / len(fields)
                break
        total_score += row_score if found_any else 0.0
    return total_score / len(gold_rows)


_SCORERS = {
    'oscillator_strengths_check': score_0,
    'faraday_parameters_check': score_1,
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
