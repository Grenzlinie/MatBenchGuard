import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    return {"gold_chi": spec.get("gold_chi", {}), "tolerance": spec.get("gold_chi_tolerance", 0.2)}


# === block: score_0 (check id='step_01_thermal_properties') ===
def score_0(artifact, step, ctx):
    tgt = {20: (5.0, 0.2), 60: (100.0/60.0, 0.6), 90: (100.0/90.0, 0.9)}
    rows = [row for row in artifact if all(col in row for col in ['n_constrictions','constriction_width_nm','relative_thermal_resistance','relative_thermal_conductivity'])]
    groups = {}
    for r in rows:
        b = int(r['constriction_width_nm'])
        groups.setdefault(b, []).append((int(r['n_constrictions']), float(r['relative_thermal_resistance']), float(r['relative_thermal_conductivity'])))
    def check_monotonic(seq, increasing=True):
        for i in range(len(seq)-1):
            if increasing and seq[i] > seq[i+1]: return False
            if not increasing and seq[i] < seq[i+1]: return False
        return True
    passed, total = 0, 0
    for b, vals in groups.items():
        vals.sort(key=lambda x: x[0])
        res_vals = [v[1] for v in vals]
        cond_vals = [v[2] for v in vals]
        total += 4
        if len(vals) >= 2:
            if check_monotonic(res_vals, True): passed += 1
            if check_monotonic(cond_vals, False): passed += 1
        if len(vals) > 0:
            res_last = res_vals[-1]
            cond_last = cond_vals[-1]
            Tr_inv, Tr = tgt[b]
            if Tr_inv > 0 and abs(res_last - Tr_inv) / Tr_inv <= 0.3:
                passed += 1
            if Tr > 0 and abs(cond_last - Tr) / Tr <= 0.3:
                passed += 1
    score = passed / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='step_02_fitted_chi') ===
def score_1(artifact, step, ctx):
    step01_path = os.path.join('/app/outputs', 'step_01_thermal_properties.csv')
    if not os.path.exists(step01_path):
        return 0.0
    with open(step01_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    rel_res = {}
    for r in rows:
        if int(r.get('constriction_width_nm', 0)) == 20:
            n = int(r['n_constrictions'])
            rel_res[n] = float(r['relative_thermal_resistance'])
    if 1 not in rel_res:
        return 0.0
    Tr_inv = 5.0
    rel_res_N1 = rel_res[1]
    chi_comp = {}
    for N in range(1, 11):
        if N not in rel_res:
            return 0.0
        num = rel_res[N] - Tr_inv
        den = N * (rel_res_N1 - 1) - (Tr_inv - 1)
        if abs(den) < 1e-9:
            return 0.0
        chi = num / den
        chi_comp[str(N)] = chi
    gold_chi = ctx['gold_chi']
    tol = ctx['tolerance']
    matches, total = 0, 0
    for N_key, gold_val in gold_chi.items():
        if N_key in chi_comp:
            total += 1
            if abs(chi_comp[N_key] - gold_val) <= tol:
                matches += 1
    score = matches / total if total > 0 else 0.0
    return score


_SCORERS = {
    'step_01_thermal_properties': score_0,
    'step_02_fitted_chi': score_1,
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
