import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import curve_fit


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
    import csv
    import os

    data_path = os.path.join(outputs_dir, 'eos_data.csv')
    ctx = {}
    ctx['eos_present'] = False
    if os.path.isfile(data_path):
        volumes = []
        energies = []
        with open(data_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                volumes.append(float(row['Volume']))
                energies.append(float(row['Energy']))
        ctx['eos_volumes'] = volumes
        ctx['eos_energies'] = energies
        ctx['eos_present'] = True
    return ctx


# === block: score_0 (check id='step_extract_lattice') ===
def score_0(artifact, step, ctx):
    row = artifact[0]
    a = float(row['a'])
    c = float(row['c'])
    a_gold = step.get('gold_a', 3.21)
    c_gold = step.get('gold_c', 11.29)
    a_tol = step.get('tol_a', 0.02)
    c_tol = step.get('tol_c', 0.1)
    score_a = 1.0 if abs(a - a_gold) <= a_tol else 0.0
    score_c = 1.0 if abs(c - c_gold) <= c_tol else 0.0
    return (score_a + score_c) / 2.0


# === block: score_1 (check id='step_fit_eos') ===
def score_1(artifact, step, ctx):
    if not ctx.get('eos_present'):
        return 0.0
    volumes = np.array(ctx['eos_volumes'])
    energies = np.array(ctx['eos_energies'])

    def bm_energy(V, V0, K0, K0p, E0):
        eta = (V0 / V) ** (2/3)
        return E0 + (9/16) * V0 * K0 * ((eta - 1)**3 * K0p + (eta - 1)**2 * (6 - 4*eta))

    p0 = [step.get('gold_V0', 100.74), step.get('gold_K0', 183.0), step.get('gold_K0p', 4.1), 0.0]
    try:
        popt, _ = curve_fit(bm_energy, volumes, energies, p0=p0, max_nfev=10000)
        fitted_V0, fitted_K0, fitted_K0p, _ = popt
    except Exception:
        return 0.0

    gold_V0 = step.get('gold_V0', 100.74)
    gold_K0 = step.get('gold_K0', 183.0)
    gold_K0p = step.get('gold_K0p', 4.1)
    tol_V0 = step.get('tol_V0', 2.0)
    tol_K0 = step.get('tol_K0', 10.0)
    tol_K0p = step.get('tol_K0p', 1.0)

    s1 = 1.0 if abs(fitted_V0 - gold_V0) <= tol_V0 else 0.0
    s2 = 1.0 if abs(fitted_K0 - gold_K0) <= tol_K0 else 0.0
    s3 = 1.0 if abs(fitted_K0p - gold_K0p) <= tol_K0p else 0.0
    return (s1 + s2 + s3) / 3.0


_SCORERS = {
    'step_extract_lattice': score_0,
    'step_fit_eos': score_1,
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
