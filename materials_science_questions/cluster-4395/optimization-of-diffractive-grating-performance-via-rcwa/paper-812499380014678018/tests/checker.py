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
    import json, os
    def prepare(outputs_dir, spec):
        return spec.get("gold", {})


# === block: score_0 (check id='check_peak_wavelength') ===
def score_0(artifact, step, ctx):
    import csv, math
    def score(artifact, step, ctx):
        try:
            with open('/app/outputs/shg_efficiency_spectrum.csv', newline='') as f:
                rows = list(csv.DictReader(f))
            if not rows:
                return 0.0
            max_row = max(rows, key=lambda r: float(r['efficiency_W-1']))
            peak_wl = float(max_row['wavelength_um'])
            if abs(peak_wl - ctx['peak_wavelength_um']) <= 0.02:
                return 1.0
            return 0.0
        except Exception:
            return 0.0


# === block: score_1 (check id='check_peak_efficiency') ===
def score_1(artifact, step, ctx):
    import csv, math
    def score(artifact, step, ctx):
        try:
            with open('/app/outputs/shg_efficiency_spectrum.csv', newline='') as f:
                rows = list(csv.DictReader(f))
            if not rows:
                return 0.0
            max_eff = max(float(r['efficiency_W-1']) for r in rows)
            ref = ctx['peak_efficiency_W-1']
            if ref == 0.0:
                return 0.0
            rel_diff = abs(max_eff - ref) / abs(ref)
            if rel_diff <= 0.10:
                return 1.0
            return 0.0
        except Exception:
            return 0.0


# === block: score_2 (check id='check_correlation') ===
def score_2(artifact, step, ctx):
    import csv, math
    def score(artifact, step, ctx):
        try:
            with open('/app/outputs/shg_efficiency_spectrum.csv', newline='') as f:
                rows = list(csv.DictReader(f))
            if len(rows) < 5:
                return 0.0
            wls = [float(r['wavelength_um']) for r in rows]
            effs = [float(r['efficiency_W-1']) for r in rows]
            peak_wl = float(ctx.get('peak_wavelength_um', 3.17))
            peak_eff = float(ctx.get('peak_efficiency_W-1', 8e-9))
            sigma = float(ctx.get('gaussian_sigma_um', 0.15))
            ref_effs = [peak_eff * math.exp(-(wl - peak_wl)**2 / (2 * sigma**2)) for wl in wls]
            n = len(wls)
            mean_eff = sum(effs) / n
            mean_ref = sum(ref_effs) / n
            num = sum((e - mean_eff) * (r - mean_ref) for e, r in zip(effs, ref_effs))
            den_a = sum((e - mean_eff)**2 for e in effs)
            den_b = sum((r - mean_ref)**2 for r in ref_effs)
            den = math.sqrt(den_a * den_b)
            if den == 0.0:
                return 0.0
            r = num / den
            if r > 0.98:
                return 1.0
            return 0.0
        except Exception:
            return 0.0


_SCORERS = {
    'check_peak_wavelength': score_0,
    'check_peak_efficiency': score_1,
    'check_correlation': score_2,
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
