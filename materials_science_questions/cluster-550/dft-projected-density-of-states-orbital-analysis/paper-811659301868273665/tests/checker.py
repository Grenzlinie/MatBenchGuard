import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    gold = {}
    for step in spec.get("steps", []):
        sid = step.get("id")
        if sid and "gold" in step:
            gold[sid] = step["gold"]
    return {"gold": gold}


# === block: score_0 (check id='magnetic_results') ===
def score_0(artifact, step, ctx):
    gold = ctx["gold"].get(step["id"])
    if not gold:
        return 0.0
    dE_gold = gold["delta_E"]
    mm_gold = gold["MM"]
    required = ["NM","FM","AFM1","AFM2","AFM3"]
    if not all(k in artifact for k in required):
        return 0.0
    dE_scores = []
    mm_scores = []
    afm3_zero = True
    for key in required:
        entry = artifact[key]
        if not isinstance(entry, dict):
            return 0.0
        agent_dE = entry.get("delta_E")
        if agent_dE is None:
            return 0.0
        if key == "AFM3":
            if abs(agent_dE) > 1e-6:
                afm3_zero = False
            dE_scores.append(1.0)
        else:
            if agent_dE < 0:
                dE_scores.append(0.0)
            else:
                diff = abs(agent_dE - dE_gold[key])
                tol = 0.05
                if diff <= tol:
                    dE_scores.append(1.0)
                else:
                    dE_scores.append(max(0.0, 1.0 - (diff - tol) / tol))
        if key == "NM":
            if entry.get("MM") is not None:
                mm_scores.append(0.0)
            else:
                mm_scores.append(1.0)
        else:
            agent_mm = entry.get("MM")
            if agent_mm is None:
                return 0.0
            if key == "AFM1":
                if not isinstance(agent_mm, list) or len(agent_mm) != 2:
                    return 0.0
                tol = 0.2
                sub = 0.0
                for i, ref in enumerate([1.77, 1.82]):
                    diff = abs(agent_mm[i] - ref)
                    if diff <= tol:
                        sub += 1.0
                    else:
                        sub += max(0.0, 1.0 - (diff - tol) / tol)
                mm_scores.append(sub / 2.0)
            else:
                if not isinstance(agent_mm, (int, float)):
                    return 0.0
                diff = abs(agent_mm - mm_gold[key])
                tol = 0.2
                if diff <= tol:
                    mm_scores.append(1.0)
                else:
                    mm_scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    avg_dE = sum(dE_scores)/len(dE_scores) if dE_scores else 0.0
    avg_mm = sum(mm_scores)/len(mm_scores) if mm_scores else 0.0
    score = (avg_dE + avg_mm) / 2.0
    if not afm3_zero:
        score *= 0.5
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='elastic_results') ===
def score_1(artifact, step, ctx):
    gold = ctx["gold"].get(step["id"])
    if not gold:
        return 0.0
    keys = ["C11","C12","C13","C33","C44","C66"]
    if not all(k in artifact for k in keys):
        return 0.0
    scores = []
    for key in keys:
        agent_val = artifact[key]
        if not isinstance(agent_val, (int, float)):
            return 0.0
        gold_val = gold[key]
        tol = max(0.15 * abs(gold_val), 10.0)
        diff = abs(agent_val - gold_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_2 (check id='bader_results') ===
def score_2(artifact, step, ctx):
    gold = ctx["gold"].get(step["id"])
    if not gold:
        return 0.0
    keys = ["Th","Cr","Si"]
    if not all(k in artifact for k in keys):
        return 0.0
    scores = []
    for key in keys:
        agent_val = artifact[key]
        if not isinstance(agent_val, (int, float)):
            return 0.0
        gold_val = gold[key]
        tol = 0.1
        diff = abs(agent_val - gold_val)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'magnetic_results': score_0,
    'elastic_results': score_1,
    'bader_results': score_2,
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
