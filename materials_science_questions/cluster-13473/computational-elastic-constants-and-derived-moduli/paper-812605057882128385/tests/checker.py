import os
import json
import csv

# === author imports / helpers ===
import csv, os


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
    step = spec["steps"][0]
    params = step.get("params", {})
    return {
        "tol_xz_pp": params.get("tolerance_mu_xz_pp", 0.15),
        "tol_xy_pp": params.get("tolerance_mu_xy_pp", 0.10),
        "target_xz": params.get("target_decrease_mu_xz", 0.5),
        "target_xy": params.get("target_decrease_mu_xy", 0.15),
        "min_rows": params.get("min_rows", 3),
    }


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if len(rows) < ctx["min_rows"]:
        return 0.0
    ratios = [float(r["ratio_Lx_Lz"]) for r in rows]
    mus_xz = [float(r["mu_xz"]) for r in rows]
    mus_xy = [float(r["mu_xy"]) for r in rows]
    # sort by ratio ascending to find min and max
    pairs = sorted(zip(ratios, mus_xz, mus_xy), key=lambda x: x[0])
    ratios_sort = [p[0] for p in pairs]
    mus_xz_sort = [p[1] for p in pairs]
    mus_xy_sort = [p[2] for p in pairs]
    max_ratio = ratios_sort[-1]
    min_ratio = ratios_sort[0]
    if min_ratio >= max_ratio:
        return 0.0
    mu_xz_max = mus_xz_sort[-1]
    mu_xz_min = mus_xz_sort[0]
    mu_xy_max = mus_xy_sort[-1]
    mu_xy_min = mus_xy_sort[0]
    if mu_xz_max == 0.0 or mu_xy_max == 0.0:
        return 0.0
    decrease_xz = (mu_xz_max - mu_xz_min) / mu_xz_max
    decrease_xy = (mu_xy_max - mu_xy_min) / mu_xy_max
    score_xz = 1.0 if abs(decrease_xz - ctx["target_xz"]) <= ctx["tol_xz_pp"] else 0.0
    score_xy = 1.0 if abs(decrease_xy - ctx["target_xy"]) <= ctx["tol_xy_pp"] else 0.0
    # Require monotonic increase: as ratio increases (sorted ascending), both moduli should increase.
    mono_violation = False
    for i in range(1, len(pairs)):
        if mus_xz_sort[i] < mus_xz_sort[i-1] - 1e-9:
            mono_violation = True
            break
        if mus_xy_sort[i] < mus_xy_sort[i-1] - 1e-9:
            mono_violation = True
            break
    score_mono = 0.0 if mono_violation else 1.0
    return 0.4 * score_xz + 0.4 * score_xy + 0.2 * score_mono


_SCORERS = {
    'step_2': score_0,
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
