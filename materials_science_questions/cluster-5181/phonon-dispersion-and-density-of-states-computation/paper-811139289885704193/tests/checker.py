import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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


# === block: score_0 (check id='step_1_elastic') ===
def score_0(artifact, step, ctx):
    elastic = artifact
    if not isinstance(elastic, dict):
        return 0.0
    targets = step["targets"]
    max_err = 0.0
    for key in ["C11","C12","C44"]:
        ref = float(targets[key])
        val = float(elastic.get(key, 0.0))
        if ref == 0:
            continue
        err = abs(val - ref) / ref
        if err > max_err:
            max_err = err
    tol = float(step["tolerance"])
    width = float(step["decay_width"])
    if max_err <= tol:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (max_err - tol) / width)
    return score


# === block: score_1 (check id='step_2_phonon') ===
def score_1(artifact, step, ctx):
    ref = step["reference_frequencies"]
    agent_rows = artifact
    if not isinstance(agent_rows, list) or not agent_rows:
        return 0.0
    squared_errors = []
    for row in agent_rows:
        qp = row.get("q_point", "").strip()
        if qp not in ref:
            continue
        gold = ref[qp]
        for i, col in enumerate(["freq1","freq2","freq3"]):
            try:
                val = float(row.get(col, 0.0))
            except (ValueError, TypeError):
                val = 0.0
            squared_errors.append((val - gold[i])**2)
    if not squared_errors:
        return 0.0
    rmse = math.sqrt(sum(squared_errors)/len(squared_errors))
    thresh = float(step["rmse_threshold"])
    decay = float(step["decay_threshold"])
    if rmse <= thresh:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (rmse - thresh) / (decay - thresh))
    return score


# === block: score_2 (check id='step_3_thermo') ===
def score_2(artifact, step, ctx):
    ref_rows = step["reference_rows"]
    ref_dict = {}
    for r in ref_rows:
        ref_dict[(float(r["T_K"]), float(r["P_GPa"]))] = r
    agent_rows = artifact
    if not isinstance(agent_rows, list) or not agent_rows:
        return 0.0
    fields = ["alpha_V_1e-6", "B_S_GPa", "C_V_J_molK", "S_J_molK"]
    errors = []
    for row in agent_rows:
        T = float(row.get("T_K", None))
        P = float(row.get("P_GPa", None))
        if (T,P) not in ref_dict:
            continue
        ref = ref_dict[(T,P)]
        for f in fields:
            ref_val = float(ref[f])
            agent_val = float(row.get(f, 0.0))
            if ref_val != 0.0:
                errors.append(abs(agent_val - ref_val) / abs(ref_val))
    if not errors:
        mare = 1.0
    else:
        mare = sum(errors) / len(errors)
    thresh = float(step["mare_threshold"])
    decay = float(step["mare_decay"])
    if mare <= thresh:
        mare_score = 1.0
    else:
        mare_score = max(0.0, 1.0 - (mare - thresh) / decay)

    groups = defaultdict(list)
    for row in agent_rows:
        P = float(row.get("P_GPa", 0.0))
        T = float(row.get("T_K", 0.0))
        Cv = float(row.get("C_V_J_molK", 0.0))
        Sval = float(row.get("S_J_molK", 0.0))
        groups[P].append((T, Cv, Sval))
    for P in groups:
        groups[P] = sorted(groups[P], key=lambda x: x[0])

    cv_ok = True
    for P, items in groups.items():
        for i in range(1, len(items)):
            if items[i][1] < items[i-1][1] - 1e-6:
                cv_ok = False
                break

    s_ok = True
    for P, items in groups.items():
        for i in range(1, len(items)):
            if items[i][2] < items[i-1][2] - 1e-6:
                s_ok = False
                break

    s_p_ok = True
    if 0 in groups and 50 in groups:
        temps0 = {t for t,_,_ in groups[0]}
        temps50 = {t for t,_,_ in groups[50]}
        common = temps0 & temps50
        for t in common:
            s0 = next(s for T,_,s in groups[0] if T==t)
            s50 = next(s for T,_,s in groups[50] if T==t)
            if s0 <= s50:
                s_p_ok = False
                break

    num_trends = 3
    trend_score = ((1.0 if cv_ok else 0.0) + (1.0 if s_ok else 0.0) + (1.0 if s_p_ok else 0.0)) / num_trends
    trend_weight = float(step["trends_weight"])
    total = (1.0 - trend_weight) * mare_score + trend_weight * trend_score
    return total


_SCORERS = {
    'step_1_elastic': score_0,
    'step_2_phonon': score_1,
    'step_3_thermo': score_2,
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
