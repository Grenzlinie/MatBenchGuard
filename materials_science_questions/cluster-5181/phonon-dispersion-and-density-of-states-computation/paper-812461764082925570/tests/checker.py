import os
import json
import csv

# === author imports / helpers ===
import json, numpy as np
la = np.linalg


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
        a0 = 5.653 / 4.0          # monolayer separation in Å
        eps_inf = 12.0
        Omega = 362.0             # cm⁻¹
        eta_z, eta_x = 22.0, 22.0
        chi_z, chi_x = 1.36, 1.08
        R_z, R_x = 4, 2
        # calibrated sqrt(Delta) from paper's Fig.1 (highest Gamma1 mode ~384 cm⁻¹)
        B0 = 133.2   # cm⁻¹
        eta_sp = 1.7 * a0
        d_z = 22 * a0            # effective width for z modes
        d_x = 20 * a0            # for x modes
        n_super = 20
        s_inds = [1,3,5,7,9]     # even s modes (5)
        g_ind = 1                # most energetic g mode
        dim = len(s_inds) + 1

        def kappa(k, d):
            return np.pi * k / (2.0 * d)
        def Omega_z(k, d):
            kp = kappa(k, d)
            return Omega - eta_z * (1 - np.exp(-(kp/chi_z)**R_z))
        def Omega_x(k, d):
            kp = kappa(k, d)
            return Omega - eta_x * (1 - np.exp(-(kp/chi_x)**R_x))
        def B_k(k, d):
            arg = np.pi * k * eta_sp / d
            return B0 * d * np.sin(arg) / (np.pi * k * eta_sp)

        B_s = {k: B_k(k, d_z) for k in s_inds}
        B_g = B_k(g_ind, d_x)

        angles = np.arange(0, 91, 1)
        ref_freqs = []
        for th in angles:
            theta = np.deg2rad(th)
            qx, qz = np.sin(theta), np.cos(theta)
            qx2 = qx**2
            M = np.zeros((dim, dim), dtype=float)
            # build s block
            for i, k in enumerate(s_inds):
                h_ss = 8.0 * B_s[k]**2 / (np.pi**2 * k * k)
                M[i,i] = Omega_z(k, d_z)**2 + B_s[k]**2 - h_ss * qx2
                for j, kp in enumerate(s_inds):
                    if i != j:
                        h = 8.0 * B_s[k] * B_s[kp] / (np.pi**2 * k * kp)
                        M[i,j] = -h * qx2
            # g block
            g_idx = len(s_inds)
            kg = g_ind
            h_gg = 8.0 * B_g**2 / (np.pi**2 * kg * kg)
            M[g_idx, g_idx] = Omega_x(kg, d_x)**2 + h_gg * qx2
            # s-g coupling
            for i, k in enumerate(s_inds):
                h_gs = 8.0 * B_s[k] * B_g / (np.pi**2 * k * kg)
                M[i, g_idx] = h_gs * qx * qz
                M[g_idx, i] = h_gs * qx * qz
            eigvals = la.eigh(M)[0]
            freqs = np.sqrt(np.maximum(eigvals, 0.0))
            for mode_i, freq in enumerate(np.sort(freqs)):
                ref_freqs.append({'theta_deg': float(th), 'mode_index': mode_i, 'frequency_cm-1': float(freq)})
        return {'ref_freqs': ref_freqs}


# === block: score_0 (check id='check_frequencies') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref_freqs = ctx.get('ref_freqs', [])
        agent_freqs = artifact.get('frequencies', [])
        if not agent_freqs:
            return 0.0
        agent_by_theta = {}
        for entry in agent_freqs:
            try:
                th = round(float(entry.get('theta_deg', -1)))
            except Exception:
                continue
            if th < 0 or th > 90:
                continue
            freq_val = entry.get('frequency_cm-1')
            if freq_val is None:
                continue
            try:
                f = float(freq_val)
            except Exception:
                continue
            if not np.isfinite(f):
                continue
            agent_by_theta.setdefault(th, []).append(f)
        ref_by_theta = {}
        for entry in ref_freqs:
            th = int(entry.get('theta_deg', -1))
            if th < 0 or th > 90:
                continue
            freq_val = entry.get('frequency_cm-1')
            if freq_val is None:
                continue
            try:
                f = float(freq_val)
            except Exception:
                continue
            if not np.isfinite(f):
                continue
            ref_by_theta.setdefault(th, []).append(f)
        common_angles = sorted(set(agent_by_theta.keys()) & set(ref_by_theta.keys()))
        if not common_angles:
            return 0.0
        errors = []
        for th in common_angles:
            agent_f = sorted(agent_by_theta[th])
            ref_f = sorted(ref_by_theta[th])
            min_len = min(len(agent_f), len(ref_f))
            if min_len == 0:
                continue
            diff = np.array(agent_f[:min_len]) - np.array(ref_f[:min_len])
            errors.extend(diff.tolist())
        if not errors:
            return 0.0
        rmsd = np.sqrt(np.mean(np.array(errors)**2))
        tol = float(step.get('target', 2.0))
        decay = float(step.get('tolerance_decay', 10.0))
        if rmsd <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (rmsd - tol) / (decay - tol))


# === block: score_1 (check id='check_fields_structure') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        fields = artifact.get('fields', [])
        if not isinstance(fields, list) or len(fields) == 0:
            return 0.0
        score = 0.0
        # required size: expect approx 10 modes * 40 monolayers * 2 thetas = 800 entries
        n_entries = len(fields)
        if n_entries >= 400:
            score += 0.3
        elif n_entries >= 200:
            score += 0.15
        # check fields are finite and physical
        ez_valid = True
        ex_valid = True
        for entry in fields:
            ez = entry.get('Ez_meV_per_A', None)
            ex = entry.get('Ex_meV_per_A', None)
            if ez is None or not np.isfinite(ez):
                ez_valid = False
            if ex is None or not np.isfinite(ex):
                ex_valid = False
        if ez_valid:
            score += 0.3
        if ex_valid:
            score += 0.3
        # check that modes are labelled and z_monolayer within 0..39
        mode_set = set()
        z_set = set()
        for entry in fields:
            mi = entry.get('mode_index')
            z = entry.get('z_monolayer')
            if isinstance(mi, int) and isinstance(z, int):
                mode_set.add(mi)
                z_set.add(z)
        if len(mode_set) >= 6:
            score += 0.05
        if len(z_set) >= 30:
            score += 0.05
        # cap at 1.0
        return min(score, 1.0)


_SCORERS = {
    'check_frequencies': score_0,
    'check_fields_structure': score_1,
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
