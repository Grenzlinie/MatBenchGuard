import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import math


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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='check_corr_010') ===
def score_0(artifact, step, ctx):
    outputs_dir = ctx["outputs_dir"]
    filepath = os.path.join(outputs_dir, "correlation_functions_XB_0.100.csv")
    try:
        with open(filepath) as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception:
        return 0.0

    if not rows:
        return 0.0
    # Robustly skip any header or non-data rows
    data_rows = []
    for row in rows:
        if not row:
            continue
        try:
            r, rho_G, psi = map(float, row[:3])
            data_rows.append((r, rho_G, psi))
        except (ValueError, TypeError):
            continue
    if not data_rows:
        return 0.0
    rs = [r for r,_,_ in data_rows]
    rhos = [rho for _,rho,_ in data_rows]
    psis = [psi for _,_,psi in data_rows]
    max_r = max(rs)
    indices = [i for i, r in enumerate(rs) if r >= 0.9 * max_r]
    if not indices:
        return 0.0
    mean_rho = sum(rhos[i] for i in indices) / len(indices)
    mean_psi = sum(psis[i] for i in indices) / len(indices)
    score = 0.0
    if mean_rho >= 0.5:
        score += 0.5
    if mean_psi >= 0.5:
        score += 0.5
    return score


# === block: score_1 (check id='check_corr_0148') ===
def score_1(artifact, step, ctx):
    outputs_dir = ctx["outputs_dir"]
    filepath = os.path.join(outputs_dir, "correlation_functions_XB_0.148.csv")
    try:
        with open(filepath) as f:
            reader = csv.reader(f)
            rows = [ [float(x) for x in row] for row in reader if row ]
    except Exception:
        return 0.0

    if not rows:
        return 0.0
    rs = [r for r,_,_ in rows]
    rhos = [rho for _,rho,_ in rows]
    psis = [psi for _,_,psi in rows]
    max_r = max(rs)
    indices = [i for i, r in enumerate(rs) if r >= 0.9 * max_r]
    if not indices:
        return 0.0
    mean_rho = sum(rhos[i] for i in indices) / len(indices)
    mean_psi = sum(psis[i] for i in indices) / len(indices)
    score = 0.0
    if mean_rho <= 0.25:
        score += 0.5
    if mean_psi >= 0.3:
        score += 0.5
    return score


# === block: score_2 (check id='check_corr_0172') ===
def score_2(artifact, step, ctx):
    outputs_dir = ctx["outputs_dir"]
    filepath = os.path.join(outputs_dir, "correlation_functions_XB_0.172.csv")
    try:
        with open(filepath) as f:
            reader = csv.reader(f)
            rows = [ [float(x) for x in row] for row in reader if row ]
    except Exception:
        return 0.0

    if not rows:
        return 0.0
    rs = [r for r,_,_ in rows]
    rhos = [rho for _,rho,_ in rows]
    psis = [psi for _,_,psi in rows]
    max_r = max(rs)
    indices = [i for i, r in enumerate(rs) if r >= 0.9 * max_r]
    if not indices:
        return 0.0
    mean_rho = sum(rhos[i] for i in indices) / len(indices)
    mean_psi = sum(psis[i] for i in indices) / len(indices)
    score = 0.0
    if mean_rho <= 0.25:
        score += 0.5
    if mean_psi >= 0.3:
        score += 0.5
    return score


# === block: score_3 (check id='check_corr_025') ===
def score_3(artifact, step, ctx):
    outputs_dir = ctx["outputs_dir"]
    filepath = os.path.join(outputs_dir, "correlation_functions_XB_0.250.csv")
    try:
        with open(filepath) as f:
            reader = csv.reader(f)
            rows = [ [float(x) for x in row] for row in reader if row ]
    except Exception:
        return 0.0

    if not rows:
        return 0.0
    rs = [r for r,_,_ in rows]
    rhos = [rho for _,rho,_ in rows]
    psis = [psi for _,_,psi in rows]
    max_r = max(rs)
    indices = [i for i, r in enumerate(rs) if r >= 0.9 * max_r]
    if not indices:
        return 0.0
    mean_rho = sum(rhos[i] for i in indices) / len(indices)
    mean_psi = sum(psis[i] for i in indices) / len(indices)
    score = 0.0
    if mean_rho <= 0.25:
        score += 0.5
    if mean_psi <= 0.25:
        score += 0.5
    return score


# === block: score_4 (check id='check_window') ===
def score_4(artifact, step, ctx):
    try:
        lower = float(artifact["lower_bound"])
        upper = float(artifact["upper_bound"])
    except (KeyError, TypeError, ValueError):
        return 0.0

    diff_lower = abs(lower - 0.148)
    if diff_lower <= 0.01:
        s_lower = 1.0
    else:
        s_lower = max(0.0, 1.0 - (diff_lower - 0.01) / 0.04)

    diff_upper = abs(upper - 0.199)
    if diff_upper <= 0.025:
        s_upper = 1.0
    else:
        s_upper = max(0.0, 1.0 - (diff_upper - 0.025) / 0.05)

    return (s_lower + s_upper) / 2.0


_SCORERS = {
    'check_corr_010': score_0,
    'check_corr_0148': score_1,
    'check_corr_0172': score_2,
    'check_corr_025': score_3,
    'check_window': score_4,
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
