import os
import json
import csv

# === author imports / helpers ===
import csv, os, json


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
    # Reference values are embedded in the checker to avoid leaking them in the grading specification.
    ref_rows = [
        {"model":"undoped",       "overpotential":0.73, "step2_energy":0.5,  "step3_energy":1.47, "step4_energy":1.48,  "step5_energy":1.47},
        {"model":"BNC-1_1B",     "overpotential":0.70, "step2_energy":0.53, "step3_energy":1.46, "step4_energy":1.465, "step5_energy":1.465},
        {"model":"BNC-1_2B",     "overpotential":0.71, "step2_energy":0.52, "step3_energy":1.47, "step4_energy":1.465, "step5_energy":1.465},
        {"model":"BNC-1_3B",     "overpotential":0.72, "step2_energy":0.51, "step3_energy":1.47, "step4_energy":1.47,  "step5_energy":1.47},
        {"model":"NNC-1",        "overpotential":0.70, "step2_energy":0.53, "step3_energy":1.46, "step4_energy":1.465, "step5_energy":1.465},
        {"model":"SiNC-1",       "overpotential":0.73, "step2_energy":1.00, "step3_energy":1.71, "step4_energy":1.71,  "step5_energy":0.50},
        {"model":"PNC-1",        "overpotential":0.48, "step2_energy":0.75, "step3_energy":1.39, "step4_energy":1.39,  "step5_energy":1.39},
        {"model":"SNC-1",        "overpotential":0.56, "step2_energy":0.67, "step3_energy":1.416,"step4_energy":1.417,"step5_energy":1.417},
    ]
    ref_dict = {row["model"]: row for row in ref_rows}
    return {"ref": ref_dict}


# === block: score_0 (check id='or_results_shape') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_cols = ["model","step2_energy","step3_energy","step4_energy","step5_energy","overpotential"]
    if not all(c in artifact[0] for c in required_cols):
        return 0.0
    expected_models = {"undoped","BNC-1_1B","BNC-1_2B","BNC-1_3B","NNC-1","SiNC-1","PNC-1","SNC-1"}
    models_present = {row["model"] for row in artifact}
    if expected_models != models_present:
        return 0.0
    for row in artifact:
        for c in required_cols[1:]:
            try:
                float(row[c])
            except:
                return 0.0
    return 1.0


# === block: score_1 (check id='or_results_consistency_overpotential') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    for row in artifact:
        steps = [float(row["step2_energy"]), float(row["step3_energy"]), float(row["step4_energy"]), float(row["step5_energy"])]
        eta_comp = 1.23 - min(steps)
        if abs(eta_comp - float(row["overpotential"])) > 0.01:
            return 0.0
    return 1.0


# === block: score_2 (check id='or_results_undoped_limiting_step') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    row = next((r for r in artifact if r["model"] == "undoped"), None)
    if row is None:
        return 0.0
    s2 = float(row["step2_energy"])
    s3 = float(row["step3_energy"])
    s4 = float(row["step4_energy"])
    s5 = float(row["step5_energy"])
    return 1.0 if s2 <= s3 and s2 <= s4 and s2 <= s5 else 0.0


# === block: score_3 (check id='or_results_BNC_limiting_step') ===
def score_3(artifact, step, ctx):
    if artifact is None:
        return 0.0
    row = next((r for r in artifact if r["model"] == "BNC-1_1B"), None)
    if row is None:
        return 0.0
    s2 = float(row["step2_energy"])
    s3 = float(row["step3_energy"])
    s4 = float(row["step4_energy"])
    s5 = float(row["step5_energy"])
    return 1.0 if s2 <= s3 and s2 <= s4 and s2 <= s5 else 0.0


# === block: score_4 (check id='or_results_PNC_vs_undoped') ===
def score_4(artifact, step, ctx):
    if artifact is None:
        return 0.0
    undoped = next((r for r in artifact if r["model"] == "undoped"), None)
    pnc = next((r for r in artifact if r["model"] == "PNC-1"), None)
    if undoped is None or pnc is None:
        return 0.0
    return 1.0 if float(pnc["overpotential"]) < float(undoped["overpotential"]) else 0.0


# === block: score_5 (check id='or_results_BNC_overpotential_trend') ===
def score_5(artifact, step, ctx):
    if artifact is None:
        return 0.0
    b1 = next((r for r in artifact if r["model"] == "BNC-1_1B"), None)
    b2 = next((r for r in artifact if r["model"] == "BNC-1_2B"), None)
    b3 = next((r for r in artifact if r["model"] == "BNC-1_3B"), None)
    if b1 is None or b2 is None or b3 is None:
        return 0.0
    ov1 = float(b1["overpotential"])
    ov2 = float(b2["overpotential"])
    ov3 = float(b3["overpotential"])
    return 1.0 if ov1 <= ov2 <= ov3 else 0.0


# === block: score_6 (check id='or_results_abs_overpotential') ===
def score_6(artifact, step, ctx):
    if artifact is None:
        return 0.0
    ref = ctx.get("ref", {})
    total = 0
    passed = 0
    for row in artifact:
        model = row["model"]
        if model in ref:
            if float(row["overpotential"]) <= ref[model]["overpotential"] + 0.15:
                passed += 1
            total += 1
    return passed / total if total > 0 else 0.0


# === block: score_7 (check id='or_results_abs_step_energies') ===
def score_7(artifact, step, ctx):
    if artifact is None:
        return 0.0
    ref = ctx.get("ref", {})
    total_pairs = 0
    passed = 0
    for row in artifact:
        model = row["model"]
        if model in ref:
            for key in ["step2_energy","step3_energy","step4_energy","step5_energy"]:
                if abs(float(row[key]) - ref[model][key]) <= 0.5:
                    passed += 1
                total_pairs += 1
    return passed / total_pairs if total_pairs > 0 else 0.0


_SCORERS = {
    'or_results_shape': score_0,
    'or_results_consistency_overpotential': score_1,
    'or_results_undoped_limiting_step': score_2,
    'or_results_BNC_limiting_step': score_3,
    'or_results_PNC_vs_undoped': score_4,
    'or_results_BNC_overpotential_trend': score_5,
    'or_results_abs_overpotential': score_6,
    'or_results_abs_step_energies': score_7,
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