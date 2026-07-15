import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='step_01_monotonic_hysteresis') ===
def score_0(artifact, step, ctx):
    strain = np.array([float(r['strain']) for r in artifact])
    stress = np.array([float(r['stress_MPa']) for r in artifact])
    if len(strain) < 4:
        return 0.0

    # split loading/unloading by peak strain
    peak_idx = np.argmax(strain)
    load_strain = strain[:peak_idx+1]
    load_stress = stress[:peak_idx+1]
    unload_strain = strain[peak_idx:]
    unload_stress = stress[peak_idx:]

    # monotonicity and hysteresis guards
    if np.any(np.diff(load_strain) < -1e-8) or np.any(np.diff(load_stress) < -1e-3):
        return 0.0
    if np.any(np.diff(unload_strain) > 1e-8) or np.any(np.diff(unload_stress) > 1e-3):
        return 0.0
    area = np.trapz(stress, strain)
    if area <= 0:
        return 0.0

    # hidden reference points from the paper's Figure 3 (Case II, 20 °C)
    # strain, stress_MPa, branch ('load' or 'unload')
    ref_points = [
        (0.02, 320.0, 'load'),
        (0.04, 430.0, 'load'),
        (0.06, 460.0, 'load'),
        (0.08, 540.0, 'load'),
        (0.06, 150.0, 'unload'),
        (0.04, 100.0, 'unload'),
        (0.02, 30.0, 'unload'),
    ]

    def within_tolerance(agent_val, ref_val):
        rel_tol = 0.20
        abs_tol = 30.0   # MPa
        return abs(agent_val - ref_val) <= max(rel_tol * abs(ref_val), abs_tol)

    ok = 0
    for ref_strain, ref_stress, branch in ref_points:
        if branch == 'load':
            if ref_strain < load_strain[0] or ref_strain > load_strain[-1]:
                return 0.0
            agent_stress = np.interp(ref_strain, load_strain, load_stress)
        else:  # 'unload'
            if ref_strain < unload_strain[-1] or ref_strain > unload_strain[0]:
                return 0.0
            agent_stress = np.interp(ref_strain, unload_strain, unload_stress)
        if within_tolerance(agent_stress, ref_stress):
            ok += 1

    # also check that the final stress at zero strain indicates residual martensite
    final_stress = stress[-1]
    if final_stress > 0 and final_stress < 100:
        ok += 1

    return float(ok) / float(len(ref_points) + 1)


# === block: score_1 (check id='step_01_residual_stress') ===
def score_1(artifact, step, ctx):
    strain_vals = [float(r['strain']) for r in artifact]
    if not strain_vals:
        return 0.0
    if abs(strain_vals[-1]) < 1e-6:
        final_stress = float(artifact[-1]['stress_MPa'])
        # The paper's pseudoelastic response at 20 °C returns to zero stress (Fig. 3)
        if abs(final_stress) <= 5.0:
            return 1.0
    return 0.0


# === block: score_2 (check id='step_01_xi_bounds') ===
def score_2(artifact, step, ctx):
    strain = np.array([float(r['strain']) for r in artifact])
    xi_S = np.array([float(r['xi_S']) for r in artifact])
    xi_T = np.array([float(r['xi_T']) for r in artifact])
    if len(strain) < 2:
        return 0.0

    # basic bounds
    if np.any((xi_S < 0.0) | (xi_S > 1.0)) or np.any((xi_T < 0.0) | (xi_T > 1.0)):
        return 0.0

    # At 20 °C, the NiTi wire is pseudoelastic: stress-induced martensite forms during loading
    # and reverts on unloading. Check that xi_S reaches a threshold at peak strain and
    # returns to a low value at zero, consistent with the transformation described in the paper.
    idx_peak = np.argmax(strain)
    xi_S_peak = xi_S[idx_peak]
    xi_S_final = xi_S[-1] if abs(strain[-1]) < 1e-6 else 0.0

    # Also xi_T should remain negligible (temperature-induced martensite not active)
    xi_T_ok = np.all(xi_T <= 0.001)

    score_parts = 0
    n_parts = 0

    # Peak xi_S > 0.8 (sufficient forward transformation)
    if xi_S_peak > 0.8:
        score_parts += 1.0
    n_parts += 1

    # Final xi_S < 0.1 (reverse transformation complete)
    if abs(strain[-1]) < 1e-6 and xi_S_final < 0.1:
        score_parts += 1.0
    n_parts += 1

    # xi_T flat
    if xi_T_ok:
        score_parts += 1.0
    n_parts += 1

    return score_parts / n_parts if n_parts > 0 else 0.0


# === block: score_3 (check id='step_01_N_norm') ===
def score_3(artifact, step, ctx):
    strain = np.array([float(r['strain']) for r in artifact])
    N_norm = np.array([float(r['N_norm']) for r in artifact])
    xi_S = np.array([float(r['xi_S']) for r in artifact])

    if len(strain) < 2:
        return 0.0

    # Non-negativity (basic)
    if np.any(N_norm < 0.0):
        return 0.0

    # Split loading / unloading
    peak_idx = np.argmax(strain)
    load_n = N_norm[:peak_idx+1]
    unload_n = N_norm[peak_idx:]
    load_strain = strain[:peak_idx+1]
    unload_strain = strain[peak_idx:]

    # 1. N_norm must be zero when strain is effectively zero (initial and final)
    zero_tol = 1e-6
    if abs(load_strain[0]) < zero_tol and abs(load_n[0]) > 0.01:
        return 0.0
    if abs(unload_strain[-1]) < zero_tol and abs(unload_n[-1]) > 0.01:
        return 0.0

    # 2. N_norm should be monotonic during loading and unloading
    if np.any(np.diff(load_n) < -1e-6) or np.any(np.diff(unload_n) > 1e-6):
        return 0.0

    # 3. At peak strain, N_norm must exceed a minimum threshold to confirm transformation
    if N_norm[peak_idx] <= 0.5:
        return 0.0

    # All structural conditions met
    return 1.0


_SCORERS = {
    'step_01_monotonic_hysteresis': score_0,
    'step_01_residual_stress': score_1,
    'step_01_xi_bounds': score_2,
    'step_01_N_norm': score_3,
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
