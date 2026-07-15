import os
import json
import csv

# === author imports / helpers ===
import json, csv, os


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
    return spec


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance_eV']
    cations = ['Li', 'Na', 'K']
    vals = {}
    errors = []
    for cat in cations:
        if cat not in artifact:
            return 0.0
        v = float(artifact[cat])
        vals[cat] = v
        errors.append(abs(v - gold[cat]))
    max_err = max(errors)
    trend_ok = vals['Li'] < vals['Na'] - 1e-9 and vals['Na'] < vals['K'] - 1e-9
    if not trend_ok:
        return 0.0
    if max_err <= tol:
        return 1.0
    else:
        # linear decay to zero at 3*tol
        decay = max(0.0, 1.0 - (max_err - tol) / (2 * tol))
        return round(decay, 4)


# === block: score_1 (check id='bader_charges_dipoles') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tols = step['tolerances']
    cations = ['Li', 'Na', 'K']
    metrics = ['O_charge', 'OH_dipole_D', 'PtO_dipole_D']
    tol_vals = {'O_charge': tols['O_charge'], 'OH_dipole_D': tols['dipole_D'], 'PtO_dipole_D': tols['dipole_D']}
    scores = []
    for met in metrics:
        vals = {}
        errs = []
        for cat in cations:
            if cat not in artifact or met not in artifact[cat]:
                return 0.0
            v = float(artifact[cat][met])
            vals[cat] = v
            errs.append(abs(v - gold[cat][met]))
        max_err = max(errs)
        # Determine ordering
        if met == 'O_charge':
            trend_ok = vals['Li'] < vals['Na'] - 1e-9 and vals['Na'] < vals['K'] - 1e-9
        else:
            trend_ok = vals['Li'] > vals['Na'] + 1e-9 and vals['Na'] > vals['K'] + 1e-9
        if not trend_ok:
            scores.append(0.0)
        else:
            if max_err <= tol_vals[met]:
                scores.append(1.0)
            else:
                decay = max(0.0, 1.0 - (max_err - tol_vals[met]) / (2 * tol_vals[met]))
                scores.append(decay)
    return round(sum(scores) / len(scores), 4)


# === block: score_2 (check id='free_energy') ===
def score_2(artifact, step, ctx):
    cols = step['required_columns']
    if not isinstance(artifact, list) or len(artifact) < 5:
        return 0.0
    for row in artifact:
        for c in cols:
            if c not in row:
                return 0.0
    rows = artifact
    n = len(rows)
    ordering_correct = 0
    for row in rows:
        try:
            li = float(row['G_ad_OH_Li'])
            na = float(row['G_ad_OH_Na'])
            k = float(row['G_ad_OH_K'])
        except:
            return 0.0
        if li < na - 1e-9 and na < k - 1e-9:
            ordering_correct += 1
    ord_score = ordering_correct / n if n > 0 else 0.0
    # monotonicity: non-increasing with potential_V
    cations = ['G_ad_OH_Li', 'G_ad_OH_Na', 'G_ad_OH_K']
    mono_score = 0
    for col in cations:
        vals = []
        for row in rows:
            vals.append(float(row[col]))
        mono = True
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1] + 1e-9:
                mono = False
                break
        if mono:
            mono_score += 1
    mono_score /= len(cations)
    return round(0.7 * ord_score + 0.3 * mono_score, 4)


_SCORERS = {
    'adsorption_energies': score_0,
    'bader_charges_dipoles': score_1,
    'free_energy': score_2,
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
