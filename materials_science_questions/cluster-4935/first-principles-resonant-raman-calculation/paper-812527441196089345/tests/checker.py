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


# === block: score_0 (check id='compute_raman_enhancement') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts with keys wavelength_nm, raman_enhancement, stored_energy_enhancement
    rows = artifact
    if not rows or len(rows) < 5:
        return 0.0

    # Extract numeric data
    data = []
    for r in rows:
        try:
            wl = float(r['wavelength_nm'])
            re = float(r['raman_enhancement'])
            se = float(r['stored_energy_enhancement'])
            data.append((wl, re, se))
        except Exception:
            pass

    if len(data) < 5:
        return 0.0

    data.sort(key=lambda x: x[0])

    # Peak of Raman enhancement
    max_re = -1.0
    peak_wl = None
    for wl, re, se in data:
        if re > max_re:
            max_re = re
            peak_wl = wl

    if peak_wl is None:
        return 0.0

    score = 0.0

    # 1) Peak wavelength must lie in magnetic dipole region (540–570 nm)
    if 540 <= peak_wl <= 570:
        score += 0.4
    else:
        # partial credit if close (500–600)
        if 500 <= peak_wl <= 600:
            score += 0.2

    # 2) Off-resonance drop: RE at ~400 nm and ~800 nm well below peak
    # Helper: find row nearest to target wavelength
    def get_val_at(target, data):
        best = None
        best_dist = 1e9
        for wl, re, se in data:
            d = abs(wl - target)
            if d < best_dist:
                best_dist = d
                best = (wl, re, se)
        return best

    val400 = get_val_at(400.0, data)
    if val400 and val400[1] < 0.6 * max_re:
        score += 0.15

    val800 = get_val_at(800.0, data)
    if val800 and val800[1] < 0.6 * max_re:
        score += 0.15

    # 3) Stored energy enhancement peak in reasonable range
    max_se = -1.0
    peak_se_wl = None
    for wl, re, se in data:
        if se > max_se:
            max_se = se
            peak_se_wl = wl

    if peak_se_wl is not None and 535 <= peak_se_wl <= 585:
        score += 0.2

    # 4) At the Raman peak, RE > stored energy enhancement (paper's trend)
    peak_re_val = max_re
    peak_se_val = None
    for wl, re, se in data:
        if wl == peak_wl:
            peak_se_val = se
            break
    if peak_se_val is not None and peak_re_val > peak_se_val:
        score += 0.1

    return min(1.0, score)


_SCORERS = {
    'compute_raman_enhancement': score_0,
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
