import os
import json
import csv

# === author imports / helpers ===
import statistics


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


# === block: score_0 (check id='step_04_kinetic_energy') ===
def score_0(artifact, step, ctx):
    try:
        rows = [row for row in artifact if row]
        max_time = step['params']['max_early_time_ps']
        min_ratio = step['params']['min_early_ratio']
        early = []
        for row in rows:
            t = float(row['time_ps'])
            if t <= max_time:
                early.append((float(row['avg_ke_si_free_eV']), float(row['avg_ke_si_doped_eV'])))
        if not early:
            return 0.0
        ok = sum(1 for f, d in early if d > 0 and f > min_ratio * d)
        return ok / len(early)
    except:
        return 0.0


# === block: score_1 (check id='step_05_geometric_deformation') ===
def score_1(artifact, step, ctx):
    try:
        rows = [row for row in artifact if row]
        min_time = step['params']['min_time_ps']
        later = []
        for row in rows:
            t = float(row['time_ps'])
            if t >= min_time:
                later.append((float(row['D_si_free_angstrom']), float(row['D_si_doped_angstrom'])))
        if not later:
            return 0.0
        ok = sum(1 for fe, de in later if de < fe)
        return ok / len(later)
    except:
        return 0.0


# === block: score_2 (check id='step_06_hamming_distance') ===
def score_2(artifact, step, ctx):
    try:
        rows = [row for row in artifact if row]
        dh_free = [float(row['DH_si_free']) for row in rows]
        dh_doped = [float(row['DH_si_doped']) for row in rows]
        if not dh_free or not dh_doped:
            return 0.0
        avg_free = statistics.mean(dh_free)
        avg_doped = statistics.mean(dh_doped)
        if avg_free == 0:
            return 0.0 if avg_doped != 0 else 1.0
        ratio = avg_doped / avg_free
        target = step['params']['expected_ratio']
        tol = step['params']['ratio_tolerance']
        if ratio <= target:
            return 1.0
        excess = ratio - target
        score = max(0.0, 1.0 - excess / tol)
        return score
    except:
        return 0.0


# === block: score_3 (check id='step_07_bop_before') ===
def score_3(artifact, step, ctx):
    try:
        rows = [row for row in artifact if row]
        pos_min = step['params']['pos_peak_bop_min']
        sharpness = step['params']['peak_sharpness_threshold']
        free_vals = []
        doped_vals = []
        free_pos = []
        doped_pos = []
        for row in rows:
            bv = float(row['bop_value'])
            sf = float(row['frequency_si_free'])
            sd = float(row['frequency_si_doped'])
            free_vals.append(sf)
            doped_vals.append(sd)
            if bv >= pos_min:
                free_pos.append(sf)
                doped_pos.append(sd)
        if not free_pos:
            return 0.0
        max_free = max(free_pos)
        max_doped = max(doped_pos) if doped_pos else 0.0
        if max_doped <= 0:
            return 1.0 if max_free > 0 else 0.0
        return 1.0 if max_free >= sharpness * max_doped else 0.0
    except:
        return 0.0


# === block: score_4 (check id='step_08_bop_after') ===
def score_4(artifact, step, ctx):
    try:
        rows = [row for row in artifact if row]
        neg_max = step['params']['neg_peak_bop_max']
        sharpness = step['params']['peak_sharpness_threshold']
        free_neg = []
        doped_neg = []
        for row in rows:
            bv = float(row['bop_value'])
            sf = float(row['frequency_si_free'])
            sd = float(row['frequency_si_doped'])
            if bv <= neg_max:
                free_neg.append(sf)
                doped_neg.append(sd)
        if not free_neg:
            return 0.0
        max_free = max(free_neg)
        max_doped = max(doped_neg) if doped_neg else 0.0
        if max_doped <= 0:
            return 1.0 if max_free > 0 else 0.0
        return 1.0 if max_free >= sharpness * max_doped else 0.0
    except:
        return 0.0


_SCORERS = {
    'step_04_kinetic_energy': score_0,
    'step_05_geometric_deformation': score_1,
    'step_06_hamming_distance': score_2,
    'step_07_bop_before': score_3,
    'step_08_bop_after': score_4,
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
