import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    expected_map = {}
    for step in spec.get('steps', []):
        if step['output_file'] == 'absorption_energies.csv':
            expected_map = step.get('expected', {})
            tol = step.get('tolerance_abs', 0.2)
            return {'expected': expected_map, 'tolerance': tol}
    return {'expected': {}, 'tolerance': 0.2}


# === block: score_0 (check id='absorption_energies_csv_check') ===
def score_0(artifact, step, ctx):
    # Recompute expected values from the provided crystal parameters
    crystals = {
        "MgO": {"struct": "rocksalt", "r0": 2.1015, "A": 1.7476, "alpha_M": 0.10, "alpha_X": 2.25, "I2": 14.96, "E2": -8.5, "dU1": 0.0, "dU2": 0.0, "chi": 0.5},
        "CaO": {"struct": "rocksalt", "r0": 2.4053, "A": 1.7476, "alpha_M": 0.54, "alpha_X": 2.25, "I2": 11.82, "E2": -8.5, "dU1": 0.0, "dU2": 0.0, "chi": 0.5},
        "SrO": {"struct": "rocksalt", "r0": 2.58, "A": 1.7476, "alpha_M": 1.0, "alpha_X": 2.25, "I2": 10.98, "E2": -8.5, "dU1": 0.0, "dU2": 0.0, "chi": 0.5},
        "BaO": {"struct": "rocksalt", "r0": 2.75, "A": 1.7476, "alpha_M": 2.08, "alpha_X": 2.25, "I2": 9.96, "E2": -8.5, "dU1": 0.0, "dU2": 0.0, "chi": 0.5},
        "CdO": {"struct": "rocksalt", "r0": 2.3415, "A": 1.7476, "alpha_M": 0.54, "alpha_X": 2.25, "I2": 16.84, "E2": -8.5, "dU1": 1.55, "dU2": 1.09, "chi": 3.5},
        "CaS": {"struct": "rocksalt", "r0": 2.84, "A": 1.7476, "alpha_M": 0.54, "alpha_X": 6.00, "I2": 11.82, "E2": -8.0, "dU1": 0.0, "dU2": 0.0, "chi": 1.2},
        "SrS": {"struct": "rocksalt", "r0": 2.935, "A": 1.7476, "alpha_M": 1.0, "alpha_X": 6.00, "I2": 10.98, "E2": -8.0, "dU1": 0.0, "dU2": 0.0, "chi": 1.2},
        "BaS": {"struct": "rocksalt", "r0": 3.175, "A": 1.7476, "alpha_M": 2.08, "alpha_X": 6.00, "I2": 9.96, "E2": -8.0, "dU1": 0.0, "dU2": 0.0, "chi": 1.2},
        "ZnS": {"struct": "zincblende", "r0": 2.3513, "A": 1.6381, "alpha_M": 0.17, "alpha_X": 6.00, "I2": 17.89, "E2": -8.0, "dU1": 1.11, "dU2": 0.81, "chi": 1.5},
        "CdS": {"struct": "wurtzite", "r0": 2.5352, "A": 1.63, "alpha_M": 0.54, "alpha_X": 6.00, "I2": 16.84, "E2": -8.0, "dU1": 1.07, "dU2": 0.77, "chi": 0.5},
    }

    e2 = 14.3996
    tol = ctx.get('tolerance', 0.2)
    n = len(crystals)
    if n == 0:
        return 0.0

    correct = 0
    for row in artifact:
        name = row.get('crystal', '').strip()
        if name not in crystals:
            continue
        p = crystals[name]
        r0 = p["r0"]
        A = p["A"]
        alpha_sum = p["alpha_M"] + p["alpha_X"]
        VM = 2 * A * e2 / r0
        electro = 2 * (2*A - 1) * e2 / r0
        if p["struct"] == "rocksalt":
            omega1 = -2.027 * e2 * alpha_sum / (r0**4)
            omega2 = -7.00  * e2 * alpha_sum / (2 * r0**4)
        else:
            omega1 = 0.0
            omega2 = -3.50  * e2 * alpha_sum / (2 * r0**4)
        Omega1 = -0.4189 * e2 / r0
        exp_hv1 = electro + p["E2"] - p["I2"] + omega1 + Omega1 + p["dU1"]
        exp_hv2 = VM      + p["E2"] - p["chi"] + omega2 + p["dU2"]
        try:
            hv1 = float(row["hν1_eV"])
            hv2 = float(row["hν2_eV"])
        except (ValueError, KeyError):
            continue
        if abs(hv1 - exp_hv1) <= tol and abs(hv2 - exp_hv2) <= tol:
            correct += 1

    return correct / n


_SCORERS = {
    'absorption_energies_csv_check': score_0,
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
