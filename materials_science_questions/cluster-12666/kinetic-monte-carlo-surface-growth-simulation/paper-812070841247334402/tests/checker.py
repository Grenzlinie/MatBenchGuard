import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import re


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
    return {
        'overstep_target': 2.0,
        'overstep_tolerance': 1.0,
        'transition_lower': 0.1,
        'transition_upper': 3.0
    }


# === block: score_0 (check id='morphology_table') ===
def score_0(artifact, step, ctx):
    # Load CSV and check monotonicity
    if not artifact:
        return 0.0
    # Extract constant runs (delta_mu_kT not empty)
    rows = []
    for r in artifact:
        try:
            dmu = r.get('delta_mu_kT', '').strip()
            if dmu == '':
                continue
            dmu_val = float(dmu)
            branch = int(r.get('branch_count', '').strip())
            rows.append((dmu_val, branch))
        except (ValueError, TypeError):
            continue
    if len(rows) < 2:
        return 0.0
    rows.sort(key=lambda x: x[0])
    branch_vals = [b for _, b in rows]
    # branch_count should be non-decreasing with increasing delta_mu_kT
    if all(branch_vals[i] <= branch_vals[i+1] for i in range(len(branch_vals)-1)):
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='transition_estimate') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    content = artifact.strip()
    lines = content.split('\n')
    transition_val = None
    overstep_val = None
    for line in lines:
        line = line.strip()
        m = re.match(r'Transition_Δμ_kT\s*=\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)', line)
        if m:
            transition_val = float(m.group(1))
            continue
        m = re.match(r'Overstep_kJ_per_mol\s*=\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)', line)
        if m:
            overstep_val = float(m.group(1))
    scores = []
    if transition_val is not None:
        lower = ctx['transition_lower']
        upper = ctx['transition_upper']
        if lower <= transition_val <= upper:
            scores.append(0.5)
        else:
            scores.append(0.0)
    else:
        scores.append(0.0)
    if overstep_val is not None:
        diff = abs(overstep_val - ctx['overstep_target'])
        if diff <= ctx['overstep_tolerance']:
            scores.append(0.5)
        else:
            scores.append(0.0)
    else:
        # overstep optional; no penalty for missing
        scores.append(0.0)
    return sum(scores)


# === block: score_2 (check id='final_grid') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    text = artifact.strip()
    if not text:
        return 0.0
    try:
        lines = text.split('\n')
        grid = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            for p in parts:
                if p not in ('0', '1'):
                    raise ValueError('non-binary')
            row = [int(p) for p in parts]
            grid.append(row)
        # check rectangular
        if not grid:
            return 0.0
        n_cols = len(grid[0])
        if n_cols == 0:
            return 0.0
        for row in grid:
            if len(row) != n_cols:
                return 0.0
        return 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'morphology_table': score_0,
    'transition_estimate': score_1,
    'final_grid': score_2,
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
