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
    return {"output_dir": outputs_dir}


# === block: score_0 (check id='binary_gaps_gold') ===
def score_0(artifact, step, ctx):
    gold = step["gold"]
    tol = step["tolerance"]
    artifact_json = artifact
    ok = 0
    total = 0
    for comp in ["MgS", "ZnS"]:
        for gap in ["Eg_Gamma", "Eg_X", "Eg_L"]:
            val = artifact_json.get(comp, {}).get(gap)
            expected = gold[comp][gap]
            if val is not None and abs(val - expected) <= tol:
                ok += 1
            total += 1
    return ok / total if total else 0.0


# === block: score_1 (check id='ternary_vca_recompute') ===
def score_1(artifact, step, ctx):
    import os, json
    binary_path = os.path.join(ctx["output_dir"], "binary_band_gaps.json")
    if not os.path.exists(binary_path):
        return 0.0
    with open(binary_path) as f:
        binary = json.load(f)
    mg_eg = binary["MgS"]
    zn_eg = binary["ZnS"]
    tol = step["tolerance"]
    rows = artifact
    gap_keys = ["Eg_Gamma", "Eg_X", "Eg_L"]
    correct_gaps = 0
    total_gaps = 0
    antisym_vals = []
    for row in rows:
        x = float(row["x"])
        for gap in gap_keys:
            expected = x * float(mg_eg[gap]) + (1 - x) * float(zn_eg[gap])
            val = float(row.get(gap, None))
            if abs(val - expected) <= tol:
                correct_gaps += 1
            total_gaps += 1
        antisym_vals.append(float(row.get("antisymmetric_gap", 0.0)))
    gap_score = correct_gaps / total_gaps if total_gaps else 0.0
    mono = True
    for i in range(1, len(antisym_vals)):
        if antisym_vals[i] < antisym_vals[i-1] - 1e-9:
            mono = False
            break
    mono_score = 1.0 if mono else 0.0
    return 0.9 * gap_score + 0.1 * mono_score


# === block: score_2 (check id='optical_recompute') ===
def score_2(artifact, step, ctx):
    import os, csv
    ternary_path = os.path.join(ctx["output_dir"], "ternary_band_gaps.csv")
    if not os.path.exists(ternary_path):
        return 0.0
    with open(ternary_path, newline="") as f:
        tern_rows = list(csv.DictReader(f))
    eg_gamma = {}
    for row in tern_rows:
        eg_gamma[float(row["x"])] = float(row["Eg_Gamma"])
    rows = artifact
    tol = step["tolerance"]
    correct = 0
    total = 0
    for row in rows:
        x_val = float(row["x"])
        eg = eg_gamma.get(x_val)
        if eg is None:
            continue
        A = 25 * eg + 212
        B = 0.21 * eg + 4.25
        n_moss = (1 + A / ((eg + B) ** 2)) ** 0.25
        n_ghosh = (1 + (25 * eg + 212) / ((eg + 4.25) ** 2)) ** 0.25
        R_moss = ((n_moss - 1) / (n_moss + 1)) ** 2
        R_ghosh = ((n_ghosh - 1) / (n_ghosh + 1)) ** 2
        for field, expected in [("n_Moss", n_moss), ("n_Ghosh", n_ghosh), ("R_Moss", R_moss), ("R_Ghosh", R_ghosh)]:
            val = float(row.get(field, None))
            if abs(val - expected) <= tol:
                correct += 1
            total += 1
    return correct / total if total else 0.0


_SCORERS = {
    'binary_gaps_gold': score_0,
    'ternary_vca_recompute': score_1,
    'optical_recompute': score_2,
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
