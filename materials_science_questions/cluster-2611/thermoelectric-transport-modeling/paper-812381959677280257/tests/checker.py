import os
import json
import csv

# === author imports / helpers ===
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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        ctx = {"steps": {}}
        for step in steps:
            step_id = step["id"]
            ctx["steps"][step_id] = {
                "reference_curves": step.get("reference_curves", {}),
                "tolerance_mape": step.get("tolerance_mape", 0.2),
                "trend_check": step.get("trend_check", None),
                "weight": step["weight"]
            }
        return ctx


# === block: score_0 (check id='power_factor') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        step_id = step["id"]
        info = ctx["steps"][step_id]
        ref_curves = info["reference_curves"]
        tol = info["tolerance_mape"]
        trend_check = info["trend_check"]
        samples = {}
        for row in artifact:
            s = row["sample"]
            conc = float(row["carrier_concentration_cm3"])
            pf = float(row["power_factor_WmK2"])
            samples.setdefault(s, ([], []))
            samples[s][0].append(conc)
            samples[s][1].append(pf)
        for s in samples:
            concs, pfs = samples[s]
            idx = sorted(range(len(concs)), key=lambda i: concs[i])
            samples[s] = ([concs[i] for i in idx], [pfs[i] for i in idx])
        mape_sum = 0.0
        n_points = 0
        for sample, ref_points in ref_curves.items():
            if sample not in samples:
                continue
            concs, pfs = samples[sample]
            for (c_ref, pf_ref) in ref_points:
                if c_ref <= concs[0]:
                    agent_pf = pfs[0]
                elif c_ref >= concs[-1]:
                    agent_pf = pfs[-1]
                else:
                    i = 0
                    while i < len(concs)-1 and concs[i+1] < c_ref:
                        i += 1
                    i = min(i, len(concs)-2)
                    x0, x1 = concs[i], concs[i+1]
                    y0, y1 = pfs[i], pfs[i+1]
                    agent_pf = y0 + (y1-y0)*(c_ref-x0)/(x1-x0)
                mape_sum += abs(agent_pf - pf_ref) / (abs(pf_ref) + 1e-12)
                n_points += 1
        if n_points == 0:
            return 0.0
        mape = mape_sum / n_points
        if mape <= tol:
            mape_score = 1.0
        else:
            mape_score = max(0.0, 1.0 - (mape - tol) / tol)
        trend_score = 1.0
        if trend_check == "power_factor_decreases_with_decreasing_period":
            test_conc = 5e19
            pf_values = {}
            for s in ("JL254", "JL255", "JL256"):
                if s in samples:
                    concs, pfs = samples[s]
                    if test_conc <= concs[0]:
                        pf = pfs[0]
                    elif test_conc >= concs[-1]:
                        pf = pfs[-1]
                    else:
                        i = 0
                        while i < len(concs)-1 and concs[i+1] < test_conc:
                            i += 1
                        i = min(i, len(concs)-2)
                        x0, x1 = concs[i], concs[i+1]
                        y0, y1 = pfs[i], pfs[i+1]
                        pf = y0 + (y1-y0)*(test_conc-x0)/(x1-x0)
                    pf_values[s] = pf
            if all(s in pf_values for s in ("JL254","JL255","JL256")):
                if not (pf_values["JL254"] > pf_values["JL255"] > pf_values["JL256"]):
                    trend_score = 0.0
        final = 0.8 * mape_score + 0.2 * trend_score
        return final


