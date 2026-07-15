import os
import json
import csv

# === author imports / helpers ===
import json, os, math
from collections import defaultdict


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
    def prepare(outputs_dir, spec):
        gp_path = os.path.join(outputs_dir, 'step_02_grand_potentials.json')
        stable = {}
        try:
            with open(gp_path) as f:
                gp_data = json.load(f)
        except:
            gp_data = None
        if gp_data is None:
            return {'stable': None}
        phases = ['Dis', 'Lam', 'Hex', 'Hex_II']
        for key, val in gp_data.items():
            try:
                s = key.strip('()')
                parts = s.split(',')
                phi = float(parts[0].strip())
                chiN = float(parts[1].strip())
            except:
                continue
            if not isinstance(val, dict):
                continue
            best_phase = None
            best_val = None
            for p in phases:
                v = val.get(p)
                if v is None:
                    continue
                if best_val is None or v < best_val:
                    best_val = v
                    best_phase = p
                elif v == best_val:
                    if best_phase == 'Dis' and p != 'Dis':
                        best_phase = p
            if best_phase:
                stable[(phi, chiN)] = best_phase
        return {'stable': stable}


# === block: score_0 (check id='step_01_stable_phases') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        stable = ctx.get('stable')
        if stable is None:
            return 0.0
        if not isinstance(artifact, list):
            return 0.0
        total = 0
        match = 0
        for row in artifact:
            if not isinstance(row, dict):
                continue
            phi_raw = row.get('phi_A_tot')
            chiN_raw = row.get('chiN')
            phase_raw = row.get('phase')
            if phi_raw is None or chiN_raw is None or phase_raw is None:
                continue
            try:
                phi = float(phi_raw)
                chiN = float(chiN_raw)
                phase = str(phase_raw).strip()
            except (ValueError, TypeError):
                continue
            key = (phi, chiN)
            expected = stable.get(key)
            if expected is not None and phase == expected:
                match += 1
            total += 1
        if total == 0:
            return 0.0
        return match / total


# === block: score_1 (check id='step_02_grand_potentials') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        stable = ctx.get('stable')
        if stable is None:
            return 0.0
        params = step.get('params', {})
        if not params:
            return 0.0

        # Build melting curve: for each phi, max chiN with phase != Dis
        phi_to_data = {}
        for (phi, chiN), phase in stable.items():
            if phi not in phi_to_data:
                phi_to_data[phi] = []
            phi_to_data[phi].append((chiN, phase))
        melting = {}
        for phi, arr in phi_to_data.items():
            ordered = [(chiN, p) for chiN, p in arr if p != 'Dis']
            if ordered:
                melting[phi] = max(chiN for chiN, p in ordered)
        if not melting:
            return 0.0
        phis = sorted(melting.keys())
        chi_values = [melting[p] for p in phis]

        # Detect local maxima (peaks)
        peaks = []
        for i in range(1, len(phis)-1):
            if chi_values[i] > chi_values[i-1] and chi_values[i] > chi_values[i+1]:
                peaks.append((phis[i], chi_values[i]))
        peak_count = len(peaks)

        # Eutectic: global minimum of melting curve
        min_idx = min(range(len(chi_values)), key=lambda i: chi_values[i])
        eutectic_phi = phis[min_idx]
        eutectic_chiN = chi_values[min_idx]

        scores = []

        # 1. Peak count (at least 2)
        if peak_count >= 2:
            s1 = 1.0
        elif peak_count == 1:
            s1 = 0.5
        else:
            s1 = 0.0
        scores.append(s1)

        # 2. Eutectic phi in range
        phi_range = params.get('eutectic_phi_range', [0.45, 0.55])
        if phi_range[0] <= eutectic_phi <= phi_range[1]:
            s2 = 1.0
        else:
            dist = min(abs(eutectic_phi - phi_range[0]), abs(eutectic_phi - phi_range[1]))
            s2 = max(0.0, 1.0 - dist / 0.1)
        scores.append(s2)

        # 3. Lobe peaks in expected position ranges
        low_range = params.get('low_lobe_peak_phi_range', [0.25, 0.40])
        high_range = params.get('high_lobe_peak_phi_range', [0.60, 0.75])
        if peak_count >= 2:
            sorted_peaks = sorted(peaks, key=lambda x: x[0])
            low_peak = sorted_peaks[0][0]
            high_peak = sorted_peaks[-1][0]
            def in_range(phi, rng):
                if rng[0] <= phi <= rng[1]:
                    return 1.0
                dist = min(abs(phi - rng[0]), abs(phi - rng[1]))
                return max(0.0, 1.0 - dist / 0.1)
            s3 = (in_range(low_peak, low_range) + in_range(high_peak, high_range)) / 2.0
        else:
            s3 = 0.3 if peak_count == 1 else 0.0
        scores.append(s3)

        # 4. Dominant phases in lobes (low lobe: Hex_II, high lobe: Lam/Hex)
        low_dominant = params.get('dominant_low_phase', 'Hex_II')
        high_dominants = params.get('dominant_high_phases', ['Lam', 'Hex'])
        low_total = 0
        low_match = 0
        high_total = 0
        high_match = 0
        for (phi, chiN), phase in stable.items():
            if 0.15 <= phi <= 0.35 and phase != 'Dis':
                low_total += 1
                if phase == low_dominant:
                    low_match += 1
            if 0.60 <= phi <= 0.85 and phase != 'Dis':
                high_total += 1
                if phase in high_dominants:
                    high_match += 1
        s4a = low_match / low_total if low_total > 0 else 0.0
        s4b = high_match / high_total if high_total > 0 else 0.0
        scores.append((s4a + s4b) / 2.0)

        # 5. Specific phase checks at given (phi, chiN)
        specific = params.get('specific_phase_checks', [])
        s5_sub = []
        for check in specific:
            target_phi = check.get('phi')
            target_chiN = check.get('chiN')
            expected_phase = check.get('phase')
            tol_phi = check.get('tolerance_phi', 0.05)
            tol_chiN = check.get('tolerance_chiN', 1.0)
            matching = []
            for (phi, chiN), phase in stable.items():
                if abs(phi - target_phi) <= tol_phi and abs(chiN - target_chiN) <= tol_chiN:
                    matching.append(phase)
            if matching:
                correct = sum(1 for p in matching if p == expected_phase)
                s5_sub.append(correct / len(matching))
            else:
                s5_sub.append(1.0)
        s5 = sum(s5_sub) / len(s5_sub) if s5_sub else 1.0
        scores.append(s5)

        final_score = sum(scores) / len(scores)
        return final_score


_SCORERS = {
    'step_01_stable_phases': score_0,
    'step_02_grand_potentials': score_1,
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
