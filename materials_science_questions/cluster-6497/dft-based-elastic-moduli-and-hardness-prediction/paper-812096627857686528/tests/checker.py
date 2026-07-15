import os
import json
import csv

# === author imports / helpers ===
import csv, os, math, json


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


# === block: score_0 (check id='file_shape') ===
def score_0(artifact, step, ctx):
    import csv, os
    path = os.path.join("/app/outputs", "atom_in_jellium_parameters.csv")
    if not os.path.isfile(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        columns = set(reader.fieldnames)
        required = {'element', 'E0_LDA', 'E0_GGA', 's0_LDA', 's0_GGA', 'eta_LDA', 'eta_GGA', 'E2_LDA', 'E2_GGA', 'B_LDA', 'B_GGA'}
        if not required.issubset(columns):
            return 0.0
        rows = list(reader)
        allowed_elements = {'H','Li','Be','B','C','N','O','F','Na','Mg','Al','Si','P','S','Cl','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn'}
        elements = {row['element'] for row in rows}
        if not allowed_elements.issubset(elements):
            return 0.0
        if len(rows) < len(allowed_elements):
            return 0.0
    return 1.0


# === block: score_1 (check id='table_accuracy') ===
def score_1(artifact, step, ctx):
    import csv, os
    path = os.path.join("/app/outputs", "atom_in_jellium_parameters.csv")
    if not os.path.isfile(path):
        return 0.0
    ref_data = {
        "H": {"E0_LDA":-2.16,"E0_GGA":-1.96,"s0_LDA":1.56,"s0_GGA":1.66,"eta_LDA":2.70,"eta_GGA":2.70,"E2_LDA":3.50,"E2_GGA":3.50,"B_LDA":172,"B_GGA":151},
        "Li": {"E0_LDA":-1.63,"E0_GGA":-1.53,"s0_LDA":3.25,"s0_GGA":3.32,"eta_LDA":2.80,"eta_GGA":2.80,"E2_LDA":0.80,"E2_GGA":0.80,"B_LDA":14,"B_GGA":13},
        "Be": {"E0_LDA":-3.32,"E0_GGA":-2.92,"s0_LDA":2.35,"s0_GGA":2.42,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":1.80,"E2_GGA":1.80,"B_LDA":130,"B_GGA":115},
        "B":  {"E0_LDA":-5.58,"E0_GGA":-5.10,"s0_LDA":2.00,"s0_GGA":2.06,"eta_LDA":3.20,"eta_GGA":3.20,"E2_LDA":3.00,"E2_GGA":3.00,"B_LDA":320,"B_GGA":280},
        "C":  {"E0_LDA":-7.37,"E0_GGA":-6.77,"s0_LDA":1.72,"s0_GGA":1.78,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":5.50,"E2_GGA":5.50,"B_LDA":440,"B_GGA":380},
        "N":  {"E0_LDA":-4.92,"E0_GGA":-4.42,"s0_LDA":1.76,"s0_GGA":1.82,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":4.00,"E2_GGA":4.00,"B_LDA":310,"B_GGA":270},
        "O":  {"E0_LDA":-4.14,"E0_GGA":-3.64,"s0_LDA":1.68,"s0_GGA":1.74,"eta_LDA":3.80,"eta_GGA":3.80,"E2_LDA":5.00,"E2_GGA":5.00,"B_LDA":400,"B_GGA":350},
        "F":  {"E0_LDA":-2.85,"E0_GGA":-2.45,"s0_LDA":1.52,"s0_GGA":1.58,"eta_LDA":4.50,"eta_GGA":4.50,"E2_LDA":6.00,"E2_GGA":6.00,"B_LDA":550,"B_GGA":480},
        "Na": {"E0_LDA":-1.13,"E0_GGA":-1.03,"s0_LDA":3.93,"s0_GGA":4.05,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":0.50,"E2_GGA":0.50,"B_LDA":7,"B_GGA":7},
        "Mg": {"E0_LDA":-1.55,"E0_GGA":-1.35,"s0_LDA":3.40,"s0_GGA":3.49,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":0.80,"E2_GGA":0.80,"B_LDA":35,"B_GGA":31},
        "Al": {"E0_LDA":-3.39,"E0_GGA":-3.09,"s0_LDA":3.00,"s0_GGA":3.08,"eta_LDA":3.10,"eta_GGA":3.10,"E2_LDA":1.50,"E2_GGA":1.50,"B_LDA":75,"B_GGA":65},
        "Si": {"E0_LDA":-4.63,"E0_GGA":-4.13,"s0_LDA":2.80,"s0_GGA":2.86,"eta_LDA":3.30,"eta_GGA":3.30,"E2_LDA":2.50,"E2_GGA":2.50,"B_LDA":100,"B_GGA":85},
        "P":  {"E0_LDA":-5.44,"E0_GGA":-4.94,"s0_LDA":2.60,"s0_GGA":2.66,"eta_LDA":3.40,"eta_GGA":3.40,"E2_LDA":3.50,"E2_GGA":3.50,"B_LDA":120,"B_GGA":105},
        "S":  {"E0_LDA":-4.92,"E0_GGA":-4.52,"s0_LDA":2.42,"s0_GGA":2.48,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":4.00,"E2_GGA":4.00,"B_LDA":150,"B_GGA":130},
        "Cl": {"E0_LDA":-3.64,"E0_GGA":-3.34,"s0_LDA":2.22,"s0_GGA":2.28,"eta_LDA":4.00,"eta_GGA":4.00,"E2_LDA":5.50,"E2_GGA":5.50,"B_LDA":200,"B_GGA":175},
        "K":  {"E0_LDA":-0.98,"E0_GGA":-0.88,"s0_LDA":4.62,"s0_GGA":4.75,"eta_LDA":2.80,"eta_GGA":2.80,"E2_LDA":0.30,"E2_GGA":0.30,"B_LDA":3,"B_GGA":3},
        "Ca": {"E0_LDA":-1.84,"E0_GGA":-1.64,"s0_LDA":3.90,"s0_GGA":4.00,"eta_LDA":2.90,"eta_GGA":2.90,"E2_LDA":0.60,"E2_GGA":0.60,"B_LDA":15,"B_GGA":13},
        "Sc": {"E0_LDA":-3.90,"E0_GGA":-3.50,"s0_LDA":3.20,"s0_GGA":3.28,"eta_LDA":3.00,"eta_GGA":3.00,"E2_LDA":1.20,"E2_GGA":1.20,"B_LDA":55,"B_GGA":48},
        "Ti": {"E0_LDA":-4.85,"E0_GGA":-4.45,"s0_LDA":3.00,"s0_GGA":3.08,"eta_LDA":3.20,"eta_GGA":3.20,"E2_LDA":1.80,"E2_GGA":1.80,"B_LDA":100,"B_GGA":85},
        "V":  {"E0_LDA":-5.31,"E0_GGA":-4.91,"s0_LDA":2.90,"s0_GGA":2.97,"eta_LDA":3.30,"eta_GGA":3.30,"E2_LDA":2.20,"E2_GGA":2.20,"B_LDA":160,"B_GGA":140},
        "Cr": {"E0_LDA":-4.10,"E0_GGA":-3.70,"s0_LDA":2.80,"s0_GGA":2.87,"eta_LDA":3.40,"eta_GGA":3.40,"E2_LDA":2.60,"E2_GGA":2.60,"B_LDA":190,"B_GGA":165},
        "Mn": {"E0_LDA":-2.95,"E0_GGA":-2.65,"s0_LDA":2.70,"s0_GGA":2.77,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":2.80,"E2_GGA":2.80,"B_LDA":210,"B_GGA":185},
        "Fe": {"E0_LDA":-4.28,"E0_GGA":-3.88,"s0_LDA":2.60,"s0_GGA":2.66,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":3.00,"E2_GGA":3.00,"B_LDA":230,"B_GGA":200},
        "Co": {"E0_LDA":-4.39,"E0_GGA":-3.99,"s0_LDA":2.55,"s0_GGA":2.60,"eta_LDA":3.65,"eta_GGA":3.65,"E2_LDA":3.10,"E2_GGA":3.10,"B_LDA":240,"B_GGA":210},
        "Ni": {"E0_LDA":-4.44,"E0_GGA":-4.04,"s0_LDA":2.50,"s0_GGA":2.55,"eta_LDA":3.70,"eta_GGA":3.70,"E2_LDA":3.20,"E2_GGA":3.20,"B_LDA":250,"B_GGA":220},
        "Cu": {"E0_LDA":-3.49,"E0_GGA":-3.19,"s0_LDA":2.67,"s0_GGA":2.73,"eta_LDA":3.60,"eta_GGA":3.60,"E2_LDA":2.50,"E2_GGA":2.50,"B_LDA":180,"B_GGA":155},
        "Zn": {"E0_LDA":-1.35,"E0_GGA":-1.25,"s0_LDA":2.90,"s0_GGA":2.98,"eta_LDA":3.50,"eta_GGA":3.50,"E2_LDA":1.50,"E2_GGA":1.50,"B_LDA":70,"B_GGA":60}
    }
    tolerances = {
        "E0_LDA": 0.2,
        "E0_GGA": 0.2,
        "s0_LDA": 0.1,
        "s0_GGA": 0.1,
        "eta_LDA": 0.1,
        "eta_GGA": 0.1,
        "E2_LDA": 0.3,
        "E2_GGA": 0.3,
        "B_LDA": 10.0,
        "B_GGA": 10.0
    }
    with open(path, newline='') as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 30:
        return 0.0
    total = 0
    count = 0
    numeric_cols = ["E0_LDA","E0_GGA","s0_LDA","s0_GGA","eta_LDA","eta_GGA","E2_LDA","E2_GGA","B_LDA","B_GGA"]
    for row in rows:
        elem = row.get("element","").strip()
        if elem not in ref_data:
            continue
        ref = ref_data[elem]
        for col in numeric_cols:
            try:
                val = float(row[col])
            except (ValueError, TypeError, KeyError):
                continue
            expected = ref[col]
            tol = tolerances.get(col, 0.2)
            if abs(val - expected) <= tol:
                total += 1
            count += 1
    if count == 0:
        return 0.0
    return total / count


# === block: score_2 (check id='trend_check') ===
def score_2(artifact, step, ctx):
    import csv, os
    path = os.path.join("/app/outputs", "atom_in_jellium_parameters.csv")
    if not os.path.isfile(path):
        return 0.0
    with open(path, newline='') as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 30:
        return 0.0
    ok = 0
    for row in rows:
        try:
            e0_l = float(row["E0_LDA"])
            e0_g = float(row["E0_GGA"])
            s0_l = float(row["s0_LDA"])
            s0_g = float(row["s0_GGA"])
            b_l = float(row["B_LDA"])
            b_g = float(row["B_GGA"])
        except (ValueError, TypeError, KeyError):
            continue
        if e0_g > e0_l and s0_g > s0_l and b_g < b_l:
            ok += 1
    return ok / 30.0


# === block: score_3 (check id='internal_consistency') ===
def score_3(artifact, step, ctx):
    import csv, os, math
    path = os.path.join("/app/outputs", "atom_in_jellium_parameters.csv")
    if not os.path.isfile(path):
        return 0.0
    with open(path, newline='') as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 27:
        return 0.0
    ratios = []
    for pair in [('LDA', 'LDA'), ('GGA', 'GGA')]:
        suf = pair[0]
        for row in rows:
            try:
                E2 = float(row["E2_" + suf])
                eta = float(row["eta_" + suf])
                s0 = float(row["s0_" + suf])
                B = float(row["B_" + suf])
            except (ValueError, TypeError, KeyError):
                continue
            if s0 == 0:
                continue
            v = E2 * eta**2 / (6 * math.pi * s0)
            if v != 0:
                ratios.append(B / v)
    if len(ratios) < 2:
        return 0.0
    median = sorted(ratios)[len(ratios)//2]
    devs = [abs(r - median) / abs(median) for r in ratios]
    mean_dev = sum(devs) / len(devs)
    if mean_dev <= 0.15:
        return 1.0
    elif mean_dev <= 0.3:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'file_shape': score_0,
    'table_accuracy': score_1,
    'trend_check': score_2,
    'internal_consistency': score_3,
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
