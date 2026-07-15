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


# === block: score_0 (check id='step1_lattice') ===
def score_0(artifact, step, ctx):
    import math
    gold = step['gold']
    tol = step.get('tolerances', {'a': 0.05, 'c': 0.05, 'V': 0.1})
    tol_a = tol.get('a', 0.05)
    tol_c = tol.get('c', 0.05)
    tol_v = tol.get('V', 0.1)
    compounds = ['CuAlS2', 'CuGaS2', 'CuInS2', 'AgGaS2']
    total = 0.0
    for comp in compounds:
        cscore = 0.0
        if comp in artifact and isinstance(artifact[comp], dict):
            a_diff = abs(artifact[comp].get('a', 0) - gold[comp]['a'])
            c_diff = abs(artifact[comp].get('c', 0) - gold[comp]['c'])
            v_diff = abs(artifact[comp].get('V', 0) - gold[comp]['V'])
            a_ok = 1.0 if a_diff <= tol_a else 0.0
            c_ok = 1.0 if c_diff <= tol_c else 0.0
            v_ok = 1.0 if v_diff <= tol_v else 0.0
            cscore = 0.4 * a_ok + 0.4 * c_ok + 0.2 * v_ok
        total += cscore
    avg = total / len(compounds) if compounds else 0.0
    return avg


# === block: score_1 (check id='step2_gaps') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tol = step.get('tolerance', 0.2)
    compounds = ['CuAlS2', 'CuGaS2', 'CuInS2', 'AgGaS2']
    total = 0.0
    for comp in compounds:
        if comp in artifact and isinstance(artifact[comp], dict):
            gap_val = artifact[comp].get('uncorrected_band_gap')
            if gap_val is None:
                continue
            diff = abs(gap_val - gold[comp]['uncorrected_band_gap'])
            if diff <= tol:
                total += 1.0
    avg = total / len(compounds) if compounds else 0.0
    return avg


# === block: score_2 (check id='step3_optical') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tol_n0 = step.get('tol_n0', 0.1)
    tol_sell = step.get('tol_sellmeier', 0.1)
    compounds = ['CuAlS2', 'CuGaS2', 'CuInS2', 'AgGaS2']
    n0_scores = []
    sell_scores = []
    for comp in compounds:
        if comp not in artifact or not isinstance(artifact[comp], dict):
            n0_scores.append(0.0)
            sell_scores.append(0.0)
            continue
        n0_val = artifact[comp].get('refractive_index_n0')
        if n0_val is None:
            n0_scores.append(0.0)
        else:
            diff = abs(n0_val - gold[comp]['n0'])
            n0_scores.append(1.0 if diff <= tol_n0 else 0.0)
        params = artifact[comp].get('sellmeier_params')
        g_params = gold[comp]['sellmeier']
        if not isinstance(params, dict):
            sell_scores.append(0.0)
            continue
        param_score = 0.0
        n_params = 0
        for par in ['A', 'B', 'C', 'D']:
            if par in params and par in g_params:
                val = params[par]
                gval = g_params[par]
                n_params += 1
                if gval != 0:
                    rel = abs(val - gval) / abs(gval)
                else:
                    rel = abs(val - gval) if val != 0 else 0.0
                param_score += 1.0 if rel <= tol_sell else 0.0
        if n_params > 0:
            param_score /= n_params
        else:
            param_score = 0.0
        sell_scores.append(param_score)
    n0_avg = sum(n0_scores) / len(compounds) if compounds else 0.0
    sell_avg = sum(sell_scores) / len(compounds) if compounds else 0.0
    return 0.5 * n0_avg + 0.5 * sell_avg


_SCORERS = {
    'step1_lattice': score_0,
    'step2_gaps': score_1,
    'step3_optical': score_2,
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
