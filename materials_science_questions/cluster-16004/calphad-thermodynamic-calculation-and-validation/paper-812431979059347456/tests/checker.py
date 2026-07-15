import os
import json
import csv

# === author imports / helpers ===
import math
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
    steps = spec['steps']
    step = steps[0]  # only one step
    comps = step['compositions']
    k = step['constants']['k']
    m = step['constants']['m']
    G = step['constants']['G']
    Gb3 = step['constants']['Gb3']
    expected = {}
    for c in comps:
        tau = math.exp(c['A'])
        W = m * k / c['B']
        # n^3 = (W^2 / tau) * (4*G / (Gb3^2))
        n_cube = (W**2 / tau) * (4.0 * G / (Gb3**2))
        n = n_cube ** (1.0/3.0)
        U_eV = W**2 / (Gb3 * n**2 * math.sqrt(c['c_frac']))
        U_meV = U_eV * 1000.0
        expected[c['composition']] = {
            'tau_o_MPa': tau,
            'W_o_eV': W,
            'n': n,
            'U_meV': U_meV
        }
    return {'expected': expected, 'peak_c_at_pct': step['peak_c_at_pct'], 'tolerances': step['tolerances']}


# === block: score_0 (check id='step_01_compute_parameters') ===
def score_0(artifact, step, ctx):
    tol = step['tolerances']
    expected = ctx['expected']
    peak_c = ctx['peak_c_at_pct']

    # assume artifact is list of dicts from csv.DictReader
    # First build lookup by composition (case-insensitive)
    agent_rows = {}
    for row in artifact:
        comp = row.get('composition', '').strip()
        agent_rows[comp.lower()] = row

    # Count correct values and check peak
    cols = ['tau_o_MPa', 'W_o_eV', 'n', 'U_meV']
    num_correct = 0
    total_cells = 0
    tau_max = -float('inf')
    max_c_at = None

    for comp_name, exp in expected.items():
        row = agent_rows.get(comp_name.lower())
        if row is None:
            # missing composition, count 0 correct for its 4 cells
            total_cells += 4
            continue
        total_cells += 4
        for col in cols:
            try:
                agent_val = float(row[col])
            except (ValueError, TypeError, KeyError):
                continue
            expected_val = exp[col]
            if abs(agent_val - expected_val) <= tol.get(col, 1e-9):
                num_correct += 1

    # peak check: find row with max W_o_eV
    for row in artifact:
        try:
            w = float(row.get('W_o_eV', -float('inf')))
            if w > tau_max:
                tau_max = w
                max_c_at = float(row.get('c_at_pct', -1))
        except (ValueError, TypeError):
            pass

    peak_ok = (max_c_at is not None and abs(max_c_at - peak_c) < 0.01)

    per_cell_weight = 0.8 / max(total_cells, 1)  # only count expected compositions
    score = num_correct * per_cell_weight + (0.2 if peak_ok else 0.0)
    return min(score, 1.0)


_SCORERS = {
    'step_01_compute_parameters': score_0,
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
