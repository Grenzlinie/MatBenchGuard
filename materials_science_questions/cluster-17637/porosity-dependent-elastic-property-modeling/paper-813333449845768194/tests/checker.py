import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math
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
    layers = {
        33: (46.0, 16.0, 17.0),
        44: (36.0, 14.0, 14.0),
        48: (25.0, 13.0, 12.0),
        52: (17.0, 12.0, 10.0),
        54: (13.0,  9.0,  8.0),
        59: (13.0,  9.0,  8.0),
        70: (6.7,   5.0,  4.8),
        72: (5.5,   3.4,  3.5),
    }
    c11_1, c12_1, c44_1 = layers[59]
    d1 = 10.0
    samples = [
        ("59-33%", 33, 15.6),
        ("59-44%", 44, 20.0),
        ("59-48%", 48, 10.0),
        ("59-52%", 52, 10.0),
        ("59-54%", 54, 10.0),
        ("59-70%", 70, 10.0),
        ("59-72%", 72, 10.0),
    ]
    por = [33, 44, 48, 52, 54, 59, 70, 72]
    xi = [p/100.0 for p in por]
    c11_vals = [46, 36, 25, 17, 13, 13, 6.7, 5.5]
    c44_vals = [17, 14, 12, 10, 8, 8, 4.8, 3.5]
    return {
        'layers': layers,
        'samples': samples,
        'c11_1': c11_1, 'c12_1': c12_1, 'c44_1': c44_1, 'd1': d1,
        'xi': xi, 'c11_vals': c11_vals, 'c44_vals': c44_vals,
    }


# === block: score_0 (check id='step_compute_sl_elastic_constants') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerance_rel', 1e-5)
    layers = ctx['layers']
    d1 = ctx['d1']
    samples_list = ctx['samples']
    c11_1, c12_1, c44_1 = layers[59]
    expected = {}
    for name, por2, d2 in samples_list:
        c11_2, c12_2, c44_2 = layers[por2]
        d = d1 + d2
        f1 = d1 / d
        f2 = d2 / d
        denom = (c11_2 * f1 / c11_1) + f2
        c13 = ((c12_1 * c11_2 * f1 / c11_1) + c12_2 * f2) / denom
        c33 = (c11_2 * f1 + c11_2 * f2) / denom
        c44 = (c44_2 * f1 + c44_2 * f2) / ((c44_2 * f1 / c44_1) + f2)
        term1 = (f1 * (c12_1 + c11_1 * (c12_2 - c12_1) / c11_1 + c11_2 * f2)) / (f1 + f2)
        term2 = (f1 * (c12_2 - c12_1) / c11_1 * (c11_2 * f1 + c11_2 * f2)) / ((f1 + f2) * ((c11_2 * f1 / c11_1) + f2))
        c11 = term1 - term2
        expected[name] = (c11, c13, c33, c44)
    agent = {}
    for row in artifact:
        try:
            name = row['sample']
            c11_a = float(row['c11'])
            c13_a = float(row['c13'])
            c33_a = float(row['c33'])
            c44_a = float(row['c44'])
            agent[name] = (c11_a, c13_a, c33_a, c44_a)
        except (ValueError, KeyError):
            pass
    total = len(expected)
    if total == 0:
        return 0.0
    good = 0
    for name, (c11e, c13e, c33e, c44e) in expected.items():
        if name not in agent:
            continue
        c11a, c13a, c33a, c44a = agent[name]
        if (abs(c11a - c11e) <= tol * max(abs(c11e), 1e-9) and
            abs(c13a - c13e) <= tol * max(abs(c13e), 1e-9) and
            abs(c33a - c33e) <= tol * max(abs(c33e), 1e-9) and
            abs(c44a - c44e) <= tol * max(abs(c44e), 1e-9)):
            good += 1
    return good / total


# === block: score_1 (check id='step_fit_porosity_exponents') ===
def score_1(artifact, step, ctx):
    tol = step.get('tolerance_gamma_abs', 0.01)
    xi = ctx['xi']
    c11_vals = ctx['c11_vals']
    c44_vals = ctx['c44_vals']
    c11_cSi, c44_cSi = 166.0, 79.0
    def model(xi, gamma, cSi):
        return cSi * (1 - xi) ** gamma
    popt11, _ = curve_fit(lambda x, g: model(x, g, c11_cSi), xi, c11_vals, p0=[2.0], bounds=(0, None))
    gamma_11_ref = float(popt11[0])
    popt44, _ = curve_fit(lambda x, g: model(x, g, c44_cSi), xi, c44_vals, p0=[2.0], bounds=(0, None))
    gamma_44_ref = float(popt44[0])
    gamma_11_agent = artifact.get('gamma_11')
    gamma_44_agent = artifact.get('gamma_44')
    if gamma_11_agent is None or gamma_44_agent is None:
        return 0.0
    score = 0.0
    if abs(gamma_11_agent - gamma_11_ref) <= tol:
        score += 0.5
    if abs(gamma_44_agent - gamma_44_ref) <= tol:
        score += 0.5
    return score


_SCORERS = {
    'step_compute_sl_elastic_constants': score_0,
    'step_fit_porosity_exponents': score_1,
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
