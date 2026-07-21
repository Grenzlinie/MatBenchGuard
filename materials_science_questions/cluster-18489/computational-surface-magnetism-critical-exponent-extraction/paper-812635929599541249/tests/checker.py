import os
import json
import csv

# === author imports / helpers ===
import math
import json
import os


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
    steps = spec.get("steps", spec.get("checks", []))
    params = steps[0].get("params", {})
    r0 = params["r0"]
    f = params["f"]
    t_list = params["t_list"]
    delta = 7.38  # Δ = π^3/(4*1.05) from paper Eq.2.2
    ref_gamma = [0.77 * r0 * math.sqrt(t) / f for t in t_list]
    ref_Lk = [delta**3 * g for g in ref_gamma]
    ref_D = [delta**2 * g for g in ref_gamma]
    t_k_star = f / (delta**2 * 0.77 * 2 * math.sqrt(3))
    L_k_star = delta**3 * 0.77 * r0 * math.sqrt(t_k_star) / f
    return {
        "ref_gamma": ref_gamma,
        "ref_Lk": ref_Lk,
        "ref_D": ref_D,
        "ref_t_k_star": t_k_star,
        "ref_L_k_star": L_k_star,
        "t_list_len": len(t_list)
    }


# === block: score_0 (check id='step_computed_quantities') ===
def score_0(artifact, step, ctx):
    tol_rel = step.get("tolerance_relative", 0.05)
    tol_abs = step.get("tolerance_absolute_low", 1e-20)
    try:
        gamma = artifact["gamma"]
        Lk = artifact["L_k"]
        D = artifact["D"]
        t_k_star = float(artifact["t_k_star"])
        L_k_star = float(artifact["L_k_star"])
    except (KeyError, TypeError, ValueError):
        return 0.0
    expected_len = ctx["t_list_len"]
    if len(gamma) != expected_len or len(Lk) != expected_len or len(D) != expected_len:
        return 0.0
    def array_score(arr, ref_arr):
        total_rel = 0.0
        for a, ref in zip(arr, ref_arr):
            denom = max(abs(ref), tol_abs)
            rel_err = abs(a - ref) / denom if denom != 0 else abs(a - ref)
            total_rel += min(rel_err, 1.0)
        mean_rel = total_rel / max(len(arr), 1)
        return max(0.0, 1.0 - (mean_rel / tol_rel))
    def scalar_score(val, ref_val):
        denom = max(abs(ref_val), tol_abs)
        rel_err = abs(val - ref_val) / denom if denom != 0 else abs(val - ref_val)
        return max(0.0, 1.0 - (rel_err / tol_rel))
    s_gamma = array_score(gamma, ctx["ref_gamma"])
    s_Lk = array_score(Lk, ctx["ref_Lk"])
    s_D = array_score(D, ctx["ref_D"])
    s_tk = scalar_score(t_k_star, ctx["ref_t_k_star"])
    s_Lkstar = scalar_score(L_k_star, ctx["ref_L_k_star"])
    final = (s_gamma + s_Lk + s_D + s_tk + s_Lkstar) / 5.0
    return max(0.0, min(1.0, final))


_SCORERS = {
    'step_computed_quantities': score_0,
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
