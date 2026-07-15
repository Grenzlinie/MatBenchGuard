import os
import json
import csv

# === author imports / helpers ===
import math
import json


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
    phases = spec['steps'][0]['reference_data']['phases']
    return {'ref_phases': phases}


# === block: score_0 (check id='step_mechanical') ===
def score_0(artifact, step, ctx):
        ref_phases = ctx['ref_phases']
        if not isinstance(artifact, list):
            return 0.0
        agent_dict = {item['phase']: item for item in artifact}
        phase_scores = []
        for ref in ref_phases:
            name = ref['phase']
            if name not in agent_dict:
                phase_scores.append(0.0)
                continue
            a = agent_dict[name]
            b_ref, g_ref, e_ref = ref['B'], ref['G'], ref['E']
            b = a.get('bulk_modulus_GPa', 0)
            g = a.get('shear_modulus_GPa', 0)
            e = a.get('young_modulus_GPa', 0)
            def rel_err(val, target, tol_frac):
                if target == 0:
                    return 0.0
                err = abs(val - target) / target
                if err <= tol_frac:
                    return 1.0
                return max(0.0, 1.0 - (err - tol_frac) / tol_frac)
            score_b = rel_err(b, b_ref, 0.05)
            score_g = rel_err(g, g_ref, 0.05)
            score_e = rel_err(e, e_ref, 0.05)
            hv_ref = ref['Hv']
            hv = a.get('hardness_GPa', 0)
            err_hv = abs(hv - hv_ref)
            if err_hv <= 2.0:
                score_hv = 1.0
            else:
                score_hv = max(0.0, 1.0 - (err_hv - 2.0) / 2.0)
            phonon = a.get('phonon_stable', False)
            score_phonon = 1.0 if phonon else 0.0
            active_checks = [score_b, score_g, score_e, score_hv, score_phonon]
            if name == "P-62m-HfO":
                n_elec = a.get('carrier_density_electrons_cm3', None)
                n_hole = a.get('carrier_density_holes_cm3', None)
                def factor2_score(val, target):
                    if val is None or val <= 0 or target <= 0:
                        return 0.0
                    ratio = val / target
                    if ratio < 1:
                        ratio = 1.0 / ratio
                    log2 = math.log2(ratio)
                    if log2 <= 1.0:
                        return 1.0
                    return max(0.0, 1.0 - (log2 - 1.0))
                s_elec = factor2_score(n_elec, 1.1e20)
                s_hole = factor2_score(n_hole, 1.1e20)
                active_checks.extend([s_elec, s_hole])
            if b > 0 and g > 0:
                k = g / b
                hv_recomp = 2.0 * (k**2 * g)**0.585 - 3.0
                diff = abs(hv - hv_recomp)
                if diff <= 0.5:
                    score_consist = 1.0
                else:
                    score_consist = max(0.0, 1.0 - (diff - 0.5) / 0.5)
                active_checks.append(score_consist)
            phase_score = sum(active_checks) / len(active_checks)
            phase_scores.append(phase_score)
        return sum(phase_scores) / len(phase_scores)


# === block: score_1 (check id='step_band') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, str):
            return 0.0
        lines = artifact.strip().split('\n')
        if len(lines) < 10:
            return 0.0
        bands = {}
        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            try:
                k_idx = int(parts[0])
                b_idx = int(parts[1])
                energy = float(parts[2])
            except:
                continue
            bands.setdefault(b_idx, []).append(energy)
        if not bands:
            return 0.0
        crossing_bands = []
        for bidx, energies in bands.items():
            mn = min(energies)
            mx = max(energies)
            if mn < -0.01 and mx > 0.01:
                crossing_bands.append((mn, mx))
        n_cross = len(crossing_bands)
        if n_cross == 0:
            score_cross = 0.0
        elif n_cross <= 3:
            score_cross = 1.0
        else:
            score_cross = max(0.0, 1.0 - (n_cross - 3) * 0.3)
        all_vals = [abs(e) for energies in bands.values() for e in energies]
        max_abs = max(all_vals) if all_vals else 0
        if max_abs < 5:
            score_mag = 1.0
        else:
            score_mag = max(0.0, 1.0 - (max_abs - 5) / 10)
        score_rows = min(1.0, len(lines) / 20)
        return 0.3 * score_rows + 0.4 * score_cross + 0.3 * score_mag


_SCORERS = {
    'step_mechanical': score_0,
    'step_band': score_1,
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
