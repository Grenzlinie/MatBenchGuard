import os
import json
import csv

# === author imports / helpers ===
import math, os


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
    const = spec.get("constants", {})
    return {"const": const}


# === block: score_0 (check id='step_01_structure') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    # at least 30 rows total
    if len(artifact) < 30:
        return 0.0
    # every (T,n) combo must be present
    expected_combos = {
        (10.0, 1e20), (10.0, 1e21), (10.0, 1e22),
        (77.0, 1e20), (77.0, 1e21), (77.0, 1e22),
        (300.0, 1e20), (300.0, 1e21), (300.0, 1e22)
    }
    present = set()
    for row in artifact:
        try:
            T = float(row["temperature_K"])
            n = float(row["carrier_concentration_m3"])
        except (KeyError, ValueError):
            continue
        # match T
        t_match = None
        for t in [10.0, 77.0, 300.0]:
            if abs(T - t) < 1e-4:
                t_match = t
                break
        if t_match is None:
            continue
        # match n (relative tolerance)
        n_match = None
        for nt in [1e20, 1e21, 1e22]:
            if abs(n - nt) / max(abs(nt), 1.0) < 1e-6:
                n_match = nt
                break
        if n_match is not None:
            present.add((t_match, n_match))
    if present == expected_combos:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_01_recompute') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    const = ctx["const"]
    e14 = const["e14"]
    kappa = const["kappa"]
    eps0 = const["epsilon0"]
    rho = const["rho"]
    c44 = const["c44"]
    kB = const["kB"]
    eps = kappa * eps0
    vT = math.sqrt(c44 / rho)
    vT3 = vT ** 3
    tol_rel = step.get("tolerance_relative", 1e-10)
    ok = 0
    total = 0
    for row in artifact:
        try:
            T = float(row["temperature_K"])
            n = float(row["carrier_concentration_m3"])
            P = float(row["flux_intensity_W_m2"])
            ratio = float(row["ratio_C_over_C0"])
        except (KeyError, ValueError):
            continue
        T_energy = kB * T
        exponent = (e14**2 * P) / (8.0 * eps * n * T_energy * rho * vT3)
        try:
            expected = math.exp(exponent)
        except OverflowError:
            expected = math.inf if exponent > 0 else 0.0
        # comparison
        if math.isinf(expected):
            if math.isinf(ratio) and (ratio > 0) == (expected > 0):
                ok += 1
            # else fail
        elif math.isinf(ratio):
            pass
        else:
            denom = max(abs(expected), 1e-300)
            rel_err = abs(ratio - expected) / denom
            if rel_err <= tol_rel:
                ok += 1
        total += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'step_01_structure': score_0,
    'step_01_recompute': score_1,
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
