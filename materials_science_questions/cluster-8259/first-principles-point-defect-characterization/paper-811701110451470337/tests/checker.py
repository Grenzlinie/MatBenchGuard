import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    return {}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    required_cols = {'defect','configuration','charge','Fermi_level','formation_energy'}
    if not required_cols.issubset(rows[0].keys()):
        return 0.0
    # Build set of required keys
    # O_Sb: 4 configs, charges -1,0,+1, Fermi 0.0,0.25
    configs_Osb = ['alpha-CCB-DX','beta-CCB-DX','OBB-DX','C3V']
    charges_Osb = [-1,0,1]
    configs_Oi = ['C3V','bb','(O-Sb)sp']
    charges_Oi = [-2,0]
    fermi_levels = [0.0, 0.25]
    needed = set()
    for conf in configs_Osb:
        for q in charges_Osb:
            for ef in fermi_levels:
                needed.add(('O_Sb', conf, q, ef))
    for conf in configs_Oi:
        for q in charges_Oi:
            for ef in fermi_levels:
                needed.add(('O_i', conf, q, ef))
    actual = set()
    for r in rows:
        try:
            actual.add((r['defect'], r['configuration'], int(r['charge']), float(r['Fermi_level'])))
        except (KeyError, ValueError):
            continue
    return 1.0 if needed.issubset(actual) else 0.0


# === block: score_1 (check id='ordering_EF0') ===
def score_1(artifact, step, ctx):
    rows = artifact
    defect_charges = {'O_Sb': (-1,1), 'O_i': (-2,0)}
    eps = 1e-9
    for defect, (neg_q, pos_q) in defect_charges.items():
        neg_vals = []
        pos_vals = []
        for r in rows:
            if r['defect'] != defect:
                continue
            try:
                ef = float(r['Fermi_level'])
                q = int(r['charge'])
                e = float(r['formation_energy'])
            except (KeyError, ValueError):
                return 0.0
            if abs(ef) < eps:
                if q == neg_q:
                    neg_vals.append(e)
                elif q == pos_q:
                    pos_vals.append(e)
        if not neg_vals or not pos_vals:
            return 0.0
        if min(neg_vals) >= min(pos_vals) - eps:
            return 0.0
    return 1.0


# === block: score_2 (check id='ordering_EF025') ===
def score_2(artifact, step, ctx):
    rows = artifact
    defect_charges = {'O_Sb': (-1,1), 'O_i': (-2,0)}
    eps = 1e-9
    for defect, (neg_q, pos_q) in defect_charges.items():
        neg_vals = []
        pos_vals = []
        for r in rows:
            if r['defect'] != defect:
                continue
            try:
                ef = float(r['Fermi_level'])
                q = int(r['charge'])
                e = float(r['formation_energy'])
            except (KeyError, ValueError):
                return 0.0
            if abs(ef - 0.25) < eps:
                if q == neg_q:
                    neg_vals.append(e)
                elif q == pos_q:
                    pos_vals.append(e)
        if not neg_vals or not pos_vals:
            return 0.0
        if min(pos_vals) >= min(neg_vals) - eps:
            return 0.0
    return 1.0


# === block: score_3 (check id='transition_level') ===
def score_3(artifact, step, ctx):
    def get_e(row, defect, conf, q, ef):
        if row['defect'] != defect:
            return None
        if row['configuration'] != conf:
            return None
        try:
            if int(row['charge']) != q:
                return None
            if abs(float(row['Fermi_level']) - ef) > 1e-6:
                return None
            return float(row['formation_energy'])
        except (KeyError, ValueError):
            return None

    # O_Sb pair: beta-CCB-DX (-1) vs OBB-DX (+1)
    defect1, conf1, q1 = 'O_Sb', 'beta-CCB-DX', -1
    defect2, conf2, q2 = 'O_Sb', 'OBB-DX', 1
    val1_0 = val2_0 = val1_025 = val2_025 = None
    for r in artifact:
        v = get_e(r, defect1, conf1, q1, 0.0)
        if v is not None: val1_0 = v
        v = get_e(r, defect2, conf2, q2, 0.0)
        if v is not None: val2_0 = v
        v = get_e(r, defect1, conf1, q1, 0.25)
        if v is not None: val1_025 = v
        v = get_e(r, defect2, conf2, q2, 0.25)
        if v is not None: val2_025 = v
    if None in (val1_0, val2_0, val1_025, val2_025):
        return 0.0
    diff0 = val1_0 - val2_0
    diff25 = val1_025 - val2_025
    if diff0 == diff25:
        return 0.0
    cross_Osb = -diff0 / (diff25 - diff0) * 0.25

    # O_i pair: C3V (-2) vs C3V (0)
    defect3, conf3, q3 = 'O_i', 'C3V', -2
    defect4, conf4, q4 = 'O_i', 'C3V', 0
    val3_0 = val4_0 = val3_025 = val4_025 = None
    for r in artifact:
        v = get_e(r, defect3, conf3, q3, 0.0)
        if v is not None: val3_0 = v
        v = get_e(r, defect4, conf4, q4, 0.0)
        if v is not None: val4_0 = v
        v = get_e(r, defect3, conf3, q3, 0.25)
        if v is not None: val3_025 = v
        v = get_e(r, defect4, conf4, q4, 0.25)
        if v is not None: val4_025 = v
    if None in (val3_0, val4_0, val3_025, val4_025):
        return 0.0
    diff0_i = val3_0 - val4_0
    diff25_i = val3_025 - val4_025
    if diff0_i == diff25_i:
        return 0.0
    cross_Oi = -diff0_i / (diff25_i - diff0_i) * 0.25

    # Check both crossings in [0.1, 0.3]
    if 0.1 - 1e-9 <= cross_Osb <= 0.3 + 1e-9 and 0.1 - 1e-9 <= cross_Oi <= 0.3 + 1e-9:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'shape_check': score_0,
    'ordering_EF0': score_1,
    'ordering_EF025': score_2,
    'transition_level': score_3,
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
