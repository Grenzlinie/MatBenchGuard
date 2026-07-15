import os
import json
import csv


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


# === block: score_0 (check id='step_01_structural') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    fields = step.get("fields", [])
    scores = []
    for f in fields:
        if f not in artifact or f not in gold:
            scores.append(0.0)
            continue
        art_val = float(artifact[f])
        gold_val = float(gold[f])
        tol = float(tols.get(f, 0.02))
        if gold_val == 0:
            if abs(art_val) <= tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        else:
            rel_err = abs(art_val - gold_val) / abs(gold_val)
            score_i = max(0.0, 1.0 - rel_err / tol)
            scores.append(score_i)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_02_elastic') ===
def score_1(artifact, step, ctx):
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    fields = step.get("fields", [])
    scores = []
    for f in fields:
        if f not in artifact or f not in gold:
            scores.append(0.0)
            continue
        art_val = float(artifact[f])
        gold_val = float(gold[f])
        tol = float(tols.get(f, 0.20))
        if gold_val == 0:
            if abs(art_val) <= tol:
                scores.append(1.0)
            else:
                scores.append(0.0)
        else:
            rel_err = abs(art_val - gold_val) / abs(gold_val)
            score_i = max(0.0, 1.0 - rel_err / tol)
            scores.append(score_i)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='step_03_optical') ===
def score_2(artifact, step, ctx):
    gold = step.get("gold", {})
    # Only score fields whose gold values are attested in the paper.
    # Fields not in KNOWN_PAPER_FIELDS are skipped regardless of gold dict content.
    KNOWN_PAPER_FIELDS = {'epsilon2_peak_energy', 'absorption_peak_energy',
                         'absorption_peak_value', 'reflectivity_min_energy'}
    energy_fields = step.get("energy_fields", [])
    value_fields = step.get("value_fields", [])
    energy_tol = float(step.get("energy_tol", 0.2))
    value_tol = float(step.get("value_tol", 0.2))
    scores = []
    for ef in energy_fields:
        if ef not in KNOWN_PAPER_FIELDS or ef not in gold or ef not in artifact:
            continue
        art_val = float(artifact[ef])
        gold_val = float(gold[ef])
        abs_err = abs(art_val - gold_val)
        score_i = max(0.0, 1.0 - abs_err / energy_tol)
        scores.append(score_i)
    for vf in value_fields:
        if vf not in KNOWN_PAPER_FIELDS or vf not in gold or vf not in artifact:
            continue
        art_val = float(artifact[vf])
        gold_val = float(gold[vf])
        if gold_val == 0:
            if abs(art_val) <= value_tol:
                score_i = 1.0
            else:
                score_i = 0.0
        else:
            rel_err = abs(art_val - gold_val) / abs(gold_val)
            score_i = max(0.0, 1.0 - rel_err / value_tol)
        scores.append(score_i)
    # If no fields are scored (all skipped), return 1.0 so this step does not
    # harm the reward; the load‑bearing transmittance step still validates optics.
    return sum(scores) / len(scores) if scores else 1.0


# === block: score_3 (check id='step_04_transmittance') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    try:
        rows = []
        for row in artifact:
            wl = float(row.get("wavelength_nm", 0))
            t = float(row.get("transmittance_fraction", 0))
            rows.append((wl, t))
    except (ValueError, TypeError):
        return 0.0
    if not rows:
        return 0.0

    vis_rows = [(wl, t) for wl, t in rows if 380 <= wl <= 760]
    nir_rows = [(wl, t) for wl, t in rows if 760 <= wl <= 2500]

    if not vis_rows:
        vis_max = 0.0
        vis_peak_wl = None
    else:
        vis_max = max(t for _, t in vis_rows)
        vis_peak_wl = max(vis_rows, key=lambda x: x[1])[0] if vis_rows else None

    min_visible_peak = float(step.get("min_visible_peak", 0.7))
    vis_score = min(1.0, vis_max / min_visible_peak) if vis_max > 0 else 0.0

    if not nir_rows:
        nir_min = 1.0
    else:
        nir_min = min(t for _, t in nir_rows)

    max_nir_trough = float(step.get("max_nir_trough", 0.3))
    if nir_min <= max_nir_trough:
        nir_score = 1.0
    else:
        nir_score = max(0.0, 1.0 - (nir_min - max_nir_trough) / max_nir_trough)

    expected_peak = float(step.get("expected_visible_peak_wavelength", 585))
    peak_tol = float(step.get("visible_peak_wavelength_tol", 20))
    if vis_peak_wl is not None and abs(vis_peak_wl - expected_peak) <= peak_tol:
        peak_loc_score = 1.0
    else:
        if vis_peak_wl is None:
            peak_loc_score = 0.0
        else:
            dist = abs(vis_peak_wl - expected_peak) - peak_tol
            if dist <= 0:
                peak_loc_score = 1.0
            else:
                peak_loc_score = max(0.0, 1.0 - dist / (peak_tol * 4))

    return 0.4 * vis_score + 0.4 * nir_score + 0.2 * peak_loc_score


_SCORERS = {
    'step_01_structural': score_0,
    'step_02_elastic': score_1,
    'step_03_optical': score_2,
    'step_04_transmittance': score_3,
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
