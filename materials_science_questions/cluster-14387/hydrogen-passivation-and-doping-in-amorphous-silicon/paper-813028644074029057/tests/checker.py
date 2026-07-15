import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import builtins

    class _NPFallback:
        def array(self, seq):
            return list(seq)

        def max(self, arr):
            return builtins.max(arr)

    np = _NPFallback()


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


# === block: score_0 (check id='check_formation') ===
def score_0(artifact, step, ctx):
    target = step['target']
    tol = step['tolerance']
    ok_sil = abs(artifact.get('silanol', 1e9) - target['silanol']) <= tol['silanol']
    ok_sioh = abs(artifact.get('Si-OOH+Si-H', 1e9) - target['Si-OOH+Si-H']) <= tol['Si-OOH+Si-H']
    return (0.5 * float(ok_sil) + 0.5 * float(ok_sioh))


# === block: score_1 (check id='check_barriers') ===
def score_1(artifact, step, ctx):
    target = step['target']
    tol = step['tolerance']
    ok_oo = abs(artifact.get('O-O_cleavage', 1e9) - target['O-O_cleavage']) <= tol['O-O_cleavage']
    ok_si = abs(artifact.get('Si-O_cleavage', 1e9) - target['Si-O_cleavage']) <= tol['Si-O_cleavage']
    return (0.5 * float(ok_oo) + 0.5 * float(ok_si))


# === block: score_2 (check id='check_absorption_peaks') ===
def score_2(artifact, step, ctx):
    target = step['target']
    tol = step['tolerance']
    cols = step['columns']
    energy_col = cols['energy']
    pol_col = cols['POL']
    sil_col = cols['silanol']
    sioh_col = cols['SiOOH_SiH']
    energies = np.array([float(row[energy_col]) for row in artifact])
    pol = np.array([float(row[pol_col]) for row in artifact])
    sil = np.array([float(row[sil_col]) for row in artifact])
    sioh = np.array([float(row[sioh_col]) for row in artifact])
    def find_peaks(x, y, rel_h=0.05):
        peaks = []
        n = len(y)
        if n < 3:
            return peaks
        ymax = np.max(y)
        if ymax == 0:
            return peaks
        for i in range(1, n-1):
            if y[i] > y[i-1] and y[i] > y[i+1] and y[i] > rel_h * ymax:
                peaks.append(x[i])
        return peaks
    def count_matches(detected, expected, tol):
        matched = 0
        for exp in expected:
            for d in detected:
                if abs(d - exp) <= tol:
                    matched += 1
                    break
        return matched
    pol_peaks = find_peaks(energies, pol)
    sil_peaks = find_peaks(energies, sil)
    sioh_peaks = find_peaks(energies, sioh)
    total_exp = len(target['POL']) + len(target['silanol']) + len(target['SiOOH_SiH'])
    total_mat = (count_matches(pol_peaks, target['POL'], tol) +
                 count_matches(sil_peaks, target['silanol'], tol) +
                 count_matches(sioh_peaks, target['SiOOH_SiH'], tol))
    return total_mat / total_exp if total_exp > 0 else 0.0


_SCORERS = {
    'check_formation': score_0,
    'check_barriers': score_1,
    'check_absorption_peaks': score_2,
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