# === block: score_1 (check id='seebeck') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        step_id = step["id"]
        info = ctx["steps"][step_id]
        ref_curves = info["reference_curves"]
        tol = info["tolerance_mape"]
        trend_check = info["trend_check"]
        samples = {}
        for row in artifact:
            s = row["sample"]
            t = float(row["temperature_K"])
            see = float(row["seebeck_uVK"])
            samples.setdefault(s, ([], []))
            samples[s][0].append(t)
            samples[s][1].append(see)
        for s in samples:
            ts, ss = samples[s]
            idx = sorted(range(len(ts)), key=lambda i: ts[i])
            samples[s] = ([ts[i] for i in idx], [ss[i] for i in idx])
        mape_sum = 0.0
        n_points = 0
        for sample, ref_points in ref_curves.items():
            if sample not in samples:
                continue
            ts, ss = samples[sample]
            for (t_ref, see_ref) in ref_points:
                if t_ref <= ts[0]:
                    agent_see = ss[0]
                elif t_ref >= ts[-1]:
                    agent_see = ss[-1]
                else:
                    i = 0
                    while i < len(ts)-1 and ts[i+1] < t_ref:
                        i += 1
                    i = min(i, len(ts)-2)
                    x0, x1 = ts[i], ts[i+1]
                    y0, y1 = ss[i], ss[i+1]
                    agent_see = y0 + (y1-y0)*(t_ref-x0)/(x1-x0)
                mape_sum += abs(agent_see - see_ref) / (abs(see_ref) + 1e-12)
                n_points += 1
        if n_points == 0:
            return 0.0
        mape = mape_sum / n_points
        if mape <= tol:
            mape_score = 1.0
        else:
            mape_score = max(0.0, 1.0 - (mape - tol) / tol)
        trend_score = 1.0
        if trend_check == "seebeck_magnitude_increases_with_decreasing_temperature":
            for s, (ts, ss) in samples.items():
                for i in range(len(ss)-1):
                    if ss[i] > ss[i+1] + 1e-9:
                        trend_score = 0.0
                        break
                if trend_score == 0.0:
                    break
        final = 0.8 * mape_score + 0.2 * trend_score
        return final


# === block: score_2 (check id='conductivity') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        step_id = step["id"]
        info = ctx["steps"][step_id]
        ref_curves = info["reference_curves"]
        tol = info["tolerance_mape"]
        trend_check = info["trend_check"]
        samples = {}
        for row in artifact:
            s = row["sample"]
            t = float(row["temperature_K"])
            sigma = float(row["conductivity_Sm"])
            samples.setdefault(s, ([], []))
            samples[s][0].append(t)
            samples[s][1].append(sigma)
        for s in samples:
            ts, sig = samples[s]
            idx = sorted(range(len(ts)), key=lambda i: ts[i])
            samples[s] = ([ts[i] for i in idx], [sig[i] for i in idx])
        mape_sum = 0.0
        n_points = 0
        for sample, ref_points in ref_curves.items():
            if sample not in samples:
                continue
            ts, sig = samples[sample]
            for (t_ref, sigma_ref) in ref_points:
                if t_ref <= ts[0]:
                    agent_sigma = sig[0]
                elif t_ref >= ts[-1]:
                    agent_sigma = sig[-1]
                else:
                    i = 0
                    while i < len(ts)-1 and ts[i+1] < t_ref:
                        i += 1
                    i = min(i, len(ts)-2)
                    x0, x1 = ts[i], ts[i+1]
                    y0, y1 = sig[i], sig[i+1]
                    agent_sigma = y0 + (y1-y0)*(t_ref-x0)/(x1-x0)
                mape_sum += abs(agent_sigma - sigma_ref) / (abs(sigma_ref) + 1e-12)
                n_points += 1
        if n_points == 0:
            return 0.0
        mape = mape_sum / n_points
        if mape <= tol:
            mape_score = 1.0
        else:
            mape_score = max(0.0, 1.0 - (mape - tol) / tol)
        trend_score = 1.0
        if trend_check == "conductivity_decreases_with_decreasing_temperature":
            for s, (ts, sig) in samples.items():
                for i in range(len(sig)-1):
                    if sig[i] > sig[i+1] + 1e-9:
                        trend_score = 0.0
                        break
                if trend_score == 0.0:
                    break
        final = 0.8 * mape_score + 0.2 * trend_score
        return final


_SCORERS = {
    'power_factor': score_0,
    'seebeck': score_1,
    'conductivity': score_2,
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
