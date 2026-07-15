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


# === block: score_0 (check id='eval_halfwidths') ===
def score_0(artifact, step, ctx):
    expected_rows = step.get('expected_rows', [])
    agent_rows = artifact   # list of dicts from CSV

    # build lookup
    lookup = {}
    for r in expected_rows:
        key = (float(r['temperature_K']), float(r['well_width_nm']), float(r['magnetic_field_T']), float(r['deformation_potential_eV']))
        lookup[key] = float(r['half_width_meV'])

    total = len(expected_rows)
    if total == 0:
        return 1.0  # trivially pass if no expectations, but normally not

    matched = 0
    rel_tol = 0.05
    abs_floor = 1e-6
    for arow in agent_rows:
        try:
            key = (float(arow['temperature_K']), float(arow['well_width_nm']), float(arow['magnetic_field_T']), float(arow['deformation_potential_eV']))
            gold = lookup.get(key)
            if gold is None:
                continue
            agent_val = float(arow['half_width_meV'])
            if gold == 0.0:
                if abs(agent_val) <= abs_floor:
                    matched += 1
            else:
                rel_err = abs(agent_val - gold) / max(abs(gold), 1e-12)
                if rel_err <= rel_tol or abs(agent_val - gold) < abs_floor:
                    matched += 1
        except (KeyError, ValueError):
            pass

    score_numeric = matched / total

    # trend checks
    # temperature increasing (T=0..100 at B=4, Lz=31)
    temp_rows = sorted(
        [r for r in agent_rows if abs(float(r['well_width_nm'])-31.0)<0.1 and abs(float(r['magnetic_field_T'])-4.0)<0.1],
        key=lambda x: float(x['temperature_K'])
    )
    trend_temp = False
    if len(temp_rows) >= 2:
        vals = [float(r['half_width_meV']) for r in temp_rows]
        trend_temp = all(vals[i] <= vals[i+1] + 1e-12 for i in range(len(vals)-1))

    # well-width peak near 32 nm (T=30, B=4)
    well_rows = sorted(
        [r for r in agent_rows if abs(float(r['temperature_K'])-30.0)<0.1 and abs(float(r['magnetic_field_T'])-4.0)<0.1],
        key=lambda x: float(x['well_width_nm'])
    )
    trend_peak = False
    if well_rows:
        vals = [float(r['half_width_meV']) for r in well_rows]
        max_val = max(vals)
        max_idx = vals.index(max_val)
        Lz_at_max = float(well_rows[max_idx]['well_width_nm'])
        if 28.0 <= Lz_at_max <= 38.0:
            # additionally check it is a local maximum (greater than neighbors)
            if 0 < max_idx < len(vals)-1:
                if max_val > vals[max_idx-1] + 1e-12 and max_val > vals[max_idx+1] + 1e-12:
                    trend_peak = True
            else:
                trend_peak = True  # peak at edge is acceptable

    # half_width at 2T > at 4T (T=30, Lz=45)
    mag_rows = {}
    for r in agent_rows:
        if abs(float(r['temperature_K'])-30.0)<0.1 and abs(float(r['well_width_nm'])-45.0)<0.1:
            mag_rows[float(r['magnetic_field_T'])] = float(r['half_width_meV'])
    trend_mag = mag_rows.get(2.0, -1) > mag_rows.get(4.0, -1) if 2.0 in mag_rows and 4.0 in mag_rows else False

    score_trends = (int(trend_temp) + int(trend_peak) + int(trend_mag)) / 3.0
    return 0.7 * score_numeric + 0.3 * score_trends


_SCORERS = {
    'eval_halfwidths': score_0,
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
