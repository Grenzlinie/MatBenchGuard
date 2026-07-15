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


# === block: score_0 (check id='step_02_table') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact)==0:
        return 0.0
    gold = step.get('reference_table', [])
    tol_rel = step.get('tolerance_relative', 0.20)
    tol_abs = step.get('tolerance_absolute', 1e-12)
    abs_thresh = step.get('absolute_threshold', 1e-10)
    species = step.get('species_columns', [])
    if not gold or not species:
        return 0.0
    gold_by_temp = {}
    for g in gold:
        try:
            t = int(g['Temperature'])
            gold_by_temp[t] = g
        except:
            pass
    headers = [h.strip() for h in artifact[0].keys()]
    if 'Temperature' not in headers:
        return 0.0
    total_entries = 0
    correct = 0
    for row in artifact:
        try:
            temp_str = str(row.get('Temperature','')).replace(',','.')
            temp = int(float(temp_str))
        except:
            continue
        if temp not in gold_by_temp:
            continue
        g = gold_by_temp[temp]
        for sp in species:
            total_entries += 1
            try:
                val_str = str(row.get(sp, '')).replace(',','.')
                val = float(val_str)
                gval = float(g.get(sp, None))
                if gval is None:
                    continue
            except:
                continue
            if abs(gval) >= abs_thresh:
                if gval == 0:
                    if abs(val) <= tol_abs:
                        correct += 1
                else:
                    rel_err = abs(val - gval) / abs(gval)
                    if rel_err <= tol_rel:
                        correct += 1
            else:
                if abs(val - gval) <= tol_abs:
                    correct += 1
    if total_entries == 0:
        return 0.0
    return correct / total_entries


# === block: score_1 (check id='step_02_sigma_w') ===
def score_1(artifact, step, ctx):
    if not artifact: return 0.0
    gold_sigma = step.get('reference_sigma_w', {})
    tol_rel = step.get('tolerance_relative', 0.20)
    if not gold_sigma: return 0.0
    agent_sigma = {}
    for row in artifact:
        try:
            temp = int(float(str(row.get('Temperature','')).replace(',','.')))
        except:
            continue
        try:
            pw = float(str(row.get('W','')).replace(',','.'))
            pwo = float(str(row.get('WO','')).replace(',','.'))
            pwo2 = float(str(row.get('WO2','')).replace(',','.'))
            pwo3 = float(str(row.get('WO3','')).replace(',','.'))
            pw2o6 = float(str(row.get('W2O6','')).replace(',','.'))
            pw3o9 = float(str(row.get('W3O9','')).replace(',','.'))
            pw4o12 = float(str(row.get('W4O12','')).replace(',','.'))
            pwo2oh2 = float(str(row.get('WO2(OH)2','')).replace(',','.'))
        except ValueError:
            continue
        sigma = pw + pwo + pwo2 + pwo3 + 2*pw2o6 + 3*pw3o9 + 4*pw4o12 + pwo2oh2
        agent_sigma[temp] = sigma
    if not agent_sigma: return 0.0
    matches = 0
    total = 0
    for temp, sigma in agent_sigma.items():
        key = str(int(temp))
        if key in gold_sigma:
            gsigma = gold_sigma[key]
            if gsigma == 0:
                if abs(sigma) <= 1e-15:
                    matches += 1
            else:
                rel_err = abs(sigma - gsigma) / abs(gsigma)
                if rel_err <= tol_rel:
                    matches += 1
            total += 1
    if total == 0:
        return 0.0
    return matches / total


_SCORERS = {
    'step_02_table': score_0,
    'step_02_sigma_w': score_1,
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
