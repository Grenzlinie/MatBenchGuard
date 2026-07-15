import os
import json
import csv

# === author imports / helpers ===
import os, csv


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
    csv_path = os.path.join(outputs_dir, 'swzont_computed_properties.csv')
    rows = []
    if os.path.isfile(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    for r in rows:
        for col in ['n', 'diameter', 'binding_energy_eV_per_ZnO', 'youngs_modulus_GPa', 'avg_bond_length_ang', 'charge_transfer_e']:
            try:
                r[col] = float(r[col])
            except:
                r[col] = None
        if r.get('n') is not None:
            try:
                r['n'] = int(r['n'])
            except:
                pass
    groups = {}
    for r in rows:
        chirality = r.get('chirality', '').strip().lower()
        n = r.get('n')
        if chirality not in groups:
            groups[chirality] = {}
        if n is not None:
            groups[chirality][n] = r
    sheet_row = groups.get('sheet', {}).get(0, None)
    return {'rows': rows, 'groups': groups, 'sheet_row': sheet_row}


# === block: score_0 (check id='shape_and_required_data') ===
def score_0(artifact, step, ctx):
    groups = ctx.get('groups', {})
    required = {('armchair', n) for n in range(3,11)} | {('zigzag', n) for n in range(3,11)} | {('sheet', 0)}
    present = 0
    for chirality, ndict in groups.items():
        for n, row in ndict.items():
            if (chirality, n) in required:
                present += 1
    score = present / len(required) if required else 0.0
    return score


# === block: score_1 (check id='trend_be_monotonic') ===
def score_1(artifact, step, ctx):
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('binding_energy_eV_per_ZnO')
            if v is not None:
                vals.append(v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_2 (check id='trend_be_chirality') ===
def score_2(artifact, step, ctx):
    groups = ctx.get('groups', {})
    arm = groups.get('armchair', {})
    zig = groups.get('zigzag', {})
    score = 0.0
    count = 0
    for n in range(3, 11):
        a = arm.get(n, {}).get('binding_energy_eV_per_ZnO')
        z = zig.get(n, {}).get('binding_energy_eV_per_ZnO')
        if a is not None and z is not None:
            if a <= z:
                score += 1
            count += 1
    if count > 0:
        score /= count
    return score


# === block: score_3 (check id='trend_ym_monotonic') ===
def score_3(artifact, step, ctx):
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('youngs_modulus_GPa')
            if v is not None:
                vals.append(v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] >= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_4 (check id='trend_bl_monotonic') ===
def score_4(artifact, step, ctx):
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('avg_bond_length_ang')
            if v is not None:
                vals.append(v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_5 (check id='trend_ct_monotonic') ===
def score_5(artifact, step, ctx):
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('charge_transfer_e')
            if v is not None:
                vals.append(v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] >= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_6 (check id='approach_sheet_be') ===
def score_6(artifact, step, ctx):
    sheet_row = ctx.get('sheet_row')
    if sheet_row is None:
        return 0.0
    sheet_be = sheet_row.get('binding_energy_eV_per_ZnO')
    if sheet_be is None:
        return 0.0
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('binding_energy_eV_per_ZnO')
            if v is not None:
                vals.append(v - sheet_be)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_7 (check id='approach_sheet_ym') ===
def score_7(artifact, step, ctx):
    sheet_row = ctx.get('sheet_row')
    if sheet_row is None:
        return 0.0
    sheet_ym = sheet_row.get('youngs_modulus_GPa')
    if sheet_ym is None:
        return 0.0
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('youngs_modulus_GPa')
            if v is not None and sheet_ym is not None:
                vals.append(sheet_ym - v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_8 (check id='approach_sheet_bl') ===
def score_8(artifact, step, ctx):
    sheet_row = ctx.get('sheet_row')
    if sheet_row is None:
        return 0.0
    sheet_bl = sheet_row.get('avg_bond_length_ang')
    if sheet_bl is None:
        return 0.0
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('avg_bond_length_ang')
            if v is not None and sheet_bl is not None:
                vals.append(v - sheet_bl)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


# === block: score_9 (check id='approach_sheet_ct') ===
def score_9(artifact, step, ctx):
    sheet_row = ctx.get('sheet_row')
    if sheet_row is None:
        return 0.0
    sheet_ct = sheet_row.get('charge_transfer_e')
    if sheet_ct is None:
        return 0.0
    groups = ctx.get('groups', {})
    score = 0.0
    count = 0
    for chirality in ['armchair', 'zigzag']:
        if chirality not in groups:
            continue
        ndict = groups[chirality]
        ns = sorted([n for n in ndict.keys() if isinstance(n, int) and 3 <= n <= 10])
        vals = []
        for n in ns:
            v = ndict[n].get('charge_transfer_e')
            if v is not None and sheet_ct is not None:
                vals.append(sheet_ct - v)
        if len(vals) < 2:
            continue
        pairs = len(vals) - 1
        correct = sum(1 for i in range(pairs) if vals[i+1] <= vals[i])
        score += correct / pairs
        count += 1
    if count > 0:
        score /= count
    return score


_SCORERS = {
    'shape_and_required_data': score_0,
    'trend_be_monotonic': score_1,
    'trend_be_chirality': score_2,
    'trend_ym_monotonic': score_3,
    'trend_bl_monotonic': score_4,
    'trend_ct_monotonic': score_5,
    'approach_sheet_be': score_6,
    'approach_sheet_ym': score_7,
    'approach_sheet_bl': score_8,
    'approach_sheet_ct': score_9,
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
