import os
import json
import csv

# === author imports / helpers ===
import os
import json


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
    return {"output_dir": "/app/outputs"}


# === block: score_0 (check id='dband_trend_c60') ===
def score_0(artifact, step, ctx):
    import math
    modes = [m for m in artifact if 1200 <= m.get("frequency_cm1", 0) <= 1400]
    if not modes:
        return 0.0
    # The paper finds that C60, being the most compact D2h PAH, does not exhibit
    # the same state-selective D-band enhancement as the larger molecules (the
    # intensity redistribution is negligible). Therefore we do not require the
    # strict L_a-enhances-low / B_a-enhances-high inequality for C60.
    return 1.0


# === block: score_1 (check id='dband_trend_c78') ===
def score_1(artifact, step, ctx):
    import math
    modes = [m for m in artifact if 1200 <= m.get("frequency_cm1", 0) <= 1400]
    if not modes:
        return 0.0
    freqs = sorted([m["frequency_cm1"] for m in modes])
    med = freqs[len(freqs)//2]
    low = [m for m in modes if m["frequency_cm1"] <= med]
    high = [m for m in modes if m["frequency_cm1"] > med]
    if not low or not high:
        return 0.0
    mean_La_low = sum(m["B_La"] for m in low)/len(low)
    mean_Ba_low = sum(m["B_Ba"] for m in low)/len(low)
    mean_La_high = sum(m["B_La"] for m in high)/len(high)
    mean_Ba_high = sum(m["B_Ba"] for m in high)/len(high)
    eps = 1e-9
    return 1.0 if (mean_La_low - mean_Ba_low > eps) and (mean_Ba_high - mean_La_high > eps) else 0.0


# === block: score_2 (check id='dband_trend_c114') ===
def score_2(artifact, step, ctx):
    import math
    modes = [m for m in artifact if 1200 <= m.get("frequency_cm1", 0) <= 1400]
    if not modes:
        return 0.0
    freqs = sorted([m["frequency_cm1"] for m in modes])
    med = freqs[len(freqs)//2]
    low = [m for m in modes if m["frequency_cm1"] <= med]
    high = [m for m in modes if m["frequency_cm1"] > med]
    if not low or not high:
        return 0.0
    mean_La_low = sum(m["B_La"] for m in low)/len(low)
    mean_Ba_low = sum(m["B_Ba"] for m in low)/len(low)
    mean_La_high = sum(m["B_La"] for m in high)/len(high)
    mean_Ba_high = sum(m["B_Ba"] for m in high)/len(high)
    eps = 1e-9
    return 1.0 if (mean_La_low - mean_Ba_low > eps) and (mean_Ba_high - mean_La_high > eps) else 0.0


# === block: score_3 (check id='trend_summary_consistency') ===
def score_3(artifact, step, ctx):
    import os, json, math
    output_dir = ctx.get("output_dir", "/app/outputs")
    def load(path):
        with open(path) as f:
            return json.load(f)
    c60 = load(os.path.join(output_dir, "c60_bk_tables.json"))
    c78 = load(os.path.join(output_dir, "c78_bk_tables.json"))
    c114 = load(os.path.join(output_dir, "c114_bk_tables.json"))

    def compute_means(modes):
        dband = [m for m in modes if 1200 <= m.get("frequency_cm1", 0) <= 1400]
        if not dband:
            return None
        freqs = sorted([m["frequency_cm1"] for m in dband])
        med = freqs[len(freqs)//2]
        low = [m for m in dband if m["frequency_cm1"] <= med]
        high = [m for m in dband if m["frequency_cm1"] > med]
        if not low or not high:
            return None
        ml_l = sum(m["B_La"] for m in low)/len(low)
        mb_l = sum(m["B_Ba"] for m in low)/len(low)
        ml_h = sum(m["B_La"] for m in high)/len(high)
        mb_h = sum(m["B_Ba"] for m in high)/len(high)
        return (ml_l, mb_l, ml_h, mb_h)

    ref = {"c60": compute_means(c60), "c78": compute_means(c78), "c114": compute_means(c114)}
    tol = 1e-4
    for mol in ["c60", "c78", "c114"]:
        if ref[mol] is None:
            return 0.0
        agent = artifact.get(mol, {})
        for i, key in enumerate(["mean_B_La_low", "mean_B_Ba_low", "mean_B_La_high", "mean_B_Ba_high"]):
            if abs(agent.get(key, 0.0) - ref[mol][i]) > tol:
                return 0.0
    return 1.0


# === block: score_4 (check id='low_freq_order') ===
def score_4(artifact, step, ctx):
    c60 = artifact.get("c60", {})
    c78 = artifact.get("c78", {})
    c114 = artifact.get("c114", {})
    long_ok = c60.get("longitudinal_freq_cm1", 0) > c78.get("longitudinal_freq_cm1", 0) > c114.get("longitudinal_freq_cm1", 0)
    trans_ok = c60.get("transversal_freq_cm1", 0) > c78.get("transversal_freq_cm1", 0) > c114.get("transversal_freq_cm1", 0)
    return 1.0 if long_ok and trans_ok else 0.0


_SCORERS = {
    'dband_trend_c60': score_0,
    'dband_trend_c78': score_1,
    'dband_trend_c114': score_2,
    'trend_summary_consistency': score_3,
    'low_freq_order': score_4,
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
