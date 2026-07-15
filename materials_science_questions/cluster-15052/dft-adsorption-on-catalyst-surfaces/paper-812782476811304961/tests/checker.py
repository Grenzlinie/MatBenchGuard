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
    return {"gold_systems": spec.get("steps", [{}])[0].get("gold_systems", [])}


# === block: score_0 (check id='adsorption_results_check') ===
def score_0(artifact, step, ctx):
    gold_systems = ctx["gold_systems"]
    artifact_systems = artifact.get("systems", [])
    if not isinstance(artifact_systems, list):
        return 0.0
    agent_map = {}
    for s in artifact_systems:
        nm = s.get("system_name")
        if nm:
            agent_map[nm] = s
    tolerances = {
        "Eads": 0.1,
        "Eg": 0.2,
        "Mtot": 0.05,
        "d_NO": 0.05,
        "d_TMN": 0.05,
        "N_NO_Lowdin": 0.1,
        "O_NO_Lowdin": 0.1,
        "Ned_gCN_Lowdin": 0.1
    }
    fields = ["Eads","Eg","Mtot","d_NO","d_TMN","N_NO_Lowdin","O_NO_Lowdin","Ned_gCN_Lowdin"]
    total_fields = 0
    correct_fields = 0
    for gsys in gold_systems:
        nm = gsys["system_name"]
        asys = agent_map.get(nm)
        if asys is None:
            total_fields += len(fields)
            continue
        for f in fields:
            total_fields += 1
            gv = gsys.get(f)
            av = asys.get(f)
            if gv is None and av is None:
                correct_fields += 1
                continue
            if gv is None or av is None:
                continue
            try:
                gv = float(gv)
                av = float(av)
            except:
                continue
            if abs(av - gv) <= tolerances[f]:
                correct_fields += 1
    pristine = agent_map.get("pristine/NO", {})
    fe = agent_map.get("Fe/NO", {})
    ru = agent_map.get("Ru/NO", {})
    os_ = agent_map.get("Os/NO", {})
    struct_score = 0.0
    try:
        e_p = float(pristine.get("Eads"))
        e_fe = float(fe.get("Eads"))
        e_ru = float(ru.get("Eads"))
        e_os = float(os_.get("Eads"))
        m_p = float(pristine.get("Mtot"))
        m_fe = float(fe.get("Mtot"))
        m_ru = float(ru.get("Mtot"))
        m_os = float(os_.get("Mtot"))
        c1 = (e_fe < e_p) and (e_ru < e_p) and (e_os < e_p)
        c2 = (e_os <= e_fe) and (e_os <= e_ru)
        c3 = (m_os > 0.05) and (m_p <= 0.05) and (m_fe <= 0.05) and (m_ru <= 0.05)
        struct_score = (c1 + c2 + c3) / 3.0
    except:
        struct_score = 0.0
    numeric_score = correct_fields / total_fields if total_fields > 0 else 0.0
    score = 0.7 * numeric_score + 0.3 * struct_score
    return score


_SCORERS = {
    'adsorption_results_check': score_0,
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
