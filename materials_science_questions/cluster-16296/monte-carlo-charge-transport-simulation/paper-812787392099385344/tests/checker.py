import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    step = spec['steps'][0]
    ctx = {
        'gold_drift': float(step['gold_drift_velocity_cm_s']),
        'tol_drift': float(step['tolerance_relative_drift']),
        'sign_pattern': step['sign_pattern']
    }
    return ctx


# === block: score_0 (check id='conductivity_eval') ===
def score_0(artifact, step, ctx):
    output_dir = '/app/outputs'
    phase_path = os.path.join(output_dir, 'phase_counts.npz')
    if not os.path.exists(phase_path):
        return 0.0
    data = np.load(phase_path, allow_pickle=False)

    e = 1.602176634e-19
    m0 = 9.10938356e-31
    m_star = 0.2 * m0
    F0 = 300000.0  # 3 kV/cm in V/m
    F_ac = 0.1 * F0
    n_e = 1e15 * 1e6  # convert cm^-3 to m^-3
    two_pi = 2.0 * np.pi

    freqs = [0.2, 0.5, 1.0]

    # --- recompute drift velocity (steady-state) from all data combined ---
    total_N = 0.0
    total_P = 0.0
    for f in freqs:
        key_N = f'N_{f:.1f}'
        key_P = f'P_{f:.1f}'
        if key_N not in data or key_P not in data:
            return 0.0
        N = data[key_N].astype(np.float64)
        P = data[key_P].astype(np.float64)
        total_N += N.sum()
        total_P += (P * N).sum()
    if total_N == 0:
        return 0.0
    P_z_avg = total_P / total_N
    V_dr_m_s = -P_z_avg / m_star
    V_dr_cm_s = V_dr_m_s * 100.0

    gold_v = ctx['gold_drift']
    tol_rel = ctx['tol_drift']
    drift_score = 1.0 if abs(V_dr_cm_s - gold_v) / gold_v <= tol_rel else 0.0

    # --- recompute conductivity and check sign pattern, and collect values ---
    sign_ok = 0
    recomputed = {}  # freq -> {Re, Im}
    for f in freqs:
        key_N = f'N_{f:.1f}'
        key_P = f'P_{f:.1f}'
        N = data[key_N].astype(np.float64)
        P = data[key_P].astype(np.float64)
        total = N.sum()
        if total == 0:
            continue
        # infer mesh dimensions from shape: N has shape (M_P, M_T, M_Z)
        M_T = N.shape[1]
        M_Z = N.shape[2]
        vp_ax = np.arange(P.shape[0])
        vt_ax = np.arange(M_T)
        vz_ax = np.arange(M_Z)
        vp, vt, vz = np.meshgrid(vp_ax, vt_ax, vz_ax, indexing='ij')
        # phi = qz - wt; with z = (vz)/M_Z * Lambda, t = (vt)/M_T * T
        # (using the paper's convention without 0.5 offset)
        phi = two_pi * (vz / M_Z - vt / M_T)
        W = N / total
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)
        Re_j = -2.0 * e / m_star * n_e * np.sum(P * W * cos_phi)
        Im_j = -2.0 * e / m_star * n_e * np.sum(P * W * sin_phi)
        sigma_factor = 1.0 / F_ac
        Re_sigma_SI = Re_j * sigma_factor  # S/m
        Im_sigma_SI = -Im_j * sigma_factor  # S/m
        # convert to cm^2/(V·s) per electron
        Re_cm2 = (Re_sigma_SI / (e * n_e)) * 1e4
        Im_cm2 = (Im_sigma_SI / (e * n_e)) * 1e4
        recomputed[f'{f:.1f}'] = (Re_cm2, Im_cm2)
        expected = ctx['sign_pattern'].get(f'{f:.1f}', {})
        exp_sign = expected.get('Re_sign', 0)
        if exp_sign == -1 and Re_cm2 < -1e-8:
            sign_ok += 1
        elif exp_sign == 1 and Re_cm2 > 1e-8:
            sign_ok += 1
    sign_score = sign_ok / len(freqs) if freqs else 0.0

    # --- self-consistency with agent CSV ---
    agent_dict = {}
    if isinstance(artifact, list):
        for row in artifact:
            try:
                freq = f"{float(row['freq_THz']):.1f}"
                agent_dict[freq] = (float(row['Re_sigma_per_e']), float(row['Im_sigma_per_e']))
            except (ValueError, KeyError):
                pass
    if len(agent_dict) == 0:
        self_score = 0.0
    else:
        matched = 0
        for freq, (re_val, im_val) in recomputed.items():
            if freq in agent_dict:
                a_re, a_im = agent_dict[freq]
                if max(abs(re_val), 1e-12) > 0:
                    rel_re = abs(a_re - re_val) / max(abs(re_val), 1e-12)
                else:
                    rel_re = abs(a_re - re_val)
                if max(abs(im_val), 1e-12) > 0:
                    rel_im = abs(a_im - im_val) / max(abs(im_val), 1e-12)
                else:
                    rel_im = abs(a_im - im_val)
                if rel_re <= 1e-4 and rel_im <= 1e-4:
                    matched += 1
        self_score = matched / len(recomputed) if recomputed else 0.0

    # Combine sub-scores: drift 0.4, sign 0.4, self 0.2
    final_score = 0.4 * drift_score + 0.4 * sign_score + 0.2 * self_score
    return max(0.0, min(1.0, final_score))


_SCORERS = {
    'conductivity_eval': score_0,
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
