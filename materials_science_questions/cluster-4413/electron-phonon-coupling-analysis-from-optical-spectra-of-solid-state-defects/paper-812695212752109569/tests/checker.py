import os
import json
import csv

# === author imports / helpers ===
import csv, math, statistics

def compute_fwhm(data):
    """Compute FWHM of a spectrum (energy, intensity) assuming single peak near 0."""
    data_sorted = sorted(data, key=lambda x: x[0])
    energies = [d[0] for d in data_sorted]
    intensities = [d[1] for d in data_sorted]
    idx0 = min(range(len(energies)), key=lambda i: abs(energies[i]))
    I0 = intensities[idx0]
    half = I0 / 2.0
    # left
    left_idx = idx0
    while left_idx > 0 and intensities[left_idx] > half:
        left_idx -= 1
    if left_idx >= 0 and left_idx < idx0:
        x1, y1 = energies[left_idx], intensities[left_idx]
        x2, y2 = energies[left_idx+1], intensities[left_idx+1]
        if abs(y2 - y1) > 1e-12:
            left_e = x1 + (half - y1) * (x2 - x1) / (y2 - y1)
        else:
            left_e = energies[left_idx]
    else:
        left_e = energies[left_idx]
    # right
    right_idx = idx0
    while right_idx < len(energies)-1 and intensities[right_idx] > half:
        right_idx += 1
    if right_idx > idx0 and right_idx < len(energies):
        x1, y1 = energies[right_idx-1], intensities[right_idx-1]
        x2, y2 = energies[right_idx], intensities[right_idx]
        if abs(y2 - y1) > 1e-12:
            right_e = x1 + (half - y1) * (x2 - x1) / (y2 - y1)
        else:
            right_e = energies[right_idx]
    else:
        right_e = energies[right_idx]
    return right_e - left_e


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


# === block: score_0 (check id='gq_vs_energy_check') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    try:
        rows = []
        for row in artifact:
            e = float(row['phonon_energy_meV'])
            g = float(row['g'])
            rows.append((e, g))
        rows.sort(key=lambda x: x[0])
        energies = [r[0] for r in rows]
        gs = [r[1] for r in rows]
        if energies[0] > 0.01 or energies[-1] < 3.99:
            return 0.0
        max_g = max(gs)
        if max_g <= 0:
            return 0.0
        idx_max = gs.index(max_g)
        e_peak = energies[idx_max]
        total_integral = 0.0
        tail_integral = 0.0
        for i in range(1, len(energies)):
            de = energies[i] - energies[i-1]
            avg_g = (gs[i] + gs[i-1]) / 2.0
            contrib = de * avg_g
            total_integral += contrib
            if energies[i-1] >= 2.0:
                tail_integral += contrib
            elif energies[i] >= 2.0:
                frac = (energies[i] - 2.0) / de if de > 0 else 0.0
                tail_integral += frac * contrib
        half = max_g / 2.0
        e_halfmax = None
        for i in range(idx_max, len(energies)-1):
            if gs[i] >= half and gs[i+1] <= half:
                e1, g1 = energies[i], gs[i]
                e2, g2 = energies[i+1], gs[i+1]
                if abs(g2 - g1) > 1e-15:
                    e_halfmax = e1 + (half - g1) * (e2 - e1) / (g2 - g1)
                else:
                    e_halfmax = e1
                break
        g0 = gs[0]
        score = 0.0
        if 0.45 <= e_peak <= 0.85:
            score += 0.3
        if e_halfmax is not None and 0.8 <= e_halfmax <= 1.6:
            score += 0.2
        if total_integral > 0 and (tail_integral / total_integral) < 0.08:
            score += 0.2
        if g0 < 0.001 * max_g:
            score += 0.1
        inc = all(gs[i] >= gs[i-1] for i in range(1, idx_max+1))
        dec = all(gs[i] <= gs[i-1] for i in range(idx_max+1, len(gs)))
        if inc and dec:
            score += 0.2
        return min(score, 1.0)
    except Exception:
        return 0.0


# === block: score_1 (check id='line_shapes_check') ===
def score_1(artifact, step, ctx):
    import math

    if not artifact:
        return 0.0
    groups = {}
    required_temps = [5, 30, 50]
    for row in artifact:
        try:
            T = int(row['temperature_K'])
            e = float(row['energy_offset_meV'])
            I = float(row['intensity'])
            groups.setdefault(T, []).append((e, I))
        except:
            pass
    if set(required_temps) != set(groups.keys()):
        return 0.0
    subscore = 0.0
    for T in required_temps:
        data = groups[T]
        # compute peak intensity
        data_sorted = sorted(data, key=lambda x: x[0])
        energies = [d[0] for d in data_sorted]
        intensities = [d[1] for d in data_sorted]
        idx0 = min(range(len(energies)), key=lambda i: abs(energies[i]))
        I0 = intensities[idx0]
        if I0 < 0.9:
            continue
        fwhm = compute_fwhm(data)
        target = 0.180 + 0.0015 * T
        if abs(fwhm - target) <= 0.03:
            subscore += 0.5/3.0
        # sideband check
        if T in (30, 50):
            max_side = max((intensities[i] for i in range(len(energies)) if 0.5 <= abs(energies[i]) <= 2.0), default=0)
            if max_side > 0.03:
                subscore += 0.25/2.0
        if T == 5:
            max_side = max((intensities[i] for i in range(len(energies)) if 0.5 <= abs(energies[i]) <= 2.0), default=0)
            if max_side > 0.005:
                subscore += 0.25/3.0
    # broadening trend
    fwhm_5 = compute_fwhm(groups.get(5))
    fwhm_30 = compute_fwhm(groups.get(30))
    fwhm_50 = compute_fwhm(groups.get(50))
    if fwhm_5 and fwhm_30 and fwhm_50 and (fwhm_5 < fwhm_30 < fwhm_50):
        subscore += 0.1
    return min(subscore, 1.0)


_SCORERS = {
    'gq_vs_energy_check': score_0,
    'line_shapes_check': score_1,
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
