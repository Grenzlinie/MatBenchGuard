import os
import json
import csv

# === author imports / helpers ===
import math, csv, os


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


# === block: score_0 (check id='compression_numeric') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    gold_rows = step.get("gold", [])
    if not gold_rows:
        return 0.0
    tol = step.get("tolerance", 0.3)
    fields = step.get("fields", [])
    total = 0.0
    count = 0
    for g in gold_rows:
        temp = g.get("temperature")
        if temp is None:
            continue
        agent_row = None
        for row in artifact:
            try:
                if float(row.get("temperature", None)) == float(temp):
                    agent_row = row
                    break
            except:
                pass
        if agent_row is None:
            total += 0.0
            count += len(fields)
            continue
        for f in fields:
            gv = g.get(f)
            try:
                av = float(agent_row.get(f, None))
            except:
                av = None
            if gv is None:
                if av is None or (isinstance(av, float) and math.isnan(av)):
                    score = 1.0
                else:
                    score = 0.0
            else:
                if av is None:
                    score = 0.0
                else:
                    diff = abs(av - gv)
                    score = max(0.0, 1.0 - diff / tol)
            total += score
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_1 (check id='superheating_numeric') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    gold_rows = step.get("gold", [])
    if not gold_rows:
        return 0.0
    tol = step.get("tolerance", 15)
    fields = step.get("fields", [])
    total = 0.0
    count = 0
    for g in gold_rows:
        lp = g.get("lateral_pressure")
        if lp is None:
            continue
        agent_row = None
        for row in artifact:
            try:
                if float(row.get("lateral_pressure", None)) == float(lp):
                    agent_row = row
                    break
            except:
                pass
        if agent_row is None:
            total += 0.0
            count += len(fields)
            continue
        for f in fields:
            gv = g.get(f)
            try:
                av = float(agent_row.get(f, None))
            except:
                av = None
            if gv is None:
                if av is None or (isinstance(av, float) and math.isnan(av)):
                    score = 1.0
                else:
                    score = 0.0
            else:
                if av is None:
                    score = 0.0
                else:
                    diff = abs(av - gv)
                    score = max(0.0, 1.0 - diff / tol)
            total += score
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_2 (check id='structural_trends') ===
def score_2(artifact, step, ctx):
    path = "/app/outputs/superheating_limit_melting.csv"
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    data = {}
    try:
        for r in rows:
            p = float(r["lateral_pressure"])
            tv = float(r["T_melt_BL_VHDI"]) if r.get("T_melt_BL_VHDI") not in (None, "") else None
            ta = float(r["T_melt_BL_AAI"]) if r.get("T_melt_BL_AAI") not in (None, "") else None
            data[p] = {"VHDI": tv, "AAI": ta}
    except:
        return 0.0
    ordered_p = sorted(data.keys())
    aai_vals = [data[p]["AAI"] for p in ordered_p if data[p]["AAI"] is not None]
    if len(aai_vals) >= 2:
        inc = all(aai_vals[i] >= aai_vals[i-1] - 1e-6 for i in range(1, len(aai_vals)))
        aai_score = 1.0 if inc else 0.0
    else:
        aai_score = 0.0
    vhd_vals = [data[p]["VHDI"] for p in ordered_p if data[p]["VHDI"] is not None]
    if len(vhd_vals) >= 4:
        cond = (vhd_vals[0] <= vhd_vals[1] + 1e-6) and (vhd_vals[1] < vhd_vals[2] + 1e-6) and (vhd_vals[2] > vhd_vals[3] + 1e-6)
        vhd_score = 1.0 if cond else 0.0
    else:
        vhd_score = 0.0
    return 0.5 * aai_score + 0.5 * vhd_score


_SCORERS = {
    'compression_numeric': score_0,
    'superheating_numeric': score_1,
    'structural_trends': score_2,
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
