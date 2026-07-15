import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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


# === block: score_0 (check id='backscattering_coefficients_check') ===
def score_0(artifact, step, ctx):
        def safe_float(val):
            try:
                return float(val)
            except (TypeError, ValueError):
                return None

        cfg = step.get('config', {})
        gold_rows = cfg.get('gold_rows', [])
        rel_tol = cfg.get('tolerance_relative', 0.10)
        abs_tol = cfg.get('tolerance_abs', 0.02)
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        # build lookup from gold (safe: we control these)
        gold_lookup = {}
        for g in gold_rows:
            thick = str(g['foil_thickness_in_s0_or_inf']) if 'foil_thickness_in_s0_or_inf' in g else str(g.get('foil_thickness_in_s0_units', ''))
            key = (g['material'].lower(), thick, float(g['incident_energy_MeV']))
            gold_lookup[key] = float(g.get('backscattering_coefficient', 0.0))
        scores = []
        for row in artifact:
            # safely extract material
            mat = (row.get('material') or '').lower()
            # safely extract thickness
            if 'foil_thickness_in_s0_or_inf' in row:
                thick = (row['foil_thickness_in_s0_or_inf'] or '').strip().lower()
            else:
                thick = (row.get('foil_thickness_in_s0_units') or '').strip()
            # safely extract energy and backscattering coefficient
            energy = safe_float(row.get('incident_energy_MeV'))
            agent_val = safe_float(row.get('backscattering_coefficient'))
            if energy is None or agent_val is None:
                continue  # skip broken rows
            key = (mat, thick, energy)
            if key not in gold_lookup:
                continue
            gold_val = gold_lookup[key]
            diff = abs(agent_val - gold_val)
            tol = max(rel_tol * abs(gold_val), abs_tol)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
        if not scores:
            return 0.0
        avg = sum(scores) / len(scores)
        # structural factor check: for graphite, silver, lead at 1 MeV, verify ratio to experimental ref
        exp_ref = cfg.get('experimental_ref', {})
        for mat, exp_val in exp_ref.items():
            key = (mat, 'inf', 1.0)
            if key in gold_lookup:
                gold_val = gold_lookup[key]
                expected_ratio = gold_val / exp_val
            else:
                continue
            # find agent row with safe conversion
            for row in artifact:
                row_mat = (row.get('material') or '').lower()
                thick_str = (row.get('foil_thickness_in_s0_or_inf') or '').lower()
                row_energy = safe_float(row.get('incident_energy_MeV'))
                row_val = safe_float(row.get('backscattering_coefficient'))
                if row_mat == mat and thick_str == 'inf' and row_energy is not None and abs(row_energy - 1.0) < 1e-9:
                    if row_val is None:
                        continue
                    agent_ratio = row_val / exp_val
                    if abs(agent_ratio - expected_ratio) / expected_ratio <= 0.20:
                        scores.append(1.0)
                    else:
                        scores.append(0.0)
                    break
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='transmission_coefficients_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        cfg = step.get('config', {})
        gold_rows = cfg.get('gold_rows', [])
        rel_tol = cfg.get('tolerance_relative', 0.20)
        abs_tol = cfg.get('tolerance_abs', 0.02)
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        gold_lookup = {}
        for g in gold_rows:
            key = (g['material'].lower(), float(g['foil_thickness_in_s0_units']), float(g['incident_energy_MeV']))
            gold_lookup[key] = float(g['transmission_coefficient'])
        scores = []
        for row in artifact:
            key = (row['material'].lower(), float(row['foil_thickness_in_s0_units']), float(row['incident_energy_MeV']))
            if key not in gold_lookup:
                continue
            agent_val = float(row['transmission_coefficient'])
            gold_val = gold_lookup[key]
            diff = abs(agent_val - gold_val)
            tol = max(rel_tol * abs(gold_val), abs_tol)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff - tol) / tol))
        return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='energy_deposition_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        cfg = step.get('config', {})
        gold_depths = cfg.get('gold_depths', [])
        gold_vals = cfg.get('gold_normalized', [])
        peak_tol = cfg.get('peak_depth_tol', 0.05)
        rmse_thresh = cfg.get('rmse_threshold', 5.0)
        if not isinstance(artifact, list) or not artifact or not gold_depths:
            return 0.0
        # extract agent depths and normalized values
        depths = []
        vals = []
        for row in artifact:
            depth = float(row['depth_in_s0_units'])
            val = float(row['energy_deposition_normalized'])
            depths.append(depth)
            vals.append(val)
        if not depths:
            return 0.0
        # align agent data to gold grid by nearest matching depth
        aligned = []
        for d, v in zip(depths, vals):
            idx = int(round(d * 20))  # assuming 0.05 spacing -> index = round(d/0.05)
            # clamp to gold range
            if 0 <= idx < len(gold_depths):
                aligned.append((idx, v))
        if not aligned:
            return 0.0
        # compute RMSE
        sse = 0.0
        for idx, v in aligned:
            sse += (v - gold_vals[idx]) ** 2
        mse = sse / len(aligned)
        # score: full credit if rmse <= 0, linear decay to 0 at rmse_thresh
        rmse_score = max(0.0, 1.0 - math.sqrt(mse) / rmse_thresh)
        # find peak depth: agent's depth at maximum normalized value
        max_idx = vals.index(max(vals))
        agent_peak = depths[max_idx]
        # assumed gold peak at 0.25
        gold_peak = 0.25
        peak_diff = abs(agent_peak - gold_peak)
        peak_score = 1.0 if peak_diff <= peak_tol else 0.0
        # combined score
        return 0.5 * rmse_score + 0.5 * peak_score


_SCORERS = {
    'backscattering_coefficients_check': score_0,
    'transmission_coefficients_check': score_1,
    'energy_deposition_check': score_2,
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
