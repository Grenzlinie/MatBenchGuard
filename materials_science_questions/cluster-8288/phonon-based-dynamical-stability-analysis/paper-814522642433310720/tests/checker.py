import os
import json
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
    return {}


# === block: score_0 (check id='formation_energy') ===
def score_0(artifact, step, ctx):
    gold_vals = step.get('gold_values', {})
    tol = step.get('tolerance', 0.3)
    trend_w = step.get('trend_weight', 0.3)
    required_x = [0.25, 0.5, 0.6]
    rows = {}
    for row in artifact:
        try:
            x = float(row.get('x', ''))
        except:
            continue
        rows[x] = row
    for x in required_x:
        if x not in rows:
            return 0.0
    fields = ['Delta_E_I', 'Delta_E_K_ion_layers', 'Delta_E_e_doping', 'Delta_E_FeSe_deformation', 'Delta_E_C']
    value_scores = []
    e_doping_vals = []
    coulomb_vals = []
    for x in required_x:
        row = rows[x]
        x_str = str(x)
        gold_row = gold_vals.get(x_str, {})
        for field in fields:
            try:
                val = float(row.get(field, 0.0))
            except:
                val = 0.0
            gold_val = float(gold_row.get(field, 0.0))
            diff = abs(val - gold_val)
            if diff <= tol:
                score = 1.0
            elif diff <= 2 * tol:
                score = 0.5
            else:
                score = 0.0
            value_scores.append(score)
        e_doping_vals.append(float(row.get('Delta_E_e_doping', 0.0)))
        coulomb_vals.append(float(row.get('Delta_E_C', 0.0)))
    value_score = sum(value_scores) / len(value_scores) if value_scores else 0.0
    trend_e = 1.0 if (e_doping_vals[0] < e_doping_vals[1] < e_doping_vals[2]) else 0.0
    trend_c = 1.0 if (coulomb_vals[0] > coulomb_vals[1] > coulomb_vals[2]) else 0.0
    sign_e = 1.0 if all(v > 0 for v in e_doping_vals) else 0.0
    sign_c = 1.0 if all(v < 0 for v in coulomb_vals) else 0.0
    trend_score = 0.25 * trend_e + 0.25 * trend_c + 0.25 * sign_e + 0.25 * sign_c
    total = value_score * (1 - trend_w) + trend_score * trend_w
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='lattice_constants') ===
def score_1(artifact, step, ctx):
    gold_data = step.get('gold', {})
    tols = step.get('tolerances', {})
    a_tol = tols.get('a_Angstrom', 0.05)
    c_tol = tols.get('c_Angstrom', 0.1)
    rows = {}
    for row in artifact:
        try:
            x = float(row.get('x', ''))
        except:
            continue
        rows[x] = row
    required_x = [0.25, 0.5]
    for x in required_x:
        if x not in rows:
            return 0.0
    scores = []
    for x in required_x:
        row = rows[x]
        gold_row = gold_data.get(str(x))
        if gold_row is None:
            return 0.0
        a_val = float(row.get('a_Angstrom', 0.0))
        c_val = float(row.get('c_Angstrom', 0.0))
        a_diff = abs(a_val - float(gold_row.get('a_Angstrom', 0.0)))
        c_diff = abs(c_val - float(gold_row.get('c_Angstrom', 0.0)))
        sub_a = 1.0 if a_diff <= a_tol else 0.0
        sub_c = 1.0 if c_diff <= c_tol else 0.0
        scores.append((sub_a + sub_c) / 2.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='phonon_x020') ===
def score_2(artifact, step, ctx):
    freqs = artifact.get('frequencies_cm-1', [])
    dos = artifact.get('dos', [])
    if not freqs or not dos or len(freqs) != len(dos):
        return 0.0
    if min(freqs) < -10.0:
        return 1.0
    return 0.0


# === block: score_3 (check id='phonon_x025') ===
def score_3(artifact, step, ctx):
    freqs = artifact.get('frequencies_cm-1', [])
    dos = artifact.get('dos', [])
    if not freqs or not dos or len(freqs) != len(dos):
        return 0.0
    if all(f >= 0 for f in freqs):
        return 1.0
    return 0.0


# === block: score_4 (check id='fe_vacancy') ===
def score_4(artifact, step, ctx):
    gold_val = -1.5
    tol = step.get('tolerance', 0.5)
    value = None
    for row in artifact:
        try:
            x = float(row.get('x', ''))
        except:
            continue
        if abs(x - 0.8) < 0.001:
            value = float(row.get('Delta_E_Fe_vacancy', 0.0))
            break
    if value is None:
        return 0.0
    if value < 0 and abs(value - gold_val) <= tol:
        return 1.0
    return 0.0


_SCORERS = {
    'formation_energy': score_0,
    'lattice_constants': score_1,
    'phonon_x020': score_2,
    'phonon_x025': score_3,
    'fe_vacancy': score_4,
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
