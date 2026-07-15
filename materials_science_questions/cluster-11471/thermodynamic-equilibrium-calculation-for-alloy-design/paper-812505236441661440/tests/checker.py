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
    return {
        "phase_gold": [
            {"depth_um":0,"f_graphite":0.0,"f_ferrite":0.0,"f_pearlite":0.0,"f_austenite":0.0,"f_ledeburite":0.92,"f_martensite":0.08},
            {"depth_um":100,"f_graphite":0.02,"f_ferrite":0.25,"f_pearlite":0.0,"f_austenite":0.18,"f_ledeburite":0.50,"f_martensite":0.05},
            {"depth_um":200,"f_graphite":0.04,"f_ferrite":0.60,"f_pearlite":0.0,"f_austenite":0.25,"f_ledeburite":0.10,"f_martensite":0.01},
            {"depth_um":300,"f_graphite":0.1165,"f_ferrite":0.8835,"f_pearlite":0.0,"f_austenite":0.0,"f_ledeburite":0.0,"f_martensite":0.0},
            {"depth_um":400,"f_graphite":0.1165,"f_ferrite":0.8835,"f_pearlite":0.0,"f_austenite":0.0,"f_ledeburite":0.0,"f_martensite":0.0}
        ],
        "layer_gold": {"case":"V2","thickness_um":220,"tolerance_um":50}
    }


# === block: score_0 (check id='phase_fractions') ===
def score_0(artifact, step, ctx):
        # artifact is a list of dicts from csv.DictReader
        gold = ctx["phase_gold"]
        phases = ["f_graphite","f_ferrite","f_pearlite","f_austenite","f_ledeburite","f_martensite"]
        tol = 0.05
        scores = []
        # build lookup by depth
        gold_by_depth = {r["depth_um"]: r for r in gold}
        for row in artifact:
            d = int(row["depth_um"])
            if d not in gold_by_depth:
                continue
            g = gold_by_depth[d]
            for p in phases:
                delta = abs(float(row[p]) - float(g[p]))
                s = max(0.0, 1.0 - delta / tol)
                scores.append(s)
        # treat missing expected depth rows as zero
        total_expected = len(gold) * len(phases)
        missing = total_expected - len(scores)
        for _ in range(missing):
            scores.append(0.0)
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


# === block: score_1 (check id='layer_thickness') ===
def score_1(artifact, step, ctx):
        # artifact is a dict with case and ledeburite_martensite_layer_thickness_um
        gold = ctx["layer_gold"]
        if artifact.get("case") != gold["case"]:
            return 0.0
        measured = float(artifact.get("ledeburite_martensite_layer_thickness_um", 0.0))
        delta = abs(measured - gold["thickness_um"])
        return max(0.0, 1.0 - delta / gold["tolerance_um"])


_SCORERS = {
    'phase_fractions': score_0,
    'layer_thickness': score_1,
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
