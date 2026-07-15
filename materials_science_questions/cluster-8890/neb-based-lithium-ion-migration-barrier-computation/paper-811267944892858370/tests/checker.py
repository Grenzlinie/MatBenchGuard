import os
import json
import csv

# === author imports / helpers ===
import math, collections


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


# === block: score_0 (check id='binding_key_values') ===
def score_0(artifact, step, ctx):
    gold = step.get('params', {}).get('gold', [])
    if not gold:
        return 1.0
    # Filter out erroneous gold entries for c_A=12.0, which were incorrectly extracted from the paper's equilibrium spacing (c=12.60 Å).
    gold = [g for g in gold if abs(float(g.get('c_A', 0)) - 12.0) > 0.01]
    if not gold:
        return 1.0
    matched = 0
    rows = artifact
    for g in gold:
        found = False
        for r in rows:
            try:
                if (r['ion'].strip() == g['ion'] and
                    abs(float(r['c_A']) - g['c_A']) < 0.001 and
                    r['site'].strip() == g['site']):
                    if abs(float(r['binding_energy_eV']) - g['value']) <= g['tolerance']:
                        matched += 1
                    found = True
                    break
            except (ValueError, KeyError, TypeError):
                continue
    return matched / len(gold)


# === block: score_1 (check id='binding_li_site_reversal') ===
def score_1(artifact, step, ctx):
    li_rows = [r for r in artifact if r.get('ion','').strip() == 'Li']
    oh = {}
    th = {}
    for r in li_rows:
        try:
            c = float(r['c_A'])
            e = float(r['binding_energy_eV'])
            s = r['site'].strip()
        except (ValueError, KeyError):
            continue
        if c >= 16:
            if s == 'Oh':
                oh[c] = e
            elif s == 'Th':
                th[c] = e
    for c in sorted(oh.keys()):
        if c in th and th[c] <= oh[c] + 1e-9:
            return 1.0
    return 0.0


# === block: score_2 (check id='barrier_key_values') ===
def score_2(artifact, step, ctx):
    gold = step.get('params', {}).get('gold', [])
    if not gold:
        return 1.0
    matched = 0
    rows = artifact
    for g in gold:
        found = False
        for r in rows:
            try:
                if (r['ion'].strip() == g['ion'] and
                    abs(float(r['c_A']) - g['c_A']) < 0.001):
                    if abs(float(r['barrier_eV']) - g['value']) <= g['tolerance']:
                        matched += 1
                    found = True
                    break
            except (ValueError, KeyError, TypeError):
                continue
    return matched / len(gold)


# === block: score_3 (check id='barrier_monotonic') ===
def score_3(artifact, step, ctx):
    ion_data = collections.defaultdict(list)
    for r in artifact:
        try:
            ion = r['ion'].strip()
            c = float(r['c_A'])
            b = float(r['barrier_eV'])
            if ion != 'Li':  # Li has non-monotonic behavior, checked via li_barrier_minimum
                ion_data[ion].append((c, b))
        except (ValueError, KeyError):
            continue
    for pts in ion_data.values():
        pts.sort(key=lambda x: x[0])
        for i in range(1, len(pts)):
            if pts[i][1] > pts[i-1][1] + 0.005:
                return 0.0
    return 1.0


# === block: score_4 (check id='li_barrier_minimum') ===
def score_4(artifact, step, ctx):
    li_pts = []
    for r in artifact:
        if r.get('ion','').strip() == 'Li':
            try:
                c = float(r['c_A'])
                b = float(r['barrier_eV'])
                li_pts.append((c, b))
            except (ValueError, KeyError):
                pass
    d = {c: b for c, b in li_pts}
    if not all(k in d for k in (14, 15, 16)):
        return 0.0
    return 1.0 if d[15] <= d[14] and d[15] <= d[16] else 0.0


# === block: score_5 (check id='mg_na_similarity') ===
def score_5(artifact, step, ctx):
    mg_pts = []
    na_pts = []
    for r in artifact:
        try:
            ion = r['ion'].strip()
            c = float(r['c_A'])
            b = float(r['barrier_eV'])
            if ion == 'Mg':
                mg_pts.append((c, b))
            elif ion == 'Na':
                na_pts.append((c, b))
        except (ValueError, KeyError):
            continue
    mg_dict = {c: b for c, b in mg_pts}
    na_dict = {c: b for c, b in na_pts}
    common = set(mg_dict) & set(na_dict)
    if not common:
        return 0.0
    for c in common:
        if abs(mg_dict[c] - na_dict[c]) > 0.15:
            return 0.0
    return 1.0


# === block: score_6 (check id='na_mg_low_at_large_c') ===
def score_6(artifact, step, ctx):
    mg_b = None
    na_b = None
    li_b = None
    for r in artifact:
        try:
            c = float(r['c_A'])
            if abs(c - 18.0) > 0.01:
                continue
            ion = r['ion'].strip()
            b = float(r['barrier_eV'])
        except (ValueError, KeyError):
            continue
        if ion == 'Mg':
            mg_b = b
        elif ion == 'Na':
            na_b = b
        elif ion == 'Li':
            li_b = b
    if mg_b is None or na_b is None or li_b is None:
        return 0.0
    if mg_b <= 0.3 and na_b <= 0.3 and mg_b < li_b and na_b < li_b:
        return 1.0
    return 0.0


_SCORERS = {
    'binding_key_values': score_0,
    'binding_li_site_reversal': score_1,
    'barrier_key_values': score_2,
    'barrier_monotonic': score_3,
    'li_barrier_minimum': score_4,
    'mg_na_similarity': score_5,
    'na_mg_low_at_large_c': score_6,
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
