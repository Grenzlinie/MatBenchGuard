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


# === block: score_0 (check id='step_02_bandgap') ===
def score_0(artifact, step, ctx):
    try:
        val = float(str(artifact).strip())
        target = step.get('target', 1.94)
        tol = step.get('tolerance_abs', 0.2)
        return 1.0 if abs(val - target) <= tol else 0.0
    except:
        return 0.0


# === block: score_1 (check id='step_06_refractive_index') ===
def score_1(artifact, step, ctx):
    try:
        val = float(str(artifact).strip())
        target = step.get('target', 2.26)
        tol = step.get('tolerance_abs', 0.1)
        return 1.0 if abs(val - target) <= tol else 0.0
    except:
        return 0.0


# === block: score_2 (check id='step_03_totaldos') ===
def score_2(artifact, step, ctx):
    import csv
    if not artifact or not isinstance(artifact, list):
        return 0.0
    cols = set(artifact[0].keys())
    if 'energy' not in cols or 'total_DOS' not in cols:
        return 0.0
    energies = []
    for row in artifact:
        try:
            e = float(row['energy'])
            d = float(row['total_DOS'])
            if d < 0:
                return 0.0
            energies.append(e)
        except:
            return 0.0
    if not energies:
        return 0.0
    emin, emax = min(energies), max(energies)
    if emin > -19 or emax < 14:  # must cover at least -20 to 15 roughly
        return 0.0
    return 1.0


# === block: score_3 (check id='step_04_pdos') ===
def score_3(artifact, step, ctx):
    import math
    if not artifact or not isinstance(artifact, list):
        return 0.0
    partial_cols = ['Cu_s','Cu_p','Cu_d','Al_s','Al_p','Al_d','S_s','S_p']
    cols = set(artifact[0].keys())
    if 'energy' not in cols or any(c not in cols for c in partial_cols):
        return 0.0
    # build energy-sorted list
    data = []
    for row in artifact:
        try:
            e = float(row['energy'])
            rowvals = {c: float(row[c]) for c in partial_cols}
            data.append((e, rowvals))
        except:
            pass
    if not data:
        return 0.0
    data.sort(key=lambda x: x[0])
    checks = step.get('checks', [])
    sub_scores = []
    for ck in checks:
        window = ck.get('window')
        num_cols = ck['numerator_columns']
        min_frac = ck.get('min_fraction', 0.0)
        lo, hi = window[0], window[1]
        num = 0.0
        den = 0.0
        for e, vals in data:
            if lo <= e <= hi:
                row_total = sum(vals.values())
                den += row_total
                num += sum(vals[cn] for cn in num_cols)
        if den <= 0:
            sub_scores.append(0.0)
        else:
            frac = num / den
            sub_scores.append(1.0 if frac >= min_frac else 0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_4 (check id='step_05_dielectric') ===
def score_4(artifact, step, ctx):
    import math
    if not artifact or not isinstance(artifact, list):
        return 0.0
    cols = set(artifact[0].keys())
    if 'energy' not in cols or 'epsilon2' not in cols:
        return 0.0
    im_vals = []
    for row in artifact:
        try:
            e = float(row['energy'])
            im = float(row['epsilon2'])
            if not math.isfinite(im) or im < 0:
                return 0.0
            im_vals.append((e, im))
        except:
            return 0.0
    if not im_vals:
        return 0.0
    checks = step.get('checks', [])
    sub_scores = []
    for ck in checks:
        if ck.get('type') == 'epsilon2_peak':
            lo, hi = ck['energy_range']
            min_val = ck.get('min_value', 0.0)
            peak = max((im for e,im in im_vals if lo <= e <= hi), default=-1.0)
            sub_scores.append(1.0 if peak >= min_val else 0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'step_02_bandgap': score_0,
    'step_06_refractive_index': score_1,
    'step_03_totaldos': score_2,
    'step_04_pdos': score_3,
    'step_05_dielectric': score_4,
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
