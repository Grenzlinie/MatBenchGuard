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
    return {}


# === block: score_0 (check id='check_lambda') ===
def score_0(artifact, step, ctx):
    # Build lookup of material->lambda.
    lam = {}
    for entry in artifact:
        lam[entry["material"]] = entry["lambda"]
    if "MgB2" not in lam or "NbB2" not in lam:
        return 0.0
    lm, ln = lam["MgB2"], lam["NbB2"]
    ordering_ok = lm > ln
    if not ordering_ok:
        return 0.0   # ordering wrong -> score 0
    gold = step["reference_values"]
    tol = step["tolerance_abs"]
    def tol_score(val, ref):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        # linear decay up to 2*tol
        if diff <= 2*tol:
            return 1.0 - (diff - tol)/tol
        return 0.0
    s_m = tol_score(lm, gold["MgB2"])
    s_n = tol_score(ln, gold["NbB2"])
    return min(s_m, s_n)


# === block: score_1 (check id='check_tc') ===
def score_1(artifact, step, ctx):
    # Find all entries for each material.
    entries_by_mat = {}
    for e in artifact:
        mat = e["material"]
        entries_by_mat.setdefault(mat, []).append(e)
    # Ensure both materials present.
    if "MgB2" not in entries_by_mat or "NbB2" not in entries_by_mat:
        return 0.0
    mgb = entries_by_mat["MgB2"]
    nbb = entries_by_mat["NbB2"]

    # --- part 1: μ*=0.10 value and ordering ---
    ref = step["reference_values"]
    tol = step["tolerance_abs"]
    def tol_score(val, refval):
        diff = abs(val - refval)
        if diff <= tol:
            return 1.0
        if diff <= 2*tol:
            return 1.0 - (diff - tol)/tol
        return 0.0

    def get_Tc_at_mu(mat_entries, mu_star):
        for e in mat_entries:
            if abs(e["mu_star"] - mu_star) < 1e-9:
                return e["Tc"]
        return None

    Tc_m = get_Tc_at_mu(mgb, 0.10)
    Tc_n = get_Tc_at_mu(nbb, 0.10)
    if Tc_m is None or Tc_n is None:
        # if the mandatory μ*=0.1 entry is missing, score zero
        return 0.0

    ordering_ok = Tc_m > Tc_n
    if not ordering_ok:
        return 0.0

    s_m = tol_score(Tc_m, ref["MgB2"])
    s_n = tol_score(Tc_n, ref["NbB2"])
    score_010 = min(s_m, s_n)

    # --- part 2: trend check (Tc decreases with increasing μ*) ---
    def trend_score(entries):
        if len(entries) < 2:
            return 1.0  # no data to check -> neutral
        sorted_entries = sorted(entries, key=lambda x: x["mu_star"])
        num_dec = 0
        num_pairs = len(sorted_entries) - 1
        for i in range(num_pairs):
            if sorted_entries[i+1]["Tc"] <= sorted_entries[i]["Tc"]:
                num_dec += 1
        return num_dec / num_pairs

    trend_m = trend_score(mgb)
    trend_n = trend_score(nbb)
    trend_total = min(trend_m, trend_n)

    # combine: 80% value+ordering, 20% trend
    return 0.8 * score_010 + 0.2 * trend_total


_SCORERS = {
    'check_lambda': score_0,
    'check_tc': score_1,
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
