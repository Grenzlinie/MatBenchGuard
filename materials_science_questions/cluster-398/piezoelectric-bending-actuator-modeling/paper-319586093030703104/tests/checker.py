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
    U0_V = 3000.0
    statV_per_V = 300.0
    L_mm = 1.0
    L_cm = L_mm / 10.0
    d24_cgse = 9e-8
    arcsec_per_rad = 206265.0
    omega_g_arcsec = 0.7

    U0_stat = U0_V / statV_per_V
    Phi_rad = 2.0 * U0_stat * d24_cgse / L_cm
    Phi_arcsec = Phi_rad * arcsec_per_rad
    gain = Phi_arcsec / omega_g_arcsec

    ctx = {
        'gold_width_arcsec': Phi_arcsec,
        'gold_gain': gain,
        'natural_width_arcsec': omega_g_arcsec,
        'tolerance_width': 0.2,
        'tolerance_gain': 0.4
    }
    return ctx


# === block: score_0 (check id='step_3') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0

    score_parts = []

    # natural mosaic width exact check
    nat_w = data.get('natural_mosaic_width_arcsec')
    if nat_w is not None and abs(nat_w - ctx['natural_width_arcsec']) < 1e-6:
        score_parts.append(1.0)
    else:
        score_parts.append(0.0)

    # piezo-quasi-mosaic width
    rep_w = data.get('piezo_quasi_mosaic_width_arcsec')
    if rep_w is not None:
        diff = abs(rep_w - ctx['gold_width_arcsec'])
        if diff <= ctx['tolerance_width']:
            score_parts.append(1.0)
        else:
            score_parts.append(max(0.0, 1.0 - (diff - ctx['tolerance_width']) / ctx['tolerance_width']))
    else:
        score_parts.append(0.0)

    # relative gain
    rep_g = data.get('relative_gain')
    if rep_g is not None:
        diff = abs(rep_g - ctx['gold_gain'])
        if diff <= ctx['tolerance_gain']:
            score_parts.append(1.0)
        else:
            score_parts.append(max(0.0, 1.0 - (diff - ctx['tolerance_gain']) / ctx['tolerance_gain']))
    else:
        score_parts.append(0.0)

    sub_weights = [0.1, 0.4, 0.5]
    return sum(s * w for s, w in zip(score_parts, sub_weights))


_SCORERS = {
    'step_3': score_0,
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
