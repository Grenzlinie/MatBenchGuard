import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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


# === block: score_0 (check id='equilibrium_delta_value') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict) or 'delta' not in data:
        return 0.0
    delta = float(data['delta'])
    target = step.get('target', 0.0039)
    tol_rel = step.get('tolerance_rel', 0.05)
    if target <= 0:
        return 0.0
    rel_err = abs(delta - target) / target
    if rel_err <= tol_rel:
        return 1.0
    elif rel_err <= 2 * tol_rel:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='oxygen_displacement_consistency') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact
        if not isinstance(data, dict) or 'delta' not in data or 'oxygen_displacement_A' not in data:
            return 0.0
        delta = float(data['delta'])
        disp = float(data['oxygen_displacement_A'])
        expected = delta * 5.468
        if expected == 0:
            return 0.0
        rel_err = abs(disp - expected) / abs(expected)
        if rel_err < 0.001:
            return 1.0
        else:
            return 0.0


# === block: score_2 (check id='csv_recompute_delta_match') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        min_delta = None
        min_energy = float('inf')
        for row in rows:
            try:
                d = float(row['delta'])
                e = float(row['energy_TIR'])
            except (KeyError, ValueError):
                continue
            if e < min_energy:
                min_energy = e
                min_delta = d
        if min_delta is None:
            return 0.0
        target = step.get('target', 0.0039)
        tol_rel = step.get('tolerance_rel', 0.03)
        if target <= 0:
            return 0.0
        rel_err = abs(min_delta - target) / target
        if rel_err <= tol_rel:
            return 1.0
        else:
            return 0.0


# === block: score_3 (check id='csv_energy_ordering') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        min_delta = None
        min_energy = float('inf')
        delta_energy_map = {}
        for row in rows:
            try:
                d = float(row['delta'])
                e_tir = float(row['energy_TIR'])
                e_allen = float(row['energy_Allen'])
            except (KeyError, ValueError):
                continue
            delta_energy_map[d] = (e_tir, e_allen)
            if e_tir < min_energy:
                min_energy = e_tir
                min_delta = d
        if min_delta is None or min_delta not in delta_energy_map:
            return 0.0
        e_tir_eq, e_allen_eq = delta_energy_map[min_delta]
        if e_tir_eq >= e_allen_eq:
            return 0.0
        sorted_deltas = sorted(delta_energy_map.keys())
        idx = sorted_deltas.index(min_delta)
        local_min = True
        if idx > 0:
            prev_delta = sorted_deltas[idx-1]
            if delta_energy_map[prev_delta][0] < e_tir_eq:
                local_min = False
        if idx < len(sorted_deltas)-1:
            next_delta = sorted_deltas[idx+1]
            if delta_energy_map[next_delta][0] < e_tir_eq:
                local_min = False
        if local_min:
            return 1.0
        else:
            return 0.0


_SCORERS = {
    'equilibrium_delta_value': score_0,
    'oxygen_displacement_consistency': score_1,
    'csv_recompute_delta_match': score_2,
    'csv_energy_ordering': score_3,
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
