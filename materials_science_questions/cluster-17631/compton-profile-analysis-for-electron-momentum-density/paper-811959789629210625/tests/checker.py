import os
import json
import csv

# === author imports / helpers ===
import csv
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
    ref_band = {}
    tol_band = {}
    ref_comp = {}
    mad_thresh = 0.3
    decline = 0.3
    for step in spec.get('steps', []):
        sid = step['id']
        if sid == 'band_gaps':
            ref_band = step.get('hidden_reference', {})
            tol_band = step.get('tolerances', {})
        elif sid == 'compton_profiles':
            for row in step.get('hidden_gold', []):
                key = (row['compound'], float(row['p_z']))
                ref_comp[key] = float(row['J_total'])
            mad_thresh = float(step.get('mad_threshold', 0.3))
            decline = float(step.get('decline_factor', 0.3))
        elif sid == 'eved_profiles':
            pass
    return {
        'band_ref': ref_band,
        'band_tol': tol_band,
        'compton_ref': ref_comp,
        'mad_threshold': mad_thresh,
        'decline_factor': decline,
    }


# === block: score_0 (check id='band_gaps') ===
def score_0(artifact, step, ctx):
    compound_ref = step.get('hidden_reference', {})
    tol = step.get('tolerances', {})
    passes = 0
    total = 0
    for row in artifact:
        c = row.get('compound')
        if c not in compound_ref:
            continue
        try:
            vL = float(row['Eg_L'])
            vG = float(row['Eg_Gamma'])
        except (ValueError, KeyError):
            continue
        if abs(vL - compound_ref[c]['Eg_L']) <= tol['Eg_L']:
            passes += 1
        if abs(vG - compound_ref[c]['Eg_Gamma']) <= tol['Eg_Gamma']:
            passes += 1
        total += 2
    if total == 0:
        return 0.0
    return passes / total


# === block: score_1 (check id='compton_profiles') ===
def score_1(artifact, step, ctx):
    ref = ctx['compton_ref']
    threshold = ctx['mad_threshold']
    decline = ctx['decline_factor']
    agent = {}
    for row in artifact:
        try:
            key = (row['compound'], float(row['p_z']))
            agent[key] = float(row['J_total'])
        except (ValueError, KeyError):
            continue
    compounds = sorted(set(k[0] for k in ref.keys()))
    scores = []
    for comp in compounds:
        diffs = []
        for (c, pz), jref in ref.items():
            if c == comp and (c, pz) in agent:
                diffs.append(abs(agent[(c, pz)] - jref))
        if not diffs:
            scores.append(0.0)
            continue
        mad = sum(diffs) / len(diffs)
        if mad <= threshold:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (mad - threshold) / decline))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='eved_profiles') ===
def score_2(artifact, step, ctx):
    row0 = None
    for row in artifact:
        try:
            if abs(float(row['p_z_over_pF'])) < 1e-9:
                row0 = row
                break
        except (ValueError, KeyError):
            continue
    if row0 is None:
        return 0.0
    J_PbS = float(row0.get('J_PbS', 0.0))
    J_PbSe = float(row0.get('J_PbSe', 0.0))
    return 1.0 if J_PbSe > J_PbS else 0.0


_SCORERS = {
    'band_gaps': score_0,
    'compton_profiles': score_1,
    'eved_profiles': score_2,
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
