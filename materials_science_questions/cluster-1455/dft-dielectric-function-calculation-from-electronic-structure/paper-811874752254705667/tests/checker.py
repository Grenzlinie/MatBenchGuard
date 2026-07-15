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
    ctx = {}
    for step in spec.get("steps", []):
        sid = step.get("id")
        if sid == "band_gap":
            ctx["band_gap_target"] = step["target"]
            ctx["band_gap_tol"] = step["tolerance"]
        elif sid == "pdos_analysis":
            ctx["pdos_checks"] = step["checks"]
        elif sid == "dielectric_function":
            ctx["dielectric_params"] = {
                "peak_targets": step["peak_targets"],
                "peak_tolerance": step["peak_tolerance"],
                "isotropy_max_energy": step["isotropy_max_energy"],
                "max_rel_diff_isotropy": step["max_rel_diff_isotropy"],
                "anisotropy_min_energy": step["anisotropy_min_energy"],
                "anisotropy_min_diff": step["anisotropy_min_diff"]
            }
    return ctx


# === block: score_0 (check id='band_gap') ===
def score_0(artifact, step, ctx):
    val = artifact.get({"indirect_band_gap_eV"})
    if val is None:
        return 0.0
    target = ctx["band_gap_target"]
    tol = ctx["band_gap_tol"]
    if abs(val - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='pdos_analysis') ===
def score_1(artifact, step, ctx):
    artifact_dict = artifact
    checks = ctx["pdos_checks"]
    total = 0.0
    count = 0
    # low_band_peak
    c = checks["low_band_peak"]
    val = artifact_dict.get(c["field"])
    if val is not None and abs(val - c["target"]) <= c["tolerance"]:
        total += 1.0
    count += 1
    # valence_band_min, max, conduction_hybrid min/max
    for key in ["valence_band_min", "valence_band_max", "conduction_hybrid_min", "conduction_hybrid_max"]:
        c = checks[key]
        val = artifact_dict.get(c["field"])
        if val is not None and abs(val - c["target"]) <= c["tolerance"]:
            total += 1.0
        count += 1
    # ta_o_hybridization
    c = checks["ta_o_hybridization"]
    val = artifact_dict.get(c["field"])
    if val == c["expected"]:
        total += 1.0
    count += 1
    return total / count if count > 0 else 0.0


# === block: score_2 (check id='dielectric_function') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    energies = []
    avg = []
    xx = []
    yy = []
    zz = []
    for r in rows:
        try:
            e = float(r["energy_eV"])
            a = float(r["epsilon2_avg"])
            x = float(r["epsilon2_xx"])
            y = float(r["epsilon2_yy"])
            z = float(r["epsilon2_zz"])
        except Exception:
            continue
        energies.append(e)
        avg.append(a)
        xx.append(x)
        yy.append(y)
        zz.append(z)

    # peak detection in epsilon2_avg
    peaks = []
    n = len(avg)
    for i in range(1, n-1):
        if avg[i] > avg[i-1] and avg[i] > avg[i+1] and avg[i] > 0.5:
            peaks.append(energies[i])

    params = ctx["dielectric_params"]
    targets = params["peak_targets"]
    tol = params["peak_tolerance"]
    matched = 0
    for t in targets:
        for p in peaks:
            if abs(p - t) <= tol:
                matched += 1
                break
    peak_score = matched / len(targets) if targets else 1.0

    # isotropy below max energy
    e_max_iso = params["isotropy_max_energy"]
    max_rel = 0.0
    for i, e in enumerate(energies):
        if e <= e_max_iso:
            vals = [xx[i], yy[i], zz[i]]
            mean_val = sum(vals) / 3.0
            if mean_val != 0:
                rel = max(abs(v - mean_val) / mean_val for v in vals)
                if rel > max_rel:
                    max_rel = rel
    iso_score = 1.0 if max_rel <= params["max_rel_diff_isotropy"] else 0.0

    # anisotropy above min_energy: check if peaks in xx, yy, zz differ > min_diff
    def find_peaks_above(arr, energies, min_e):
        local = []
        n = len(arr)
        for i in range(1, n-1):
            if energies[i] >= min_e and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > 0.5:
                local.append(energies[i])
        return local
    px = find_peaks_above(xx, energies, params["anisotropy_min_energy"])
    py = find_peaks_above(yy, energies, params["anisotropy_min_energy"])
    pz = find_peaks_above(zz, energies, params["anisotropy_min_energy"])
    all_peaks = px + py + pz
    aniso = False
    if len(all_peaks) >= 2:
        max_e = max(all_peaks)
        min_e = min(all_peaks)
        if (max_e - min_e) >= params["anisotropy_min_diff"]:
            aniso = True
    aniso_score = 1.0 if aniso else 0.0

    return 0.6 * peak_score + 0.2 * iso_score + 0.2 * aniso_score


_SCORERS = {
    'band_gap': score_0,
    'pdos_analysis': score_1,
    'dielectric_function': score_2,
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
