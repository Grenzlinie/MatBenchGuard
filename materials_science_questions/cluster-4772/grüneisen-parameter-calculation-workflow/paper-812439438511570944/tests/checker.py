import os
import json
import csv

# === author imports / helpers ===
import csv, os, math

try:
    import numpy as np
    from scipy.optimize import curve_fit
except ImportError:
    np = None
    curve_fit = None


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
    steps = spec.get("steps", [])
    gold_params = {}
    param_tols = {}
    volumes = []
    pressure_tol = 0.10
    for step in steps:
        if step["id"] == "reduced_isotherm_data_score":
            gold_params = step.get("gold_eos_params", {})
            param_tols = step.get("param_tolerances", {})
            volumes = step.get("pressure_consistency_volumes", [])
            pressure_tol = step.get("pressure_consistency_rel_tol", 0.10)
            break
    if not gold_params:
        for step in steps:
            if step["id"] == "reduced_isotherm_parameters_score":
                gold_params = step.get("gold_eos_params", {})
                param_tols = step.get("param_tolerances", {})
                break
    return {
        "gold_params": gold_params,
        "param_tols": param_tols,
        "volumes": volumes,
        "pressure_tol": pressure_tol
    }


# === block: score_0 (check id='reduced_isotherm_data_score') ===
def score_0(artifact, step, ctx):
    # Load CSV and group by element
    artifact_path = os.path.join("/app/outputs", "reduced_isotherm_data.csv")
    if not os.path.exists(artifact_path):
        return 0.0

    # Guard against missing numpy/scipy in the sandbox
    if np is None or curve_fit is None:
        return 0.0

    rows = []
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    # Group points
    data = {}
    for r in rows:
        elem = r.get("element").strip()
        try:
            X = float(r["reduced_volume_X"])
            P = float(r["pressure_GPa"])
        except (ValueError, KeyError):
            continue
        data.setdefault(elem, []).append((X, P))

    gold_params = ctx.get("gold_params", {})
    param_tols = ctx.get("param_tols", {})
    volumes = ctx.get("volumes", [0.75, 0.85, 0.95])
    pressure_tol = ctx.get("pressure_tol", 0.10)

    def universal_eos(X, B0, eta, beta, xi, delta):
        x13 = np.power(X, 1.0/3.0)
        factor = (1.0 - x13) / np.power(X, 2.0/3.0)
        exponent = eta*(1.0 - x13) + beta*(1.0 - x13)**2 + xi*(1.0 - x13)**3 + delta*(1.0 - x13)**4
        return 3.0 * B0 * factor * np.exp(exponent)

    def fit_and_score_metal(elem, points):
        if elem not in gold_params:
            return 0.0
        gold = gold_params[elem]
        Xs = np.array([p[0] for p in points])
        Ps = np.array([p[1] for p in points])
        if len(Xs) < 5:
            return 0.0
        # initial guess from gold params to help convergence
        p0 = [gold["B0"], gold["eta"], gold["beta"], gold["xi"], gold["delta"]]
        try:
            popt, _ = curve_fit(universal_eos, Xs, Ps, p0=p0, maxfev=10000)
        except Exception:
            return 0.0
        # parameter comparison
        param_names = ["B0", "eta", "beta", "xi", "delta"]
        pass_count = 0
        for i, name in enumerate(param_names):
            val = popt[i]
            gval = gold[name]
            tol = param_tols.get(name, 0.2)
            rel_err = abs(val - gval) / max(abs(gval), 1e-12)
            if rel_err <= tol:
                pass_count += 1
        param_score = pass_count / 5.0
        # pressure consistency at hidden volumes
        if not volumes:
            return param_score
        pass_pressure = 0
        for X in volumes:
            P_gold = universal_eos(X, *p0)  # p0 is gold params
            P_agent = universal_eos(X, *popt)
            rel_err_p = abs(P_agent - P_gold) / max(abs(P_gold), 1e-12)
            if rel_err_p <= pressure_tol:
                pass_pressure += 1
        pressure_score = pass_pressure / len(volumes)
        # combine
        metal_score = 0.6 * param_score + 0.4 * pressure_score
        return metal_score

    metals = ["Cu", "Ta", "Mo", "Pt", "Au"]
    scores = []
    for m in metals:
        pts = data.get(m, [])
        if not pts:
            scores.append(0.0)
        else:
            scores.append(fit_and_score_metal(m, pts))
    return float(np.mean(scores)) if scores else 0.0


# === block: score_1 (check id='reduced_isotherm_parameters_score') ===
def score_1(artifact, step, ctx):
    artifact_path = os.path.join("/app/outputs", "reduced_isotherm_parameters.csv")
    if not os.path.exists(artifact_path):
        return 0.0
    rows = []
    try:
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    except Exception:
        return 0.0
    if not rows:
        return 0.0

    gold_params = ctx.get("gold_params", {})
    param_tols = ctx.get("param_tols", {})

    param_names = ["B0", "eta", "beta", "xi", "delta"]
    metals = ["Cu", "Ta", "Mo", "Pt", "Au"]
    agent_params = {}
    for r in rows:
        elem = r.get("element").strip()
        try:
            vals = {"B0": float(r["B0"]), "eta": float(r["eta"]), "beta": float(r["beta"]), "xi": float(r["xi"]), "delta": float(r["delta"])}
        except (ValueError, KeyError):
            continue
        agent_params[elem] = vals

    scores = []
    for m in metals:
        gold = gold_params.get(m)
        agent = agent_params.get(m)
        if not gold or not agent:
            scores.append(0.0)
            continue
        pass_count = 0
        for name in param_names:
            gval = gold[name]
            aval = agent[name]
            tol = param_tols.get(name, 0.2)
            rel_err = abs(aval - gval) / max(abs(gval), 1e-12)
            if rel_err <= tol:
                pass_count += 1
        scores.append(pass_count / 5.0)

    return float(np.mean(scores)) if scores else 0.0


_SCORERS = {
    'reduced_isotherm_data_score': score_0,
    'reduced_isotherm_parameters_score': score_1,
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
