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
    import json, os
    fe_path = os.path.join("/app/outputs", "fe_doped.json")
    ctx = {}
    try:
        with open(fe_path) as f:
            fe_data = json.load(f)
        ctx["fe_occ_above_vbm_pbe"] = fe_data.get("pbe_occ_above_vbm", None)
    except Exception:
        ctx["fe_occ_above_vbm_pbe"] = None
    return ctx


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    artifact = load_artifact(os.path.join("/app/outputs", "perfect_lonsdaleite.json"))
    if not artifact: return 0.0
    targets = {"pbe_bg": 3.65, "hse06_bg": 4.60}
    tolerances = {"pbe_bg": 0.1, "hse06_bg": 0.2}
    score = 0.0
    count = 0
    for f,t in targets.items():
        tol = tolerances.get(f, 0.0)
        val = artifact.get(f)
        if val is not None:
            if abs(val - t) <= tol:
                score += 1.0
            count += 1
    return score / max(count, 1)


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    artifact = load_artifact(os.path.join("/app/outputs", "fe_doped.json"))
    if not artifact: return 0.0
    targets = {"pbe_occ_unocc_gap": 2.20, "pbe_occ_above_vbm": 0.30, "ggau1_occ_unocc_gap": 2.40, "ggau1_occ_above_vbm": 0.10}
    tolerances = {"pbe_occ_unocc_gap": 0.1, "pbe_occ_above_vbm": 0.1, "ggau1_occ_unocc_gap": 0.05, "ggau1_occ_above_vbm": 0.05}
    score = 0.0
    count = 0
    for f,t in targets.items():
        tol = tolerances.get(f, 0.0)
        val = artifact.get(f)
        if val is not None:
            if abs(val - t) <= tol:
                score += 1.0
            count += 1
    return score / max(count, 1)


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    artifact = load_artifact(os.path.join("/app/outputs", "additional_dopants.json"))
    if not artifact: return 0.0
    fe_occ = ctx.get("fe_occ_above_vbm_pbe", 0.30)
    systems = ["K_lonsdaleite","Ca_lonsdaleite","Zn_lonsdaleite","C_vacancy_lonsdaleite","Cr_lonsdaleite","Mn_lonsdaleite","Fe_cubic_diamond"]
    targets = {"K_lonsdaleite":0.50,"Ca_lonsdaleite":0.0,"Fe_cubic_diamond":0.65}
    tolerances = {"K_lonsdaleite":0.2,"Ca_lonsdaleite":0.2,"Fe_cubic_diamond":0.2}
    scores = []
    for sys_key in systems:
        sys_data = artifact.get(sys_key)
        if not isinstance(sys_data, dict):
            scores.append(0.0)
            continue
        occ_val = sys_data.get("occ_level_above_vbm_pbe")
        if occ_val is None:
            scores.append(0.0)
            continue
        if sys_key in targets:
            target = targets[sys_key]
            tol = tolerances.get(sys_key, 0.2)
            if abs(occ_val - target) <= tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        else:
            in_range = (0.0 <= occ_val <= 2.0)
            if sys_key in ("Cr_lonsdaleite","Mn_lonsdaleite"):
                if in_range and fe_occ is not None and occ_val < fe_occ:
                    scores.append(1.0)
                elif in_range:
                    scores.append(0.5)
                else:
                    scores.append(0.0)
            else:
                scores.append(1.0 if in_range else 0.0)
    return sum(scores) / len(scores)


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
