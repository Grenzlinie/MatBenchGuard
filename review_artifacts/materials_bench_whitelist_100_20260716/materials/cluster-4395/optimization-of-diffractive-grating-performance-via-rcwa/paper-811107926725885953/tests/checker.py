import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math
import os


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
        # Read step_02.csv and recompute peak efficiency and center wavelength for each config
        spec_steps = spec.get("steps", [])
        step_02_config = None
        for s in spec_steps:
            if s["id"] == "step_02":
                step_02_config = s.get("gold", {}).get("configs", [])
                break
        if step_02_config is None:
            raise Exception("step_02 config not found")

        artifact_path = os.path.join(outputs_dir, "step_02_efficiency_spectra.csv")
        if not os.path.exists(artifact_path):
            return {"step_02_peaks": None}

        rows = []
        with open(artifact_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        peaks = {}
        for cfg in step_02_config:
            pol = cfg["polarization"]
            wl_min, wl_max = cfg["wavelength_range"]
            max_eff = -1.0
            best_wl = None
            for row in rows:
                if row["polarization"] == pol:
                    wl = float(row["wavelength_nm"])
                    eff = float(row["coupling_efficiency"])
                    if wl_min <= wl <= wl_max and eff > max_eff:
                        max_eff = eff
                        best_wl = wl
            # key: e.g., TE_1550
            if pol == "TE":
                key = f"TE_{cfg['operational_wavelength_nm']}"
            else:
                key = f"TM_{cfg['operational_wavelength_nm']}"
            peaks[key] = {"peak_efficiency": max_eff, "center_wavelength_nm": best_wl}

        return {"step_02_peaks": peaks}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        gold_configs = step.get("gold", {}).get("configs", [])
        if not gold_configs:
            return 0.0

        if artifact is None:
            return 0.0

        # Build lookup from csv rows
        rows = artifact  # already parsed as list of dicts
        total_score = 0.0
        n = len(gold_configs)
        if n == 0:
            return 0.0

        for gc in gold_configs:
            pol = gc["polarization"]
            wl = gc["wavelength_um"]
            target_period = gc["period_nm"]
            target_ff = gc["fill_factor"]
            period_tol = gc["period_tol_nm"]
            ff_tol = gc["fill_factor_tol"]

            # find matching row
            row = None
            for r in rows:
                if r["polarization"] == pol and abs(float(r["wavelength_um"]) - wl) < 0.005:
                    row = r
                    break
            if row is None:
                # missing row -> score 0 for this config
                continue

            period = float(row["period_nm"])
            ff = float(row["fill_factor"])

            # score period: 1 if within tolerance, else 0; but we can give partial credit based on distance
            period_err = abs(period - target_period)
            period_score = max(0.0, 1.0 - period_err / (period_tol * 2.0)) if period_tol > 0 else 0.0
            ff_err = abs(ff - target_ff)
            ff_score = max(0.0, 1.0 - ff_err / (ff_tol * 2.0)) if ff_tol > 0 else 0.0

            total_score += (period_score + ff_score) / 2.0

        return total_score / n


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
        peaks = ctx.get("step_02_peaks")
        if peaks is None:
            return 0.0

        gold_configs = step.get("gold", {}).get("configs", [])
        if not gold_configs:
            return 0.0

        n = len(gold_configs)
        total = 0.0
        for cfg in gold_configs:
            pol = cfg["polarization"]
            op_wl = cfg["operational_wavelength_nm"]
            paper_eff = cfg["paper_peak_efficiency"]
            center_tol = cfg["center_tolerance_nm"]
            key = f"{pol}_{op_wl}"
            entry = peaks.get(key)
            if entry is None or entry["center_wavelength_nm"] is None:
                continue
            peak_eff = entry["peak_efficiency"]
            center_wl = entry["center_wavelength_nm"]

            # Efficiency score: higher is better; full credit if >= paper_eff, else linear down to 0.0 at paper_eff*0.5
            eff_threshold = paper_eff  # meeting paper gets full
            if peak_eff >= eff_threshold:
                eff_score = 1.0
            else:
                reduction = (eff_threshold - peak_eff) / (eff_threshold * 0.5)
                eff_score = max(0.0, 1.0 - reduction)

            # Center wavelength score: within tolerance gives full, else linear
            wl_diff = abs(center_wl - op_wl)
            if wl_diff <= center_tol:
                wl_score = 1.0
            else:
                wl_score = max(0.0, 1.0 - (wl_diff - center_tol) / (op_wl * 0.02))

            total += (0.5 * eff_score + 0.5 * wl_score)

        return total / n if n > 0 else 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
        if artifact is None or not isinstance(artifact, dict):
            return 0.0

        peaks = ctx.get("step_02_peaks")
        if peaks is None:
            return 0.0

        required_keys = ["TE_1550", "TE_1310", "TM_1550", "TM_1310"]
        ok = 0
        total = len(required_keys)
        for key in required_keys:
            if key not in artifact:
                continue
            val = artifact[key]
            if not isinstance(val, dict):
                continue
            if "peak_efficiency" not in val or "center_wavelength_nm" not in val:
                continue
            # Compare with recomputed values
            ref = peaks.get(key)
            if ref is None:
                continue
            eff_diff = abs(float(val["peak_efficiency"]) - ref["peak_efficiency"]) if ref["peak_efficiency"] is not None else 0.0
            wl_diff = abs(float(val["center_wavelength_nm"]) - ref["center_wavelength_nm"]) if ref["center_wavelength_nm"] is not None else 0.0
            if eff_diff <= 0.01 and wl_diff <= 1.0:
                ok += 1

        return ok / total if total > 0 else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
