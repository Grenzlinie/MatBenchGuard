import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    gold = {
        ("Ih", "Ag147"): {"freq": 3.97, "fwhm": 1.53},
        ("Ih", "Ag309"): {"freq": 3.92, "fwhm": 1.36},
        ("Ih", "Ag561"): {"freq": 3.87, "fwhm": 1.26},
        ("Ih", "Ag923"): {"freq": 3.83, "fwhm": 1.40},
        ("Ih", "Ag1415"): {"freq": 3.80, "fwhm": 1.51},
        ("Ih", "Ag2057"): {"freq": 3.79, "fwhm": 1.48},
        ("Ih", "Ag2869"): {"freq": 3.78, "fwhm": 1.46},
        ("Ih", "Ag3871"): {"freq": 3.77, "fwhm": 1.44},
        ("i-Dh", "Ag85"): {"freq": 3.93, "fwhm": 1.60},
        ("i-Dh", "Ag207"): {"freq": 3.85, "fwhm": 1.52},
        ("i-Dh", "Ag409"): {"freq": 3.75, "fwhm": 1.44},
        ("i-Dh", "Ag711"): {"freq": 3.65, "fwhm": 1.37},
        ("i-Dh", "Ag1133"): {"freq": 3.55, "fwhm": 1.32},
        ("i-Dh", "Ag1695"): {"freq": 3.48, "fwhm": 1.28},
        ("i-Dh", "Ag2417"): {"freq": 3.43, "fwhm": 1.24},
        ("i-Dh", "Ag3319"): {"freq": 3.40, "fwhm": 1.21},
        ("m-Dh", "Ag75"): {"freq": 4.02, "fwhm": 1.58},
        ("m-Dh", "Ag192"): {"freq": 3.95, "fwhm": 1.48},
        ("m-Dh", "Ag389"): {"freq": 3.88, "fwhm": 1.39},
        ("m-Dh", "Ag686"): {"freq": 3.78, "fwhm": 1.31},
        ("m-Dh", "Ag1103"): {"freq": 3.68, "fwhm": 1.25},
        ("m-Dh", "Ag1660"): {"freq": 3.60, "fwhm": 1.20},
        ("m-Dh", "Ag2377"): {"freq": 3.53, "fwhm": 1.16},
        ("m-Dh", "Ag3274"): {"freq": 3.48, "fwhm": 1.13},
        ("TO", "Ag201"): {"freq": 3.55, "fwhm": 1.65},
        ("TO", "Ag586"): {"freq": 3.62, "fwhm": 1.55},
        ("TO", "Ag1289"): {"freq": 3.70, "fwhm": 1.48},
        ("TO", "Ag2406"): {"freq": 3.76, "fwhm": 1.50},
        ("TO", "Ag4033"): {"freq": 3.79, "fwhm": 1.52},
        ("c-TO", "Ag147"): {"freq": 4.15, "fwhm": 1.60},
        ("c-TO", "Ag309"): {"freq": 4.05, "fwhm": 1.50},
        ("c-TO", "Ag561"): {"freq": 3.95, "fwhm": 1.45},
        ("c-TO", "Ag923"): {"freq": 3.85, "fwhm": 1.42},
        ("c-TO", "Ag1415"): {"freq": 3.78, "fwhm": 1.48},
        ("c-TO", "Ag2057"): {"freq": 3.74, "fwhm": 1.52},
        ("c-TO", "Ag2869"): {"freq": 3.72, "fwhm": 1.58},
        ("c-TO", "Ag3871"): {"freq": 3.71, "fwhm": 1.62}
    }
    return {"gold": gold}


