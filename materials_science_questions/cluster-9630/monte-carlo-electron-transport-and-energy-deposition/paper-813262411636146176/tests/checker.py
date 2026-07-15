import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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
    return {
        "ratio_min": 200,
        "ratio_max": 250,
        "peak_depth_min": 150,
        "peak_depth_max": 250,
        "max_vacancy_fraction": 0.015,
        "max_he_fraction": 0.01,
        "cdse_thickness_nm": 5.2
    }


# === block: score_0 (check id='check_ratio') ===
def score_0(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    ratio = float(artifact.get("ratio", -1))
    if ctx["ratio_min"] <= ratio <= ctx["ratio_max"]:
        return 1.0
    return 0.0


# === block: score_1 (check id='check_vacancy_profile') ===
def score_1(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0
    try:
        depths = []
        vacs = []
        hes = []
        for r in rows:
            d = float(r["depth_nm"])
            v = int(r["total_vacancies"])
            h = int(r["he_ions_remaining"])
            depths.append(d)
            vacs.append(v)
            hes.append(h)
    except (KeyError, ValueError, TypeError):
        return 0.0
    total_v = sum(vacs)
    total_h = sum(hes)
    if total_v == 0 or total_h == 0:
        return 0.0
    max_v = max(vacs)
    max_idx = vacs.index(max_v)
    peak_depth = depths[max_idx]
    cdse_thick = ctx["cdse_thickness_nm"]
    v_shallow = sum(v for d, v in zip(depths, vacs) if d < cdse_thick)
    h_shallow = sum(h for d, h in zip(depths, hes) if d < cdse_thick)
    v_frac = v_shallow / total_v
    h_frac = h_shallow / total_h
    score_peak = 1.0 if ctx["peak_depth_min"] <= peak_depth <= ctx["peak_depth_max"] else 0.0
    score_vfrac = 1.0 if v_frac <= ctx["max_vacancy_fraction"] else 0.0
    score_hfrac = 1.0 if h_frac <= ctx["max_he_fraction"] else 0.0
    return 0.3 * score_peak + 0.4 * score_vfrac + 0.3 * score_hfrac


_SCORERS = {
    'check_ratio': score_0,
    'check_vacancy_profile': score_1,
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
