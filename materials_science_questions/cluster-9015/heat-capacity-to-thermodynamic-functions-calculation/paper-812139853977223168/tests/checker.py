import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    atoms = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 4:
            try:
                x = float(parts[1]); y = float(parts[2]); z = float(parts[3])
            except: continue
            atoms.append((parts[0], (x,y,z)))
    hg_idx = None
    for i, (sym, pos) in enumerate(atoms):
        if sym == 'Hg':
            hg_idx = i; hg_pos = pos
            break
    if hg_idx is None: return 0.0
    min_C = float('inf'); min_S = float('inf')
    for sym, pos in atoms:
        d = math.sqrt(sum((a-b)**2 for a,b in zip(pos, hg_pos)))
        if sym == 'C' and d < min_C: min_C = d
        elif sym == 'S' and d < min_S: min_S = d
    gold = step.get('gold', {})
    tol = max(0.15, gold.get('tolerance_abs', 0.1))
    score = 0.0
    if abs(min_C - gold.get('Hg_C_distance', 2.049)) <= tol:
        score += 0.5
    if abs(min_S - gold.get('Hg_S_distance', 2.401)) <= tol:
        score += 0.5
    return min(score, 1.0)


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    order_hg_c = None; order_hg_s = None
    for row in artifact:
        bond = row.get('bond','').strip()
        order = row.get('order')
        if bond == 'Hg-C': order_hg_c = float(order)
        elif bond == 'Hg-S': order_hg_s = float(order)
    if order_hg_c is None or order_hg_s is None: return 0.0
    return 1.0 if order_hg_c > order_hg_s else 0.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    gold_rows = gold['rows']
    tol_Cp = gold['tolerances']['Cp']
    tol_S = gold['tolerances']['S']
    tol_H = gold['tolerances']['H']
    gold_by_T = {r['T']: r for r in gold_rows}
    score = 0.0
    for row in artifact:
        T = float(row['T'])
        if T not in gold_by_T: continue
        g = gold_by_T[T]
        cp_ok = abs(float(row['Cp']) - g['Cp']) <= tol_Cp
        s_ok = abs(float(row['S']) - g['S']) <= tol_S
        h_ok = abs(float(row['H']) - g['H']) <= tol_H
        if cp_ok and s_ok and h_ok:
            score += 1.0
    score = score / len(gold_rows)
    return min(score, 1.0)


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    gold_val = step['gold']['beta_mu']
    rel_tol = step['gold']['relative_tolerance']
    for row in artifact:
        if row.get('property','').strip() == 'beta_mu':
            try:
                val = float(row['value'])
            except: return 0.0
            err = abs(val - gold_val) / abs(gold_val)
            if err <= rel_tol:
                return 1.0
            elif err <= 1.0:
                return max(0.0, 1.0 - (err - rel_tol) / (1.0 - rel_tol))
            else:
                return 0.0
    return 0.0


# === block: score_4 (check id='step_06') ===
def score_4(artifact, step, ctx):
    gold_trans = step['gold']['transitions']
    wl_tol = step['gold']['wavelength_tol']
    osc_tol = step['gold']['oscillator_tol']
    rows = sorted(artifact, key=lambda r: float(r['wavelength_nm']))
    gold = sorted(gold_trans, key=lambda g: g['wavelength'])
    if len(rows) < len(gold): return 0.0
    score_each = 1.0 / (len(gold) * 2)
    total = 0.0
    matched = []
    for g in gold:
        best_idx = None
        best_diff = float('inf')
        for i, r in enumerate(rows):
            if i in matched: continue
            diff = abs(float(r['wavelength_nm']) - g['wavelength'])
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        if best_idx is not None:
            if best_diff <= wl_tol:
                total += score_each
            r = rows[best_idx]
            try:
                if abs(float(r['oscillator_strength']) - g['oscillator']) <= osc_tol:
                    total += score_each
            except: pass
            matched.append(best_idx)
    return min(total, 1.0)


_SCORERS = {
    'step_01': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
    'step_06': score_4,
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
