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
    gold_frenkel = {"type1_to_type2": 0.53, "type1_to_type3": 1.07, "type1_to_type4": 1.29, "tetrahedral_minimum": 0.60}
    gold_interstitial = {"minimum_path_type3_intermediate": 0.75, "direct_type2_to_type2": 0.89}
    gold_vacancy = {"octahedral_type1_along_a": 0.58, "octahedral_type1_along_c": 1.01, "tetrahedral_minimum": 0.17, "octahedral_to_tetrahedral_minimum": 0.21, "continuous_1d_barrier": 0.30, "inter_channel_barrier": 0.33}
    gold_activation = {"vacancy_EA": 0.60, "interstitial_EA": 1.02}
    ctx = {
        "gold_frenkel": gold_frenkel,
        "tol_frenkel": 0.10,
        "gold_interstitial_barriers": gold_interstitial,
        "tol_barriers": 0.08,
        "gold_vacancy_barriers": gold_vacancy,
        "gold_activation": gold_activation,
        "tol_activation": 0.10,
    }
    return ctx


# === block: score_0 (check id='frenkel_energies') ===
def score_0(artifact, step, ctx):
    req_keys = ["type1_to_type2","type1_to_type3","type1_to_type4","tetrahedral_minimum"]
    gold = ctx["gold_frenkel"]
    tol = ctx["tol_frenkel"]
    ff = artifact.get("frenkel_formation_energies", {})
    if not all(k in ff for k in req_keys):
        return 0.0
    scores = []
    for k in req_keys:
        v = ff[k]
        if not isinstance(v, (int, float)):
            return 0.0
        err = abs(v - gold[k])
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / (2 * tol)))
    return sum(scores) / len(scores)


# === block: score_1 (check id='interstitial_barriers') ===
def score_1(artifact, step, ctx):
    req_keys = ["minimum_path_type3_intermediate", "direct_type2_to_type2"]
    gold = ctx["gold_interstitial_barriers"]
    tol = ctx["tol_barriers"]
    ib = artifact.get("interstitial_migration_barriers", {})
    if not all(k in ib for k in req_keys):
        return 0.0
    scores = []
    for k in req_keys:
        v = ib[k]
        if not isinstance(v, (int, float)):
            return 0.0
        if v <= gold[k] + tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (v - (gold[k] + tol)) / (2 * tol)))
    return sum(scores) / len(scores)


# === block: score_2 (check id='vacancy_barriers') ===
def score_2(artifact, step, ctx):
    req_keys = ["octahedral_type1_along_a", "octahedral_type1_along_c", "tetrahedral_minimum", "octahedral_to_tetrahedral_minimum", "continuous_1d_barrier", "inter_channel_barrier"]
    gold = ctx["gold_vacancy_barriers"]
    tol = ctx["tol_barriers"]
    vb = artifact.get("vacancy_migration_barriers", {})
    if not all(k in vb for k in req_keys):
        return 0.0
    scores = []
    for k in req_keys:
        v = vb[k]
        if not isinstance(v, (int, float)):
            return 0.0
        if v <= gold[k] + tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (v - (gold[k] + tol)) / (2 * tol)))
    return sum(scores) / len(scores)


# === block: score_3 (check id='activation_energies') ===
def score_3(artifact, step, ctx):
    req_keys = ["vacancy_EA", "interstitial_EA"]
    gold = ctx["gold_activation"]
    tol = ctx["tol_activation"]
    ae = artifact.get("activation_energies", {})
    if not all(k in ae for k in req_keys):
        return 0.0
    scores = []
    for k in req_keys:
        v = ae[k]
        if not isinstance(v, (int, float)):
            return 0.0
        err = abs(v - gold[k])
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / (2 * tol)))
    return sum(scores) / len(scores)


# === block: score_4 (check id='dominant_mechanism') ===
def score_4(artifact, step, ctx):
    dom = artifact.get("dominant_mechanism")
    ae = artifact.get("activation_energies", {})
    vac = ae.get("vacancy_EA")
    int_ = ae.get("interstitial_EA")
    if dom == "vacancy" and isinstance(vac, (int,float)) and isinstance(int_, (int,float)) and vac < int_:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'frenkel_energies': score_0,
    'interstitial_barriers': score_1,
    'vacancy_barriers': score_2,
    'activation_energies': score_3,
    'dominant_mechanism': score_4,
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
