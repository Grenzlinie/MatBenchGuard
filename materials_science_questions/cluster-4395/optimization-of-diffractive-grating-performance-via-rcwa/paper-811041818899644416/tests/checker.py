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


# === block: score_0 (check id='check_spectral_data') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step["params"]
        targets = params["targets"]
        max_wl_tol = params["max_wl_tol"]
        refl_min = params["reflectance_min"]
        sub = params["sub_weights"]

        rows = []
        for r in artifact:
            try:
                wl = float(r.get("wavelength_um", math.nan))
                ph = float(r.get("phase_difference_rad", math.nan))
                ref = float(r.get("reflectance", math.nan))
                if not (math.isfinite(wl) and math.isfinite(ph) and math.isfinite(ref)):
                    continue
                rows.append((wl, ph, ref))
            except:
                continue

        if len(rows) == 0:
            return 0.0

        phase_scores = []
        refl_scores = []
        for t in targets:
            twl = t["wavelength_um"]
            tphase = t["phase_target"]
            tptol = t["phase_tol"]
            best = None
            best_diff = 1e9
            for r in rows:
                diff = abs(r[0] - twl)
                if diff < best_diff:
                    best_diff = diff
                    best = r
            if best is None or best_diff > max_wl_tol:
                phase_scores.append(0.0)
                refl_scores.append(0.0)
            else:
                phase_diff = abs(best[1] - tphase)
                phase_scores.append(1.0 if phase_diff <= tptol else 0.0)
                refl_scores.append(1.0 if best[2] >= refl_min else 0.0)

        sorted_rows = sorted(rows, key=lambda x: x[0])
        mono = True
        prev_phase = None
        for wl, ph, _ in sorted_rows:
            if prev_phase is not None and ph > prev_phase + 1e-9:
                mono = False
                break
            prev_phase = ph
        mono_score = 1.0 if mono else 0.0

        n = len(targets)
        ph_avg = sum(phase_scores) / n if n>0 else 0.0
        ref_avg = sum(refl_scores) / n if n>0 else 0.0

        total = sub["phase"] * ph_avg + sub["reflectance"] * ref_avg + sub["monotonic"] * mono_score
        return total


# === block: score_1 (check id='check_beta_one_theta') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step["params"]
        target_wls = params["target_wavelengths"]
        max_wl_tol = params["max_wl_tol"]
        theta_min = params["theta_min"]
        theta_max = params["theta_max"]

        rows_list = []
        for r in artifact:
            try:
                wl = float(r.get("wavelength_um", math.nan))
                th = float(r.get("theta_deg", math.nan))
                if not (math.isfinite(wl) and math.isfinite(th)):
                    continue
                rows_list.append((wl, th))
            except:
                continue

        score = 0.0
        for twl in target_wls:
            best_th = None
            best_diff = 1e9
            for wl, th in rows_list:
                diff = abs(wl - twl)
                if diff < best_diff:
                    best_diff = diff
                    best_th = th
            if best_th is not None and best_diff <= max_wl_tol and theta_min <= best_th <= theta_max:
                score += 1.0
        total = score / len(target_wls) if target_wls else 0.0
        return total


_SCORERS = {
    'check_spectral_data': score_0,
    'check_beta_one_theta': score_1,
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
