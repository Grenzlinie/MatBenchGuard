import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math


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


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    import re
    gold_vals = step.get('gold_values', [])
    tol = step.get('tolerance_rel', 0.30)
    # Extract all signed floating-point numbers from the artifact (handles labels, commas, etc.)
    nums = [float(m) for m in re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', artifact.strip())]
    scores = []
    for i, g in enumerate(gold_vals):
        if i >= len(nums):
            scores.append(0.0)
            continue
        v = nums[i]
        rel_err = abs(v - g) / (abs(g) + 1e-9)
        scores.append(1.0 if rel_err <= tol else 0.0)
    return sum(scores) / len(gold_vals) if gold_vals else 0.0


# === block: score_1 (check id='zone_center_phonons') ===
def score_1(artifact, step, ctx):
    # Only score against the 15 modes whose DFT frequencies are reported in the paper (Table III).
    paper_freqs = {119.0, 137.0, 173.0, 216.0, 335.0, 422.0, 476.0, 482.0, 616.0, 1159.0, 1181.0, 2206.0, 2209.0, 2243.0, 2280.0}
    gold_modes = [gm for gm in step.get('gold_modes', []) if gm.get('freq') in paper_freqs]
    if not gold_modes:
        return 0.0

    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    abs_tol = step.get('freq_tolerance_abs', 15.0)
    rel_tol = step.get('freq_tolerance_rel', 0.05)
    matched = 0
    for gm in gold_modes:
        gfreq = gm['freq']
        girrep = gm['irrep']
        best_row = None
        best_diff = float('inf')
        for row in rows:
            if row.get('irrep', '').strip() != girrep:
                continue
            try:
                freq = float(row['frequency_cm1'])
            except (ValueError, KeyError):
                continue
            diff = abs(freq - gfreq)
            if diff < best_diff:
                best_diff = diff
                best_row = row
        if best_row is not None:
            tolerance = max(abs_tol, rel_tol * abs(gfreq))
            if best_diff <= tolerance:
                matched += 1
    return matched / len(gold_modes) if gold_modes else 0.0


# === block: score_2 (check id='mode_gruneisen') ===
def score_2(artifact, step, ctx):
    gruneisen_rows = artifact
    if not isinstance(gruneisen_rows, list) or not gruneisen_rows:
        return 0.0
    # Load zone_center file to get irrep by mode_index
    zone_path = os.path.join(step.get('_outputs_dir', '/app/outputs'), 'zone_center_phonon_frequencies.txt')
    zone_index_map = {}
    try:
        with open(zone_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    idx = int(row['mode_index'])
                except (ValueError, KeyError):
                    continue
                zone_index_map[idx] = {
                    'irrep': row.get('irrep', '').strip(),
                    'freq': float(row.get('frequency_cm1', 0))
                }
    except Exception:
        return 0.0

    # Only score against the 15 modes whose DFT frequencies and Gamma are reported in the paper (Table III).
    paper_freqs = {119.0, 137.0, 173.0, 216.0, 335.0, 422.0, 476.0, 482.0, 616.0, 1159.0, 1181.0, 2206.0, 2209.0, 2243.0, 2280.0}
    gold_modes = [gm for gm in step.get('gold_modes', []) if gm.get('freq') in paper_freqs]
    if not gold_modes:
        return 0.0

    gamma_tol_rel = step.get('gamma_tolerance_rel', 0.50)
    gamma_tol_zero = step.get('gamma_tolerance_abs_for_zero', 0.5)
    matched = 0
    for gm in gold_modes:
        ggamma = gm['gamma']
        girrep = gm['irrep']
        gfreq = gm['freq']
        best_match = None
        best_diff = float('inf')
        for row in gruneisen_rows:
            try:
                idx = int(row['mode_index'])
                agent_freq = float(row['frequency_at_V0_cm1'])
                agent_gamma = float(row['gruneisen_parameter'])
            except (ValueError, KeyError):
                continue
            if idx not in zone_index_map:
                continue
            if zone_index_map[idx]['irrep'] != girrep:
                continue
            diff = abs(agent_freq - gfreq)
            if diff < best_diff:
                best_diff = diff
                best_match = agent_gamma
        if best_match is None:
            continue
        # tolerance for frequency matching
        if best_diff > max(15.0, 0.05 * abs(gfreq)):
            continue
        if abs(ggamma) < 1e-9:
            if abs(best_match) <= gamma_tol_zero:
                matched += 1
        else:
            if (ggamma > 0 and best_match > 0) or (ggamma < 0 and best_match < 0):
                rel_err = abs(best_match - ggamma) / (abs(ggamma) + 1e-9)
                if rel_err <= gamma_tol_rel:
                    matched += 1
    return matched / len(gold_modes) if gold_modes else 0.0


# === block: score_3 (check id='thermal_expansion') ===
def score_3(artifact, step, ctx):
    line = artifact.strip()
    try:
        val = float(line)
    except ValueError:
        return 0.0
    gold = step.get('gold_value', 15.6)
    tol = step.get('tolerance_rel', 0.30)
    if abs(gold) < 1e-9:
        return 0.0
    rel_err = abs(val - gold) / abs(gold)
    return 1.0 if rel_err <= tol else 0.0


_SCORERS = {
    'elastic_constants': score_0,
    'zone_center_phonons': score_1,
    'mode_gruneisen': score_2,
    'thermal_expansion': score_3,
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