# === block: score_0 (check id='spectra_audit') ===
def score_0(artifact, step, ctx):
    spectra_path = os.path.join("/app/outputs", "absorption_spectra.csv")
    if not os.path.exists(spectra_path):
        return 0.0
    with open(spectra_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    groups = {}
    for r in rows:
        key = (r['motif'].strip(), r['cluster_label'].strip())
        energy = float(r['energy_eV'])
        sigma = float(r['sigma_per_atom'])
        groups.setdefault(key, []).append((energy, sigma))
    valid = 0
    total = len(groups)
    if total == 0:
        return 0.0
    for key, pts in groups.items():
        if not pts:
            continue
        max_sigma = max(abs(p[1]) for p in pts)
        peak_energy = max(pts, key=lambda p: abs(p[1]))[0]
        if 2.4 <= peak_energy <= 4.8 and max_sigma > 0:
            valid += 1
    return valid / total


# === block: score_1 (check id='plasmon_compare') ===
def score_1(artifact, step, ctx):
    spectra_path = os.path.join("/app/outputs", "absorption_spectra.csv")
    if not os.path.exists(spectra_path):
        return 0.0
    with open(spectra_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    gold = ctx.get("gold", {})
    if not gold:
        return 0.0
    # Organize spectra per cluster
    from collections import defaultdict
    spectra = defaultdict(list)
    for r in rows:
        motif = r['motif'].strip()
        clabel = r['cluster_label'].strip()
        energy = float(r['energy_eV'])
        sigma = float(r['sigma_per_atom'])
        spectra[(motif, clabel)].append((energy, sigma))

    # Helper to compute peak and FWHM
    def compute_peak_fwhm(points):
        """points: list of (energy, sigma). Returns (peak_energy, fwhm) or None."""
        if len(points) < 2:
            return None
        # Find max abs sigma
        max_idx = max(range(len(points)), key=lambda i: abs(points[i][1]))
        max_energy, max_val = points[max_idx]
        half_max = max_val / 2.0
        # Find left and right crossings via linear interpolation
        left = None
        right = None
        # sort by energy
        sorted_pts = sorted(points, key=lambda p: p[0])
        energies = [p[0] for p in sorted_pts]
        sigmas = [p[1] for p in sorted_pts]
        # left bound: first energy where sigma >= half_max
        for i in range(1, len(sorted_pts)):
            if sigmas[i-1] <= half_max <= sigmas[i] or sigmas[i-1] >= half_max >= sigmas[i]:
                frac = (half_max - sigmas[i-1]) / (sigmas[i] - sigmas[i-1]) if sigmas[i] != sigmas[i-1] else 0.0
                left = energies[i-1] + frac * (energies[i] - energies[i-1])
                break
        if left is None:
            return (max_energy, 0.0)
        # right bound: from after peak
        for i in range(max_idx+1, len(sorted_pts)):
            if sigmas[i-1] >= half_max >= sigmas[i] or sigmas[i-1] <= half_max <= sigmas[i]:
                frac = (half_max - sigmas[i-1]) / (sigmas[i] - sigmas[i-1]) if sigmas[i] != sigmas[i-1] else 0.0
                right = energies[i-1] + frac * (energies[i] - energies[i-1])
                break
        if right is None:
            right = energies[-1]
        fwhm = abs(right - left)
        return (max_energy, fwhm)

    TOL_FREQ = 0.15
    TOL_FWHM = 0.2
    passed = 0
    total = len(gold)
    if total == 0:
        return 0.0
    for key, vals in gold.items():
        motif, clabel = key
        pts = spectra.get((motif, clabel), [])
        if not pts:
            continue
        ret = compute_peak_fwhm(pts)
        if ret is None:
            continue
        peak_energy, fwhm = ret
        if abs(peak_energy - vals["freq"]) <= TOL_FREQ and abs(fwhm - vals["fwhm"]) <= TOL_FWHM:
            passed += 1
    score = passed / total
    # Bonus: also check that the agent's plasmon_summary.csv exists and matches recomputed within tight tolerance (low impact)
    summary_path = os.path.join("/app/outputs", "plasmon_summary.csv")
    if os.path.exists(summary_path):
        try:
            with open(summary_path, newline='') as f:
                summ_reader = csv.DictReader(f)
                for row in summ_reader:
                    motif_s = row['motif'].strip()
                    clabel_s = row['cluster_label'].strip()
                    freq_s = float(row['plasmon_freq_eV'])
                    fwhm_s = float(row['FWHM_eV'])
                    pts = spectra.get((motif_s, clabel_s), [])
                    if pts:
                        ret2 = compute_peak_fwhm(pts)
                        if ret2 and abs(freq_s - ret2[0]) <= 0.01 and abs(fwhm_s - ret2[1]) <= 0.01:
                            pass  # consistency fine
        except Exception:
            pass
    return min(1.0, score)  # already in [0,1]


_SCORERS = {
    'spectra_audit': score_0,
    'plasmon_compare': score_1,
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
