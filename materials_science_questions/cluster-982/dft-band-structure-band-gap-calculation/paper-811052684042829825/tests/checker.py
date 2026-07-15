import os
import json
import csv

# === author imports / helpers ===
import re


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


# === block: score_0 (check id='check_bandgaps_trend') ===
def score_0(artifact, step, ctx):
    import re
    content = artifact
    pbe = None
    hse = None
    for line in content.splitlines():
        if line.startswith('PBE_bandgap_eV'):
            m = re.search(r'=\s*([\d.]+)', line)
            if m: pbe = float(m.group(1))
        elif line.startswith('HSE06_bandgap_eV'):
            m = re.search(r'=\s*([\d.]+)', line)
            if m: hse = float(m.group(1))
    if pbe is None or hse is None:
        return 0.0
    score = 0.0
    if pbe < hse:
        score += 0.2
    if pbe > 1.0:
        score += 0.2
    if pbe < 2.2:
        score += 0.2
    if hse > 2.0:
        score += 0.2
    if hse - pbe >= 0.4:
        score += 0.2
    return score


# === block: score_1 (check id='check_formation_energies_trend') ===
def score_1(artifact, step, ctx):
    rows = {r['defect_type'].strip(): float(r['formation_energy_eV']) for r in artifact}
    required = ['V_Li-', 'V_S2_2+', 'p-', 'p+']
    for k in required:
        if k not in rows:
            return 0.0
    vli = rows['V_Li-']
    vs2 = rows['V_S2_2+']
    pmin = rows['p-']
    pp = rows['p+']
    score = 0.0
    if vli <= 1.5:
        score += 0.25
    if pp <= 1.5:
        score += 0.25
    if vs2 > vli and vs2 > pp:
        score += 0.25
    if pmin > vli and pmin > pp:
        score += 0.25
    return score


# === block: score_2 (check id='check_diffusion_barriers_trend') ===
def score_2(artifact, step, ctx):
    barriers = {}
    for row in artifact:
        defect = row['defect_type'].strip()
        orient = row['orientation'].strip()
        val = float(row['barrier_eV'])
        if orient not in barriers:
            barriers[orient] = {}
        barriers[orient][defect] = val
    cond1 = True  # all p+ <= 0.1
    cond2 = True  # all V_Li- <= 1.0
    cond3 = True  # all V_S2_2+ >= 0.4
    cond4 = True  # p+ is the smallest in each orientation
    for orient, defs in barriers.items():
        if 'p+' in defs:
            if defs['p+'] > 0.1:
                cond1 = False
        else:
            cond1 = False
        if 'V_Li-' in defs:
            if defs['V_Li-'] > 1.0:
                cond2 = False
        else:
            cond2 = False
        if 'V_S2_2+' in defs:
            if defs['V_S2_2+'] < 0.4:
                cond3 = False
        else:
            cond3 = False
        vals = list(defs.values())
        min_val = min(vals)
        if 'p+' in defs and defs['p+'] != min_val:
            cond4 = False
    score = 0.0
    if cond1:
        score += 0.25
    if cond2:
        score += 0.25
    if cond3:
        score += 0.25
    if cond4:
        score += 0.25
    return score


# === block: score_3 (check id='check_conductivity_summary_trend') ===
def score_3(artifact, step, ctx):
    rows = {r['charge_carrier'].strip(): r for r in artifact}
    if 'p+' not in rows or 'V_Li-' not in rows:
        return 0.0
    mob_p = float(rows['p+']['mobility_cm2_Vs'])
    mob_v = float(rows['V_Li-']['mobility_cm2_Vs'])
    cond_p = float(rows['p+']['conductivity_S_cm'])
    cond_v = float(rows['V_Li-']['conductivity_S_cm'])
    ratio_mob = mob_p / mob_v if mob_v != 0 else float('inf')
    ratio_cond = cond_p / cond_v if cond_v != 0 else float('inf')
    score = 0.0
    if ratio_mob >= 1e8:
        score += 0.5
    if ratio_cond >= 1e8:
        score += 0.5
    return score


_SCORERS = {
    'check_bandgaps_trend': score_0,
    'check_formation_energies_trend': score_1,
    'check_diffusion_barriers_trend': score_2,
    'check_conductivity_summary_trend': score_3,
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
